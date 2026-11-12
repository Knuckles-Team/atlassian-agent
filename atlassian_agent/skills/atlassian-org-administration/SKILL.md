---
name: atlassian-org-administration
skill_type: skill
description: >-
  Atlassian organization administration: organizations, directories, domains,
  workspaces, admin and policy resources, audit events and role assignments
  through the cloud admin APIs. Use when the agent must inspect or administer an
  Atlassian organization. Do NOT use for product-level Jira or Confluence work.
license: MIT
tags: [atlassian, organization, admin, audit]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Atlassian organization administration

Typed organization operations on the cloud admin APIs (v1 and v2). Policy and role changes are destructive-tier: approval first.

## When to use
- List organizations, directories, domains and workspaces.
- Read audit events and policies; create or change a policy.
- Manage organization roles and groups.

## When NOT to use
- Jira and Confluence content: use their product skills.
- User provisioning: use atlassian-user-lifecycle.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (114)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `admin_cloud_add_resource_to_policy` | W | org_id, payload, policy_id |
| `admin_cloud_assign_role` | W | org_id, payload, user_id |
| `admin_cloud_assign_role_to_group` | W | group_id, org_id, payload |
| `admin_cloud_create_policy` | W | org_id, payload |
| `admin_cloud_delete_policy` | D | confirm, org_id, payload, policy_id |
| `admin_cloud_delete_policy_resource` | D | confirm, org_id, payload, policy_id, resource_id |
| `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id` | D | confirm, force_if_not_empty, group_id, org_id, payload |
| `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` | D | account_id, confirm, group_id, org_id, payload |
| `admin_cloud_delete_v1_orgs_org_id_directory_users_account_id` | D | account_id, confirm, org_id, payload |
| `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` | D | confirm, directory_id, group_id, org_id, payload |
| `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` | D | account_id, confirm, directory_id, group_id, org_id, payload |
| `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` | D | account_id, confirm, directory_id, org_id, payload |
| `admin_cloud_get_directories_for_org` | R | org_id, payload |
| `admin_cloud_get_directory_user_details` | R | directory_id, org_id, payload, user_id |
| `admin_cloud_get_directory_users` | R | directory_id, org_id, payload |
| `admin_cloud_get_directory_users_count` | R | directory_id, org_id, payload |
| `admin_cloud_get_domain_by_id` | R | domain_id, org_id, payload |
| `admin_cloud_get_domains` | R | cursor, org_id, payload |
| `admin_cloud_get_event_actions` | R | org_id, payload |
| `admin_cloud_get_event_by_id` | R | event_id, org_id, payload |
| `admin_cloud_get_events` | R | actor, cursor, event_action, from_, ip, limit, location, org_id |
| `admin_cloud_get_group` | R | directory_id, group_id, org_id, payload |
| `admin_cloud_get_group_role_assignments` | R | directory_id, group_id, org_id, payload |
| `admin_cloud_get_groups` | R | directory_id, org_id, payload |
| `admin_cloud_get_groups_count` | R | directory_id, org_id, payload |
| `admin_cloud_get_groups_stats` | R | directory_id, org_id, payload |
| `admin_cloud_get_org_by_id` | R | org_id, payload |
| `admin_cloud_get_orgs` | R | cursor, payload |
| `admin_cloud_get_policies` | R | cursor, org_id, payload, type_ |
| `admin_cloud_get_policy_by_id` | R | org_id, payload, policy_id |
| `admin_cloud_get_user_role_assignments` | R | account_id, directory_id, org_id, payload |
| `admin_cloud_get_user_stats` | R | directory_id, org_id, payload |
| `admin_cloud_get_users` | R | cursor, org_id, payload |
| `admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` | R | account_id, cursor, org_id, payload |
| `admin_cloud_poll_events` | R | cursor, from_, limit, org_id, payload, sort_order, to |
| `admin_cloud_post_v1_orgs_org_id_directory_groups` | W | org_id, payload |
| `admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` | W | group_id, org_id, payload |
| `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` | W | account_id, org_id, payload |
| `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` | W | account_id, org_id, payload |
| `admin_cloud_post_v1_orgs_org_id_users_invite` | W | org_id, payload |
| `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` | W | org_id, payload, user_id |
| `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` | W | org_id, payload, user_id |
| `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups` | W | directory_id, org_id, payload |
| `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` | W | directory_id, group_id, org_id, payload |
| `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` | W | directory_id, group_id, org_id, payload |
| `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` | W | directory_id, group_id, org_id, payload |
| `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` | W | account_id, directory_id, org_id, payload |
| `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` | W | account_id, directory_id, org_id, payload |
| `admin_cloud_post_v2_orgs_org_id_users_invite` | W | org_id, payload |
| `admin_cloud_query_workspaces_v2` | W | org_id, payload |
| `admin_cloud_revoke_role` | W | org_id, payload, user_id |
| `admin_cloud_revoke_role_to_group` | W | group_id, org_id, payload |
| `admin_cloud_search_groups` | W | org_id, payload |
| `admin_cloud_search_users` | W | org_id, payload |
| `admin_cloud_update_policy` | W | org_id, payload, policy_id |
| `admin_cloud_update_policy_resource` | W | org_id, payload, policy_id, resource_id |
| `admin_cloud_validate_policy` | R | org_id, payload, policy_id |
| `org_cloud_add_resource_to_policy` | W | org_id, payload, policy_id |
| `org_cloud_assign_role` | W | org_id, payload, user_id |
| `org_cloud_assign_role_to_group` | W | group_id, org_id, payload |
| `org_cloud_create_policy` | W | org_id, payload |
| `org_cloud_delete_policy` | D | confirm, org_id, payload, policy_id |
| `org_cloud_delete_policy_resource` | D | confirm, org_id, payload, policy_id, resource_id |
| `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id` | D | confirm, force_if_not_empty, group_id, org_id, payload |
| `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` | D | account_id, confirm, group_id, org_id, payload |
| `org_cloud_delete_v1_orgs_org_id_directory_users_account_id` | D | account_id, confirm, org_id, payload |
| `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` | D | confirm, directory_id, group_id, org_id, payload |
| `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` | D | account_id, confirm, directory_id, group_id, org_id, payload |
| `org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` | D | account_id, confirm, directory_id, org_id, payload |
| `org_cloud_get_directories_for_org` | R | org_id, payload |
| `org_cloud_get_directory_user_details` | R | directory_id, org_id, payload, user_id |
| `org_cloud_get_directory_users` | R | directory_id, org_id, payload |
| `org_cloud_get_directory_users_count` | R | directory_id, org_id, payload |
| `org_cloud_get_domain_by_id` | R | domain_id, org_id, payload |
| `org_cloud_get_domains` | R | cursor, org_id, payload |
| `org_cloud_get_event_actions` | R | org_id, payload |
| `org_cloud_get_event_by_id` | R | event_id, org_id, payload |
| `org_cloud_get_events` | R | actor, cursor, event_action, from_, ip, limit, location, org_id |
| `org_cloud_get_group` | R | directory_id, group_id, org_id, payload |
| `org_cloud_get_group_role_assignments` | R | directory_id, group_id, org_id, payload |
| `org_cloud_get_groups` | R | directory_id, org_id, payload |
| `org_cloud_get_groups_count` | R | directory_id, org_id, payload |
| `org_cloud_get_groups_stats` | R | directory_id, org_id, payload |
| `org_cloud_get_org_by_id` | R | org_id, payload |
| `org_cloud_get_orgs` | R | cursor, payload |
| `org_cloud_get_policies` | R | cursor, org_id, payload, type_ |
| `org_cloud_get_policy_by_id` | R | org_id, payload, policy_id |
| `org_cloud_get_user_role_assignments` | R | account_id, directory_id, org_id, payload |
| `org_cloud_get_user_stats` | R | directory_id, org_id, payload |
| `org_cloud_get_users` | R | cursor, org_id, payload |
| `org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` | R | account_id, cursor, org_id, payload |
| `org_cloud_poll_events` | R | cursor, from_, limit, org_id, payload, sort_order, to |
| `org_cloud_post_v1_orgs_org_id_directory_groups` | W | org_id, payload |
| `org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` | W | group_id, org_id, payload |
| `org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` | W | account_id, org_id, payload |
| `org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` | W | account_id, org_id, payload |
| `org_cloud_post_v1_orgs_org_id_users_invite` | W | org_id, payload |
| `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` | W | org_id, payload, user_id |
| `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` | W | org_id, payload, user_id |
| `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups` | W | directory_id, org_id, payload |
| `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` | W | directory_id, group_id, org_id, payload |
| `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` | W | directory_id, group_id, org_id, payload |
| `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` | W | directory_id, group_id, org_id, payload |
| `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` | W | account_id, directory_id, org_id, payload |
| `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` | W | account_id, directory_id, org_id, payload |
| `org_cloud_post_v2_orgs_org_id_users_invite` | W | org_id, payload |
| `org_cloud_query_workspaces_v2` | W | org_id, payload |
| `org_cloud_revoke_role` | W | org_id, payload, user_id |
| `org_cloud_revoke_role_to_group` | W | group_id, org_id, payload |
| `org_cloud_search_groups` | W | org_id, payload |
| `org_cloud_search_users` | W | org_id, payload |
| `org_cloud_update_policy` | W | org_id, payload, policy_id |
| `org_cloud_update_policy_resource` | W | org_id, payload, policy_id, resource_id |
| `org_cloud_validate_policy` | R | org_id, payload, policy_id |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `org-directory-org`: `admin_cloud_get_directories_for_org` -> `org_cloud_get_directories_for_org`
- `org-directory-user`: `admin_cloud_get_directory_user_details` -> `admin_cloud_get_directory_users` -> `admin_cloud_get_directory_users_count` -> `org_cloud_get_directory_user_details` -> `org_cloud_get_directory_users` -> `org_cloud_get_directory_users_count`
- `org-domain`: `admin_cloud_get_domains` -> `org_cloud_get_domains`
- `org-domain-id`: `admin_cloud_get_domain_by_id` -> `org_cloud_get_domain_by_id`
- `org-event`: `admin_cloud_get_events` -> `org_cloud_get_events` -> `admin_cloud_poll_events` -> `org_cloud_poll_events`
- `org-event-action`: `admin_cloud_get_event_actions` -> `org_cloud_get_event_actions`
- `org-event-id`: `admin_cloud_get_event_by_id` -> `org_cloud_get_event_by_id`
- `org-group`: `admin_cloud_get_group` -> `admin_cloud_get_groups` -> `admin_cloud_search_groups` -> `org_cloud_get_group` -> `org_cloud_get_groups` -> `org_cloud_search_groups`
- `org-group-count`: `admin_cloud_get_groups_count` -> `org_cloud_get_groups_count`
- `org-group-role`: `admin_cloud_get_group_role_assignments` -> `org_cloud_get_group_role_assignments`
- `org-group-stat`: `admin_cloud_get_groups_stats` -> `org_cloud_get_groups_stats`
- `org`: `admin_cloud_get_orgs` -> `org_cloud_get_orgs`
- `org-id`: `admin_cloud_get_org_by_id` -> `org_cloud_get_org_by_id`
- `org-policy`: `admin_cloud_get_policies` -> `admin_cloud_validate_policy` -> `org_cloud_get_policies` -> `org_cloud_validate_policy` -> `admin_cloud_create_policy` -> `org_cloud_create_policy` -> `admin_cloud_update_policy` -> `org_cloud_update_policy` -> `admin_cloud_delete_policy` -> `org_cloud_delete_policy`
- `org-policy-id`: `admin_cloud_get_policy_by_id` -> `org_cloud_get_policy_by_id`
- `org-policy-resource`: `admin_cloud_update_policy_resource` -> `org_cloud_update_policy_resource` -> `admin_cloud_delete_policy_resource` -> `org_cloud_delete_policy_resource`
- `org-resource-policy`: `admin_cloud_add_resource_to_policy` -> `org_cloud_add_resource_to_policy`
- `org-role`: `admin_cloud_assign_role` -> `org_cloud_assign_role` -> `admin_cloud_revoke_role` -> `org_cloud_revoke_role`
- `org-role-group`: `admin_cloud_assign_role_to_group` -> `org_cloud_assign_role_to_group` -> `admin_cloud_revoke_role_to_group` -> `org_cloud_revoke_role_to_group`
- `org-user`: `admin_cloud_get_users` -> `admin_cloud_search_users` -> `org_cloud_get_users` -> `org_cloud_search_users`
- `org-user-role`: `admin_cloud_get_user_role_assignments` -> `org_cloud_get_user_role_assignments`
- `org-user-stat`: `admin_cloud_get_user_stats` -> `org_cloud_get_user_stats`
- `org-v1-org`: `admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` -> `org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` -> `admin_cloud_post_v1_orgs_org_id_directory_groups` -> `admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` -> `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` -> `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` -> `admin_cloud_post_v1_orgs_org_id_users_invite` -> `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` -> `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` -> `org_cloud_post_v1_orgs_org_id_directory_groups` -> `org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` -> `org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` -> `org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` -> `org_cloud_post_v1_orgs_org_id_users_invite` -> `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` -> `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` -> `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id` -> `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` -> `admin_cloud_delete_v1_orgs_org_id_directory_users_account_id` -> `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id` -> `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` -> `org_cloud_delete_v1_orgs_org_id_directory_users_account_id`
- `org-v2-org`: `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups` -> `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` -> `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` -> `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` -> `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` -> `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` -> `admin_cloud_post_v2_orgs_org_id_users_invite` -> `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups` -> `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` -> `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` -> `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` -> `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` -> `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` -> `org_cloud_post_v2_orgs_org_id_users_invite` -> `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` -> `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` -> `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` -> `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` -> `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` -> `org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id`
- `org-workspace-v2`: `admin_cloud_query_workspaces_v2` -> `org_cloud_query_workspaces_v2`
