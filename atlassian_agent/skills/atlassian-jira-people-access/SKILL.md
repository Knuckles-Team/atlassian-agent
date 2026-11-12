---
name: atlassian-jira-people-access
skill_type: skill
description: >-
  Jira users, groups and membership, project roles and actors, avatars and
  permission checks. Use when the agent must look up a user, manage group
  membership or review access. Do NOT use for organization-wide identity (use
  atlassian-user-lifecycle).
license: MIT
tags: [atlassian, jira, users, groups, permissions]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Jira users, groups, roles and permissions

Typed people and access operations for one Jira site.

## When to use
- Find users and read their groups.
- Add or remove group members; create or delete groups.
- Read and change project role actors; check permissions.

## When NOT to use
- Organization directory and SCIM: use atlassian-user-lifecycle and atlassian-org-administration.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (54)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `jira_add_actor_users` | W | id_, payload, project_id_or_key |
| `jira_add_share_permission` | W | id_, payload |
| `jira_add_user_to_group` | W | group_id, groupname, payload |
| `jira_bulk_get_groups` | R | access_type, application_key, group_id, group_name, max_results, payload, start_at |
| `jira_bulk_get_users` | R | account_id, key, max_results, payload, start_at, username |
| `jira_bulk_get_users_migration` | R | key, max_results, payload, start_at, username |
| `jira_create_group` | W | payload |
| `jira_create_permission_grant` | W | expand, payload, scheme_id |
| `jira_create_user` | W | payload |
| `jira_delete_actor` | D | confirm, group, group_id, id_, payload, project_id_or_key, user |
| `jira_delete_avatar` | D | confirm, id_, owning_object_id, payload, type_ |
| `jira_delete_share_permission` | D | confirm, id_, payload, permission_id |
| `jira_delete_user_property` | D | account_id, confirm, payload, property_key, user_key, username |
| `jira_find_assignable_users` | R | account_id, account_type, action_descriptor_id, app_type, issue_id, issue_key, max_results, payload |
| `jira_find_bulk_assignable_users` | R | account_id, max_results, payload, project_keys, query, start_at, username |
| `jira_find_groups` | R | account_id, case_insensitive, exclude, exclude_id, max_results, payload, query, user_name |
| `jira_find_user_keys_by_query` | R | max_result, payload, query, start_at |
| `jira_find_users` | R | account_id, max_results, payload, property, query, start_at, username |
| `jira_find_users_and_groups` | R | avatar_size, case_insensitive, exclude_connect_addons, field_id, issue_type_id, max_results, payload, project_id |
| `jira_find_users_by_query` | R | max_results, payload, query, start_at |
| `jira_find_users_for_picker` | R | avatar_size, exclude, exclude_account_ids, exclude_connect_users, max_results, payload, query, show_avatar |
| `jira_find_users_with_all_permissions` | R | account_id, issue_key, max_results, payload, permissions, project_key, query, start_at |
| `jira_find_users_with_browse_permission` | R | account_id, issue_key, max_results, payload, project_key, query, start_at, username |
| `jira_get_all_application_roles` | R | payload |
| `jira_get_all_permissions` | R | payload |
| `jira_get_all_system_avatars` | R | payload, type_ |
| `jira_get_all_user_data_classification_levels` | R | order_by, payload, status |
| `jira_get_all_users` | R | expand, max_results, payload, start_at |
| `jira_get_application_role` | R | key, payload |
| `jira_get_avatar_image_by_id` | R | format, id_, payload, size, type_ |
| `jira_get_avatar_image_by_owner` | R | entity_id, format, payload, size, type_ |
| `jira_get_avatar_image_by_type` | R | format, payload, size, type_ |
| `jira_get_avatars` | R | entity_id, payload, type_ |
| `jira_get_bulk_permissions` | W | payload |
| `jira_get_current_user` | R | expand, payload |
| `jira_get_group` | R | expand, group_id, groupname, payload |
| `jira_get_my_permissions` | R | comment_id, issue_id, issue_key, payload, permissions, project_configuration_uuid, project_id, project_key |
| `jira_get_share_permission` | R | id_, payload, permission_id |
| `jira_get_share_permissions` | R | id_, payload |
| `jira_get_user` | R | account_id, expand, key, payload, username |
| `jira_get_user_email` | R | account_id, payload |
| `jira_get_user_email_bulk` | R | account_id, payload |
| `jira_get_user_groups` | R | account_id, key, payload, username |
| `jira_get_user_property` | R | account_id, payload, property_key, user_key, username |
| `jira_get_user_property_keys` | R | account_id, payload, user_key, username |
| `jira_get_users_from_group` | R | group_id, groupname, include_inactive_users, max_results, payload, start_at |
| `jira_remove_group` | D | confirm, group_id, groupname, payload, swap_group, swap_group_id |
| `jira_remove_user` | D | account_id, confirm, key, payload, username |
| `jira_remove_user_from_group` | D | account_id, confirm, group_id, groupname, payload, username |
| `jira_reset_user_columns` | D | account_id, confirm, payload, username |
| `jira_set_actors` | W | id_, payload, project_id_or_key |
| `jira_set_user_columns` | W | account_id, payload |
| `jira_set_user_property` | W | account_id, payload, property_key, user_key, username |
| `jira_store_avatar` | W | entity_id, payload, size, type_, x, y |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `jira-people-access-actor`: `jira_set_actors` -> `jira_delete_actor`
- `jira-people-access-application-role`: `jira_get_all_application_roles` -> `jira_get_application_role`
- `jira-people-access-avatar`: `jira_get_avatars` -> `jira_store_avatar` -> `jira_delete_avatar`
- `jira-people-access-avatar-image`: `jira_get_avatar_image_by_id` -> `jira_get_avatar_image_by_owner` -> `jira_get_avatar_image_by_type`
- `jira-people-access-get-user`: `jira_bulk_get_users` -> `jira_bulk_get_users_migration`
- `jira-people-access-group`: `jira_find_groups` -> `jira_get_group` -> `jira_create_group` -> `jira_remove_group`
- `jira-people-access-permission`: `jira_get_all_permissions` -> `jira_get_my_permissions`
- `jira-people-access-share-permission`: `jira_get_share_permission` -> `jira_get_share_permissions` -> `jira_add_share_permission` -> `jira_delete_share_permission`
- `jira-people-access-user`: `jira_find_users` -> `jira_get_all_users` -> `jira_get_user` -> `jira_create_user` -> `jira_remove_user`
- `jira-people-access-user-column`: `jira_reset_user_columns` -> `jira_set_user_columns`
- `jira-people-access-user-email`: `jira_get_user_email` -> `jira_get_user_email_bulk`
- `jira-people-access-user-group`: `jira_find_users_and_groups` -> `jira_get_user_groups` -> `jira_get_users_from_group` -> `jira_add_user_to_group` -> `jira_remove_user_from_group`
- `jira-people-access-user-property`: `jira_get_user_property` -> `jira_get_user_property_keys` -> `jira_set_user_property` -> `jira_delete_user_property`
- `jira-people-access-read-records`: `jira_bulk_get_groups` -> `jira_find_assignable_users` -> `jira_find_bulk_assignable_users` -> `jira_find_user_keys_by_query` -> `jira_find_users_by_query` -> `jira_find_users_for_picker` -> `jira_find_users_with_all_permissions` -> `jira_find_users_with_browse_permission` -> `jira_get_all_system_avatars` -> `jira_get_all_user_data_classification_levels` -> `jira_get_current_user`
- `jira-people-access-change-records`: `jira_get_bulk_permissions` -> `jira_add_actor_users` -> `jira_create_permission_grant`
