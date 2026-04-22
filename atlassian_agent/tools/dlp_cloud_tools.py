# Generated MCP Tools for DLPCloud
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.dlp_cloud_api import DLPCloudAPI
from ..auth import get_base_client


def get_api() -> DLPCloudAPI:
    return DLPCloudAPI(get_base_client())


def register_dlp_cloud_tools(mcp: FastMCP):
    @mcp.tool(name="dlp_cloud_create_level", tags={"atlassian-dlp"})
    def dlp_cloud_create_level(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new classification level"""
        api = get_api()
        response = api.dlp_cloud_create_level(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="dlp_cloud_get_level_list", tags={"atlassian-dlp"})
    def dlp_cloud_get_level_list(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all classification levels by org_id"""
        api = get_api()
        response = api.dlp_cloud_get_level_list(
            org_id=org_id,
        )
        return response.model_dump()

    @mcp.tool(name="dlp_cloud_get_level", tags={"atlassian-dlp"})
    def dlp_cloud_get_level(
        level_id: str = Field(
            ...,
            description="Unique ID associated with the classification level obtained during its creation.",
        ),
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a classification level"""
        api = get_api()
        response = api.dlp_cloud_get_level(
            level_id=level_id,
            org_id=org_id,
        )
        return response.model_dump()

    @mcp.tool(name="dlp_cloud_edit_level", tags={"atlassian-dlp"})
    def dlp_cloud_edit_level(
        level_id: str = Field(
            ...,
            description="Unique ID associated with the classification level, obtained during its creation.",
        ),
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Edit a classification level"""
        api = get_api()
        response = api.dlp_cloud_edit_level(
            level_id=level_id,
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="dlp_cloud_publish_level", tags={"atlassian-dlp"})
    def dlp_cloud_publish_level(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Publish classification level(s)"""
        api = get_api()
        response = api.dlp_cloud_publish_level(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="dlp_cloud_archive_level", tags={"atlassian-dlp"})
    def dlp_cloud_archive_level(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Archive a data classification level"""
        api = get_api()
        response = api.dlp_cloud_archive_level(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="dlp_cloud_restore_level", tags={"atlassian-dlp"})
    def dlp_cloud_restore_level(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Restore a classification level"""
        api = get_api()
        response = api.dlp_cloud_restore_level(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="dlp_cloud_reorder", tags={"atlassian-dlp"})
    def dlp_cloud_reorder(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reorder classification levels"""
        api = get_api()
        response = api.dlp_cloud_reorder(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()
