# Generated MCP Tools for APIAccessCloud
from typing import Any, Dict, Optional
from pydantic import Field
from fastmcp import FastMCP, Context
from ..api.api_access_cloud_api import APIAccessCloudAPI
from ..auth import get_base_client


def get_api() -> APIAccessCloudAPI:
    return APIAccessCloudAPI(get_base_client())


def register_api_access_cloud_tools(mcp: FastMCP):
    @mcp.tool(
        name="api_access_cloud_get_all_api_tokens_by_org_id",
        tags={"atlassian-api-access"},
    )
    def api_access_cloud_get_all_api_tokens_by_org_id(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and organization API key simultaneously.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all API tokens in an org"""
        api = get_api()
        response = api.api_access_cloud_get_all_api_tokens_by_org_id(
            org_id=org_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="api_access_cloud_bulk_revoke_api_tokens", tags={"atlassian-api-access"}
    )
    def api_access_cloud_bulk_revoke_api_tokens(
        org_id: str = Field(..., description="Id of organization revoking the token"),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Bulk revoke API tokens in an organization"""
        api = get_api()
        response = api.api_access_cloud_bulk_revoke_api_tokens(
            org_id=org_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="api_access_cloud_get_api_token_count_by_org_id",
        tags={"atlassian-api-access"},
    )
    def api_access_cloud_get_api_token_count_by_org_id(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and organization API key simultaneously.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get API token count in an org"""
        api = get_api()
        response = api.api_access_cloud_get_api_token_count_by_org_id(
            org_id=org_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="api_access_cloud_count_service_account_api_tokens",
        tags={"atlassian-api-access"},
    )
    def api_access_cloud_count_service_account_api_tokens(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and organization API key simultaneously.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get service account API token count in an org"""
        api = get_api()
        response = api.api_access_cloud_count_service_account_api_tokens(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="api_access_cloud_get_service_account_api_token",
        tags={"atlassian-api-access"},
    )
    def api_access_cloud_get_service_account_api_token(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and organization API key simultaneously.",
        ),
        account_id: str = Field(
            ...,
            description="ID for the service account whose API tokens you want to retrieve.",
        ),
        token_label: Optional[str] = Field(
            None, description="Optional filter to search for tokens by label."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all service account API tokens in an org"""
        api = get_api()
        response = api.api_access_cloud_get_service_account_api_token(
            org_id=org_id,
            account_id=account_id,
            token_label=token_label,
        )
        return response.model_dump()

    @mcp.tool(name="api_access_cloud_revoke_api_tokens", tags={"atlassian-api-access"})
    def api_access_cloud_revoke_api_tokens(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and organization API key simultaneously.",
        ),
        account_id: str = Field(
            ...,
            description="ID for the service account whose API tokens you want to revoke.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Revoke all API tokens for a service account"""
        api = get_api()
        response = api.api_access_cloud_revoke_api_tokens(
            org_id=org_id,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="api_access_cloud_get_api_key_count_by_org_id",
        tags={"atlassian-api-access"},
    )
    def api_access_cloud_get_api_key_count_by_org_id(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and organization API key simultaneously.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get API key count in an org"""
        api = get_api()
        response = api.api_access_cloud_get_api_key_count_by_org_id(
            org_id=org_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="api_access_cloud_get_all_api_keys_by_org_id",
        tags={"atlassian-api-access"},
    )
    def api_access_cloud_get_all_api_keys_by_org_id(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and organization API key simultaneously.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all API keys in an org"""
        api = get_api()
        response = api.api_access_cloud_get_all_api_keys_by_org_id(
            org_id=org_id,
        )
        return response.model_dump()

    @mcp.tool(name="api_access_cloud_revoke_api_key", tags={"atlassian-api-access"})
    def api_access_cloud_revoke_api_key(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and organization API key simultaneously.",
        ),
        api_key_id: str = Field(
            ..., description="ID for the API key you want to revoke."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Revoke an API key for an org"""
        api = get_api()
        response = api.api_access_cloud_revoke_api_key(
            org_id=org_id,
            api_key_id=api_key_id,
        )
        return response.model_dump()
