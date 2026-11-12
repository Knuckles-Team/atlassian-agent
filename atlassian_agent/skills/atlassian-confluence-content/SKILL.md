---
name: atlassian-confluence-content
skill_type: skill
description: >-
  Confluence content: pages, blog posts, footer and inline comments,
  attachments, labels, folders, smart links, whiteboards, databases, tasks,
  custom content and versions. Use when the agent must find, read, write or
  organize Confluence content. Do NOT use for space administration (use
  atlassian-confluence-spaces).
license: MIT
tags: [atlassian, confluence, pages, content]
metadata:
  author: Knuckles-Team
  version: '0.2.0'
---
# Confluence pages, blog posts, comments and whiteboards

Typed `confluence_<operation>` tools. Cloud or Server/Data Center is chosen by ATLASSIAN_CONFLUENCE_DEPLOYMENT.

## When to use
- List and read pages by space, then read their body and children.
- Create or update a page or blog post with a storage-format body.
- Comment, label and attach files.
- Manage folders, whiteboards, databases, smart links and tasks.

## When NOT to use
- Space settings and permissions: use atlassian-confluence-spaces.

## Safety
- Changes follow the signed-in account's permissions; the product refuses what the account may not do.
- Destructive tools (delete, remove, archive, revoke) need explicit approval naming the target.
- Never print tokens or API keys.

## Tools (160)

R = read-only, W = changes data, D = destructive (needs approval). Parameters in brackets are the typed inputs.

| Tool | Kind | Inputs |
|---|---|---|
| `confluence_convert_content_ids_to_content_types` | W | payload |
| `confluence_create_attachment_property` | W | attachment_id, payload |
| `confluence_create_blog_post` | W | payload, private |
| `confluence_create_blogpost_property` | W | blogpost_id, payload |
| `confluence_create_comment_property` | W | comment_id, payload |
| `confluence_create_custom_content` | W | payload |
| `confluence_create_custom_content_property` | W | custom_content_id, payload |
| `confluence_create_database` | W | payload, private |
| `confluence_create_database_property` | W | id_, payload |
| `confluence_create_folder` | W | payload |
| `confluence_create_folder_property` | W | id_, payload |
| `confluence_create_footer_comment` | W | payload |
| `confluence_create_inline_comment` | W | payload |
| `confluence_create_page` | W | embedded, payload, private, root_level |
| `confluence_create_page_property` | W | page_id, payload |
| `confluence_create_smart_link` | W | payload |
| `confluence_create_smart_link_property` | W | id_, payload |
| `confluence_create_whiteboard` | W | payload, private |
| `confluence_create_whiteboard_property` | W | id_, payload |
| `confluence_delete_attachment` | D | confirm, id_, payload, purge |
| `confluence_delete_attachment_property_by_id` | D | attachment_id, confirm, payload, property_id |
| `confluence_delete_blog_post` | D | confirm, draft, id_, payload, purge |
| `confluence_delete_blogpost_property_by_id` | D | blogpost_id, confirm, payload, property_id |
| `confluence_delete_comment_property_by_id` | D | comment_id, confirm, payload, property_id |
| `confluence_delete_custom_content` | D | confirm, id_, payload, purge |
| `confluence_delete_custom_content_property_by_id` | D | confirm, custom_content_id, payload, property_id |
| `confluence_delete_database` | D | confirm, id_, payload |
| `confluence_delete_database_property_by_id` | D | confirm, database_id, payload, property_id |
| `confluence_delete_folder` | D | confirm, id_, payload |
| `confluence_delete_folder_property_by_id` | D | confirm, folder_id, payload, property_id |
| `confluence_delete_footer_comment` | D | comment_id, confirm, payload |
| `confluence_delete_inline_comment` | D | comment_id, confirm, payload |
| `confluence_delete_page` | D | confirm, draft, id_, payload, purge |
| `confluence_delete_page_property_by_id` | D | confirm, page_id, payload, property_id |
| `confluence_delete_smart_link` | D | confirm, id_, payload |
| `confluence_delete_smart_link_property_by_id` | D | confirm, embed_id, payload, property_id |
| `confluence_delete_whiteboard` | D | confirm, id_, payload |
| `confluence_delete_whiteboard_property_by_id` | D | confirm, payload, property_id, whiteboard_id |
| `confluence_get_attachment_by_id` | R | id_, include_collaborators, include_labels, include_operations, include_properties, include_version, include_versions, payload |
| `confluence_get_attachment_comments` | R | body_format, cursor, id_, limit, payload, sort, version |
| `confluence_get_attachment_content_properties` | R | attachment_id, cursor, key, limit, payload, sort |
| `confluence_get_attachment_content_properties_by_id` | R | attachment_id, payload, property_id |
| `confluence_get_attachment_labels` | R | cursor, id_, limit, payload, prefix, sort |
| `confluence_get_attachment_operations` | R | id_, payload |
| `confluence_get_attachment_version_details` | R | attachment_id, payload, version_number |
| `confluence_get_attachment_versions` | R | cursor, id_, limit, payload, sort |
| `confluence_get_attachments` | R | cursor, filename, limit, media_type, payload, sort, status |
| `confluence_get_blog_post_by_id` | R | body_format, get_draft, id_, include_collaborators, include_favorited_by_current_user_status, include_labels, include_likes, include_operations |
| `confluence_get_blog_post_footer_comments` | R | body_format, cursor, id_, limit, payload, sort, status |
| `confluence_get_blog_post_inline_comments` | R | body_format, cursor, id_, limit, payload, resolution_status, sort, status |
| `confluence_get_blog_post_labels` | R | cursor, id_, limit, payload, prefix, sort |
| `confluence_get_blog_post_like_count` | R | id_, payload |
| `confluence_get_blog_post_like_users` | R | cursor, id_, limit, payload |
| `confluence_get_blog_post_operations` | R | id_, payload |
| `confluence_get_blog_post_version_details` | R | blogpost_id, payload, version_number |
| `confluence_get_blog_post_versions` | R | body_format, cursor, id_, limit, payload, sort |
| `confluence_get_blog_posts` | R | body_format, cursor, id_, limit, payload, sort, space_id, status |
| `confluence_get_blogpost_attachments` | R | cursor, filename, id_, limit, media_type, payload, sort, status |
| `confluence_get_blogpost_content_properties` | R | blogpost_id, cursor, key, limit, payload, sort |
| `confluence_get_blogpost_content_properties_by_id` | R | blogpost_id, payload, property_id |
| `confluence_get_child_custom_content` | R | cursor, id_, limit, payload, sort |
| `confluence_get_child_pages` | R | cursor, id_, limit, payload, sort |
| `confluence_get_comment_content_properties` | R | comment_id, cursor, key, limit, payload, sort |
| `confluence_get_comment_content_properties_by_id` | R | comment_id, payload, property_id |
| `confluence_get_custom_content_attachments` | R | cursor, filename, id_, limit, media_type, payload, sort, status |
| `confluence_get_custom_content_by_id` | R | body_format, id_, include_collaborators, include_labels, include_operations, include_properties, include_version, include_versions |
| `confluence_get_custom_content_by_type` | R | body_format, cursor, id_, limit, payload, sort, space_id, type_ |
| `confluence_get_custom_content_by_type_in_blog_post` | R | body_format, cursor, id_, limit, payload, sort, type_ |
| `confluence_get_custom_content_by_type_in_page` | R | body_format, cursor, id_, limit, payload, sort, type_ |
| `confluence_get_custom_content_comments` | R | body_format, cursor, id_, limit, payload, sort |
| `confluence_get_custom_content_content_properties` | R | cursor, custom_content_id, key, limit, payload, sort |
| `confluence_get_custom_content_content_properties_by_id` | R | custom_content_id, payload, property_id |
| `confluence_get_custom_content_labels` | R | cursor, id_, limit, payload, prefix, sort |
| `confluence_get_custom_content_operations` | R | id_, payload |
| `confluence_get_custom_content_version_details` | R | custom_content_id, payload, version_number |
| `confluence_get_custom_content_versions` | R | body_format, cursor, custom_content_id, limit, payload, sort |
| `confluence_get_database_ancestors` | R | id_, limit, payload |
| `confluence_get_database_by_id` | R | id_, include_collaborators, include_direct_children, include_operations, include_properties, payload |
| `confluence_get_database_content_properties` | R | cursor, id_, key, limit, payload, sort |
| `confluence_get_database_content_properties_by_id` | R | database_id, payload, property_id |
| `confluence_get_database_descendants` | R | cursor, depth, id_, limit, payload |
| `confluence_get_database_direct_children` | R | cursor, id_, limit, payload, sort |
| `confluence_get_database_operations` | R | id_, payload |
| `confluence_get_folder_ancestors` | R | id_, limit, payload |
| `confluence_get_folder_by_id` | R | id_, include_collaborators, include_direct_children, include_operations, include_properties, payload |
| `confluence_get_folder_content_properties` | R | cursor, id_, key, limit, payload, sort |
| `confluence_get_folder_content_properties_by_id` | R | folder_id, payload, property_id |
| `confluence_get_folder_descendants` | R | cursor, depth, id_, limit, payload |
| `confluence_get_folder_direct_children` | R | cursor, id_, limit, payload, sort |
| `confluence_get_folder_operations` | R | id_, payload |
| `confluence_get_footer_comment_by_id` | R | body_format, comment_id, include_likes, include_operations, include_properties, include_version, include_versions, payload |
| `confluence_get_footer_comment_children` | R | body_format, cursor, id_, limit, payload, sort |
| `confluence_get_footer_comment_operations` | R | id_, payload |
| `confluence_get_footer_comment_version_details` | R | id_, payload, version_number |
| `confluence_get_footer_comment_versions` | R | body_format, cursor, id_, limit, payload, sort |
| `confluence_get_footer_comments` | R | body_format, cursor, limit, payload, sort |
| `confluence_get_footer_like_count` | R | id_, payload |
| `confluence_get_footer_like_users` | R | cursor, id_, limit, payload |
| `confluence_get_inline_comment_by_id` | R | body_format, comment_id, include_likes, include_operations, include_properties, include_version, include_versions, payload |
| `confluence_get_inline_comment_children` | R | body_format, cursor, id_, limit, payload, sort |
| `confluence_get_inline_comment_operations` | R | id_, payload |
| `confluence_get_inline_comment_version_details` | R | id_, payload, version_number |
| `confluence_get_inline_comment_versions` | R | body_format, cursor, id_, limit, payload, sort |
| `confluence_get_inline_comments` | R | body_format, cursor, limit, payload, sort |
| `confluence_get_inline_like_count` | R | id_, payload |
| `confluence_get_inline_like_users` | R | cursor, id_, limit, payload |
| `confluence_get_label_attachments` | R | cursor, id_, limit, payload, sort |
| `confluence_get_label_blog_posts` | R | body_format, cursor, id_, limit, payload, sort, space_id |
| `confluence_get_label_pages` | R | body_format, cursor, id_, limit, payload, sort, space_id |
| `confluence_get_labels` | R | cursor, label_id, limit, payload, prefix, sort |
| `confluence_get_page_ancestors` | R | id_, limit, payload |
| `confluence_get_page_attachments` | R | cursor, filename, id_, limit, media_type, payload, sort, status |
| `confluence_get_page_by_id` | R | body_format, get_draft, id_, include_collaborators, include_direct_children, include_favorited_by_current_user_status, include_labels, include_likes |
| `confluence_get_page_content_properties` | R | cursor, key, limit, page_id, payload, sort |
| `confluence_get_page_content_properties_by_id` | R | page_id, payload, property_id |
| `confluence_get_page_descendants` | R | cursor, depth, id_, limit, payload |
| `confluence_get_page_direct_children` | R | cursor, id_, limit, payload, sort |
| `confluence_get_page_footer_comments` | R | body_format, cursor, id_, limit, payload, sort, status |
| `confluence_get_page_inline_comments` | R | body_format, cursor, id_, limit, payload, resolution_status, sort, status |
| `confluence_get_page_labels` | R | cursor, id_, limit, payload, prefix, sort |
| `confluence_get_page_like_count` | R | id_, payload |
| `confluence_get_page_like_users` | R | cursor, id_, limit, payload |
| `confluence_get_page_operations` | R | id_, payload |
| `confluence_get_page_version_details` | R | page_id, payload, version_number |
| `confluence_get_page_versions` | R | body_format, cursor, id_, limit, payload, sort |
| `confluence_get_pages` | R | body_format, cursor, id_, limit, payload, sort, space_id, status |
| `confluence_get_smart_link_ancestors` | R | id_, limit, payload |
| `confluence_get_smart_link_by_id` | R | id_, include_collaborators, include_direct_children, include_operations, include_properties, payload |
| `confluence_get_smart_link_content_properties` | R | cursor, id_, key, limit, payload, sort |
| `confluence_get_smart_link_content_properties_by_id` | R | embed_id, payload, property_id |
| `confluence_get_smart_link_descendants` | R | cursor, depth, id_, limit, payload |
| `confluence_get_smart_link_direct_children` | R | cursor, id_, limit, payload, sort |
| `confluence_get_smart_link_operations` | R | id_, payload |
| `confluence_get_task_by_id` | R | body_format, id_, payload |
| `confluence_get_tasks` | R | assigned_to, blogpost_id, body_format, completed_at_from, completed_at_to, completed_by, created_at_from, created_at_to |
| `confluence_get_whiteboard_ancestors` | R | id_, limit, payload |
| `confluence_get_whiteboard_by_id` | R | id_, include_collaborators, include_direct_children, include_operations, include_properties, payload |
| `confluence_get_whiteboard_content_properties` | R | cursor, id_, key, limit, payload, sort |
| `confluence_get_whiteboard_content_properties_by_id` | R | payload, property_id, whiteboard_id |
| `confluence_get_whiteboard_descendants` | R | cursor, depth, id_, limit, payload |
| `confluence_get_whiteboard_direct_children` | R | cursor, id_, limit, payload, sort |
| `confluence_get_whiteboard_operations` | R | id_, payload |
| `confluence_post_redact_blog` | W | id_, payload |
| `confluence_post_redact_page` | W | id_, payload |
| `confluence_update_attachment_property_by_id` | W | attachment_id, payload, property_id |
| `confluence_update_blog_post` | W | id_, payload |
| `confluence_update_blogpost_property_by_id` | W | blogpost_id, payload, property_id |
| `confluence_update_comment_property_by_id` | W | comment_id, payload, property_id |
| `confluence_update_custom_content` | W | id_, payload |
| `confluence_update_custom_content_property_by_id` | W | custom_content_id, payload, property_id |
| `confluence_update_database_property_by_id` | W | database_id, payload, property_id |
| `confluence_update_folder_property_by_id` | W | folder_id, payload, property_id |
| `confluence_update_footer_comment` | W | comment_id, payload |
| `confluence_update_inline_comment` | W | comment_id, payload |
| `confluence_update_page` | W | id_, payload |
| `confluence_update_page_property_by_id` | W | page_id, payload, property_id |
| `confluence_update_page_title` | W | id_, payload |
| `confluence_update_smart_link_property_by_id` | W | embed_id, payload, property_id |
| `confluence_update_task` | W | body_format, id_, payload |
| `confluence_update_whiteboard_property_by_id` | W | payload, property_id, whiteboard_id |

## Tasks

Each task is a tool-use contract the platform serves; steps run in this order.

- `confluence-content-attachment`: `confluence_get_attachments` -> `confluence_delete_attachment`
- `confluence-content-attachment-content`: `confluence_get_attachment_content_properties` -> `confluence_get_attachment_content_properties_by_id`
- `confluence-content-attachment-property`: `confluence_create_attachment_property` -> `confluence_update_attachment_property_by_id` -> `confluence_delete_attachment_property_by_id`
- `confluence-content-attachment-version`: `confluence_get_attachment_version_details` -> `confluence_get_attachment_versions`
- `confluence-content-blog-post`: `confluence_get_blog_post_by_id` -> `confluence_get_blog_post_footer_comments` -> `confluence_get_blog_post_inline_comments` -> `confluence_get_blog_post_labels` -> `confluence_get_blog_post_like_count` -> `confluence_get_blog_post_like_users` -> `confluence_get_blog_post_operations` -> `confluence_get_blog_post_version_details` -> `confluence_get_blog_post_versions` -> `confluence_get_blog_posts` -> `confluence_create_blog_post` -> `confluence_update_blog_post` -> `confluence_delete_blog_post`
- `confluence-content-blogpost-content`: `confluence_get_blogpost_content_properties` -> `confluence_get_blogpost_content_properties_by_id`
- `confluence-content-blogpost-property`: `confluence_create_blogpost_property` -> `confluence_update_blogpost_property_by_id` -> `confluence_delete_blogpost_property_by_id`
- `confluence-content-comment-content`: `confluence_get_comment_content_properties` -> `confluence_get_comment_content_properties_by_id`
- `confluence-content-comment-property`: `confluence_create_comment_property` -> `confluence_update_comment_property_by_id` -> `confluence_delete_comment_property_by_id`
- `confluence-content-custom-content`: `confluence_get_custom_content_attachments` -> `confluence_get_custom_content_by_id` -> `confluence_get_custom_content_by_type` -> `confluence_get_custom_content_by_type_in_blog_post` -> `confluence_get_custom_content_by_type_in_page` -> `confluence_get_custom_content_comments` -> `confluence_get_custom_content_content_properties` -> `confluence_get_custom_content_content_properties_by_id` -> `confluence_get_custom_content_labels` -> `confluence_get_custom_content_operations` -> `confluence_get_custom_content_version_details` -> `confluence_get_custom_content_versions` -> `confluence_create_custom_content` -> `confluence_create_custom_content_property` -> `confluence_update_custom_content` -> `confluence_update_custom_content_property_by_id` -> `confluence_delete_custom_content` -> `confluence_delete_custom_content_property_by_id`
- `confluence-content-database`: `confluence_create_database` -> `confluence_delete_database`
- `confluence-content-database-content`: `confluence_get_database_content_properties` -> `confluence_get_database_content_properties_by_id`
- `confluence-content-database-property`: `confluence_create_database_property` -> `confluence_update_database_property_by_id` -> `confluence_delete_database_property_by_id`
- `confluence-content-folder`: `confluence_create_folder` -> `confluence_delete_folder`
- `confluence-content-folder-content`: `confluence_get_folder_content_properties` -> `confluence_get_folder_content_properties_by_id`
- `confluence-content-folder-property`: `confluence_create_folder_property` -> `confluence_update_folder_property_by_id` -> `confluence_delete_folder_property_by_id`
- `confluence-content-footer-comment`: `confluence_get_footer_comment_by_id` -> `confluence_get_footer_comment_children` -> `confluence_get_footer_comment_operations` -> `confluence_get_footer_comment_version_details` -> `confluence_get_footer_comment_versions` -> `confluence_get_footer_comments` -> `confluence_create_footer_comment` -> `confluence_update_footer_comment` -> `confluence_delete_footer_comment`
- `confluence-content-footer-like`: `confluence_get_footer_like_count` -> `confluence_get_footer_like_users`
- `confluence-content-inline-comment`: `confluence_get_inline_comment_by_id` -> `confluence_get_inline_comment_children` -> `confluence_get_inline_comment_operations` -> `confluence_get_inline_comment_version_details` -> `confluence_get_inline_comment_versions` -> `confluence_get_inline_comments` -> `confluence_create_inline_comment` -> `confluence_update_inline_comment` -> `confluence_delete_inline_comment`
- `confluence-content-inline-like`: `confluence_get_inline_like_count` -> `confluence_get_inline_like_users`
- `confluence-content-page`: `confluence_get_pages` -> `confluence_create_page` -> `confluence_update_page` -> `confluence_delete_page`
- `confluence-content-page-content`: `confluence_get_page_content_properties` -> `confluence_get_page_content_properties_by_id`
- `confluence-content-page-like`: `confluence_get_page_like_count` -> `confluence_get_page_like_users`
- `confluence-content-page-property`: `confluence_create_page_property` -> `confluence_update_page_property_by_id` -> `confluence_delete_page_property_by_id`
- `confluence-content-page-version`: `confluence_get_page_version_details` -> `confluence_get_page_versions`
- `confluence-content-smart-link`: `confluence_get_smart_link_ancestors` -> `confluence_get_smart_link_by_id` -> `confluence_get_smart_link_content_properties` -> `confluence_get_smart_link_content_properties_by_id` -> `confluence_get_smart_link_descendants` -> `confluence_get_smart_link_direct_children` -> `confluence_get_smart_link_operations` -> `confluence_create_smart_link` -> `confluence_create_smart_link_property` -> `confluence_update_smart_link_property_by_id` -> `confluence_delete_smart_link` -> `confluence_delete_smart_link_property_by_id`
- `confluence-content-task`: `confluence_get_tasks` -> `confluence_update_task`
- `confluence-content-whiteboard`: `confluence_create_whiteboard` -> `confluence_delete_whiteboard`
- `confluence-content-whiteboard-content`: `confluence_get_whiteboard_content_properties` -> `confluence_get_whiteboard_content_properties_by_id`
- `confluence-content-whiteboard-property`: `confluence_create_whiteboard_property` -> `confluence_update_whiteboard_property_by_id` -> `confluence_delete_whiteboard_property_by_id`
- `confluence-content-read-records-1`: `confluence_get_attachment_by_id` -> `confluence_get_attachment_comments` -> `confluence_get_attachment_labels` -> `confluence_get_attachment_operations` -> `confluence_get_blogpost_attachments` -> `confluence_get_child_custom_content` -> `confluence_get_child_pages` -> `confluence_get_database_ancestors` -> `confluence_get_database_by_id` -> `confluence_get_database_descendants` -> `confluence_get_database_direct_children` -> `confluence_get_database_operations`
- `confluence-content-read-records-2`: `confluence_get_folder_ancestors` -> `confluence_get_folder_by_id` -> `confluence_get_folder_descendants` -> `confluence_get_folder_direct_children` -> `confluence_get_folder_operations` -> `confluence_get_label_attachments` -> `confluence_get_label_blog_posts` -> `confluence_get_label_pages` -> `confluence_get_labels` -> `confluence_get_page_ancestors` -> `confluence_get_page_attachments` -> `confluence_get_page_by_id`
- `confluence-content-read-records-3`: `confluence_get_page_descendants` -> `confluence_get_page_direct_children` -> `confluence_get_page_footer_comments` -> `confluence_get_page_inline_comments` -> `confluence_get_page_labels` -> `confluence_get_page_operations` -> `confluence_get_task_by_id` -> `confluence_get_whiteboard_ancestors` -> `confluence_get_whiteboard_by_id` -> `confluence_get_whiteboard_descendants` -> `confluence_get_whiteboard_direct_children` -> `confluence_get_whiteboard_operations`
- `confluence-content-change-records`: `confluence_convert_content_ids_to_content_types` -> `confluence_post_redact_blog` -> `confluence_post_redact_page` -> `confluence_update_page_title`
