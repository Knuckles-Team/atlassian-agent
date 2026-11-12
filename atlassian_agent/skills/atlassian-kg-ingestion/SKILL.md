---
name: atlassian-kg-ingestion
skill_type: skill
description: >-
  Ingest Jira issues and Confluence pages into the knowledge graph as typed
  nodes and documents. Use when the agent must make Atlassian content queryable
  alongside other sources. Do NOT use to read or edit Jira or Confluence
  directly.
license: MIT
tags: [atlassian, knowledge-graph, ingestion]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Atlassian knowledge-graph ingestion

Two Wire-First ingest tools: they list through the product clients and push the records best-effort.

## When to use
- Ingest issues selected by JQL.
- Ingest Confluence pages for a space.

## When NOT to use
- Reading or editing content: use the product skills.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (2)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `atlassian_ingest_confluence` | W | limit, space_id |
| `atlassian_ingest_issues` | W | jql, max_results |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `kg-change-records`: `atlassian_ingest_confluence` -> `atlassian_ingest_issues`
