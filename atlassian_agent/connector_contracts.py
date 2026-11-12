"""Surface contracts: tool use, links, data locations and business roles.

Generated from the served tool surface and edited as data; every tool is called by a step.
"""

# ruff: noqa: E501
from scion_sdk.surface_contracts import (
    BusinessRole,
    DataLocation,
    Refusal,
    SurfaceLink,
    ToolStep,
    ToolUseContract,
)

CONTRACTS = (
    ToolUseContract(
        task="confluence-content-attachment",
        description="Read and remove content attachment through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_attachments",
                params=(
                    "cursor",
                    "filename",
                    "limit",
                    "media_type",
                    "payload",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_attachment",
                params=("confirm", "id_", "payload", "purge"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-attachment-content",
        description="Read content attachment content through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_attachment_content_properties",
                params=("attachment_id", "cursor", "key", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_attachment_content_properties_by_id",
                params=("attachment_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-attachment-property",
        description="Create or change and remove content attachment property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_attachment_property",
                params=("attachment_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_update_attachment_property_by_id",
                params=("attachment_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_attachment_property_by_id",
                params=("attachment_id", "confirm", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-attachment-version",
        description="Read content attachment version through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_attachment_version_details",
                params=("attachment_id", "payload", "version_number"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_attachment_versions",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-blog-post",
        description="Read, create or change and remove content blog post through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_blog_post_by_id",
                params=(
                    "body_format",
                    "get_draft",
                    "id_",
                    "include_collaborators",
                    "include_favorited_by_current_user_status",
                    "include_labels",
                    "include_likes",
                    "include_operations",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_post_footer_comments",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_post_inline_comments",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "resolution_status",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_post_labels",
                params=("cursor", "id_", "limit", "payload", "prefix", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_post_like_count",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_post_like_users",
                params=("cursor", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_post_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_post_version_details",
                params=("blogpost_id", "payload", "version_number"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_post_versions",
                params=("body_format", "cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_posts",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "space_id",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_blog_post",
                params=("payload", "private"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_blog_post",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_blog_post",
                params=("confirm", "draft", "id_", "payload", "purge"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-blogpost-content",
        description="Read content blogpost content through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_blogpost_content_properties",
                params=("blogpost_id", "cursor", "key", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blogpost_content_properties_by_id",
                params=("blogpost_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-blogpost-property",
        description="Create or change and remove content blogpost property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_blogpost_property",
                params=("blogpost_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_update_blogpost_property_by_id",
                params=("blogpost_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_blogpost_property_by_id",
                params=("blogpost_id", "confirm", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-comment-content",
        description="Read content comment content through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_comment_content_properties",
                params=("comment_id", "cursor", "key", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_comment_content_properties_by_id",
                params=("comment_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-comment-property",
        description="Create or change and remove content comment property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_comment_property",
                params=("comment_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_update_comment_property_by_id",
                params=("comment_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_comment_property_by_id",
                params=("comment_id", "confirm", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-custom-content",
        description="Read, create or change and remove content custom content through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_custom_content_attachments",
                params=(
                    "cursor",
                    "filename",
                    "id_",
                    "limit",
                    "media_type",
                    "payload",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_by_id",
                params=(
                    "body_format",
                    "id_",
                    "include_collaborators",
                    "include_labels",
                    "include_operations",
                    "include_properties",
                    "include_version",
                    "include_versions",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_by_type",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "space_id",
                    "type_",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_by_type_in_blog_post",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "type_",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_by_type_in_page",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "type_",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_comments",
                params=("body_format", "cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_content_properties",
                params=(
                    "cursor",
                    "custom_content_id",
                    "key",
                    "limit",
                    "payload",
                    "sort",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_content_properties_by_id",
                params=("custom_content_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_labels",
                params=("cursor", "id_", "limit", "payload", "prefix", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_version_details",
                params=("custom_content_id", "payload", "version_number"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_versions",
                params=(
                    "body_format",
                    "cursor",
                    "custom_content_id",
                    "limit",
                    "payload",
                    "sort",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_custom_content",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_custom_content_property",
                params=("custom_content_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_update_custom_content",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_custom_content_property_by_id",
                params=("custom_content_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_custom_content",
                params=("confirm", "id_", "payload", "purge"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_custom_content_property_by_id",
                params=("confirm", "custom_content_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-database",
        description="Create or change and remove content database through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_database",
                params=("payload", "private"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_database",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-database-content",
        description="Read content database content through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_database_content_properties",
                params=("cursor", "id_", "key", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_database_content_properties_by_id",
                params=("database_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-database-property",
        description="Create or change and remove content database property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_database_property",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_database_property_by_id",
                params=("database_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_database_property_by_id",
                params=("confirm", "database_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-folder",
        description="Create or change and remove content folder through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_folder",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_folder",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-folder-content",
        description="Read content folder content through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_folder_content_properties",
                params=("cursor", "id_", "key", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_folder_content_properties_by_id",
                params=("folder_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-folder-property",
        description="Create or change and remove content folder property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_folder_property",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_folder_property_by_id",
                params=("folder_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_folder_property_by_id",
                params=("confirm", "folder_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-footer-comment",
        description="Read, create or change and remove content footer comment through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_footer_comment_by_id",
                params=(
                    "body_format",
                    "comment_id",
                    "include_likes",
                    "include_operations",
                    "include_properties",
                    "include_version",
                    "include_versions",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_footer_comment_children",
                params=("body_format", "cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_footer_comment_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_footer_comment_version_details",
                params=("id_", "payload", "version_number"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_footer_comment_versions",
                params=("body_format", "cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_footer_comments",
                params=("body_format", "cursor", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_footer_comment",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_footer_comment",
                params=("comment_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_footer_comment",
                params=("comment_id", "confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-footer-like",
        description="Read content footer like through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_footer_like_count",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_footer_like_users",
                params=("cursor", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-inline-comment",
        description="Read, create or change and remove content inline comment through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_inline_comment_by_id",
                params=(
                    "body_format",
                    "comment_id",
                    "include_likes",
                    "include_operations",
                    "include_properties",
                    "include_version",
                    "include_versions",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_inline_comment_children",
                params=("body_format", "cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_inline_comment_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_inline_comment_version_details",
                params=("id_", "payload", "version_number"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_inline_comment_versions",
                params=("body_format", "cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_inline_comments",
                params=("body_format", "cursor", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_inline_comment",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_inline_comment",
                params=("comment_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_inline_comment",
                params=("comment_id", "confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-inline-like",
        description="Read content inline like through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_inline_like_count",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_inline_like_users",
                params=("cursor", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-page",
        description="Read, create or change and remove content page through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_pages",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "space_id",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_page",
                params=("embedded", "payload", "private", "root_level"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_page",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_page",
                params=("confirm", "draft", "id_", "payload", "purge"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-page-content",
        description="Read content page content through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_page_content_properties",
                params=("cursor", "key", "limit", "page_id", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_content_properties_by_id",
                params=("page_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-page-like",
        description="Read content page like through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_page_like_count",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_like_users",
                params=("cursor", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-page-property",
        description="Create or change and remove content page property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_page_property",
                params=("page_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_update_page_property_by_id",
                params=("page_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_page_property_by_id",
                params=("confirm", "page_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-page-version",
        description="Read content page version through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_page_version_details",
                params=("page_id", "payload", "version_number"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_versions",
                params=("body_format", "cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-smart-link",
        description="Read, create or change and remove content smart link through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_smart_link_ancestors",
                params=("id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_smart_link_by_id",
                params=(
                    "id_",
                    "include_collaborators",
                    "include_direct_children",
                    "include_operations",
                    "include_properties",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_smart_link_content_properties",
                params=("cursor", "id_", "key", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_smart_link_content_properties_by_id",
                params=("embed_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_smart_link_descendants",
                params=("cursor", "depth", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_smart_link_direct_children",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_smart_link_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_smart_link",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_smart_link_property",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_smart_link_property_by_id",
                params=("embed_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_smart_link",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_smart_link_property_by_id",
                params=("confirm", "embed_id", "payload", "property_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-task",
        description="Read and create or change content task through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_tasks",
                params=(
                    "assigned_to",
                    "blogpost_id",
                    "body_format",
                    "completed_at_from",
                    "completed_at_to",
                    "completed_by",
                    "created_at_from",
                    "created_at_to",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_task",
                params=("body_format", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-whiteboard",
        description="Create or change and remove content whiteboard through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_whiteboard",
                params=("payload", "private"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_whiteboard",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-whiteboard-content",
        description="Read content whiteboard content through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_whiteboard_content_properties",
                params=("cursor", "id_", "key", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_whiteboard_content_properties_by_id",
                params=("payload", "property_id", "whiteboard_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-whiteboard-property",
        description="Create or change and remove content whiteboard property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_create_whiteboard_property",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_whiteboard_property_by_id",
                params=("payload", "property_id", "whiteboard_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_whiteboard_property_by_id",
                params=("confirm", "payload", "property_id", "whiteboard_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-platform-admin-key",
        description="Read, create or change and remove platform admin key through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_admin_key",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_disable_admin_key",
                params=("confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_enable_admin_key",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-platform-forge-app",
        description="Read, create or change and remove platform forge app through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_forge_app_properties",
                params=("cursor", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_forge_app_property",
                params=("payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_put_forge_app_property",
                params=("payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_forge_app_property",
                params=("confirm", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-available-space",
        description="Read spaces available space through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_available_space_permissions",
                params=("cursor", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_available_space_roles",
                params=(
                    "cursor",
                    "limit",
                    "payload",
                    "principal_id",
                    "principal_type",
                    "role_type",
                    "space_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-blog-post",
        description="Read and create or change spaces blog post through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_blog_post_classification_level",
                params=("id_", "payload", "status"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blog_posts_in_space",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "status",
                    "title",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_post_blog_post_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_put_blog_post_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-database-classification",
        description="Read and create or change spaces database classification through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_database_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_post_database_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_put_database_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-page-classification",
        description="Read and create or change spaces page classification through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_page_classification_level",
                params=("id_", "payload", "status"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_post_page_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_put_page_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-space",
        description="Read and create or change spaces space through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_spaces",
                params=(
                    "cursor",
                    "description_format",
                    "favorited_by",
                    "ids",
                    "include_icon",
                    "keys",
                    "labels",
                    "limit",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_space",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-space-default",
        description="Read, create or change and remove spaces space default through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_space_default_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_put_space_default_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_space_default_classification_level",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-space-property",
        description="Read, create or change and remove spaces space property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_space_properties",
                params=("cursor", "key", "limit", "payload", "space_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_space_property_by_id",
                params=("payload", "property_id", "space_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_space_property",
                params=("payload", "space_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_update_space_property_by_id",
                params=("payload", "property_id", "space_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="confluence_delete_space_property_by_id",
                params=("confirm", "payload", "property_id", "space_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-space-role",
        description="Read, create or change and remove spaces space role through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_space_role_assignments",
                params=(
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "principal_id",
                    "principal_type",
                    "role_id",
                    "role_type",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_space_role_mode",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_space_roles_by_id",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_space_role",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_set_space_role_assignments",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_space_role",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_delete_space_role",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-whiteboard-classification",
        description="Read and create or change spaces whiteboard classification through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_whiteboard_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_post_whiteboard_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_put_whiteboard_classification_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-api-key",
        description="Read and create or change api key through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="api_access_cloud_get_all_api_keys_by_org_id",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="api_access_cloud_get_api_key_count_by_org_id",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="api_access_cloud_revoke_api_key",
                params=("api_key_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-api-token",
        description="Read and remove api token through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="api_access_cloud_get_all_api_tokens_by_org_id",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="api_access_cloud_get_api_token_count_by_org_id",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="api_access_cloud_revoke_api_tokens",
                params=("account_id", "confirm", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-is-create",
        description="Create or change is create through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="control_cloud_ap_is_create_policy",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_create_policy_v2",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_create_resource",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-is-delete",
        description="Remove is delete through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="control_cloud_ap_is_delete_policy",
                params=("confirm", "org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_delete_resource",
                params=("confirm", "org_id", "payload", "policy_id", "resource_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_delete_resources",
                params=("confirm", "org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_delete_resources_v2",
                params=("confirm", "org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-is-get",
        description="Read is get through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="control_cloud_ap_is_get_policies",
                params=("cursor", "org_id", "payload", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_get_policies_v2",
                params=("cursor", "org_id", "payload", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_get_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_get_policy_v2",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_get_resources",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_get_resources_v2",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_get_task_status",
                params=("org_id", "payload", "task_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-is-update",
        description="Create or change is update through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="control_cloud_ap_is_update_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_update_policy_v2",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_update_resource",
                params=("org_id", "payload", "policy_id", "resource_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-level",
        description="Read and create or change level through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="dlp_cloud_get_level",
                params=("level_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="dlp_cloud_create_level",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="dlp_cloud_archive_level",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="dlp_cloud_edit_level",
                params=("level_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="dlp_cloud_publish_level",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="dlp_cloud_restore_level",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-service-account",
        description="Read and create or change service account through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="api_access_cloud_count_service_account_api_tokens",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="api_access_cloud_get_service_account_api_token",
                params=("account_id", "org_id", "payload", "token_label"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-dashboard",
        description="Read, create or change and remove boards dashboards dashboard through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_dashboards",
                params=("filter", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_dashboard",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_copy_dashboard",
                params=("extend_admin_permissions", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_dashboard",
                params=("extend_admin_permissions", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_dashboard",
                params=("extend_admin_permissions", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_dashboard",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-dashboard-item",
        description="Read, create or change and remove boards dashboards dashboard item through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_dashboard_item_property",
                params=("dashboard_id", "item_id", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_dashboard_item_property_keys",
                params=("dashboard_id", "item_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_dashboard_item_property",
                params=("dashboard_id", "item_id", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_dashboard_item_property",
                params=(
                    "confirm",
                    "dashboard_id",
                    "item_id",
                    "payload",
                    "property_key",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-favourite-filter",
        description="Read, create or change and remove boards dashboards favourite filter through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_favourite_filters",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_favourite_for_filter",
                params=("expand", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_favourite_for_filter",
                params=("confirm", "expand", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-filter",
        description="Read, create or change and remove boards dashboards filter through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_filter",
                params=("expand", "id_", "override_share_permissions", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_my_filters",
                params=("expand", "include_favourites", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_filter",
                params=("expand", "override_share_permissions", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_filter",
                params=("expand", "id_", "override_share_permissions", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_filter",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-gadget",
        description="Read, create or change and remove boards dashboards gadget through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_gadgets",
                params=("dashboard_id", "gadget_id", "module_key", "payload", "uri"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_gadget",
                params=("dashboard_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_gadget",
                params=("dashboard_id", "gadget_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_gadget",
                params=("confirm", "dashboard_id", "gadget_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-plan",
        description="Read and create or change boards dashboards plan through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_plan",
                params=("payload", "plan_id", "use_group_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_plans",
                params=(
                    "cursor",
                    "include_archived",
                    "include_trashed",
                    "max_results",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_plan",
                params=("payload", "use_group_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_duplicate_plan",
                params=("payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_trash_plan",
                params=("payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_archive_plan",
                params=("payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_plan",
                params=("payload", "plan_id", "use_group_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-plan-only",
        description="Read, create or change and remove boards dashboards plan only through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_plan_only_team",
                params=("payload", "plan_id", "plan_only_team_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_plan_only_team",
                params=("payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_plan_only_team",
                params=("payload", "plan_id", "plan_only_team_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_plan_only_team",
                params=("confirm", "payload", "plan_id", "plan_only_team_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-context-field",
        description="Read configuration context field through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_contexts_for_field",
                params=(
                    "context_id",
                    "field_id",
                    "is_any_issue_type",
                    "is_global_context",
                    "max_results",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_contexts_for_field_deprecated",
                params=("field_id", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-create-issue",
        description="Read configuration create issue through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_create_issue_meta_issue_type_id",
                params=(
                    "issue_type_id",
                    "max_results",
                    "payload",
                    "project_id_or_key",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_create_issue_meta_issue_types",
                params=("max_results", "payload", "project_id_or_key", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-custom-field",
        description="Read, create or change and remove configuration custom field through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_custom_field_configuration",
                params=(
                    "field_context_id",
                    "field_id_or_key",
                    "id_",
                    "issue_id",
                    "issue_type_id",
                    "max_results",
                    "payload",
                    "project_key_or_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_custom_field_contexts_for_projects_and_issue_types",
                params=("field_id", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_get_custom_field_option",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_custom_fields_configurations",
                params=(
                    "field_context_id",
                    "id_",
                    "issue_id",
                    "issue_type_id",
                    "max_results",
                    "payload",
                    "project_key_or_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_create_custom_field",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_custom_field_context",
                params=("field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_create_custom_field_option",
                params=("context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_trash_custom_field",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_reorder_custom_field_options",
                params=("context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_replace_custom_field_option",
                params=(
                    "confirm",
                    "context_id",
                    "field_id",
                    "jql",
                    "option_id",
                    "payload",
                    "replace_with",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_restore_custom_field",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_custom_field",
                params=("field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_custom_field_configuration",
                params=("field_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_custom_field_context",
                params=("context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_custom_field_option",
                params=("context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_custom_field_value",
                params=("field_id_or_key", "generate_changelog", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_custom_field",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_custom_field_context",
                params=("confirm", "context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_custom_field_option",
                params=("confirm", "context_id", "field_id", "option_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_custom_field_context_from_projects",
                params=("confirm", "context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-default-project",
        description="Read, create or change and remove configuration default project through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_default_project_classification",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_default_project_classification",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_default_project_classification",
                params=("confirm", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-default-share",
        description="Read and create or change configuration default share through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_default_share_scope",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_default_share_scope",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-default-value",
        description="Read and create or change configuration default value through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_default_values",
                params=("context_id", "field_id", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_default_values",
                params=("field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-default-workflow",
        description="Read, create or change and remove configuration default workflow through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_default_workflow",
                params=("id_", "payload", "return_draft_if_exists"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_default_workflow",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_default_workflow",
                params=("confirm", "id_", "payload", "update_draft_if_needed"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-draft-default",
        description="Read, create or change and remove configuration draft default through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_draft_default_workflow",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_draft_default_workflow",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_draft_default_workflow",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-draft-workflow",
        description="Read, create or change and remove configuration draft workflow through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_draft_workflow",
                params=("id_", "payload", "workflow_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_publish_draft_workflow_scheme",
                params=("id_", "payload", "validate_only"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_draft_workflow_mapping",
                params=("id_", "payload", "workflow_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_draft_workflow_mapping",
                params=("confirm", "id_", "payload", "workflow_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-field-associated",
        description="Create or change and remove configuration field associated through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_update_fields_associated_with_schemes",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_remove_fields_associated_with_schemes",
                params=("confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-field-association",
        description="Read, create or change and remove configuration field association through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_field_association_scheme_by_id",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_field_association_scheme_item_parameters",
                params=("field_id", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_field_association_schemes",
                params=("max_results", "payload", "project_id", "query", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_field_association_scheme_fields",
                params=("field_id", "id_", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_field_association_scheme_projects",
                params=("id_", "max_results", "payload", "project_id", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_clone_field_association_scheme",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_field_association_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_field_association_scheme",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_field_association_scheme_item_parameters",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_field_association_scheme",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_remove_field_association_scheme_item_parameters",
                params=("confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-field-configuration",
        description="Read, create or change and remove configuration field configuration through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_field_configuration_schemes",
                params=("id_", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_all_field_configurations",
                params=(
                    "id_",
                    "is_default",
                    "max_results",
                    "payload",
                    "query",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_field_configuration_items",
                params=("id_", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_field_configuration_scheme_mappings",
                params=(
                    "field_configuration_scheme_id",
                    "max_results",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_field_configuration_scheme_project_mapping",
                params=("max_results", "payload", "project_id", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_field_configuration",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_field_configuration_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_assign_field_configuration_scheme_to_project",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_field_configuration_scheme_mapping",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_field_configuration",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_field_configuration_items",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_field_configuration_scheme",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_field_configuration",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_field_configuration_scheme",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-issue-field",
        description="Read, create or change and remove configuration issue field through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_issue_field_options",
                params=("field_key", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_field_option",
                params=("field_key", "option_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_app_issue_field_value_update_resource_update_issue_fields_put",
                params=("atlassian_transfer_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_create_issue_field_option",
                params=("field_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_replace_issue_field_option",
                params=(
                    "confirm",
                    "field_key",
                    "jql",
                    "option_id",
                    "override_editable_flag",
                    "override_screen_security",
                    "payload",
                    "replace_with",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_issue_field_option",
                params=("field_key", "option_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue_field_option",
                params=("confirm", "field_key", "option_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-issue-link",
        description="Read, create or change and remove configuration issue link through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_issue_link_type",
                params=("issue_link_type_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_link_types",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_issue_link_type",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_issue_link_type",
                params=("issue_link_type_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue_link_type",
                params=("confirm", "issue_link_type_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-issue-navigator",
        description="Read and create or change configuration issue navigator through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_issue_navigator_default_columns",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_issue_navigator_default_columns",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-issue-security",
        description="Read and create or change configuration issue security through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_issue_security_level",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_security_level_members",
                params=(
                    "expand",
                    "issue_security_level_id",
                    "issue_security_scheme_id",
                    "max_results",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_security_scheme",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_security_schemes",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_issue_security_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_issue_security_scheme",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-issue-type",
        description="Read, create or change and remove configuration issue type through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_issue_type_schemes",
                params=(
                    "expand",
                    "id_",
                    "max_results",
                    "order_by",
                    "payload",
                    "query_string",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type_mappings_for_contexts",
                params=("context_id", "field_id", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type_property",
                params=("issue_type_id", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type_property_keys",
                params=("issue_type_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type_scheme_for_projects",
                params=("max_results", "payload", "project_id", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type_schemes_mapping",
                params=("issue_type_scheme_id", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type_screen_scheme_mappings",
                params=(
                    "issue_type_screen_scheme_id",
                    "max_results",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type_screen_scheme_project_associations",
                params=("max_results", "payload", "project_id", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_type_screen_schemes",
                params=(
                    "expand",
                    "id_",
                    "max_results",
                    "order_by",
                    "payload",
                    "query_string",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_types_for_project",
                params=("level", "payload", "project_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_issue_types_to_context",
                params=("context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_add_issue_types_to_issue_type_scheme",
                params=("issue_type_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_create_issue_type",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_issue_type_avatar",
                params=("id_", "payload", "size", "x", "y"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_issue_type_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_issue_type_screen_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_assign_issue_type_scheme_to_project",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_assign_issue_type_screen_scheme_to_project",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_reorder_issue_types_in_issue_type_scheme",
                params=("issue_type_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_set_issue_type_property",
                params=("issue_type_id", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_issue_type",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_issue_type_scheme",
                params=("issue_type_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_issue_type_screen_scheme",
                params=("issue_type_screen_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue_type",
                params=("alternative_issue_type_id", "confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue_type_property",
                params=("confirm", "issue_type_id", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue_type_scheme",
                params=("confirm", "issue_type_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue_type_screen_scheme",
                params=("confirm", "issue_type_screen_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_issue_type_from_issue_type_scheme",
                params=("confirm", "issue_type_id", "issue_type_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_issue_types_from_context",
                params=("confirm", "context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_issue_types_from_global_field_configuration_scheme",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-mapping-issue",
        description="Create or change and remove configuration mapping issue through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_append_mappings_for_issue_type_screen_scheme",
                params=("issue_type_screen_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_mappings_from_issue_type_screen_scheme",
                params=("confirm", "issue_type_screen_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-notification-scheme",
        description="Read, create or change and remove configuration notification scheme through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_notification_scheme",
                params=("expand", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_notification_scheme_for_project",
                params=("expand", "payload", "project_key_or_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_notification_scheme_to_project_mappings",
                params=(
                    "max_results",
                    "notification_scheme_id",
                    "payload",
                    "project_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_notification_schemes",
                params=(
                    "expand",
                    "id_",
                    "max_results",
                    "only_default",
                    "payload",
                    "project_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_notification_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_notification_scheme",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_notification_scheme",
                params=("confirm", "notification_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-permission-scheme",
        description="Read, create or change and remove configuration permission scheme through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_permission_schemes",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_permission_scheme",
                params=("expand", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_permission_scheme_grant",
                params=("expand", "payload", "permission_id", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_permission_scheme_grants",
                params=("expand", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_permission_scheme",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_assign_permission_scheme",
                params=("expand", "payload", "project_key_or_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_permission_scheme",
                params=("expand", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_permission_scheme",
                params=("confirm", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_permission_scheme_entity",
                params=("confirm", "payload", "permission_id", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-priority",
        description="Read, create or change and remove configuration priority through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_priorities",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_priority",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_priorities",
                params=(
                    "expand",
                    "id_",
                    "max_results",
                    "only_default",
                    "payload",
                    "priority_name",
                    "project_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_priority",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_move_priorities",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_priority",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_priority",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-priority-scheme",
        description="Read, create or change and remove configuration priority scheme through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_priority_schemes",
                params=(
                    "expand",
                    "max_results",
                    "only_default",
                    "order_by",
                    "payload",
                    "priority_id",
                    "scheme_id",
                    "scheme_name",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_priority_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_priority_scheme",
                params=("payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_priority_scheme",
                params=("confirm", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-project-custom",
        description="Create or change configuration project custom through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_create_project_with_custom_template",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_assign_projects_to_custom_field_context",
                params=("context_id", "field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-project-field",
        description="Read and create or change configuration project field through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_project_fields",
                params=(
                    "field_id",
                    "max_results",
                    "payload",
                    "project_id",
                    "start_at",
                    "work_type_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_projects_with_field_schemes",
                params=("max_results", "payload", "project_id", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_associate_projects_to_field_association_schemes",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-project-issue",
        description="Read configuration project issue through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_project_issue_security_scheme",
                params=("payload", "project_key_or_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_issue_type_usages_for_status",
                params=(
                    "max_results",
                    "next_page_token",
                    "payload",
                    "project_id",
                    "status_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_projects_for_issue_type_screen_scheme",
                params=(
                    "issue_type_screen_scheme_id",
                    "max_results",
                    "payload",
                    "query",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-project-usage",
        description="Read configuration project usage through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_project_usages_for_status",
                params=("max_results", "next_page_token", "payload", "status_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_usages_for_workflow",
                params=("max_results", "next_page_token", "payload", "workflow_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_usages_for_workflow_scheme",
                params=(
                    "max_results",
                    "next_page_token",
                    "payload",
                    "workflow_scheme_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-resolution",
        description="Read, create or change and remove configuration resolution through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_resolution",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_resolutions",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_resolutions",
                params=("id_", "max_results", "only_default", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_resolution",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_move_resolutions",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_resolution",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_resolution",
                params=("confirm", "id_", "payload", "replace_with"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-scheme-project",
        description="Create or change configuration scheme project through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_assign_scheme_to_project",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_associate_schemes_to_projects",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-screen",
        description="Read, create or change and remove configuration screen through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_screens",
                params=(
                    "id_",
                    "max_results",
                    "order_by",
                    "payload",
                    "query_string",
                    "scope",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_screen",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_screen",
                params=("payload", "screen_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_screen",
                params=("confirm", "payload", "screen_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-screen-scheme",
        description="Read, create or change and remove configuration screen scheme through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_screen_schemes",
                params=(
                    "expand",
                    "id_",
                    "max_results",
                    "order_by",
                    "payload",
                    "query_string",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_screen_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_screen_scheme",
                params=("payload", "screen_scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_screen_scheme",
                params=("confirm", "payload", "screen_scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-screen-tab",
        description="Read, create or change and remove configuration screen tab through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_screen_tab_fields",
                params=("payload", "project_key", "screen_id", "tab_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_all_screen_tabs",
                params=("payload", "project_key", "screen_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_screen_tab",
                params=("payload", "screen_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_add_screen_tab_field",
                params=("payload", "screen_id", "tab_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_rename_screen_tab",
                params=("payload", "screen_id", "tab_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_move_screen_tab",
                params=("payload", "pos", "screen_id", "tab_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_move_screen_tab_field",
                params=("id_", "payload", "screen_id", "tab_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_screen_tab",
                params=("confirm", "payload", "screen_id", "tab_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_screen_tab_field",
                params=("confirm", "id_", "payload", "screen_id", "tab_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-security-level",
        description="Read and create or change configuration security level through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_security_level_members",
                params=(
                    "expand",
                    "id_",
                    "level_id",
                    "max_results",
                    "payload",
                    "scheme_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_security_levels",
                params=(
                    "id_",
                    "max_results",
                    "only_default",
                    "payload",
                    "scheme_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_security_levels_for_project",
                params=("payload", "project_key_or_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_security_level",
                params=("payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_add_security_level_members",
                params=("level_id", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_security_level",
                params=("level_id", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-security-scheme",
        description="Read and remove configuration security scheme through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_search_security_schemes",
                params=("id_", "max_results", "payload", "project_id", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_security_scheme",
                params=("confirm", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-shared-time",
        description="Read and create or change configuration shared time through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_shared_time_tracking_configuration",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_shared_time_tracking_configuration",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-status",
        description="Read and create or change configuration status through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_statuses",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_status",
                params=("id_or_name", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_statuses",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_statuses",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_statuses",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-status-category",
        description="Read configuration status category through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_status_categories",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_status_category",
                params=("id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-status-id",
        description="Read and remove configuration status id through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_statuses_by_id",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_statuses_by_id",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-template",
        description="Read, create or change and remove configuration template through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_live_template",
                params=("payload", "project_id", "template_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_save_template",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_edit_template",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_remove_template",
                params=("confirm", "payload", "template_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-ui-modification",
        description="Read, create or change and remove configuration ui modification through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_ui_modifications",
                params=("expand", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_ui_modification",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_ui_modification",
                params=("payload", "ui_modification_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_ui_modification",
                params=("confirm", "payload", "ui_modification_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-user-default",
        description="Read configuration user default through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_users_default",
                params=("expand", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_user_default_columns",
                params=("account_id", "payload", "username"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-workflow",
        description="Read and create or change configuration workflow through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_workflows",
                params=("payload", "workflow_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow",
                params=("id_", "payload", "return_draft_if_exists", "workflow_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_read_workflows",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_workflows",
                params=(
                    "expand",
                    "is_active",
                    "max_results",
                    "order_by",
                    "payload",
                    "query_string",
                    "scope",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_workflow",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_workflows",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_workflows",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-workflow-history",
        description="Create or change configuration workflow history through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_list_workflow_history",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_read_workflow_from_history",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-workflow-mapping",
        description="Create or change and remove configuration workflow mapping through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_update_workflow_mapping",
                params=("id_", "payload", "workflow_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_workflow_mapping",
                params=(
                    "confirm",
                    "id_",
                    "payload",
                    "update_draft_if_needed",
                    "workflow_name",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-workflow-scheme",
        description="Read, create or change and remove configuration workflow scheme through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_workflow_schemes",
                params=("max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow_scheme",
                params=("id_", "payload", "return_draft_if_exists"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow_scheme_draft",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow_scheme_draft_issue_type",
                params=("id_", "issue_type", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow_scheme_issue_type",
                params=("id_", "issue_type", "payload", "return_draft_if_exists"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow_scheme_project_associations",
                params=("payload", "project_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow_scheme_usages_for_workflow",
                params=("max_results", "next_page_token", "payload", "workflow_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_read_workflow_schemes",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_workflow_scheme",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_workflow_scheme_draft_from_parent",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_switch_workflow_scheme_for_project",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_workflow_scheme_draft_issue_type",
                params=("id_", "issue_type", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_workflow_scheme_issue_type",
                params=("id_", "issue_type", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_workflow_scheme",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_workflow_scheme_draft",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_workflow_scheme",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_workflow_scheme_draft",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_workflow_scheme_draft_issue_type",
                params=("confirm", "id_", "issue_type", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_workflow_scheme_issue_type",
                params=(
                    "confirm",
                    "id_",
                    "issue_type",
                    "payload",
                    "update_draft_if_needed",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-workflow-transition",
        description="Read, create or change and remove configuration workflow transition through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_workflow_transition_properties",
                params=(
                    "include_reserved_keys",
                    "key",
                    "payload",
                    "transition_id",
                    "workflow_mode",
                    "workflow_name",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow_transition_rule_configurations",
                params=(
                    "draft",
                    "expand",
                    "keys",
                    "max_results",
                    "payload",
                    "start_at",
                    "types",
                    "with_tags",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_workflow_transition_property",
                params=(
                    "key",
                    "payload",
                    "transition_id",
                    "workflow_mode",
                    "workflow_name",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_workflow_transition_property",
                params=(
                    "key",
                    "payload",
                    "transition_id",
                    "workflow_mode",
                    "workflow_name",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_workflow_transition_rule_configurations",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_workflow_transition_property",
                params=(
                    "confirm",
                    "key",
                    "payload",
                    "transition_id",
                    "workflow_mode",
                    "workflow_name",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_workflow_transition_rule_configurations",
                params=("confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-application-property",
        description="Read and create or change issues application property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_application_property",
                params=("key", "key_filter", "payload", "permission_level"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_application_property",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-attachment",
        description="Read, create or change and remove issues attachment through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_attachment",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_attachment",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_attachment",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-comment",
        description="Read, create or change and remove issues comment through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_comment",
                params=("expand", "id_", "issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_comments",
                params=(
                    "expand",
                    "issue_id_or_key",
                    "max_results",
                    "order_by",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_comment",
                params=("expand", "issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_comment",
                params=(
                    "expand",
                    "id_",
                    "issue_id_or_key",
                    "notify_users",
                    "override_editable_flag",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_comment",
                params=("confirm", "id_", "issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-comment-property",
        description="Read, create or change and remove issues comment property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_comment_property",
                params=("comment_id", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_comment_property_keys",
                params=("comment_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_comment_property",
                params=("comment_id", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_comment_property",
                params=("comment_id", "confirm", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-forge-app",
        description="Read, create or change and remove issues forge app through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_forge_app_property",
                params=("payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_forge_app_property_keys",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_put_forge_app_property",
                params=("payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_forge_app_property",
                params=("confirm", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-ids-worklog",
        description="Read issues ids worklog through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_ids_of_worklogs_deleted_since",
                params=("payload", "since"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_ids_of_worklogs_modified_since",
                params=("expand", "payload", "since"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-issue",
        description="Read, create or change and remove issues issue through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_count_issues",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue",
                params=(
                    "expand",
                    "fields",
                    "fields_by_keys",
                    "issue_id_or_key",
                    "payload",
                    "properties",
                    "update_history",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_issue",
                params=("payload", "update_history"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_issues",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_link_issues",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_match_issues",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_archive_issues",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_assign_issue",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_edit_issue",
                params=(
                    "expand",
                    "issue_id_or_key",
                    "notify_users",
                    "override_editable_flag",
                    "override_screen_security",
                    "payload",
                    "return_issue",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue",
                params=("confirm", "delete_subtasks", "issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_unarchive_issues",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-issue-link",
        description="Read and remove issues issue link through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_issue_link",
                params=("link_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue_link",
                params=("confirm", "link_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-issue-property",
        description="Read, create or change and remove issues issue property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_issue_property",
                params=("issue_id_or_key", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_property_keys",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_issue_property",
                params=("issue_id_or_key", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_issue_property",
                params=("confirm", "issue_id_or_key", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-issue-using",
        description="Read and create or change issues issue using through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_search_for_issues_using_jql",
                params=(
                    "expand",
                    "fields",
                    "fields_by_keys",
                    "jql",
                    "max_results",
                    "payload",
                    "properties",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_for_issues_using_jql_post",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-jql-query",
        description="Create or change issues jql query through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_parse_jql_queries",
                params=("payload", "validation"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_sanitise_jql_queries",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-property-resource",
        description="Read, create or change and remove issues property resource through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_addon_properties_resource_delete_addon_property_delete",
                params=("addon_key", "confirm", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_addon_properties_resource_get_addon_property_get",
                params=("addon_key", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_addon_properties_resource_put_addon_property_put",
                params=("addon_key", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-reconsile-issue",
        description="Read and create or change issues reconsile issue through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_search_and_reconsile_issues_using_jql",
                params=(
                    "expand",
                    "fields",
                    "fields_by_keys",
                    "jql",
                    "max_results",
                    "next_page_token",
                    "payload",
                    "properties",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_and_reconsile_issues_using_jql_post",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-remote-issue",
        description="Read, create or change and remove issues remote issue through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_remote_issue_link_by_id",
                params=("issue_id_or_key", "link_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_remote_issue_links",
                params=("global_id", "issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_remote_issue_link",
                params=("issue_id_or_key", "link_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_remote_issue_link_by_global_id",
                params=("confirm", "global_id", "issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_remote_issue_link_by_id",
                params=("confirm", "issue_id_or_key", "link_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-set-issue",
        description="Create or change issues set issue through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_bulk_set_issue_properties_by_issue",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_bulk_set_issue_property",
                params=("payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_bulk_set_issues_properties_list",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-transition",
        description="Read and create or change issues transition through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_transitions",
                params=(
                    "expand",
                    "include_unavailable_transitions",
                    "issue_id_or_key",
                    "payload",
                    "skip_remote_only_condition",
                    "sort_by_ops_bar_and_status",
                    "transition_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_do_transition",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-vote",
        description="Read, create or change and remove issues vote through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_votes",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_vote",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_vote",
                params=("confirm", "issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-watcher",
        description="Create or change and remove issues watcher through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_add_watcher",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_watcher",
                params=(
                    "account_id",
                    "confirm",
                    "issue_id_or_key",
                    "payload",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-worklog",
        description="Read, create or change and remove issues worklog through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_worklog",
                params=("expand", "id_", "issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_worklog",
                params=(
                    "adjust_estimate",
                    "expand",
                    "issue_id_or_key",
                    "new_estimate",
                    "notify_users",
                    "override_editable_flag",
                    "payload",
                    "reduce_by",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_worklog",
                params=(
                    "adjust_estimate",
                    "expand",
                    "id_",
                    "issue_id_or_key",
                    "new_estimate",
                    "notify_users",
                    "override_editable_flag",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_worklog",
                params=(
                    "adjust_estimate",
                    "confirm",
                    "id_",
                    "increase_by",
                    "issue_id_or_key",
                    "new_estimate",
                    "notify_users",
                    "override_editable_flag",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-worklog-property",
        description="Read, create or change and remove issues worklog property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_worklog_property",
                params=("issue_id_or_key", "payload", "property_key", "worklog_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_worklog_property_keys",
                params=("issue_id_or_key", "payload", "worklog_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_worklog_property",
                params=("issue_id_or_key", "payload", "property_key", "worklog_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_worklog_property",
                params=(
                    "confirm",
                    "issue_id_or_key",
                    "payload",
                    "property_key",
                    "worklog_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-actor",
        description="Create or change and remove people access actor through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_set_actors",
                params=("id_", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_actor",
                params=(
                    "confirm",
                    "group",
                    "group_id",
                    "id_",
                    "payload",
                    "project_id_or_key",
                    "user",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-application-role",
        description="Read people access application role through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_application_roles",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_application_role",
                params=("key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-avatar",
        description="Read, create or change and remove people access avatar through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_avatars",
                params=("entity_id", "payload", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_store_avatar",
                params=("entity_id", "payload", "size", "type_", "x", "y"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_avatar",
                params=("confirm", "id_", "owning_object_id", "payload", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-avatar-image",
        description="Read people access avatar image through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_avatar_image_by_id",
                params=("format", "id_", "payload", "size", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_avatar_image_by_owner",
                params=("entity_id", "format", "payload", "size", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_avatar_image_by_type",
                params=("format", "payload", "size", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-get-user",
        description="Read people access get user through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_bulk_get_users",
                params=(
                    "account_id",
                    "key",
                    "max_results",
                    "payload",
                    "start_at",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_bulk_get_users_migration",
                params=("key", "max_results", "payload", "start_at", "username"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-group",
        description="Read, create or change and remove people access group through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_find_groups",
                params=(
                    "account_id",
                    "case_insensitive",
                    "exclude",
                    "exclude_id",
                    "max_results",
                    "payload",
                    "query",
                    "user_name",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_group",
                params=("expand", "group_id", "groupname", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_group",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_remove_group",
                params=(
                    "confirm",
                    "group_id",
                    "groupname",
                    "payload",
                    "swap_group",
                    "swap_group_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-permission",
        description="Read people access permission through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_permissions",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_my_permissions",
                params=(
                    "comment_id",
                    "issue_id",
                    "issue_key",
                    "payload",
                    "permissions",
                    "project_configuration_uuid",
                    "project_id",
                    "project_key",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-share-permission",
        description="Read, create or change and remove people access share permission through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_share_permission",
                params=("id_", "payload", "permission_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_share_permissions",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_share_permission",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_share_permission",
                params=("confirm", "id_", "payload", "permission_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-user",
        description="Read, create or change and remove people access user through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_find_users",
                params=(
                    "account_id",
                    "max_results",
                    "payload",
                    "property",
                    "query",
                    "start_at",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_all_users",
                params=("expand", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_user",
                params=("account_id", "expand", "key", "payload", "username"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_user",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_remove_user",
                params=("account_id", "confirm", "key", "payload", "username"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-user-column",
        description="Create or change and remove people access user column through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_reset_user_columns",
                params=("account_id", "confirm", "payload", "username"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_set_user_columns",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-user-email",
        description="Read people access user email through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_user_email",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_user_email_bulk",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-user-group",
        description="Read, create or change and remove people access user group through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_find_users_and_groups",
                params=(
                    "avatar_size",
                    "case_insensitive",
                    "exclude_connect_addons",
                    "field_id",
                    "issue_type_id",
                    "max_results",
                    "payload",
                    "project_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_user_groups",
                params=("account_id", "key", "payload", "username"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_users_from_group",
                params=(
                    "group_id",
                    "groupname",
                    "include_inactive_users",
                    "max_results",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_user_to_group",
                params=("group_id", "groupname", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_user_from_group",
                params=(
                    "account_id",
                    "confirm",
                    "group_id",
                    "groupname",
                    "payload",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-user-property",
        description="Read, create or change and remove people access user property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_user_property",
                params=(
                    "account_id",
                    "payload",
                    "property_key",
                    "user_key",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_user_property_keys",
                params=("account_id", "payload", "user_key", "username"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_user_property",
                params=(
                    "account_id",
                    "payload",
                    "property_key",
                    "user_key",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_user_property",
                params=(
                    "account_id",
                    "confirm",
                    "payload",
                    "property_key",
                    "user_key",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-association",
        description="Create or change and remove platform association through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_create_associations",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_remove_associations",
                params=("confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-atlassian-team",
        description="Read, create or change and remove platform atlassian team through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_atlassian_team",
                params=("atlassian_team_id", "payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_atlassian_team",
                params=("payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_atlassian_team",
                params=("atlassian_team_id", "payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_atlassian_team",
                params=("atlassian_team_id", "confirm", "payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-auto-complete",
        description="Read and create or change platform auto complete through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_auto_complete",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_auto_complete_post",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-banner",
        description="Read and create or change platform banner through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_banner",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_banner",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-change-log",
        description="Read and create or change platform change log through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_change_logs",
                params=("issue_id_or_key", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_change_logs_by_ids",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-column",
        description="Read, create or change and remove platform column through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_columns",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_reset_columns",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_columns",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-dynamic-webhook",
        description="Read and create or change platform dynamic webhook through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_dynamic_webhooks_for_app",
                params=("max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_register_dynamic_webhooks",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-forge-migration",
        description="Read and create or change platform forge migration through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get",
                params=("connect_key", "jira_issue_fields_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_connect_to_forge_migration_task_submission_resource_submit_task_post",
                params=("connect_key", "jira_issue_fields_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-locale",
        description="Read and create or change platform locale through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_locale",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_locale",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-module-resource",
        description="Read, create or change and remove platform module resource through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_dynamic_modules_resource_get_modules_get",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_dynamic_modules_resource_register_modules_post",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_dynamic_modules_resource_remove_modules_delete",
                params=("confirm", "module_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-policy",
        description="Read platform policy through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_policies",
                params=("ids", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_policy",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-precomputation",
        description="Read and create or change platform precomputation through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_precomputations",
                params=(
                    "function_key",
                    "max_results",
                    "order_by",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_precomputations",
                params=("payload", "skip_not_found_precomputations"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-preference",
        description="Read, create or change and remove platform preference through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_preference",
                params=("key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_preference",
                params=("key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_preference",
                params=("confirm", "key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-related-work",
        description="Read, create or change and remove platform related work through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_related_work",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_related_work",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_related_work",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_related_work",
                params=("confirm", "payload", "related_work_id", "version_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-task",
        description="Read and create or change platform task through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_task",
                params=("payload", "task_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_cancel_task",
                params=("payload", "task_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-accessible-project",
        description="Read projects accessible project through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_accessible_project_type_by_key",
                params=("payload", "project_type_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_all_accessible_project_types",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-component",
        description="Read, create or change and remove projects component through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_component",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_component",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_component",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_component",
                params=("confirm", "id_", "move_issues_to", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-feature-project",
        description="Read and create or change projects feature project through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_features_for_project",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_toggle_feature_for_project",
                params=("feature_key", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project",
        description="Read, create or change and remove projects project through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_projects",
                params=("expand", "payload", "properties", "recent"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project",
                params=("expand", "payload", "project_id_or_key", "properties"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_projects",
                params=(
                    "category_id",
                    "expand",
                    "id_",
                    "keys",
                    "max_results",
                    "order_by",
                    "payload",
                    "permission_action",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_project",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_archive_project",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_project",
                params=("expand", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_project",
                params=("confirm", "enable_undo", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project-avatar",
        description="Read, create or change and remove projects project avatar through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_project_avatars",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_project_avatar",
                params=("payload", "project_id_or_key", "size", "x", "y"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_project_avatar",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_project_avatar",
                params=("confirm", "id_", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project-category",
        description="Read, create or change and remove projects project category through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_project_categories",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_category_by_id",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_project_category",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_project_category",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_remove_project_category",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project-component",
        description="Read projects project component through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_project_components",
                params=("component_source", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_components_paginated",
                params=(
                    "component_source",
                    "max_results",
                    "order_by",
                    "payload",
                    "project_id_or_key",
                    "query",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project-email",
        description="Read and create or change projects project email through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_project_email",
                params=("payload", "project_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_project_email",
                params=("payload", "project_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project-property",
        description="Read, create or change and remove projects project property through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_project_property",
                params=("payload", "project_id_or_key", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_property_keys",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_project_property",
                params=("payload", "project_id_or_key", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_project_property",
                params=("confirm", "payload", "project_id_or_key", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project-role",
        description="Read, create or change and remove projects project role through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_project_roles",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_role",
                params=(
                    "exclude_inactive_users",
                    "id_",
                    "payload",
                    "project_id_or_key",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_role_actors_for_role",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_role_by_id",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_role_details",
                params=(
                    "current_member",
                    "exclude_connect_addons",
                    "exclude_other_service_roles",
                    "payload",
                    "project_id_or_key",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_roles",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_project_role_actors_to_role",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_project_role",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_project_role",
                params=("confirm", "id_", "payload", "swap"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_project_role_actors_from_role",
                params=("confirm", "group", "group_id", "id_", "payload", "user"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project-type",
        description="Read projects project type through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_project_types",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_type_by_key",
                params=("payload", "project_type_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-project-version",
        description="Read projects project version through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_project_versions",
                params=("expand", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_versions_paginated",
                params=(
                    "expand",
                    "max_results",
                    "order_by",
                    "payload",
                    "project_id_or_key",
                    "query",
                    "start_at",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-update-project",
        description="Create or change projects update project through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_fully_update_project_role",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_partial_update_project_role",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-valid-project",
        description="Read projects valid project through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_valid_project_key",
                params=("key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_valid_project_name",
                params=("name", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-version",
        description="Read, create or change and remove projects version through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_version",
                params=("expand", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_version",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_merge_versions",
                params=("id_", "move_issues_to", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_move_version",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_version",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_version",
                params=(
                    "confirm",
                    "id_",
                    "move_affected_issues_to",
                    "move_fix_issues_to",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="lifecycle-scim-link",
        description="Read and create or change scim link through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="user_provisioning_cloud_get_scim_links",
                params=("aa_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_scim_links_by_email",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="lifecycle-user-account",
        description="Read, create or change and remove user account through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="user_mgmt_cloud_get_users_account_id_manage",
                params=("account_id", "payload", "privileges"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_get_users_account_id_manage_api_tokens",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_get_users_account_id_manage_profile",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete",
                params=("account_id", "confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete",
                params=("account_id", "confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_patch_users_account_id_manage_profile",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_put_users_account_id_manage_email",
                params=("account_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id",
                params=("account_id", "confirm", "payload", "token_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="lifecycle-user-an",
        description="Read, create or change and remove user an through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="user_provisioning_cloud_get_users_from_an_active_directory",
                params=(
                    "attributes",
                    "count",
                    "directory_id",
                    "excluded_attributes",
                    "filter",
                    "payload",
                    "start_index",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_create_a_user_in_an_active_directory",
                params=("attributes", "directory_id", "excluded_attributes", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_delete_a_user_from_an_active_directory",
                params=("confirm", "directory_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="lifecycle-user-information",
        description="Create or change user information through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="user_provisioning_cloud_patch_user_information_in_an_active_directory",
                params=(
                    "attributes",
                    "directory_id",
                    "excluded_attributes",
                    "payload",
                    "user_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_update_user_information_in_an_active_directory",
                params=(
                    "attributes",
                    "directory_id",
                    "excluded_attributes",
                    "payload",
                    "user_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-directory-org",
        description="Read directory org through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_directories_for_org",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_directories_for_org",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-directory-user",
        description="Read directory user through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_directory_user_details",
                params=("directory_id", "org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_get_directory_users",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_get_directory_users_count",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_directory_user_details",
                params=("directory_id", "org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_directory_users",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_directory_users_count",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-domain",
        description="Read domain through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_domains",
                params=("cursor", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_domains",
                params=("cursor", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-domain-id",
        description="Read domain id through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_domain_by_id",
                params=("domain_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_domain_by_id",
                params=("domain_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-event",
        description="Read event through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_events",
                params=(
                    "actor",
                    "cursor",
                    "event_action",
                    "from_",
                    "ip",
                    "limit",
                    "location",
                    "org_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_events",
                params=(
                    "actor",
                    "cursor",
                    "event_action",
                    "from_",
                    "ip",
                    "limit",
                    "location",
                    "org_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_poll_events",
                params=(
                    "cursor",
                    "from_",
                    "limit",
                    "org_id",
                    "payload",
                    "sort_order",
                    "to",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_poll_events",
                params=(
                    "cursor",
                    "from_",
                    "limit",
                    "org_id",
                    "payload",
                    "sort_order",
                    "to",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-event-action",
        description="Read event action through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_event_actions",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_event_actions",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-event-id",
        description="Read event id through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_event_by_id",
                params=("event_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_event_by_id",
                params=("event_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-group",
        description="Read and create or change group through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_group",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_get_groups",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_search_groups",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_group",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_groups",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_search_groups",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-group-count",
        description="Read group count through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_groups_count",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_groups_count",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-group-role",
        description="Read group role through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_group_role_assignments",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_group_role_assignments",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-group-stat",
        description="Read group stat through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_groups_stats",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_groups_stats",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org",
        description="Read org through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_orgs",
                params=("cursor", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_orgs",
                params=("cursor", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-id",
        description="Read id through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_org_by_id",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_org_by_id",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-policy",
        description="Read, create or change and remove policy through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_policies",
                params=("cursor", "org_id", "payload", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_validate_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_policies",
                params=("cursor", "org_id", "payload", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_validate_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_create_policy",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_create_policy",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_update_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_update_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_delete_policy",
                params=("confirm", "org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_delete_policy",
                params=("confirm", "org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-policy-id",
        description="Read policy id through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_policy_by_id",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_policy_by_id",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-policy-resource",
        description="Create or change and remove policy resource through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_update_policy_resource",
                params=("org_id", "payload", "policy_id", "resource_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_update_policy_resource",
                params=("org_id", "payload", "policy_id", "resource_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_delete_policy_resource",
                params=("confirm", "org_id", "payload", "policy_id", "resource_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_delete_policy_resource",
                params=("confirm", "org_id", "payload", "policy_id", "resource_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-resource-policy",
        description="Create or change resource policy through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_add_resource_to_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_add_resource_to_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-role",
        description="Create or change role through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_assign_role",
                params=("org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_assign_role",
                params=("org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_revoke_role",
                params=("org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_revoke_role",
                params=("org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-role-group",
        description="Create or change role group through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_assign_role_to_group",
                params=("group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_assign_role_to_group",
                params=("group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_revoke_role_to_group",
                params=("group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_revoke_role_to_group",
                params=("group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-user",
        description="Read and create or change user through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_users",
                params=("cursor", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_search_users",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_users",
                params=("cursor", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_search_users",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-user-role",
        description="Read user role through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_user_role_assignments",
                params=("account_id", "directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_user_role_assignments",
                params=("account_id", "directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-user-stat",
        description="Read user stat through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_user_stats",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_user_stats",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-v1-org",
        description="Read, create or change and remove v1 org through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates",
                params=("account_id", "cursor", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates",
                params=("account_id", "cursor", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v1_orgs_org_id_directory_groups",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships",
                params=("group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access",
                params=("account_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access",
                params=("account_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v1_orgs_org_id_users_invite",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign",
                params=("org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke",
                params=("org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v1_orgs_org_id_directory_groups",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships",
                params=("group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access",
                params=("account_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access",
                params=("account_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v1_orgs_org_id_users_invite",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign",
                params=("org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke",
                params=("org_id", "payload", "user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id",
                params=(
                    "confirm",
                    "force_if_not_empty",
                    "group_id",
                    "org_id",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id",
                params=("account_id", "confirm", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_delete_v1_orgs_org_id_directory_users_account_id",
                params=("account_id", "confirm", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_delete_v1_orgs_org_id_directory_groups_group_id",
                params=(
                    "confirm",
                    "force_if_not_empty",
                    "group_id",
                    "org_id",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id",
                params=("account_id", "confirm", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_delete_v1_orgs_org_id_directory_users_account_id",
                params=("account_id", "confirm", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-v2-org",
        description="Create or change and remove v2 org through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore",
                params=("account_id", "directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend",
                params=("account_id", "directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_post_v2_orgs_org_id_users_invite",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v2_orgs_org_id_directories_directory_id_groups",
                params=("directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke",
                params=("directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore",
                params=("account_id", "directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend",
                params=("account_id", "directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_post_v2_orgs_org_id_users_invite",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id",
                params=("confirm", "directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id",
                params=(
                    "account_id",
                    "confirm",
                    "directory_id",
                    "group_id",
                    "org_id",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id",
                params=("account_id", "confirm", "directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id",
                params=("confirm", "directory_id", "group_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id",
                params=(
                    "account_id",
                    "confirm",
                    "directory_id",
                    "group_id",
                    "org_id",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id",
                params=("account_id", "confirm", "directory_id", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="org-workspace-v2",
        description="Create or change workspace v2 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="admin_cloud_query_workspaces_v2",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="org_cloud_query_workspaces_v2",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-read-records-1",
        description="Read content read records 1 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_attachment_by_id",
                params=(
                    "id_",
                    "include_collaborators",
                    "include_labels",
                    "include_operations",
                    "include_properties",
                    "include_version",
                    "include_versions",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_attachment_comments",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "version",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_attachment_labels",
                params=("cursor", "id_", "limit", "payload", "prefix", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_attachment_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_blogpost_attachments",
                params=(
                    "cursor",
                    "filename",
                    "id_",
                    "limit",
                    "media_type",
                    "payload",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_child_custom_content",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_child_pages",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_database_ancestors",
                params=("id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_database_by_id",
                params=(
                    "id_",
                    "include_collaborators",
                    "include_direct_children",
                    "include_operations",
                    "include_properties",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_database_descendants",
                params=("cursor", "depth", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_database_direct_children",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_database_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-read-records-2",
        description="Read content read records 2 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_folder_ancestors",
                params=("id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_folder_by_id",
                params=(
                    "id_",
                    "include_collaborators",
                    "include_direct_children",
                    "include_operations",
                    "include_properties",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_folder_descendants",
                params=("cursor", "depth", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_folder_direct_children",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_folder_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_label_attachments",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_label_blog_posts",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "space_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_label_pages",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "space_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_labels",
                params=("cursor", "label_id", "limit", "payload", "prefix", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_ancestors",
                params=("id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_attachments",
                params=(
                    "cursor",
                    "filename",
                    "id_",
                    "limit",
                    "media_type",
                    "payload",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_by_id",
                params=(
                    "body_format",
                    "get_draft",
                    "id_",
                    "include_collaborators",
                    "include_direct_children",
                    "include_favorited_by_current_user_status",
                    "include_labels",
                    "include_likes",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-read-records-3",
        description="Read content read records 3 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_page_descendants",
                params=("cursor", "depth", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_direct_children",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_footer_comments",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_inline_comments",
                params=(
                    "body_format",
                    "cursor",
                    "id_",
                    "limit",
                    "payload",
                    "resolution_status",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_labels",
                params=("cursor", "id_", "limit", "payload", "prefix", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_page_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_task_by_id",
                params=("body_format", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_whiteboard_ancestors",
                params=("id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_whiteboard_by_id",
                params=(
                    "id_",
                    "include_collaborators",
                    "include_direct_children",
                    "include_operations",
                    "include_properties",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_whiteboard_descendants",
                params=("cursor", "depth", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_whiteboard_direct_children",
                params=("cursor", "id_", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_whiteboard_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-content-change-records",
        description="Create or change content change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_convert_content_ids_to_content_types",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_post_redact_blog",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_post_redact_page",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_update_page_title",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-platform-read-records",
        description="Read platform read records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_data_policy_metadata",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-platform-change-records",
        description="Create or change platform change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_check_access_by_email",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_create_bulk_user_lookup",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_invite_by_email",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-read-records",
        description="Read spaces read records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_get_calendars",
                params=("end", "payload", "start", "sub_calendar_id", "time_zone_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_classification_levels",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_custom_content_by_type_in_space",
                params=("body_format", "cursor", "id_", "limit", "payload", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_data_policy_spaces",
                params=("cursor", "ids", "keys", "limit", "payload", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_pages_in_space",
                params=(
                    "body_format",
                    "cursor",
                    "depth",
                    "id_",
                    "limit",
                    "payload",
                    "sort",
                    "status",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_space_by_id",
                params=(
                    "description_format",
                    "id_",
                    "include_icon",
                    "include_labels",
                    "include_operations",
                    "include_permissions",
                    "include_properties",
                    "include_role_assignments",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_space_content_labels",
                params=("cursor", "id_", "limit", "payload", "prefix", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_space_labels",
                params=("cursor", "id_", "limit", "payload", "prefix", "sort"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_space_operations",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="confluence_get_space_permissions_assignments",
                params=("cursor", "id_", "limit", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="confluence-spaces-change-records",
        description="Create or change spaces change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="confluence_add_calendar_event",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-read-records",
        description="Read read records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="control_cloud_ap_is_validate_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="dlp_cloud_get_level_list",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="controls-change-records",
        description="Create or change and remove change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="control_cloud_ap_is_add_users_to_policy",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_attach_detach_resources_v2",
                params=("org_id", "payload", "policy_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_bulk_fetch_auth_policy",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="control_cloud_ap_is_publish_draft_policies",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="api_access_cloud_bulk_revoke_api_tokens",
                params=("confirm", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="dlp_cloud_reorder",
                params=("org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-read-records",
        description="Read boards dashboards read records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_all_available_dashboard_gadgets",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_dashboards_paginated",
                params=(
                    "account_id",
                    "dashboard_name",
                    "expand",
                    "group_id",
                    "groupname",
                    "max_results",
                    "order_by",
                    "owner",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_filters_paginated",
                params=(
                    "account_id",
                    "expand",
                    "filter_name",
                    "group_id",
                    "groupname",
                    "id_",
                    "is_substring_match",
                    "max_results",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-boards-dashboards-change-records",
        description="Create or change boards dashboards change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_bulk_edit_dashboards",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_change_filter_owner",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-read-records-1",
        description="Read configuration read records 1 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_alternative_issue_types",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_assigned_permission_scheme",
                params=("expand", "payload", "project_key_or_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_available_priorities_by_priority_scheme",
                params=(
                    "exclude",
                    "max_results",
                    "payload",
                    "query",
                    "scheme_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_available_screen_fields",
                params=("payload", "screen_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_available_time_tracking_implementations",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_bulk_editable_fields",
                params=(
                    "ending_before",
                    "issue_ids_or_keys",
                    "payload",
                    "search_text",
                    "starting_after",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_bulk_screen_tabs",
                params=("max_result", "payload", "screen_id", "start_at", "tab_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_configuration",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_default_editor",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_field_auto_complete_for_query_string",
                params=(
                    "field_name",
                    "field_value",
                    "payload",
                    "predicate_name",
                    "predicate_value",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_field_project_associations",
                params=("field_id", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_fields",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-read-records-2",
        description="Read configuration read records 2 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_fields_paginated",
                params=(
                    "expand",
                    "id_",
                    "max_results",
                    "order_by",
                    "payload",
                    "project_ids",
                    "query",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_options_for_context",
                params=(
                    "context_id",
                    "field_id",
                    "max_results",
                    "only_options",
                    "option_id",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_priorities_by_priority_scheme",
                params=("max_results", "payload", "scheme_id", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_context_mapping",
                params=("context_id", "field_id", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_projects_by_priority_scheme",
                params=(
                    "max_results",
                    "payload",
                    "project_id",
                    "query",
                    "scheme_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_redaction_status",
                params=("job_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_screens_for_field",
                params=("expand", "field_id", "max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_selectable_issue_field_options",
                params=(
                    "field_key",
                    "max_results",
                    "payload",
                    "project_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_selected_time_tracking_implementation",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_statuses_by_name",
                params=("name", "payload", "project_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_trashed_fields_paginated",
                params=(
                    "expand",
                    "id_",
                    "max_results",
                    "order_by",
                    "payload",
                    "query",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_visible_issue_field_options",
                params=(
                    "field_key",
                    "max_results",
                    "payload",
                    "project_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-read-records-3",
        description="Read configuration read records 3 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_workflow_project_issue_type_usages",
                params=(
                    "max_results",
                    "next_page_token",
                    "payload",
                    "project_id",
                    "workflow_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflow_usages_for_status",
                params=("max_results", "next_page_token", "payload", "status_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_workflows_paginated",
                params=(
                    "expand",
                    "is_active",
                    "max_results",
                    "order_by",
                    "payload",
                    "query_string",
                    "start_at",
                    "workflow_name",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search_projects_using_security_schemes",
                params=(
                    "issue_security_scheme_id",
                    "max_results",
                    "payload",
                    "project_id",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_workflow_capabilities",
                params=("issue_type_id", "payload", "project_id", "workflow_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-change-records-1",
        description="Create or change configuration change records 1 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_required_workflow_scheme_mappings",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_read_workflow_previews",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_validate_create_workflows",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_validate_update_workflows",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_field_to_default_screen",
                params=("field_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_add_notifications",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_migration_resource_workflow_rule_search_post",
                params=("atlassian_transfer_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_select_time_tracking_implementation",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_suggested_priorities_for_mappings",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_default_levels",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_default_priority",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_set_default_resolution",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-configuration-change-records-2",
        description="Create or change and remove configuration change records 2 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_update_default_screen_scheme",
                params=("issue_type_screen_scheme_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_update_multiple_custom_field_values",
                params=("generate_changelog", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_update_schemes",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_inactive_workflow",
                params=("confirm", "entity_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_member_from_security_level",
                params=("confirm", "level_id", "member_id", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_remove_notification_from_notification_scheme",
                params=(
                    "confirm",
                    "notification_id",
                    "notification_scheme_id",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-read-records-1",
        description="Read issues read records 1 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_expand_attachment_for_humans",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_expand_attachment_for_machines",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_all_labels",
                params=("max_results", "payload", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_approximate_application_license_count",
                params=("application_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_approximate_license_count",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_attachment_content",
                params=("id_", "payload", "redirect"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_attachment_meta",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_attachment_thumbnail",
                params=(
                    "fallback_to_default",
                    "height",
                    "id_",
                    "payload",
                    "redirect",
                    "width",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_available_transitions",
                params=(
                    "ending_before",
                    "issue_ids_or_keys",
                    "payload",
                    "starting_after",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_bulk_operation_progress",
                params=("payload", "task_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_create_issue_meta",
                params=(
                    "expand",
                    "issuetype_ids",
                    "issuetype_names",
                    "payload",
                    "project_ids",
                    "project_keys",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_edit_issue_meta",
                params=(
                    "issue_id_or_key",
                    "override_editable_flag",
                    "override_screen_security",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-read-records-2",
        description="Read issues read records 2 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_issue_all_types",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_limit_report",
                params=("is_returning_keys", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_picker_resource",
                params=(
                    "current_issue_key",
                    "current_jql",
                    "current_project_id",
                    "payload",
                    "query",
                    "show_sub_task_parent",
                    "show_sub_tasks",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_watchers",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_issue_worklog",
                params=(
                    "expand",
                    "issue_id_or_key",
                    "max_results",
                    "payload",
                    "start_at",
                    "started_after",
                    "started_before",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_search",
                params=(
                    "max_results",
                    "payload",
                    "project_id",
                    "search_string",
                    "start_at",
                    "status_category",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-change-records-1",
        description="Create or change and remove issues change records 1 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_bulk_changelogs",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_comments_by_ids",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_is_watching_issue_bulk",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_worklogs_by_issue_id_and_worklog_id",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_worklogs_for_ids",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_create_or_update_remote_issue_link",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_export_archived_issues",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_submit_bulk_delete",
                params=("confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_submit_bulk_edit",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_submit_bulk_move",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_submit_bulk_transition",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_submit_bulk_unwatch",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-issues-change-records-2",
        description="Create or change and remove issues change records 2 through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_submit_bulk_watch",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_archive_issues_async",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_bulk_delete_issue_property",
                params=("confirm", "payload", "property_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_bulk_delete_worklogs",
                params=(
                    "adjust_estimate",
                    "confirm",
                    "issue_id_or_key",
                    "override_editable_flag",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_bulk_fetch_issues",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_bulk_move_worklogs",
                params=(
                    "adjust_estimate",
                    "issue_id_or_key",
                    "override_editable_flag",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-read-records",
        description="Read people access read records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_bulk_get_groups",
                params=(
                    "access_type",
                    "application_key",
                    "group_id",
                    "group_name",
                    "max_results",
                    "payload",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_find_assignable_users",
                params=(
                    "account_id",
                    "account_type",
                    "action_descriptor_id",
                    "app_type",
                    "issue_id",
                    "issue_key",
                    "max_results",
                    "payload",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_find_bulk_assignable_users",
                params=(
                    "account_id",
                    "max_results",
                    "payload",
                    "project_keys",
                    "query",
                    "start_at",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_find_user_keys_by_query",
                params=("max_result", "payload", "query", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_find_users_by_query",
                params=("max_results", "payload", "query", "start_at"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_find_users_for_picker",
                params=(
                    "avatar_size",
                    "exclude",
                    "exclude_account_ids",
                    "exclude_connect_users",
                    "max_results",
                    "payload",
                    "query",
                    "show_avatar",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_find_users_with_all_permissions",
                params=(
                    "account_id",
                    "issue_key",
                    "max_results",
                    "payload",
                    "permissions",
                    "project_key",
                    "query",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_find_users_with_browse_permission",
                params=(
                    "account_id",
                    "issue_key",
                    "max_results",
                    "payload",
                    "project_key",
                    "query",
                    "start_at",
                    "username",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_all_system_avatars",
                params=("payload", "type_"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_all_user_data_classification_levels",
                params=("order_by", "payload", "status"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_current_user",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-people-access-change-records",
        description="Create or change people access change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_bulk_permissions",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_add_actor_users",
                params=("id_", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_create_permission_grant",
                params=("expand", "payload", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-read-records",
        description="Read platform read records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_addon_properties_resource_get_addon_properties_get",
                params=("addon_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_advanced_settings",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_audit_records",
                params=("filter", "from_", "limit", "offset", "payload", "to"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_events",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_failed_webhooks",
                params=("after", "max_results", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_hierarchy",
                params=("payload", "project_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_license",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_recent",
                params=("expand", "payload", "properties"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_server_info",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_teams",
                params=("cursor", "max_results", "payload", "plan_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_service_registry_resource_services_get",
                params=("payload", "service_ids"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-platform-change-records",
        description="Create or change and remove platform change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_analyse_expression",
                params=("check", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_evaluate_jira_expression",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_evaluate_jsis_jira_expression",
                params=("expand", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_precomputations_by_id",
                params=("order_by", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_migrate_queries",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_migration_resource_update_entity_properties_value_put",
                params=("atlassian_transfer_id", "entity_type", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_notify",
                params=("issue_id_or_key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_redact",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_refresh_webhooks",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_restore",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="jira_delete_webhook_by_id",
                params=("confirm", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_remove_level",
                params=("confirm", "level_id", "payload", "replace_with", "scheme_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-read-records",
        description="Read projects read records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_find_components_for_projects",
                params=(
                    "max_results",
                    "order_by",
                    "payload",
                    "project_ids_or_keys",
                    "query",
                    "start_at",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_component_related_issues",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_project_classification_config",
                params=("payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_version_related_issues",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_get_version_unresolved_issues",
                params=("id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the permission this read requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_validate_project_key",
                params=("key", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="jira-projects-change-records",
        description="Create or change and remove projects change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="jira_get_permitted_projects",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_bulk_pin_unpin_projects_async",
                params=("payload",),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_and_replace_version",
                params=("confirm", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                ),
            ),
            ToolStep(
                tool="jira_delete_project_asynchronously",
                params=("confirm", "payload", "project_id_or_key"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="kg-change-records",
        description="Create or change change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="atlassian_ingest_confluence",
                params=("limit", "space_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="atlassian_ingest_issues",
                params=("jql", "max_results"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="lifecycle-read-records",
        description="Read read records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="user_provisioning_cloud_get",
                params=("directory_id", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_a_user_from_active_directory",
                params=(
                    "attributes",
                    "directory_id",
                    "excluded_attributes",
                    "payload",
                    "user_id",
                ),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_all_groups_from_an_active_directory",
                params=("count", "directory_id", "filter", "payload", "start_index"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_config",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_extension_user_schemas",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_group_resource_type",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_group_schemas",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_resource_types",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_schemas",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_user_resource_type",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_get_user_schemas",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="NOT_FOUND",
                        when="the target record does not exist or is not visible to the caller",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        task="lifecycle-change-records",
        description="Create or change and remove change records through their typed operations, in dependency order.",
        steps=(
            ToolStep(
                tool="user_provisioning_cloud_create_a_group_in_active_directory",
                params=("directory_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_unlink_scim_user",
                params=("org_id", "payload", "scim_directory_id", "scim_user_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_patch",
                params=("directory_id", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_put",
                params=("directory_id", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks the product permission this change requires",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_delete_a_group",
                params=("confirm", "directory_id", "id_", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
            ToolStep(
                tool="user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db",
                params=("aaid", "confirm", "org_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        code="FORBIDDEN",
                        when="the caller lacks permission, or approval for this destructive call is missing",
                    ),
                    Refusal(code="NOT_FOUND", when="the target record does not exist"),
                ),
            ),
        ),
    ),
)

LINKS = (
    SurfaceLink(
        "confluence-content-attachment",
        tools=("confluence_get_attachments", "confluence_delete_attachment"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-attachment-content",
        tools=(
            "confluence_get_attachment_content_properties",
            "confluence_get_attachment_content_properties_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-attachment-property",
        tools=(
            "confluence_create_attachment_property",
            "confluence_update_attachment_property_by_id",
            "confluence_delete_attachment_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-attachment-version",
        tools=(
            "confluence_get_attachment_version_details",
            "confluence_get_attachment_versions",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-blog-post",
        tools=(
            "confluence_get_blog_post_by_id",
            "confluence_get_blog_post_footer_comments",
            "confluence_get_blog_post_inline_comments",
            "confluence_get_blog_post_labels",
            "confluence_get_blog_post_like_count",
            "confluence_get_blog_post_like_users",
            "confluence_get_blog_post_operations",
            "confluence_get_blog_post_version_details",
            "confluence_get_blog_post_versions",
            "confluence_get_blog_posts",
            "confluence_create_blog_post",
            "confluence_update_blog_post",
            "confluence_delete_blog_post",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-blogpost-content",
        tools=(
            "confluence_get_blogpost_content_properties",
            "confluence_get_blogpost_content_properties_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-blogpost-property",
        tools=(
            "confluence_create_blogpost_property",
            "confluence_update_blogpost_property_by_id",
            "confluence_delete_blogpost_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-comment-content",
        tools=(
            "confluence_get_comment_content_properties",
            "confluence_get_comment_content_properties_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-comment-property",
        tools=(
            "confluence_create_comment_property",
            "confluence_update_comment_property_by_id",
            "confluence_delete_comment_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-custom-content",
        tools=(
            "confluence_get_custom_content_attachments",
            "confluence_get_custom_content_by_id",
            "confluence_get_custom_content_by_type",
            "confluence_get_custom_content_by_type_in_blog_post",
            "confluence_get_custom_content_by_type_in_page",
            "confluence_get_custom_content_comments",
            "confluence_get_custom_content_content_properties",
            "confluence_get_custom_content_content_properties_by_id",
            "confluence_get_custom_content_labels",
            "confluence_get_custom_content_operations",
            "confluence_get_custom_content_version_details",
            "confluence_get_custom_content_versions",
            "confluence_create_custom_content",
            "confluence_create_custom_content_property",
            "confluence_update_custom_content",
            "confluence_update_custom_content_property_by_id",
            "confluence_delete_custom_content",
            "confluence_delete_custom_content_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-database",
        tools=("confluence_create_database", "confluence_delete_database"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-database-content",
        tools=(
            "confluence_get_database_content_properties",
            "confluence_get_database_content_properties_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-database-property",
        tools=(
            "confluence_create_database_property",
            "confluence_update_database_property_by_id",
            "confluence_delete_database_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-folder",
        tools=("confluence_create_folder", "confluence_delete_folder"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-folder-content",
        tools=(
            "confluence_get_folder_content_properties",
            "confluence_get_folder_content_properties_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-folder-property",
        tools=(
            "confluence_create_folder_property",
            "confluence_update_folder_property_by_id",
            "confluence_delete_folder_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-footer-comment",
        tools=(
            "confluence_get_footer_comment_by_id",
            "confluence_get_footer_comment_children",
            "confluence_get_footer_comment_operations",
            "confluence_get_footer_comment_version_details",
            "confluence_get_footer_comment_versions",
            "confluence_get_footer_comments",
            "confluence_create_footer_comment",
            "confluence_update_footer_comment",
            "confluence_delete_footer_comment",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-footer-like",
        tools=("confluence_get_footer_like_count", "confluence_get_footer_like_users"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-inline-comment",
        tools=(
            "confluence_get_inline_comment_by_id",
            "confluence_get_inline_comment_children",
            "confluence_get_inline_comment_operations",
            "confluence_get_inline_comment_version_details",
            "confluence_get_inline_comment_versions",
            "confluence_get_inline_comments",
            "confluence_create_inline_comment",
            "confluence_update_inline_comment",
            "confluence_delete_inline_comment",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-inline-like",
        tools=("confluence_get_inline_like_count", "confluence_get_inline_like_users"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-page",
        tools=(
            "confluence_get_pages",
            "confluence_create_page",
            "confluence_update_page",
            "confluence_delete_page",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-page-content",
        tools=(
            "confluence_get_page_content_properties",
            "confluence_get_page_content_properties_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-page-like",
        tools=("confluence_get_page_like_count", "confluence_get_page_like_users"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-page-property",
        tools=(
            "confluence_create_page_property",
            "confluence_update_page_property_by_id",
            "confluence_delete_page_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-page-version",
        tools=("confluence_get_page_version_details", "confluence_get_page_versions"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-smart-link",
        tools=(
            "confluence_get_smart_link_ancestors",
            "confluence_get_smart_link_by_id",
            "confluence_get_smart_link_content_properties",
            "confluence_get_smart_link_content_properties_by_id",
            "confluence_get_smart_link_descendants",
            "confluence_get_smart_link_direct_children",
            "confluence_get_smart_link_operations",
            "confluence_create_smart_link",
            "confluence_create_smart_link_property",
            "confluence_update_smart_link_property_by_id",
            "confluence_delete_smart_link",
            "confluence_delete_smart_link_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-task",
        tools=("confluence_get_tasks", "confluence_update_task"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-whiteboard",
        tools=("confluence_create_whiteboard", "confluence_delete_whiteboard"),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-whiteboard-content",
        tools=(
            "confluence_get_whiteboard_content_properties",
            "confluence_get_whiteboard_content_properties_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-whiteboard-property",
        tools=(
            "confluence_create_whiteboard_property",
            "confluence_update_whiteboard_property_by_id",
            "confluence_delete_whiteboard_property_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-platform-admin-key",
        tools=(
            "confluence_get_admin_key",
            "confluence_disable_admin_key",
            "confluence_enable_admin_key",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-platform",),
    ),
    SurfaceLink(
        "confluence-platform-forge-app",
        tools=(
            "confluence_get_forge_app_properties",
            "confluence_get_forge_app_property",
            "confluence_put_forge_app_property",
            "confluence_delete_forge_app_property",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-platform",),
    ),
    SurfaceLink(
        "confluence-spaces-available-space",
        tools=(
            "confluence_get_available_space_permissions",
            "confluence_get_available_space_roles",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-blog-post",
        tools=(
            "confluence_get_blog_post_classification_level",
            "confluence_get_blog_posts_in_space",
            "confluence_post_blog_post_classification_level",
            "confluence_put_blog_post_classification_level",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-database-classification",
        tools=(
            "confluence_get_database_classification_level",
            "confluence_post_database_classification_level",
            "confluence_put_database_classification_level",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-page-classification",
        tools=(
            "confluence_get_page_classification_level",
            "confluence_post_page_classification_level",
            "confluence_put_page_classification_level",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-space",
        tools=("confluence_get_spaces", "confluence_create_space"),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-space-default",
        tools=(
            "confluence_get_space_default_classification_level",
            "confluence_put_space_default_classification_level",
            "confluence_delete_space_default_classification_level",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-space-property",
        tools=(
            "confluence_get_space_properties",
            "confluence_get_space_property_by_id",
            "confluence_create_space_property",
            "confluence_update_space_property_by_id",
            "confluence_delete_space_property_by_id",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-space-role",
        tools=(
            "confluence_get_space_role_assignments",
            "confluence_get_space_role_mode",
            "confluence_get_space_roles_by_id",
            "confluence_create_space_role",
            "confluence_set_space_role_assignments",
            "confluence_update_space_role",
            "confluence_delete_space_role",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-whiteboard-classification",
        tools=(
            "confluence_get_whiteboard_classification_level",
            "confluence_post_whiteboard_classification_level",
            "confluence_put_whiteboard_classification_level",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "controls-api-key",
        tools=(
            "api_access_cloud_get_all_api_keys_by_org_id",
            "api_access_cloud_get_api_key_count_by_org_id",
            "api_access_cloud_revoke_api_key",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "controls-api-token",
        tools=(
            "api_access_cloud_get_all_api_tokens_by_org_id",
            "api_access_cloud_get_api_token_count_by_org_id",
            "api_access_cloud_revoke_api_tokens",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "controls-is-create",
        tools=(
            "control_cloud_ap_is_create_policy",
            "control_cloud_ap_is_create_policy_v2",
            "control_cloud_ap_is_create_resource",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "controls-is-delete",
        tools=(
            "control_cloud_ap_is_delete_policy",
            "control_cloud_ap_is_delete_resource",
            "control_cloud_ap_is_delete_resources",
            "control_cloud_ap_is_delete_resources_v2",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "controls-is-get",
        tools=(
            "control_cloud_ap_is_get_policies",
            "control_cloud_ap_is_get_policies_v2",
            "control_cloud_ap_is_get_policy",
            "control_cloud_ap_is_get_policy_v2",
            "control_cloud_ap_is_get_resources",
            "control_cloud_ap_is_get_resources_v2",
            "control_cloud_ap_is_get_task_status",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "controls-is-update",
        tools=(
            "control_cloud_ap_is_update_policy",
            "control_cloud_ap_is_update_policy_v2",
            "control_cloud_ap_is_update_resource",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "controls-level",
        tools=(
            "dlp_cloud_get_level",
            "dlp_cloud_create_level",
            "dlp_cloud_archive_level",
            "dlp_cloud_edit_level",
            "dlp_cloud_publish_level",
            "dlp_cloud_restore_level",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "controls-service-account",
        tools=(
            "api_access_cloud_count_service_account_api_tokens",
            "api_access_cloud_get_service_account_api_token",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "jira-boards-dashboards-dashboard",
        tools=(
            "jira_get_all_dashboards",
            "jira_get_dashboard",
            "jira_copy_dashboard",
            "jira_create_dashboard",
            "jira_update_dashboard",
            "jira_delete_dashboard",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-boards-dashboards-dashboard-item",
        tools=(
            "jira_get_dashboard_item_property",
            "jira_get_dashboard_item_property_keys",
            "jira_set_dashboard_item_property",
            "jira_delete_dashboard_item_property",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-boards-dashboards-favourite-filter",
        tools=(
            "jira_get_favourite_filters",
            "jira_set_favourite_for_filter",
            "jira_delete_favourite_for_filter",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-boards-dashboards-filter",
        tools=(
            "jira_get_filter",
            "jira_get_my_filters",
            "jira_create_filter",
            "jira_update_filter",
            "jira_delete_filter",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-boards-dashboards-gadget",
        tools=(
            "jira_get_all_gadgets",
            "jira_add_gadget",
            "jira_update_gadget",
            "jira_remove_gadget",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-boards-dashboards-plan",
        tools=(
            "jira_get_plan",
            "jira_get_plans",
            "jira_create_plan",
            "jira_duplicate_plan",
            "jira_trash_plan",
            "jira_archive_plan",
            "jira_update_plan",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-boards-dashboards-plan-only",
        tools=(
            "jira_get_plan_only_team",
            "jira_create_plan_only_team",
            "jira_update_plan_only_team",
            "jira_delete_plan_only_team",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-configuration-context-field",
        tools=("jira_get_contexts_for_field", "jira_get_contexts_for_field_deprecated"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-create-issue",
        tools=(
            "jira_get_create_issue_meta_issue_type_id",
            "jira_get_create_issue_meta_issue_types",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-custom-field",
        tools=(
            "jira_get_custom_field_configuration",
            "jira_get_custom_field_contexts_for_projects_and_issue_types",
            "jira_get_custom_field_option",
            "jira_get_custom_fields_configurations",
            "jira_create_custom_field",
            "jira_create_custom_field_context",
            "jira_create_custom_field_option",
            "jira_trash_custom_field",
            "jira_reorder_custom_field_options",
            "jira_replace_custom_field_option",
            "jira_restore_custom_field",
            "jira_update_custom_field",
            "jira_update_custom_field_configuration",
            "jira_update_custom_field_context",
            "jira_update_custom_field_option",
            "jira_update_custom_field_value",
            "jira_delete_custom_field",
            "jira_delete_custom_field_context",
            "jira_delete_custom_field_option",
            "jira_remove_custom_field_context_from_projects",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-default-project",
        tools=(
            "jira_get_default_project_classification",
            "jira_update_default_project_classification",
            "jira_remove_default_project_classification",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-default-share",
        tools=("jira_get_default_share_scope", "jira_set_default_share_scope"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-default-value",
        tools=("jira_get_default_values", "jira_set_default_values"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-default-workflow",
        tools=(
            "jira_get_default_workflow",
            "jira_update_default_workflow",
            "jira_delete_default_workflow",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-draft-default",
        tools=(
            "jira_get_draft_default_workflow",
            "jira_update_draft_default_workflow",
            "jira_delete_draft_default_workflow",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-draft-workflow",
        tools=(
            "jira_get_draft_workflow",
            "jira_publish_draft_workflow_scheme",
            "jira_update_draft_workflow_mapping",
            "jira_delete_draft_workflow_mapping",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-field-associated",
        tools=(
            "jira_update_fields_associated_with_schemes",
            "jira_remove_fields_associated_with_schemes",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-field-association",
        tools=(
            "jira_get_field_association_scheme_by_id",
            "jira_get_field_association_scheme_item_parameters",
            "jira_get_field_association_schemes",
            "jira_search_field_association_scheme_fields",
            "jira_search_field_association_scheme_projects",
            "jira_clone_field_association_scheme",
            "jira_create_field_association_scheme",
            "jira_update_field_association_scheme",
            "jira_update_field_association_scheme_item_parameters",
            "jira_delete_field_association_scheme",
            "jira_remove_field_association_scheme_item_parameters",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-field-configuration",
        tools=(
            "jira_get_all_field_configuration_schemes",
            "jira_get_all_field_configurations",
            "jira_get_field_configuration_items",
            "jira_get_field_configuration_scheme_mappings",
            "jira_get_field_configuration_scheme_project_mapping",
            "jira_create_field_configuration",
            "jira_create_field_configuration_scheme",
            "jira_assign_field_configuration_scheme_to_project",
            "jira_set_field_configuration_scheme_mapping",
            "jira_update_field_configuration",
            "jira_update_field_configuration_items",
            "jira_update_field_configuration_scheme",
            "jira_delete_field_configuration",
            "jira_delete_field_configuration_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-issue-field",
        tools=(
            "jira_get_all_issue_field_options",
            "jira_get_issue_field_option",
            "jira_app_issue_field_value_update_resource_update_issue_fields_put",
            "jira_create_issue_field_option",
            "jira_replace_issue_field_option",
            "jira_update_issue_field_option",
            "jira_delete_issue_field_option",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-issue-link",
        tools=(
            "jira_get_issue_link_type",
            "jira_get_issue_link_types",
            "jira_create_issue_link_type",
            "jira_update_issue_link_type",
            "jira_delete_issue_link_type",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-issue-navigator",
        tools=(
            "jira_get_issue_navigator_default_columns",
            "jira_set_issue_navigator_default_columns",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-issue-security",
        tools=(
            "jira_get_issue_security_level",
            "jira_get_issue_security_level_members",
            "jira_get_issue_security_scheme",
            "jira_get_issue_security_schemes",
            "jira_create_issue_security_scheme",
            "jira_update_issue_security_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-issue-type",
        tools=(
            "jira_get_all_issue_type_schemes",
            "jira_get_issue_type",
            "jira_get_issue_type_mappings_for_contexts",
            "jira_get_issue_type_property",
            "jira_get_issue_type_property_keys",
            "jira_get_issue_type_scheme_for_projects",
            "jira_get_issue_type_schemes_mapping",
            "jira_get_issue_type_screen_scheme_mappings",
            "jira_get_issue_type_screen_scheme_project_associations",
            "jira_get_issue_type_screen_schemes",
            "jira_get_issue_types_for_project",
            "jira_add_issue_types_to_context",
            "jira_add_issue_types_to_issue_type_scheme",
            "jira_create_issue_type",
            "jira_create_issue_type_avatar",
            "jira_create_issue_type_scheme",
            "jira_create_issue_type_screen_scheme",
            "jira_assign_issue_type_scheme_to_project",
            "jira_assign_issue_type_screen_scheme_to_project",
            "jira_reorder_issue_types_in_issue_type_scheme",
            "jira_set_issue_type_property",
            "jira_update_issue_type",
            "jira_update_issue_type_scheme",
            "jira_update_issue_type_screen_scheme",
            "jira_delete_issue_type",
            "jira_delete_issue_type_property",
            "jira_delete_issue_type_scheme",
            "jira_delete_issue_type_screen_scheme",
            "jira_remove_issue_type_from_issue_type_scheme",
            "jira_remove_issue_types_from_context",
            "jira_remove_issue_types_from_global_field_configuration_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-mapping-issue",
        tools=(
            "jira_append_mappings_for_issue_type_screen_scheme",
            "jira_remove_mappings_from_issue_type_screen_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-notification-scheme",
        tools=(
            "jira_get_notification_scheme",
            "jira_get_notification_scheme_for_project",
            "jira_get_notification_scheme_to_project_mappings",
            "jira_get_notification_schemes",
            "jira_create_notification_scheme",
            "jira_update_notification_scheme",
            "jira_delete_notification_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-permission-scheme",
        tools=(
            "jira_get_all_permission_schemes",
            "jira_get_permission_scheme",
            "jira_get_permission_scheme_grant",
            "jira_get_permission_scheme_grants",
            "jira_create_permission_scheme",
            "jira_assign_permission_scheme",
            "jira_update_permission_scheme",
            "jira_delete_permission_scheme",
            "jira_delete_permission_scheme_entity",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-priority",
        tools=(
            "jira_get_priorities",
            "jira_get_priority",
            "jira_search_priorities",
            "jira_create_priority",
            "jira_move_priorities",
            "jira_update_priority",
            "jira_delete_priority",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-priority-scheme",
        tools=(
            "jira_get_priority_schemes",
            "jira_create_priority_scheme",
            "jira_update_priority_scheme",
            "jira_delete_priority_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-project-custom",
        tools=(
            "jira_create_project_with_custom_template",
            "jira_assign_projects_to_custom_field_context",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-project-field",
        tools=(
            "jira_get_project_fields",
            "jira_get_projects_with_field_schemes",
            "jira_associate_projects_to_field_association_schemes",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-project-issue",
        tools=(
            "jira_get_project_issue_security_scheme",
            "jira_get_project_issue_type_usages_for_status",
            "jira_get_projects_for_issue_type_screen_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-project-usage",
        tools=(
            "jira_get_project_usages_for_status",
            "jira_get_project_usages_for_workflow",
            "jira_get_project_usages_for_workflow_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-resolution",
        tools=(
            "jira_get_resolution",
            "jira_get_resolutions",
            "jira_search_resolutions",
            "jira_create_resolution",
            "jira_move_resolutions",
            "jira_update_resolution",
            "jira_delete_resolution",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-scheme-project",
        tools=("jira_assign_scheme_to_project", "jira_associate_schemes_to_projects"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-screen",
        tools=(
            "jira_get_screens",
            "jira_create_screen",
            "jira_update_screen",
            "jira_delete_screen",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-screen-scheme",
        tools=(
            "jira_get_screen_schemes",
            "jira_create_screen_scheme",
            "jira_update_screen_scheme",
            "jira_delete_screen_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-screen-tab",
        tools=(
            "jira_get_all_screen_tab_fields",
            "jira_get_all_screen_tabs",
            "jira_add_screen_tab",
            "jira_add_screen_tab_field",
            "jira_rename_screen_tab",
            "jira_move_screen_tab",
            "jira_move_screen_tab_field",
            "jira_delete_screen_tab",
            "jira_remove_screen_tab_field",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-security-level",
        tools=(
            "jira_get_security_level_members",
            "jira_get_security_levels",
            "jira_get_security_levels_for_project",
            "jira_add_security_level",
            "jira_add_security_level_members",
            "jira_update_security_level",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-security-scheme",
        tools=("jira_search_security_schemes", "jira_delete_security_scheme"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-shared-time",
        tools=(
            "jira_get_shared_time_tracking_configuration",
            "jira_set_shared_time_tracking_configuration",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-status",
        tools=(
            "jira_get_all_statuses",
            "jira_get_status",
            "jira_get_statuses",
            "jira_create_statuses",
            "jira_update_statuses",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-status-category",
        tools=("jira_get_status_categories", "jira_get_status_category"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-status-id",
        tools=("jira_get_statuses_by_id", "jira_delete_statuses_by_id"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-template",
        tools=(
            "jira_live_template",
            "jira_save_template",
            "jira_edit_template",
            "jira_remove_template",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-ui-modification",
        tools=(
            "jira_get_ui_modifications",
            "jira_create_ui_modification",
            "jira_update_ui_modification",
            "jira_delete_ui_modification",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-user-default",
        tools=("jira_get_all_users_default", "jira_get_user_default_columns"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-workflow",
        tools=(
            "jira_get_all_workflows",
            "jira_get_workflow",
            "jira_read_workflows",
            "jira_search_workflows",
            "jira_create_workflow",
            "jira_create_workflows",
            "jira_update_workflows",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-workflow-history",
        tools=("jira_list_workflow_history", "jira_read_workflow_from_history"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-workflow-mapping",
        tools=("jira_update_workflow_mapping", "jira_delete_workflow_mapping"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-workflow-scheme",
        tools=(
            "jira_get_all_workflow_schemes",
            "jira_get_workflow_scheme",
            "jira_get_workflow_scheme_draft",
            "jira_get_workflow_scheme_draft_issue_type",
            "jira_get_workflow_scheme_issue_type",
            "jira_get_workflow_scheme_project_associations",
            "jira_get_workflow_scheme_usages_for_workflow",
            "jira_read_workflow_schemes",
            "jira_create_workflow_scheme",
            "jira_create_workflow_scheme_draft_from_parent",
            "jira_switch_workflow_scheme_for_project",
            "jira_set_workflow_scheme_draft_issue_type",
            "jira_set_workflow_scheme_issue_type",
            "jira_update_workflow_scheme",
            "jira_update_workflow_scheme_draft",
            "jira_delete_workflow_scheme",
            "jira_delete_workflow_scheme_draft",
            "jira_delete_workflow_scheme_draft_issue_type",
            "jira_delete_workflow_scheme_issue_type",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-workflow-transition",
        tools=(
            "jira_get_workflow_transition_properties",
            "jira_get_workflow_transition_rule_configurations",
            "jira_create_workflow_transition_property",
            "jira_update_workflow_transition_property",
            "jira_update_workflow_transition_rule_configurations",
            "jira_delete_workflow_transition_property",
            "jira_delete_workflow_transition_rule_configurations",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-issues-application-property",
        tools=("jira_get_application_property", "jira_set_application_property"),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-attachment",
        tools=("jira_get_attachment", "jira_add_attachment", "jira_remove_attachment"),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-comment",
        tools=(
            "jira_get_comment",
            "jira_get_comments",
            "jira_add_comment",
            "jira_update_comment",
            "jira_delete_comment",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-comment-property",
        tools=(
            "jira_get_comment_property",
            "jira_get_comment_property_keys",
            "jira_set_comment_property",
            "jira_delete_comment_property",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-forge-app",
        tools=(
            "jira_get_forge_app_property",
            "jira_get_forge_app_property_keys",
            "jira_put_forge_app_property",
            "jira_delete_forge_app_property",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-ids-worklog",
        tools=(
            "jira_get_ids_of_worklogs_deleted_since",
            "jira_get_ids_of_worklogs_modified_since",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-issue",
        tools=(
            "jira_count_issues",
            "jira_get_issue",
            "jira_create_issue",
            "jira_create_issues",
            "jira_link_issues",
            "jira_match_issues",
            "jira_archive_issues",
            "jira_assign_issue",
            "jira_edit_issue",
            "jira_delete_issue",
            "jira_unarchive_issues",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-issue-link",
        tools=("jira_get_issue_link", "jira_delete_issue_link"),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-issue-property",
        tools=(
            "jira_get_issue_property",
            "jira_get_issue_property_keys",
            "jira_set_issue_property",
            "jira_delete_issue_property",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-issue-using",
        tools=(
            "jira_search_for_issues_using_jql",
            "jira_search_for_issues_using_jql_post",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-jql-query",
        tools=("jira_parse_jql_queries", "jira_sanitise_jql_queries"),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-property-resource",
        tools=(
            "jira_addon_properties_resource_delete_addon_property_delete",
            "jira_addon_properties_resource_get_addon_property_get",
            "jira_addon_properties_resource_put_addon_property_put",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-reconsile-issue",
        tools=(
            "jira_search_and_reconsile_issues_using_jql",
            "jira_search_and_reconsile_issues_using_jql_post",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-remote-issue",
        tools=(
            "jira_get_remote_issue_link_by_id",
            "jira_get_remote_issue_links",
            "jira_update_remote_issue_link",
            "jira_delete_remote_issue_link_by_global_id",
            "jira_delete_remote_issue_link_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-set-issue",
        tools=(
            "jira_bulk_set_issue_properties_by_issue",
            "jira_bulk_set_issue_property",
            "jira_bulk_set_issues_properties_list",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-transition",
        tools=("jira_get_transitions", "jira_do_transition"),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-vote",
        tools=("jira_get_votes", "jira_add_vote", "jira_remove_vote"),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-watcher",
        tools=("jira_add_watcher", "jira_remove_watcher"),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-worklog",
        tools=(
            "jira_get_worklog",
            "jira_add_worklog",
            "jira_update_worklog",
            "jira_delete_worklog",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-worklog-property",
        tools=(
            "jira_get_worklog_property",
            "jira_get_worklog_property_keys",
            "jira_set_worklog_property",
            "jira_delete_worklog_property",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-people-access-actor",
        tools=("jira_set_actors", "jira_delete_actor"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-application-role",
        tools=("jira_get_all_application_roles", "jira_get_application_role"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-avatar",
        tools=("jira_get_avatars", "jira_store_avatar", "jira_delete_avatar"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-avatar-image",
        tools=(
            "jira_get_avatar_image_by_id",
            "jira_get_avatar_image_by_owner",
            "jira_get_avatar_image_by_type",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-get-user",
        tools=("jira_bulk_get_users", "jira_bulk_get_users_migration"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-group",
        tools=(
            "jira_find_groups",
            "jira_get_group",
            "jira_create_group",
            "jira_remove_group",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-permission",
        tools=("jira_get_all_permissions", "jira_get_my_permissions"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-share-permission",
        tools=(
            "jira_get_share_permission",
            "jira_get_share_permissions",
            "jira_add_share_permission",
            "jira_delete_share_permission",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-user",
        tools=(
            "jira_find_users",
            "jira_get_all_users",
            "jira_get_user",
            "jira_create_user",
            "jira_remove_user",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-user-column",
        tools=("jira_reset_user_columns", "jira_set_user_columns"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-user-email",
        tools=("jira_get_user_email", "jira_get_user_email_bulk"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-user-group",
        tools=(
            "jira_find_users_and_groups",
            "jira_get_user_groups",
            "jira_get_users_from_group",
            "jira_add_user_to_group",
            "jira_remove_user_from_group",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-user-property",
        tools=(
            "jira_get_user_property",
            "jira_get_user_property_keys",
            "jira_set_user_property",
            "jira_delete_user_property",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-platform-association",
        tools=("jira_create_associations", "jira_remove_associations"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-atlassian-team",
        tools=(
            "jira_get_atlassian_team",
            "jira_add_atlassian_team",
            "jira_update_atlassian_team",
            "jira_remove_atlassian_team",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-auto-complete",
        tools=("jira_get_auto_complete", "jira_get_auto_complete_post"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-banner",
        tools=("jira_get_banner", "jira_set_banner"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-change-log",
        tools=("jira_get_change_logs", "jira_get_change_logs_by_ids"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-column",
        tools=("jira_get_columns", "jira_reset_columns", "jira_set_columns"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-dynamic-webhook",
        tools=("jira_get_dynamic_webhooks_for_app", "jira_register_dynamic_webhooks"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-forge-migration",
        tools=(
            "jira_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get",
            "jira_connect_to_forge_migration_task_submission_resource_submit_task_post",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-locale",
        tools=("jira_get_locale", "jira_set_locale"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-module-resource",
        tools=(
            "jira_dynamic_modules_resource_get_modules_get",
            "jira_dynamic_modules_resource_register_modules_post",
            "jira_dynamic_modules_resource_remove_modules_delete",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-policy",
        tools=("jira_get_policies", "jira_get_policy"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-precomputation",
        tools=("jira_get_precomputations", "jira_update_precomputations"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-preference",
        tools=("jira_get_preference", "jira_set_preference", "jira_remove_preference"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-related-work",
        tools=(
            "jira_get_related_work",
            "jira_create_related_work",
            "jira_update_related_work",
            "jira_delete_related_work",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-task",
        tools=("jira_get_task", "jira_cancel_task"),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-projects-accessible-project",
        tools=(
            "jira_get_accessible_project_type_by_key",
            "jira_get_all_accessible_project_types",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-component",
        tools=(
            "jira_get_component",
            "jira_create_component",
            "jira_update_component",
            "jira_delete_component",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-feature-project",
        tools=("jira_get_features_for_project", "jira_toggle_feature_for_project"),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project",
        tools=(
            "jira_get_all_projects",
            "jira_get_project",
            "jira_search_projects",
            "jira_create_project",
            "jira_archive_project",
            "jira_update_project",
            "jira_delete_project",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project-avatar",
        tools=(
            "jira_get_all_project_avatars",
            "jira_create_project_avatar",
            "jira_update_project_avatar",
            "jira_delete_project_avatar",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project-category",
        tools=(
            "jira_get_all_project_categories",
            "jira_get_project_category_by_id",
            "jira_create_project_category",
            "jira_update_project_category",
            "jira_remove_project_category",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project-component",
        tools=("jira_get_project_components", "jira_get_project_components_paginated"),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project-email",
        tools=("jira_get_project_email", "jira_update_project_email"),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project-property",
        tools=(
            "jira_get_project_property",
            "jira_get_project_property_keys",
            "jira_set_project_property",
            "jira_delete_project_property",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project-role",
        tools=(
            "jira_get_all_project_roles",
            "jira_get_project_role",
            "jira_get_project_role_actors_for_role",
            "jira_get_project_role_by_id",
            "jira_get_project_role_details",
            "jira_get_project_roles",
            "jira_add_project_role_actors_to_role",
            "jira_create_project_role",
            "jira_delete_project_role",
            "jira_delete_project_role_actors_from_role",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project-type",
        tools=("jira_get_all_project_types", "jira_get_project_type_by_key"),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-project-version",
        tools=("jira_get_project_versions", "jira_get_project_versions_paginated"),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-update-project",
        tools=("jira_fully_update_project_role", "jira_partial_update_project_role"),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-valid-project",
        tools=("jira_get_valid_project_key", "jira_get_valid_project_name"),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-version",
        tools=(
            "jira_get_version",
            "jira_create_version",
            "jira_merge_versions",
            "jira_move_version",
            "jira_update_version",
            "jira_delete_version",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "lifecycle-scim-link",
        tools=(
            "user_provisioning_cloud_get_scim_links",
            "user_provisioning_cloud_get_scim_links_by_email",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-user-lifecycle",),
    ),
    SurfaceLink(
        "lifecycle-user-account",
        tools=(
            "user_mgmt_cloud_get_users_account_id_manage",
            "user_mgmt_cloud_get_users_account_id_manage_api_tokens",
            "user_mgmt_cloud_get_users_account_id_manage_profile",
            "user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete",
            "user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete",
            "user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable",
            "user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable",
            "user_mgmt_cloud_patch_users_account_id_manage_profile",
            "user_mgmt_cloud_put_users_account_id_manage_email",
            "user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-user-lifecycle",),
    ),
    SurfaceLink(
        "lifecycle-user-an",
        tools=(
            "user_provisioning_cloud_get_users_from_an_active_directory",
            "user_provisioning_cloud_create_a_user_in_an_active_directory",
            "user_provisioning_cloud_delete_a_user_from_an_active_directory",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-user-lifecycle",),
    ),
    SurfaceLink(
        "lifecycle-user-information",
        tools=(
            "user_provisioning_cloud_patch_user_information_in_an_active_directory",
            "user_provisioning_cloud_update_user_information_in_an_active_directory",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-user-lifecycle",),
    ),
    SurfaceLink(
        "org-directory-org",
        tools=(
            "admin_cloud_get_directories_for_org",
            "org_cloud_get_directories_for_org",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-directory-user",
        tools=(
            "admin_cloud_get_directory_user_details",
            "admin_cloud_get_directory_users",
            "admin_cloud_get_directory_users_count",
            "org_cloud_get_directory_user_details",
            "org_cloud_get_directory_users",
            "org_cloud_get_directory_users_count",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-domain",
        tools=("admin_cloud_get_domains", "org_cloud_get_domains"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-domain-id",
        tools=("admin_cloud_get_domain_by_id", "org_cloud_get_domain_by_id"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-event",
        tools=(
            "admin_cloud_get_events",
            "org_cloud_get_events",
            "admin_cloud_poll_events",
            "org_cloud_poll_events",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-event-action",
        tools=("admin_cloud_get_event_actions", "org_cloud_get_event_actions"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-event-id",
        tools=("admin_cloud_get_event_by_id", "org_cloud_get_event_by_id"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-group",
        tools=(
            "admin_cloud_get_group",
            "admin_cloud_get_groups",
            "admin_cloud_search_groups",
            "org_cloud_get_group",
            "org_cloud_get_groups",
            "org_cloud_search_groups",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-group-count",
        tools=("admin_cloud_get_groups_count", "org_cloud_get_groups_count"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-group-role",
        tools=(
            "admin_cloud_get_group_role_assignments",
            "org_cloud_get_group_role_assignments",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-group-stat",
        tools=("admin_cloud_get_groups_stats", "org_cloud_get_groups_stats"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org",
        tools=("admin_cloud_get_orgs", "org_cloud_get_orgs"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-id",
        tools=("admin_cloud_get_org_by_id", "org_cloud_get_org_by_id"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-policy",
        tools=(
            "admin_cloud_get_policies",
            "admin_cloud_validate_policy",
            "org_cloud_get_policies",
            "org_cloud_validate_policy",
            "admin_cloud_create_policy",
            "org_cloud_create_policy",
            "admin_cloud_update_policy",
            "org_cloud_update_policy",
            "admin_cloud_delete_policy",
            "org_cloud_delete_policy",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-policy-id",
        tools=("admin_cloud_get_policy_by_id", "org_cloud_get_policy_by_id"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-policy-resource",
        tools=(
            "admin_cloud_update_policy_resource",
            "org_cloud_update_policy_resource",
            "admin_cloud_delete_policy_resource",
            "org_cloud_delete_policy_resource",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-resource-policy",
        tools=(
            "admin_cloud_add_resource_to_policy",
            "org_cloud_add_resource_to_policy",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-role",
        tools=(
            "admin_cloud_assign_role",
            "org_cloud_assign_role",
            "admin_cloud_revoke_role",
            "org_cloud_revoke_role",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-role-group",
        tools=(
            "admin_cloud_assign_role_to_group",
            "org_cloud_assign_role_to_group",
            "admin_cloud_revoke_role_to_group",
            "org_cloud_revoke_role_to_group",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-user",
        tools=(
            "admin_cloud_get_users",
            "admin_cloud_search_users",
            "org_cloud_get_users",
            "org_cloud_search_users",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-user-role",
        tools=(
            "admin_cloud_get_user_role_assignments",
            "org_cloud_get_user_role_assignments",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-user-stat",
        tools=("admin_cloud_get_user_stats", "org_cloud_get_user_stats"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-v1-org",
        tools=(
            "admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates",
            "org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates",
            "admin_cloud_post_v1_orgs_org_id_directory_groups",
            "admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships",
            "admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access",
            "admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access",
            "admin_cloud_post_v1_orgs_org_id_users_invite",
            "admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign",
            "admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke",
            "org_cloud_post_v1_orgs_org_id_directory_groups",
            "org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships",
            "org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access",
            "org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access",
            "org_cloud_post_v1_orgs_org_id_users_invite",
            "org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign",
            "org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke",
            "admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id",
            "admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id",
            "admin_cloud_delete_v1_orgs_org_id_directory_users_account_id",
            "org_cloud_delete_v1_orgs_org_id_directory_groups_group_id",
            "org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id",
            "org_cloud_delete_v1_orgs_org_id_directory_users_account_id",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-v2-org",
        tools=(
            "admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups",
            "admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships",
            "admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign",
            "admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke",
            "admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore",
            "admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend",
            "admin_cloud_post_v2_orgs_org_id_users_invite",
            "org_cloud_post_v2_orgs_org_id_directories_directory_id_groups",
            "org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships",
            "org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign",
            "org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke",
            "org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore",
            "org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend",
            "org_cloud_post_v2_orgs_org_id_users_invite",
            "admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id",
            "admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id",
            "admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id",
            "org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id",
            "org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id",
            "org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "org-workspace-v2",
        tools=("admin_cloud_query_workspaces_v2", "org_cloud_query_workspaces_v2"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-org-administration",),
    ),
    SurfaceLink(
        "confluence-content-read-records-1",
        tools=(
            "confluence_get_attachment_by_id",
            "confluence_get_attachment_comments",
            "confluence_get_attachment_labels",
            "confluence_get_attachment_operations",
            "confluence_get_blogpost_attachments",
            "confluence_get_child_custom_content",
            "confluence_get_child_pages",
            "confluence_get_database_ancestors",
            "confluence_get_database_by_id",
            "confluence_get_database_descendants",
            "confluence_get_database_direct_children",
            "confluence_get_database_operations",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-read-records-2",
        tools=(
            "confluence_get_folder_ancestors",
            "confluence_get_folder_by_id",
            "confluence_get_folder_descendants",
            "confluence_get_folder_direct_children",
            "confluence_get_folder_operations",
            "confluence_get_label_attachments",
            "confluence_get_label_blog_posts",
            "confluence_get_label_pages",
            "confluence_get_labels",
            "confluence_get_page_ancestors",
            "confluence_get_page_attachments",
            "confluence_get_page_by_id",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-read-records-3",
        tools=(
            "confluence_get_page_descendants",
            "confluence_get_page_direct_children",
            "confluence_get_page_footer_comments",
            "confluence_get_page_inline_comments",
            "confluence_get_page_labels",
            "confluence_get_page_operations",
            "confluence_get_task_by_id",
            "confluence_get_whiteboard_ancestors",
            "confluence_get_whiteboard_by_id",
            "confluence_get_whiteboard_descendants",
            "confluence_get_whiteboard_direct_children",
            "confluence_get_whiteboard_operations",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-content-change-records",
        tools=(
            "confluence_convert_content_ids_to_content_types",
            "confluence_post_redact_blog",
            "confluence_post_redact_page",
            "confluence_update_page_title",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-knowledge-manager",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-confluence-content",
            "atlassian-search-company-knowledge",
            "atlassian-generate-status-report",
        ),
    ),
    SurfaceLink(
        "confluence-platform-read-records",
        tools=("confluence_get_data_policy_metadata",),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-platform",),
    ),
    SurfaceLink(
        "confluence-platform-change-records",
        tools=(
            "confluence_check_access_by_email",
            "confluence_create_bulk_user_lookup",
            "confluence_invite_by_email",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-platform",),
    ),
    SurfaceLink(
        "confluence-spaces-read-records",
        tools=(
            "confluence_get_calendars",
            "confluence_get_classification_levels",
            "confluence_get_custom_content_by_type_in_space",
            "confluence_get_data_policy_spaces",
            "confluence_get_pages_in_space",
            "confluence_get_space_by_id",
            "confluence_get_space_content_labels",
            "confluence_get_space_labels",
            "confluence_get_space_operations",
            "confluence_get_space_permissions_assignments",
        ),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "confluence-spaces-change-records",
        tools=("confluence_add_calendar_event",),
        prompts=("atlassian-operator", "atlassian-knowledge-manager"),
        skills=("atlassian-confluence-spaces",),
    ),
    SurfaceLink(
        "controls-read-records",
        tools=("control_cloud_ap_is_validate_policy", "dlp_cloud_get_level_list"),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "controls-change-records",
        tools=(
            "control_cloud_ap_is_add_users_to_policy",
            "control_cloud_ap_is_attach_detach_resources_v2",
            "control_cloud_ap_is_bulk_fetch_auth_policy",
            "control_cloud_ap_is_publish_draft_policies",
            "api_access_cloud_bulk_revoke_api_tokens",
            "dlp_cloud_reorder",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-security-controls",),
    ),
    SurfaceLink(
        "jira-boards-dashboards-read-records",
        tools=(
            "jira_get_all_available_dashboard_gadgets",
            "jira_get_dashboards_paginated",
            "jira_get_filters_paginated",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-boards-dashboards-change-records",
        tools=("jira_bulk_edit_dashboards", "jira_change_filter_owner"),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-boards-dashboards", "atlassian-jira-filters"),
    ),
    SurfaceLink(
        "jira-configuration-read-records-1",
        tools=(
            "jira_get_alternative_issue_types",
            "jira_get_assigned_permission_scheme",
            "jira_get_available_priorities_by_priority_scheme",
            "jira_get_available_screen_fields",
            "jira_get_available_time_tracking_implementations",
            "jira_get_bulk_editable_fields",
            "jira_get_bulk_screen_tabs",
            "jira_get_configuration",
            "jira_get_default_editor",
            "jira_get_field_auto_complete_for_query_string",
            "jira_get_field_project_associations",
            "jira_get_fields",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-read-records-2",
        tools=(
            "jira_get_fields_paginated",
            "jira_get_options_for_context",
            "jira_get_priorities_by_priority_scheme",
            "jira_get_project_context_mapping",
            "jira_get_projects_by_priority_scheme",
            "jira_get_redaction_status",
            "jira_get_screens_for_field",
            "jira_get_selectable_issue_field_options",
            "jira_get_selected_time_tracking_implementation",
            "jira_get_statuses_by_name",
            "jira_get_trashed_fields_paginated",
            "jira_get_visible_issue_field_options",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-read-records-3",
        tools=(
            "jira_get_workflow_project_issue_type_usages",
            "jira_get_workflow_usages_for_status",
            "jira_get_workflows_paginated",
            "jira_search_projects_using_security_schemes",
            "jira_workflow_capabilities",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-change-records-1",
        tools=(
            "jira_get_required_workflow_scheme_mappings",
            "jira_read_workflow_previews",
            "jira_validate_create_workflows",
            "jira_validate_update_workflows",
            "jira_add_field_to_default_screen",
            "jira_add_notifications",
            "jira_migration_resource_workflow_rule_search_post",
            "jira_select_time_tracking_implementation",
            "jira_suggested_priorities_for_mappings",
            "jira_set_default_levels",
            "jira_set_default_priority",
            "jira_set_default_resolution",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-configuration-change-records-2",
        tools=(
            "jira_update_default_screen_scheme",
            "jira_update_multiple_custom_field_values",
            "jira_update_schemes",
            "jira_delete_inactive_workflow",
            "jira_remove_member_from_security_level",
            "jira_remove_notification_from_notification_scheme",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-configuration",),
    ),
    SurfaceLink(
        "jira-issues-read-records-1",
        tools=(
            "jira_expand_attachment_for_humans",
            "jira_expand_attachment_for_machines",
            "jira_get_all_labels",
            "jira_get_approximate_application_license_count",
            "jira_get_approximate_license_count",
            "jira_get_attachment_content",
            "jira_get_attachment_meta",
            "jira_get_attachment_thumbnail",
            "jira_get_available_transitions",
            "jira_get_bulk_operation_progress",
            "jira_get_create_issue_meta",
            "jira_get_edit_issue_meta",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-read-records-2",
        tools=(
            "jira_get_issue_all_types",
            "jira_get_issue_limit_report",
            "jira_get_issue_picker_resource",
            "jira_get_issue_watchers",
            "jira_get_issue_worklog",
            "jira_search",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-change-records-1",
        tools=(
            "jira_get_bulk_changelogs",
            "jira_get_comments_by_ids",
            "jira_get_is_watching_issue_bulk",
            "jira_get_worklogs_by_issue_id_and_worklog_id",
            "jira_get_worklogs_for_ids",
            "jira_create_or_update_remote_issue_link",
            "jira_export_archived_issues",
            "jira_submit_bulk_delete",
            "jira_submit_bulk_edit",
            "jira_submit_bulk_move",
            "jira_submit_bulk_transition",
            "jira_submit_bulk_unwatch",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-issues-change-records-2",
        tools=(
            "jira_submit_bulk_watch",
            "jira_archive_issues_async",
            "jira_bulk_delete_issue_property",
            "jira_bulk_delete_worklogs",
            "jira_bulk_fetch_issues",
            "jira_bulk_move_worklogs",
        ),
        prompts=(
            "atlassian-operator",
            "atlassian-delivery-lead",
            "atlassian-data-steward",
        ),
        skills=(
            "atlassian-jira-issues",
            "atlassian-agent-operations",
            "atlassian-triage-issue",
            "atlassian-create-issue-guided",
            "atlassian-my-priority-queue",
            "atlassian-capture-tasks-from-meeting-notes",
            "atlassian-spec-to-backlog",
        ),
    ),
    SurfaceLink(
        "jira-people-access-read-records",
        tools=(
            "jira_bulk_get_groups",
            "jira_find_assignable_users",
            "jira_find_bulk_assignable_users",
            "jira_find_user_keys_by_query",
            "jira_find_users_by_query",
            "jira_find_users_for_picker",
            "jira_find_users_with_all_permissions",
            "jira_find_users_with_browse_permission",
            "jira_get_all_system_avatars",
            "jira_get_all_user_data_classification_levels",
            "jira_get_current_user",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-people-access-change-records",
        tools=(
            "jira_get_bulk_permissions",
            "jira_add_actor_users",
            "jira_create_permission_grant",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-people-access",),
    ),
    SurfaceLink(
        "jira-platform-read-records",
        tools=(
            "jira_addon_properties_resource_get_addon_properties_get",
            "jira_get_advanced_settings",
            "jira_get_audit_records",
            "jira_get_events",
            "jira_get_failed_webhooks",
            "jira_get_hierarchy",
            "jira_get_license",
            "jira_get_recent",
            "jira_get_server_info",
            "jira_get_teams",
            "jira_service_registry_resource_services_get",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-platform-change-records",
        tools=(
            "jira_analyse_expression",
            "jira_evaluate_jira_expression",
            "jira_evaluate_jsis_jira_expression",
            "jira_get_precomputations_by_id",
            "jira_migrate_queries",
            "jira_migration_resource_update_entity_properties_value_put",
            "jira_notify",
            "jira_redact",
            "jira_refresh_webhooks",
            "jira_restore",
            "jira_delete_webhook_by_id",
            "jira_remove_level",
        ),
        prompts=("atlassian-operator", "atlassian-jira-administrator"),
        skills=("atlassian-jira-platform",),
    ),
    SurfaceLink(
        "jira-projects-read-records",
        tools=(
            "jira_find_components_for_projects",
            "jira_get_component_related_issues",
            "jira_get_project_classification_config",
            "jira_get_version_related_issues",
            "jira_get_version_unresolved_issues",
            "jira_validate_project_key",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "jira-projects-change-records",
        tools=(
            "jira_get_permitted_projects",
            "jira_bulk_pin_unpin_projects_async",
            "jira_delete_and_replace_version",
            "jira_delete_project_asynchronously",
        ),
        prompts=("atlassian-operator", "atlassian-delivery-lead"),
        skills=("atlassian-jira-projects", "atlassian-generate-status-report"),
    ),
    SurfaceLink(
        "kg-change-records",
        tools=("atlassian_ingest_confluence", "atlassian_ingest_issues"),
        prompts=("atlassian-operator", "atlassian-data-steward"),
        skills=("atlassian-kg-ingestion",),
    ),
    SurfaceLink(
        "lifecycle-read-records",
        tools=(
            "user_provisioning_cloud_get",
            "user_provisioning_cloud_get_a_user_from_active_directory",
            "user_provisioning_cloud_get_all_groups_from_an_active_directory",
            "user_provisioning_cloud_get_config",
            "user_provisioning_cloud_get_extension_user_schemas",
            "user_provisioning_cloud_get_group_resource_type",
            "user_provisioning_cloud_get_group_schemas",
            "user_provisioning_cloud_get_resource_types",
            "user_provisioning_cloud_get_schemas",
            "user_provisioning_cloud_get_user_resource_type",
            "user_provisioning_cloud_get_user_schemas",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-user-lifecycle",),
    ),
    SurfaceLink(
        "lifecycle-change-records",
        tools=(
            "user_provisioning_cloud_create_a_group_in_active_directory",
            "user_provisioning_cloud_unlink_scim_user",
            "user_provisioning_cloud_patch",
            "user_provisioning_cloud_put",
            "user_provisioning_cloud_delete_a_group",
            "user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db",
        ),
        prompts=("atlassian-operator", "atlassian-organization-administrator"),
        skills=("atlassian-user-lifecycle",),
    ),
)

LOCATIONS = (
    DataLocation(
        "atlassian-jira-issues",
        ("Issue", "Comment", "Worklog", "Attachment"),
        "ATLASSIAN_AGENT_URL",
        "jira_search_for_issues_using_jql",
        federation_key="key",
    ),
    DataLocation(
        "atlassian-jira-projects",
        ("Project", "Component", "Version"),
        "ATLASSIAN_AGENT_URL",
        "jira_get_all_projects",
        federation_key="key",
    ),
    DataLocation(
        "atlassian-jira-configuration",
        ("Workflow", "CustomField", "Screen", "IssueType"),
        "ATLASSIAN_AGENT_URL",
        "jira_get_all_statuses",
        federation_key="id",
    ),
    DataLocation(
        "atlassian-jira-people",
        ("Person", "Group", "ProjectRole"),
        "ATLASSIAN_AGENT_URL",
        "jira_get_all_users",
        federation_key="account_id",
    ),
    DataLocation(
        "atlassian-jira-filters",
        ("Filter", "Dashboard", "Plan"),
        "ATLASSIAN_AGENT_URL",
        "jira_get_filters_paginated",
        federation_key="id",
    ),
    DataLocation(
        "atlassian-jira-platform",
        ("App", "Webhook", "Task"),
        "ATLASSIAN_AGENT_URL",
        "jira_get_server_info",
        federation_key="id",
    ),
    DataLocation(
        "atlassian-confluence-pages",
        ("Page", "BlogPost", "Comment", "Attachment"),
        "ATLASSIAN_AGENT_URL",
        "confluence_get_pages",
        federation_key="id",
    ),
    DataLocation(
        "atlassian-confluence-spaces",
        ("Space", "SpacePermission"),
        "ATLASSIAN_AGENT_URL",
        "confluence_get_spaces",
        federation_key="id",
    ),
    DataLocation(
        "atlassian-confluence-platform",
        ("App", "DataPolicy"),
        "ATLASSIAN_AGENT_URL",
        "confluence_get_data_policy_metadata",
        federation_key="id",
    ),
    DataLocation(
        "atlassian-organization",
        ("Organization", "Directory", "Domain", "Policy"),
        "ATLASSIAN_AGENT_URL",
        "admin_cloud_get_orgs",
        route_param="org_id",
        federation_key="id",
    ),
    DataLocation(
        "atlassian-accounts",
        ("Person", "ScimUser", "ScimGroup"),
        "ATLASSIAN_AGENT_URL",
        "user_mgmt_cloud_get_users_account_id_manage",
        federation_key="account_id",
    ),
    DataLocation(
        "atlassian-controls",
        ("ApiKey", "ClassificationLevel"),
        "ATLASSIAN_AGENT_URL",
        "api_access_cloud_get_all_api_keys_by_org_id",
        route_param="org_id",
        federation_key="id",
    ),
    DataLocation(
        "atlassian-ingest-state",
        ("Issue", "ConfluencePage"),
        "ATLASSIAN_AGENT_URL",
        "atlassian_ingest_issues",
        federation_key="id",
    ),
)

ROLES = (
    BusinessRole(
        "delivery lead",
        tasks=(
            "jira-issues-application-property",
            "jira-issues-attachment",
            "jira-issues-comment",
            "jira-issues-comment-property",
            "jira-issues-forge-app",
            "jira-issues-ids-worklog",
            "jira-issues-issue",
            "jira-issues-issue-link",
            "jira-issues-issue-property",
            "jira-issues-issue-using",
            "jira-issues-jql-query",
            "jira-issues-property-resource",
            "jira-issues-reconsile-issue",
            "jira-issues-remote-issue",
            "jira-issues-set-issue",
            "jira-issues-transition",
            "jira-issues-vote",
            "jira-issues-watcher",
            "jira-issues-worklog",
            "jira-issues-worklog-property",
            "jira-issues-read-records-1",
            "jira-issues-read-records-2",
            "jira-issues-change-records-1",
            "jira-issues-change-records-2",
            "jira-boards-dashboards-dashboard",
            "jira-boards-dashboards-dashboard-item",
            "jira-boards-dashboards-favourite-filter",
            "jira-boards-dashboards-filter",
            "jira-boards-dashboards-gadget",
            "jira-boards-dashboards-plan",
            "jira-boards-dashboards-plan-only",
            "jira-boards-dashboards-read-records",
            "jira-boards-dashboards-change-records",
            "jira-projects-accessible-project",
            "jira-projects-component",
            "jira-projects-feature-project",
            "jira-projects-project",
            "jira-projects-project-avatar",
            "jira-projects-project-category",
            "jira-projects-project-component",
            "jira-projects-project-email",
            "jira-projects-project-property",
            "jira-projects-project-role",
            "jira-projects-project-type",
            "jira-projects-project-version",
            "jira-projects-update-project",
            "jira-projects-valid-project",
            "jira-projects-version",
            "jira-projects-read-records",
            "jira-projects-change-records",
        ),
        description="Keep Jira work flowing: triage, assign, transition, report and keep filters and dashboards current.",
    ),
    BusinessRole(
        "jira administrator",
        tasks=(
            "jira-configuration-context-field",
            "jira-configuration-create-issue",
            "jira-configuration-custom-field",
            "jira-configuration-default-project",
            "jira-configuration-default-share",
            "jira-configuration-default-value",
            "jira-configuration-default-workflow",
            "jira-configuration-draft-default",
            "jira-configuration-draft-workflow",
            "jira-configuration-field-associated",
            "jira-configuration-field-association",
            "jira-configuration-field-configuration",
            "jira-configuration-issue-field",
            "jira-configuration-issue-link",
            "jira-configuration-issue-navigator",
            "jira-configuration-issue-security",
            "jira-configuration-issue-type",
            "jira-configuration-mapping-issue",
            "jira-configuration-notification-scheme",
            "jira-configuration-permission-scheme",
            "jira-configuration-priority",
            "jira-configuration-priority-scheme",
            "jira-configuration-project-custom",
            "jira-configuration-project-field",
            "jira-configuration-project-issue",
            "jira-configuration-project-usage",
            "jira-configuration-resolution",
            "jira-configuration-scheme-project",
            "jira-configuration-screen",
            "jira-configuration-screen-scheme",
            "jira-configuration-screen-tab",
            "jira-configuration-security-level",
            "jira-configuration-security-scheme",
            "jira-configuration-shared-time",
            "jira-configuration-status",
            "jira-configuration-status-category",
            "jira-configuration-status-id",
            "jira-configuration-template",
            "jira-configuration-ui-modification",
            "jira-configuration-user-default",
            "jira-configuration-workflow",
            "jira-configuration-workflow-history",
            "jira-configuration-workflow-mapping",
            "jira-configuration-workflow-scheme",
            "jira-configuration-workflow-transition",
            "jira-configuration-read-records-1",
            "jira-configuration-read-records-2",
            "jira-configuration-read-records-3",
            "jira-configuration-change-records-1",
            "jira-configuration-change-records-2",
            "jira-people-access-actor",
            "jira-people-access-application-role",
            "jira-people-access-avatar",
            "jira-people-access-avatar-image",
            "jira-people-access-get-user",
            "jira-people-access-group",
            "jira-people-access-permission",
            "jira-people-access-share-permission",
            "jira-people-access-user",
            "jira-people-access-user-column",
            "jira-people-access-user-email",
            "jira-people-access-user-group",
            "jira-people-access-user-property",
            "jira-people-access-read-records",
            "jira-people-access-change-records",
            "jira-platform-association",
            "jira-platform-atlassian-team",
            "jira-platform-auto-complete",
            "jira-platform-banner",
            "jira-platform-change-log",
            "jira-platform-column",
            "jira-platform-dynamic-webhook",
            "jira-platform-forge-migration",
            "jira-platform-locale",
            "jira-platform-module-resource",
            "jira-platform-policy",
            "jira-platform-precomputation",
            "jira-platform-preference",
            "jira-platform-related-work",
            "jira-platform-task",
            "jira-platform-read-records",
            "jira-platform-change-records",
        ),
        description="Administer Jira configuration, access and site services safely.",
    ),
    BusinessRole(
        "knowledge manager",
        tasks=(
            "confluence-content-attachment",
            "confluence-content-attachment-content",
            "confluence-content-attachment-property",
            "confluence-content-attachment-version",
            "confluence-content-blog-post",
            "confluence-content-blogpost-content",
            "confluence-content-blogpost-property",
            "confluence-content-comment-content",
            "confluence-content-comment-property",
            "confluence-content-custom-content",
            "confluence-content-database",
            "confluence-content-database-content",
            "confluence-content-database-property",
            "confluence-content-folder",
            "confluence-content-folder-content",
            "confluence-content-folder-property",
            "confluence-content-footer-comment",
            "confluence-content-footer-like",
            "confluence-content-inline-comment",
            "confluence-content-inline-like",
            "confluence-content-page",
            "confluence-content-page-content",
            "confluence-content-page-like",
            "confluence-content-page-property",
            "confluence-content-page-version",
            "confluence-content-smart-link",
            "confluence-content-task",
            "confluence-content-whiteboard",
            "confluence-content-whiteboard-content",
            "confluence-content-whiteboard-property",
            "confluence-content-read-records-1",
            "confluence-content-read-records-2",
            "confluence-content-read-records-3",
            "confluence-content-change-records",
            "confluence-spaces-available-space",
            "confluence-spaces-blog-post",
            "confluence-spaces-database-classification",
            "confluence-spaces-page-classification",
            "confluence-spaces-space",
            "confluence-spaces-space-default",
            "confluence-spaces-space-property",
            "confluence-spaces-space-role",
            "confluence-spaces-whiteboard-classification",
            "confluence-spaces-read-records",
            "confluence-spaces-change-records",
            "confluence-platform-admin-key",
            "confluence-platform-forge-app",
            "confluence-platform-read-records",
            "confluence-platform-change-records",
        ),
        description="Find, write and organize Confluence knowledge and keep space access correct.",
    ),
    BusinessRole(
        "organization administrator",
        tasks=(
            "org-directory-org",
            "org-directory-user",
            "org-domain",
            "org-domain-id",
            "org-event",
            "org-event-action",
            "org-event-id",
            "org-group",
            "org-group-count",
            "org-group-role",
            "org-group-stat",
            "org",
            "org-id",
            "org-policy",
            "org-policy-id",
            "org-policy-resource",
            "org-resource-policy",
            "org-role",
            "org-role-group",
            "org-user",
            "org-user-role",
            "org-user-stat",
            "org-v1-org",
            "org-v2-org",
            "org-workspace-v2",
            "lifecycle-scim-link",
            "lifecycle-user-account",
            "lifecycle-user-an",
            "lifecycle-user-information",
            "lifecycle-read-records",
            "lifecycle-change-records",
            "controls-api-key",
            "controls-api-token",
            "controls-is-create",
            "controls-is-delete",
            "controls-is-get",
            "controls-is-update",
            "controls-level",
            "controls-service-account",
            "controls-read-records",
            "controls-change-records",
        ),
        description="Administer the Atlassian organization: directories, accounts, policies and security controls.",
    ),
    BusinessRole(
        "data steward",
        tasks=(
            "kg-change-records",
            "jira-issues-application-property",
            "jira-issues-attachment",
            "jira-issues-comment",
            "jira-issues-comment-property",
            "jira-issues-forge-app",
            "jira-issues-ids-worklog",
            "jira-issues-issue",
            "jira-issues-issue-link",
            "jira-issues-issue-property",
            "jira-issues-issue-using",
            "jira-issues-jql-query",
            "jira-issues-property-resource",
            "jira-issues-reconsile-issue",
            "jira-issues-remote-issue",
            "jira-issues-set-issue",
            "jira-issues-transition",
            "jira-issues-vote",
            "jira-issues-watcher",
            "jira-issues-worklog",
            "jira-issues-worklog-property",
            "jira-issues-read-records-1",
            "jira-issues-read-records-2",
            "jira-issues-change-records-1",
            "jira-issues-change-records-2",
            "confluence-content-attachment",
            "confluence-content-attachment-content",
            "confluence-content-attachment-property",
            "confluence-content-attachment-version",
            "confluence-content-blog-post",
            "confluence-content-blogpost-content",
            "confluence-content-blogpost-property",
            "confluence-content-comment-content",
            "confluence-content-comment-property",
            "confluence-content-custom-content",
            "confluence-content-database",
            "confluence-content-database-content",
            "confluence-content-database-property",
            "confluence-content-folder",
            "confluence-content-folder-content",
            "confluence-content-folder-property",
            "confluence-content-footer-comment",
            "confluence-content-footer-like",
            "confluence-content-inline-comment",
            "confluence-content-inline-like",
            "confluence-content-page",
            "confluence-content-page-content",
            "confluence-content-page-like",
            "confluence-content-page-property",
            "confluence-content-page-version",
            "confluence-content-smart-link",
            "confluence-content-task",
            "confluence-content-whiteboard",
            "confluence-content-whiteboard-content",
            "confluence-content-whiteboard-property",
            "confluence-content-read-records-1",
            "confluence-content-read-records-2",
            "confluence-content-read-records-3",
            "confluence-content-change-records",
        ),
        description="Keep the knowledge graph in step with Jira and Confluence.",
    ),
)
