# Generated API Client for ConfluenceCloud
from typing import Any

from ..models import Response
from .base import BaseAtlassianClient


class ConfluenceCloudAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def confluence_cloud_get_admin_key(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get Admin Key

        Path: /admin-key
        Method: GET
        """
        path = "/admin-key"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_enable_admin_key(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Enable Admin Key

        Path: /admin-key
        Method: POST
        """
        path = "/admin-key"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_disable_admin_key(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Disable Admin Key

        Path: /admin-key
        Method: DELETE
        """
        path = "/admin-key"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachments(
        self,
        sort: str | None = None,
        cursor: str | None = None,
        status: list[Any] | None = None,
        media_type: str | None = None,
        filename: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachments

        Path: /attachments
        Method: GET
        """
        path = "/attachments"
        params = {
            "sort": sort,
            "cursor": cursor,
            "status": status,
            "mediaType": media_type,
            "filename": filename,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachment_by_id(
        self,
        id_: str,
        version: int | None = None,
        include_labels: bool | None = None,
        include_properties: bool | None = None,
        include_operations: bool | None = None,
        include_versions: bool | None = None,
        include_version: bool | None = None,
        include_collaborators: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachment by id

        Path: /attachments/{id}
        Method: GET
        """
        path = f"/attachments/{id_}"
        params = {
            "version": version,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-versions": include_versions,
            "include-version": include_version,
            "include-collaborators": include_collaborators,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_attachment(
        self,
        id_: int,
        purge: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete attachment

        Path: /attachments/{id}
        Method: DELETE
        """
        path = f"/attachments/{id_}"
        params = {
            "purge": purge,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachment_labels(
        self,
        id_: int,
        prefix: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get labels for attachment

        Path: /attachments/{id}/labels
        Method: GET
        """
        path = f"/attachments/{id_}/labels"
        params = {
            "prefix": prefix,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachment_operations(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for attachment

        Path: /attachments/{id}/operations
        Method: GET
        """
        path = f"/attachments/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachment_content_properties(
        self,
        attachment_id: str,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for attachment

        Path: /attachments/{attachment-id}/properties
        Method: GET
        """
        path = f"/attachments/{attachment_id}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_attachment_property(
        self,
        attachment_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for attachment

        Path: /attachments/{attachment-id}/properties
        Method: POST
        """
        path = f"/attachments/{attachment_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachment_content_properties_by_id(
        self,
        attachment_id: str,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for attachment by id

        Path: /attachments/{attachment-id}/properties/{property-id}
        Method: GET
        """
        path = f"/attachments/{attachment_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_attachment_property_by_id(
        self,
        attachment_id: str,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for attachment by id

        Path: /attachments/{attachment-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/attachments/{attachment_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_attachment_property_by_id(
        self,
        attachment_id: str,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for attachment by id

        Path: /attachments/{attachment-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/attachments/{attachment_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachment_versions(
        self,
        id_: str,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachment versions

        Path: /attachments/{id}/versions
        Method: GET
        """
        path = f"/attachments/{id_}/versions"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachment_version_details(
        self,
        attachment_id: str,
        version_number: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version details for attachment version

        Path: /attachments/{attachment-id}/versions/{version-number}
        Method: GET
        """
        path = f"/attachments/{attachment_id}/versions/{version_number}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_attachment_comments(
        self,
        id_: str,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        version: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachment comments

        Path: /attachments/{id}/footer-comments
        Method: GET
        """
        path = f"/attachments/{id_}/footer-comments"
        params = {
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
            "version": version,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_posts(
        self,
        id_: list[Any] | None = None,
        space_id: list[Any] | None = None,
        sort: str | None = None,
        status: list[Any] | None = None,
        title: str | None = None,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get blog posts

        Path: /blogposts
        Method: GET
        """
        path = "/blogposts"
        params = {
            "id": id_,
            "space-id": space_id,
            "sort": sort,
            "status": status,
            "title": title,
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_blog_post(
        self,
        private: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create blog post

        Path: /blogposts
        Method: POST
        """
        path = "/blogposts"
        params = {
            "private": private,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_by_id(
        self,
        id_: int,
        body_format: str | None = None,
        get_draft: bool | None = None,
        status: list[Any] | None = None,
        version: int | None = None,
        include_labels: bool | None = None,
        include_properties: bool | None = None,
        include_operations: bool | None = None,
        include_likes: bool | None = None,
        include_versions: bool | None = None,
        include_version: bool | None = None,
        include_favorited_by_current_user_status: bool | None = None,
        include_webresources: bool | None = None,
        include_collaborators: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get blog post by id

        Path: /blogposts/{id}
        Method: GET
        """
        path = f"/blogposts/{id_}"
        params = {
            "body-format": body_format,
            "get-draft": get_draft,
            "status": status,
            "version": version,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-likes": include_likes,
            "include-versions": include_versions,
            "include-version": include_version,
            "include-favorited-by-current-user-status": include_favorited_by_current_user_status,
            "include-webresources": include_webresources,
            "include-collaborators": include_collaborators,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_blog_post(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update blog post

        Path: /blogposts/{id}
        Method: PUT
        """
        path = f"/blogposts/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_blog_post(
        self,
        id_: int,
        purge: bool | None = None,
        draft: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete blog post

        Path: /blogposts/{id}
        Method: DELETE
        """
        path = f"/blogposts/{id_}"
        params = {
            "purge": purge,
            "draft": draft,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blogpost_attachments(
        self,
        id_: int,
        sort: str | None = None,
        cursor: str | None = None,
        status: list[Any] | None = None,
        media_type: str | None = None,
        filename: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachments for blog post

        Path: /blogposts/{id}/attachments
        Method: GET
        """
        path = f"/blogposts/{id_}/attachments"
        params = {
            "sort": sort,
            "cursor": cursor,
            "status": status,
            "mediaType": media_type,
            "filename": filename,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_by_type_in_blog_post(
        self,
        id_: int,
        type_: str,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        body_format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom content by type in blog post

        Path: /blogposts/{id}/custom-content
        Method: GET
        """
        path = f"/blogposts/{id_}/custom-content"
        params = {
            "type": type_,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
            "body-format": body_format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_labels(
        self,
        id_: int,
        prefix: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get labels for blog post

        Path: /blogposts/{id}/labels
        Method: GET
        """
        path = f"/blogposts/{id_}/labels"
        params = {
            "prefix": prefix,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_like_count(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get like count for blog post

        Path: /blogposts/{id}/likes/count
        Method: GET
        """
        path = f"/blogposts/{id_}/likes/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_like_users(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get account IDs of likes for blog post

        Path: /blogposts/{id}/likes/users
        Method: GET
        """
        path = f"/blogposts/{id_}/likes/users"
        params = {
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blogpost_content_properties(
        self,
        blogpost_id: int,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for blog post

        Path: /blogposts/{blogpost-id}/properties
        Method: GET
        """
        path = f"/blogposts/{blogpost_id}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_blogpost_property(
        self,
        blogpost_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for blog post

        Path: /blogposts/{blogpost-id}/properties
        Method: POST
        """
        path = f"/blogposts/{blogpost_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blogpost_content_properties_by_id(
        self,
        blogpost_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for blog post by id

        Path: /blogposts/{blogpost-id}/properties/{property-id}
        Method: GET
        """
        path = f"/blogposts/{blogpost_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_blogpost_property_by_id(
        self,
        blogpost_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for blog post by id

        Path: /blogposts/{blogpost-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/blogposts/{blogpost_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_blogpost_property_by_id(
        self,
        blogpost_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for blogpost by id

        Path: /blogposts/{blogpost-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/blogposts/{blogpost_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for blog post

        Path: /blogposts/{id}/operations
        Method: GET
        """
        path = f"/blogposts/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_versions(
        self,
        id_: int,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get blog post versions

        Path: /blogposts/{id}/versions
        Method: GET
        """
        path = f"/blogposts/{id_}/versions"
        params = {
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_version_details(
        self,
        blogpost_id: int,
        version_number: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version details for blog post version

        Path: /blogposts/{blogpost-id}/versions/{version-number}
        Method: GET
        """
        path = f"/blogposts/{blogpost_id}/versions/{version_number}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_convert_content_ids_to_content_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Convert content ids to content types

        Path: /content/convert-ids-to-types
        Method: POST
        """
        path = "/content/convert-ids-to-types"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_by_type(
        self,
        type_: str,
        id_: list[Any] | None = None,
        space_id: list[Any] | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        body_format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom content by type

        Path: /custom-content
        Method: GET
        """
        path = "/custom-content"
        params = {
            "type": type_,
            "id": id_,
            "space-id": space_id,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
            "body-format": body_format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_custom_content(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create custom content

        Path: /custom-content
        Method: POST
        """
        path = "/custom-content"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_by_id(
        self,
        id_: int,
        body_format: str | None = None,
        version: int | None = None,
        include_labels: bool | None = None,
        include_properties: bool | None = None,
        include_operations: bool | None = None,
        include_versions: bool | None = None,
        include_version: bool | None = None,
        include_collaborators: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom content by id

        Path: /custom-content/{id}
        Method: GET
        """
        path = f"/custom-content/{id_}"
        params = {
            "body-format": body_format,
            "version": version,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-versions": include_versions,
            "include-version": include_version,
            "include-collaborators": include_collaborators,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_custom_content(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update custom content

        Path: /custom-content/{id}
        Method: PUT
        """
        path = f"/custom-content/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_custom_content(
        self,
        id_: int,
        purge: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete custom content

        Path: /custom-content/{id}
        Method: DELETE
        """
        path = f"/custom-content/{id_}"
        params = {
            "purge": purge,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_attachments(
        self,
        id_: int,
        sort: str | None = None,
        cursor: str | None = None,
        status: list[Any] | None = None,
        media_type: str | None = None,
        filename: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachments for custom content

        Path: /custom-content/{id}/attachments
        Method: GET
        """
        path = f"/custom-content/{id_}/attachments"
        params = {
            "sort": sort,
            "cursor": cursor,
            "status": status,
            "mediaType": media_type,
            "filename": filename,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_comments(
        self,
        id_: int,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom content comments

        Path: /custom-content/{id}/footer-comments
        Method: GET
        """
        path = f"/custom-content/{id_}/footer-comments"
        params = {
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_labels(
        self,
        id_: int,
        prefix: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get labels for custom content

        Path: /custom-content/{id}/labels
        Method: GET
        """
        path = f"/custom-content/{id_}/labels"
        params = {
            "prefix": prefix,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for custom content

        Path: /custom-content/{id}/operations
        Method: GET
        """
        path = f"/custom-content/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_content_properties(
        self,
        custom_content_id: int,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for custom content

        Path: /custom-content/{custom-content-id}/properties
        Method: GET
        """
        path = f"/custom-content/{custom_content_id}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_custom_content_property(
        self,
        custom_content_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for custom content

        Path: /custom-content/{custom-content-id}/properties
        Method: POST
        """
        path = f"/custom-content/{custom_content_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_content_properties_by_id(
        self,
        custom_content_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for custom content by id

        Path: /custom-content/{custom-content-id}/properties/{property-id}
        Method: GET
        """
        path = f"/custom-content/{custom_content_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_custom_content_property_by_id(
        self,
        custom_content_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for custom content by id

        Path: /custom-content/{custom-content-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/custom-content/{custom_content_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_custom_content_property_by_id(
        self,
        custom_content_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for custom content by id

        Path: /custom-content/{custom-content-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/custom-content/{custom_content_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_labels(
        self,
        label_id: list[Any] | None = None,
        prefix: list[Any] | None = None,
        cursor: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get labels

        Path: /labels
        Method: GET
        """
        path = "/labels"
        params = {
            "label-id": label_id,
            "prefix": prefix,
            "cursor": cursor,
            "sort": sort,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_label_attachments(
        self,
        id_: int,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachments for label

        Path: /labels/{id}/attachments
        Method: GET
        """
        path = f"/labels/{id_}/attachments"
        params = {
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_label_blog_posts(
        self,
        id_: int,
        space_id: list[Any] | None = None,
        body_format: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get blog posts for label

        Path: /labels/{id}/blogposts
        Method: GET
        """
        path = f"/labels/{id_}/blogposts"
        params = {
            "space-id": space_id,
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_label_pages(
        self,
        id_: int,
        space_id: list[Any] | None = None,
        body_format: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get pages for label

        Path: /labels/{id}/pages
        Method: GET
        """
        path = f"/labels/{id_}/pages"
        params = {
            "space-id": space_id,
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_pages(
        self,
        id_: list[Any] | None = None,
        space_id: list[Any] | None = None,
        sort: str | None = None,
        status: list[Any] | None = None,
        title: str | None = None,
        body_format: str | None = None,
        subtype: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get pages

        Path: /pages
        Method: GET
        """
        path = "/pages"
        params = {
            "id": id_,
            "space-id": space_id,
            "sort": sort,
            "status": status,
            "title": title,
            "body-format": body_format,
            "subtype": subtype,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_page(
        self,
        embedded: bool | None = None,
        private: bool | None = None,
        root_level: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create page

        Path: /pages
        Method: POST
        """
        path = "/pages"
        params = {
            "embedded": embedded,
            "private": private,
            "root-level": root_level,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_by_id(
        self,
        id_: int,
        body_format: str | None = None,
        get_draft: bool | None = None,
        status: list[Any] | None = None,
        version: int | None = None,
        include_labels: bool | None = None,
        include_properties: bool | None = None,
        include_operations: bool | None = None,
        include_likes: bool | None = None,
        include_versions: bool | None = None,
        include_version: bool | None = None,
        include_favorited_by_current_user_status: bool | None = None,
        include_webresources: bool | None = None,
        include_collaborators: bool | None = None,
        include_direct_children: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get page by id

        Path: /pages/{id}
        Method: GET
        """
        path = f"/pages/{id_}"
        params = {
            "body-format": body_format,
            "get-draft": get_draft,
            "status": status,
            "version": version,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-likes": include_likes,
            "include-versions": include_versions,
            "include-version": include_version,
            "include-favorited-by-current-user-status": include_favorited_by_current_user_status,
            "include-webresources": include_webresources,
            "include-collaborators": include_collaborators,
            "include-direct-children": include_direct_children,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_page(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update page

        Path: /pages/{id}
        Method: PUT
        """
        path = f"/pages/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_page(
        self,
        id_: int,
        purge: bool | None = None,
        draft: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete page

        Path: /pages/{id}
        Method: DELETE
        """
        path = f"/pages/{id_}"
        params = {
            "purge": purge,
            "draft": draft,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_attachments(
        self,
        id_: int,
        sort: str | None = None,
        cursor: str | None = None,
        status: list[Any] | None = None,
        media_type: str | None = None,
        filename: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachments for page

        Path: /pages/{id}/attachments
        Method: GET
        """
        path = f"/pages/{id_}/attachments"
        params = {
            "sort": sort,
            "cursor": cursor,
            "status": status,
            "mediaType": media_type,
            "filename": filename,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_by_type_in_page(
        self,
        id_: int,
        type_: str,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        body_format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom content by type in page

        Path: /pages/{id}/custom-content
        Method: GET
        """
        path = f"/pages/{id_}/custom-content"
        params = {
            "type": type_,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
            "body-format": body_format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_labels(
        self,
        id_: int,
        prefix: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get labels for page

        Path: /pages/{id}/labels
        Method: GET
        """
        path = f"/pages/{id_}/labels"
        params = {
            "prefix": prefix,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_like_count(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get like count for page

        Path: /pages/{id}/likes/count
        Method: GET
        """
        path = f"/pages/{id_}/likes/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_like_users(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get account IDs of likes for page

        Path: /pages/{id}/likes/users
        Method: GET
        """
        path = f"/pages/{id_}/likes/users"
        params = {
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for page

        Path: /pages/{id}/operations
        Method: GET
        """
        path = f"/pages/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_content_properties(
        self,
        page_id: int,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for page

        Path: /pages/{page-id}/properties
        Method: GET
        """
        path = f"/pages/{page_id}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_page_property(
        self,
        page_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for page

        Path: /pages/{page-id}/properties
        Method: POST
        """
        path = f"/pages/{page_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_content_properties_by_id(
        self,
        page_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for page by id

        Path: /pages/{page-id}/properties/{property-id}
        Method: GET
        """
        path = f"/pages/{page_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_page_property_by_id(
        self,
        page_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for page by id

        Path: /pages/{page-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/pages/{page_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_page_property_by_id(
        self,
        page_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for page by id

        Path: /pages/{page-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/pages/{page_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_post_redact_page(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Redact Content in a Confluence Page

        Path: /pages/{id}/redact
        Method: POST
        """
        path = f"/pages/{id_}/redact"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_post_redact_blog(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Redact Content in a Confluence Blog Post

        Path: /blogposts/{id}/redact
        Method: POST
        """
        path = f"/blogposts/{id_}/redact"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_page_title(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update page title

        Path: /pages/{id}/title
        Method: PUT
        """
        path = f"/pages/{id_}/title"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_versions(
        self,
        id_: int,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get page versions

        Path: /pages/{id}/versions
        Method: GET
        """
        path = f"/pages/{id_}/versions"
        params = {
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_whiteboard(
        self,
        private: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create whiteboard

        Path: /whiteboards
        Method: POST
        """
        path = "/whiteboards"
        params = {
            "private": private,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_whiteboard_by_id(
        self,
        id_: int,
        include_collaborators: bool | None = None,
        include_direct_children: bool | None = None,
        include_operations: bool | None = None,
        include_properties: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get whiteboard by id

        Path: /whiteboards/{id}
        Method: GET
        """
        path = f"/whiteboards/{id_}"
        params = {
            "include-collaborators": include_collaborators,
            "include-direct-children": include_direct_children,
            "include-operations": include_operations,
            "include-properties": include_properties,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_whiteboard(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete whiteboard

        Path: /whiteboards/{id}
        Method: DELETE
        """
        path = f"/whiteboards/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_whiteboard_content_properties(
        self,
        id_: int,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for whiteboard

        Path: /whiteboards/{id}/properties
        Method: GET
        """
        path = f"/whiteboards/{id_}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_whiteboard_property(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for whiteboard

        Path: /whiteboards/{id}/properties
        Method: POST
        """
        path = f"/whiteboards/{id_}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_whiteboard_content_properties_by_id(
        self,
        whiteboard_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for whiteboard by id

        Path: /whiteboards/{whiteboard-id}/properties/{property-id}
        Method: GET
        """
        path = f"/whiteboards/{whiteboard_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_whiteboard_property_by_id(
        self,
        whiteboard_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for whiteboard by id

        Path: /whiteboards/{whiteboard-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/whiteboards/{whiteboard_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_whiteboard_property_by_id(
        self,
        whiteboard_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for whiteboard by id

        Path: /whiteboards/{whiteboard-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/whiteboards/{whiteboard_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_whiteboard_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for a whiteboard

        Path: /whiteboards/{id}/operations
        Method: GET
        """
        path = f"/whiteboards/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_whiteboard_direct_children(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get direct children of a whiteboard

        Path: /whiteboards/{id}/direct-children
        Method: GET
        """
        path = f"/whiteboards/{id_}/direct-children"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_whiteboard_descendants(
        self,
        id_: int,
        limit: int | None = None,
        depth: int | None = None,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get descendants of a whiteboard

        Path: /whiteboards/{id}/descendants
        Method: GET
        """
        path = f"/whiteboards/{id_}/descendants"
        params = {
            "limit": limit,
            "depth": depth,
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_whiteboard_ancestors(
        self,
        id_: int,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all ancestors of whiteboard

        Path: /whiteboards/{id}/ancestors
        Method: GET
        """
        path = f"/whiteboards/{id_}/ancestors"
        params = {
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_database(
        self,
        private: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create database

        Path: /databases
        Method: POST
        """
        path = "/databases"
        params = {
            "private": private,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_database_by_id(
        self,
        id_: int,
        include_collaborators: bool | None = None,
        include_direct_children: bool | None = None,
        include_operations: bool | None = None,
        include_properties: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get database by id

        Path: /databases/{id}
        Method: GET
        """
        path = f"/databases/{id_}"
        params = {
            "include-collaborators": include_collaborators,
            "include-direct-children": include_direct_children,
            "include-operations": include_operations,
            "include-properties": include_properties,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_database(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete database

        Path: /databases/{id}
        Method: DELETE
        """
        path = f"/databases/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_database_content_properties(
        self,
        id_: int,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for database

        Path: /databases/{id}/properties
        Method: GET
        """
        path = f"/databases/{id_}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_database_property(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for database

        Path: /databases/{id}/properties
        Method: POST
        """
        path = f"/databases/{id_}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_database_content_properties_by_id(
        self,
        database_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for database by id

        Path: /databases/{database-id}/properties/{property-id}
        Method: GET
        """
        path = f"/databases/{database_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_database_property_by_id(
        self,
        database_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for database by id

        Path: /databases/{database-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/databases/{database_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_database_property_by_id(
        self,
        database_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for database by id

        Path: /databases/{database-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/databases/{database_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_database_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for a database

        Path: /databases/{id}/operations
        Method: GET
        """
        path = f"/databases/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_database_direct_children(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get direct children of a database

        Path: /databases/{id}/direct-children
        Method: GET
        """
        path = f"/databases/{id_}/direct-children"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_database_descendants(
        self,
        id_: int,
        limit: int | None = None,
        depth: int | None = None,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get descendants of a database

        Path: /databases/{id}/descendants
        Method: GET
        """
        path = f"/databases/{id_}/descendants"
        params = {
            "limit": limit,
            "depth": depth,
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_database_ancestors(
        self,
        id_: int,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all ancestors of database

        Path: /databases/{id}/ancestors
        Method: GET
        """
        path = f"/databases/{id_}/ancestors"
        params = {
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_smart_link(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create Smart Link in the content tree

        Path: /embeds
        Method: POST
        """
        path = "/embeds"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_smart_link_by_id(
        self,
        id_: int,
        include_collaborators: bool | None = None,
        include_direct_children: bool | None = None,
        include_operations: bool | None = None,
        include_properties: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get Smart Link in the content tree by id

        Path: /embeds/{id}
        Method: GET
        """
        path = f"/embeds/{id_}"
        params = {
            "include-collaborators": include_collaborators,
            "include-direct-children": include_direct_children,
            "include-operations": include_operations,
            "include-properties": include_properties,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_smart_link(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete Smart Link in the content tree

        Path: /embeds/{id}
        Method: DELETE
        """
        path = f"/embeds/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_smart_link_content_properties(
        self,
        id_: int,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for Smart Link in the content tree

        Path: /embeds/{id}/properties
        Method: GET
        """
        path = f"/embeds/{id_}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_smart_link_property(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for Smart Link in the content tree

        Path: /embeds/{id}/properties
        Method: POST
        """
        path = f"/embeds/{id_}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_smart_link_content_properties_by_id(
        self,
        embed_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for Smart Link in the content tree by id

        Path: /embeds/{embed-id}/properties/{property-id}
        Method: GET
        """
        path = f"/embeds/{embed_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_smart_link_property_by_id(
        self,
        embed_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for Smart Link in the content tree by id

        Path: /embeds/{embed-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/embeds/{embed_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_smart_link_property_by_id(
        self,
        embed_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for Smart Link in the content tree by id

        Path: /embeds/{embed-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/embeds/{embed_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_smart_link_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for a Smart Link in the content tree

        Path: /embeds/{id}/operations
        Method: GET
        """
        path = f"/embeds/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_smart_link_direct_children(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get direct children of a Smart Link

        Path: /embeds/{id}/direct-children
        Method: GET
        """
        path = f"/embeds/{id_}/direct-children"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_smart_link_descendants(
        self,
        id_: int,
        limit: int | None = None,
        depth: int | None = None,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get descendants of a smart link

        Path: /embeds/{id}/descendants
        Method: GET
        """
        path = f"/embeds/{id_}/descendants"
        params = {
            "limit": limit,
            "depth": depth,
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_smart_link_ancestors(
        self,
        id_: int,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all ancestors of Smart Link in content tree

        Path: /embeds/{id}/ancestors
        Method: GET
        """
        path = f"/embeds/{id_}/ancestors"
        params = {
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_folder(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create folder

        Path: /folders
        Method: POST
        """
        path = "/folders"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_folder_by_id(
        self,
        id_: int,
        include_collaborators: bool | None = None,
        include_direct_children: bool | None = None,
        include_operations: bool | None = None,
        include_properties: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get folder by id

        Path: /folders/{id}
        Method: GET
        """
        path = f"/folders/{id_}"
        params = {
            "include-collaborators": include_collaborators,
            "include-direct-children": include_direct_children,
            "include-operations": include_operations,
            "include-properties": include_properties,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_folder(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete folder

        Path: /folders/{id}
        Method: DELETE
        """
        path = f"/folders/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_folder_content_properties(
        self,
        id_: int,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for folder

        Path: /folders/{id}/properties
        Method: GET
        """
        path = f"/folders/{id_}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_folder_property(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for folder

        Path: /folders/{id}/properties
        Method: POST
        """
        path = f"/folders/{id_}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_folder_content_properties_by_id(
        self,
        folder_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for folder by id

        Path: /folders/{folder-id}/properties/{property-id}
        Method: GET
        """
        path = f"/folders/{folder_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_folder_property_by_id(
        self,
        folder_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for folder by id

        Path: /folders/{folder-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/folders/{folder_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_folder_property_by_id(
        self,
        folder_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for folder by id

        Path: /folders/{folder-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/folders/{folder_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_folder_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for a folder

        Path: /folders/{id}/operations
        Method: GET
        """
        path = f"/folders/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_folder_direct_children(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get direct children of a folder

        Path: /folders/{id}/direct-children
        Method: GET
        """
        path = f"/folders/{id_}/direct-children"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_folder_descendants(
        self,
        id_: int,
        limit: int | None = None,
        depth: int | None = None,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get descendants of folder

        Path: /folders/{id}/descendants
        Method: GET
        """
        path = f"/folders/{id_}/descendants"
        params = {
            "limit": limit,
            "depth": depth,
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_folder_ancestors(
        self,
        id_: int,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all ancestors of folder

        Path: /folders/{id}/ancestors
        Method: GET
        """
        path = f"/folders/{id_}/ancestors"
        params = {
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_version_details(
        self,
        page_id: int,
        version_number: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version details for page version

        Path: /pages/{page-id}/versions/{version-number}
        Method: GET
        """
        path = f"/pages/{page_id}/versions/{version_number}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_versions(
        self,
        custom_content_id: int,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom content versions

        Path: /custom-content/{custom-content-id}/versions
        Method: GET
        """
        path = f"/custom-content/{custom_content_id}/versions"
        params = {
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_version_details(
        self,
        custom_content_id: int,
        version_number: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version details for custom content version

        Path: /custom-content/{custom-content-id}/versions/{version-number}
        Method: GET
        """
        path = f"/custom-content/{custom_content_id}/versions/{version_number}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_spaces(
        self,
        ids: list[Any] | None = None,
        keys: list[Any] | None = None,
        type_: str | None = None,
        status: str | None = None,
        labels: list[Any] | None = None,
        favorited_by: str | None = None,
        not_favorited_by: str | None = None,
        sort: str | None = None,
        description_format: str | None = None,
        include_icon: bool | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get spaces

        Path: /spaces
        Method: GET
        """
        path = "/spaces"
        params = {
            "ids": ids,
            "keys": keys,
            "type": type_,
            "status": status,
            "labels": labels,
            "favorited-by": favorited_by,
            "not-favorited-by": not_favorited_by,
            "sort": sort,
            "description-format": description_format,
            "include-icon": include_icon,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_space(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create space

        Path: /spaces
        Method: POST
        """
        path = "/spaces"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_by_id(
        self,
        id_: int,
        description_format: str | None = None,
        include_icon: bool | None = None,
        include_operations: bool | None = None,
        include_properties: bool | None = None,
        include_permissions: bool | None = None,
        include_role_assignments: bool | None = None,
        include_labels: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space by id

        Path: /spaces/{id}
        Method: GET
        """
        path = f"/spaces/{id_}"
        params = {
            "description-format": description_format,
            "include-icon": include_icon,
            "include-operations": include_operations,
            "include-properties": include_properties,
            "include-permissions": include_permissions,
            "include-role-assignments": include_role_assignments,
            "include-labels": include_labels,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_posts_in_space(
        self,
        id_: int,
        sort: str | None = None,
        status: list[Any] | None = None,
        title: str | None = None,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get blog posts in space

        Path: /spaces/{id}/blogposts
        Method: GET
        """
        path = f"/spaces/{id_}/blogposts"
        params = {
            "sort": sort,
            "status": status,
            "title": title,
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_labels(
        self,
        id_: int,
        prefix: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get labels for space

        Path: /spaces/{id}/labels
        Method: GET
        """
        path = f"/spaces/{id_}/labels"
        params = {
            "prefix": prefix,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_content_labels(
        self,
        id_: int,
        prefix: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get labels for space content

        Path: /spaces/{id}/content/labels
        Method: GET
        """
        path = f"/spaces/{id_}/content/labels"
        params = {
            "prefix": prefix,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_custom_content_by_type_in_space(
        self,
        id_: int,
        type_: str,
        cursor: str | None = None,
        limit: int | None = None,
        body_format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom content by type in space

        Path: /spaces/{id}/custom-content
        Method: GET
        """
        path = f"/spaces/{id_}/custom-content"
        params = {
            "type": type_,
            "cursor": cursor,
            "limit": limit,
            "body-format": body_format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for space

        Path: /spaces/{id}/operations
        Method: GET
        """
        path = f"/spaces/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_pages_in_space(
        self,
        id_: int,
        depth: str | None = None,
        sort: str | None = None,
        status: list[Any] | None = None,
        title: str | None = None,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get pages in space

        Path: /spaces/{id}/pages
        Method: GET
        """
        path = f"/spaces/{id_}/pages"
        params = {
            "depth": depth,
            "sort": sort,
            "status": status,
            "title": title,
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_properties(
        self,
        space_id: int,
        key: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space properties in space

        Path: /spaces/{space-id}/properties
        Method: GET
        """
        path = f"/spaces/{space_id}/properties"
        params = {
            "key": key,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_space_property(
        self,
        space_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create space property in space

        Path: /spaces/{space-id}/properties
        Method: POST
        """
        path = f"/spaces/{space_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_property_by_id(
        self,
        space_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space property by id

        Path: /spaces/{space-id}/properties/{property-id}
        Method: GET
        """
        path = f"/spaces/{space_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_space_property_by_id(
        self,
        space_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update space property by id

        Path: /spaces/{space-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/spaces/{space_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_space_property_by_id(
        self,
        space_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete space property by id

        Path: /spaces/{space-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/spaces/{space_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_permissions_assignments(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space permissions assignments

        Path: /spaces/{id}/permissions
        Method: GET
        """
        path = f"/spaces/{id_}/permissions"
        params = {
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_available_space_permissions(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get available space permissions

        Path: /space-permissions
        Method: GET
        """
        path = "/space-permissions"
        params = {
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_available_space_roles(
        self,
        space_id: str | None = None,
        role_type: str | None = None,
        principal_id: str | None = None,
        principal_type: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get available space roles

        Path: /space-roles
        Method: GET
        """
        path = "/space-roles"
        params = {
            "space-id": space_id,
            "role-type": role_type,
            "principal-id": principal_id,
            "principal-type": principal_type,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_space_role(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a space role

        Path: /space-roles
        Method: POST
        """
        path = "/space-roles"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_roles_by_id(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space role by ID

        Path: /space-roles/{id}
        Method: GET
        """
        path = f"/space-roles/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_space_role(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a space role

        Path: /space-roles/{id}
        Method: PUT
        """
        path = f"/space-roles/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_space_role(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a space role

        Path: /space-roles/{id}
        Method: DELETE
        """
        path = f"/space-roles/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_role_mode(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get space role mode

        Path: /space-role-mode
        Method: GET
        """
        path = "/space-role-mode"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_role_assignments(
        self,
        id_: int,
        role_id: str | None = None,
        role_type: str | None = None,
        principal_id: str | None = None,
        principal_type: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space role assignments

        Path: /spaces/{id}/role-assignments
        Method: GET
        """
        path = f"/spaces/{id_}/role-assignments"
        params = {
            "role-id": role_id,
            "role-type": role_type,
            "principal-id": principal_id,
            "principal-type": principal_type,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_set_space_role_assignments(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set space role assignments

        Path: /spaces/{id}/role-assignments
        Method: POST
        """
        path = f"/spaces/{id_}/role-assignments"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_footer_comments(
        self,
        id_: int,
        body_format: str | None = None,
        status: list[Any] | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get footer comments for page

        Path: /pages/{id}/footer-comments
        Method: GET
        """
        path = f"/pages/{id_}/footer-comments"
        params = {
            "body-format": body_format,
            "status": status,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_inline_comments(
        self,
        id_: int,
        body_format: str | None = None,
        status: list[Any] | None = None,
        resolution_status: list[Any] | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get inline comments for page

        Path: /pages/{id}/inline-comments
        Method: GET
        """
        path = f"/pages/{id_}/inline-comments"
        params = {
            "body-format": body_format,
            "status": status,
            "resolution-status": resolution_status,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_footer_comments(
        self,
        id_: int,
        body_format: str | None = None,
        status: list[Any] | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get footer comments for blog post

        Path: /blogposts/{id}/footer-comments
        Method: GET
        """
        path = f"/blogposts/{id_}/footer-comments"
        params = {
            "body-format": body_format,
            "status": status,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_inline_comments(
        self,
        id_: int,
        body_format: str | None = None,
        status: list[Any] | None = None,
        resolution_status: list[Any] | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get inline comments for blog post

        Path: /blogposts/{id}/inline-comments
        Method: GET
        """
        path = f"/blogposts/{id_}/inline-comments"
        params = {
            "body-format": body_format,
            "status": status,
            "resolution-status": resolution_status,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_footer_comments(
        self,
        body_format: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get footer comments

        Path: /footer-comments
        Method: GET
        """
        path = "/footer-comments"
        params = {
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_footer_comment(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create footer comment

        Path: /footer-comments
        Method: POST
        """
        path = "/footer-comments"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_footer_comment_by_id(
        self,
        comment_id: int,
        body_format: str | None = None,
        version: int | None = None,
        include_properties: bool | None = None,
        include_operations: bool | None = None,
        include_likes: bool | None = None,
        include_versions: bool | None = None,
        include_version: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get footer comment by id

        Path: /footer-comments/{comment-id}
        Method: GET
        """
        path = f"/footer-comments/{comment_id}"
        params = {
            "body-format": body_format,
            "version": version,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-likes": include_likes,
            "include-versions": include_versions,
            "include-version": include_version,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_footer_comment(
        self,
        comment_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update footer comment

        Path: /footer-comments/{comment-id}
        Method: PUT
        """
        path = f"/footer-comments/{comment_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_footer_comment(
        self,
        comment_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete footer comment

        Path: /footer-comments/{comment-id}
        Method: DELETE
        """
        path = f"/footer-comments/{comment_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_footer_comment_children(
        self,
        id_: int,
        body_format: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get children footer comments

        Path: /footer-comments/{id}/children
        Method: GET
        """
        path = f"/footer-comments/{id_}/children"
        params = {
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_footer_like_count(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get like count for footer comment

        Path: /footer-comments/{id}/likes/count
        Method: GET
        """
        path = f"/footer-comments/{id_}/likes/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_footer_like_users(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get account IDs of likes for footer comment

        Path: /footer-comments/{id}/likes/users
        Method: GET
        """
        path = f"/footer-comments/{id_}/likes/users"
        params = {
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_footer_comment_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for footer comment

        Path: /footer-comments/{id}/operations
        Method: GET
        """
        path = f"/footer-comments/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_footer_comment_versions(
        self,
        id_: int,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get footer comment versions

        Path: /footer-comments/{id}/versions
        Method: GET
        """
        path = f"/footer-comments/{id_}/versions"
        params = {
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_footer_comment_version_details(
        self,
        id_: int,
        version_number: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version details for footer comment version

        Path: /footer-comments/{id}/versions/{version-number}
        Method: GET
        """
        path = f"/footer-comments/{id_}/versions/{version_number}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_inline_comments(
        self,
        body_format: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get inline comments

        Path: /inline-comments
        Method: GET
        """
        path = "/inline-comments"
        params = {
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_inline_comment(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create inline comment

        Path: /inline-comments
        Method: POST
        """
        path = "/inline-comments"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_inline_comment_by_id(
        self,
        comment_id: int,
        body_format: str | None = None,
        version: int | None = None,
        include_properties: bool | None = None,
        include_operations: bool | None = None,
        include_likes: bool | None = None,
        include_versions: bool | None = None,
        include_version: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get inline comment by id

        Path: /inline-comments/{comment-id}
        Method: GET
        """
        path = f"/inline-comments/{comment_id}"
        params = {
            "body-format": body_format,
            "version": version,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-likes": include_likes,
            "include-versions": include_versions,
            "include-version": include_version,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_inline_comment(
        self,
        comment_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update inline comment

        Path: /inline-comments/{comment-id}
        Method: PUT
        """
        path = f"/inline-comments/{comment_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_inline_comment(
        self,
        comment_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete inline comment

        Path: /inline-comments/{comment-id}
        Method: DELETE
        """
        path = f"/inline-comments/{comment_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_inline_comment_children(
        self,
        id_: int,
        body_format: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get children inline comments

        Path: /inline-comments/{id}/children
        Method: GET
        """
        path = f"/inline-comments/{id_}/children"
        params = {
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_inline_like_count(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get like count for inline comment

        Path: /inline-comments/{id}/likes/count
        Method: GET
        """
        path = f"/inline-comments/{id_}/likes/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_inline_like_users(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get account IDs of likes for inline comment

        Path: /inline-comments/{id}/likes/users
        Method: GET
        """
        path = f"/inline-comments/{id_}/likes/users"
        params = {
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_inline_comment_operations(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permitted operations for inline comment

        Path: /inline-comments/{id}/operations
        Method: GET
        """
        path = f"/inline-comments/{id_}/operations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_inline_comment_versions(
        self,
        id_: int,
        body_format: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get inline comment versions

        Path: /inline-comments/{id}/versions
        Method: GET
        """
        path = f"/inline-comments/{id_}/versions"
        params = {
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_inline_comment_version_details(
        self,
        id_: int,
        version_number: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version details for inline comment version

        Path: /inline-comments/{id}/versions/{version-number}
        Method: GET
        """
        path = f"/inline-comments/{id_}/versions/{version_number}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_comment_content_properties(
        self,
        comment_id: int,
        key: str | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content properties for comment

        Path: /comments/{comment-id}/properties
        Method: GET
        """
        path = f"/comments/{comment_id}/properties"
        params = {
            "key": key,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_comment_property(
        self,
        comment_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content property for comment

        Path: /comments/{comment-id}/properties
        Method: POST
        """
        path = f"/comments/{comment_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_comment_content_properties_by_id(
        self,
        comment_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content property for comment by id

        Path: /comments/{comment-id}/properties/{property-id}
        Method: GET
        """
        path = f"/comments/{comment_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_comment_property_by_id(
        self,
        comment_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property for comment by id

        Path: /comments/{comment-id}/properties/{property-id}
        Method: PUT
        """
        path = f"/comments/{comment_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_comment_property_by_id(
        self,
        comment_id: int,
        property_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property for comment by id

        Path: /comments/{comment-id}/properties/{property-id}
        Method: DELETE
        """
        path = f"/comments/{comment_id}/properties/{property_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_tasks(
        self,
        body_format: str | None = None,
        include_blank_tasks: bool | None = None,
        status: str | None = None,
        task_id: list[Any] | None = None,
        space_id: list[Any] | None = None,
        page_id: list[Any] | None = None,
        blogpost_id: list[Any] | None = None,
        created_by: list[Any] | None = None,
        assigned_to: list[Any] | None = None,
        completed_by: list[Any] | None = None,
        created_at_from: int | None = None,
        created_at_to: int | None = None,
        due_at_from: int | None = None,
        due_at_to: int | None = None,
        completed_at_from: int | None = None,
        completed_at_to: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get tasks

        Path: /tasks
        Method: GET
        """
        path = "/tasks"
        params = {
            "body-format": body_format,
            "include-blank-tasks": include_blank_tasks,
            "status": status,
            "task-id": task_id,
            "space-id": space_id,
            "page-id": page_id,
            "blogpost-id": blogpost_id,
            "created-by": created_by,
            "assigned-to": assigned_to,
            "completed-by": completed_by,
            "created-at-from": created_at_from,
            "created-at-to": created_at_to,
            "due-at-from": due_at_from,
            "due-at-to": due_at_to,
            "completed-at-from": completed_at_from,
            "completed-at-to": completed_at_to,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_task_by_id(
        self,
        id_: int,
        body_format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get task by id

        Path: /tasks/{id}
        Method: GET
        """
        path = f"/tasks/{id_}"
        params = {
            "body-format": body_format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_update_task(
        self,
        id_: int,
        body_format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update task

        Path: /tasks/{id}
        Method: PUT
        """
        path = f"/tasks/{id_}"
        params = {
            "body-format": body_format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_child_pages(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get child pages

        Path: /pages/{id}/children
        Method: GET
        """
        path = f"/pages/{id_}/children"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_child_custom_content(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get child custom content

        Path: /custom-content/{id}/children
        Method: GET
        """
        path = f"/custom-content/{id_}/children"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_direct_children(
        self,
        id_: int,
        cursor: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get direct children of a page

        Path: /pages/{id}/direct-children
        Method: GET
        """
        path = f"/pages/{id_}/direct-children"
        params = {
            "cursor": cursor,
            "limit": limit,
            "sort": sort,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_ancestors(
        self,
        id_: int,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all ancestors of page

        Path: /pages/{id}/ancestors
        Method: GET
        """
        path = f"/pages/{id_}/ancestors"
        params = {
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_descendants(
        self,
        id_: int,
        limit: int | None = None,
        depth: int | None = None,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get descendants of page

        Path: /pages/{id}/descendants
        Method: GET
        """
        path = f"/pages/{id_}/descendants"
        params = {
            "limit": limit,
            "depth": depth,
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_create_bulk_user_lookup(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create bulk user lookup using ids

        Path: /users-bulk
        Method: POST
        """
        path = "/users-bulk"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_check_access_by_email(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Check site access for a list of emails

        Path: /user/access/check-access-by-email
        Method: POST
        """
        path = "/user/access/check-access-by-email"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_invite_by_email(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Invite a list of emails to the site

        Path: /user/access/invite-by-email
        Method: POST
        """
        path = "/user/access/invite-by-email"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_data_policy_metadata(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get data policy metadata for the workspace

        Path: /data-policies/metadata
        Method: GET
        """
        path = "/data-policies/metadata"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_data_policy_spaces(
        self,
        ids: list[Any] | None = None,
        keys: list[Any] | None = None,
        sort: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get spaces with data policies

        Path: /data-policies/spaces
        Method: GET
        """
        path = "/data-policies/spaces"
        params = {
            "ids": ids,
            "keys": keys,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_classification_levels(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get list of classification levels

        Path: /classification-levels
        Method: GET
        """
        path = "/classification-levels"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_space_default_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space default classification level

        Path: /spaces/{id}/classification-level/default
        Method: GET
        """
        path = f"/spaces/{id_}/classification-level/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_put_space_default_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update space default classification level

        Path: /spaces/{id}/classification-level/default
        Method: PUT
        """
        path = f"/spaces/{id_}/classification-level/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_space_default_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete space default classification level

        Path: /spaces/{id}/classification-level/default
        Method: DELETE
        """
        path = f"/spaces/{id_}/classification-level/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_page_classification_level(
        self,
        id_: int,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get page classification level

        Path: /pages/{id}/classification-level
        Method: GET
        """
        path = f"/pages/{id_}/classification-level"
        params = {
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_put_page_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update page classification level

        Path: /pages/{id}/classification-level
        Method: PUT
        """
        path = f"/pages/{id_}/classification-level"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_post_page_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset page classification level

        Path: /pages/{id}/classification-level/reset
        Method: POST
        """
        path = f"/pages/{id_}/classification-level/reset"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_blog_post_classification_level(
        self,
        id_: int,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get blog post classification level

        Path: /blogposts/{id}/classification-level
        Method: GET
        """
        path = f"/blogposts/{id_}/classification-level"
        params = {
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_put_blog_post_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update blog post classification level

        Path: /blogposts/{id}/classification-level
        Method: PUT
        """
        path = f"/blogposts/{id_}/classification-level"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_post_blog_post_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset blog post classification level

        Path: /blogposts/{id}/classification-level/reset
        Method: POST
        """
        path = f"/blogposts/{id_}/classification-level/reset"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_whiteboard_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get whiteboard classification level

        Path: /whiteboards/{id}/classification-level
        Method: GET
        """
        path = f"/whiteboards/{id_}/classification-level"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_put_whiteboard_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update whiteboard classification level

        Path: /whiteboards/{id}/classification-level
        Method: PUT
        """
        path = f"/whiteboards/{id_}/classification-level"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_post_whiteboard_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset whiteboard classification level

        Path: /whiteboards/{id}/classification-level/reset
        Method: POST
        """
        path = f"/whiteboards/{id_}/classification-level/reset"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_database_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get database classification level

        Path: /databases/{id}/classification-level
        Method: GET
        """
        path = f"/databases/{id_}/classification-level"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_put_database_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update database classification level

        Path: /databases/{id}/classification-level
        Method: PUT
        """
        path = f"/databases/{id_}/classification-level"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_post_database_classification_level(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset database classification level

        Path: /databases/{id}/classification-level/reset
        Method: POST
        """
        path = f"/databases/{id_}/classification-level/reset"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_forge_app_properties(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get Forge app properties.

        Path: /app/properties
        Method: GET
        """
        path = "/app/properties"
        params = {
            "cursor": cursor,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_get_forge_app_property(
        self,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a Forge app property by key.

        Path: /app/properties/{propertyKey}
        Method: GET
        """
        path = f"/app/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_put_forge_app_property(
        self,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create or update a Forge app property.

        Path: /app/properties/{propertyKey}
        Method: PUT
        """
        path = f"/app/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_cloud_delete_forge_app_property(
        self,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Deletes a Forge app property.

        Path: /app/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/app/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )
