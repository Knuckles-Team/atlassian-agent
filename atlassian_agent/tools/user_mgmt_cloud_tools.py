# Generated MCP Tools for UserMgmtCloud
from typing import Any, Dict, List, Optional
from pydantic import Field
from fastmcp import FastMCP, Context
from ..api.user_mgmt_cloud_api import UserMgmtCloudAPI
from ..auth import get_base_client


def get_api() -> UserMgmtCloudAPI:
    return UserMgmtCloudAPI(get_base_client())


def register_user_mgmt_cloud_tools(mcp: FastMCP):
    @mcp.tool(
        name="user_mgmt_cloud_get_users_account_id_manage", tags={"atlassian-user-mgmt"}
    )
    def user_mgmt_cloud_get_users_account_id_manage(
        account_id: str = Field(..., description="The user account to manage"),
        privileges: Optional[List[Any]] = Field(
            None, description="Parameter privileges"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get user management permissions"""
        api = get_api()
        response = api.user_mgmt_cloud_get_users_account_id_manage(
            account_id=account_id,
            privileges=privileges,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_get_users_account_id_manage_profile",
        tags={"atlassian-user-mgmt"},
    )
    def user_mgmt_cloud_get_users_account_id_manage_profile(
        account_id: str = Field(..., description="The ID of the user"),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get profile"""
        api = get_api()
        response = api.user_mgmt_cloud_get_users_account_id_manage_profile(
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_patch_users_account_id_manage_profile",
        tags={"atlassian-user-mgmt"},
    )
    def user_mgmt_cloud_patch_users_account_id_manage_profile(
        account_id: str = Field(..., description="The ID of the user to update"),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update profile"""
        api = get_api()
        response = api.user_mgmt_cloud_patch_users_account_id_manage_profile(
            account_id=account_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_put_users_account_id_manage_email",
        tags={"atlassian-user-mgmt"},
    )
    def user_mgmt_cloud_put_users_account_id_manage_email(
        account_id: str = Field(..., description="The ID of the user"),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set email"""
        api = get_api()
        response = api.user_mgmt_cloud_put_users_account_id_manage_email(
            account_id=account_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_get_users_account_id_manage_api_tokens",
        tags={"atlassian-user-mgmt"},
    )
    def user_mgmt_cloud_get_users_account_id_manage_api_tokens(
        account_id: str = Field(..., description="The ID of the user"),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get API tokens"""
        api = get_api()
        response = api.user_mgmt_cloud_get_users_account_id_manage_api_tokens(
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id",
        tags={"atlassian-user-mgmt"},
    )
    def user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id(
        account_id: str = Field(..., description="The ID of the user"),
        token_id: str = Field(..., description="The ID of the API token"),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete API token"""
        api = get_api()
        response = (
            api.user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id(
                account_id=account_id,
                token_id=token_id,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable",
        tags={"atlassian"},
    )
    def user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable(
        account_id: str = Field(..., description="The ID of the user"),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Deactivate a user"""
        api = get_api()
        response = api.user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable(
            account_id=account_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable",
        tags={"atlassian"},
    )
    def user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable(
        account_id: str = Field(
            ..., description="The unique identifier of the user to activate."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Activate a user"""
        api = get_api()
        response = api.user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable(
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete",
        tags={"atlassian"},
    )
    def user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete(
        account_id: str = Field(
            ...,
            description="Unique ID of the user's account that you are deleting. Use the [Get users in an organization API](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-orgs-orgid-users-get) to get the accountId.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete account"""
        api = get_api()
        response = api.user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete(
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete",
        tags={"atlassian-user-mgmt"},
    )
    def user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete(
        account_id: str = Field(
            ...,
            description="Unique ID of the user's account that you are deleting. Use the [Get users in an organization API](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-orgs-orgid-users-get) to get the accountId.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Cancel delete account"""
        api = get_api()
        response = (
            api.user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete(
                account_id=account_id,
            )
        )
        return response.model_dump()
