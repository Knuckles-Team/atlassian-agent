---
name: atlassian-user-lifecycle
skill_type: skill
description: >-
  Atlassian managed users (suspend, restore, read and update profiles) and SCIM
  user and group provisioning (users, groups, schemas, patch and put). Use when
  the agent must onboard, update, suspend or remove a managed account. Do NOT
  use for Jira group membership (use atlassian-jira-people-access).
license: MIT
tags: [atlassian, scim, users, provisioning]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Atlassian user management and SCIM provisioning

Typed operations for the user management and user provisioning APIs. Deleting or suspending an account is destructive-tier.

## When to use
- Read managed accounts.
- Suspend or restore a managed account.
- Create, patch, replace or delete SCIM users and groups; read schemas.

## When NOT to use
- Jira-only user lookups: use atlassian-jira-people-access.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (34)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id` | D | account_id, confirm, payload, token_id |
| `user_mgmt_cloud_get_users_account_id_manage` | R | account_id, payload, privileges |
| `user_mgmt_cloud_get_users_account_id_manage_api_tokens` | R | account_id, payload |
| `user_mgmt_cloud_get_users_account_id_manage_profile` | R | account_id, payload |
| `user_mgmt_cloud_patch_users_account_id_manage_profile` | W | account_id, payload |
| `user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete` | D | account_id, confirm, payload |
| `user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete` | D | account_id, confirm, payload |
| `user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable` | W | account_id, payload |
| `user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable` | W | account_id, payload |
| `user_mgmt_cloud_put_users_account_id_manage_email` | W | account_id, payload |
| `user_provisioning_cloud_create_a_group_in_active_directory` | W | directory_id, payload |
| `user_provisioning_cloud_create_a_user_in_an_active_directory` | W | attributes, directory_id, excluded_attributes, payload |
| `user_provisioning_cloud_delete_a_group` | D | confirm, directory_id, id_, payload |
| `user_provisioning_cloud_delete_a_user_from_an_active_directory` | D | confirm, directory_id, payload, user_id |
| `user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db` | D | aaid, confirm, org_id, payload |
| `user_provisioning_cloud_get` | R | directory_id, id_, payload |
| `user_provisioning_cloud_get_a_user_from_active_directory` | R | attributes, directory_id, excluded_attributes, payload, user_id |
| `user_provisioning_cloud_get_all_groups_from_an_active_directory` | R | count, directory_id, filter, payload, start_index |
| `user_provisioning_cloud_get_config` | R | directory_id, payload |
| `user_provisioning_cloud_get_extension_user_schemas` | R | directory_id, payload |
| `user_provisioning_cloud_get_group_resource_type` | R | directory_id, payload |
| `user_provisioning_cloud_get_group_schemas` | R | directory_id, payload |
| `user_provisioning_cloud_get_resource_types` | R | directory_id, payload |
| `user_provisioning_cloud_get_schemas` | R | directory_id, payload |
| `user_provisioning_cloud_get_scim_links` | R | aa_id, org_id, payload |
| `user_provisioning_cloud_get_scim_links_by_email` | W | org_id, payload |
| `user_provisioning_cloud_get_user_resource_type` | R | directory_id, payload |
| `user_provisioning_cloud_get_user_schemas` | R | directory_id, payload |
| `user_provisioning_cloud_get_users_from_an_active_directory` | R | attributes, count, directory_id, excluded_attributes, filter, payload, start_index |
| `user_provisioning_cloud_patch` | W | directory_id, id_, payload |
| `user_provisioning_cloud_patch_user_information_in_an_active_directory` | W | attributes, directory_id, excluded_attributes, payload, user_id |
| `user_provisioning_cloud_put` | W | directory_id, id_, payload |
| `user_provisioning_cloud_unlink_scim_user` | W | org_id, payload, scim_directory_id, scim_user_id |
| `user_provisioning_cloud_update_user_information_in_an_active_directory` | W | attributes, directory_id, excluded_attributes, payload, user_id |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `lifecycle-scim-link`: `user_provisioning_cloud_get_scim_links` -> `user_provisioning_cloud_get_scim_links_by_email`
- `lifecycle-user-account`: `user_mgmt_cloud_get_users_account_id_manage` -> `user_mgmt_cloud_get_users_account_id_manage_api_tokens` -> `user_mgmt_cloud_get_users_account_id_manage_profile` -> `user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete` -> `user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete` -> `user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable` -> `user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable` -> `user_mgmt_cloud_patch_users_account_id_manage_profile` -> `user_mgmt_cloud_put_users_account_id_manage_email` -> `user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id`
- `lifecycle-user-an`: `user_provisioning_cloud_get_users_from_an_active_directory` -> `user_provisioning_cloud_create_a_user_in_an_active_directory` -> `user_provisioning_cloud_delete_a_user_from_an_active_directory`
- `lifecycle-user-information`: `user_provisioning_cloud_patch_user_information_in_an_active_directory` -> `user_provisioning_cloud_update_user_information_in_an_active_directory`
- `lifecycle-read-records`: `user_provisioning_cloud_get` -> `user_provisioning_cloud_get_a_user_from_active_directory` -> `user_provisioning_cloud_get_all_groups_from_an_active_directory` -> `user_provisioning_cloud_get_config` -> `user_provisioning_cloud_get_extension_user_schemas` -> `user_provisioning_cloud_get_group_resource_type` -> `user_provisioning_cloud_get_group_schemas` -> `user_provisioning_cloud_get_resource_types` -> `user_provisioning_cloud_get_schemas` -> `user_provisioning_cloud_get_user_resource_type` -> `user_provisioning_cloud_get_user_schemas`
- `lifecycle-change-records`: `user_provisioning_cloud_create_a_group_in_active_directory` -> `user_provisioning_cloud_unlink_scim_user` -> `user_provisioning_cloud_patch` -> `user_provisioning_cloud_put` -> `user_provisioning_cloud_delete_a_group` -> `user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db`
