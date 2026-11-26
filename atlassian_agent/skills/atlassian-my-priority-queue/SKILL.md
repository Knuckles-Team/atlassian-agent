---
name: atlassian-my-priority-queue
skill_type: skill
description: >-
  Surface the Jira issues assigned to the current user, rank them by a combined priority + staleness score (highest priority at the top, items untouched for more than 7 days flagged and boosted), and suggest updates to those issues from the current session's context.
license: MIT
tags: [jira, atlassian, my-work, triage, staleness, priority, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---
# My Jira Priority Queue

Scope: Surface the Jira issues assigned to the current user, rank them by a combined priority + staleness score (highest priority at the top, items untouched for more than 7 days flagged and boosted), and suggest updates to those issues from the current session's context. Use when the agent must answer "what should I work on", "what's assigned to me", "what's gone stale", or wants to push conversation findings back onto the user's open tickets. Do NOT use for creating new issues (use atlassian-create-issue-guided), full project status reports (use atlassian-generate-status-report), or Plane work items (use plane-my-priority-queue).

Find everything assigned to the current user, present it as **one list ordered by a
combined priority + staleness score**, and turn what was learned in this session into
concrete, confirm-before-write updates on those issues.

## When to use
- "What's assigned to me / what should I work on next?"
- "What of mine has gone stale?" (untouched > 7 days)
- After a working session, to push findings (a fix landed, a blocker cleared, a
  decision made) back onto the relevant open tickets.

## When NOT to use
- Creating a new issue with type/field discovery → `atlassian-create-issue-guided`.
- Project-wide status reports for stakeholders → `atlassian-generate-status-report`.
- The same capability on Plane → `plane-my-priority-queue`.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`atlassian-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `ATLASSIAN_JIRA_CLOUD_URL` (or `ATLASSIAN_AGENT_URL`) | ✅ | Jira base URL |
| `ATLASSIAN_JIRA_CLOUD_USER` / `_TOKEN` (or `ATLASSIAN_AGENT_USER`/`_TOKEN`) | ✅ | Email + API token (or a bearer/OAuth token — see auth.py) |
| `MCP_TOOL_MODE` | optional | `condensed` (default) exposes the action-routed tools below |

The condensed tools take `action` + a `params_json` object + `deployment`
(`jira_cloud` default, or `jira_server`). Unsure of an exact action name? Call the
tool with `action="list_actions"` to enumerate them.

## Tools & actions
| Condensed tool | Key actions used here |
|----------------|-----------------------|
| Jira | `jira_get_current_user`, `jira_search_and_reconsile_issues_using_jql` (enhanced endpoint; fall back to `jira_search_for_issues_using_jql`), `jira_get_transitions`, `jira_do_transition`, `jira_update_issue` |
| Jira | `jira_add_comment` |

### Key parameters
- **Search** (`search_and_reconsile_issues_using_jql`): `params_json` = `{"jql": "...",
  "fields": ["summary","priority","status","updated","issuetype","project"],
  "max_results": 100}`. Page with `next_page_token`.
- The staleness/priority math lives in `scripts/rank_items.py` — do NOT eyeball the
  ordering; pipe the raw search JSON through it.

## Steps

1. Confirm who the token authenticates as with `jira_get_current_user`. Verify the account name matches the user.
2. Search assigned work with `jira_search_and_reconsile_issues_using_jql` and `{"jql":"assignee = currentUser() AND statusCategory != Done"}`. Verify the response has an `issues` list and save it to `results.json`.
3. Rank the results with `python scripts/rank_items.py results.json`. Verify the table shows the highest priority first with stale items flagged.
4. Draft updates from this session's context, for example a `jira_add_comment` body, and show them to the user. Verify each draft names an issue key and the user confirmed it.
5. Apply confirmed updates with `jira_add_comment`(issue_id_or_key, payload) or `jira_do_transition`. Verify the issue shows the comment or new status via `jira_get_issue`.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| Empty queue | The token authenticates as a different account or no issues are open | Check `jira_get_current_user` and loosen the JQL in `references/jql-recipes.md`. |
| Ranking script fails | The saved file is not the raw search JSON | Save the full tool response to `results.json` and rerun `python scripts/rank_items.py results.json`. |
| Comment rejected | The Cloud body is not ADF | Send a valid Atlassian Document Format document as the comment body. |

## Recipes

### 1. List my ranked, stale-flagged queue
Run the assigned-to-me JQL (server-side `ORDER BY` is a hint; the script is authoritative):
```json
{"jql":"assignee = currentUser() AND statusCategory != Done ORDER BY priority DESC, updated ASC","fields":["summary","priority","status","updated","issuetype","project"],"max_results":100}
```
Save the tool's JSON response, then rank it:
```bash
python scripts/rank_items.py results.json          # human table with ⚠STALE flags
python scripts/rank_items.py --json results.json   # ranked JSON for further use
```
`score = priority_rank*100 + min(days_stale,30) + (25 if days_stale>7)` — priority is
the dominant term, staleness breaks ties and lifts anything older than 7 days. See
`references/jql-recipes.md` for scoped variants (single project, overdue, by sprint).

### 2. Suggest updates from this session's context
For each ranked issue, scan the **current conversation** for facts that concern it —
e.g. "I fixed the null-pointer in the auth handler" maps to the auth bug ticket, "we
decided to defer the migration" maps to the migration story. For every match, **draft**
one of the following and **show it to the user for confirmation before writing**:
- A progress comment → `jira_add_comment`,
  `params_json={"issue_id_or_key":"PROJ-123","payload":{...comment body...}}`.
- A field edit (e.g. remaining estimate, labels) → the `jira_<operation>` tools
  `action="update_issue"`, `params_json={"issue_id_or_key":"PROJ-123","payload":{"fields":{...}}}`.
- A status change → `jira_get_transitions` to find the valid
  transition id, then `action="do_transition"`.

Never apply a write without explicit user confirmation of the drafted change.

## Gotchas
- `currentUser()` resolves to whoever the configured token authenticates as — confirm
  with `get_current_user` if the identity is ambiguous.
- The search-endpoint action is spelled `search_and_reconsile_issues_using_jql`
  (the vendor's misspelling of "reconcile"); the enhanced `/search/jql` endpoint pages
  with `next_page_token`, not `start_at`.
- Comment/rich-text bodies on Jira **Cloud** use ADF (Atlassian Document Format), not
  plain markdown — pass a valid ADF document as the comment `body`.
- `rank_items.py` treats a missing priority as Medium and clamps the staleness term at
  30 days; adjust the constants in the script if your instance uses custom priorities.

## Related
- **atlassian-create-issue-guided** — open a new issue with type/field discovery.
- **atlassian-generate-status-report** — project-wide reporting to Confluence.
- **plane-my-priority-queue** — the same capability for Plane work items.
