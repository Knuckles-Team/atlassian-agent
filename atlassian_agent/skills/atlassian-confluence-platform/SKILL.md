---
name: atlassian-confluence-platform
skill_type: skill
description: >-
  Confluence site-level operations: admin key, Forge and app data, data policy
  and other platform services. Use when the agent must read or change site-level
  Confluence settings. Do NOT use for page or space work.
license: MIT
tags: [atlassian, confluence, platform]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Confluence platform: admin keys, apps and data policy

Typed site-level operations.

## When to use
- Read site-level metadata and policies.
- Manage the admin key.

## When NOT to use
- Pages and spaces: use the Confluence content and space skills.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (11)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `confluence_check_access_by_email` | W | payload |
| `confluence_create_bulk_user_lookup` | W | payload |
| `confluence_delete_forge_app_property` | D | confirm, payload, property_key |
| `confluence_disable_admin_key` | D | confirm, payload |
| `confluence_enable_admin_key` | W | payload |
| `confluence_get_admin_key` | R | payload |
| `confluence_get_data_policy_metadata` | R | payload |
| `confluence_get_forge_app_properties` | R | cursor, limit, payload |
| `confluence_get_forge_app_property` | R | payload, property_key |
| `confluence_invite_by_email` | W | payload |
| `confluence_put_forge_app_property` | W | payload, property_key |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `confluence-platform-admin-key`: `confluence_get_admin_key` -> `confluence_disable_admin_key` -> `confluence_enable_admin_key`
- `confluence-platform-forge-app`: `confluence_get_forge_app_properties` -> `confluence_get_forge_app_property` -> `confluence_put_forge_app_property` -> `confluence_delete_forge_app_property`
- `confluence-platform-read-records`: `confluence_get_data_policy_metadata`
- `confluence-platform-change-records`: `confluence_check_access_by_email` -> `confluence_create_bulk_user_lookup` -> `confluence_invite_by_email`
