"""Native epistemic-graph ingestion — Wire-First coverage for atlassian-agent.

Exercises the ``ingest_issues`` / ``ingest_confluence_pages`` / ``ingest_attachment``
mappers against the connector SDK's :class:`KnowledgeIngest` over a fake transport
(no engine required), asserting the Jira issue → :Issue/:Epic/:Person mapping, the
Confluence page → :ConfluencePage document mapping, the attachment → blob path, and
strict propagation of ingest failures.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest
from agent_connector_sdk.ingest import IngestError, KnowledgeIngest

import atlassian_agent.kg_ingest as kg


class _FakeTransport:
    def __init__(self):
        self.requests = []
        self.blobs: list[bytes] = []

    async def source_status(self, connector, stream):
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request):
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, data):
        self.blobs.append(data)
        return "sha256:" + "0" * 64


class _FailingTransport(_FakeTransport):
    async def submit(self, request):
        raise RuntimeError("engine unavailable")


@pytest.fixture
def ingest():
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


def _node_type(record) -> str:
    return record.mapping_reference.rsplit("/", 1)[-1]


def _relation(rel) -> str:
    return rel.relation_reference.rsplit("/", 1)[-1]


async def test_ingest_issues_maps_issue_epic_person(ingest):
    service, transport = ingest
    res = await kg.ingest_issues(
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
        ],
        ingest=service,
    )
    assert res == {"nodes": 4, "edges": 3}
    request = transport.requests[0]
    assert request.connector == "atlassian-agent"
    by_id = {r.record_id: r for r in request.records}
    issue = by_id["atlassian:issue:PROJ-1"]
    assert _node_type(issue) == "Issue"
    assert issue.payload["issueKey"] == "PROJ-1"
    assert issue.payload["status"] == "In Progress"
    assert issue.payload["priority"] == "High"
    assert issue.stream == "atlassian"
    assert _node_type(by_id["atlassian:person:acc-1"]) == "Person"
    assert _node_type(by_id["atlassian:epic:PROJ-100"]) == "Epic"
    rel_types = {_relation(r) for r in request.relationships}
    assert rel_types == {"assignedTo", "reportedBy", "inEpic"}


async def test_ingest_issues_epic_becomes_epic_node(ingest):
    service, transport = ingest
    await kg.ingest_issues(
        [
            {
                "key": "PROJ-100",
                "fields": {"issuetype": {"name": "Epic"}, "summary": "E"},
            }
        ],
        ingest=service,
    )
    request = transport.requests[0]
    assert request.records[0].record_id == "atlassian:epic:PROJ-100"
    assert _node_type(request.records[0]) == "Epic"
    assert request.relationships == []


async def test_ingest_confluence_maps_document(ingest):
    service, transport = ingest
    res = await kg.ingest_confluence_pages(
        [
            {
                "id": "555",
                "title": "Runbook",
                "spaceId": "42",
                "status": "current",
                "body": {"storage": {"value": "<p>How to deploy</p>"}},
                "_links": {"webui": "/wiki/pages/555"},
            }
        ],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 0}
    doc = transport.requests[0].records[0]
    assert doc.record_id == "atlassian:page:555"
    assert _node_type(doc) == "ConfluencePage"
    assert doc.payload["text"] == "<p>How to deploy</p>"
    # The page link rides record provenance; the SDK privacy guard sanitizes
    # path-like payload properties, so the payload copy is not asserted.
    assert doc.provenance.source_uri == "/wiki/pages/555"
    assert doc.payload["space_id"] == "42"
    assert doc.stream == "atlassian"


async def test_ingest_attachment_stores_blob(ingest):
    service, transport = ingest
    out = await kg.ingest_attachment(
        b"PDFBYTES",
        name="spec.pdf",
        mime_type="application/pdf",
        issue_key="PROJ-1",
        ingest=service,
    )
    assert out == {"nodes": 1, "edges": 0}
    assert transport.blobs == [b"PDFBYTES"]
    asset = transport.requests[0].records[0]
    assert _node_type(asset) == "MediaAsset"
    assert asset.payload["name"] == "spec.pdf"
    assert asset.payload["mime_type"] == "application/pdf"
    assert asset.payload["issue_key"] == "PROJ-1"


async def test_ingest_propagates_engine_failure():
    service = KnowledgeIngest(_FailingTransport(), loop=None)
    with pytest.raises(IngestError, match="engine unavailable"):
        await kg.ingest_issues([{"key": "PROJ-1", "fields": {}}], ingest=service)


async def test_ingest_empty_is_rejected(ingest):
    service, transport = ingest
    with pytest.raises(IngestError, match="at least one entity"):
        await kg.ingest_issues([], ingest=service)
    with pytest.raises(IngestError, match="at least one document"):
        await kg.ingest_confluence_pages([], ingest=service)
    assert await kg.ingest_attachment(b"", ingest=service) is None
    assert transport.requests == []
