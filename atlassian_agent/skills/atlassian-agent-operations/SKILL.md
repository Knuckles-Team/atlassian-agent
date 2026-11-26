---
name: atlassian-agent-operations
skill_type: skill
description: >-
  Operate atlassian-agent through its governed MCP and Arbora capabilities, including atlassian capture tasks from meeting notes, atlassian create issue guided, atlassian generate status report, atlassian jira filters, atlassian my priority queue, atlassian search company knowledge, atlassian spec to backlog, atlassian triage issue.
---

# Atlassian Agent Operations

Scope: Operate atlassian-agent through its governed MCP and Arbora capabilities, including atlassian capture tasks from meeting notes, atlassian create issue guided, atlassian generate status report, atlassian jira filters, atlassian my priority queue, atlassian search company knowledge, atlassian spec to backlog, atlassian triage issue. Use when a request requires this provider's read, change, automation, ingestion, troubleshooting, or evidence workflows.

Use the provider's governed MCP tools through Arbora delegation.

## Steps

1. Establish the verified GraphSession and tenant with `manage(intent="session")`. Verify the response names the expected tenant.
2. Discover the current tool surface with `find(intent="atlassian")`. Verify the tool name and parameter schema you plan to use appear in the result.
3. Inspect the target read-only first, for example with `jira_get_issue` or `confluence_get_page_by_id`. Verify the returned record matches the intended target id.
4. Preview any change with the tool's dry-run or plan mode via `act(op="fleet.call")`. Verify the plan lists the exact records to be changed and obtain approval for destructive ones.
5. Execute the approved change as a fenced WorkItem with `act(op="fleet.call")` and read the result back. Verify the durable record and its trace show the new state before reporting completion.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| Tool or schema not found | The tool name is stale | Rediscover with `find(intent=...)` and use the returned op id and parameters. |
| Authorization refused | The signed-in account lacks the permission | Stop and report the missing permission; do not widen access without explicit approval. |
| Plan lacks confirmation | A destructive tool was called without `confirm=true` | Resubmit with `confirm=true` only after the user approves the named target. |

## Workflow

1. Establish the verified GraphSession and tenant before discovery or retrieval.
2. Discover the current condensed tool surface; never assume a stale tool name or schema.
3. Prefer read-only inspection first. For changes, present impact and use the provider's
   dry-run or preview mode when available.
4. Execute mutations as fenced WorkItems so retries remain idempotent and auditable.
5. Ingest source data only through the signed connector preset and ChangeEnvelope path.
6. Verify the durable result and its trace/evidence before reporting completion.

## Safety contract

- Never persist credentials, endpoints, raw personal identifiers, hostnames, or local paths.
- Resolve TLS trust and verification from environment/configuration; never hardcode bypasses.
- Treat unknown ACL, tenant, schema, or tool-contract state as a hard failure.
- Require explicit approval for destructive, externally visible, or irreversible actions.
- Keep runtime traces policy-scoped and privacy-sanitized.

## Specialized workflows

Read [the workflow catalog](references/catalog.md) only when the request needs a
provider-specific procedure, parameter map, script, or reference asset.
