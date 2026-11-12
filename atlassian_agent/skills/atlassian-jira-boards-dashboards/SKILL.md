---
name: atlassian-jira-boards-dashboards
skill_type: skill
description: >-
  Jira saved filters, filter sharing, dashboards and gadgets, favourites and
  plans. Use when the agent must create or share a filter, build a dashboard or
  read a plan. Do NOT use for issue edits.
license: MIT
tags: [atlassian, jira, filters, dashboards]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Jira filters, dashboards and plans

Typed operations for saved views of Jira work.

## When to use
- Create, update, share or delete a filter.
- Build or copy a dashboard and manage its gadgets.
- Read and archive plans.

## When NOT to use
- Issue edits: use atlassian-jira-issues.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (38)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `jira_add_gadget` | W | dashboard_id, payload |
| `jira_archive_plan` | W | payload, plan_id |
| `jira_bulk_edit_dashboards` | W | payload |
| `jira_change_filter_owner` | W | id_, payload |
| `jira_copy_dashboard` | W | extend_admin_permissions, id_, payload |
| `jira_create_dashboard` | W | extend_admin_permissions, payload |
| `jira_create_filter` | W | expand, override_share_permissions, payload |
| `jira_create_plan` | W | payload, use_group_id |
| `jira_create_plan_only_team` | W | payload, plan_id |
| `jira_delete_dashboard` | D | confirm, id_, payload |
| `jira_delete_dashboard_item_property` | D | confirm, dashboard_id, item_id, payload, property_key |
| `jira_delete_favourite_for_filter` | D | confirm, expand, id_, payload |
| `jira_delete_filter` | D | confirm, id_, payload |
| `jira_delete_plan_only_team` | D | confirm, payload, plan_id, plan_only_team_id |
| `jira_duplicate_plan` | W | payload, plan_id |
| `jira_get_all_available_dashboard_gadgets` | R | payload |
| `jira_get_all_dashboards` | R | filter, max_results, payload, start_at |
| `jira_get_all_gadgets` | R | dashboard_id, gadget_id, module_key, payload, uri |
| `jira_get_dashboard` | R | id_, payload |
| `jira_get_dashboard_item_property` | R | dashboard_id, item_id, payload, property_key |
| `jira_get_dashboard_item_property_keys` | R | dashboard_id, item_id, payload |
| `jira_get_dashboards_paginated` | R | account_id, dashboard_name, expand, group_id, groupname, max_results, order_by, owner |
| `jira_get_favourite_filters` | R | expand, payload |
| `jira_get_filter` | R | expand, id_, override_share_permissions, payload |
| `jira_get_filters_paginated` | R | account_id, expand, filter_name, group_id, groupname, id_, is_substring_match, max_results |
| `jira_get_my_filters` | R | expand, include_favourites, payload |
| `jira_get_plan` | R | payload, plan_id, use_group_id |
| `jira_get_plan_only_team` | R | payload, plan_id, plan_only_team_id |
| `jira_get_plans` | R | cursor, include_archived, include_trashed, max_results, payload |
| `jira_remove_gadget` | D | confirm, dashboard_id, gadget_id, payload |
| `jira_set_dashboard_item_property` | W | dashboard_id, item_id, payload, property_key |
| `jira_set_favourite_for_filter` | W | expand, id_, payload |
| `jira_trash_plan` | W | payload, plan_id |
| `jira_update_dashboard` | W | extend_admin_permissions, id_, payload |
| `jira_update_filter` | W | expand, id_, override_share_permissions, payload |
| `jira_update_gadget` | W | dashboard_id, gadget_id, payload |
| `jira_update_plan` | W | payload, plan_id, use_group_id |
| `jira_update_plan_only_team` | W | payload, plan_id, plan_only_team_id |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `jira-boards-dashboards-dashboard`: `jira_get_all_dashboards` -> `jira_get_dashboard` -> `jira_copy_dashboard` -> `jira_create_dashboard` -> `jira_update_dashboard` -> `jira_delete_dashboard`
- `jira-boards-dashboards-dashboard-item`: `jira_get_dashboard_item_property` -> `jira_get_dashboard_item_property_keys` -> `jira_set_dashboard_item_property` -> `jira_delete_dashboard_item_property`
- `jira-boards-dashboards-favourite-filter`: `jira_get_favourite_filters` -> `jira_set_favourite_for_filter` -> `jira_delete_favourite_for_filter`
- `jira-boards-dashboards-filter`: `jira_get_filter` -> `jira_get_my_filters` -> `jira_create_filter` -> `jira_update_filter` -> `jira_delete_filter`
- `jira-boards-dashboards-gadget`: `jira_get_all_gadgets` -> `jira_add_gadget` -> `jira_update_gadget` -> `jira_remove_gadget`
- `jira-boards-dashboards-plan`: `jira_get_plan` -> `jira_get_plans` -> `jira_create_plan` -> `jira_duplicate_plan` -> `jira_trash_plan` -> `jira_archive_plan` -> `jira_update_plan`
- `jira-boards-dashboards-plan-only`: `jira_get_plan_only_team` -> `jira_create_plan_only_team` -> `jira_update_plan_only_team` -> `jira_delete_plan_only_team`
- `jira-boards-dashboards-read-records`: `jira_get_all_available_dashboard_gadgets` -> `jira_get_dashboards_paginated` -> `jira_get_filters_paginated`
- `jira-boards-dashboards-change-records`: `jira_bulk_edit_dashboards` -> `jira_change_filter_owner`
