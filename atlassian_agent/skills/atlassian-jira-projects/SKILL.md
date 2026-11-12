---
name: atlassian-jira-projects
skill_type: skill
description: >-
  Jira projects, project components, versions and releases, categories and
  project roles. Use when the agent must list or configure projects, manage
  components and versions, or read project metadata. Do NOT use for issue work
  (use atlassian-jira-issues).
license: MIT
tags: [atlassian, jira, projects]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Jira projects, components and versions

Typed project operations. Archiving or deleting a project is destructive and needs approval.

## When to use
- List and read projects and their metadata.
- Create or update components and versions; release a version.
- Archive, restore or delete a project.

## When NOT to use
- Issues: use atlassian-jira-issues.
- Workflow and field schemes: use atlassian-jira-configuration.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (66)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `jira_add_project_role_actors_to_role` | W | id_, payload |
| `jira_archive_project` | W | payload, project_id_or_key |
| `jira_bulk_pin_unpin_projects_async` | W | payload |
| `jira_create_component` | W | payload |
| `jira_create_project` | W | payload |
| `jira_create_project_avatar` | W | payload, project_id_or_key, size, x, y |
| `jira_create_project_category` | W | payload |
| `jira_create_project_role` | W | payload |
| `jira_create_version` | W | payload |
| `jira_delete_and_replace_version` | D | confirm, id_, payload |
| `jira_delete_component` | D | confirm, id_, move_issues_to, payload |
| `jira_delete_project` | D | confirm, enable_undo, payload, project_id_or_key |
| `jira_delete_project_asynchronously` | D | confirm, payload, project_id_or_key |
| `jira_delete_project_avatar` | D | confirm, id_, payload, project_id_or_key |
| `jira_delete_project_property` | D | confirm, payload, project_id_or_key, property_key |
| `jira_delete_project_role` | D | confirm, id_, payload, swap |
| `jira_delete_project_role_actors_from_role` | D | confirm, group, group_id, id_, payload, user |
| `jira_delete_version` | D | confirm, id_, move_affected_issues_to, move_fix_issues_to, payload |
| `jira_find_components_for_projects` | R | max_results, order_by, payload, project_ids_or_keys, query, start_at |
| `jira_fully_update_project_role` | W | id_, payload |
| `jira_get_accessible_project_type_by_key` | R | payload, project_type_key |
| `jira_get_all_accessible_project_types` | R | payload |
| `jira_get_all_project_avatars` | R | payload, project_id_or_key |
| `jira_get_all_project_categories` | R | payload |
| `jira_get_all_project_roles` | R | payload |
| `jira_get_all_project_types` | R | payload |
| `jira_get_all_projects` | R | expand, payload, properties, recent |
| `jira_get_component` | R | id_, payload |
| `jira_get_component_related_issues` | R | id_, payload |
| `jira_get_features_for_project` | R | payload, project_id_or_key |
| `jira_get_permitted_projects` | W | payload |
| `jira_get_project` | R | expand, payload, project_id_or_key, properties |
| `jira_get_project_category_by_id` | R | id_, payload |
| `jira_get_project_classification_config` | R | payload, project_id_or_key |
| `jira_get_project_components` | R | component_source, payload, project_id_or_key |
| `jira_get_project_components_paginated` | R | component_source, max_results, order_by, payload, project_id_or_key, query, start_at |
| `jira_get_project_email` | R | payload, project_id |
| `jira_get_project_property` | R | payload, project_id_or_key, property_key |
| `jira_get_project_property_keys` | R | payload, project_id_or_key |
| `jira_get_project_role` | R | exclude_inactive_users, id_, payload, project_id_or_key |
| `jira_get_project_role_actors_for_role` | R | id_, payload |
| `jira_get_project_role_by_id` | R | id_, payload |
| `jira_get_project_role_details` | R | current_member, exclude_connect_addons, exclude_other_service_roles, payload, project_id_or_key |
| `jira_get_project_roles` | R | payload, project_id_or_key |
| `jira_get_project_type_by_key` | R | payload, project_type_key |
| `jira_get_project_versions` | R | expand, payload, project_id_or_key |
| `jira_get_project_versions_paginated` | R | expand, max_results, order_by, payload, project_id_or_key, query, start_at, status |
| `jira_get_valid_project_key` | R | key, payload |
| `jira_get_valid_project_name` | R | name, payload |
| `jira_get_version` | R | expand, id_, payload |
| `jira_get_version_related_issues` | R | id_, payload |
| `jira_get_version_unresolved_issues` | R | id_, payload |
| `jira_merge_versions` | W | id_, move_issues_to, payload |
| `jira_move_version` | W | id_, payload |
| `jira_partial_update_project_role` | W | id_, payload |
| `jira_remove_project_category` | D | confirm, id_, payload |
| `jira_search_projects` | R | category_id, expand, id_, keys, max_results, order_by, payload, permission_action |
| `jira_set_project_property` | W | payload, project_id_or_key, property_key |
| `jira_toggle_feature_for_project` | W | feature_key, payload, project_id_or_key |
| `jira_update_component` | W | id_, payload |
| `jira_update_project` | W | expand, payload, project_id_or_key |
| `jira_update_project_avatar` | W | payload, project_id_or_key |
| `jira_update_project_category` | W | id_, payload |
| `jira_update_project_email` | W | payload, project_id |
| `jira_update_version` | W | id_, payload |
| `jira_validate_project_key` | R | key, payload |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `jira-projects-accessible-project`: `jira_get_accessible_project_type_by_key` -> `jira_get_all_accessible_project_types`
- `jira-projects-component`: `jira_get_component` -> `jira_create_component` -> `jira_update_component` -> `jira_delete_component`
- `jira-projects-feature-project`: `jira_get_features_for_project` -> `jira_toggle_feature_for_project`
- `jira-projects-project`: `jira_get_all_projects` -> `jira_get_project` -> `jira_search_projects` -> `jira_create_project` -> `jira_archive_project` -> `jira_update_project` -> `jira_delete_project`
- `jira-projects-project-avatar`: `jira_get_all_project_avatars` -> `jira_create_project_avatar` -> `jira_update_project_avatar` -> `jira_delete_project_avatar`
- `jira-projects-project-category`: `jira_get_all_project_categories` -> `jira_get_project_category_by_id` -> `jira_create_project_category` -> `jira_update_project_category` -> `jira_remove_project_category`
- `jira-projects-project-component`: `jira_get_project_components` -> `jira_get_project_components_paginated`
- `jira-projects-project-email`: `jira_get_project_email` -> `jira_update_project_email`
- `jira-projects-project-property`: `jira_get_project_property` -> `jira_get_project_property_keys` -> `jira_set_project_property` -> `jira_delete_project_property`
- `jira-projects-project-role`: `jira_get_all_project_roles` -> `jira_get_project_role` -> `jira_get_project_role_actors_for_role` -> `jira_get_project_role_by_id` -> `jira_get_project_role_details` -> `jira_get_project_roles` -> `jira_add_project_role_actors_to_role` -> `jira_create_project_role` -> `jira_delete_project_role` -> `jira_delete_project_role_actors_from_role`
- `jira-projects-project-type`: `jira_get_all_project_types` -> `jira_get_project_type_by_key`
- `jira-projects-project-version`: `jira_get_project_versions` -> `jira_get_project_versions_paginated`
- `jira-projects-update-project`: `jira_fully_update_project_role` -> `jira_partial_update_project_role`
- `jira-projects-valid-project`: `jira_get_valid_project_key` -> `jira_get_valid_project_name`
- `jira-projects-version`: `jira_get_version` -> `jira_create_version` -> `jira_merge_versions` -> `jira_move_version` -> `jira_update_version` -> `jira_delete_version`
- `jira-projects-read-records`: `jira_find_components_for_projects` -> `jira_get_component_related_issues` -> `jira_get_project_classification_config` -> `jira_get_version_related_issues` -> `jira_get_version_unresolved_issues` -> `jira_validate_project_key`
- `jira-projects-change-records`: `jira_get_permitted_projects` -> `jira_bulk_pin_unpin_projects_async` -> `jira_delete_and_replace_version` -> `jira_delete_project_asynchronously`
