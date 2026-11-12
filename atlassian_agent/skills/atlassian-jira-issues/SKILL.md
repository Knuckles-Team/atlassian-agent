---
name: atlassian-jira-issues
skill_type: skill
description: >-
  Jira issue work through typed operations: search with JQL, read and edit
  issues, comment, log work, attach files, watch and vote, link issues, read
  changelogs, bulk-edit and archive. Use when the agent must find, triage,
  change or report on Jira issues. Do NOT use for project or workflow
  configuration (use atlassian-jira-configuration) or for boards, filters and
  dashboards (use atlassian-jira-boards-dashboards).
license: MIT
tags: [atlassian, jira, issues, jql]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Jira issues: search, comments, worklogs, attachments and bulk changes

Typed `jira_<operation>` tools for issues. Cloud or Server/Data Center is chosen by ATLASSIAN_JIRA_DEPLOYMENT, and each tool picks the matching client.

## When to use
- Search issues with JQL and read one by key.
- Create or edit an issue, assign it, transition it.
- Add comments, worklogs and attachments; watch or vote.
- Link issues and read issue properties and changelogs.
- Bulk edit, move or archive issues.

## When NOT to use
- Workflows, screens and fields: use atlassian-jira-configuration.
- Filters and dashboards: use atlassian-jira-boards-dashboards.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (105)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `jira_add_attachment` | W | issue_id_or_key, payload |
| `jira_add_comment` | W | expand, issue_id_or_key, payload |
| `jira_add_vote` | W | issue_id_or_key, payload |
| `jira_add_watcher` | W | issue_id_or_key, payload |
| `jira_add_worklog` | W | adjust_estimate, expand, issue_id_or_key, new_estimate, notify_users, override_editable_flag, payload, reduce_by |
| `jira_addon_properties_resource_delete_addon_property_delete` | D | addon_key, confirm, payload, property_key |
| `jira_addon_properties_resource_get_addon_property_get` | R | addon_key, payload, property_key |
| `jira_addon_properties_resource_put_addon_property_put` | W | addon_key, payload, property_key |
| `jira_archive_issues` | W | payload |
| `jira_archive_issues_async` | W | payload |
| `jira_assign_issue` | W | issue_id_or_key, payload |
| `jira_bulk_delete_issue_property` | D | confirm, payload, property_key |
| `jira_bulk_delete_worklogs` | D | adjust_estimate, confirm, issue_id_or_key, override_editable_flag, payload |
| `jira_bulk_fetch_issues` | W | payload |
| `jira_bulk_move_worklogs` | W | adjust_estimate, issue_id_or_key, override_editable_flag, payload |
| `jira_bulk_set_issue_properties_by_issue` | W | payload |
| `jira_bulk_set_issue_property` | W | payload, property_key |
| `jira_bulk_set_issues_properties_list` | W | payload |
| `jira_count_issues` | W | payload |
| `jira_create_issue` | W | payload, update_history |
| `jira_create_issues` | W | payload |
| `jira_create_or_update_remote_issue_link` | W | issue_id_or_key, payload |
| `jira_delete_comment` | D | confirm, id_, issue_id_or_key, payload |
| `jira_delete_comment_property` | D | comment_id, confirm, payload, property_key |
| `jira_delete_forge_app_property` | D | confirm, payload, property_key |
| `jira_delete_issue` | D | confirm, delete_subtasks, issue_id_or_key, payload |
| `jira_delete_issue_link` | D | confirm, link_id, payload |
| `jira_delete_issue_property` | D | confirm, issue_id_or_key, payload, property_key |
| `jira_delete_remote_issue_link_by_global_id` | D | confirm, global_id, issue_id_or_key, payload |
| `jira_delete_remote_issue_link_by_id` | D | confirm, issue_id_or_key, link_id, payload |
| `jira_delete_worklog` | D | adjust_estimate, confirm, id_, increase_by, issue_id_or_key, new_estimate, notify_users, override_editable_flag |
| `jira_delete_worklog_property` | D | confirm, issue_id_or_key, payload, property_key, worklog_id |
| `jira_do_transition` | W | issue_id_or_key, payload |
| `jira_edit_issue` | W | expand, issue_id_or_key, notify_users, override_editable_flag, override_screen_security, payload, return_issue |
| `jira_expand_attachment_for_humans` | R | id_, payload |
| `jira_expand_attachment_for_machines` | R | id_, payload |
| `jira_export_archived_issues` | W | payload |
| `jira_get_all_labels` | R | max_results, payload, start_at |
| `jira_get_application_property` | R | key, key_filter, payload, permission_level |
| `jira_get_approximate_application_license_count` | R | application_key, payload |
| `jira_get_approximate_license_count` | R | payload |
| `jira_get_attachment` | R | id_, payload |
| `jira_get_attachment_content` | R | id_, payload, redirect |
| `jira_get_attachment_meta` | R | payload |
| `jira_get_attachment_thumbnail` | R | fallback_to_default, height, id_, payload, redirect, width |
| `jira_get_available_transitions` | R | ending_before, issue_ids_or_keys, payload, starting_after |
| `jira_get_bulk_changelogs` | W | payload |
| `jira_get_bulk_operation_progress` | R | payload, task_id |
| `jira_get_comment` | R | expand, id_, issue_id_or_key, payload |
| `jira_get_comment_property` | R | comment_id, payload, property_key |
| `jira_get_comment_property_keys` | R | comment_id, payload |
| `jira_get_comments` | R | expand, issue_id_or_key, max_results, order_by, payload, start_at |
| `jira_get_comments_by_ids` | W | expand, payload |
| `jira_get_create_issue_meta` | R | expand, issuetype_ids, issuetype_names, payload, project_ids, project_keys |
| `jira_get_edit_issue_meta` | R | issue_id_or_key, override_editable_flag, override_screen_security, payload |
| `jira_get_forge_app_property` | R | payload, property_key |
| `jira_get_forge_app_property_keys` | R | payload |
| `jira_get_ids_of_worklogs_deleted_since` | R | payload, since |
| `jira_get_ids_of_worklogs_modified_since` | R | expand, payload, since |
| `jira_get_is_watching_issue_bulk` | W | payload |
| `jira_get_issue` | R | expand, fields, fields_by_keys, issue_id_or_key, payload, properties, update_history |
| `jira_get_issue_all_types` | R | payload |
| `jira_get_issue_limit_report` | R | is_returning_keys, payload |
| `jira_get_issue_link` | R | link_id, payload |
| `jira_get_issue_picker_resource` | R | current_issue_key, current_jql, current_project_id, payload, query, show_sub_task_parent, show_sub_tasks |
| `jira_get_issue_property` | R | issue_id_or_key, payload, property_key |
| `jira_get_issue_property_keys` | R | issue_id_or_key, payload |
| `jira_get_issue_watchers` | R | issue_id_or_key, payload |
| `jira_get_issue_worklog` | R | expand, issue_id_or_key, max_results, payload, start_at, started_after, started_before |
| `jira_get_remote_issue_link_by_id` | R | issue_id_or_key, link_id, payload |
| `jira_get_remote_issue_links` | R | global_id, issue_id_or_key, payload |
| `jira_get_transitions` | R | expand, include_unavailable_transitions, issue_id_or_key, payload, skip_remote_only_condition, sort_by_ops_bar_and_status, transition_id |
| `jira_get_votes` | R | issue_id_or_key, payload |
| `jira_get_worklog` | R | expand, id_, issue_id_or_key, payload |
| `jira_get_worklog_property` | R | issue_id_or_key, payload, property_key, worklog_id |
| `jira_get_worklog_property_keys` | R | issue_id_or_key, payload, worklog_id |
| `jira_get_worklogs_by_issue_id_and_worklog_id` | W | payload |
| `jira_get_worklogs_for_ids` | W | expand, payload |
| `jira_link_issues` | W | payload |
| `jira_match_issues` | W | payload |
| `jira_parse_jql_queries` | W | payload, validation |
| `jira_put_forge_app_property` | W | payload, property_key |
| `jira_remove_attachment` | D | confirm, id_, payload |
| `jira_remove_vote` | D | confirm, issue_id_or_key, payload |
| `jira_remove_watcher` | D | account_id, confirm, issue_id_or_key, payload, username |
| `jira_sanitise_jql_queries` | W | payload |
| `jira_search` | R | max_results, payload, project_id, search_string, start_at, status_category |
| `jira_search_and_reconsile_issues_using_jql` | R | expand, fields, fields_by_keys, jql, max_results, next_page_token, payload, properties |
| `jira_search_and_reconsile_issues_using_jql_post` | W | payload |
| `jira_search_for_issues_using_jql` | R | expand, fields, fields_by_keys, jql, max_results, payload, properties, start_at |
| `jira_search_for_issues_using_jql_post` | W | payload |
| `jira_set_application_property` | W | id_, payload |
| `jira_set_comment_property` | W | comment_id, payload, property_key |
| `jira_set_issue_property` | W | issue_id_or_key, payload, property_key |
| `jira_set_worklog_property` | W | issue_id_or_key, payload, property_key, worklog_id |
| `jira_submit_bulk_delete` | D | confirm, payload |
| `jira_submit_bulk_edit` | W | payload |
| `jira_submit_bulk_move` | W | payload |
| `jira_submit_bulk_transition` | W | payload |
| `jira_submit_bulk_unwatch` | W | payload |
| `jira_submit_bulk_watch` | W | payload |
| `jira_unarchive_issues` | W | payload |
| `jira_update_comment` | W | expand, id_, issue_id_or_key, notify_users, override_editable_flag, payload |
| `jira_update_remote_issue_link` | W | issue_id_or_key, link_id, payload |
| `jira_update_worklog` | W | adjust_estimate, expand, id_, issue_id_or_key, new_estimate, notify_users, override_editable_flag, payload |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `jira-issues-application-property`: `jira_get_application_property` -> `jira_set_application_property`
- `jira-issues-attachment`: `jira_get_attachment` -> `jira_add_attachment` -> `jira_remove_attachment`
- `jira-issues-comment`: `jira_get_comment` -> `jira_get_comments` -> `jira_add_comment` -> `jira_update_comment` -> `jira_delete_comment`
- `jira-issues-comment-property`: `jira_get_comment_property` -> `jira_get_comment_property_keys` -> `jira_set_comment_property` -> `jira_delete_comment_property`
- `jira-issues-forge-app`: `jira_get_forge_app_property` -> `jira_get_forge_app_property_keys` -> `jira_put_forge_app_property` -> `jira_delete_forge_app_property`
- `jira-issues-ids-worklog`: `jira_get_ids_of_worklogs_deleted_since` -> `jira_get_ids_of_worklogs_modified_since`
- `jira-issues-issue`: `jira_count_issues` -> `jira_get_issue` -> `jira_create_issue` -> `jira_create_issues` -> `jira_link_issues` -> `jira_match_issues` -> `jira_archive_issues` -> `jira_assign_issue` -> `jira_edit_issue` -> `jira_delete_issue` -> `jira_unarchive_issues`
- `jira-issues-issue-link`: `jira_get_issue_link` -> `jira_delete_issue_link`
- `jira-issues-issue-property`: `jira_get_issue_property` -> `jira_get_issue_property_keys` -> `jira_set_issue_property` -> `jira_delete_issue_property`
- `jira-issues-issue-using`: `jira_search_for_issues_using_jql` -> `jira_search_for_issues_using_jql_post`
- `jira-issues-jql-query`: `jira_parse_jql_queries` -> `jira_sanitise_jql_queries`
- `jira-issues-property-resource`: `jira_addon_properties_resource_delete_addon_property_delete` -> `jira_addon_properties_resource_get_addon_property_get` -> `jira_addon_properties_resource_put_addon_property_put`
- `jira-issues-reconsile-issue`: `jira_search_and_reconsile_issues_using_jql` -> `jira_search_and_reconsile_issues_using_jql_post`
- `jira-issues-remote-issue`: `jira_get_remote_issue_link_by_id` -> `jira_get_remote_issue_links` -> `jira_update_remote_issue_link` -> `jira_delete_remote_issue_link_by_global_id` -> `jira_delete_remote_issue_link_by_id`
- `jira-issues-set-issue`: `jira_bulk_set_issue_properties_by_issue` -> `jira_bulk_set_issue_property` -> `jira_bulk_set_issues_properties_list`
- `jira-issues-transition`: `jira_get_transitions` -> `jira_do_transition`
- `jira-issues-vote`: `jira_get_votes` -> `jira_add_vote` -> `jira_remove_vote`
- `jira-issues-watcher`: `jira_add_watcher` -> `jira_remove_watcher`
- `jira-issues-worklog`: `jira_get_worklog` -> `jira_add_worklog` -> `jira_update_worklog` -> `jira_delete_worklog`
- `jira-issues-worklog-property`: `jira_get_worklog_property` -> `jira_get_worklog_property_keys` -> `jira_set_worklog_property` -> `jira_delete_worklog_property`
- `jira-issues-read-records-1`: `jira_expand_attachment_for_humans` -> `jira_expand_attachment_for_machines` -> `jira_get_all_labels` -> `jira_get_approximate_application_license_count` -> `jira_get_approximate_license_count` -> `jira_get_attachment_content` -> `jira_get_attachment_meta` -> `jira_get_attachment_thumbnail` -> `jira_get_available_transitions` -> `jira_get_bulk_operation_progress` -> `jira_get_create_issue_meta` -> `jira_get_edit_issue_meta`
- `jira-issues-read-records-2`: `jira_get_issue_all_types` -> `jira_get_issue_limit_report` -> `jira_get_issue_picker_resource` -> `jira_get_issue_watchers` -> `jira_get_issue_worklog` -> `jira_search`
- `jira-issues-change-records-1`: `jira_get_bulk_changelogs` -> `jira_get_comments_by_ids` -> `jira_get_is_watching_issue_bulk` -> `jira_get_worklogs_by_issue_id_and_worklog_id` -> `jira_get_worklogs_for_ids` -> `jira_create_or_update_remote_issue_link` -> `jira_export_archived_issues` -> `jira_submit_bulk_delete` -> `jira_submit_bulk_edit` -> `jira_submit_bulk_move` -> `jira_submit_bulk_transition` -> `jira_submit_bulk_unwatch`
- `jira-issues-change-records-2`: `jira_submit_bulk_watch` -> `jira_archive_issues_async` -> `jira_bulk_delete_issue_property` -> `jira_bulk_delete_worklogs` -> `jira_bulk_fetch_issues` -> `jira_bulk_move_worklogs`
