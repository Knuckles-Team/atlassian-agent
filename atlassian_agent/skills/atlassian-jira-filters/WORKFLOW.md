# Atlassian Jira Filters

Manage Jira saved filters (saved JQL searches) end to end — create, get, search, update, delete, run/use them, star them as favourites, manage their columns, change owner, and administer their share/edit permissions (add, get, delete) and the instance default share scope. Use when the agent must create or curate reusable JQL filters, share a filter with a group/project/user, audit who a filter is shared with, or run a saved filter's results. Do NOT use for one-off ad-hoc JQL queries (just run the search directly), listing the user's own issues (use atlassian-my-priority-queue), or Plane — Plane's public API exposes no saved-views/filters equivalent.

# Jira Saved Filters

Create and curate reusable **saved filters** (named JQL searches), run them, and
administer their **sharing/edit permissions**. A filter is just a stored JQL query plus
ownership, favourite state, column config, and a set of share permissions.

## When to use
- Create / update / delete a saved filter, or search existing filters.
- Run ("use") a saved filter to get its issues.
- Star/unstar a filter, manage its result columns, or change its owner.
- Add, inspect, or remove **share/edit permissions**, or set the default share scope.

## When NOT to use
- A throwaway JQL query with no need to persist it → run the search directly
  (`atlassian_jira_issue` `search_and_reconsile_issues_using_jql`).
- "What's assigned to me" → `atlassian-my-priority-queue`.
- Plane: its public v1 API has **no** Views/Saved-Filters resource, so there is no
  equivalent tool — this skill is Jira-only.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`atlassian-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `ATLASSIAN_JIRA_CLOUD_URL` (or `ATLASSIAN_AGENT_URL`) | ✅ | Jira base URL |
| `ATLASSIAN_JIRA_CLOUD_USER` / `_TOKEN` (or `ATLASSIAN_AGENT_USER`/`_TOKEN`) | ✅ | Auth |
| `MCP_TOOL_MODE` | optional | `condensed` (default) exposes the action-routed tools |

All filter actions run on the **`atlassian_jira_other`** condensed tool with
`action` + `params_json` + `deployment` (`jira_cloud` default / `jira_server`). Filters
exist on both Cloud (v3) and Server/DC (v2). Unsure of an action or its exact params?
Call `atlassian_jira_other` with `action="list_actions"` or `action="help"`.

## Tools & actions
| Action (on `atlassian_jira_other`) | Purpose |
|-----------------------------------|---------|
| `create_filter` | Create a filter (`payload`: name, jql, description, favourite, sharePermissions, editPermissions) |
| `get_filter` | Read one filter (`id_`, optional `expand`) — returns its `jql`, `searchUrl`, permissions |
| `get_filters_paginated` | **Search** filters (`filter_name`, `account_id`, `owner`, `project_id`, `order_by`, `max_results`, `expand`) |
| `get_my_filters` / `get_favourite_filters` | The caller's own / starred filters |
| `update_filter` | Update a filter (`id_`, `payload`) |
| `delete_filter` | Delete a filter (`id_`) |
| `set_favourite_for_filter` / `delete_favourite_for_filter` | Star / unstar (`id_`) |
| `get_columns` / `set_columns` / `reset_columns` | Result column config (`id_`, `payload`) |
| `change_filter_owner` | Transfer ownership (`id_`, `payload={"accountId":"…"}`) |
| `get_share_permissions` | List a filter's share permissions (`id_`) |
| `add_share_permission` | Add a share/edit permission (`id_`, `payload`) |
| `get_share_permission` / `delete_share_permission` | Read / remove one permission (`id_`, `permission_id`) |
| `get_default_share_scope` / `set_default_share_scope` | Instance default share scope (`payload={"scope":"GLOBAL\|AUTHENTICATED\|PRIVATE"}`) |

> Path-id params use the trailing-underscore name `id_` (and `permission_id`) — that is
> the exact keyword the generated client expects. If a call rejects the key, run
> `action="help"` on the tool to confirm the parameter names for your instance.

## Recipes (`params_json`)

### Create a filter (optionally pre-shared)
```json
{"payload":{"name":"My team open bugs","jql":"project = PROJ AND type = Bug AND statusCategory != Done ORDER BY priority DESC","description":"Open bugs for triage","favourite":true,"sharePermissions":[{"type":"project","project":{"id":"10000"}}]}}
```
`action="create_filter"` → returns the new filter's `id`, `jql`, and `searchUrl`.

### Find existing filters
```json
{"filter_name":"bugs","order_by":"name","max_results":50,"expand":"jql,owner,sharePermissions"}
```
`action="get_filters_paginated"`. Or `action="get_my_filters"` / `action="get_favourite_filters"`.

### Use (run) a saved filter
Read it, then run its JQL via the referenced filter id — JQL natively supports `filter = <id>`:
```json
{"id_":12345,"expand":"jql"}
```
`action="get_filter"`, then `atlassian_jira_issue` `action="search_and_reconsile_issues_using_jql"`:
```json
{"jql":"filter = 12345 ORDER BY updated DESC","fields":["summary","status","assignee","updated"],"max_results":100}
```

### Update / delete
```json
{"id_":12345,"payload":{"name":"My team open bugs (P1+)","jql":"project = PROJ AND type = Bug AND priority in (Highest,High) AND statusCategory != Done"}}
```
`action="update_filter"`; `action="delete_filter"` with `{"id_":12345}`.

### Manage share / edit permissions
Inspect: `action="get_share_permissions"` `{"id_":12345}`. Add one (type is one of
`group`, `project`, `user`, `authenticated` (any logged-in user), `global`/`loggedin`):
```json
{"id_":12345,"payload":{"type":"group","group":{"name":"jira-developers"}}}
```
```json
{"id_":12345,"payload":{"type":"user","user":{"accountId":"5b10ac8d82e05b22cc7d4ef5"}}}
```
```json
{"id_":12345,"payload":{"type":"project","project":{"id":"10000"},"role":{"id":"10002"}}}
```
`action="add_share_permission"` → returns the created permission with its `id`. Remove it
with `action="delete_share_permission"` `{"id_":12345,"permission_id":67890}`.

### Default share scope (admin)
```json
{"payload":{"scope":"AUTHENTICATED"}}
```
`action="set_default_share_scope"` (`GLOBAL` | `AUTHENTICATED` | `PRIVATE`);
`action="get_default_share_scope"` to read it.

## Gotchas
- `sharePermissions` (view) and `editPermissions` (edit) are **separate** lists — adding a
  view share does not grant edit, and vice-versa. `add_share_permission` targets the view
  list; set `editPermissions` at create/update time in the `payload`.
- Only the filter **owner** (or an admin) may change permissions or owner; a shared filter
  you don't own is read-only to you.
- On Jira **Server/DC** (`deployment="jira_server"`) use `name`/`key`-based identifiers for
  users/groups instead of Cloud's `accountId`, and note some Cloud-only endpoints
  (`get_my_filters`, columns) may differ — fall back to `get_filters_paginated`.
- Sharing to `project` optionally scopes to a project **role** (`role.id`); omit it to
  share with the whole project.
- Deleting a filter that dashboards/boards depend on will break them — check with
  `get_filter` `expand=...` before deleting.

## Related
- **atlassian-my-priority-queue** — the ranked "assigned to me" queue (ad-hoc, not saved).
- **atlassian-create-issue-guided** — open a new issue with field discovery.
