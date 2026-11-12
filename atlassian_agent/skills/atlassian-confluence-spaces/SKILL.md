---
name: atlassian-confluence-spaces
skill_type: skill
description: >-
  Confluence spaces, their properties, permissions, roles, classification and
  calendars. Use when the agent must list or create a space or review who can
  access it. Do NOT use for page content (use atlassian-confluence-content).
license: MIT
tags: [atlassian, confluence, spaces, permissions]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Confluence spaces, permissions and roles

Typed space operations. Permission and role changes widen or narrow access: ask for approval.

## When to use
- List and read spaces.
- Create a space; read and change its permissions and roles.
- Read content classification.

## When NOT to use
- Page content: use atlassian-confluence-content.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (43)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `confluence_add_calendar_event` | W | payload |
| `confluence_create_space` | W | payload |
| `confluence_create_space_property` | W | payload, space_id |
| `confluence_create_space_role` | W | payload |
| `confluence_delete_space_default_classification_level` | D | confirm, id_, payload |
| `confluence_delete_space_property_by_id` | D | confirm, payload, property_id, space_id |
| `confluence_delete_space_role` | D | confirm, id_, payload |
| `confluence_get_available_space_permissions` | R | cursor, limit, payload |
| `confluence_get_available_space_roles` | R | cursor, limit, payload, principal_id, principal_type, role_type, space_id |
| `confluence_get_blog_post_classification_level` | R | id_, payload, status |
| `confluence_get_blog_posts_in_space` | R | body_format, cursor, id_, limit, payload, sort, status, title |
| `confluence_get_calendars` | R | end, payload, start, sub_calendar_id, time_zone_id |
| `confluence_get_classification_levels` | R | payload |
| `confluence_get_custom_content_by_type_in_space` | R | body_format, cursor, id_, limit, payload, type_ |
| `confluence_get_data_policy_spaces` | R | cursor, ids, keys, limit, payload, sort |
| `confluence_get_database_classification_level` | R | id_, payload |
| `confluence_get_page_classification_level` | R | id_, payload, status |
| `confluence_get_pages_in_space` | R | body_format, cursor, depth, id_, limit, payload, sort, status |
| `confluence_get_space_by_id` | R | description_format, id_, include_icon, include_labels, include_operations, include_permissions, include_properties, include_role_assignments |
| `confluence_get_space_content_labels` | R | cursor, id_, limit, payload, prefix, sort |
| `confluence_get_space_default_classification_level` | R | id_, payload |
| `confluence_get_space_labels` | R | cursor, id_, limit, payload, prefix, sort |
| `confluence_get_space_operations` | R | id_, payload |
| `confluence_get_space_permissions_assignments` | R | cursor, id_, limit, payload |
| `confluence_get_space_properties` | R | cursor, key, limit, payload, space_id |
| `confluence_get_space_property_by_id` | R | payload, property_id, space_id |
| `confluence_get_space_role_assignments` | R | cursor, id_, limit, payload, principal_id, principal_type, role_id, role_type |
| `confluence_get_space_role_mode` | R | payload |
| `confluence_get_space_roles_by_id` | R | id_, payload |
| `confluence_get_spaces` | R | cursor, description_format, favorited_by, ids, include_icon, keys, labels, limit |
| `confluence_get_whiteboard_classification_level` | R | id_, payload |
| `confluence_post_blog_post_classification_level` | W | id_, payload |
| `confluence_post_database_classification_level` | W | id_, payload |
| `confluence_post_page_classification_level` | W | id_, payload |
| `confluence_post_whiteboard_classification_level` | W | id_, payload |
| `confluence_put_blog_post_classification_level` | W | id_, payload |
| `confluence_put_database_classification_level` | W | id_, payload |
| `confluence_put_page_classification_level` | W | id_, payload |
| `confluence_put_space_default_classification_level` | W | id_, payload |
| `confluence_put_whiteboard_classification_level` | W | id_, payload |
| `confluence_set_space_role_assignments` | W | id_, payload |
| `confluence_update_space_property_by_id` | W | payload, property_id, space_id |
| `confluence_update_space_role` | W | id_, payload |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `confluence-spaces-available-space`: `confluence_get_available_space_permissions` -> `confluence_get_available_space_roles`
- `confluence-spaces-blog-post`: `confluence_get_blog_post_classification_level` -> `confluence_get_blog_posts_in_space` -> `confluence_post_blog_post_classification_level` -> `confluence_put_blog_post_classification_level`
- `confluence-spaces-database-classification`: `confluence_get_database_classification_level` -> `confluence_post_database_classification_level` -> `confluence_put_database_classification_level`
- `confluence-spaces-page-classification`: `confluence_get_page_classification_level` -> `confluence_post_page_classification_level` -> `confluence_put_page_classification_level`
- `confluence-spaces-space`: `confluence_get_spaces` -> `confluence_create_space`
- `confluence-spaces-space-default`: `confluence_get_space_default_classification_level` -> `confluence_put_space_default_classification_level` -> `confluence_delete_space_default_classification_level`
- `confluence-spaces-space-property`: `confluence_get_space_properties` -> `confluence_get_space_property_by_id` -> `confluence_create_space_property` -> `confluence_update_space_property_by_id` -> `confluence_delete_space_property_by_id`
- `confluence-spaces-space-role`: `confluence_get_space_role_assignments` -> `confluence_get_space_role_mode` -> `confluence_get_space_roles_by_id` -> `confluence_create_space_role` -> `confluence_set_space_role_assignments` -> `confluence_update_space_role` -> `confluence_delete_space_role`
- `confluence-spaces-whiteboard-classification`: `confluence_get_whiteboard_classification_level` -> `confluence_post_whiteboard_classification_level` -> `confluence_put_whiteboard_classification_level`
- `confluence-spaces-read-records`: `confluence_get_calendars` -> `confluence_get_classification_levels` -> `confluence_get_custom_content_by_type_in_space` -> `confluence_get_data_policy_spaces` -> `confluence_get_pages_in_space` -> `confluence_get_space_by_id` -> `confluence_get_space_content_labels` -> `confluence_get_space_labels` -> `confluence_get_space_operations` -> `confluence_get_space_permissions_assignments`
- `confluence-spaces-change-records`: `confluence_add_calendar_event`
