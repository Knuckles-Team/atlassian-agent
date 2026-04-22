# Generated MCP Tools for JiraCloud - core
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.jira_cloud_api import JiraCloudAPI
from ..auth import get_base_client


def get_api() -> JiraCloudAPI:
    return JiraCloudAPI(get_base_client())


def register_jira_core_tools(mcp: FastMCP):
    @mcp.tool(name="jira_cloud_get_banner", tags={"jira-cloud-core"})
    def jira_cloud_get_banner(_ctx: Context | None = None) -> dict[str, Any]:
        """Get announcement banner configuration"""
        api = get_api()
        response = api.jira_cloud_get_banner()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_banner", tags={"jira-cloud-core"})
    def jira_cloud_set_banner(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update announcement banner configuration"""
        api = get_api()
        response = api.jira_cloud_set_banner(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_application_property", tags={"jira-cloud-core"})
    def jira_cloud_get_application_property(
        key: str | None = Field(
            None, description="The key of the application property."
        ),
        permission_level: str | None = Field(
            None,
            description="The permission level of all items being returned in the list.",
        ),
        key_filter: str | None = Field(
            None,
            description="When a `key` isn't provided, this filters the list of results by the application property `key` using a regular expression. For example, using `jira.lf.*` will return all application properties with keys that start with *jira.lf.*.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get application property"""
        api = get_api()
        response = api.jira_cloud_get_application_property(
            key=key,
            permission_level=permission_level,
            key_filter=key_filter,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_advanced_settings", tags={"jira-cloud-core"})
    def jira_cloud_get_advanced_settings(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get advanced settings"""
        api = get_api()
        response = api.jira_cloud_get_advanced_settings()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_application_property", tags={"jira-cloud-core"})
    def jira_cloud_set_application_property(
        id_: str = Field(
            ..., description="The key of the application property to update."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set application property"""
        api = get_api()
        response = api.jira_cloud_set_application_property(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_audit_records", tags={"jira-cloud-core"})
    def jira_cloud_get_audit_records(
        offset: int | None = Field(
            None,
            description="The number of records to skip before returning the first result.",
        ),
        limit: int | None = Field(
            None, description="The maximum number of results to return."
        ),
        filter: str | None = Field(
            None,
            description="The strings to match with audit field content, space separated.",
        ),
        from_: str | None = Field(
            None,
            description="The date and time on or after which returned audit records must have been created. If `to` is provided `from` must be before `to` or no audit records are returned.",
        ),
        to: str | None = Field(
            None,
            description="The date and time on or before which returned audit results must have been created. If `from` is provided `to` must be after `from` or no audit records are returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get audit records"""
        api = get_api()
        response = api.jira_cloud_get_audit_records(
            offset=offset,
            limit=limit,
            filter=filter,
            from_=from_,
            to=to,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_system_avatars", tags={"jira-cloud-core"})
    def jira_cloud_get_all_system_avatars(
        type_: str = Field(..., description="The avatar type."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get system avatars by type"""
        api = get_api()
        response = api.jira_cloud_get_all_system_avatars(
            type_=type_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_configuration", tags={"jira-cloud-core"})
    def jira_cloud_get_configuration(_ctx: Context | None = None) -> dict[str, Any]:
        """Get global settings"""
        api = get_api()
        response = api.jira_cloud_get_configuration()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_shared_time_tracking_configuration",
        tags={"jira-cloud-core"},
    )
    def jira_cloud_get_shared_time_tracking_configuration(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get time tracking settings"""
        api = get_api()
        response = api.jira_cloud_get_shared_time_tracking_configuration()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_shared_time_tracking_configuration",
        tags={"jira-cloud-core"},
    )
    def jira_cloud_set_shared_time_tracking_configuration(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set time tracking settings"""
        api = get_api()
        response = api.jira_cloud_set_shared_time_tracking_configuration(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_avatars", tags={"jira-cloud-core"})
    def jira_cloud_get_avatars(
        type_: str = Field(..., description="The avatar type."),
        entity_id: str = Field(
            ..., description="The ID of the item the avatar is associated with."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get avatars"""
        api = get_api()
        response = api.jira_cloud_get_avatars(
            type_=type_,
            entity_id=entity_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_store_avatar", tags={"jira-cloud-core"})
    def jira_cloud_store_avatar(
        type_: str = Field(..., description="The avatar type."),
        entity_id: str = Field(
            ..., description="The ID of the item the avatar is associated with."
        ),
        size: int = Field(
            ..., description="The length of each side of the crop region."
        ),
        x: int | None = Field(
            None,
            description="The X coordinate of the top-left corner of the crop region.",
        ),
        y: int | None = Field(
            None,
            description="The Y coordinate of the top-left corner of the crop region.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Load avatar"""
        api = get_api()
        response = api.jira_cloud_store_avatar(
            type_=type_,
            entity_id=entity_id,
            x=x,
            y=y,
            size=size,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_avatar", tags={"jira-cloud-core"})
    def jira_cloud_delete_avatar(
        type_: str = Field(..., description="The avatar type."),
        owning_object_id: str = Field(
            ..., description="The ID of the item the avatar is associated with."
        ),
        id_: int = Field(..., description="The ID of the avatar."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete avatar"""
        api = get_api()
        response = api.jira_cloud_delete_avatar(
            type_=type_,
            owning_object_id=owning_object_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_avatar_image_by_id", tags={"jira-cloud-core"})
    def jira_cloud_get_avatar_image_by_id(
        type_: str = Field(..., description="The icon type of the avatar."),
        id_: int = Field(..., description="The ID of the avatar."),
        size: str | None = Field(
            None,
            description="The size of the avatar image. If not provided the default size is returned.",
        ),
        format: str | None = Field(
            None,
            description="The format to return the avatar image in. If not provided the original content format is returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get avatar image by ID"""
        api = get_api()
        response = api.jira_cloud_get_avatar_image_by_id(
            type_=type_,
            id_=id_,
            size=size,
            format=format,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_avatar_image_by_owner", tags={"jira-cloud-core"})
    def jira_cloud_get_avatar_image_by_owner(
        type_: str = Field(..., description="The icon type of the avatar."),
        entity_id: str = Field(
            ...,
            description="The ID of the project or issue type the avatar belongs to.",
        ),
        size: str | None = Field(
            None,
            description="The size of the avatar image. If not provided the default size is returned.",
        ),
        format: str | None = Field(
            None,
            description="The format to return the avatar image in. If not provided the original content format is returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get avatar image by owner"""
        api = get_api()
        response = api.jira_cloud_get_avatar_image_by_owner(
            type_=type_,
            entity_id=entity_id,
            size=size,
            format=format,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_forge_app_property_keys", tags={"jira-cloud-core"})
    def jira_cloud_get_forge_app_property_keys(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get app property keys (Forge)"""
        api = get_api()
        response = api.jira_cloud_get_forge_app_property_keys()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_forge_app_property", tags={"jira-cloud-core"})
    def jira_cloud_delete_forge_app_property(
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete app property (Forge)"""
        api = get_api()
        response = api.jira_cloud_delete_forge_app_property(
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_forge_app_property", tags={"jira-cloud-core"})
    def jira_cloud_get_forge_app_property(
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get app property (Forge)"""
        api = get_api()
        response = api.jira_cloud_get_forge_app_property(
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_put_forge_app_property", tags={"jira-cloud-core"})
    def jira_cloud_put_forge_app_property(
        property_key: str = Field(..., description="The key of the property."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set app property (Forge)"""
        api = get_api()
        response = api.jira_cloud_put_forge_app_property(
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()
