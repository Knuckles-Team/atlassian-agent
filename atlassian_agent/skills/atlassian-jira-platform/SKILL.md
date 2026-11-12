---
name: atlassian-jira-platform
skill_type: skill
description: >-
  Jira platform services: app and add-on properties, Forge and Connect
  migration, webhooks, long-running tasks, labels, server info, expressions,
  announcements and other site-level operations. Use when the agent must manage
  apps or site-level services. Do NOT use for issue or project work.
license: MIT
tags: [atlassian, jira, platform, webhooks, forge]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Jira platform: apps, webhooks, tasks, labels and migration

Typed site-level operations, including ones that act on installed apps.

## When to use
- Read and write app properties.
- Register, list or delete webhooks.
- Poll or cancel a long-running task.
- Evaluate a Jira expression; read server info.

## When NOT to use
- Issues and projects: use the Jira issue and project skills.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (60)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `jira_add_atlassian_team` | W | payload, plan_id |
| `jira_addon_properties_resource_get_addon_properties_get` | R | addon_key, payload |
| `jira_analyse_expression` | W | check, payload |
| `jira_cancel_task` | W | payload, task_id |
| `jira_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get` | R | connect_key, jira_issue_fields_key, payload |
| `jira_connect_to_forge_migration_task_submission_resource_submit_task_post` | W | connect_key, jira_issue_fields_key, payload |
| `jira_create_associations` | W | payload |
| `jira_create_related_work` | W | id_, payload |
| `jira_delete_related_work` | D | confirm, payload, related_work_id, version_id |
| `jira_delete_webhook_by_id` | D | confirm, payload |
| `jira_dynamic_modules_resource_get_modules_get` | R | payload |
| `jira_dynamic_modules_resource_register_modules_post` | W | payload |
| `jira_dynamic_modules_resource_remove_modules_delete` | D | confirm, module_key, payload |
| `jira_evaluate_jira_expression` | W | expand, payload |
| `jira_evaluate_jsis_jira_expression` | W | expand, payload |
| `jira_get_advanced_settings` | R | payload |
| `jira_get_atlassian_team` | R | atlassian_team_id, payload, plan_id |
| `jira_get_audit_records` | R | filter, from_, limit, offset, payload, to |
| `jira_get_auto_complete` | R | payload |
| `jira_get_auto_complete_post` | W | payload |
| `jira_get_banner` | R | payload |
| `jira_get_change_logs` | R | issue_id_or_key, max_results, payload, start_at |
| `jira_get_change_logs_by_ids` | W | issue_id_or_key, payload |
| `jira_get_columns` | R | id_, payload |
| `jira_get_dynamic_webhooks_for_app` | R | max_results, payload, start_at |
| `jira_get_events` | R | payload |
| `jira_get_failed_webhooks` | R | after, max_results, payload |
| `jira_get_hierarchy` | R | payload, project_id |
| `jira_get_license` | R | payload |
| `jira_get_locale` | R | payload |
| `jira_get_policies` | R | ids, payload |
| `jira_get_policy` | R | payload |
| `jira_get_precomputations` | R | function_key, max_results, order_by, payload, start_at |
| `jira_get_precomputations_by_id` | W | order_by, payload |
| `jira_get_preference` | R | key, payload |
| `jira_get_recent` | R | expand, payload, properties |
| `jira_get_related_work` | R | id_, payload |
| `jira_get_server_info` | R | payload |
| `jira_get_task` | R | payload, task_id |
| `jira_get_teams` | R | cursor, max_results, payload, plan_id |
| `jira_migrate_queries` | W | payload |
| `jira_migration_resource_update_entity_properties_value_put` | W | atlassian_transfer_id, entity_type, payload |
| `jira_notify` | W | issue_id_or_key, payload |
| `jira_redact` | W | payload |
| `jira_refresh_webhooks` | W | payload |
| `jira_register_dynamic_webhooks` | W | payload |
| `jira_remove_associations` | D | confirm, payload |
| `jira_remove_atlassian_team` | D | atlassian_team_id, confirm, payload, plan_id |
| `jira_remove_level` | D | confirm, level_id, payload, replace_with, scheme_id |
| `jira_remove_preference` | D | confirm, key, payload |
| `jira_reset_columns` | D | confirm, id_, payload |
| `jira_restore` | W | payload, project_id_or_key |
| `jira_service_registry_resource_services_get` | R | payload, service_ids |
| `jira_set_banner` | W | payload |
| `jira_set_columns` | W | id_, payload |
| `jira_set_locale` | W | payload |
| `jira_set_preference` | W | key, payload |
| `jira_update_atlassian_team` | W | atlassian_team_id, payload, plan_id |
| `jira_update_precomputations` | W | payload, skip_not_found_precomputations |
| `jira_update_related_work` | W | id_, payload |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `jira-platform-association`: `jira_create_associations` -> `jira_remove_associations`
- `jira-platform-atlassian-team`: `jira_get_atlassian_team` -> `jira_add_atlassian_team` -> `jira_update_atlassian_team` -> `jira_remove_atlassian_team`
- `jira-platform-auto-complete`: `jira_get_auto_complete` -> `jira_get_auto_complete_post`
- `jira-platform-banner`: `jira_get_banner` -> `jira_set_banner`
- `jira-platform-change-log`: `jira_get_change_logs` -> `jira_get_change_logs_by_ids`
- `jira-platform-column`: `jira_get_columns` -> `jira_reset_columns` -> `jira_set_columns`
- `jira-platform-dynamic-webhook`: `jira_get_dynamic_webhooks_for_app` -> `jira_register_dynamic_webhooks`
- `jira-platform-forge-migration`: `jira_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get` -> `jira_connect_to_forge_migration_task_submission_resource_submit_task_post`
- `jira-platform-locale`: `jira_get_locale` -> `jira_set_locale`
- `jira-platform-module-resource`: `jira_dynamic_modules_resource_get_modules_get` -> `jira_dynamic_modules_resource_register_modules_post` -> `jira_dynamic_modules_resource_remove_modules_delete`
- `jira-platform-policy`: `jira_get_policies` -> `jira_get_policy`
- `jira-platform-precomputation`: `jira_get_precomputations` -> `jira_update_precomputations`
- `jira-platform-preference`: `jira_get_preference` -> `jira_set_preference` -> `jira_remove_preference`
- `jira-platform-related-work`: `jira_get_related_work` -> `jira_create_related_work` -> `jira_update_related_work` -> `jira_delete_related_work`
- `jira-platform-task`: `jira_get_task` -> `jira_cancel_task`
- `jira-platform-read-records`: `jira_addon_properties_resource_get_addon_properties_get` -> `jira_get_advanced_settings` -> `jira_get_audit_records` -> `jira_get_events` -> `jira_get_failed_webhooks` -> `jira_get_hierarchy` -> `jira_get_license` -> `jira_get_recent` -> `jira_get_server_info` -> `jira_get_teams` -> `jira_service_registry_resource_services_get`
- `jira-platform-change-records`: `jira_analyse_expression` -> `jira_evaluate_jira_expression` -> `jira_evaluate_jsis_jira_expression` -> `jira_get_precomputations_by_id` -> `jira_migrate_queries` -> `jira_migration_resource_update_entity_properties_value_put` -> `jira_notify` -> `jira_redact` -> `jira_refresh_webhooks` -> `jira_restore` -> `jira_delete_webhook_by_id` -> `jira_remove_level`
