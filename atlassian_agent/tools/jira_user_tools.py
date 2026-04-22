# Generated MCP Tools for JiraCloud - user
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.jira_cloud_api import JiraCloudAPI
from ..auth import get_base_client


def get_api() -> JiraCloudAPI:
    return JiraCloudAPI(get_base_client())


def register_jira_user_tools(mcp: FastMCP):
    @mcp.tool(
        name="jira_cloud_get_all_application_roles",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_get_all_application_roles(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all application roles"""
        api = get_api()
        response = api.jira_cloud_get_all_application_roles()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_application_role",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_get_application_role(
        key: str = Field(
            ...,
            description="The key of the application role. Use the [Get all application roles](#api-rest-api-3-applicationrole-get) operation to get the key for each application role.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get application role"""
        api = get_api()
        response = api.jira_cloud_get_application_role(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_user_data_classification_levels",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_get_all_user_data_classification_levels(
        status: list[Any] | None = Field(
            None, description="Optional set of statuses to filter by."
        ),
        order_by: str | None = Field(
            None,
            description="Ordering of the results by a given field. If not provided, values will not be sorted.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all classification levels"""
        api = get_api()
        response = api.jira_cloud_get_all_user_data_classification_levels(
            status=status,
            order_by=order_by,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_share_permissions", tags={"jira-cloud-user"})
    def jira_cloud_get_share_permissions(
        id_: int = Field(..., description="The ID of the filter."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get share permissions"""
        api = get_api()
        response = api.jira_cloud_get_share_permissions(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_share_permission", tags={"jira-cloud-user"})
    def jira_cloud_add_share_permission(
        id_: int = Field(..., description="The ID of the filter."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add share permission"""
        api = get_api()
        response = api.jira_cloud_add_share_permission(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_share_permission", tags={"jira-cloud-user"})
    def jira_cloud_delete_share_permission(
        id_: int = Field(..., description="The ID of the filter."),
        permission_id: int = Field(..., description="The ID of the share permission."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete share permission"""
        api = get_api()
        response = api.jira_cloud_delete_share_permission(
            id_=id_,
            permission_id=permission_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_share_permission", tags={"jira-cloud-user"})
    def jira_cloud_get_share_permission(
        id_: int = Field(..., description="The ID of the filter."),
        permission_id: int = Field(..., description="The ID of the share permission."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get share permission"""
        api = get_api()
        response = api.jira_cloud_get_share_permission(
            id_=id_,
            permission_id=permission_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_group", tags={"jira-cloud-user"})
    def jira_cloud_remove_group(
        groupname: str | None = Field(None, description="Parameter groupname"),
        group_id: str | None = Field(
            None,
            description="The ID of the group. This parameter cannot be used with the `groupname` parameter.",
        ),
        swap_group: str | None = Field(
            None,
            description="As a group's name can change, use of `swapGroupId` is recommended to identify a group.   The group to transfer restrictions to. Only comments and worklogs are transferred. If restrictions are not transferred, comments and worklogs are inaccessible after the deletion. This parameter cannot be used with the `swapGroupId` parameter.",
        ),
        swap_group_id: str | None = Field(
            None,
            description="The ID of the group to transfer restrictions to. Only comments and worklogs are transferred. If restrictions are not transferred, comments and worklogs are inaccessible after the deletion. This parameter cannot be used with the `swapGroup` parameter.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove group"""
        api = get_api()
        response = api.jira_cloud_remove_group(
            groupname=groupname,
            group_id=group_id,
            swap_group=swap_group,
            swap_group_id=swap_group_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_group", tags={"jira-cloud-user"})
    def jira_cloud_get_group(
        groupname: str | None = Field(
            None,
            description="As a group's name can change, use of `groupId` is recommended to identify a group.   The name of the group. This parameter cannot be used with the `groupId` parameter.",
        ),
        group_id: str | None = Field(
            None,
            description="The ID of the group. This parameter cannot be used with the `groupName` parameter.",
        ),
        expand: str | None = Field(None, description="List of fields to expand."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group"""
        api = get_api()
        response = api.jira_cloud_get_group(
            groupname=groupname,
            group_id=group_id,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_group", tags={"jira-cloud-user"})
    def jira_cloud_create_group(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create group"""
        api = get_api()
        response = api.jira_cloud_create_group(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_users_from_group", tags={"jira-cloud-user"})
    def jira_cloud_get_users_from_group(
        groupname: str | None = Field(
            None,
            description="As a group's name can change, use of `groupId` is recommended to identify a group.   The name of the group. This parameter cannot be used with the `groupId` parameter.",
        ),
        group_id: str | None = Field(
            None,
            description="The ID of the group. This parameter cannot be used with the `groupName` parameter.",
        ),
        include_inactive_users: bool | None = Field(
            None, description="Include inactive users."
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of items to return per page (number should be between 1 and 50).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get users from group"""
        api = get_api()
        response = api.jira_cloud_get_users_from_group(
            groupname=groupname,
            group_id=group_id,
            include_inactive_users=include_inactive_users,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_user_from_group", tags={"jira-cloud-user"})
    def jira_cloud_remove_user_from_group(
        account_id: str = Field(
            ...,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        groupname: str | None = Field(
            None,
            description="As a group's name can change, use of `groupId` is recommended to identify a group.   The name of the group. This parameter cannot be used with the `groupId` parameter.",
        ),
        group_id: str | None = Field(
            None,
            description="The ID of the group. This parameter cannot be used with the `groupName` parameter.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove user from group"""
        api = get_api()
        response = api.jira_cloud_remove_user_from_group(
            groupname=groupname,
            group_id=group_id,
            username=username,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_user_to_group", tags={"jira-cloud-user"})
    def jira_cloud_add_user_to_group(
        groupname: str | None = Field(
            None,
            description="As a group's name can change, use of `groupId` is recommended to identify a group.   The name of the group. This parameter cannot be used with the `groupId` parameter.",
        ),
        group_id: str | None = Field(
            None,
            description="The ID of the group. This parameter cannot be used with the `groupName` parameter.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add user to group"""
        api = get_api()
        response = api.jira_cloud_add_user_to_group(
            groupname=groupname,
            group_id=group_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_find_groups", tags={"jira-cloud-user"})
    def jira_cloud_find_groups(
        account_id: str | None = Field(
            None,
            description="This parameter is deprecated, setting it does not affect the results. To find groups containing a particular user, use [Get user groups](#api-rest-api-3-user-groups-get).",
        ),
        query: str | None = Field(
            None, description="The string to find in group names."
        ),
        exclude: list[Any] | None = Field(
            None,
            description="As a group's name can change, use of `excludeGroupIds` is recommended to identify a group.   A group to exclude from the result. To exclude multiple groups, provide an ampersand-separated list. For example, `exclude=group1&exclude=group2`. This parameter cannot be used with the `excludeGroupIds` parameter.",
        ),
        exclude_id: list[Any] | None = Field(
            None,
            description="A group ID to exclude from the result. To exclude multiple groups, provide an ampersand-separated list. For example, `excludeId=group1-id&excludeId=group2-id`. This parameter cannot be used with the `excludeGroups` parameter.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of groups to return. The maximum number of groups that can be returned is limited by the system property `jira.ajax.autocomplete.limit`.",
        ),
        case_insensitive: bool | None = Field(
            None,
            description="Whether the search for groups should be case insensitive.",
        ),
        user_name: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find groups"""
        api = get_api()
        response = api.jira_cloud_find_groups(
            account_id=account_id,
            query=query,
            exclude=exclude,
            exclude_id=exclude_id,
            max_results=max_results,
            case_insensitive=case_insensitive,
            user_name=user_name,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_find_users_and_groups", tags={"jira-cloud-user"})
    def jira_cloud_find_users_and_groups(
        query: str = Field(..., description="The search string."),
        max_results: int | None = Field(
            None, description="The maximum number of items to return in each list."
        ),
        show_avatar: bool | None = Field(
            None,
            description="Whether the user avatar should be returned. If an invalid value is provided, the default value is used.",
        ),
        field_id: str | None = Field(
            None, description="The custom field ID of the field this request is for."
        ),
        project_id: list[Any] | None = Field(
            None,
            description="The ID of a project that returned users and groups must have permission to view. To include multiple projects, provide an ampersand-separated list. For example, `projectId=10000&projectId=10001`. This parameter is only used when `fieldId` is present.",
        ),
        issue_type_id: list[Any] | None = Field(
            None,
            description="The ID of an issue type that returned users and groups must have permission to view. To include multiple issue types, provide an ampersand-separated list. For example, `issueTypeId=10000&issueTypeId=10001`. Special values, such as `-1` (all standard issue types) and `-2` (all subtask issue types), are supported. This parameter is only used when `fieldId` is present.",
        ),
        avatar_size: str | None = Field(
            None,
            description="The size of the avatar to return. If an invalid value is provided, the default value is used.",
        ),
        case_insensitive: bool | None = Field(
            None,
            description="Whether the search for groups should be case insensitive.",
        ),
        exclude_connect_addons: bool | None = Field(
            None,
            description="Whether Connect app users and groups should be excluded from the search results. If an invalid value is provided, the default value is used.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users and groups"""
        api = get_api()
        response = api.jira_cloud_find_users_and_groups(
            query=query,
            max_results=max_results,
            show_avatar=show_avatar,
            field_id=field_id,
            project_id=project_id,
            issue_type_id=issue_type_id,
            avatar_size=avatar_size,
            case_insensitive=case_insensitive,
            exclude_connect_addons=exclude_connect_addons,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_my_permissions", tags={"jira-cloud-user"})
    def jira_cloud_get_my_permissions(
        project_key: str | None = Field(
            None, description="The key of project. Ignored if `projectId` is provided."
        ),
        project_id: str | None = Field(None, description="The ID of project."),
        issue_key: str | None = Field(
            None, description="The key of the issue. Ignored if `issueId` is provided."
        ),
        issue_id: str | None = Field(None, description="The ID of the issue."),
        permissions: str | None = Field(
            None,
            description="A list of permission keys. (Required) This parameter accepts a comma-separated list. To get the list of available permissions, use [Get all permissions](#api-rest-api-3-permissions-get).",
        ),
        project_uuid: str | None = Field(None, description="Parameter projectUuid"),
        project_configuration_uuid: str | None = Field(
            None, description="Parameter projectConfigurationUuid"
        ),
        comment_id: str | None = Field(None, description="The ID of the comment."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get my permissions"""
        api = get_api()
        response = api.jira_cloud_get_my_permissions(
            project_key=project_key,
            project_id=project_id,
            issue_key=issue_key,
            issue_id=issue_id,
            permissions=permissions,
            project_uuid=project_uuid,
            project_configuration_uuid=project_configuration_uuid,
            comment_id=comment_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_current_user", tags={"jira-cloud-user"})
    def jira_cloud_get_current_user(
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about user in the response. This parameter accepts a comma-separated list. Expand options include:   *  `groups` Returns all groups, including nested groups, the user belongs to.  *  `applicationRoles` Returns the application roles the user is assigned to.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get current user"""
        api = get_api()
        response = api.jira_cloud_get_current_user(
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_permissions", tags={"jira-cloud-user"})
    def jira_cloud_get_all_permissions(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all permissions"""
        api = get_api()
        response = api.jira_cloud_get_all_permissions()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_permission_schemes",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_get_all_permission_schemes(
        expand: str | None = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:   *  `all` Returns all expandable information.  *  `field` Returns information about the custom field granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `permissions` Returns all permission grants for each permission scheme.  *  `projectRole` Returns information about the project role granted the permission.  *  `user` Returns information about the user who is granted the permission.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all permission schemes"""
        api = get_api()
        response = api.jira_cloud_get_all_permission_schemes(
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_permission_scheme", tags={"jira-cloud-user"})
    def jira_cloud_create_permission_scheme(
        expand: str | None = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  `all` Returns all expandable information.  *  `field` Returns information about the custom field granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `permissions` Returns all permission grants for each permission scheme.  *  `projectRole` Returns information about the project role granted the permission.  *  `user` Returns information about the user who is granted the permission.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create permission scheme"""
        api = get_api()
        response = api.jira_cloud_create_permission_scheme(
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_permission_scheme", tags={"jira-cloud-user"})
    def jira_cloud_delete_permission_scheme(
        scheme_id: int = Field(
            ..., description="The ID of the permission scheme being deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete permission scheme"""
        api = get_api()
        response = api.jira_cloud_delete_permission_scheme(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_permission_scheme", tags={"jira-cloud-user"})
    def jira_cloud_get_permission_scheme(
        scheme_id: int = Field(
            ..., description="The ID of the permission scheme to return."
        ),
        expand: str | None = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:   *  `all` Returns all expandable information.  *  `field` Returns information about the custom field granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `permissions` Returns all permission grants for each permission scheme.  *  `projectRole` Returns information about the project role granted the permission.  *  `user` Returns information about the user who is granted the permission.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permission scheme"""
        api = get_api()
        response = api.jira_cloud_get_permission_scheme(
            scheme_id=scheme_id,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_permission_scheme", tags={"jira-cloud-user"})
    def jira_cloud_update_permission_scheme(
        scheme_id: int = Field(
            ..., description="The ID of the permission scheme to update."
        ),
        expand: str | None = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  `all` Returns all expandable information.  *  `field` Returns information about the custom field granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `permissions` Returns all permission grants for each permission scheme.  *  `projectRole` Returns information about the project role granted the permission.  *  `user` Returns information about the user who is granted the permission.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update permission scheme"""
        api = get_api()
        response = api.jira_cloud_update_permission_scheme(
            scheme_id=scheme_id,
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_permission_scheme_grants",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_get_permission_scheme_grants(
        scheme_id: int = Field(..., description="The ID of the permission scheme."),
        expand: str | None = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  `permissions` Returns all permission grants for each permission scheme.  *  `user` Returns information about the user who is granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `projectRole` Returns information about the project role granted the permission.  *  `field` Returns information about the custom field granted the permission.  *  `all` Returns all expandable information.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permission scheme grants"""
        api = get_api()
        response = api.jira_cloud_get_permission_scheme_grants(
            scheme_id=scheme_id,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_permission_grant", tags={"jira-cloud-user"})
    def jira_cloud_create_permission_grant(
        scheme_id: int = Field(
            ...,
            description="The ID of the permission scheme in which to create a new permission grant.",
        ),
        expand: str | None = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  `permissions` Returns all permission grants for each permission scheme.  *  `user` Returns information about the user who is granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `projectRole` Returns information about the project role granted the permission.  *  `field` Returns information about the custom field granted the permission.  *  `all` Returns all expandable information.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create permission grant"""
        api = get_api()
        response = api.jira_cloud_create_permission_grant(
            scheme_id=scheme_id,
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_permission_scheme_entity",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_delete_permission_scheme_entity(
        scheme_id: int = Field(
            ...,
            description="The ID of the permission scheme to delete the permission grant from.",
        ),
        permission_id: int = Field(
            ..., description="The ID of the permission grant to delete."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete permission scheme grant"""
        api = get_api()
        response = api.jira_cloud_delete_permission_scheme_entity(
            scheme_id=scheme_id,
            permission_id=permission_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_permission_scheme_grant",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_get_permission_scheme_grant(
        scheme_id: int = Field(..., description="The ID of the permission scheme."),
        permission_id: int = Field(..., description="The ID of the permission grant."),
        expand: str | None = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  `all` Returns all expandable information.  *  `field` Returns information about the custom field granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `permissions` Returns all permission grants for each permission scheme.  *  `projectRole` Returns information about the project role granted the permission.  *  `user` Returns information about the user who is granted the permission.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permission scheme grant"""
        api = get_api()
        response = api.jira_cloud_get_permission_scheme_grant(
            scheme_id=scheme_id,
            permission_id=permission_id,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_actor_users", tags={"jira-cloud-user"})
    def jira_cloud_add_actor_users(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add actors to project role"""
        api = get_api()
        response = api.jira_cloud_add_actor_users(
            project_id_or_key=project_id_or_key,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_assigned_permission_scheme",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_get_assigned_permission_scheme(
        project_key_or_id: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:   *  `all` Returns all expandable information.  *  `field` Returns information about the custom field granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `permissions` Returns all permission grants for each permission scheme.  *  `projectRole` Returns information about the project role granted the permission.  *  `user` Returns information about the user who is granted the permission.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get assigned permission scheme"""
        api = get_api()
        response = api.jira_cloud_get_assigned_permission_scheme(
            project_key_or_id=project_key_or_id,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_assign_permission_scheme", tags={"jira-cloud-user"})
    def jira_cloud_assign_permission_scheme(
        project_key_or_id: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:   *  `all` Returns all expandable information.  *  `field` Returns information about the custom field granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `permissions` Returns all permission grants for each permission scheme.  *  `projectRole` Returns information about the project role granted the permission.  *  `user` Returns information about the user who is granted the permission.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign permission scheme"""
        api = get_api()
        response = api.jira_cloud_assign_permission_scheme(
            project_key_or_id=project_key_or_id,
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_user", tags={"jira-cloud-user"})
    def jira_cloud_remove_user(
        account_id: str = Field(
            ...,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        key: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete user"""
        api = get_api()
        response = api.jira_cloud_remove_user(
            account_id=account_id,
            username=username,
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_user", tags={"jira-cloud-user"})
    def jira_cloud_get_user(
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide) for details.",
        ),
        key: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide) for details.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about users in the response. This parameter accepts a comma-separated list. Expand options include:   *  `groups` includes all groups and nested groups to which the user belongs.  *  `applicationRoles` includes details of all the applications to which the user has access.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user"""
        api = get_api()
        response = api.jira_cloud_get_user(
            account_id=account_id,
            username=username,
            key=key,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_user", tags={"jira-cloud-user"})
    def jira_cloud_create_user(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create user"""
        api = get_api()
        response = api.jira_cloud_create_user(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_find_assignable_users", tags={"jira-cloud-user"})
    def jira_cloud_find_assignable_users(
        query: str | None = Field(
            None,
            description="A query string that is matched against user attributes, such as `displayName`, and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `username` or `accountId` is specified.",
        ),
        session_id: str | None = Field(
            None,
            description="The sessionId of this request. SessionId is the same until the assignee is set.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        account_id: str | None = Field(
            None,
            description="A query string that is matched exactly against user `accountId`. Required, unless `query` is specified.",
        ),
        project: str | None = Field(
            None,
            description="The project ID or project key (case sensitive). Required, unless `issueKey` or `issueId` is specified.",
        ),
        issue_key: str | None = Field(
            None,
            description="The key of the issue. Required, unless `issueId` or `project` is specified.",
        ),
        issue_id: str | None = Field(
            None,
            description="The ID of the issue. Required, unless `issueKey` or `project` is specified.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of items to return. This operation may return less than the maximum number of items even if more are available. The operation fetches users up to the maximum and then, from the fetched users, returns only the users that can be assigned to the issue.",
        ),
        action_descriptor_id: int | None = Field(
            None, description="The ID of the transition."
        ),
        recommend: bool | None = Field(None, description="Parameter recommend"),
        account_type: list[Any] | None = Field(
            None, description="Parameter accountType"
        ),
        app_type: list[Any] | None = Field(None, description="Parameter appType"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users assignable to issues"""
        api = get_api()
        response = api.jira_cloud_find_assignable_users(
            query=query,
            session_id=session_id,
            username=username,
            account_id=account_id,
            project=project,
            issue_key=issue_key,
            issue_id=issue_id,
            start_at=start_at,
            max_results=max_results,
            action_descriptor_id=action_descriptor_id,
            recommend=recommend,
            account_type=account_type,
            app_type=app_type,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_reset_user_columns", tags={"jira-cloud-user"})
    def jira_cloud_reset_user_columns(
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset user default columns"""
        api = get_api()
        response = api.jira_cloud_reset_user_columns(
            account_id=account_id,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_user_default_columns", tags={"jira-cloud-user"})
    def jira_cloud_get_user_default_columns(
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user default columns"""
        api = get_api()
        response = api.jira_cloud_get_user_default_columns(
            account_id=account_id,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_user_columns", tags={"jira-cloud-user"})
    def jira_cloud_set_user_columns(
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set user default columns"""
        api = get_api()
        response = api.jira_cloud_set_user_columns(
            account_id=account_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_user_email", tags={"jira-cloud-user"})
    def jira_cloud_get_user_email(
        account_id: str = Field(
            ...,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, `5b10ac8d82e05b22cc7d4ef5`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user email"""
        api = get_api()
        response = api.jira_cloud_get_user_email(
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_user_groups", tags={"jira-cloud-user"})
    def jira_cloud_get_user_groups(
        account_id: str = Field(
            ...,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        key: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user groups"""
        api = get_api()
        response = api.jira_cloud_get_user_groups(
            account_id=account_id,
            username=username,
            key=key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_find_users_with_all_permissions",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_find_users_with_all_permissions(
        permissions: str = Field(
            ...,
            description="A comma separated list of permissions. Permissions can be specified as any:   *  permission returned by [Get all permissions](#api-rest-api-3-permissions-get).  *  custom project permission added by Connect apps.  *  (deprecated) one of the following:           *  ASSIGNABLE\\_USER      *  ASSIGN\\_ISSUE      *  ATTACHMENT\\_DELETE\\_ALL      *  ATTACHMENT\\_DELETE\\_OWN      *  BROWSE      *  CLOSE\\_ISSUE      *  COMMENT\\_DELETE\\_ALL      *  COMMENT\\_DELETE\\_OWN      *  COMMENT\\_EDIT\\_ALL      *  COMMENT\\_EDIT\\_OWN      *  COMMENT\\_ISSUE      *  CREATE\\_ATTACHMENT      *  CREATE\\_ISSUE      *  DELETE\\_ISSUE      *  EDIT\\_ISSUE      *  LINK\\_ISSUE      *  MANAGE\\_WATCHER\\_LIST      *  MODIFY\\_REPORTER      *  MOVE\\_ISSUE      *  PROJECT\\_ADMIN      *  RESOLVE\\_ISSUE      *  SCHEDULE\\_ISSUE      *  SET\\_ISSUE\\_SECURITY      *  TRANSITION\\_ISSUE      *  VIEW\\_VERSION\\_CONTROL      *  VIEW\\_VOTERS\\_AND\\_WATCHERS      *  VIEW\\_WORKFLOW\\_READONLY      *  WORKLOG\\_DELETE\\_ALL      *  WORKLOG\\_DELETE\\_OWN      *  WORKLOG\\_EDIT\\_ALL      *  WORKLOG\\_EDIT\\_OWN      *  WORK\\_ISSUE",
        ),
        query: str | None = Field(
            None,
            description="A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        account_id: str | None = Field(
            None,
            description="A query string that is matched exactly against user `accountId`. Required, unless `query` is specified.",
        ),
        issue_key: str | None = Field(None, description="The issue key for the issue."),
        project_key: str | None = Field(
            None, description="The project key for the project (case sensitive)."
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users with permissions"""
        api = get_api()
        response = api.jira_cloud_find_users_with_all_permissions(
            query=query,
            username=username,
            account_id=account_id,
            permissions=permissions,
            issue_key=issue_key,
            project_key=project_key,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_find_users_for_picker", tags={"jira-cloud-user"})
    def jira_cloud_find_users_for_picker(
        query: str = Field(
            ...,
            description="A query string that is matched against user attributes, such as `displayName`, and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of items to return. The total number of matched users is returned in `total`.",
        ),
        show_avatar: bool | None = Field(
            None, description="Include the URI to the user's avatar."
        ),
        exclude: list[Any] | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        exclude_account_ids: list[Any] | None = Field(
            None,
            description="A list of account IDs to exclude from the search results. This parameter accepts a comma-separated list. Multiple account IDs can also be provided using an ampersand-separated list. For example, `excludeAccountIds=5b10a2844c20165700ede21g,5b10a0effa615349cb016cd8&excludeAccountIds=5b10ac8d82e05b22cc7d4ef5`. Cannot be provided with `exclude`.",
        ),
        avatar_size: str | None = Field(None, description="Parameter avatarSize"),
        exclude_connect_users: bool | None = Field(
            None, description="Parameter excludeConnectUsers"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users for picker"""
        api = get_api()
        response = api.jira_cloud_find_users_for_picker(
            query=query,
            max_results=max_results,
            show_avatar=show_avatar,
            exclude=exclude,
            exclude_account_ids=exclude_account_ids,
            avatar_size=avatar_size,
            exclude_connect_users=exclude_connect_users,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_user_property_keys", tags={"jira-cloud-user"})
    def jira_cloud_get_user_property_keys(
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        user_key: str | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user property keys"""
        api = get_api()
        response = api.jira_cloud_get_user_property_keys(
            account_id=account_id,
            user_key=user_key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_user_property", tags={"jira-cloud-user"})
    def jira_cloud_delete_user_property(
        property_key: str = Field(..., description="The key of the user's property."),
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        user_key: str | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete user property"""
        api = get_api()
        response = api.jira_cloud_delete_user_property(
            account_id=account_id,
            user_key=user_key,
            username=username,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_user_property", tags={"jira-cloud-user"})
    def jira_cloud_get_user_property(
        property_key: str = Field(..., description="The key of the user's property."),
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        user_key: str | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user property"""
        api = get_api()
        response = api.jira_cloud_get_user_property(
            account_id=account_id,
            user_key=user_key,
            username=username,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_user_property", tags={"jira-cloud-user"})
    def jira_cloud_set_user_property(
        property_key: str = Field(
            ...,
            description="The key of the user's property. The maximum length is 255 characters.",
        ),
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
        user_key: str | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set user property"""
        api = get_api()
        response = api.jira_cloud_set_user_property(
            account_id=account_id,
            user_key=user_key,
            username=username,
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_find_users", tags={"jira-cloud-user"})
    def jira_cloud_find_users(
        query: str | None = Field(
            None,
            description="A query string that is matched against user attributes ( `displayName`, and `emailAddress`) to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` or `property` is specified.",
        ),
        username: str | None = Field(None, description="Parameter username"),
        account_id: str | None = Field(
            None,
            description="A query string that is matched exactly against a user `accountId`. Required, unless `query` or `property` is specified.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of filtered results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        property: str | None = Field(
            None,
            description="A query string used to search properties. Property keys are specified by path, so property keys containing dot (.) or equals (=) characters cannot be used. The query string cannot be specified using a JSON object. Example: To search for the value of `nested` from `{'something':{'nested':1,'other':2}}` use `thepropertykey.something.nested=1`. Required, unless `accountId` or `query` is specified.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users"""
        api = get_api()
        response = api.jira_cloud_find_users(
            query=query,
            username=username,
            account_id=account_id,
            start_at=start_at,
            max_results=max_results,
            property=property,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_find_users_by_query", tags={"jira-cloud-user"})
    def jira_cloud_find_users_by_query(
        query: str = Field(..., description="The search query."),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users by query"""
        api = get_api()
        response = api.jira_cloud_find_users_by_query(
            query=query,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_find_user_keys_by_query", tags={"jira-cloud-user"})
    def jira_cloud_find_user_keys_by_query(
        query: str = Field(..., description="The search query."),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_result: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find user keys by query"""
        api = get_api()
        response = api.jira_cloud_find_user_keys_by_query(
            query=query,
            start_at=start_at,
            max_result=max_result,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_find_users_with_browse_permission",
        tags={"jira-cloud-user"},
    )
    def jira_cloud_find_users_with_browse_permission(
        query: str | None = Field(
            None,
            description="A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified.",
        ),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        account_id: str | None = Field(
            None,
            description="A query string that is matched exactly against user `accountId`. Required, unless `query` is specified.",
        ),
        issue_key: str | None = Field(
            None,
            description="The issue key for the issue. Required, unless `projectKey` is specified.",
        ),
        project_key: str | None = Field(
            None,
            description="The project key for the project (case sensitive). Required, unless `issueKey` is specified.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users with browse permission"""
        api = get_api()
        response = api.jira_cloud_find_users_with_browse_permission(
            query=query,
            username=username,
            account_id=account_id,
            issue_key=issue_key,
            project_key=project_key,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_users_default", tags={"jira-cloud-user"})
    def jira_cloud_get_all_users_default(
        start_at: int | None = Field(
            None, description="The index of the first item to return."
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return (limited to 1000)."
        ),
        expand: str | None = Field(None, description="Parameter expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all users default"""
        api = get_api()
        response = api.jira_cloud_get_all_users_default(
            start_at=start_at,
            max_results=max_results,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_users", tags={"jira-cloud-user"})
    def jira_cloud_get_all_users(
        start_at: int | None = Field(
            None, description="The index of the first item to return."
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return (limited to 1000)."
        ),
        expand: str | None = Field(None, description="Parameter expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all users"""
        api = get_api()
        response = api.jira_cloud_get_all_users(
            start_at=start_at,
            max_results=max_results,
            expand=expand,
        )
        return response.model_dump()
