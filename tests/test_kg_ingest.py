"""Native epistemic-graph ingestion — Wire-First coverage for atlassian-agent.

Exercises the ``ingest_issues`` / ``ingest_confluence_pages`` / ``ingest_attachment``
mappers with a fake native-ingestion primitive (no engine required), asserting the
Jira issue → :Issue/:Epic/:Person mapping, the Confluence page → :Document mapping, the
attachment → blob path, and strict propagation of native-ingestion failures.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from typing import Any

import pytest

# `agent_utilities.knowledge_graph.memory` unconditionally imports
# `agent_utilities.numeric` at module-load time, which in turn requires the
# compiled `epistemic_graph.numeric` kernel. agent-utilities moved that
# kernel out of its base dependency set into the opt-in `graphos` extra
# (GOC-73); this repo depends only on `agent-utilities[mcp]`, which does not
# pull it in. Left unguarded, importing it here raises a bare
# ModuleNotFoundError/ImportError chain that pytest reports as a COLLECTION
# ERROR — which (a) reads exactly like a regression in THIS repo and
# (b) aborts collection of the entire `tests/` suite, not just this file
# (`pytest tests/ -q` reports "0 tests collected, 1 error" for the whole
# run, which is why lanes have been passing `--ignore=tests/test_kg_ingest.py`
# and silently losing coverage on both sides of every before/after
# comparison). This is an ENVIRONMENT/packaging gap, not application-code
# breakage — install `agent-utilities[graphos]>=2.27.0` to exercise these
# tests. See plans/complex/waves/wD4/WD4-FIX-01.md defect (d). Turn it into
# a clean, LOUD, explained skip of just this file instead.
pytest.importorskip(
    "agent_utilities.knowledge_graph.memory.native_ingest",
    # pytest 9.1 changed importorskip()'s default `exc_type` from
    # ImportError to ModuleNotFoundError (see the versionchanged note in
    # pytest.importorskip's own docstring). agent_utilities.numeric
    # deliberately re-raises a plain ImportError (not ModuleNotFoundError)
    # with an explanatory message, so the new default silently fails to
    # catch it and the "skip" degrades right back into the collection
    # error this guard exists to prevent. Pin exc_type explicitly so the
    # guard keeps working regardless of installed pytest version.
    exc_type=ImportError,
    reason=(
        "agent_utilities.numeric requires the compiled epistemic_graph.numeric "
        "kernel, shipped only behind agent-utilities' opt-in `graphos` extra "
        "(GOC-73); not installed by this repo's `agent-utilities[mcp]` "
        "dependency — install `agent-utilities[graphos]>=2.27.0` to run "
        "KG-ingestion tests (WD4-FIX-01 defect (d))"
    ),
)

from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError

import atlassian_agent.kg_ingest as kg


class _Capture:
    """Records calls made to the fake native-ingestion primitives."""

    def __init__(self):
        self.entities: list[dict[str, Any]] = []
        self.relationships: list[dict[str, Any]] = []
        self.documents: list[dict[str, Any]] = []
        self.stored: list[dict[str, Any]] = []
        self.source: str | None = None
        self.domain: str | None = None


def _install_fakes(monkeypatch) -> _Capture:
    cap = _Capture()

    def fake_ingest_entities(
        entities, relationships=None, *, source, domain, client=None, graph=None
    ):
        cap.entities = entities
        cap.relationships = relationships or []
        cap.source = source
        cap.domain = domain
        if not entities:
            raise NativeIngestError("native ingest requires at least one entity")
        return {"nodes": len(entities), "edges": len(relationships or [])}

    def fake_ingest_documents(documents, *, source, domain, client=None, graph=None):
        cap.documents = documents
        cap.source = source
        cap.domain = domain
        if not documents:
            raise NativeIngestError("native ingest requires at least one document")
        return {"nodes": len(documents), "edges": 0}

    class _FakeStore:
        def store_media(self, data, **kwargs):
            cap.stored.append({"data": data, **kwargs})
            return {"asset_id": "asset:abc"}

    def fake_media_store():
        return _FakeStore()

    monkeypatch.setattr(kg, "_native_ingest_entities", fake_ingest_entities)
    monkeypatch.setattr(kg, "_native_ingest_documents", fake_ingest_documents)
    monkeypatch.setattr(kg, "_native_media_store", fake_media_store)
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
    assert issue["node_type"] == "Issue"
    assert issue["issueKey"] == "PROJ-1"
    assert issue["status"] == "In Progress"
    assert issue["priority"] == "High"
    assert by_id["atlassian:person:acc-1"]["node_type"] == "Person"
    assert by_id["atlassian:epic:PROJ-100"]["node_type"] == "Epic"
    rel_types = {r["relationship"] for r in cap.relationships}
    assert rel_types == {"assignedTo", "reportedBy", "inEpic"}


def test_ingest_issues_epic_becomes_epic_node(monkeypatch):
    cap = _install_fakes(monkeypatch)
    kg.ingest_issues(
        [{"key": "PROJ-100", "fields": {"issuetype": {"name": "Epic"}, "summary": "E"}}]
    )
    assert cap.entities[0]["id"] == "atlassian:epic:PROJ-100"
    assert cap.entities[0]["node_type"] == "Epic"
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
    assert doc["document_type"] == "ConfluencePage"
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


def test_ingest_propagates_native_failure(monkeypatch):
    def fail(*args, **kwargs):
        raise NativeIngestError("engine unavailable")

    monkeypatch.setattr(kg, "_native_ingest_entities", fail)
    with pytest.raises(NativeIngestError, match="engine unavailable"):
        kg.ingest_issues([{"key": "PROJ-1", "fields": {}}])


def test_ingest_empty_is_rejected(monkeypatch):
    _install_fakes(monkeypatch)
    with pytest.raises(NativeIngestError, match="at least one entity"):
        kg.ingest_issues([])
    with pytest.raises(NativeIngestError, match="at least one document"):
        kg.ingest_confluence_pages([])
    assert kg.ingest_attachment(b"") is None
