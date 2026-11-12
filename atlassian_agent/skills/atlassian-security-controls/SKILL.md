---
name: atlassian-security-controls
skill_type: skill
description: >-
  Organization API key management, data loss prevention classification levels
  and the control APIs for Atlassian Guard. Use when the agent must review API
  keys, classification levels or control settings. Do NOT use for product
  content.
license: MIT
tags: [atlassian, dlp, api-keys, security]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Atlassian API keys, data loss prevention and policy controls

Typed security-control operations. Revoking a key or reordering levels takes effect organization-wide: approval first.

## When to use
- List API keys and service accounts; revoke a key.
- Read, create and reorder data classification levels.
- Read control settings.

## When NOT to use
- User accounts: use atlassian-user-lifecycle.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (39)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `api_access_cloud_bulk_revoke_api_tokens` | D | confirm, org_id, payload |
| `api_access_cloud_count_service_account_api_tokens` | W | org_id, payload |
| `api_access_cloud_get_all_api_keys_by_org_id` | R | org_id, payload |
| `api_access_cloud_get_all_api_tokens_by_org_id` | R | org_id, payload |
| `api_access_cloud_get_api_key_count_by_org_id` | R | org_id, payload |
| `api_access_cloud_get_api_token_count_by_org_id` | R | org_id, payload |
| `api_access_cloud_get_service_account_api_token` | R | account_id, org_id, payload, token_label |
| `api_access_cloud_revoke_api_key` | W | api_key_id, org_id, payload |
| `api_access_cloud_revoke_api_tokens` | D | account_id, confirm, org_id, payload |
| `control_cloud_ap_is_add_users_to_policy` | W | org_id, payload, policy_id |
| `control_cloud_ap_is_attach_detach_resources_v2` | W | org_id, payload, policy_id |
| `control_cloud_ap_is_bulk_fetch_auth_policy` | W | org_id, payload |
| `control_cloud_ap_is_create_policy` | W | org_id, payload |
| `control_cloud_ap_is_create_policy_v2` | W | org_id, payload |
| `control_cloud_ap_is_create_resource` | W | org_id, payload, policy_id |
| `control_cloud_ap_is_delete_policy` | D | confirm, org_id, payload, policy_id |
| `control_cloud_ap_is_delete_resource` | D | confirm, org_id, payload, policy_id, resource_id |
| `control_cloud_ap_is_delete_resources` | D | confirm, org_id, payload, policy_id |
| `control_cloud_ap_is_delete_resources_v2` | D | confirm, org_id, payload, policy_id |
| `control_cloud_ap_is_get_policies` | R | cursor, org_id, payload, type_ |
| `control_cloud_ap_is_get_policies_v2` | R | cursor, org_id, payload, type_ |
| `control_cloud_ap_is_get_policy` | R | org_id, payload, policy_id |
| `control_cloud_ap_is_get_policy_v2` | R | org_id, payload, policy_id |
| `control_cloud_ap_is_get_resources` | R | org_id, payload, policy_id |
| `control_cloud_ap_is_get_resources_v2` | R | org_id, payload, policy_id |
| `control_cloud_ap_is_get_task_status` | R | org_id, payload, task_id |
| `control_cloud_ap_is_publish_draft_policies` | W | org_id, payload |
| `control_cloud_ap_is_update_policy` | W | org_id, payload, policy_id |
| `control_cloud_ap_is_update_policy_v2` | W | org_id, payload, policy_id |
| `control_cloud_ap_is_update_resource` | W | org_id, payload, policy_id, resource_id |
| `control_cloud_ap_is_validate_policy` | R | org_id, payload, policy_id |
| `dlp_cloud_archive_level` | W | org_id, payload |
| `dlp_cloud_create_level` | W | org_id, payload |
| `dlp_cloud_edit_level` | W | level_id, org_id, payload |
| `dlp_cloud_get_level` | R | level_id, org_id, payload |
| `dlp_cloud_get_level_list` | R | org_id, payload |
| `dlp_cloud_publish_level` | W | org_id, payload |
| `dlp_cloud_reorder` | W | org_id, payload |
| `dlp_cloud_restore_level` | W | org_id, payload |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `controls-api-key`: `api_access_cloud_get_all_api_keys_by_org_id` -> `api_access_cloud_get_api_key_count_by_org_id` -> `api_access_cloud_revoke_api_key`
- `controls-api-token`: `api_access_cloud_get_all_api_tokens_by_org_id` -> `api_access_cloud_get_api_token_count_by_org_id` -> `api_access_cloud_revoke_api_tokens`
- `controls-is-create`: `control_cloud_ap_is_create_policy` -> `control_cloud_ap_is_create_policy_v2` -> `control_cloud_ap_is_create_resource`
- `controls-is-delete`: `control_cloud_ap_is_delete_policy` -> `control_cloud_ap_is_delete_resource` -> `control_cloud_ap_is_delete_resources` -> `control_cloud_ap_is_delete_resources_v2`
- `controls-is-get`: `control_cloud_ap_is_get_policies` -> `control_cloud_ap_is_get_policies_v2` -> `control_cloud_ap_is_get_policy` -> `control_cloud_ap_is_get_policy_v2` -> `control_cloud_ap_is_get_resources` -> `control_cloud_ap_is_get_resources_v2` -> `control_cloud_ap_is_get_task_status`
- `controls-is-update`: `control_cloud_ap_is_update_policy` -> `control_cloud_ap_is_update_policy_v2` -> `control_cloud_ap_is_update_resource`
- `controls-level`: `dlp_cloud_get_level` -> `dlp_cloud_create_level` -> `dlp_cloud_archive_level` -> `dlp_cloud_edit_level` -> `dlp_cloud_publish_level` -> `dlp_cloud_restore_level`
- `controls-service-account`: `api_access_cloud_count_service_account_api_tokens` -> `api_access_cloud_get_service_account_api_token`
- `controls-read-records`: `control_cloud_ap_is_validate_policy` -> `dlp_cloud_get_level_list`
- `controls-change-records`: `control_cloud_ap_is_add_users_to_policy` -> `control_cloud_ap_is_attach_detach_resources_v2` -> `control_cloud_ap_is_bulk_fetch_auth_policy` -> `control_cloud_ap_is_publish_draft_policies` -> `api_access_cloud_bulk_revoke_api_tokens` -> `dlp_cloud_reorder`
