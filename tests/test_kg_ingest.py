"""Native epistemic-graph ingestion — Wire-First coverage for atlassian-agent.

Exercises the ``ingest_issues`` / ``ingest_confluence_pages`` / ``ingest_attachment``
mappers with a fake native-ingestion primitive (no engine required), asserting the
Jira issue → :Issue/:Epic/:Person mapping, the Confluence page → :Document mapping, the
attachment → blob path, and the clean no-op when no KG engine is present.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from typing import Any

import atlassian_agent.kg_ingest as kg


class _Capture:
    """Records calls made to the fake native-ingestion primitives."""

    def __init__(self):
        self.entities: list[dict[str, Any]] = []
        self.relationships: list[dict[str, Any]] = []
        self.documents: list[dict[str, Any]] = []
        self.stored: list[dict[str, Any]] = []


def _install_fakes(monkeypatch) -> _Capture:
    cap = _Capture()

    def fake_ingest_entities(entities, relationships=None, *, source, domain):
        cap.entities = entities
        cap.relationships = relationships or []
        cap.source = source
        cap.domain = domain
        if not entities:  # mirror the real primitive's empty no-op
            return None
        return {"nodes": len(entities), "edges": len(relationships or [])}

    def fake_ingest_documents(documents, *, source, domain):
        cap.documents = documents
        cap.source = source
        cap.domain = domain
        if not documents:  # mirror the real primitive's empty no-op
            return None
        return {"nodes": len(documents), "edges": 0}

    class _FakeStore:
        def store_media(self, data, **kwargs):
            cap.stored.append({"data": data, **kwargs})
            return {"asset_id": "asset:abc"}

    def fake_media_store():
        return _FakeStore()

    monkeypatch.setattr(
        kg,
        "_primitives",
        lambda: (fake_ingest_entities, fake_ingest_documents, fake_media_store),
    )
    return cap


def test_ingest_issues_maps_issue_epic_person(monkeypatch):
    cap = _install_fakes(monkeypatch)
    res = kg.ingest_issues(
        [
            {
                "id": "10001",
                "key": "PROJ-1",
                "fields": {
                    "summary": "Login times out",
                    "status": {"name": "In Progress"},
                    "priority": {"name": "High"},
                    "issuetype": {"name": "Bug"},
                    "assignee": {"accountId": "acc-1", "displayName": "Jane"},
                    "reporter": {"accountId": "acc-2", "displayName": "John"},
                    "parent": {
                        "key": "PROJ-100",
                        "fields": {"issuetype": {"name": "Epic"}},
                    },
                },
            }
        ]
    )
    assert res == {"nodes": 4, "edges": 3}
    assert cap.source == "atlassian-agent"
    assert cap.domain == "atlassian"
    by_id = {e["id"]: e for e in cap.entities}
    issue = by_id["atlassian:issue:PROJ-1"]
    assert issue["type"] == "Issue"
    assert issue["issueKey"] == "PROJ-1"
    assert issue["status"] == "In Progress"
    assert issue["priority"] == "High"
    assert by_id["atlassian:person:acc-1"]["type"] == "Person"
    assert by_id["atlassian:epic:PROJ-100"]["type"] == "Epic"
    rel_types = {r["type"] for r in cap.relationships}
    assert rel_types == {"assignedTo", "reportedBy", "inEpic"}


def test_ingest_issues_epic_becomes_epic_node(monkeypatch):
    cap = _install_fakes(monkeypatch)
    kg.ingest_issues(
        [{"key": "PROJ-100", "fields": {"issuetype": {"name": "Epic"}, "summary": "E"}}]
    )
    assert cap.entities[0]["id"] == "atlassian:epic:PROJ-100"
    assert cap.entities[0]["type"] == "Epic"
    assert cap.relationships == []


def test_ingest_confluence_maps_document(monkeypatch):
    cap = _install_fakes(monkeypatch)
    res = kg.ingest_confluence_pages(
        [
            {
                "id": "555",
                "title": "Runbook",
                "spaceId": "42",
                "status": "current",
                "body": {"storage": {"value": "<p>How to deploy</p>"}},
                "_links": {"webui": "/wiki/pages/555"},
            }
        ]
    )
    assert res == {"nodes": 1, "edges": 0}
    doc = cap.documents[0]
    assert doc["id"] == "atlassian:page:555"
    assert doc["type"] == "ConfluencePage"
    assert doc["text"] == "<p>How to deploy</p>"
    assert doc["source_uri"] == "/wiki/pages/555"
    assert cap.domain == "atlassian"


def test_ingest_attachment_stores_blob(monkeypatch):
    cap = _install_fakes(monkeypatch)
    out = kg.ingest_attachment(
        b"PDFBYTES", name="spec.pdf", mime_type="application/pdf", issue_key="PROJ-1"
    )
    assert out == {"asset_id": "asset:abc"}
    assert cap.stored[0]["data"] == b"PDFBYTES"
    assert cap.stored[0]["name"] == "spec.pdf"
    assert cap.stored[0]["source"] == "atlassian-agent"


def test_ingest_noops_without_engine(monkeypatch):
    monkeypatch.setattr(kg, "_primitives", lambda: None)
    assert kg.ingest_issues([{"key": "PROJ-1", "fields": {}}]) is None
    assert kg.ingest_confluence_pages([{"id": "1", "body": "x"}]) is None
    assert kg.ingest_attachment(b"x", name="a") is None


def test_ingest_empty_is_noop(monkeypatch):
    _install_fakes(monkeypatch)
    assert kg.ingest_issues([]) is None
    assert kg.ingest_confluence_pages([]) is None
    assert kg.ingest_attachment(b"") is None
