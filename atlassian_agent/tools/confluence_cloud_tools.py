# Generated MCP Tools for ConfluenceCloud
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.confluence_cloud_api import ConfluenceCloudAPI
from ..auth import get_base_client


def get_api() -> ConfluenceCloudAPI:
    return ConfluenceCloudAPI(get_base_client())


def register_confluence_cloud_tools(mcp: FastMCP):
    @mcp.tool(name="confluence_cloud_get_admin_key", tags={"confluence-cloud-other"})
    def confluence_cloud_get_admin_key(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get Admin Key"""
        api = get_api()
        response = api.confluence_cloud_get_admin_key()
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_enable_admin_key", tags={"confluence-cloud-other"})
    def confluence_cloud_enable_admin_key(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Enable Admin Key"""
        api = get_api()
        response = api.confluence_cloud_enable_admin_key(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_disable_admin_key", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_disable_admin_key(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Disable Admin Key"""
        api = get_api()
        response = api.confluence_cloud_disable_admin_key()
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachments", tags={"confluence-cloud-attachment"}
    )
    def confluence_cloud_get_attachments(
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        status: list[Any] | None = Field(
            None,
            description="Filter the results to attachments based on their status. By default, `current` and `archived` are used.",
        ),
        media_type: str | None = Field(
            None,
            description="Filters on the mediaType of attachments. Only one may be specified.",
        ),
        filename: str | None = Field(
            None,
            description="Filters on the file-name of attachments. Only one may be specified.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachments"""
        api = get_api()
        response = api.confluence_cloud_get_attachments(
            sort=sort,
            cursor=cursor,
            status=status,
            media_type=media_type,
            filename=filename,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachment_by_id",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_attachment_by_id(
        id_: str = Field(
            ...,
            description="The ID of the attachment to be returned. If you don't know the attachment's ID, use Get attachments for page/blogpost/custom content.",
        ),
        version: int | None = Field(
            None,
            description="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.",
        ),
        include_labels: bool | None = Field(
            None,
            description="Includes labels associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this attachment in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_versions: bool | None = Field(
            None,
            description="Includes versions associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_version: bool | None = Field(
            None,
            description="Includes the current version associated with this attachment in the response. By default this is included and can be omitted by setting the value to `false`.",
        ),
        include_collaborators: bool | None = Field(
            None, description="Includes collaborators on the attachment."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachment by id"""
        api = get_api()
        response = api.confluence_cloud_get_attachment_by_id(
            id_=id_,
            version=version,
            include_labels=include_labels,
            include_properties=include_properties,
            include_operations=include_operations,
            include_versions=include_versions,
            include_version=include_version,
            include_collaborators=include_collaborators,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_attachment", tags={"confluence-cloud-attachment"}
    )
    def confluence_cloud_delete_attachment(
        id_: int = Field(..., description="The ID of the attachment to be deleted."),
        purge: bool | None = Field(
            None, description="If attempting to purge the attachment."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete attachment"""
        api = get_api()
        response = api.confluence_cloud_delete_attachment(
            id_=id_,
            purge=purge,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachment_labels",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_attachment_labels(
        id_: int = Field(
            ...,
            description="The ID of the attachment for which labels should be returned.",
        ),
        prefix: str | None = Field(
            None, description="Filter the results to labels based on their prefix."
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get labels for attachment"""
        api = get_api()
        response = api.confluence_cloud_get_attachment_labels(
            id_=id_,
            prefix=prefix,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachment_operations",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_attachment_operations(
        id_: str = Field(
            ...,
            description="The ID of the attachment for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for attachment"""
        api = get_api()
        response = api.confluence_cloud_get_attachment_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachment_content_properties",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_attachment_content_properties(
        attachment_id: str = Field(
            ...,
            description="The ID of the attachment for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for attachment"""
        api = get_api()
        response = api.confluence_cloud_get_attachment_content_properties(
            attachment_id=attachment_id,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_attachment_property",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_create_attachment_property(
        attachment_id: str = Field(
            ..., description="The ID of the attachment to create a property for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for attachment"""
        api = get_api()
        response = api.confluence_cloud_create_attachment_property(
            attachment_id=attachment_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachment_content_properties_by_id",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_attachment_content_properties_by_id(
        attachment_id: str = Field(
            ...,
            description="The ID of the attachment for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the content property to be returned"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for attachment by id"""
        api = get_api()
        response = api.confluence_cloud_get_attachment_content_properties_by_id(
            attachment_id=attachment_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_attachment_property_by_id",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_update_attachment_property_by_id(
        attachment_id: str = Field(
            ..., description="The ID of the attachment the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for attachment by id"""
        api = get_api()
        response = api.confluence_cloud_update_attachment_property_by_id(
            attachment_id=attachment_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_attachment_property_by_id",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_delete_attachment_property_by_id(
        attachment_id: str = Field(
            ..., description="The ID of the attachment the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for attachment by id"""
        api = get_api()
        response = api.confluence_cloud_delete_attachment_property_by_id(
            attachment_id=attachment_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachment_versions",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_attachment_versions(
        id_: str = Field(
            ...,
            description="The ID of the attachment to be queried for its versions. If you don't know the attachment ID, use Get attachments and filter the results.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachment versions"""
        api = get_api()
        response = api.confluence_cloud_get_attachment_versions(
            id_=id_,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachment_version_details",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_attachment_version_details(
        attachment_id: str = Field(
            ...,
            description="The ID of the attachment for which version details should be returned.",
        ),
        version_number: int = Field(
            ..., description="The version number of the attachment to be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version details for attachment version"""
        api = get_api()
        response = api.confluence_cloud_get_attachment_version_details(
            attachment_id=attachment_id,
            version_number=version_number,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_attachment_comments",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_attachment_comments(
        id_: str = Field(
            ...,
            description="The ID of the attachment for which comments should be returned.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        version: int | None = Field(
            None,
            description="Version number of the attachment to retrieve comments for. If no version provided, retrieves comments for the latest version.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachment comments"""
        api = get_api()
        response = api.confluence_cloud_get_attachment_comments(
            id_=id_,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
            sort=sort,
            version=version,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_get_blog_posts", tags={"confluence-cloud-other"})
    def confluence_cloud_get_blog_posts(
        id_: list[Any] | None = Field(
            None,
            description="Filter the results based on blog post ids. Multiple blog post ids can be specified as a comma-separated list.",
        ),
        space_id: list[Any] | None = Field(
            None,
            description="Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        status: list[Any] | None = Field(
            None,
            description="Filter the results to blog posts based on their status. By default, `current` is used.",
        ),
        title: str | None = Field(
            None, description="Filter the results to blog posts based on their title."
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of blog posts per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get blog posts"""
        api = get_api()
        response = api.confluence_cloud_get_blog_posts(
            id_=id_,
            space_id=space_id,
            sort=sort,
            status=status,
            title=title,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_create_blog_post", tags={"confluence-cloud-other"})
    def confluence_cloud_create_blog_post(
        private: bool | None = Field(
            None,
            description="The blog post will be private. Only the user who creates this blog post will have permission to view and edit one.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create blog post"""
        api = get_api()
        response = api.confluence_cloud_create_blog_post(
            private=private,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_by_id", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_blog_post_by_id(
        id_: int = Field(
            ...,
            description="The ID of the blog post to be returned. If you don't know the blog post ID, use Get blog posts and filter the results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        get_draft: bool | None = Field(
            None, description="Retrieve the draft version of this blog post."
        ),
        status: list[Any] | None = Field(
            None, description="Filter the blog post being retrieved by its status."
        ),
        version: int | None = Field(
            None,
            description="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.",
        ),
        include_labels: bool | None = Field(
            None,
            description="Includes labels associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this blog post in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_likes: bool | None = Field(
            None,
            description="Includes likes associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_versions: bool | None = Field(
            None,
            description="Includes versions associated with this blog post in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_version: bool | None = Field(
            None,
            description="Includes the current version associated with this blog post in the response. By default this is included and can be omitted by setting the value to `false`.",
        ),
        include_favorited_by_current_user_status: bool | None = Field(
            None,
            description="Includes whether this blog post has been favorited by the current user.",
        ),
        include_webresources: bool | None = Field(
            None,
            description="Includes web resources that can be used to render blog post content on a client.",
        ),
        include_collaborators: bool | None = Field(
            None, description="Includes collaborators on the blog post."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get blog post by id"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_by_id(
            id_=id_,
            body_format=body_format,
            get_draft=get_draft,
            status=status,
            version=version,
            include_labels=include_labels,
            include_properties=include_properties,
            include_operations=include_operations,
            include_likes=include_likes,
            include_versions=include_versions,
            include_version=include_version,
            include_favorited_by_current_user_status=include_favorited_by_current_user_status,
            include_webresources=include_webresources,
            include_collaborators=include_collaborators,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_update_blog_post", tags={"confluence-cloud-other"})
    def confluence_cloud_update_blog_post(
        id_: int = Field(
            ...,
            description="The ID of the blog post to be updated. If you don't know the blog post ID, use Get Blog Posts and filter the results.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update blog post"""
        api = get_api()
        response = api.confluence_cloud_update_blog_post(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_delete_blog_post", tags={"confluence-cloud-other"})
    def confluence_cloud_delete_blog_post(
        id_: int = Field(..., description="The ID of the blog post to be deleted."),
        purge: bool | None = Field(
            None, description="If attempting to purge the blog post."
        ),
        draft: bool | None = Field(
            None, description="If attempting to delete a blog post that is a draft."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete blog post"""
        api = get_api()
        response = api.confluence_cloud_delete_blog_post(
            id_=id_,
            purge=purge,
            draft=draft,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blogpost_attachments",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_blogpost_attachments(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which attachments should be returned.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        status: list[Any] | None = Field(
            None,
            description="Filter the results to attachments based on their status. By default, `current` and `archived` are used.",
        ),
        media_type: str | None = Field(
            None,
            description="Filters on the mediaType of attachments. Only one may be specified.",
        ),
        filename: str | None = Field(
            None,
            description="Filters on the file-name of attachments. Only one may be specified.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachments for blog post"""
        api = get_api()
        response = api.confluence_cloud_get_blogpost_attachments(
            id_=id_,
            sort=sort,
            cursor=cursor,
            status=status,
            media_type=media_type,
            filename=filename,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_by_type_in_blog_post",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_by_type_in_blog_post(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which custom content should be returned.",
        ),
        type_: str = Field(
            ...,
            description="The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.  Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom content by type in blog post"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_by_type_in_blog_post(
            id_=id_,
            type_=type_,
            sort=sort,
            cursor=cursor,
            limit=limit,
            body_format=body_format,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_labels", tags={"confluence-cloud-label"}
    )
    def confluence_cloud_get_blog_post_labels(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which labels should be returned.",
        ),
        prefix: str | None = Field(
            None, description="Filter the results to labels based on their prefix."
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get labels for blog post"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_labels(
            id_=id_,
            prefix=prefix,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_like_count",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_blog_post_like_count(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which like count should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get like count for blog post"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_like_count(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_like_users", tags={"confluence-cloud-user"}
    )
    def confluence_cloud_get_blog_post_like_users(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which account IDs should be returned.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get account IDs of likes for blog post"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_like_users(
            id_=id_,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blogpost_content_properties",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_blogpost_content_properties(
        blogpost_id: int = Field(
            ...,
            description="The ID of the blog post for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for blog post"""
        api = get_api()
        response = api.confluence_cloud_get_blogpost_content_properties(
            blogpost_id=blogpost_id,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_blogpost_property",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_create_blogpost_property(
        blogpost_id: int = Field(
            ..., description="The ID of the blog post to create a property for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for blog post"""
        api = get_api()
        response = api.confluence_cloud_create_blogpost_property(
            blogpost_id=blogpost_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blogpost_content_properties_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_blogpost_content_properties_by_id(
        blogpost_id: int = Field(
            ...,
            description="The ID of the blog post for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the property being requested"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for blog post by id"""
        api = get_api()
        response = api.confluence_cloud_get_blogpost_content_properties_by_id(
            blogpost_id=blogpost_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_blogpost_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_update_blogpost_property_by_id(
        blogpost_id: int = Field(
            ..., description="The ID of the blog post the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for blog post by id"""
        api = get_api()
        response = api.confluence_cloud_update_blogpost_property_by_id(
            blogpost_id=blogpost_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_blogpost_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_delete_blogpost_property_by_id(
        blogpost_id: int = Field(
            ..., description="The ID of the blog post the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for blogpost by id"""
        api = get_api()
        response = api.confluence_cloud_delete_blogpost_property_by_id(
            blogpost_id=blogpost_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_operations",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_blog_post_operations(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for blog post"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_versions", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_blog_post_versions(
        id_: int = Field(
            ...,
            description="The ID of the blog post to be queried for its versions. If you don't know the blog post ID, use Get blog posts and filter the results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get blog post versions"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_versions(
            id_=id_,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_version_details",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_blog_post_version_details(
        blogpost_id: int = Field(
            ...,
            description="The ID of the blog post for which version details should be returned.",
        ),
        version_number: int = Field(
            ..., description="The version number of the blog post to be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version details for blog post version"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_version_details(
            blogpost_id=blogpost_id,
            version_number=version_number,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_convert_content_ids_to_content_types",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_convert_content_ids_to_content_types(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Convert content ids to content types"""
        api = get_api()
        response = api.confluence_cloud_convert_content_ids_to_content_types(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_by_type",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_by_type(
        type_: str = Field(
            ...,
            description="The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.",
        ),
        id_: list[Any] | None = Field(
            None,
            description="Filter the results based on custom content ids. Multiple custom content ids can be specified as a comma-separated list.",
        ),
        space_id: list[Any] | None = Field(
            None,
            description="Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.  Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom content by type"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_by_type(
            type_=type_,
            id_=id_,
            space_id=space_id,
            sort=sort,
            cursor=cursor,
            limit=limit,
            body_format=body_format,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_custom_content", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_create_custom_content(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create custom content"""
        api = get_api()
        response = api.confluence_cloud_create_custom_content(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_by_id(
        id_: int = Field(
            ...,
            description="The ID of the custom content to be returned. If you don't know the custom content ID, use Get Custom Content by Type and filter the results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.  Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.",
        ),
        version: int | None = Field(
            None,
            description="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.",
        ),
        include_labels: bool | None = Field(
            None,
            description="Includes labels associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this custom content in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_versions: bool | None = Field(
            None,
            description="Includes versions associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_version: bool | None = Field(
            None,
            description="Includes the current version associated with this custom content in the response. By default this is included and can be omitted by setting the value to `false`.",
        ),
        include_collaborators: bool | None = Field(
            None, description="Includes collaborators on the custom content."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom content by id"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_by_id(
            id_=id_,
            body_format=body_format,
            version=version,
            include_labels=include_labels,
            include_properties=include_properties,
            include_operations=include_operations,
            include_versions=include_versions,
            include_version=include_version,
            include_collaborators=include_collaborators,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_custom_content", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_update_custom_content(
        id_: int = Field(
            ...,
            description="The ID of the custom content to be updated. If you don't know the custom content ID, use Get Custom Content by Type and filter the results.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update custom content"""
        api = get_api()
        response = api.confluence_cloud_update_custom_content(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_custom_content", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_delete_custom_content(
        id_: int = Field(
            ..., description="The ID of the custom content to be deleted."
        ),
        purge: bool | None = Field(
            None, description="If attempting to purge the custom content."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete custom content"""
        api = get_api()
        response = api.confluence_cloud_delete_custom_content(
            id_=id_,
            purge=purge,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_attachments",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_custom_content_attachments(
        id_: int = Field(
            ...,
            description="The ID of the custom content for which attachments should be returned.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        status: list[Any] | None = Field(
            None,
            description="Filter the results to attachments based on their status. By default, `current` and `archived` are used.",
        ),
        media_type: str | None = Field(
            None,
            description="Filters on the mediaType of attachments. Only one may be specified.",
        ),
        filename: str | None = Field(
            None,
            description="Filters on the file-name of attachments. Only one may be specified.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachments for custom content"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_attachments(
            id_=id_,
            sort=sort,
            cursor=cursor,
            status=status,
            media_type=media_type,
            filename=filename,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_comments",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_comments(
        id_: int = Field(
            ...,
            description="The ID of the custom content for which comments should be returned.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom content comments"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_comments(
            id_=id_,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_labels",
        tags={"confluence-cloud-label"},
    )
    def confluence_cloud_get_custom_content_labels(
        id_: int = Field(
            ...,
            description="The ID of the custom content for which labels should be returned.",
        ),
        prefix: str | None = Field(
            None, description="Filter the results to labels based on their prefix."
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get labels for custom content"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_labels(
            id_=id_,
            prefix=prefix,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_operations",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_operations(
        id_: int = Field(
            ...,
            description="The ID of the custom content for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for custom content"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_content_properties",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_content_properties(
        custom_content_id: int = Field(
            ...,
            description="The ID of the custom content for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for custom content"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_content_properties(
            custom_content_id=custom_content_id,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_custom_content_property",
        tags={"confluence-cloud-content-property"},
    )
    def confluence_cloud_create_custom_content_property(
        custom_content_id: int = Field(
            ..., description="The ID of the custom content to create a property for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for custom content"""
        api = get_api()
        response = api.confluence_cloud_create_custom_content_property(
            custom_content_id=custom_content_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_content_properties_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_content_properties_by_id(
        custom_content_id: int = Field(
            ...,
            description="The ID of the custom content for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the content property being requested."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for custom content by id"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_content_properties_by_id(
            custom_content_id=custom_content_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_custom_content_property_by_id",
        tags={"confluence-cloud-content-property"},
    )
    def confluence_cloud_update_custom_content_property_by_id(
        custom_content_id: int = Field(
            ..., description="The ID of the custom content the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for custom content by id"""
        api = get_api()
        response = api.confluence_cloud_update_custom_content_property_by_id(
            custom_content_id=custom_content_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_custom_content_property_by_id",
        tags={"confluence-cloud-content-property"},
    )
    def confluence_cloud_delete_custom_content_property_by_id(
        custom_content_id: int = Field(
            ..., description="The ID of the custom content the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for custom content by id"""
        api = get_api()
        response = api.confluence_cloud_delete_custom_content_property_by_id(
            custom_content_id=custom_content_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_get_labels", tags={"confluence-cloud-label"})
    def confluence_cloud_get_labels(
        label_id: list[Any] | None = Field(
            None,
            description="Filters on label ID. Multiple IDs can be specified as a comma-separated list.",
        ),
        prefix: list[Any] | None = Field(
            None,
            description="Filters on label prefix. Multiple IDs can be specified as a comma-separated list.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get labels"""
        api = get_api()
        response = api.confluence_cloud_get_labels(
            label_id=label_id,
            prefix=prefix,
            cursor=cursor,
            sort=sort,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_label_attachments",
        tags={"confluence-cloud-attachment"},
    )
    def confluence_cloud_get_label_attachments(
        id_: int = Field(
            ...,
            description="The ID of the label for which attachments should be returned.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachments for label"""
        api = get_api()
        response = api.confluence_cloud_get_label_attachments(
            id_=id_,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_label_blog_posts", tags={"confluence-cloud-label"}
    )
    def confluence_cloud_get_label_blog_posts(
        id_: int = Field(
            ...,
            description="The ID of the label for which blog posts should be returned.",
        ),
        space_id: list[Any] | None = Field(
            None,
            description="Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of blog posts per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get blog posts for label"""
        api = get_api()
        response = api.confluence_cloud_get_label_blog_posts(
            id_=id_,
            space_id=space_id,
            body_format=body_format,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_label_pages", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_label_pages(
        id_: int = Field(
            ..., description="The ID of the label for which pages should be returned."
        ),
        space_id: list[Any] | None = Field(
            None,
            description="Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get pages for label"""
        api = get_api()
        response = api.confluence_cloud_get_label_pages(
            id_=id_,
            space_id=space_id,
            body_format=body_format,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_get_pages", tags={"confluence-cloud-page-core"})
    def confluence_cloud_get_pages(
        id_: list[Any] | None = Field(
            None,
            description="Filter the results based on page ids. Multiple page ids can be specified as a comma-separated list.",
        ),
        space_id: list[Any] | None = Field(
            None,
            description="Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        status: list[Any] | None = Field(
            None,
            description="Filter the results to pages based on their status. By default, `current` and `archived` are used.",
        ),
        title: str | None = Field(
            None, description="Filter the results to pages based on their title."
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        subtype: str | None = Field(
            None, description="Filter the results to pages based on their subtype."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get pages"""
        api = get_api()
        response = api.confluence_cloud_get_pages(
            id_=id_,
            space_id=space_id,
            sort=sort,
            status=status,
            title=title,
            body_format=body_format,
            subtype=subtype,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_create_page", tags={"confluence-cloud-page-core"})
    def confluence_cloud_create_page(
        embedded: bool | None = Field(
            None,
            description="Tag the content as embedded and content will be created in NCS.",
        ),
        private: bool | None = Field(
            None,
            description="The page will be private. Only the user who creates this page will have permission to view and edit one.",
        ),
        root_level: bool | None = Field(
            None,
            description="The page will be created at the root level of the space (outside the space homepage tree). If true, then a  value may not be supplied for the `parentId` body parameter.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create page"""
        api = get_api()
        response = api.confluence_cloud_create_page(
            embedded=embedded,
            private=private,
            root_level=root_level,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_by_id", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_page_by_id(
        id_: int = Field(
            ...,
            description="The ID of the page to be returned. If you don't know the page ID, use Get pages and filter the results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        get_draft: bool | None = Field(
            None, description="Retrieve the draft version of this page."
        ),
        status: list[Any] | None = Field(
            None, description="Filter the page being retrieved by its status."
        ),
        version: int | None = Field(
            None,
            description="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.",
        ),
        include_labels: bool | None = Field(
            None,
            description="Includes labels associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this page in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_likes: bool | None = Field(
            None,
            description="Includes likes associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_versions: bool | None = Field(
            None,
            description="Includes versions associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_version: bool | None = Field(
            None,
            description="Includes the current version associated with this page in the response. By default this is included and can be omitted by setting the value to `false`.",
        ),
        include_favorited_by_current_user_status: bool | None = Field(
            None,
            description="Includes whether this page has been favorited by the current user.",
        ),
        include_webresources: bool | None = Field(
            None,
            description="Includes web resources that can be used to render page content on a client.",
        ),
        include_collaborators: bool | None = Field(
            None, description="Includes collaborators on the page."
        ),
        include_direct_children: bool | None = Field(
            None,
            description="Includes direct children of the page, as defined in the `ChildrenResponse` object.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get page by id"""
        api = get_api()
        response = api.confluence_cloud_get_page_by_id(
            id_=id_,
            body_format=body_format,
            get_draft=get_draft,
            status=status,
            version=version,
            include_labels=include_labels,
            include_properties=include_properties,
            include_operations=include_operations,
            include_likes=include_likes,
            include_versions=include_versions,
            include_version=include_version,
            include_favorited_by_current_user_status=include_favorited_by_current_user_status,
            include_webresources=include_webresources,
            include_collaborators=include_collaborators,
            include_direct_children=include_direct_children,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_update_page", tags={"confluence-cloud-page-core"})
    def confluence_cloud_update_page(
        id_: int = Field(
            ...,
            description="The ID of the page to be updated. If you don't know the page ID, use Get Pages and filter the results.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update page"""
        api = get_api()
        response = api.confluence_cloud_update_page(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_delete_page", tags={"confluence-cloud-page-core"})
    def confluence_cloud_delete_page(
        id_: int = Field(..., description="The ID of the page to be deleted."),
        purge: bool | None = Field(
            None, description="If attempting to purge the page."
        ),
        draft: bool | None = Field(
            None, description="If attempting to delete a page that is a draft."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete page"""
        api = get_api()
        response = api.confluence_cloud_delete_page(
            id_=id_,
            purge=purge,
            draft=draft,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_attachments",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_get_page_attachments(
        id_: int = Field(
            ...,
            description="The ID of the page for which attachments should be returned.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        status: list[Any] | None = Field(
            None,
            description="Filter the results to attachments based on their status. By default, `current` and `archived` are used.",
        ),
        media_type: str | None = Field(
            None,
            description="Filters on the mediaType of attachments. Only one may be specified.",
        ),
        filename: str | None = Field(
            None,
            description="Filters on the file-name of attachments. Only one may be specified.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachments for page"""
        api = get_api()
        response = api.confluence_cloud_get_page_attachments(
            id_=id_,
            sort=sort,
            cursor=cursor,
            status=status,
            media_type=media_type,
            filename=filename,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_by_type_in_page",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_get_custom_content_by_type_in_page(
        id_: int = Field(
            ...,
            description="The ID of the page for which custom content should be returned.",
        ),
        type_: str = Field(
            ...,
            description="The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.  Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom content by type in page"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_by_type_in_page(
            id_=id_,
            type_=type_,
            sort=sort,
            cursor=cursor,
            limit=limit,
            body_format=body_format,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_labels", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_page_labels(
        id_: int = Field(
            ..., description="The ID of the page for which labels should be returned."
        ),
        prefix: str | None = Field(
            None, description="Filter the results to labels based on their prefix."
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get labels for page"""
        api = get_api()
        response = api.confluence_cloud_get_page_labels(
            id_=id_,
            prefix=prefix,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_like_count", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_page_like_count(
        id_: int = Field(
            ...,
            description="The ID of the page for which like count should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get like count for page"""
        api = get_api()
        response = api.confluence_cloud_get_page_like_count(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_like_users", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_page_like_users(
        id_: int = Field(
            ...,
            description="The ID of the page for which like count should be returned.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get account IDs of likes for page"""
        api = get_api()
        response = api.confluence_cloud_get_page_like_users(
            id_=id_,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_operations", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_page_operations(
        id_: int = Field(
            ...,
            description="The ID of the page for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for page"""
        api = get_api()
        response = api.confluence_cloud_get_page_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_content_properties",
        tags={"confluence-cloud-page-content"},
    )
    def confluence_cloud_get_page_content_properties(
        page_id: int = Field(
            ...,
            description="The ID of the page for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for page"""
        api = get_api()
        response = api.confluence_cloud_get_page_content_properties(
            page_id=page_id,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_page_property",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_create_page_property(
        page_id: int = Field(
            ..., description="The ID of the page to create a property for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for page"""
        api = get_api()
        response = api.confluence_cloud_create_page_property(
            page_id=page_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_content_properties_by_id",
        tags={"confluence-cloud-page-content"},
    )
    def confluence_cloud_get_page_content_properties_by_id(
        page_id: int = Field(
            ...,
            description="The ID of the page for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the content property being requested."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for page by id"""
        api = get_api()
        response = api.confluence_cloud_get_page_content_properties_by_id(
            page_id=page_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_page_property_by_id",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_update_page_property_by_id(
        page_id: int = Field(
            ..., description="The ID of the page the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for page by id"""
        api = get_api()
        response = api.confluence_cloud_update_page_property_by_id(
            page_id=page_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_page_property_by_id",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_delete_page_property_by_id(
        page_id: int = Field(
            ..., description="The ID of the page the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for page by id"""
        api = get_api()
        response = api.confluence_cloud_delete_page_property_by_id(
            page_id=page_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_post_redact_page", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_post_redact_page(
        id_: int = Field(..., description="The ID of the page to redact content from."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Redact Content in a Confluence Page"""
        api = get_api()
        response = api.confluence_cloud_post_redact_page(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_post_redact_blog", tags={"confluence-cloud-other"})
    def confluence_cloud_post_redact_blog(
        id_: int = Field(
            ..., description="The ID of the blog post to redact content from."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Redact Content in a Confluence Blog Post"""
        api = get_api()
        response = api.confluence_cloud_post_redact_blog(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_page_title", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_update_page_title(
        id_: int = Field(
            ...,
            description="The ID of the page to be updated. If you don't know the page ID, use Get Pages and filter the results",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update page title"""
        api = get_api()
        response = api.confluence_cloud_update_page_title(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_versions", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_page_versions(
        id_: int = Field(
            ...,
            description="The ID of the page to be queried for its versions. If you don't know the page ID, use Get pages and filter the results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get page versions"""
        api = get_api()
        response = api.confluence_cloud_get_page_versions(
            id_=id_,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_whiteboard", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_create_whiteboard(
        private: bool | None = Field(
            None,
            description="The whiteboard will be private. Only the user who creates this whiteboard will have permission to view and edit one.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create whiteboard"""
        api = get_api()
        response = api.confluence_cloud_create_whiteboard(
            private=private,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_whiteboard_by_id", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_whiteboard_by_id(
        id_: int = Field(..., description="The ID of the whiteboard to be returned"),
        include_collaborators: bool | None = Field(
            None, description="Includes collaborators on the whiteboard."
        ),
        include_direct_children: bool | None = Field(
            None,
            description="Includes direct children of the whiteboard, as defined in the `ChildrenResponse` object.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this whiteboard in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this whiteboard in the response. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get whiteboard by id"""
        api = get_api()
        response = api.confluence_cloud_get_whiteboard_by_id(
            id_=id_,
            include_collaborators=include_collaborators,
            include_direct_children=include_direct_children,
            include_operations=include_operations,
            include_properties=include_properties,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_whiteboard", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_delete_whiteboard(
        id_: int = Field(..., description="The ID of the whiteboard to be deleted."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete whiteboard"""
        api = get_api()
        response = api.confluence_cloud_delete_whiteboard(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_whiteboard_content_properties",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_whiteboard_content_properties(
        id_: int = Field(
            ...,
            description="The ID of the whiteboard for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for whiteboard"""
        api = get_api()
        response = api.confluence_cloud_get_whiteboard_content_properties(
            id_=id_,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_whiteboard_property",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_create_whiteboard_property(
        id_: int = Field(
            ..., description="The ID of the whiteboard to create a property for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for whiteboard"""
        api = get_api()
        response = api.confluence_cloud_create_whiteboard_property(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_whiteboard_content_properties_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_whiteboard_content_properties_by_id(
        whiteboard_id: int = Field(
            ...,
            description="The ID of the whiteboard for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the content property being requested."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for whiteboard by id"""
        api = get_api()
        response = api.confluence_cloud_get_whiteboard_content_properties_by_id(
            whiteboard_id=whiteboard_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_whiteboard_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_update_whiteboard_property_by_id(
        whiteboard_id: int = Field(
            ..., description="The ID of the whiteboard the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for whiteboard by id"""
        api = get_api()
        response = api.confluence_cloud_update_whiteboard_property_by_id(
            whiteboard_id=whiteboard_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_whiteboard_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_delete_whiteboard_property_by_id(
        whiteboard_id: int = Field(
            ..., description="The ID of the whiteboard the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for whiteboard by id"""
        api = get_api()
        response = api.confluence_cloud_delete_whiteboard_property_by_id(
            whiteboard_id=whiteboard_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_whiteboard_operations",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_whiteboard_operations(
        id_: int = Field(
            ...,
            description="The ID of the whiteboard for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for a whiteboard"""
        api = get_api()
        response = api.confluence_cloud_get_whiteboard_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_whiteboard_direct_children",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_whiteboard_direct_children(
        id_: int = Field(..., description="The ID of the parent whiteboard."),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get direct children of a whiteboard"""
        api = get_api()
        response = api.confluence_cloud_get_whiteboard_direct_children(
            id_=id_,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_whiteboard_descendants",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_whiteboard_descendants(
        id_: int = Field(..., description="The ID of the whiteboard."),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results.",
        ),
        depth: int | None = Field(
            None,
            description="Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get descendants of a whiteboard"""
        api = get_api()
        response = api.confluence_cloud_get_whiteboard_descendants(
            id_=id_,
            limit=limit,
            depth=depth,
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_whiteboard_ancestors",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_whiteboard_ancestors(
        id_: int = Field(..., description="The ID of the whiteboard."),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all ancestors of whiteboard"""
        api = get_api()
        response = api.confluence_cloud_get_whiteboard_ancestors(
            id_=id_,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_create_database", tags={"confluence-cloud-other"})
    def confluence_cloud_create_database(
        private: bool | None = Field(
            None,
            description="The database will be private. Only the user who creates this database will have permission to view and edit one.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create database"""
        api = get_api()
        response = api.confluence_cloud_create_database(
            private=private,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_database_by_id", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_database_by_id(
        id_: int = Field(..., description="The ID of the database to be returned"),
        include_collaborators: bool | None = Field(
            None, description="Includes collaborators on the database."
        ),
        include_direct_children: bool | None = Field(
            None,
            description="Includes direct children of the database, as defined in the `ChildrenResponse` object.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this database in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this database in the response. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get database by id"""
        api = get_api()
        response = api.confluence_cloud_get_database_by_id(
            id_=id_,
            include_collaborators=include_collaborators,
            include_direct_children=include_direct_children,
            include_operations=include_operations,
            include_properties=include_properties,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_delete_database", tags={"confluence-cloud-other"})
    def confluence_cloud_delete_database(
        id_: int = Field(..., description="The ID of the database to be deleted."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete database"""
        api = get_api()
        response = api.confluence_cloud_delete_database(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_database_content_properties",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_database_content_properties(
        id_: int = Field(
            ...,
            description="The ID of the database for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for database"""
        api = get_api()
        response = api.confluence_cloud_get_database_content_properties(
            id_=id_,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_database_property",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_create_database_property(
        id_: int = Field(
            ..., description="The ID of the database to create a property for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for database"""
        api = get_api()
        response = api.confluence_cloud_create_database_property(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_database_content_properties_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_database_content_properties_by_id(
        database_id: int = Field(
            ...,
            description="The ID of the database for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the content property being requested."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for database by id"""
        api = get_api()
        response = api.confluence_cloud_get_database_content_properties_by_id(
            database_id=database_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_database_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_update_database_property_by_id(
        database_id: int = Field(
            ..., description="The ID of the database the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for database by id"""
        api = get_api()
        response = api.confluence_cloud_update_database_property_by_id(
            database_id=database_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_database_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_delete_database_property_by_id(
        database_id: int = Field(
            ..., description="The ID of the database the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for database by id"""
        api = get_api()
        response = api.confluence_cloud_delete_database_property_by_id(
            database_id=database_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_database_operations", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_database_operations(
        id_: int = Field(
            ...,
            description="The ID of the database for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for a database"""
        api = get_api()
        response = api.confluence_cloud_get_database_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_database_direct_children",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_database_direct_children(
        id_: int = Field(..., description="The ID of the parent database."),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get direct children of a database"""
        api = get_api()
        response = api.confluence_cloud_get_database_direct_children(
            id_=id_,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_database_descendants",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_database_descendants(
        id_: int = Field(..., description="The ID of the database."),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results.",
        ),
        depth: int | None = Field(
            None,
            description="Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get descendants of a database"""
        api = get_api()
        response = api.confluence_cloud_get_database_descendants(
            id_=id_,
            limit=limit,
            depth=depth,
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_database_ancestors", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_database_ancestors(
        id_: int = Field(..., description="The ID of the database."),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all ancestors of database"""
        api = get_api()
        response = api.confluence_cloud_get_database_ancestors(
            id_=id_,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_smart_link", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_create_smart_link(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create Smart Link in the content tree"""
        api = get_api()
        response = api.confluence_cloud_create_smart_link(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_smart_link_by_id", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_smart_link_by_id(
        id_: int = Field(
            ...,
            description="The ID of the Smart Link in the content tree to be returned.",
        ),
        include_collaborators: bool | None = Field(
            None, description="Includes collaborators on the Smart Link."
        ),
        include_direct_children: bool | None = Field(
            None,
            description="Includes direct children of the Smart Link, as defined in the `ChildrenResponse` object.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this Smart Link in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this Smart Link in the response. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get Smart Link in the content tree by id"""
        api = get_api()
        response = api.confluence_cloud_get_smart_link_by_id(
            id_=id_,
            include_collaborators=include_collaborators,
            include_direct_children=include_direct_children,
            include_operations=include_operations,
            include_properties=include_properties,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_smart_link", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_delete_smart_link(
        id_: int = Field(
            ...,
            description="The ID of the Smart Link in the content tree to be deleted.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete Smart Link in the content tree"""
        api = get_api()
        response = api.confluence_cloud_delete_smart_link(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_smart_link_content_properties",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_smart_link_content_properties(
        id_: int = Field(
            ...,
            description="The ID of the Smart Link in the content tree for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of Smart Links per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for Smart Link in the content tree"""
        api = get_api()
        response = api.confluence_cloud_get_smart_link_content_properties(
            id_=id_,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_smart_link_property",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_create_smart_link_property(
        id_: int = Field(
            ...,
            description="The ID of the Smart Link in the content tree to create a property for.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for Smart Link in the content tree"""
        api = get_api()
        response = api.confluence_cloud_create_smart_link_property(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_smart_link_content_properties_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_smart_link_content_properties_by_id(
        embed_id: int = Field(
            ...,
            description="The ID of the Smart Link in the content tree for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the content property being requested."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for Smart Link in the content tree by id"""
        api = get_api()
        response = api.confluence_cloud_get_smart_link_content_properties_by_id(
            embed_id=embed_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_smart_link_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_update_smart_link_property_by_id(
        embed_id: int = Field(
            ...,
            description="The ID of the Smart Link in the content tree the property belongs to.",
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for Smart Link in the content tree by id"""
        api = get_api()
        response = api.confluence_cloud_update_smart_link_property_by_id(
            embed_id=embed_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_smart_link_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_delete_smart_link_property_by_id(
        embed_id: int = Field(
            ...,
            description="The ID of the Smart Link in the content tree the property belongs to.",
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for Smart Link in the content tree by id"""
        api = get_api()
        response = api.confluence_cloud_delete_smart_link_property_by_id(
            embed_id=embed_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_smart_link_operations",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_smart_link_operations(
        id_: int = Field(
            ...,
            description="The ID of the Smart Link in the content tree for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for a Smart Link in the content tree"""
        api = get_api()
        response = api.confluence_cloud_get_smart_link_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_smart_link_direct_children",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_smart_link_direct_children(
        id_: int = Field(..., description="The ID of the parent smart link."),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get direct children of a Smart Link"""
        api = get_api()
        response = api.confluence_cloud_get_smart_link_direct_children(
            id_=id_,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_smart_link_descendants",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_smart_link_descendants(
        id_: int = Field(..., description="The ID of the smart link."),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results.",
        ),
        depth: int | None = Field(
            None,
            description="Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get descendants of a smart link"""
        api = get_api()
        response = api.confluence_cloud_get_smart_link_descendants(
            id_=id_,
            limit=limit,
            depth=depth,
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_smart_link_ancestors",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_smart_link_ancestors(
        id_: int = Field(
            ..., description="The ID of the Smart Link in the content tree."
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all ancestors of Smart Link in content tree"""
        api = get_api()
        response = api.confluence_cloud_get_smart_link_ancestors(
            id_=id_,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_create_folder", tags={"confluence-cloud-other"})
    def confluence_cloud_create_folder(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create folder"""
        api = get_api()
        response = api.confluence_cloud_create_folder(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_get_folder_by_id", tags={"confluence-cloud-other"})
    def confluence_cloud_get_folder_by_id(
        id_: int = Field(..., description="The ID of the folder to be returned."),
        include_collaborators: bool | None = Field(
            None, description="Includes collaborators on the folder."
        ),
        include_direct_children: bool | None = Field(
            None,
            description="Includes direct children of the folder, as defined in the `ChildrenResponse` object.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this folder in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this folder in the response. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get folder by id"""
        api = get_api()
        response = api.confluence_cloud_get_folder_by_id(
            id_=id_,
            include_collaborators=include_collaborators,
            include_direct_children=include_direct_children,
            include_operations=include_operations,
            include_properties=include_properties,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_delete_folder", tags={"confluence-cloud-other"})
    def confluence_cloud_delete_folder(
        id_: int = Field(..., description="The ID of the folder to be deleted."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete folder"""
        api = get_api()
        response = api.confluence_cloud_delete_folder(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_folder_content_properties",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_folder_content_properties(
        id_: int = Field(
            ...,
            description="The ID of the folder for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for folder"""
        api = get_api()
        response = api.confluence_cloud_get_folder_content_properties(
            id_=id_,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_folder_property", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_create_folder_property(
        id_: int = Field(
            ..., description="The ID of the folder to create a property for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for folder"""
        api = get_api()
        response = api.confluence_cloud_create_folder_property(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_folder_content_properties_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_folder_content_properties_by_id(
        folder_id: int = Field(
            ...,
            description="The ID of the folder for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the content property being requested."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for folder by id"""
        api = get_api()
        response = api.confluence_cloud_get_folder_content_properties_by_id(
            folder_id=folder_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_folder_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_update_folder_property_by_id(
        folder_id: int = Field(
            ..., description="The ID of the folder the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for folder by id"""
        api = get_api()
        response = api.confluence_cloud_update_folder_property_by_id(
            folder_id=folder_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_folder_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_delete_folder_property_by_id(
        folder_id: int = Field(
            ..., description="The ID of the folder the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for folder by id"""
        api = get_api()
        response = api.confluence_cloud_delete_folder_property_by_id(
            folder_id=folder_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_folder_operations", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_folder_operations(
        id_: int = Field(
            ...,
            description="The ID of the folder for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for a folder"""
        api = get_api()
        response = api.confluence_cloud_get_folder_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_folder_direct_children",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_folder_direct_children(
        id_: int = Field(..., description="The ID of the parent folder."),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get direct children of a folder"""
        api = get_api()
        response = api.confluence_cloud_get_folder_direct_children(
            id_=id_,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_folder_descendants", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_folder_descendants(
        id_: int = Field(..., description="The ID of the folder."),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results.",
        ),
        depth: int | None = Field(
            None,
            description="Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get descendants of folder"""
        api = get_api()
        response = api.confluence_cloud_get_folder_descendants(
            id_=id_,
            limit=limit,
            depth=depth,
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_folder_ancestors", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_folder_ancestors(
        id_: int = Field(..., description="The ID of the folder."),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all ancestors of folder"""
        api = get_api()
        response = api.confluence_cloud_get_folder_ancestors(
            id_=id_,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_version_details",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_get_page_version_details(
        page_id: int = Field(
            ...,
            description="The ID of the page for which version details should be returned.",
        ),
        version_number: int = Field(
            ..., description="The version number of the page to be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version details for page version"""
        api = get_api()
        response = api.confluence_cloud_get_page_version_details(
            page_id=page_id,
            version_number=version_number,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_versions",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_versions(
        custom_content_id: int = Field(
            ...,
            description="The ID of the custom content to be queried for its versions. If you don't know the custom content ID, use Get custom-content by type and filter the results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.  Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom content versions"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_versions(
            custom_content_id=custom_content_id,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_version_details",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_custom_content_version_details(
        custom_content_id: int = Field(
            ...,
            description="The ID of the custom content for which version details should be returned.",
        ),
        version_number: int = Field(
            ..., description="The version number of the custom content to be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version details for custom content version"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_version_details(
            custom_content_id=custom_content_id,
            version_number=version_number,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_get_spaces", tags={"confluence-cloud-space-core"})
    def confluence_cloud_get_spaces(
        ids: list[Any] | None = Field(
            None,
            description="Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list.",
        ),
        keys: list[Any] | None = Field(
            None,
            description="Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list.",
        ),
        type_: str | None = Field(
            None, description="Filter the results to spaces based on their type."
        ),
        status: str | None = Field(
            None, description="Filter the results to spaces based on their status."
        ),
        labels: list[Any] | None = Field(
            None,
            description="Filter the results to spaces based on their labels. Multiple labels can be specified as a comma-separated list.",
        ),
        favorited_by: str | None = Field(
            None,
            description="Filter the results to spaces favorited by the user with the specified account ID.",
        ),
        not_favorited_by: str | None = Field(
            None,
            description="Filter the results to spaces NOT favorited by the user with the specified account ID.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        description_format: str | None = Field(
            None,
            description="The content format type to be returned in the `description` field of the response. If available, the representation will be available under a response field of the same name under the `description` field.",
        ),
        include_icon: bool | None = Field(
            None, description="If the icon for the space should be fetched or not."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of spaces per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get spaces"""
        api = get_api()
        response = api.confluence_cloud_get_spaces(
            ids=ids,
            keys=keys,
            type_=type_,
            status=status,
            labels=labels,
            favorited_by=favorited_by,
            not_favorited_by=not_favorited_by,
            sort=sort,
            description_format=description_format,
            include_icon=include_icon,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_space", tags={"confluence-cloud-space-core"}
    )
    def confluence_cloud_create_space(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create space"""
        api = get_api()
        response = api.confluence_cloud_create_space(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_by_id", tags={"confluence-cloud-space-core"}
    )
    def confluence_cloud_get_space_by_id(
        id_: int = Field(..., description="The ID of the space to be returned."),
        description_format: str | None = Field(
            None,
            description="The content format type to be returned in the `description` field of the response. If available, the representation will be available under a response field of the same name under the `description` field.",
        ),
        include_icon: bool | None = Field(
            None, description="If the icon for the space should be fetched or not."
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this space in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes space properties associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_permissions: bool | None = Field(
            None,
            description="Includes space permissions associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_role_assignments: bool | None = Field(
            None,
            description="Includes role assignments associated with this space in the response. This parameter is only accepted for EAP sites. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_labels: bool | None = Field(
            None,
            description="Includes labels associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order. A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space by id"""
        api = get_api()
        response = api.confluence_cloud_get_space_by_id(
            id_=id_,
            description_format=description_format,
            include_icon=include_icon,
            include_operations=include_operations,
            include_properties=include_properties,
            include_permissions=include_permissions,
            include_role_assignments=include_role_assignments,
            include_labels=include_labels,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_posts_in_space",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_blog_posts_in_space(
        id_: int = Field(
            ...,
            description="The ID of the space for which blog posts should be returned.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        status: list[Any] | None = Field(
            None,
            description="Filter the results to blog posts based on their status. By default, `current` is used.",
        ),
        title: str | None = Field(
            None, description="Filter the results to blog posts based on their title."
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of blog posts per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get blog posts in space"""
        api = get_api()
        response = api.confluence_cloud_get_blog_posts_in_space(
            id_=id_,
            sort=sort,
            status=status,
            title=title,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_labels", tags={"confluence-cloud-space-core"}
    )
    def confluence_cloud_get_space_labels(
        id_: int = Field(
            ..., description="The ID of the space for which labels should be returned."
        ),
        prefix: str | None = Field(
            None, description="Filter the results to labels based on their prefix."
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get labels for space"""
        api = get_api()
        response = api.confluence_cloud_get_space_labels(
            id_=id_,
            prefix=prefix,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_content_labels",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_space_content_labels(
        id_: int = Field(
            ..., description="The ID of the space for which labels should be returned."
        ),
        prefix: str | None = Field(
            None, description="Filter the results to labels based on their prefix."
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get labels for space content"""
        api = get_api()
        response = api.confluence_cloud_get_space_content_labels(
            id_=id_,
            prefix=prefix,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_custom_content_by_type_in_space",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_custom_content_by_type_in_space(
        id_: int = Field(
            ...,
            description="The ID of the space for which custom content should be returned.",
        ),
        type_: str = Field(
            ...,
            description="The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.  Note: If the custom content body type is `storage`, the `storage` and `atlas_doc_format` body formats are able to be returned. If the custom content body type is `raw`, only the `raw` body format is able to be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom content by type in space"""
        api = get_api()
        response = api.confluence_cloud_get_custom_content_by_type_in_space(
            id_=id_,
            type_=type_,
            cursor=cursor,
            limit=limit,
            body_format=body_format,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_operations",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_space_operations(
        id_: int = Field(
            ...,
            description="The ID of the space for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for space"""
        api = get_api()
        response = api.confluence_cloud_get_space_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_pages_in_space", tags={"confluence-cloud-space-core"}
    )
    def confluence_cloud_get_pages_in_space(
        id_: int = Field(
            ..., description="The ID of the space for which pages should be returned."
        ),
        depth: str | None = Field(
            None,
            description="Filter the results to pages at the root level of the space or to all pages in the space.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        status: list[Any] | None = Field(
            None,
            description="Filter the results to pages based on their status. By default, `current` and `archived` are used.",
        ),
        title: str | None = Field(
            None, description="Filter the results to pages based on their title."
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get pages in space"""
        api = get_api()
        response = api.confluence_cloud_get_pages_in_space(
            id_=id_,
            depth=depth,
            sort=sort,
            status=status,
            title=title,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_properties",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_space_properties(
        space_id: int = Field(
            ...,
            description="The ID of the space for which space properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="The key of the space property to retrieve. This should be used when a user knows the key of their property, but needs to retrieve the id for use in other methods.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space properties in space"""
        api = get_api()
        response = api.confluence_cloud_get_space_properties(
            space_id=space_id,
            key=key,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_space_property",
        tags={"confluence-cloud-space-property"},
    )
    def confluence_cloud_create_space_property(
        space_id: int = Field(
            ...,
            description="The ID of the space for which space properties should be returned.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create space property in space"""
        api = get_api()
        response = api.confluence_cloud_create_space_property(
            space_id=space_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_property_by_id",
        tags={"confluence-cloud-space-property"},
    )
    def confluence_cloud_get_space_property_by_id(
        space_id: int = Field(
            ..., description="The ID of the space the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be retrieved."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space property by id"""
        api = get_api()
        response = api.confluence_cloud_get_space_property_by_id(
            space_id=space_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_space_property_by_id",
        tags={"confluence-cloud-space-property"},
    )
    def confluence_cloud_update_space_property_by_id(
        space_id: int = Field(
            ..., description="The ID of the space the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update space property by id"""
        api = get_api()
        response = api.confluence_cloud_update_space_property_by_id(
            space_id=space_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_space_property_by_id",
        tags={"confluence-cloud-space-property"},
    )
    def confluence_cloud_delete_space_property_by_id(
        space_id: int = Field(
            ..., description="The ID of the space the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete space property by id"""
        api = get_api()
        response = api.confluence_cloud_delete_space_property_by_id(
            space_id=space_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_permissions_assignments",
        tags={"confluence-cloud-space-permission"},
    )
    def confluence_cloud_get_space_permissions_assignments(
        id_: int = Field(..., description="The ID of the space to be returned."),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of assignments to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space permissions assignments"""
        api = get_api()
        response = api.confluence_cloud_get_space_permissions_assignments(
            id_=id_,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_available_space_permissions",
        tags={"confluence-cloud-space-permission"},
    )
    def confluence_cloud_get_available_space_permissions(
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of space permissions to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available space permissions"""
        api = get_api()
        response = api.confluence_cloud_get_available_space_permissions(
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_available_space_roles",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_available_space_roles(
        space_id: str | None = Field(
            None,
            description="The space ID for which to filter available space roles; if empty, return all available space roles for the tenant.",
        ),
        role_type: str | None = Field(
            None, description="The space role type to filter results by."
        ),
        principal_id: str | None = Field(
            None,
            description="The principal ID to filter results by. If specified, a principal-type must also be specified. Paired with a `principal-type` of `ACCESS_CLASS`, valid values include [`anonymous-users`, `jsm-project-admins`, `authenticated-users`, `all-licensed-users`, `all-product-admins`]",
        ),
        principal_type: str | None = Field(
            None,
            description="The principal type to filter results by. If specified, a principal-id must also be specified.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of space roles to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available space roles"""
        api = get_api()
        response = api.confluence_cloud_get_available_space_roles(
            space_id=space_id,
            role_type=role_type,
            principal_id=principal_id,
            principal_type=principal_type,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_space_role", tags={"confluence-cloud-space-core"}
    )
    def confluence_cloud_create_space_role(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a space role"""
        api = get_api()
        response = api.confluence_cloud_create_space_role(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_roles_by_id",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_space_roles_by_id(
        id_: int = Field(..., description="The ID of the space role to retrieve."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space role by ID"""
        api = get_api()
        response = api.confluence_cloud_get_space_roles_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_space_role", tags={"confluence-cloud-space-core"}
    )
    def confluence_cloud_update_space_role(
        id_: str = Field(..., description="Id of the space role"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a space role"""
        api = get_api()
        response = api.confluence_cloud_update_space_role(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_space_role", tags={"confluence-cloud-space-core"}
    )
    def confluence_cloud_delete_space_role(
        id_: str = Field(..., description="Id of the space role"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a space role"""
        api = get_api()
        response = api.confluence_cloud_delete_space_role(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_role_mode",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_space_role_mode(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space role mode"""
        api = get_api()
        response = api.confluence_cloud_get_space_role_mode()
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_role_assignments",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_space_role_assignments(
        id_: int = Field(
            ..., description="The ID of the space for which to retrieve assignments."
        ),
        role_id: str | None = Field(
            None,
            description="Filters the returned role assignments to the provided role ID.",
        ),
        role_type: str | None = Field(
            None,
            description="Filters the returned role assignments to the provided role type.",
        ),
        principal_id: str | None = Field(
            None,
            description="Filters the returned role assignments to the provided principal id. If specified, a principal-type must also be specified. Paired with a `principal-type` of `ACCESS_CLASS`, valid values include [`anonymous-users`, `jsm-project-admins`, `authenticated-users`, `all-licensed-users`, `all-product-admins`]",
        ),
        principal_type: str | None = Field(
            None,
            description="Filters the returned role assignments to the provided principal type. If specified, a principal-id must also be specified.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of space roles to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space role assignments"""
        api = get_api()
        response = api.confluence_cloud_get_space_role_assignments(
            id_=id_,
            role_id=role_id,
            role_type=role_type,
            principal_id=principal_id,
            principal_type=principal_type,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_set_space_role_assignments",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_set_space_role_assignments(
        id_: int = Field(
            ..., description="The ID of the space for which to retrieve assignments."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set space role assignments"""
        api = get_api()
        response = api.confluence_cloud_set_space_role_assignments(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_footer_comments",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_get_page_footer_comments(
        id_: int = Field(
            ...,
            description="The ID of the page for which footer comments should be returned.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        status: list[Any] | None = Field(
            None, description="Filter the footer comment being retrieved by its status."
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get footer comments for page"""
        api = get_api()
        response = api.confluence_cloud_get_page_footer_comments(
            id_=id_,
            body_format=body_format,
            status=status,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_inline_comments",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_get_page_inline_comments(
        id_: int = Field(
            ...,
            description="The ID of the page for which inline comments should be returned.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        status: list[Any] | None = Field(
            None, description="Filter the inline comment being retrieved by its status."
        ),
        resolution_status: list[Any] | None = Field(
            None,
            description="Filter the inline comment being retrieved by its resolution status.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of inline comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get inline comments for page"""
        api = get_api()
        response = api.confluence_cloud_get_page_inline_comments(
            id_=id_,
            body_format=body_format,
            status=status,
            resolution_status=resolution_status,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_footer_comments",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_blog_post_footer_comments(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which footer comments should be returned.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        status: list[Any] | None = Field(
            None, description="Filter the footer comment being retrieved by its status."
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get footer comments for blog post"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_footer_comments(
            id_=id_,
            body_format=body_format,
            status=status,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_inline_comments",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_blog_post_inline_comments(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which inline comments should be returned.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        status: list[Any] | None = Field(
            None, description="Filter the inline comment being retrieved by its status."
        ),
        resolution_status: list[Any] | None = Field(
            None,
            description="Filter the inline comment being retrieved by its resolution status.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of inline comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get inline comments for blog post"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_inline_comments(
            id_=id_,
            body_format=body_format,
            status=status,
            resolution_status=resolution_status,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_footer_comments", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_footer_comments(
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get footer comments"""
        api = get_api()
        response = api.confluence_cloud_get_footer_comments(
            body_format=body_format,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_footer_comment", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_create_footer_comment(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create footer comment"""
        api = get_api()
        response = api.confluence_cloud_create_footer_comment(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_footer_comment_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_footer_comment_by_id(
        comment_id: int = Field(
            ..., description="The ID of the comment to be retrieved."
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        version: int | None = Field(
            None,
            description="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this footer comment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this footer comment in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_likes: bool | None = Field(
            None,
            description="Includes likes associated with this footer comment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_versions: bool | None = Field(
            None,
            description="Includes versions associated with this footer comment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_version: bool | None = Field(
            None,
            description="Includes the current version associated with this footer comment in the response. By default this is included and can be omitted by setting the value to `false`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get footer comment by id"""
        api = get_api()
        response = api.confluence_cloud_get_footer_comment_by_id(
            comment_id=comment_id,
            body_format=body_format,
            version=version,
            include_properties=include_properties,
            include_operations=include_operations,
            include_likes=include_likes,
            include_versions=include_versions,
            include_version=include_version,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_footer_comment", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_update_footer_comment(
        comment_id: int = Field(
            ..., description="The ID of the comment to be retrieved."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update footer comment"""
        api = get_api()
        response = api.confluence_cloud_update_footer_comment(
            comment_id=comment_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_footer_comment", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_delete_footer_comment(
        comment_id: int = Field(
            ..., description="The ID of the comment to be retrieved."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete footer comment"""
        api = get_api()
        response = api.confluence_cloud_delete_footer_comment(
            comment_id=comment_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_footer_comment_children",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_footer_comment_children(
        id_: int = Field(
            ...,
            description="The ID of the parent comment for which footer comment children should be returned.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get children footer comments"""
        api = get_api()
        response = api.confluence_cloud_get_footer_comment_children(
            id_=id_,
            body_format=body_format,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_footer_like_count", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_footer_like_count(
        id_: int = Field(
            ...,
            description="The ID of the footer comment for which like count should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get like count for footer comment"""
        api = get_api()
        response = api.confluence_cloud_get_footer_like_count(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_footer_like_users", tags={"confluence-cloud-user"}
    )
    def confluence_cloud_get_footer_like_users(
        id_: int = Field(
            ...,
            description="The ID of the footer comment for which like count should be returned.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get account IDs of likes for footer comment"""
        api = get_api()
        response = api.confluence_cloud_get_footer_like_users(
            id_=id_,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_footer_comment_operations",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_footer_comment_operations(
        id_: int = Field(
            ...,
            description="The ID of the footer comment for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for footer comment"""
        api = get_api()
        response = api.confluence_cloud_get_footer_comment_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_footer_comment_versions",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_footer_comment_versions(
        id_: int = Field(
            ...,
            description="The ID of the footer comment for which versions should be returned",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get footer comment versions"""
        api = get_api()
        response = api.confluence_cloud_get_footer_comment_versions(
            id_=id_,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_footer_comment_version_details",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_footer_comment_version_details(
        id_: int = Field(
            ...,
            description="The ID of the footer comment for which version details should be returned.",
        ),
        version_number: int = Field(
            ..., description="The version number of the footer comment to be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version details for footer comment version"""
        api = get_api()
        response = api.confluence_cloud_get_footer_comment_version_details(
            id_=id_,
            version_number=version_number,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_inline_comments", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_inline_comments(
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get inline comments"""
        api = get_api()
        response = api.confluence_cloud_get_inline_comments(
            body_format=body_format,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_inline_comment", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_create_inline_comment(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create inline comment"""
        api = get_api()
        response = api.confluence_cloud_create_inline_comment(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_inline_comment_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_inline_comment_by_id(
        comment_id: int = Field(
            ..., description="The ID of the comment to be retrieved."
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        version: int | None = Field(
            None,
            description="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.",
        ),
        include_properties: bool | None = Field(
            None,
            description="Includes content properties associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_operations: bool | None = Field(
            None,
            description="Includes operations associated with this inline comment in the response, as defined in the `Operation` object. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_likes: bool | None = Field(
            None,
            description="Includes likes associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_versions: bool | None = Field(
            None,
            description="Includes versions associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order.  A `meta` and `_links` property will be present to indicate if more results are available and a link to retrieve the rest of the results.",
        ),
        include_version: bool | None = Field(
            None,
            description="Includes the current version associated with this inline comment in the response. By default this is included and can be omitted by setting the value to `false`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get inline comment by id"""
        api = get_api()
        response = api.confluence_cloud_get_inline_comment_by_id(
            comment_id=comment_id,
            body_format=body_format,
            version=version,
            include_properties=include_properties,
            include_operations=include_operations,
            include_likes=include_likes,
            include_versions=include_versions,
            include_version=include_version,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_inline_comment", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_update_inline_comment(
        comment_id: int = Field(
            ..., description="The ID of the comment to be retrieved."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update inline comment"""
        api = get_api()
        response = api.confluence_cloud_update_inline_comment(
            comment_id=comment_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_inline_comment", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_delete_inline_comment(
        comment_id: int = Field(
            ..., description="The ID of the comment to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete inline comment"""
        api = get_api()
        response = api.confluence_cloud_delete_inline_comment(
            comment_id=comment_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_inline_comment_children",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_inline_comment_children(
        id_: int = Field(
            ...,
            description="The ID of the parent comment for which inline comment children should be returned.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get children inline comments"""
        api = get_api()
        response = api.confluence_cloud_get_inline_comment_children(
            id_=id_,
            body_format=body_format,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_inline_like_count", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_inline_like_count(
        id_: int = Field(
            ...,
            description="The ID of the inline comment for which like count should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get like count for inline comment"""
        api = get_api()
        response = api.confluence_cloud_get_inline_like_count(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_inline_like_users", tags={"confluence-cloud-user"}
    )
    def confluence_cloud_get_inline_like_users(
        id_: int = Field(
            ...,
            description="The ID of the inline comment for which like count should be returned.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get account IDs of likes for inline comment"""
        api = get_api()
        response = api.confluence_cloud_get_inline_like_users(
            id_=id_,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_inline_comment_operations",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_inline_comment_operations(
        id_: int = Field(
            ...,
            description="The ID of the inline comment for which operations should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permitted operations for inline comment"""
        api = get_api()
        response = api.confluence_cloud_get_inline_comment_operations(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_inline_comment_versions",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_inline_comment_versions(
        id_: int = Field(
            ...,
            description="The ID of the inline comment for which versions should be returned",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get inline comment versions"""
        api = get_api()
        response = api.confluence_cloud_get_inline_comment_versions(
            id_=id_,
            body_format=body_format,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_inline_comment_version_details",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_inline_comment_version_details(
        id_: int = Field(
            ...,
            description="The ID of the inline comment for which version details should be returned.",
        ),
        version_number: int = Field(
            ..., description="The version number of the inline comment to be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version details for inline comment version"""
        api = get_api()
        response = api.confluence_cloud_get_inline_comment_version_details(
            id_=id_,
            version_number=version_number,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_comment_content_properties",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_comment_content_properties(
        comment_id: int = Field(
            ...,
            description="The ID of the comment for which content properties should be returned.",
        ),
        key: str | None = Field(
            None,
            description="Filters the response to return a specific content property with matching key (case sensitive).",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content properties for comment"""
        api = get_api()
        response = api.confluence_cloud_get_comment_content_properties(
            comment_id=comment_id,
            key=key,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_comment_property", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_create_comment_property(
        comment_id: int = Field(
            ..., description="The ID of the comment to create a property for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content property for comment"""
        api = get_api()
        response = api.confluence_cloud_create_comment_property(
            comment_id=comment_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_comment_content_properties_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_comment_content_properties_by_id(
        comment_id: int = Field(
            ...,
            description="The ID of the comment for which content properties should be returned.",
        ),
        property_id: int = Field(
            ..., description="The ID of the content property being requested."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content property for comment by id"""
        api = get_api()
        response = api.confluence_cloud_get_comment_content_properties_by_id(
            comment_id=comment_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_update_comment_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_update_comment_property_by_id(
        comment_id: int = Field(
            ..., description="The ID of the comment the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property for comment by id"""
        api = get_api()
        response = api.confluence_cloud_update_comment_property_by_id(
            comment_id=comment_id,
            property_id=property_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_comment_property_by_id",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_delete_comment_property_by_id(
        comment_id: int = Field(
            ..., description="The ID of the comment the property belongs to."
        ),
        property_id: int = Field(
            ..., description="The ID of the property to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property for comment by id"""
        api = get_api()
        response = api.confluence_cloud_delete_comment_property_by_id(
            comment_id=comment_id,
            property_id=property_id,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_get_tasks", tags={"confluence-cloud-other"})
    def confluence_cloud_get_tasks(
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        include_blank_tasks: bool | None = Field(
            None,
            description="Specifies whether to include blank tasks in the response. Defaults to `true`.",
        ),
        status: str | None = Field(
            None, description="Filters on the status of the task."
        ),
        task_id: list[Any] | None = Field(
            None, description="Filters on task ID. Multiple IDs can be specified."
        ),
        space_id: list[Any] | None = Field(
            None,
            description="Filters on the space ID of the task. Multiple IDs can be specified.",
        ),
        page_id: list[Any] | None = Field(
            None,
            description="Filters on the page ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction.",
        ),
        blogpost_id: list[Any] | None = Field(
            None,
            description="Filters on the blog post ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction.",
        ),
        created_by: list[Any] | None = Field(
            None,
            description="Filters on the Account ID of the user who created this task. Multiple IDs can be specified.",
        ),
        assigned_to: list[Any] | None = Field(
            None,
            description="Filters on the Account ID of the user to whom this task is assigned. Multiple IDs can be specified.",
        ),
        completed_by: list[Any] | None = Field(
            None,
            description="Filters on the Account ID of the user who completed this task. Multiple IDs can be specified.",
        ),
        created_at_from: int | None = Field(
            None,
            description="Filters on start of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds.",
        ),
        created_at_to: int | None = Field(
            None,
            description="Filters on end of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds.",
        ),
        due_at_from: int | None = Field(
            None,
            description="Filters on start of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds.",
        ),
        due_at_to: int | None = Field(
            None,
            description="Filters on end of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds.",
        ),
        completed_at_from: int | None = Field(
            None,
            description="Filters on start of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds.",
        ),
        completed_at_to: int | None = Field(
            None,
            description="Filters on end of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of tasks per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get tasks"""
        api = get_api()
        response = api.confluence_cloud_get_tasks(
            body_format=body_format,
            include_blank_tasks=include_blank_tasks,
            status=status,
            task_id=task_id,
            space_id=space_id,
            page_id=page_id,
            blogpost_id=blogpost_id,
            created_by=created_by,
            assigned_to=assigned_to,
            completed_by=completed_by,
            created_at_from=created_at_from,
            created_at_to=created_at_to,
            due_at_from=due_at_from,
            due_at_to=due_at_to,
            completed_at_from=completed_at_from,
            completed_at_to=completed_at_to,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_get_task_by_id", tags={"confluence-cloud-other"})
    def confluence_cloud_get_task_by_id(
        id_: int = Field(
            ...,
            description="The ID of the task to be returned. If you don't know the task ID, use Get tasks and filter the results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get task by id"""
        api = get_api()
        response = api.confluence_cloud_get_task_by_id(
            id_=id_,
            body_format=body_format,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_update_task", tags={"confluence-cloud-other"})
    def confluence_cloud_update_task(
        id_: int = Field(
            ...,
            description="The ID of the task to be updated. If you don't know the task ID, use Get tasks and filter the results.",
        ),
        body_format: str | None = Field(
            None,
            description="The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update task"""
        api = get_api()
        response = api.confluence_cloud_update_task(
            id_=id_,
            body_format=body_format,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_child_pages", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_child_pages(
        id_: int = Field(
            ...,
            description="The ID of the parent page. If you don't know the page ID, use Get pages and filter the results.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get child pages"""
        api = get_api()
        response = api.confluence_cloud_get_child_pages(
            id_=id_,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_child_custom_content",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_child_custom_content(
        id_: int = Field(
            ...,
            description="The ID of the parent custom content. If you don't know the custom content ID, use Get custom-content and filter the results.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get child custom content"""
        api = get_api()
        response = api.confluence_cloud_get_child_custom_content(
            id_=id_,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_direct_children",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_get_page_direct_children(
        id_: int = Field(..., description="The ID of the parent page."),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get direct children of a page"""
        api = get_api()
        response = api.confluence_cloud_get_page_direct_children(
            id_=id_,
            cursor=cursor,
            limit=limit,
            sort=sort,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_ancestors", tags={"confluence-cloud-page-core"}
    )
    def confluence_cloud_get_page_ancestors(
        id_: int = Field(..., description="The ID of the page."),
        limit: int | None = Field(
            None,
            description="Maximum number of pages per result to return. If more results exist, call this endpoint with the highest ancestor's ID to fetch the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all ancestors of page"""
        api = get_api()
        response = api.confluence_cloud_get_page_ancestors(
            id_=id_,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_descendants",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_get_page_descendants(
        id_: int = Field(..., description="The ID of the page."),
        limit: int | None = Field(
            None,
            description="Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results.",
        ),
        depth: int | None = Field(
            None,
            description="Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants.",
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get descendants of page"""
        api = get_api()
        response = api.confluence_cloud_get_page_descendants(
            id_=id_,
            limit=limit,
            depth=depth,
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_create_bulk_user_lookup", tags={"confluence-cloud-user"}
    )
    def confluence_cloud_create_bulk_user_lookup(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create bulk user lookup using ids"""
        api = get_api()
        response = api.confluence_cloud_create_bulk_user_lookup(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_check_access_by_email", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_check_access_by_email(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Check site access for a list of emails"""
        api = get_api()
        response = api.confluence_cloud_check_access_by_email(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_cloud_invite_by_email", tags={"confluence-cloud-other"})
    def confluence_cloud_invite_by_email(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Invite a list of emails to the site"""
        api = get_api()
        response = api.confluence_cloud_invite_by_email(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_data_policy_metadata",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_data_policy_metadata(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get data policy metadata for the workspace"""
        api = get_api()
        response = api.confluence_cloud_get_data_policy_metadata()
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_data_policy_spaces",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_data_policy_spaces(
        ids: list[Any] | None = Field(
            None,
            description="Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list.",
        ),
        keys: list[Any] | None = Field(
            None,
            description="Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list.",
        ),
        sort: str | None = Field(
            None, description="Used to sort the result by a particular field."
        ),
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of spaces per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get spaces with data policies"""
        api = get_api()
        response = api.confluence_cloud_get_data_policy_spaces(
            ids=ids,
            keys=keys,
            sort=sort,
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_classification_levels",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_classification_levels(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of classification levels"""
        api = get_api()
        response = api.confluence_cloud_get_classification_levels()
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_space_default_classification_level",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_get_space_default_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the space for which default classification level should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space default classification level"""
        api = get_api()
        response = api.confluence_cloud_get_space_default_classification_level(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_put_space_default_classification_level",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_put_space_default_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the space for which default classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update space default classification level"""
        api = get_api()
        response = api.confluence_cloud_put_space_default_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_space_default_classification_level",
        tags={"confluence-cloud-space-core"},
    )
    def confluence_cloud_delete_space_default_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the space for which default classification level should be deleted.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete space default classification level"""
        api = get_api()
        response = api.confluence_cloud_delete_space_default_classification_level(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_page_classification_level",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_get_page_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the page for which classification level should be returned.",
        ),
        status: str | None = Field(
            None,
            description="Status of page from which classification level will fetched.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get page classification level"""
        api = get_api()
        response = api.confluence_cloud_get_page_classification_level(
            id_=id_,
            status=status,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_put_page_classification_level",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_put_page_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the page for which classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update page classification level"""
        api = get_api()
        response = api.confluence_cloud_put_page_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_post_page_classification_level",
        tags={"confluence-cloud-page-core"},
    )
    def confluence_cloud_post_page_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the page for which classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset page classification level"""
        api = get_api()
        response = api.confluence_cloud_post_page_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_blog_post_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_blog_post_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which classification level should be returned.",
        ),
        status: str | None = Field(
            None,
            description="Status of blog post from which classification level will fetched.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get blog post classification level"""
        api = get_api()
        response = api.confluence_cloud_get_blog_post_classification_level(
            id_=id_,
            status=status,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_put_blog_post_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_put_blog_post_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update blog post classification level"""
        api = get_api()
        response = api.confluence_cloud_put_blog_post_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_post_blog_post_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_post_blog_post_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the blog post for which classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset blog post classification level"""
        api = get_api()
        response = api.confluence_cloud_post_blog_post_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_whiteboard_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_whiteboard_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the whiteboard for which classification level should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get whiteboard classification level"""
        api = get_api()
        response = api.confluence_cloud_get_whiteboard_classification_level(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_put_whiteboard_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_put_whiteboard_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the whiteboard for which classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update whiteboard classification level"""
        api = get_api()
        response = api.confluence_cloud_put_whiteboard_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_post_whiteboard_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_post_whiteboard_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the whiteboard for which classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset whiteboard classification level"""
        api = get_api()
        response = api.confluence_cloud_post_whiteboard_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_database_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_database_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the database for which classification level should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get database classification level"""
        api = get_api()
        response = api.confluence_cloud_get_database_classification_level(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_put_database_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_put_database_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the database for which classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update database classification level"""
        api = get_api()
        response = api.confluence_cloud_put_database_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_post_database_classification_level",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_post_database_classification_level(
        id_: int = Field(
            ...,
            description="The ID of the database for which classification level should be updated.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset database classification level"""
        api = get_api()
        response = api.confluence_cloud_post_database_classification_level(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_forge_app_properties",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_get_forge_app_properties(
        cursor: str | None = Field(
            None,
            description="Used for pagination, this opaque cursor represents the last returned property key. It will be included in the response body as the next link. Use this key to request the next set of results.",
        ),
        limit: int | None = Field(
            None,
            description="Maximum number of app properties per result to return. If more results exist, use the last returned property key from the Link field in the response body as a cursor to retrieve the next set of results.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get Forge app properties."""
        api = get_api()
        response = api.confluence_cloud_get_forge_app_properties(
            cursor=cursor,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_get_forge_app_property", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_get_forge_app_property(
        property_key: str = Field(..., description="The key of the property"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a Forge app property by key."""
        api = get_api()
        response = api.confluence_cloud_get_forge_app_property(
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_put_forge_app_property", tags={"confluence-cloud-other"}
    )
    def confluence_cloud_put_forge_app_property(
        property_key: str = Field(..., description="The key of the property"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create or update a Forge app property."""
        api = get_api()
        response = api.confluence_cloud_put_forge_app_property(
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_cloud_delete_forge_app_property",
        tags={"confluence-cloud-other"},
    )
    def confluence_cloud_delete_forge_app_property(
        property_key: str = Field(..., description="The key of the property"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Deletes a Forge app property."""
        api = get_api()
        response = api.confluence_cloud_delete_forge_app_property(
            property_key=property_key,
        )
        return response.model_dump()
