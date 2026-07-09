# JQL recipes for "assigned to me" queues

All queries below feed `atlassian_jira_issue` `action="search_and_reconsile_issues_using_jql"`
(or `search_for_issues_using_jql`) via `params_json.jql`. Request at least the fields
`summary, priority, status, updated, issuetype, project` so `scripts/rank_items.py` can
score them. The server-side `ORDER BY` is only a hint — the ranking script is authoritative.

## Core queue (all open work assigned to me)
```
assignee = currentUser() AND statusCategory != Done ORDER BY priority DESC, updated ASC
```

## Only the stale ones (untouched > 7 days)
```
assignee = currentUser() AND statusCategory != Done AND updated <= -7d ORDER BY updated ASC
```
`rank_items.py` already flags these with `⚠STALE`; this variant is for when the user
explicitly wants *only* the stale backlog.

## Scoped to one project
```
assignee = currentUser() AND project = "PROJ" AND statusCategory != Done ORDER BY priority DESC, updated ASC
```

## Overdue (past due date)
```
assignee = currentUser() AND statusCategory != Done AND duedate < now() ORDER BY duedate ASC
```

## In the active sprint (Jira Software boards)
```
assignee = currentUser() AND sprint in openSprints() AND statusCategory != Done ORDER BY priority DESC
```

## Recently commented (needs a reply)
```
assignee = currentUser() AND statusCategory != Done ORDER BY updated DESC
```
Then read each issue's comments to find those where the last commenter is not the user.

## Blocked / flagged
```
assignee = currentUser() AND (status = Blocked OR flagged = Impediment) ORDER BY priority DESC
```

## Notes
- `statusCategory != Done` is portable across workflows; prefer it over enumerating
  named statuses (`status not in (Done, Closed, Resolved)`), which varies per project.
- `currentUser()` requires an authenticated token; it will not work with anonymous access.
- Time units for `updated`/`created`: `-7d`, `-2w`, `-1h`. Negative = "ago".
- On Jira **Server/Data Center** set `deployment="jira_server"`; `statusCategory` and
  `openSprints()` are still supported on modern DC versions.
