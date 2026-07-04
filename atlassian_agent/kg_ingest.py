"""Native epistemic-graph ingestion for Atlassian records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. The atlassian-agent package natively
pushes its data into the ONE epistemic-graph knowledge graph in every modality that
applies (the "maximum ingestion" bar):

* **Jira issues** → typed OWL nodes ``:Issue`` / ``:Epic`` / ``:Person`` (+ ``:assignedTo``
  / ``:inEpic`` / ``:reportedBy`` links) via :func:`ingest_issues`.
* **Confluence pages** → ``:Document`` (``:ConfluencePage``) nodes carrying the page body
  text + ``source_uri`` for semantic search via :func:`ingest_confluence_pages`.
* **Attachments** → raw ``:Blob`` / ``:MediaAsset`` bytes via :func:`ingest_attachment`.

All three ride the shared native-ingestion primitive
(``agent_utilities.knowledge_graph.memory.native_ingest``) — the ONE txn write path — so
this module ships only thin record→dict mappers. Everything is dependency-/engine-guarded:
with no agent-utilities KG stack or no reachable engine every entry point **no-ops**
(returns ``None``), so the connector keeps working with zero KG infrastructure. Node ids
follow ``atlassian:<class>:<externalId>`` and ``type`` matches a class the package's
``ontology_providers`` ``atlassian.ttl`` federates.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("atlassian_agent.kg")

_SOURCE = "atlassian-agent"
_DOMAIN = "atlassian"


def _primitives() -> tuple[Any, Any, Any] | None:
    """Return ``(ingest_entities, ingest_documents, media_store)`` or ``None``.

    Guarded import of the shared native-ingestion primitive; when the KG stack is
    absent this returns ``None`` and every caller cleanly no-ops.
    """
    try:
        from agent_utilities.knowledge_graph.memory.native_ingest import (
            ingest_documents,
            ingest_entities,
            media_store,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None
    return ingest_entities, ingest_documents, media_store


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
        "type": "Person",
        "name": actor.get("displayName") or actor.get("name"),
        "email": actor.get("emailAddress"),
        "externalToolId": str(account_id),
    }


def ingest_issues(
    issues: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map Jira issue records → ``:Issue`` / ``:Epic`` / ``:Person`` nodes and ingest.

    ``issues``: raw Jira issue dicts (as returned by
    ``jira_cloud_search_for_issues_using_jql`` / ``jira_cloud_get_issue``), each with a
    ``key`` and a ``fields`` sub-dict. Epics (issuetype == "Epic") become ``:Epic`` nodes;
    everything else becomes an ``:Issue`` linked to its assignee/reporter (``:Person``) and
    its parent epic (``:inEpic``). Returns ``{"nodes":n, "edges":m}`` or ``None``.
    ``client``/``graph`` are accepted for parity/injection but the shared primitive resolves
    the engine on demand.
    """
    prims = _primitives()
    if prims is None:
        return None
    ingest_entities, _ingest_documents, _media_store = prims

    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for issue in issues or []:
        key = issue.get("key")
        if not key:
            continue
        fields = _fields(issue)
        issue_type = _name_of(fields.get("issuetype")) or ""
        is_epic = issue_type.lower() == "epic"
        node_id = f"atlassian:{'epic' if is_epic else 'issue'}:{key}"
        entities.append(
            {
                "id": node_id,
                "type": "Epic" if is_epic else "Issue",
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
        )

        if is_epic:
            continue

        assignee = _person_entity(fields.get("assignee"))
        if assignee:
            entities.append(assignee)
            relationships.append(
                {"source": node_id, "target": assignee["id"], "type": "assignedTo"}
            )
        reporter = _person_entity(fields.get("reporter"))
        if reporter:
            entities.append(reporter)
            relationships.append(
                {"source": node_id, "target": reporter["id"], "type": "reportedBy"}
            )

        # Epic link: team-managed projects use `parent`; classic projects an epic field.
        parent = fields.get("parent")
        epic_key = None
        if isinstance(parent, dict):
            p_type = _name_of((parent.get("fields") or {}).get("issuetype"))
            if (p_type or "").lower() == "epic":
                epic_key = parent.get("key")
        if not epic_key:
            epic = fields.get("epic")
            epic_key = epic.get("key") if isinstance(epic, dict) else None
        if epic_key:
            epic_id = f"atlassian:epic:{epic_key}"
            entities.append(
                {"id": epic_id, "type": "Epic", "issueKey": epic_key}
            )
            relationships.append(
                {"source": node_id, "target": epic_id, "type": "inEpic"}
            )

    return ingest_entities(
        entities, relationships, source=_SOURCE, domain=_DOMAIN
    )


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


def ingest_confluence_pages(
    pages: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map Confluence page records → ``:Document`` (``:ConfluencePage``) nodes and ingest.

    ``pages``: raw Confluence page dicts (as returned by ``confluence_cloud_get_pages`` /
    ``confluence_cloud_get_page_by_id``) — each with an ``id``, ``title`` and a ``body``
    (request ``body_format=storage``). Each becomes a ``:Document`` carrying the page body
    text + ``source_uri`` so hub-side enrichment chunks/embeds it. Returns
    ``{"nodes":n, "edges":0}`` or ``None``.
    """
    prims = _primitives()
    if prims is None:
        return None
    _ingest_entities, ingest_documents, _media_store = prims

    documents: list[dict[str, Any]] = []
    for page in pages or []:
        pid = page.get("id")
        text = _page_text(page)
        if not pid or not text:
            continue
        links = page.get("_links") or {}
        source_uri = links.get("webui") or links.get("self") or page.get("webui")
        documents.append(
            {
                "id": f"atlassian:page:{pid}",
                "type": "ConfluencePage",
                "title": page.get("title"),
                "text": text,
                "source_uri": source_uri,
                "space_id": page.get("spaceId") or page.get("space_id"),
                "status": page.get("status"),
                "externalToolId": str(pid),
            }
        )
    return ingest_documents(documents, source=_SOURCE, domain=_DOMAIN)


def ingest_attachment(
    data: bytes,
    *,
    name: str = "",
    mime_type: str = "",
    issue_key: str | None = None,
    store: Any | None = None,
) -> Any | None:
    """Store an Atlassian attachment's raw bytes as a ``:Blob`` / ``:MediaAsset``.

    Best-effort: returns the :class:`StoredMedia` (or ``None`` with no engine / on
    failure; never raises). ``store`` may be injected (tests); otherwise a
    :class:`MediaStore` is built on demand via the shared primitive.
    """
    if not data:
        return None
    if store is None:
        prims = _primitives()
        if prims is None:
            return None
        _ingest_entities, _ingest_documents, media_store = prims
        store = media_store()
    if store is None:
        return None
    try:
        return store.store_media(
            data,
            media_type="attachment",
            mime_type=mime_type,
            source=_SOURCE,
            name=name,
            extra={"domain": _DOMAIN, "issue_key": issue_key} if issue_key else {"domain": _DOMAIN},
        )
    except Exception as e:  # noqa: BLE001 — store failure is non-fatal
        logger.warning("KG ingest: attachment store failed: %s", e)
        return None
