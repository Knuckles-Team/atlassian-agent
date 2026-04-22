# Generated MCP Tools for OrgCloud
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.org_cloud_api import OrgCloudAPI
from ..auth import get_base_client


def get_api() -> OrgCloudAPI:
    return OrgCloudAPI(get_base_client())


def register_org_cloud_tools(mcp: FastMCP):
    @mcp.tool(name="org_cloud_get_orgs", tags={"atlassian-org"})
    def org_cloud_get_orgs(
        cursor: str | None = Field(
            None,
            description="Sets the starting point for the page of results to return.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get organizations"""
        api = get_api()
        response = api.org_cloud_get_orgs(
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_org_by_id", tags={"atlassian-org"})
    def org_cloud_get_org_by_id(
        org_id: str = Field(..., description="Org Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get an organization by ID"""
        api = get_api()
        response = api.org_cloud_get_org_by_id(org_id=org_id)
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_directory_users", tags={"atlassian-org"})
    def org_cloud_get_directory_users(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get users in an organization"""
        api = get_api()
        response = api.org_cloud_get_directory_users(
            org_id=org_id, directory_id=directory_id
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_directory_user_details", tags={"atlassian-org"})
    def org_cloud_get_directory_user_details(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        user_id: str = Field(..., description="User Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get details of a user in a directory"""
        api = get_api()
        response = api.org_cloud_get_directory_user_details(
            org_id=org_id, directory_id=directory_id, user_id=user_id
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_users", tags={"atlassian-org"})
    def org_cloud_get_users(
        org_id: str = Field(..., description="Org Id"),
        cursor: str | None = Field(
            None,
            description="Sets the starting point for the page of results to return.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get managed accounts in an organization"""
        api = get_api()
        response = api.org_cloud_get_users(
            org_id=org_id,
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_post_v2_orgs_org_id_users_invite", tags={"atlassian-org"})
    def org_cloud_post_v2_orgs_org_id_users_invite(
        org_id: str = Field(..., description="Org Id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Invite users to an organization"""
        api = get_api()
        response = api.org_cloud_post_v2_orgs_org_id_users_invite(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_user_role_assignments", tags={"atlassian-org"})
    def org_cloud_get_user_role_assignments(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        account_id: str = Field(..., description="Account Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user role assignments"""
        api = get_api()
        response = api.org_cloud_get_user_role_assignments(
            org_id=org_id, directory_id=directory_id, account_id=account_id
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_assign_role", tags={"atlassian-org"})
    def org_cloud_assign_role(
        org_id: str = Field(..., description="Org Id"),
        user_id: str = Field(
            ...,
            description="The UserId on which the action(Role Assign) needs to happen. Use the [Search for users within an organization API](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v1-orgs-orgid-users-get) to get the userId.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Grant user access"""
        api = get_api()
        response = api.org_cloud_assign_role(
            org_id=org_id,
            user_id=user_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_revoke_role", tags={"atlassian-org"})
    def org_cloud_revoke_role(
        org_id: str = Field(..., description="Org Id"),
        user_id: str = Field(
            ...,
            description="The UserId on which the action(Role Revoke) needs to happen. Use the [Search for users within an organization API](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v1-orgs-orgid-users-get) to get the userId.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Revoke user access"""
        api = get_api()
        response = api.org_cloud_revoke_role(
            org_id=org_id,
            user_id=user_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        account_id: str = Field(
            ...,
            description="Every user has a unique ID. Find a user’s account ID by using the [Get users endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v2-orgs-orgid-directories-directoryid-users-get).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Suspend user access in directory"""
        api = get_api()
        response = api.org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend(
            org_id=org_id,
            directory_id=directory_id,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        account_id: str = Field(
            ...,
            description="Every user has a unique ID. Find a user’s account ID by using the [Get users endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v2-orgs-orgid-directories-directoryid-users-get).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Restore user access in directory"""
        api = get_api()
        response = api.org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore(
            org_id=org_id,
            directory_id=directory_id,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id",
        tags={"atlassian-org"},
    )
    def org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        account_id: str = Field(
            ...,
            description="Every user has a unique ID. Find a user’s account ID by using the [Get users endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v2-orgs-orgid-directories-directoryid-users-get).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove user from directory"""
        api = get_api()
        response = api.org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id(
            org_id=org_id,
            directory_id=directory_id,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        user_id: str = Field(
            ...,
            description="Every user has a unique ID. Find a user’s account ID by using the [Get users endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v2-orgs-orgid-directories-directoryid-users-get).",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign organization-level role"""
        api = get_api()
        response = (
            api.org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign(
                org_id=org_id,
                user_id=user_id,
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        user_id: str = Field(
            ...,
            description="Every user has a unique ID. Find a user's account ID by using the [Get users endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v2-orgs-orgid-directories-directoryid-users-get).",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove organization-level role"""
        api = get_api()
        response = (
            api.org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke(
                org_id=org_id,
                user_id=user_id,
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_directory_users_count", tags={"atlassian-org"})
    def org_cloud_get_directory_users_count(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get count of users in an organization"""
        api = get_api()
        response = api.org_cloud_get_directory_users_count(
            org_id=org_id, directory_id=directory_id
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_user_stats", tags={"atlassian-org"})
    def org_cloud_get_user_stats(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user stats in an organization"""
        api = get_api()
        response = api.org_cloud_get_user_stats(
            org_id=org_id, directory_id=directory_id
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates",
        tags={"atlassian-org"},
    )
    def org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates(
        org_id: str = Field(..., description="Organization ID"),
        account_id: str = Field(
            ...,
            description="Unique ID of the user's account. Use the [Jira User Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) to get the accountId (if Jira is available for your Organization). **Jira APIs use a different [authentication method ](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).** If you don’t have Jira, export a .csv of the user list. Learn how to [export users from a site](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/).",
        ),
        cursor: str | None = Field(None, description="Cursor to fetch the next page"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """User’s last active dates"""
        api = get_api()
        response = api.org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates(
            org_id=org_id,
            account_id=account_id,
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_search_users", tags={"atlassian-org"})
    def org_cloud_search_users(
        org_id: str = Field(..., description="Organization ID"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search for users in an organization"""
        api = get_api()
        response = api.org_cloud_search_users(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_post_v1_orgs_org_id_users_invite", tags={"atlassian-org"})
    def org_cloud_post_v1_orgs_org_id_users_invite(
        org_id: str = Field(..., description="Organization ID"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Invite user to org"""
        api = get_api()
        response = api.org_cloud_post_v1_orgs_org_id_users_invite(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access(
        org_id: str = Field(..., description="Organization ID"),
        account_id: str = Field(
            ...,
            description="Unique ID of the user's account that you are suspending. Use the [Jira User Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) to get the accountId (if Jira is available for your Organization). **Jira APIs use a different [authentication method ](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).** If you don’t have Jira, export a .csv of the user list. Learn how to [export users from a site](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Suspend user access"""
        api = get_api()
        response = (
            api.org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access(
                org_id=org_id,
                account_id=account_id,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access(
        org_id: str = Field(..., description="Organization ID"),
        account_id: str = Field(
            ...,
            description="Unique ID of the user's account that you are suspending. Use the [Jira User Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) to get the accountId (if Jira is available for your Organization). **Jira APIs use a different [authentication method ](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).** If you don’t have Jira, export a .csv of the user list. Learn how to [export users from a site](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Restore user access"""
        api = get_api()
        response = (
            api.org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access(
                org_id=org_id,
                account_id=account_id,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_delete_v1_orgs_org_id_directory_users_account_id",
        tags={"atlassian-org"},
    )
    def org_cloud_delete_v1_orgs_org_id_directory_users_account_id(
        org_id: str = Field(..., description="Organization ID"),
        account_id: str = Field(
            ...,
            description="Unique ID of the user's account that you are deleting. Use the [Jira User Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) to get the accountId (if Jira is available for your Organization). **Jira APIs use a different [authentication method ](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).** If you don’t have Jira, export a .csv of the user list. Learn how to [export users from a site](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove user access"""
        api = get_api()
        response = api.org_cloud_delete_v1_orgs_org_id_directory_users_account_id(
            org_id=org_id,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_groups", tags={"atlassian-org"})
    def org_cloud_get_groups(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get groups in an organization"""
        api = get_api()
        response = api.org_cloud_get_groups(org_id=org_id, directory_id=directory_id)
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v2_orgs_org_id_directories_directory_id_groups",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v2_orgs_org_id_directories_directory_id_groups(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create group"""
        api = get_api()
        response = api.org_cloud_post_v2_orgs_org_id_directories_directory_id_groups(
            org_id=org_id,
            directory_id=directory_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_group_role_assignments", tags={"atlassian-org"})
    def org_cloud_get_group_role_assignments(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        group_id: str = Field(..., description="Group Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group role assignments"""
        api = get_api()
        response = api.org_cloud_get_group_role_assignments(
            org_id=org_id, directory_id=directory_id, group_id=group_id
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        group_id: str = Field(
            ...,
            description="A group has a unique ID. Use the [Get groups endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-v2-orgs-orgid-directories-directoryid-groups-get) to find the group ID.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Grant access to group"""
        api = get_api()
        response = api.org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign(
            org_id=org_id,
            directory_id=directory_id,
            group_id=group_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        group_id: str = Field(
            ...,
            description="A group has a unique ID. Use the [Get groups endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-v2-orgs-orgid-directories-directoryid-groups-get) to find the group ID.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove access from group"""
        api = get_api()
        response = api.org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke(
            org_id=org_id,
            directory_id=directory_id,
            group_id=group_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        group_id: str = Field(
            ...,
            description="A group has a unique ID. Use the [Get groups endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-v2-orgs-orgid-directories-directoryid-groups-get) to find the group ID.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add user to group"""
        api = get_api()
        response = api.org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships(
            org_id=org_id,
            directory_id=directory_id,
            group_id=group_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id",
        tags={"atlassian-org"},
    )
    def org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        group_id: str = Field(
            ...,
            description="A group has a unique ID. Use the [Get groups endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-v2-orgs-orgid-directories-directoryid-groups-get) to find the group ID.",
        ),
        account_id: str = Field(
            ...,
            description="Every user has a unique ID. Find a user’s account ID by using the [Get users endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-users/#api-v2-orgs-orgid-directories-directoryid-users-get).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove user from group"""
        api = get_api()
        response = api.org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id(
            org_id=org_id,
            directory_id=directory_id,
            group_id=group_id,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id",
        tags={"atlassian-org"},
    )
    def org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id(
        org_id: str = Field(
            ...,
            description="Your organization has a unique ID. Find this ID in your Atlassian Administration URL or when you create your API key.",
        ),
        directory_id: str = Field(
            ...,
            description="A directory has a unique ID. Use the [Get directories endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-directory/#api-v2-orgs-orgid-directories-get) to find the directory ID.",
        ),
        group_id: str = Field(
            ...,
            description="A group has a unique ID. Use the [Get groups endpoint](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-v2-orgs-orgid-directories-directoryid-groups-get) to find the group ID.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete group"""
        api = get_api()
        response = api.org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id(
            org_id=org_id,
            directory_id=directory_id,
            group_id=group_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_group", tags={"atlassian-org"})
    def org_cloud_get_group(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        group_id: str = Field(..., description="Group Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group details"""
        api = get_api()
        response = api.org_cloud_get_group(
            org_id=org_id, directory_id=directory_id, group_id=group_id
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_groups_count", tags={"atlassian-org"})
    def org_cloud_get_groups_count(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the count of groups in an organization"""
        api = get_api()
        response = api.org_cloud_get_groups_count(
            org_id=org_id, directory_id=directory_id
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_groups_stats", tags={"atlassian-org"})
    def org_cloud_get_groups_stats(
        org_id: str = Field(..., description="Org Id"),
        directory_id: str = Field(..., description="Directory Id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group stats"""
        api = get_api()
        response = api.org_cloud_get_groups_stats(
            org_id=org_id, directory_id=directory_id
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_search_groups", tags={"atlassian-org"})
    def org_cloud_search_groups(
        org_id: str = Field(..., description="Organization ID"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search for groups within an organization"""
        api = get_api()
        response = api.org_cloud_search_groups(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v1_orgs_org_id_directory_groups", tags={"atlassian-org"}
    )
    def org_cloud_post_v1_orgs_org_id_directory_groups(
        org_id: str = Field(..., description="Organization ID"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create group"""
        api = get_api()
        response = api.org_cloud_post_v1_orgs_org_id_directory_groups(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_delete_v1_orgs_org_id_directory_groups_group_id",
        tags={"atlassian-org"},
    )
    def org_cloud_delete_v1_orgs_org_id_directory_groups_group_id(
        org_id: str = Field(..., description="Organization ID"),
        group_id: str = Field(
            ...,
            description="Unique ID that serves as reference to the group. Use the [Jira Group Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-groups-picker-get) to get the groupId (if Jira is available for your Organization). **Jira APIs use a different [authentication method ](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).** If you don’t have Jira, export a .csv of the user list. Make sure to select **pivot to column** when prompted. Learn how to [export users from a site](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/).",
        ),
        force_if_not_empty: bool | None = Field(
            None,
            description="Groups cannot be deleted if it contains users, unless `forceIfNotEmpty=true` is provided",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete group"""
        api = get_api()
        response = api.org_cloud_delete_v1_orgs_org_id_directory_groups_group_id(
            org_id=org_id,
            group_id=group_id,
            force_if_not_empty=force_if_not_empty,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_assign_role_to_group", tags={"atlassian-org"})
    def org_cloud_assign_role_to_group(
        org_id: str = Field(..., description="Organization ID"),
        group_id: str = Field(
            ...,
            description="Unique ID that serves as reference to the group. Use the [Search for groups within an organization API](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-v1-orgs-orgid-groups-search-post) to get the groupId.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign roles to a group"""
        api = get_api()
        response = api.org_cloud_assign_role_to_group(
            org_id=org_id,
            group_id=group_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_revoke_role_to_group", tags={"atlassian-org"})
    def org_cloud_revoke_role_to_group(
        org_id: str = Field(..., description="Organization ID"),
        group_id: str = Field(
            ...,
            description="Unique ID that serves as reference to the group. Use the [Search for groups within an organization API](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-v1-orgs-orgid-groups-search-post) to get the groupId.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Revoke roles from a group"""
        api = get_api()
        response = api.org_cloud_revoke_role_to_group(
            org_id=org_id,
            group_id=group_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships",
        tags={"atlassian-org"},
    )
    def org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships(
        org_id: str = Field(..., description="Organization ID"),
        group_id: str = Field(
            ...,
            description="Unique ID that serves as reference to the group. Use the [Jira Group Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-groups-picker-get) to get the groupId (if Jira is available for your Organization). **Jira APIs use a different [authentication method ](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).** If you don’t have Jira, export a .csv of the user list. Make sure to select **pivot to column** when prompted. Learn how to [export users from a site](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/).",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add user to group"""
        api = get_api()
        response = (
            api.org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships(
                org_id=org_id,
                group_id=group_id,
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id",
        tags={"atlassian-org"},
    )
    def org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id(
        org_id: str = Field(..., description="Organization ID"),
        group_id: str = Field(
            ...,
            description="Unique ID that serves as reference to the group. Use the [Jira Group Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-groups-picker-get) to get the groupId (if Jira is available for your Organization). **Jira APIs use a different [authentication method ](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).** If you don’t have Jira, export a .csv of the user list. Make sure to select **pivot to column** when prompted. Learn how to [export users from a site](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/).",
        ),
        account_id: str = Field(
            ...,
            description="Unique ID of the user's account that you are adding to the group. Use the [Jira User Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) to get the accountId (if Jira is available for your Organization). **Jira APIs use a different [authentication method ](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).** If you don’t have Jira, export a .csv of the user list. Learn how to [export users from a site](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove user from group"""
        api = get_api()
        response = api.org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id(
            org_id=org_id,
            group_id=group_id,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_directories_for_org", tags={"atlassian-org"})
    def org_cloud_get_directories_for_org(
        org_id: str = Field(..., description="Organization ID"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get directories in an organization"""
        api = get_api()
        response = api.org_cloud_get_directories_for_org(org_id=org_id)
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_domains", tags={"atlassian-org"})
    def org_cloud_get_domains(
        org_id: str = Field(..., description="Organization ID"),
        cursor: str | None = Field(
            None,
            description="Sets the starting point for the page of results to return.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get domains in an organization"""
        api = get_api()
        response = api.org_cloud_get_domains(
            org_id=org_id,
            cursor=cursor,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_domain_by_id", tags={"atlassian-org"})
    def org_cloud_get_domain_by_id(
        org_id: str = Field(..., description="Organization ID"),
        domain_id: str = Field(..., description="ID of the domain to return"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get domain by ID"""
        api = get_api()
        response = api.org_cloud_get_domain_by_id(
            org_id=org_id,
            domain_id=domain_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_events", tags={"atlassian-org"})
    def org_cloud_get_events(
        org_id: str = Field(..., description="Organization ID"),
        cursor: str | None = Field(
            None,
            description="Sets the starting point for the page of results to return",
        ),
        q: str | None = Field(
            None, description="Single query term for searching events."
        ),
        from_: str | None = Field(
            None,
            description="The earliest date and time of the event represented as a UNIX epoch time in milliseconds.",
        ),
        to: str | None = Field(
            None,
            description="The latest date and time of the event represented as a UNIX epoch time in milliseconds.",
        ),
        action: str | None = Field(
            None,
            description="A query filter that returns events of a specific action type.",
        ),
        actor: list[Any] | None = Field(
            None,
            description="A query filter that returns events by one or more specific actors.",
        ),
        ip: list[Any] | None = Field(
            None,
            description="A query filter that returns events by one or more specific ip addresses.",
        ),
        product: list[Any] | None = Field(
            None,
            description="A query filter that returns events by one or more specific products.",
        ),
        location: str | None = Field(
            None,
            description="A query filter that returns events by one or more specific locations. Of format: [ { 'city': '<CityName>', 'countryName': '<CountryName>' }, ... ]",
        ),
        limit: int | None = Field(
            None, description="The maximum number of events to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Query audit log events"""
        api = get_api()
        response = api.org_cloud_get_events(
            org_id=org_id,
            cursor=cursor,
            q=q,
            from_=from_,
            to=to,
            action=action,
            actor=actor,
            ip=ip,
            product=product,
            location=location,
            limit=limit,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_poll_events", tags={"atlassian-org"})
    def org_cloud_poll_events(
        org_id: str = Field(..., description="Organization ID"),
        cursor: str | None = Field(
            None,
            description="Sets the starting point for the page of results to return. Can be used when last page is reached to poll for new events. The sort order is maintained in the cursor across requests.",
        ),
        from_: str | None = Field(
            None,
            description="The earliest date and time of the event represented as a UNIX epoch time in milliseconds.",
        ),
        to: str | None = Field(
            None,
            description="The latest date and time of the event represented as a UNIX epoch time in milliseconds.",
        ),
        limit: int | None = Field(
            None, description="The maximum number of events to return per page."
        ),
        sort_order: str | None = Field(
            None,
            description="The order used to sort events by processing time. Defaults to ascending.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Poll audit log events"""
        api = get_api()
        response = api.org_cloud_poll_events(
            org_id=org_id,
            cursor=cursor,
            from_=from_,
            to=to,
            limit=limit,
            sort_order=sort_order,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_event_by_id", tags={"atlassian-org"})
    def org_cloud_get_event_by_id(
        org_id: str = Field(..., description="Organization ID"),
        event_id: str = Field(..., description="ID of the event to return"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get an event by ID"""
        api = get_api()
        response = api.org_cloud_get_event_by_id(
            org_id=org_id,
            event_id=event_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_event_actions", tags={"atlassian-org"})
    def org_cloud_get_event_actions(
        org_id: str = Field(..., description="Organization ID"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of event actions"""
        api = get_api()
        response = api.org_cloud_get_event_actions(org_id=org_id)
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_policies", tags={"atlassian-org"})
    def org_cloud_get_policies(
        org_id: str = Field(..., description="Organization ID"),
        cursor: str | None = Field(
            None,
            description="Sets the starting point for the page of results to return.",
        ),
        type_: str | None = Field(
            None, description="Sets the type for the page of policies to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of policies"""
        api = get_api()
        response = api.org_cloud_get_policies(
            org_id=org_id,
            cursor=cursor,
            type_=type_,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_create_policy", tags={"atlassian-org"})
    def org_cloud_create_policy(
        org_id: str = Field(..., description="Organization ID"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a policy"""
        api = get_api()
        response = api.org_cloud_create_policy(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_get_policy_by_id", tags={"atlassian-org"})
    def org_cloud_get_policy_by_id(
        org_id: str = Field(..., description="Organization ID"),
        policy_id: str = Field(..., description="ID of the policy to query"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a policy by ID"""
        api = get_api()
        response = api.org_cloud_get_policy_by_id(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_update_policy", tags={"atlassian-org"})
    def org_cloud_update_policy(
        org_id: str = Field(..., description="Organization ID"),
        policy_id: str = Field(..., description="ID of the policy to update"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a policy"""
        api = get_api()
        response = api.org_cloud_update_policy(
            org_id=org_id,
            policy_id=policy_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_delete_policy", tags={"atlassian-org"})
    def org_cloud_delete_policy(
        org_id: str = Field(..., description="Organization ID"),
        policy_id: str = Field(..., description="ID of the policy to delete"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a policy"""
        api = get_api()
        response = api.org_cloud_delete_policy(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_add_resource_to_policy", tags={"atlassian-org"})
    def org_cloud_add_resource_to_policy(
        org_id: str = Field(..., description="Organization ID"),
        policy_id: str = Field(..., description="ID of the policy to query"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add Resource to Policy"""
        api = get_api()
        response = api.org_cloud_add_resource_to_policy(
            org_id=org_id,
            policy_id=policy_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_update_policy_resource", tags={"atlassian-org"})
    def org_cloud_update_policy_resource(
        org_id: str = Field(..., description="Organization ID"),
        policy_id: str = Field(..., description="ID of the policy to query"),
        resource_id: str = Field(..., description="Resource ID"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update Policy Resource"""
        api = get_api()
        response = api.org_cloud_update_policy_resource(
            org_id=org_id,
            policy_id=policy_id,
            resource_id=resource_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_delete_policy_resource", tags={"atlassian-org"})
    def org_cloud_delete_policy_resource(
        org_id: str = Field(..., description="Organization ID"),
        policy_id: str = Field(..., description="ID of the policy to query"),
        resource_id: str = Field(..., description="Resource ID"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete Policy Resource"""
        api = get_api()
        response = api.org_cloud_delete_policy_resource(
            org_id=org_id,
            policy_id=policy_id,
            resource_id=resource_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_validate_policy", tags={"atlassian-org"})
    def org_cloud_validate_policy(
        org_id: str = Field(..., description="Organization ID"),
        policy_id: str = Field(..., description="Policy ID"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Validate Policy"""
        api = get_api()
        response = api.org_cloud_validate_policy(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="org_cloud_query_workspaces_v2", tags={"atlassian-org"})
    def org_cloud_query_workspaces_v2(
        org_id: str = Field(..., description="Organization ID"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of workspaces"""
        api = get_api()
        response = api.org_cloud_query_workspaces_v2(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()
