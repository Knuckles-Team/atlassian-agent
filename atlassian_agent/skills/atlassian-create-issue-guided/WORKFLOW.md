# Atlassian Create Issue Guided

Create a Jira issue after discovering, from the live instance, exactly which fields the chosen project + issue type support — including which are required and which are custom fields (customfield_xxxxx) — then populate and submit it. Use when the agent must open a Jira issue/bug/story/task and needs to know the correct, possibly custom, field schema instead of guessing. Do NOT use for listing the user's own work (use atlassian-my-priority-queue), bulk spec breakdowns (use atlassian-spec-to-backlog), or Plane work items (use plane-create-work-item-guided).

# Guided Jira Issue Creation

Never guess a field schema. This skill **queries the instance** for the issue types a
project offers and the exact field set (required + optional + custom) each type accepts,
then builds a valid `create_issue` payload.

## When to use
- Open a new Jira issue where you must respect required and custom fields.
- The user says "file a bug/story/task in PROJ" and the project has a non-default schema.

## When NOT to use
- Listing / triaging the user's own issues → `atlassian-my-priority-queue`.
- Breaking a spec into many tickets → `atlassian-spec-to-backlog`.
- Creating a Plane work item → `plane-create-work-item-guided`.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`atlassian-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `ATLASSIAN_JIRA_CLOUD_URL` (or `ATLASSIAN_AGENT_URL`) | ✅ | Jira base URL |
| `ATLASSIAN_JIRA_CLOUD_USER` / `_TOKEN` (or `ATLASSIAN_AGENT_USER`/`_TOKEN`) | ✅ | Auth (basic email+token, bearer/PAT, or OAuth) |
| `MCP_TOOL_MODE` | optional | `condensed` (default) exposes the action-routed tools |

Tools take `action` + `params_json` + `deployment` (`jira_cloud` default / `jira_server`).
Unsure of an action name? Call the tool with `action="list_actions"`.

## Tools & actions
| Condensed tool | Key actions |
|----------------|-------------|
| `atlassian_jira_issue` | `get_issue_types_for_project`, `get_create_issue_meta_issue_type_id`, `get_create_issue_meta`, `create_issue` |
| `atlassian_jira_field` | `get_fields` (map custom-field **name → id**) |
| `atlassian_jira_project` | `search_projects` / `get_project` (resolve a project name → key/id) |

## Recipes (discover → populate → create)

### 1. Resolve the project and its issue types
```json
{"project_id_or_key":"PROJ"}
```
`atlassian_jira_issue` `action="get_issue_types_for_project"` → the types (Bug, Story,
Task, Epic, Sub-task, and any custom types) valid for that project. Pick one with the user.

### 2. Discover the exact field schema for project + issue type
```json
{"project_id_or_key":"PROJ","issue_type_id":"10004"}
```
`atlassian_jira_issue` `action="get_create_issue_meta_issue_type_id"` returns, per field:
`fieldId` (e.g. `summary`, `customfield_10011`), `name`, `required` (bool), `schema.type`,
and `allowedValues` for option fields. This is the source of truth for **what to collect
and what is mandatory** — including custom fields. See `references/field-discovery.md` for
how to read the response and map each `schema.type` to a value shape.

If the user names a custom field by label ("Sprint", "Story Points"), resolve its id with
`atlassian_jira_field` `action="get_fields"` and match on `name`.

### 3. Collect values, then create
Prompt the user only for **required** fields plus any they explicitly asked to set. Build
the payload keyed by field id (custom fields by their `customfield_*` id):
```json
{"payload":{"fields":{
  "project":{"key":"PROJ"},
  "issuetype":{"id":"10004"},
  "summary":"Login page 500s on empty password",
  "description":{"type":"doc","version":1,"content":[{"type":"paragraph","content":[{"type":"text","text":"Steps to reproduce ..."}]}]},
  "priority":{"name":"High"},
  "customfield_10011":"AUTH-Sprint-14",
  "customfield_10016":5
}}}
```
`atlassian_jira_issue` `action="create_issue"`. Report the returned `key` and browse URL.

## Gotchas
- **ADF, not markdown:** on Jira **Cloud** the `description` (and any rich-text custom
  field) must be an Atlassian Document Format object, as above — a plain string is
  rejected. On **Server/DC** (`deployment="jira_server"`) those fields are wiki-markup strings.
- A field absent from `get_create_issue_meta_issue_type_id` is **not on the create screen**
  for that type — setting it will fail; add it via the project's screen scheme first, or
  set it with `update_issue` after creation if it is editable.
- `required: true` fields must be present or the create 400s. Do not invent values for
  required custom fields — ask the user.
- Reference-type fields expect ids/objects: `assignee` → `{"accountId":"..."}` (Cloud) or
  `{"name":"..."}` (Server); option fields → `{"id":"..."}` or `{"value":"..."}` from
  `allowedValues`; multi-select → a list of such objects.
- If `get_create_issue_meta_issue_type_id` is unavailable on an older instance, fall back
  to `get_create_issue_meta` with `expand="projects.issuetypes.fields"`.

## Related
- **atlassian-my-priority-queue** — after creating, see it in the ranked queue.
- **atlassian-spec-to-backlog** — bulk-create Epics + tickets from a Confluence spec.
- **plane-create-work-item-guided** — the same discovery-driven creation on Plane.
