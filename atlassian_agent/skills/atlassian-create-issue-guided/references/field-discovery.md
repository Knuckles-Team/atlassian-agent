# Reading Jira createmeta output & mapping field types

`atlassian_jira_issue` `action="get_create_issue_meta_issue_type_id"`
(`params_json={"project_id_or_key":"PROJ","issue_type_id":"10004"}`) returns a paginated
list of field descriptors for exactly one project + issue-type combination. Each descriptor
looks like:

```json
{
  "fieldId": "customfield_10016",
  "name": "Story Points",
  "required": false,
  "schema": {"type": "number", "custom": "com.pyxis.greenhopper.jira:jsw-story-points", "customId": 10016},
  "allowedValues": []
}
```

## What to collect
1. Every descriptor with `required: true` — these MUST be in the payload.
2. Any field the user explicitly asked to set (match by `name`, case-insensitive; custom
   fields are matched by label here and keyed by `fieldId` in the payload).

Ignore fields that are neither required nor requested — leave them to Jira defaults.

## schema.type → payload value shape

| `schema.type` | Payload value | Notes |
|---------------|---------------|-------|
| `string` | `"text"` | Plain single-line/paragraph text (non-ADF fields). |
| `doc` (system `description`, `environment`) | ADF object | Cloud only; see ADF note below. Server = wiki string. |
| `number` | `5` | Bare JSON number. |
| `date` | `"2026-07-15"` | `YYYY-MM-DD`. |
| `datetime` | `"2026-07-15T09:00:00.000+0000"` | ISO-8601 with offset. |
| `option` | `{"id":"10201"}` or `{"value":"Green"}` | Pick from `allowedValues`. |
| `array` of `option` | `[{"id":"10201"},{"id":"10202"}]` | Multi-select. |
| `array` of `string` | `["backend","urgent"]` | e.g. Labels. |
| `user` | `{"accountId":"5b10..."}` (Cloud) / `{"name":"jsmith"}` (Server) | Resolve via `atlassian_jira_user` find-assignable-users. |
| `array` of `user` | list of the above | Multi-user pickers. |
| `priority` | `{"name":"High"}` or `{"id":"2"}` | From `allowedValues`. |
| `project` | `{"key":"PROJ"}` | Usually set once at top level. |
| `issuetype` | `{"id":"10004"}` | The chosen type. |
| `array` of `version` | `[{"id":"10100"}]` | Fix Version / Affects Version. |
| `array` of `component` | `[{"id":"10300"}]` | Components. |
| `any` / cascading select | `{"value":"Parent","child":{"value":"Child"}}` | Read `allowedValues` for the nested tree. |

## ADF (Atlassian Document Format) — Cloud rich text
`doc`-typed fields (`description`, `comment`, some custom text fields) require an ADF
document on Cloud, not a markdown/plain string:

```json
{"type":"doc","version":1,"content":[
  {"type":"paragraph","content":[{"type":"text","text":"Your text here."}]}
]}
```
On Jira **Server/Data Center** (`deployment="jira_server"`) the same fields take a wiki-
markup **string** instead — do not send ADF there.

## Option values
For `option`, `priority`, `version`, `component`, etc., always pick from the descriptor's
`allowedValues` array — sending a `value`/`id` that is not in that list fails validation.
Each entry carries both `id` and a human field (`value`/`name`); prefer `id` for stability.

## Fallback for older instances
If `get_create_issue_meta_issue_type_id` 404s (older Jira), use:
`atlassian_jira_issue` `action="get_create_issue_meta"` with
`params_json={"project_keys":"PROJ","issuetype_ids":"10004","expand":"projects.issuetypes.fields"}`
and read `projects[0].issuetypes[0].fields` — the same descriptor shape under a nested path.
