"""Native epistemic-graph ingestion for Atlassian records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. The atlassian-agent package natively
pushes its data into the ONE epistemic-graph knowledge graph in every modality that
applies (the "maximum ingestion" bar):

* **Jira issues** → typed OWL nodes ``:Issue`` / ``:Epic`` / ``:Person`` (+ ``:assignedTo``
  / ``:inEpic`` / ``:reportedBy`` links) via :func:`ingest_issues`.
* **Confluence pages** → ``:Document`` (``:ConfluencePage``) nodes carrying the page body
  text + ``source_uri`` for semantic search via :func:`ingest_confluence_pages`.
* **Attachments** → raw ``:Blob`` / ``:MediaAsset`` bytes via :func:`ingest_attachment`.

All three are submitted through the connector SDK's knowledge-ingest service
(:mod:`agent_connector_sdk.ingest`) under this connector's :class:`IngestBinding`, so
this module ships only thin record→dict mappers. Provenance (connector, stream) is
carried by the binding server-side, not stamped onto node properties. Node ids follow
``atlassian:<class>:<externalId>`` and ``node_type`` matches a class the package's
``ontology_providers`` ``atlassian.ttl`` federates.

Every public ingest function is ``async`` and must be awaited; each accepts an
``ingest=`` :class:`KnowledgeIngest` for injection (default: :func:`current_ingest`).
"""

from __future__ import annotations

from typing import Any

from agent_connector_sdk.ingest import (
    ChangeSet,
    Document,
    Entity,
    IngestBinding,
    IngestError,
    KnowledgeIngest,
    MediaAsset,
    Relationship,
    current_ingest,
)

_CONNECTOR = "atlassian-agent"
_STREAM = "atlassian"

_BINDING = IngestBinding(connector=_CONNECTOR, stream=_STREAM)
_PAGE_BINDING = IngestBinding(
    connector=_CONNECTOR, stream=_STREAM, document_type="ConfluencePage"
)


def _fields(issue: dict[str, Any]) -> dict[str, Any]:
    """Return the Jira issue's ``fields`` sub-dict (or the record itself if flat)."""
    fields = issue.get("fields")
    return fields if isinstance(fields, dict) else issue


def _name_of(obj: Any) -> str | None:
    """Extract a display ``name`` from a Jira nested object (status/priority/type)."""
    if isinstance(obj, dict):
        return obj.get("name") or obj.get("value")
    return obj if isinstance(obj, str) else None


def _person_entity(actor: Any) -> dict[str, Any] | None:
    """Map a Jira user object → a ``:Person`` entity dict (or ``None``)."""
    if not isinstance(actor, dict):
        return None
    account_id = actor.get("accountId") or actor.get("key") or actor.get("name")
    if not account_id:
        return None
    return {
        "id": f"atlassian:person:{account_id}",
        "node_type": "Person",
        "name": actor.get("displayName") or actor.get("name"),
        "email": actor.get("emailAddress"),
        "externalToolId": str(account_id),
    }


def _issue_node(
    key: str,
    issue: dict[str, Any],
    fields: dict[str, Any],
    node_id: str,
    is_epic: bool,
    issue_type: str,
) -> dict[str, Any]:
    """Build the :Issue/:Epic node payload for one issue."""
    return {
        "id": node_id,
        "node_type": "Epic" if is_epic else "Issue",
        "issueKey": key,
        "summary": fields.get("summary"),
        "status": _name_of(fields.get("status")),
        "priority": _name_of(fields.get("priority")),
        "issueType": issue_type or None,
        "project": (fields.get("project") or {}).get("key")
        if isinstance(fields.get("project"), dict)
        else None,
        "externalToolId": str(issue.get("id") or key),
    }


def _issue_people(
    node_id: str, fields: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Build :Person nodes + assignedTo/reportedBy links for one issue."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    assignee = _person_entity(fields.get("assignee"))
    if assignee:
        entities.append(assignee)
        relationships.append(
            {"source": node_id, "target": assignee["id"], "relationship": "assignedTo"}
        )
    reporter = _person_entity(fields.get("reporter"))
    if reporter:
        entities.append(reporter)
        relationships.append(
            {"source": node_id, "target": reporter["id"], "relationship": "reportedBy"}
        )
    return entities, relationships


def _resolve_epic_key(fields: dict[str, Any]) -> str | None:
    """Team-managed projects use `parent`; classic projects an epic field."""
    parent = fields.get("parent")
    if isinstance(parent, dict):
        p_type = _name_of((parent.get("fields") or {}).get("issuetype"))
        if (p_type or "").lower() == "epic":
            return parent.get("key")
    epic = fields.get("epic")
    return epic.get("key") if isinstance(epic, dict) else None


def _epic_link(
    node_id: str, fields: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Build the :Epic stub node + :inEpic link for one issue's parent epic, if any."""
    epic_key = _resolve_epic_key(fields)
    if not epic_key:
        return [], []
    epic_id = f"atlassian:epic:{epic_key}"
    return (
        [{"id": epic_id, "node_type": "Epic", "issueKey": epic_key}],
        [{"source": node_id, "target": epic_id, "relationship": "inEpic"}],
    )


def _map_one_issue(
    issue: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Map one Jira issue record → (entities, relationships); ([], []) to skip it."""
    key = issue.get("key")
    if not key:
        return [], []
    fields = _fields(issue)
    issue_type = _name_of(fields.get("issuetype")) or ""
    is_epic = issue_type.lower() == "epic"
    node_id = f"atlassian:{'epic' if is_epic else 'issue'}:{key}"

    entities = [_issue_node(key, issue, fields, node_id, is_epic, issue_type)]
    relationships: list[dict[str, Any]] = []

    if is_epic:
        return entities, relationships

    people_entities, people_relationships = _issue_people(node_id, fields)
    entities.extend(people_entities)
    relationships.extend(people_relationships)

    epic_entities, epic_relationships = _epic_link(node_id, fields)
    entities.extend(epic_entities)
    relationships.extend(epic_relationships)

    return entities, relationships


def _to_entity(record: dict[str, Any]) -> Entity:
    return Entity(
        id=record.get("id"),
        node_type=record.get("node_type"),
        properties={k: v for k, v in record.items() if k not in ("id", "node_type")},
    )


def _to_relationship(record: dict[str, Any]) -> Relationship:
    props = {
        k: v for k, v in record.items() if k not in ("source", "target", "relationship")
    }
    return Relationship(
        source=record["source"],
        target=record["target"],
        relationship=record["relationship"],
        properties=props or None,
    )


async def _submit(
    binding: IngestBinding, change_set: ChangeSet, ingest: KnowledgeIngest | None
) -> dict[str, int]:
    service = ingest or current_ingest()
    receipt = await service.submit(binding, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


async def ingest_issues(
    issues: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map Jira issue records → ``:Issue`` / ``:Epic`` / ``:Person`` nodes and ingest.

    ``issues``: raw Jira issue dicts (as returned by
    ``jira_cloud_search_for_issues_using_jql`` / ``jira_cloud_get_issue``), each with a
    ``key`` and a ``fields`` sub-dict. Epics (issuetype == "Epic") become ``:Epic`` nodes;
    everything else becomes an ``:Issue`` linked to its assignee/reporter (``:Person``) and
    its parent epic (``:inEpic``). Returns ``{"nodes", "edges"}`` from the commit
    receipt; validation and engine failures propagate as :class:`IngestError`.
    """
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for issue in issues or []:
        issue_entities, issue_relationships = _map_one_issue(issue)
        entities.extend(issue_entities)
        relationships.extend(issue_relationships)

    if not entities:
        raise IngestError("ingest_issues needs at least one entity")
    change_set = ChangeSet(
        entities=tuple(_to_entity(e) for e in entities),
        relationships=tuple(_to_relationship(r) for r in relationships),
    )
    return await _submit(_BINDING, change_set, ingest)


def _page_text(page: dict[str, Any]) -> str | None:
    """Extract the body text of a Confluence page across body-format shapes."""
    body = page.get("body")
    if isinstance(body, str):
        return body
    if isinstance(body, dict):
        for fmt in ("storage", "atlas_doc_format", "view", "export_view"):
            part = body.get(fmt)
            if isinstance(part, dict) and part.get("value"):
                return part["value"]
            if isinstance(part, str) and part:
                return part
    return None


async def ingest_confluence_pages(
    pages: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map Confluence page records → ``:Document`` (``:ConfluencePage``) nodes and ingest.

    ``pages``: raw Confluence page dicts (as returned by ``confluence_cloud_get_pages`` /
    ``confluence_cloud_get_page_by_id``) — each with an ``id``, ``title`` and a ``body``
    (request ``body_format=storage``). Each becomes a ``:ConfluencePage`` document
    carrying the page body text + ``source_uri`` so hub-side enrichment chunks/embeds
    it. Returns ``{"nodes", "edges"}`` from the commit receipt; validation and engine
    failures propagate as :class:`IngestError`.
    """
    documents: list[Document] = []
    for page in pages or []:
        pid = page.get("id")
        text = _page_text(page)
        if not pid or not text:
            continue
        links = page.get("_links") or {}
        documents.append(
            Document(
                id=f"atlassian:page:{pid}",
                text=text,
                title=page.get("title"),
                source_uri=links.get("webui") or links.get("self") or page.get("webui"),
                properties={
                    "space_id": page.get("spaceId") or page.get("space_id"),
                    "status": page.get("status"),
                    "externalToolId": str(pid),
                },
            )
        )
    if not documents:
        raise IngestError("ingest_confluence_pages needs at least one document")
    return await _submit(_PAGE_BINDING, ChangeSet(documents=tuple(documents)), ingest)


async def ingest_attachment(
    data: bytes,
    *,
    name: str = "",
    mime_type: str = "",
    issue_key: str | None = None,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int] | None:
    """Store an Atlassian attachment's raw bytes as a ``:MediaAsset`` (Blob CAS).

    Returns ``None`` for empty ``data``, else ``{"nodes", "edges"}`` from the receipt.
    """
    if not data:
        return None
    asset = MediaAsset(
        data=data,
        mime_type=mime_type or "application/octet-stream",
        name=name,
        properties={"issue_key": issue_key} if issue_key else {},
    )
    return await _submit(_BINDING, ChangeSet(media=(asset,)), ingest)
