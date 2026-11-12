---
name: atlassian-jira-configuration
skill_type: skill
description: >-
  Jira instance configuration: workflows and their statuses, custom fields and
  contexts, screens, issue types and type schemes, priorities, resolutions,
  notification, permission and security schemes. Use when the agent must inspect
  or change how Jira is configured. Do NOT use for issue content (use atlassian-
  jira-issues).
license: MIT
tags: [atlassian, jira, configuration, workflows, fields]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Jira configuration: workflows, fields, screens and schemes

Typed configuration operations. Scheme and workflow changes affect every project that uses them: read the usage first and ask for approval before changing or deleting.

## When to use
- Inspect workflows, statuses and transitions.
- Create or update custom fields, contexts and options.
- Manage screens, screen tabs and screen schemes.
- Manage issue types, priorities, resolutions and schemes, and assign schemes to projects.

## When NOT to use
- Issue content: use atlassian-jira-issues.
- Users and groups: use atlassian-jira-people-access.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (298)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `jira_add_field_to_default_screen` | W | field_id, payload |
| `jira_add_issue_types_to_context` | W | context_id, field_id, payload |
| `jira_add_issue_types_to_issue_type_scheme` | W | issue_type_scheme_id, payload |
| `jira_add_notifications` | W | id_, payload |
| `jira_add_screen_tab` | W | payload, screen_id |
| `jira_add_screen_tab_field` | W | payload, screen_id, tab_id |
| `jira_add_security_level` | W | payload, scheme_id |
| `jira_add_security_level_members` | W | level_id, payload, scheme_id |
| `jira_app_issue_field_value_update_resource_update_issue_fields_put` | W | atlassian_transfer_id, payload |
| `jira_append_mappings_for_issue_type_screen_scheme` | W | issue_type_screen_scheme_id, payload |
| `jira_assign_field_configuration_scheme_to_project` | W | payload |
| `jira_assign_issue_type_scheme_to_project` | W | payload |
| `jira_assign_issue_type_screen_scheme_to_project` | W | payload |
| `jira_assign_permission_scheme` | W | expand, payload, project_key_or_id |
| `jira_assign_projects_to_custom_field_context` | W | context_id, field_id, payload |
| `jira_assign_scheme_to_project` | W | payload |
| `jira_associate_projects_to_field_association_schemes` | W | payload |
| `jira_associate_schemes_to_projects` | W | payload |
| `jira_clone_field_association_scheme` | W | id_, payload |
| `jira_create_custom_field` | W | payload |
| `jira_create_custom_field_context` | W | field_id, payload |
| `jira_create_custom_field_option` | W | context_id, field_id, payload |
| `jira_create_field_association_scheme` | W | payload |
| `jira_create_field_configuration` | W | payload |
| `jira_create_field_configuration_scheme` | W | payload |
| `jira_create_issue_field_option` | W | field_key, payload |
| `jira_create_issue_link_type` | W | payload |
| `jira_create_issue_security_scheme` | W | payload |
| `jira_create_issue_type` | W | payload |
| `jira_create_issue_type_avatar` | W | id_, payload, size, x, y |
| `jira_create_issue_type_scheme` | W | payload |
| `jira_create_issue_type_screen_scheme` | W | payload |
| `jira_create_notification_scheme` | W | payload |
| `jira_create_permission_scheme` | W | expand, payload |
| `jira_create_priority` | W | payload |
| `jira_create_priority_scheme` | W | payload |
| `jira_create_project_with_custom_template` | W | payload |
| `jira_create_resolution` | W | payload |
| `jira_create_screen` | W | payload |
| `jira_create_screen_scheme` | W | payload |
| `jira_create_statuses` | W | payload |
| `jira_create_ui_modification` | W | payload |
| `jira_create_workflow` | W | payload |
| `jira_create_workflow_scheme` | W | payload |
| `jira_create_workflow_scheme_draft_from_parent` | W | id_, payload |
| `jira_create_workflow_transition_property` | W | key, payload, transition_id, workflow_mode, workflow_name |
| `jira_create_workflows` | W | payload |
| `jira_delete_custom_field` | D | confirm, id_, payload |
| `jira_delete_custom_field_context` | D | confirm, context_id, field_id, payload |
| `jira_delete_custom_field_option` | D | confirm, context_id, field_id, option_id, payload |
| `jira_delete_default_workflow` | D | confirm, id_, payload, update_draft_if_needed |
| `jira_delete_draft_default_workflow` | D | confirm, id_, payload |
| `jira_delete_draft_workflow_mapping` | D | confirm, id_, payload, workflow_name |
| `jira_delete_field_association_scheme` | D | confirm, id_, payload |
| `jira_delete_field_configuration` | D | confirm, id_, payload |
| `jira_delete_field_configuration_scheme` | D | confirm, id_, payload |
| `jira_delete_inactive_workflow` | D | confirm, entity_id, payload |
| `jira_delete_issue_field_option` | D | confirm, field_key, option_id, payload |
| `jira_delete_issue_link_type` | D | confirm, issue_link_type_id, payload |
| `jira_delete_issue_type` | D | alternative_issue_type_id, confirm, id_, payload |
| `jira_delete_issue_type_property` | D | confirm, issue_type_id, payload, property_key |
| `jira_delete_issue_type_scheme` | D | confirm, issue_type_scheme_id, payload |
| `jira_delete_issue_type_screen_scheme` | D | confirm, issue_type_screen_scheme_id, payload |
| `jira_delete_notification_scheme` | D | confirm, notification_scheme_id, payload |
| `jira_delete_permission_scheme` | D | confirm, payload, scheme_id |
| `jira_delete_permission_scheme_entity` | D | confirm, payload, permission_id, scheme_id |
| `jira_delete_priority` | D | confirm, id_, payload |
| `jira_delete_priority_scheme` | D | confirm, payload, scheme_id |
| `jira_delete_resolution` | D | confirm, id_, payload, replace_with |
| `jira_delete_screen` | D | confirm, payload, screen_id |
| `jira_delete_screen_scheme` | D | confirm, payload, screen_scheme_id |
| `jira_delete_screen_tab` | D | confirm, payload, screen_id, tab_id |
| `jira_delete_security_scheme` | D | confirm, payload, scheme_id |
| `jira_delete_statuses_by_id` | D | confirm, id_, payload |
| `jira_delete_ui_modification` | D | confirm, payload, ui_modification_id |
| `jira_delete_workflow_mapping` | D | confirm, id_, payload, update_draft_if_needed, workflow_name |
| `jira_delete_workflow_scheme` | D | confirm, id_, payload |
| `jira_delete_workflow_scheme_draft` | D | confirm, id_, payload |
| `jira_delete_workflow_scheme_draft_issue_type` | D | confirm, id_, issue_type, payload |
| `jira_delete_workflow_scheme_issue_type` | D | confirm, id_, issue_type, payload, update_draft_if_needed |
| `jira_delete_workflow_transition_property` | D | confirm, key, payload, transition_id, workflow_mode, workflow_name |
| `jira_delete_workflow_transition_rule_configurations` | D | confirm, payload |
| `jira_edit_template` | W | payload |
| `jira_get_all_field_configuration_schemes` | R | id_, max_results, payload, start_at |
| `jira_get_all_field_configurations` | R | id_, is_default, max_results, payload, query, start_at |
| `jira_get_all_issue_field_options` | R | field_key, max_results, payload, start_at |
| `jira_get_all_issue_type_schemes` | R | expand, id_, max_results, order_by, payload, query_string, start_at |
| `jira_get_all_permission_schemes` | R | expand, payload |
| `jira_get_all_screen_tab_fields` | R | payload, project_key, screen_id, tab_id |
| `jira_get_all_screen_tabs` | R | payload, project_key, screen_id |
| `jira_get_all_statuses` | R | payload, project_id_or_key |
| `jira_get_all_users_default` | R | expand, max_results, payload, start_at |
| `jira_get_all_workflow_schemes` | R | max_results, payload, start_at |
| `jira_get_all_workflows` | R | payload, workflow_name |
| `jira_get_alternative_issue_types` | R | id_, payload |
| `jira_get_assigned_permission_scheme` | R | expand, payload, project_key_or_id |
| `jira_get_available_priorities_by_priority_scheme` | R | exclude, max_results, payload, query, scheme_id, start_at |
| `jira_get_available_screen_fields` | R | payload, screen_id |
| `jira_get_available_time_tracking_implementations` | R | payload |
| `jira_get_bulk_editable_fields` | R | ending_before, issue_ids_or_keys, payload, search_text, starting_after |
| `jira_get_bulk_screen_tabs` | R | max_result, payload, screen_id, start_at, tab_id |
| `jira_get_configuration` | R | payload |
| `jira_get_contexts_for_field` | R | context_id, field_id, is_any_issue_type, is_global_context, max_results, payload, start_at |
| `jira_get_contexts_for_field_deprecated` | R | field_id, max_results, payload, start_at |
| `jira_get_create_issue_meta_issue_type_id` | R | issue_type_id, max_results, payload, project_id_or_key, start_at |
| `jira_get_create_issue_meta_issue_types` | R | max_results, payload, project_id_or_key, start_at |
| `jira_get_custom_field_configuration` | R | field_context_id, field_id_or_key, id_, issue_id, issue_type_id, max_results, payload, project_key_or_id |
| `jira_get_custom_field_contexts_for_projects_and_issue_types` | W | field_id, max_results, payload, start_at |
| `jira_get_custom_field_option` | R | id_, payload |
| `jira_get_custom_fields_configurations` | W | field_context_id, id_, issue_id, issue_type_id, max_results, payload, project_key_or_id, start_at |
| `jira_get_default_editor` | R | payload |
| `jira_get_default_project_classification` | R | payload, project_id_or_key |
| `jira_get_default_share_scope` | R | payload |
| `jira_get_default_values` | R | context_id, field_id, max_results, payload, start_at |
| `jira_get_default_workflow` | R | id_, payload, return_draft_if_exists |
| `jira_get_draft_default_workflow` | R | id_, payload |
| `jira_get_draft_workflow` | R | id_, payload, workflow_name |
| `jira_get_field_association_scheme_by_id` | R | id_, payload |
| `jira_get_field_association_scheme_item_parameters` | R | field_id, id_, payload |
| `jira_get_field_association_schemes` | R | max_results, payload, project_id, query, start_at |
| `jira_get_field_auto_complete_for_query_string` | R | field_name, field_value, payload, predicate_name, predicate_value |
| `jira_get_field_configuration_items` | R | id_, max_results, payload, start_at |
| `jira_get_field_configuration_scheme_mappings` | R | field_configuration_scheme_id, max_results, payload, start_at |
| `jira_get_field_configuration_scheme_project_mapping` | R | max_results, payload, project_id, start_at |
| `jira_get_field_project_associations` | R | field_id, max_results, payload, start_at |
| `jira_get_fields` | R | payload |
| `jira_get_fields_paginated` | R | expand, id_, max_results, order_by, payload, project_ids, query, start_at |
| `jira_get_issue_field_option` | R | field_key, option_id, payload |
| `jira_get_issue_link_type` | R | issue_link_type_id, payload |
| `jira_get_issue_link_types` | R | payload |
| `jira_get_issue_navigator_default_columns` | R | payload |
| `jira_get_issue_security_level` | R | id_, payload |
| `jira_get_issue_security_level_members` | R | expand, issue_security_level_id, issue_security_scheme_id, max_results, payload, start_at |
| `jira_get_issue_security_scheme` | R | id_, payload |
| `jira_get_issue_security_schemes` | R | payload |
| `jira_get_issue_type` | R | id_, payload |
| `jira_get_issue_type_mappings_for_contexts` | R | context_id, field_id, max_results, payload, start_at |
| `jira_get_issue_type_property` | R | issue_type_id, payload, property_key |
| `jira_get_issue_type_property_keys` | R | issue_type_id, payload |
| `jira_get_issue_type_scheme_for_projects` | R | max_results, payload, project_id, start_at |
| `jira_get_issue_type_schemes_mapping` | R | issue_type_scheme_id, max_results, payload, start_at |
| `jira_get_issue_type_screen_scheme_mappings` | R | issue_type_screen_scheme_id, max_results, payload, start_at |
| `jira_get_issue_type_screen_scheme_project_associations` | R | max_results, payload, project_id, start_at |
| `jira_get_issue_type_screen_schemes` | R | expand, id_, max_results, order_by, payload, query_string, start_at |
| `jira_get_issue_types_for_project` | R | level, payload, project_id |
| `jira_get_notification_scheme` | R | expand, id_, payload |
| `jira_get_notification_scheme_for_project` | R | expand, payload, project_key_or_id |
| `jira_get_notification_scheme_to_project_mappings` | R | max_results, notification_scheme_id, payload, project_id, start_at |
| `jira_get_notification_schemes` | R | expand, id_, max_results, only_default, payload, project_id, start_at |
| `jira_get_options_for_context` | R | context_id, field_id, max_results, only_options, option_id, payload, start_at |
| `jira_get_permission_scheme` | R | expand, payload, scheme_id |
| `jira_get_permission_scheme_grant` | R | expand, payload, permission_id, scheme_id |
| `jira_get_permission_scheme_grants` | R | expand, payload, scheme_id |
| `jira_get_priorities` | R | payload |
| `jira_get_priorities_by_priority_scheme` | R | max_results, payload, scheme_id, start_at |
| `jira_get_priority` | R | id_, payload |
| `jira_get_priority_schemes` | R | expand, max_results, only_default, order_by, payload, priority_id, scheme_id, scheme_name |
| `jira_get_project_context_mapping` | R | context_id, field_id, max_results, payload, start_at |
| `jira_get_project_fields` | R | field_id, max_results, payload, project_id, start_at, work_type_id |
| `jira_get_project_issue_security_scheme` | R | payload, project_key_or_id |
| `jira_get_project_issue_type_usages_for_status` | R | max_results, next_page_token, payload, project_id, status_id |
| `jira_get_project_usages_for_status` | R | max_results, next_page_token, payload, status_id |
| `jira_get_project_usages_for_workflow` | R | max_results, next_page_token, payload, workflow_id |
| `jira_get_project_usages_for_workflow_scheme` | R | max_results, next_page_token, payload, workflow_scheme_id |
| `jira_get_projects_by_priority_scheme` | R | max_results, payload, project_id, query, scheme_id, start_at |
| `jira_get_projects_for_issue_type_screen_scheme` | R | issue_type_screen_scheme_id, max_results, payload, query, start_at |
| `jira_get_projects_with_field_schemes` | R | max_results, payload, project_id, start_at |
| `jira_get_redaction_status` | R | job_id, payload |
| `jira_get_required_workflow_scheme_mappings` | W | payload |
| `jira_get_resolution` | R | id_, payload |
| `jira_get_resolutions` | R | payload |
| `jira_get_screen_schemes` | R | expand, id_, max_results, order_by, payload, query_string, start_at |
| `jira_get_screens` | R | id_, max_results, order_by, payload, query_string, scope, start_at |
| `jira_get_screens_for_field` | R | expand, field_id, max_results, payload, start_at |
| `jira_get_security_level_members` | R | expand, id_, level_id, max_results, payload, scheme_id, start_at |
| `jira_get_security_levels` | R | id_, max_results, only_default, payload, scheme_id, start_at |
| `jira_get_security_levels_for_project` | R | payload, project_key_or_id |
| `jira_get_selectable_issue_field_options` | R | field_key, max_results, payload, project_id, start_at |
| `jira_get_selected_time_tracking_implementation` | R | payload |
| `jira_get_shared_time_tracking_configuration` | R | payload |
| `jira_get_status` | R | id_or_name, payload |
| `jira_get_status_categories` | R | payload |
| `jira_get_status_category` | R | id_or_key, payload |
| `jira_get_statuses` | R | payload |
| `jira_get_statuses_by_id` | R | id_, payload |
| `jira_get_statuses_by_name` | R | name, payload, project_id |
| `jira_get_trashed_fields_paginated` | R | expand, id_, max_results, order_by, payload, query, start_at |
| `jira_get_ui_modifications` | R | expand, max_results, payload, start_at |
| `jira_get_user_default_columns` | R | account_id, payload, username |
| `jira_get_visible_issue_field_options` | R | field_key, max_results, payload, project_id, start_at |
| `jira_get_workflow` | R | id_, payload, return_draft_if_exists, workflow_name |
| `jira_get_workflow_project_issue_type_usages` | R | max_results, next_page_token, payload, project_id, workflow_id |
| `jira_get_workflow_scheme` | R | id_, payload, return_draft_if_exists |
| `jira_get_workflow_scheme_draft` | R | id_, payload |
| `jira_get_workflow_scheme_draft_issue_type` | R | id_, issue_type, payload |
| `jira_get_workflow_scheme_issue_type` | R | id_, issue_type, payload, return_draft_if_exists |
| `jira_get_workflow_scheme_project_associations` | R | payload, project_id |
| `jira_get_workflow_scheme_usages_for_workflow` | R | max_results, next_page_token, payload, workflow_id |
| `jira_get_workflow_transition_properties` | R | include_reserved_keys, key, payload, transition_id, workflow_mode, workflow_name |
| `jira_get_workflow_transition_rule_configurations` | R | draft, expand, keys, max_results, payload, start_at, types, with_tags |
| `jira_get_workflow_usages_for_status` | R | max_results, next_page_token, payload, status_id |
| `jira_get_workflows_paginated` | R | expand, is_active, max_results, order_by, payload, query_string, start_at, workflow_name |
| `jira_list_workflow_history` | W | expand, payload |
| `jira_live_template` | R | payload, project_id, template_key |
| `jira_migration_resource_workflow_rule_search_post` | W | atlassian_transfer_id, payload |
| `jira_move_priorities` | W | payload |
| `jira_move_resolutions` | W | payload |
| `jira_move_screen_tab` | W | payload, pos, screen_id, tab_id |
| `jira_move_screen_tab_field` | W | id_, payload, screen_id, tab_id |
| `jira_publish_draft_workflow_scheme` | W | id_, payload, validate_only |
| `jira_read_workflow_from_history` | W | payload |
| `jira_read_workflow_previews` | W | payload |
| `jira_read_workflow_schemes` | W | payload |
| `jira_read_workflows` | W | payload |
| `jira_remove_custom_field_context_from_projects` | D | confirm, context_id, field_id, payload |
| `jira_remove_default_project_classification` | D | confirm, payload, project_id_or_key |
| `jira_remove_field_association_scheme_item_parameters` | D | confirm, payload |
| `jira_remove_fields_associated_with_schemes` | D | confirm, payload |
| `jira_remove_issue_type_from_issue_type_scheme` | D | confirm, issue_type_id, issue_type_scheme_id, payload |
| `jira_remove_issue_types_from_context` | D | confirm, context_id, field_id, payload |
| `jira_remove_issue_types_from_global_field_configuration_scheme` | D | confirm, id_, payload |
| `jira_remove_mappings_from_issue_type_screen_scheme` | D | confirm, issue_type_screen_scheme_id, payload |
| `jira_remove_member_from_security_level` | D | confirm, level_id, member_id, payload, scheme_id |
| `jira_remove_notification_from_notification_scheme` | D | confirm, notification_id, notification_scheme_id, payload |
| `jira_remove_screen_tab_field` | D | confirm, id_, payload, screen_id, tab_id |
| `jira_remove_template` | D | confirm, payload, template_key |
| `jira_rename_screen_tab` | W | payload, screen_id, tab_id |
| `jira_reorder_custom_field_options` | W | context_id, field_id, payload |
| `jira_reorder_issue_types_in_issue_type_scheme` | W | issue_type_scheme_id, payload |
| `jira_replace_custom_field_option` | D | confirm, context_id, field_id, jql, option_id, payload, replace_with |
| `jira_replace_issue_field_option` | D | confirm, field_key, jql, option_id, override_editable_flag, override_screen_security, payload, replace_with |
| `jira_restore_custom_field` | W | id_, payload |
| `jira_save_template` | W | payload |
| `jira_search_field_association_scheme_fields` | R | field_id, id_, max_results, payload, start_at |
| `jira_search_field_association_scheme_projects` | R | id_, max_results, payload, project_id, start_at |
| `jira_search_priorities` | R | expand, id_, max_results, only_default, payload, priority_name, project_id, start_at |
| `jira_search_projects_using_security_schemes` | R | issue_security_scheme_id, max_results, payload, project_id, start_at |
| `jira_search_resolutions` | R | id_, max_results, only_default, payload, start_at |
| `jira_search_security_schemes` | R | id_, max_results, payload, project_id, start_at |
| `jira_search_workflows` | R | expand, is_active, max_results, order_by, payload, query_string, scope, start_at |
| `jira_select_time_tracking_implementation` | W | payload |
| `jira_set_default_levels` | W | payload |
| `jira_set_default_priority` | W | payload |
| `jira_set_default_resolution` | W | payload |
| `jira_set_default_share_scope` | W | payload |
| `jira_set_default_values` | W | field_id, payload |
| `jira_set_field_configuration_scheme_mapping` | W | id_, payload |
| `jira_set_issue_navigator_default_columns` | W | payload |
| `jira_set_issue_type_property` | W | issue_type_id, payload, property_key |
| `jira_set_shared_time_tracking_configuration` | W | payload |
| `jira_set_workflow_scheme_draft_issue_type` | W | id_, issue_type, payload |
| `jira_set_workflow_scheme_issue_type` | W | id_, issue_type, payload |
| `jira_suggested_priorities_for_mappings` | W | payload |
| `jira_switch_workflow_scheme_for_project` | W | payload |
| `jira_trash_custom_field` | W | id_, payload |
| `jira_update_custom_field` | W | field_id, payload |
| `jira_update_custom_field_configuration` | W | field_id_or_key, payload |
| `jira_update_custom_field_context` | W | context_id, field_id, payload |
| `jira_update_custom_field_option` | W | context_id, field_id, payload |
| `jira_update_custom_field_value` | W | field_id_or_key, generate_changelog, payload |
| `jira_update_default_project_classification` | W | payload, project_id_or_key |
| `jira_update_default_screen_scheme` | W | issue_type_screen_scheme_id, payload |
| `jira_update_default_workflow` | W | id_, payload |
| `jira_update_draft_default_workflow` | W | id_, payload |
| `jira_update_draft_workflow_mapping` | W | id_, payload, workflow_name |
| `jira_update_field_association_scheme` | W | id_, payload |
| `jira_update_field_association_scheme_item_parameters` | W | payload |
| `jira_update_field_configuration` | W | id_, payload |
| `jira_update_field_configuration_items` | W | id_, payload |
| `jira_update_field_configuration_scheme` | W | id_, payload |
| `jira_update_fields_associated_with_schemes` | W | payload |
| `jira_update_issue_field_option` | W | field_key, option_id, payload |
| `jira_update_issue_link_type` | W | issue_link_type_id, payload |
| `jira_update_issue_security_scheme` | W | id_, payload |
| `jira_update_issue_type` | W | id_, payload |
| `jira_update_issue_type_scheme` | W | issue_type_scheme_id, payload |
| `jira_update_issue_type_screen_scheme` | W | issue_type_screen_scheme_id, payload |
| `jira_update_multiple_custom_field_values` | W | generate_changelog, payload |
| `jira_update_notification_scheme` | W | id_, payload |
| `jira_update_permission_scheme` | W | expand, payload, scheme_id |
| `jira_update_priority` | W | id_, payload |
| `jira_update_priority_scheme` | W | payload, scheme_id |
| `jira_update_resolution` | W | id_, payload |
| `jira_update_schemes` | W | payload |
| `jira_update_screen` | W | payload, screen_id |
| `jira_update_screen_scheme` | W | payload, screen_scheme_id |
| `jira_update_security_level` | W | level_id, payload, scheme_id |
| `jira_update_statuses` | W | payload |
| `jira_update_ui_modification` | W | payload, ui_modification_id |
| `jira_update_workflow_mapping` | W | id_, payload, workflow_name |
| `jira_update_workflow_scheme` | W | id_, payload |
| `jira_update_workflow_scheme_draft` | W | id_, payload |
| `jira_update_workflow_transition_property` | W | key, payload, transition_id, workflow_mode, workflow_name |
| `jira_update_workflow_transition_rule_configurations` | W | payload |
| `jira_update_workflows` | W | payload |
| `jira_validate_create_workflows` | W | payload |
| `jira_validate_update_workflows` | W | payload |
| `jira_workflow_capabilities` | R | issue_type_id, payload, project_id, workflow_id |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `jira-configuration-context-field`: `jira_get_contexts_for_field` -> `jira_get_contexts_for_field_deprecated`
- `jira-configuration-create-issue`: `jira_get_create_issue_meta_issue_type_id` -> `jira_get_create_issue_meta_issue_types`
- `jira-configuration-custom-field`: `jira_get_custom_field_configuration` -> `jira_get_custom_field_contexts_for_projects_and_issue_types` -> `jira_get_custom_field_option` -> `jira_get_custom_fields_configurations` -> `jira_create_custom_field` -> `jira_create_custom_field_context` -> `jira_create_custom_field_option` -> `jira_trash_custom_field` -> `jira_reorder_custom_field_options` -> `jira_replace_custom_field_option` -> `jira_restore_custom_field` -> `jira_update_custom_field` -> `jira_update_custom_field_configuration` -> `jira_update_custom_field_context` -> `jira_update_custom_field_option` -> `jira_update_custom_field_value` -> `jira_delete_custom_field` -> `jira_delete_custom_field_context` -> `jira_delete_custom_field_option` -> `jira_remove_custom_field_context_from_projects`
- `jira-configuration-default-project`: `jira_get_default_project_classification` -> `jira_update_default_project_classification` -> `jira_remove_default_project_classification`
- `jira-configuration-default-share`: `jira_get_default_share_scope` -> `jira_set_default_share_scope`
- `jira-configuration-default-value`: `jira_get_default_values` -> `jira_set_default_values`
- `jira-configuration-default-workflow`: `jira_get_default_workflow` -> `jira_update_default_workflow` -> `jira_delete_default_workflow`
- `jira-configuration-draft-default`: `jira_get_draft_default_workflow` -> `jira_update_draft_default_workflow` -> `jira_delete_draft_default_workflow`
- `jira-configuration-draft-workflow`: `jira_get_draft_workflow` -> `jira_publish_draft_workflow_scheme` -> `jira_update_draft_workflow_mapping` -> `jira_delete_draft_workflow_mapping`
- `jira-configuration-field-associated`: `jira_update_fields_associated_with_schemes` -> `jira_remove_fields_associated_with_schemes`
- `jira-configuration-field-association`: `jira_get_field_association_scheme_by_id` -> `jira_get_field_association_scheme_item_parameters` -> `jira_get_field_association_schemes` -> `jira_search_field_association_scheme_fields` -> `jira_search_field_association_scheme_projects` -> `jira_clone_field_association_scheme` -> `jira_create_field_association_scheme` -> `jira_update_field_association_scheme` -> `jira_update_field_association_scheme_item_parameters` -> `jira_delete_field_association_scheme` -> `jira_remove_field_association_scheme_item_parameters`
- `jira-configuration-field-configuration`: `jira_get_all_field_configuration_schemes` -> `jira_get_all_field_configurations` -> `jira_get_field_configuration_items` -> `jira_get_field_configuration_scheme_mappings` -> `jira_get_field_configuration_scheme_project_mapping` -> `jira_create_field_configuration` -> `jira_create_field_configuration_scheme` -> `jira_assign_field_configuration_scheme_to_project` -> `jira_set_field_configuration_scheme_mapping` -> `jira_update_field_configuration` -> `jira_update_field_configuration_items` -> `jira_update_field_configuration_scheme` -> `jira_delete_field_configuration` -> `jira_delete_field_configuration_scheme`
- `jira-configuration-issue-field`: `jira_get_all_issue_field_options` -> `jira_get_issue_field_option` -> `jira_app_issue_field_value_update_resource_update_issue_fields_put` -> `jira_create_issue_field_option` -> `jira_replace_issue_field_option` -> `jira_update_issue_field_option` -> `jira_delete_issue_field_option`
- `jira-configuration-issue-link`: `jira_get_issue_link_type` -> `jira_get_issue_link_types` -> `jira_create_issue_link_type` -> `jira_update_issue_link_type` -> `jira_delete_issue_link_type`
- `jira-configuration-issue-navigator`: `jira_get_issue_navigator_default_columns` -> `jira_set_issue_navigator_default_columns`
- `jira-configuration-issue-security`: `jira_get_issue_security_level` -> `jira_get_issue_security_level_members` -> `jira_get_issue_security_scheme` -> `jira_get_issue_security_schemes` -> `jira_create_issue_security_scheme` -> `jira_update_issue_security_scheme`
- `jira-configuration-issue-type`: `jira_get_all_issue_type_schemes` -> `jira_get_issue_type` -> `jira_get_issue_type_mappings_for_contexts` -> `jira_get_issue_type_property` -> `jira_get_issue_type_property_keys` -> `jira_get_issue_type_scheme_for_projects` -> `jira_get_issue_type_schemes_mapping` -> `jira_get_issue_type_screen_scheme_mappings` -> `jira_get_issue_type_screen_scheme_project_associations` -> `jira_get_issue_type_screen_schemes` -> `jira_get_issue_types_for_project` -> `jira_add_issue_types_to_context` -> `jira_add_issue_types_to_issue_type_scheme` -> `jira_create_issue_type` -> `jira_create_issue_type_avatar` -> `jira_create_issue_type_scheme` -> `jira_create_issue_type_screen_scheme` -> `jira_assign_issue_type_scheme_to_project` -> `jira_assign_issue_type_screen_scheme_to_project` -> `jira_reorder_issue_types_in_issue_type_scheme` -> `jira_set_issue_type_property` -> `jira_update_issue_type` -> `jira_update_issue_type_scheme` -> `jira_update_issue_type_screen_scheme` -> `jira_delete_issue_type` -> `jira_delete_issue_type_property` -> `jira_delete_issue_type_scheme` -> `jira_delete_issue_type_screen_scheme` -> `jira_remove_issue_type_from_issue_type_scheme` -> `jira_remove_issue_types_from_context` -> `jira_remove_issue_types_from_global_field_configuration_scheme`
- `jira-configuration-mapping-issue`: `jira_append_mappings_for_issue_type_screen_scheme` -> `jira_remove_mappings_from_issue_type_screen_scheme`
- `jira-configuration-notification-scheme`: `jira_get_notification_scheme` -> `jira_get_notification_scheme_for_project` -> `jira_get_notification_scheme_to_project_mappings` -> `jira_get_notification_schemes` -> `jira_create_notification_scheme` -> `jira_update_notification_scheme` -> `jira_delete_notification_scheme`
- `jira-configuration-permission-scheme`: `jira_get_all_permission_schemes` -> `jira_get_permission_scheme` -> `jira_get_permission_scheme_grant` -> `jira_get_permission_scheme_grants` -> `jira_create_permission_scheme` -> `jira_assign_permission_scheme` -> `jira_update_permission_scheme` -> `jira_delete_permission_scheme` -> `jira_delete_permission_scheme_entity`
- `jira-configuration-priority`: `jira_get_priorities` -> `jira_get_priority` -> `jira_search_priorities` -> `jira_create_priority` -> `jira_move_priorities` -> `jira_update_priority` -> `jira_delete_priority`
- `jira-configuration-priority-scheme`: `jira_get_priority_schemes` -> `jira_create_priority_scheme` -> `jira_update_priority_scheme` -> `jira_delete_priority_scheme`
- `jira-configuration-project-custom`: `jira_create_project_with_custom_template` -> `jira_assign_projects_to_custom_field_context`
- `jira-configuration-project-field`: `jira_get_project_fields` -> `jira_get_projects_with_field_schemes` -> `jira_associate_projects_to_field_association_schemes`
- `jira-configuration-project-issue`: `jira_get_project_issue_security_scheme` -> `jira_get_project_issue_type_usages_for_status` -> `jira_get_projects_for_issue_type_screen_scheme`
- `jira-configuration-project-usage`: `jira_get_project_usages_for_status` -> `jira_get_project_usages_for_workflow` -> `jira_get_project_usages_for_workflow_scheme`
- `jira-configuration-resolution`: `jira_get_resolution` -> `jira_get_resolutions` -> `jira_search_resolutions` -> `jira_create_resolution` -> `jira_move_resolutions` -> `jira_update_resolution` -> `jira_delete_resolution`
- `jira-configuration-scheme-project`: `jira_assign_scheme_to_project` -> `jira_associate_schemes_to_projects`
- `jira-configuration-screen`: `jira_get_screens` -> `jira_create_screen` -> `jira_update_screen` -> `jira_delete_screen`
- `jira-configuration-screen-scheme`: `jira_get_screen_schemes` -> `jira_create_screen_scheme` -> `jira_update_screen_scheme` -> `jira_delete_screen_scheme`
- `jira-configuration-screen-tab`: `jira_get_all_screen_tab_fields` -> `jira_get_all_screen_tabs` -> `jira_add_screen_tab` -> `jira_add_screen_tab_field` -> `jira_rename_screen_tab` -> `jira_move_screen_tab` -> `jira_move_screen_tab_field` -> `jira_delete_screen_tab` -> `jira_remove_screen_tab_field`
- `jira-configuration-security-level`: `jira_get_security_level_members` -> `jira_get_security_levels` -> `jira_get_security_levels_for_project` -> `jira_add_security_level` -> `jira_add_security_level_members` -> `jira_update_security_level`
- `jira-configuration-security-scheme`: `jira_search_security_schemes` -> `jira_delete_security_scheme`
- `jira-configuration-shared-time`: `jira_get_shared_time_tracking_configuration` -> `jira_set_shared_time_tracking_configuration`
- `jira-configuration-status`: `jira_get_all_statuses` -> `jira_get_status` -> `jira_get_statuses` -> `jira_create_statuses` -> `jira_update_statuses`
- `jira-configuration-status-category`: `jira_get_status_categories` -> `jira_get_status_category`
- `jira-configuration-status-id`: `jira_get_statuses_by_id` -> `jira_delete_statuses_by_id`
- `jira-configuration-template`: `jira_live_template` -> `jira_save_template` -> `jira_edit_template` -> `jira_remove_template`
- `jira-configuration-ui-modification`: `jira_get_ui_modifications` -> `jira_create_ui_modification` -> `jira_update_ui_modification` -> `jira_delete_ui_modification`
- `jira-configuration-user-default`: `jira_get_all_users_default` -> `jira_get_user_default_columns`
- `jira-configuration-workflow`: `jira_get_all_workflows` -> `jira_get_workflow` -> `jira_read_workflows` -> `jira_search_workflows` -> `jira_create_workflow` -> `jira_create_workflows` -> `jira_update_workflows`
- `jira-configuration-workflow-history`: `jira_list_workflow_history` -> `jira_read_workflow_from_history`
- `jira-configuration-workflow-mapping`: `jira_update_workflow_mapping` -> `jira_delete_workflow_mapping`
- `jira-configuration-workflow-scheme`: `jira_get_all_workflow_schemes` -> `jira_get_workflow_scheme` -> `jira_get_workflow_scheme_draft` -> `jira_get_workflow_scheme_draft_issue_type` -> `jira_get_workflow_scheme_issue_type` -> `jira_get_workflow_scheme_project_associations` -> `jira_get_workflow_scheme_usages_for_workflow` -> `jira_read_workflow_schemes` -> `jira_create_workflow_scheme` -> `jira_create_workflow_scheme_draft_from_parent` -> `jira_switch_workflow_scheme_for_project` -> `jira_set_workflow_scheme_draft_issue_type` -> `jira_set_workflow_scheme_issue_type` -> `jira_update_workflow_scheme` -> `jira_update_workflow_scheme_draft` -> `jira_delete_workflow_scheme` -> `jira_delete_workflow_scheme_draft` -> `jira_delete_workflow_scheme_draft_issue_type` -> `jira_delete_workflow_scheme_issue_type`
- `jira-configuration-workflow-transition`: `jira_get_workflow_transition_properties` -> `jira_get_workflow_transition_rule_configurations` -> `jira_create_workflow_transition_property` -> `jira_update_workflow_transition_property` -> `jira_update_workflow_transition_rule_configurations` -> `jira_delete_workflow_transition_property` -> `jira_delete_workflow_transition_rule_configurations`
- `jira-configuration-read-records-1`: `jira_get_alternative_issue_types` -> `jira_get_assigned_permission_scheme` -> `jira_get_available_priorities_by_priority_scheme` -> `jira_get_available_screen_fields` -> `jira_get_available_time_tracking_implementations` -> `jira_get_bulk_editable_fields` -> `jira_get_bulk_screen_tabs` -> `jira_get_configuration` -> `jira_get_default_editor` -> `jira_get_field_auto_complete_for_query_string` -> `jira_get_field_project_associations` -> `jira_get_fields`
- `jira-configuration-read-records-2`: `jira_get_fields_paginated` -> `jira_get_options_for_context` -> `jira_get_priorities_by_priority_scheme` -> `jira_get_project_context_mapping` -> `jira_get_projects_by_priority_scheme` -> `jira_get_redaction_status` -> `jira_get_screens_for_field` -> `jira_get_selectable_issue_field_options` -> `jira_get_selected_time_tracking_implementation` -> `jira_get_statuses_by_name` -> `jira_get_trashed_fields_paginated` -> `jira_get_visible_issue_field_options`
- `jira-configuration-read-records-3`: `jira_get_workflow_project_issue_type_usages` -> `jira_get_workflow_usages_for_status` -> `jira_get_workflows_paginated` -> `jira_search_projects_using_security_schemes` -> `jira_workflow_capabilities`
- `jira-configuration-change-records-1`: `jira_get_required_workflow_scheme_mappings` -> `jira_read_workflow_previews` -> `jira_validate_create_workflows` -> `jira_validate_update_workflows` -> `jira_add_field_to_default_screen` -> `jira_add_notifications` -> `jira_migration_resource_workflow_rule_search_post` -> `jira_select_time_tracking_implementation` -> `jira_suggested_priorities_for_mappings` -> `jira_set_default_levels` -> `jira_set_default_priority` -> `jira_set_default_resolution`
- `jira-configuration-change-records-2`: `jira_update_default_screen_scheme` -> `jira_update_multiple_custom_field_values` -> `jira_update_schemes` -> `jira_delete_inactive_workflow` -> `jira_remove_member_from_security_level` -> `jira_remove_notification_from_notification_scheme`
