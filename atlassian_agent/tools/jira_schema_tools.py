# Generated MCP Tools for JiraCloud - schema
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.jira_cloud_api import JiraCloudAPI
from ..auth import get_base_client


def get_api() -> JiraCloudAPI:
    return JiraCloudAPI(get_base_client())


def register_jira_schema_tools(mcp: FastMCP):
    @mcp.tool(
        name="jira_cloud_get_custom_fields_configurations",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_get_custom_fields_configurations(
        id_: list[Any] | None = Field(
            None,
            description="The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: `id=10000&id=10001`. Can't be provided with `fieldContextId`, `issueId`, `projectKeyOrId`, or `issueTypeId`.",
        ),
        field_context_id: list[Any] | None = Field(
            None,
            description="The list of field context IDs. To include multiple field contexts, separate IDs with an ampersand: `fieldContextId=10000&fieldContextId=10001`. Can't be provided with `id`, `issueId`, `projectKeyOrId`, or `issueTypeId`.",
        ),
        issue_id: int | None = Field(
            None,
            description="The ID of the issue to filter results by. If the issue doesn't exist, an empty list is returned. Can't be provided with `projectKeyOrId`, or `issueTypeId`.",
        ),
        project_key_or_id: str | None = Field(
            None,
            description="The ID or key of the project to filter results by. Must be provided with `issueTypeId`. Can't be provided with `issueId`.",
        ),
        issue_type_id: str | None = Field(
            None,
            description="The ID of the issue type to filter results by. Must be provided with `projectKeyOrId`. Can't be provided with `issueId`.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk get custom field configurations"""
        api = get_api()
        response = api.jira_cloud_get_custom_fields_configurations(
            id_=id_,
            field_context_id=field_context_id,
            issue_id=issue_id,
            project_key_or_id=project_key_or_id,
            issue_type_id=issue_type_id,
            start_at=start_at,
            max_results=max_results,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_multiple_custom_field_values",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_update_multiple_custom_field_values(
        generate_changelog: bool | None = Field(
            None, description="Whether to generate a changelog for this update."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update custom fields"""
        api = get_api()
        response = api.jira_cloud_update_multiple_custom_field_values(
            generate_changelog=generate_changelog,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_custom_field_configuration",
        tags={"jira-cloud-schema-field-configuration"},
    )
    def jira_cloud_get_custom_field_configuration(
        field_id_or_key: str = Field(
            ...,
            description="The ID or key of the custom field, for example `customfield_10000`.",
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: `id=10000&id=10001`. Can't be provided with `fieldContextId`, `issueId`, `projectKeyOrId`, or `issueTypeId`.",
        ),
        field_context_id: list[Any] | None = Field(
            None,
            description="The list of field context IDs. To include multiple field contexts, separate IDs with an ampersand: `fieldContextId=10000&fieldContextId=10001`. Can't be provided with `id`, `issueId`, `projectKeyOrId`, or `issueTypeId`.",
        ),
        issue_id: int | None = Field(
            None,
            description="The ID of the issue to filter results by. If the issue doesn't exist, an empty list is returned. Can't be provided with `projectKeyOrId`, or `issueTypeId`.",
        ),
        project_key_or_id: str | None = Field(
            None,
            description="The ID or key of the project to filter results by. Must be provided with `issueTypeId`. Can't be provided with `issueId`.",
        ),
        issue_type_id: str | None = Field(
            None,
            description="The ID of the issue type to filter results by. Must be provided with `projectKeyOrId`. Can't be provided with `issueId`.",
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
        """Get custom field configurations"""
        api = get_api()
        response = api.jira_cloud_get_custom_field_configuration(
            field_id_or_key=field_id_or_key,
            id_=id_,
            field_context_id=field_context_id,
            issue_id=issue_id,
            project_key_or_id=project_key_or_id,
            issue_type_id=issue_type_id,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_custom_field_configuration",
        tags={"jira-cloud-schema-field-configuration"},
    )
    def jira_cloud_update_custom_field_configuration(
        field_id_or_key: str = Field(
            ...,
            description="The ID or key of the custom field, for example `customfield_10000`.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update custom field configurations"""
        api = get_api()
        response = api.jira_cloud_update_custom_field_configuration(
            field_id_or_key=field_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_custom_field_value", tags={"jira-cloud-schema-field"}
    )
    def jira_cloud_update_custom_field_value(
        field_id_or_key: str = Field(
            ...,
            description="The ID or key of the custom field. For example, `customfield_10010`.",
        ),
        generate_changelog: bool | None = Field(
            None, description="Whether to generate a changelog for this update."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update custom field value"""
        api = get_api()
        response = api.jira_cloud_update_custom_field_value(
            field_id_or_key=field_id_or_key,
            generate_changelog=generate_changelog,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_field_association_schemes",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_get_field_association_schemes(
        project_id: list[Any] | None = Field(
            None,
            description="(optional) List of project IDs to filter schemes by. If not provided, schemes from all projects are returned.",
        ),
        query: str | None = Field(
            None,
            description="(optional) Text filter for scheme name or description matching (case-insensitive). If not provided, no text filtering is applied.",
        ),
        start_at: int | None = Field(
            None,
            description="Zero-based index of the first item to return (default: 0)",
        ),
        max_results: int | None = Field(
            None,
            description="Maximum number of items to return per page (default: 50, max: 100)",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get field schemes"""
        api = get_api()
        response = api.jira_cloud_get_field_association_schemes(
            project_id=project_id,
            query=query,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_field_association_scheme",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_create_field_association_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create field scheme"""
        api = get_api()
        response = api.jira_cloud_create_field_association_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_fields_associated_with_schemes",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_remove_fields_associated_with_schemes(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove fields associated with field schemes"""
        api = get_api()
        response = api.jira_cloud_remove_fields_associated_with_schemes(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_fields_associated_with_schemes",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_update_fields_associated_with_schemes(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update fields associated with field schemes"""
        api = get_api()
        response = api.jira_cloud_update_fields_associated_with_schemes(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_field_association_scheme",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_delete_field_association_scheme(
        id_: int = Field(
            ..., description="The ID of the field association scheme to delete."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a field scheme"""
        api = get_api()
        response = api.jira_cloud_delete_field_association_scheme(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_field_association_scheme_by_id",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_get_field_association_scheme_by_id(
        id_: int = Field(..., description="The scheme id to fetch"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get field scheme"""
        api = get_api()
        response = api.jira_cloud_get_field_association_scheme_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_field_association_scheme",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_update_field_association_scheme(
        id_: int = Field(..., description="Parameter id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update field scheme"""
        api = get_api()
        response = api.jira_cloud_update_field_association_scheme(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_clone_field_association_scheme",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_clone_field_association_scheme(
        id_: int = Field(
            ...,
            description="The ID of the source field association scheme to clone from",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Clone field scheme"""
        api = get_api()
        response = api.jira_cloud_clone_field_association_scheme(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_field_association_scheme_fields",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_search_field_association_scheme_fields(
        id_: int = Field(..., description="The scheme ID to search for child fields"),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned fields. Base index: 0.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of fields to return per page, maximum allowed value is 100.",
        ),
        field_id: list[Any] | None = Field(
            None,
            description="The field IDs to filter by, if empty then all fields belonging to a field association scheme will be returned",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search field scheme fields"""
        api = get_api()
        response = api.jira_cloud_search_field_association_scheme_fields(
            start_at=start_at,
            max_results=max_results,
            field_id=field_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_field_association_scheme_item_parameters",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_get_field_association_scheme_item_parameters(
        id_: int = Field(
            ...,
            description="the ID of the field association scheme to retrieve parameters for",
        ),
        field_id: str = Field(..., description="the ID of the field"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get field parameters"""
        api = get_api()
        response = api.jira_cloud_get_field_association_scheme_item_parameters(
            id_=id_,
            field_id=field_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_custom_field_option",
        tags={"jira-cloud-schema-field-option"},
    )
    def jira_cloud_get_custom_field_option(
        id_: str = Field(..., description="The ID of the custom field option."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom field option"""
        api = get_api()
        response = api.jira_cloud_get_custom_field_option(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_dashboards", tags={"jira-cloud-schema-other"})
    def jira_cloud_get_all_dashboards(
        filter: str | None = Field(
            None,
            description="The filter applied to the list of dashboards. Valid values are:   *  `favourite` Returns dashboards the user has marked as favorite.  *  `my` Returns dashboards owned by the user.",
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
        """Get all dashboards"""
        api = get_api()
        response = api.jira_cloud_get_all_dashboards(
            filter=filter,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_dashboard", tags={"jira-cloud-schema-other"})
    def jira_cloud_create_dashboard(
        extend_admin_permissions: bool | None = Field(
            None,
            description="Whether admin level permissions are used. It should only be true if the user has *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create dashboard"""
        api = get_api()
        response = api.jira_cloud_create_dashboard(
            extend_admin_permissions=extend_admin_permissions,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_available_dashboard_gadgets",
        tags={"jira-cloud-schema-other"},
    )
    def jira_cloud_get_all_available_dashboard_gadgets(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available gadgets"""
        api = get_api()
        response = api.jira_cloud_get_all_available_dashboard_gadgets()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_dashboards_paginated", tags={"jira-cloud-schema-other"}
    )
    def jira_cloud_get_dashboards_paginated(
        dashboard_name: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with `name`.",
        ),
        account_id: str | None = Field(
            None,
            description="User account ID used to return dashboards with the matching `owner.accountId`. This parameter cannot be used with the `owner` parameter.",
        ),
        owner: str | None = Field(
            None,
            description="This parameter is deprecated because of privacy changes. Use `accountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return dashboards with the matching `owner.name`. This parameter cannot be used with the `accountId` parameter.",
        ),
        groupname: str | None = Field(
            None,
            description="As a group's name can change, use of `groupId` is recommended. Group name used to return dashboards that are shared with a group that matches `sharePermissions.group.name`. This parameter cannot be used with the `groupId` parameter.",
        ),
        group_id: str | None = Field(
            None,
            description="Group ID used to return dashboards that are shared with a group that matches `sharePermissions.group.groupId`. This parameter cannot be used with the `groupname` parameter.",
        ),
        project_id: int | None = Field(
            None,
            description="Project ID used to returns dashboards that are shared with a project that matches `sharePermissions.project.id`.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `description` Sorts by dashboard description. Note that this sort works independently of whether the expand to display the description field is in use.  *  `favourite_count` Sorts by dashboard popularity.  *  `id` Sorts by dashboard ID.  *  `is_favourite` Sorts by whether the dashboard is marked as a favorite.  *  `name` Sorts by dashboard name.  *  `owner` Sorts by dashboard owner name.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        status: str | None = Field(
            None,
            description="The status to filter by. It may be active, archived or deleted.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about dashboard in the response. This parameter accepts a comma-separated list. Expand options include:   *  `description` Returns the description of the dashboard.  *  `owner` Returns the owner of the dashboard.  *  `viewUrl` Returns the URL that is used to view the dashboard.  *  `favourite` Returns `isFavourite`, an indicator of whether the user has set the dashboard as a favorite.  *  `favouritedCount` Returns `popularity`, a count of how many users have set this dashboard as a favorite.  *  `sharePermissions` Returns details of the share permissions defined for the dashboard.  *  `editPermissions` Returns details of the edit permissions defined for the dashboard.  *  `isWritable` Returns whether the current user has permission to edit the dashboard.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search for dashboards"""
        api = get_api()
        response = api.jira_cloud_get_dashboards_paginated(
            dashboard_name=dashboard_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            status=status,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_dashboard_item_property_keys",
        tags={"jira-cloud-schema-other"},
    )
    def jira_cloud_get_dashboard_item_property_keys(
        dashboard_id: str = Field(..., description="The ID of the dashboard."),
        item_id: str = Field(..., description="The ID of the dashboard item."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get dashboard item property keys"""
        api = get_api()
        response = api.jira_cloud_get_dashboard_item_property_keys(
            dashboard_id=dashboard_id,
            item_id=item_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_dashboard_item_property",
        tags={"jira-cloud-schema-other"},
    )
    def jira_cloud_delete_dashboard_item_property(
        dashboard_id: str = Field(..., description="The ID of the dashboard."),
        item_id: str = Field(..., description="The ID of the dashboard item."),
        property_key: str = Field(
            ..., description="The key of the dashboard item property."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete dashboard item property"""
        api = get_api()
        response = api.jira_cloud_delete_dashboard_item_property(
            dashboard_id=dashboard_id,
            item_id=item_id,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_dashboard_item_property", tags={"jira-cloud-schema-other"}
    )
    def jira_cloud_get_dashboard_item_property(
        dashboard_id: str = Field(..., description="The ID of the dashboard."),
        item_id: str = Field(..., description="The ID of the dashboard item."),
        property_key: str = Field(
            ..., description="The key of the dashboard item property."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get dashboard item property"""
        api = get_api()
        response = api.jira_cloud_get_dashboard_item_property(
            dashboard_id=dashboard_id,
            item_id=item_id,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_dashboard_item_property", tags={"jira-cloud-schema-other"}
    )
    def jira_cloud_set_dashboard_item_property(
        dashboard_id: str = Field(..., description="The ID of the dashboard."),
        item_id: str = Field(..., description="The ID of the dashboard item."),
        property_key: str = Field(
            ...,
            description="The key of the dashboard item property. The maximum length is 255 characters. For dashboard items with a spec URI and no complete module key, if the provided propertyKey is equal to 'config', the request body's JSON must be an object with all keys and values as strings.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set dashboard item property"""
        api = get_api()
        response = api.jira_cloud_set_dashboard_item_property(
            dashboard_id=dashboard_id,
            item_id=item_id,
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_dashboard", tags={"jira-cloud-schema-other"})
    def jira_cloud_delete_dashboard(
        id_: str = Field(..., description="The ID of the dashboard."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete dashboard"""
        api = get_api()
        response = api.jira_cloud_delete_dashboard(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_dashboard", tags={"jira-cloud-schema-other"})
    def jira_cloud_get_dashboard(
        id_: str = Field(..., description="The ID of the dashboard."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get dashboard"""
        api = get_api()
        response = api.jira_cloud_get_dashboard(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_dashboard", tags={"jira-cloud-schema-other"})
    def jira_cloud_update_dashboard(
        id_: str = Field(..., description="The ID of the dashboard to update."),
        extend_admin_permissions: bool | None = Field(
            None,
            description="Whether admin level permissions are used. It should only be true if the user has *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update dashboard"""
        api = get_api()
        response = api.jira_cloud_update_dashboard(
            id_=id_,
            extend_admin_permissions=extend_admin_permissions,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_copy_dashboard", tags={"jira-cloud-schema-other"})
    def jira_cloud_copy_dashboard(
        id_: str = Field(..., description="Parameter id"),
        extend_admin_permissions: bool | None = Field(
            None,
            description="Whether admin level permissions are used. It should only be true if the user has *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Copy dashboard"""
        api = get_api()
        response = api.jira_cloud_copy_dashboard(
            id_=id_,
            extend_admin_permissions=extend_admin_permissions,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_fields", tags={"jira-cloud-schema-field"})
    def jira_cloud_get_fields(_ctx: Context | None = None) -> dict[str, Any]:
        """Get fields"""
        api = get_api()
        response = api.jira_cloud_get_fields()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_custom_field", tags={"jira-cloud-schema-field"})
    def jira_cloud_create_custom_field(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create custom field"""
        api = get_api()
        response = api.jira_cloud_create_custom_field(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_fields_paginated", tags={"jira-cloud-schema-field"})
    def jira_cloud_get_fields_paginated(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        type_: list[Any] | None = Field(
            None, description="The type of fields to search."
        ),
        id_: list[Any] | None = Field(
            None,
            description="The IDs of the custom fields to return or, where `query` is specified, filter.",
        ),
        query: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with field names or descriptions.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by:   *  `contextsCount` sorts by the number of contexts related to a field  *  `lastUsed` sorts by the date when the value of the field last changed  *  `name` sorts by the field name  *  `screensCount` sorts by the number of screens related to a field",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `key` returns the key for each field  *  `stableId` returns the stableId for each field  *  `lastUsed` returns the date when the value of the field last changed  *  `screensCount` returns the number of screens related to a field  *  `contextsCount` returns the number of contexts related to a field  *  `isLocked` returns information about whether the field is locked  *  `searcherKey` returns the searcher key for each custom field",
        ),
        project_ids: list[Any] | None = Field(
            None,
            description="The IDs of the projects to filter the fields by. Fields belonging to project Ids that the user does not have access to will not be returned",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get fields paginated"""
        api = get_api()
        response = api.jira_cloud_get_fields_paginated(
            start_at=start_at,
            max_results=max_results,
            type_=type_,
            id_=id_,
            query=query,
            order_by=order_by,
            expand=expand,
            project_ids=project_ids,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_trashed_fields_paginated", tags={"jira-cloud-schema-field"}
    )
    def jira_cloud_get_trashed_fields_paginated(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(None, description="Parameter id"),
        query: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with field names or descriptions.",
        ),
        expand: str | None = Field(None, description="Parameter expand"),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `name` sorts by the field name  *  `trashDate` sorts by the date the field was moved to the trash  *  `plannedDeletionDate` sorts by the planned deletion date",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get fields in trash paginated"""
        api = get_api()
        response = api.jira_cloud_get_trashed_fields_paginated(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            query=query,
            expand=expand,
            order_by=order_by,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_custom_field", tags={"jira-cloud-schema-field"})
    def jira_cloud_update_custom_field(
        field_id: str = Field(..., description="The ID of the custom field."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update custom field"""
        api = get_api()
        response = api.jira_cloud_update_custom_field(
            field_id=field_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_contexts_for_field", tags={"jira-cloud-schema-field"}
    )
    def jira_cloud_get_contexts_for_field(
        field_id: str = Field(..., description="The ID of the custom field."),
        is_any_issue_type: bool | None = Field(
            None,
            description="Whether to return contexts that apply to all issue types.",
        ),
        is_global_context: bool | None = Field(
            None, description="Whether to return contexts that apply to all projects."
        ),
        context_id: list[Any] | None = Field(
            None,
            description="The list of context IDs. To include multiple contexts, separate IDs with ampersand: `contextId=10000&contextId=10001`.",
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
        """Get custom field contexts"""
        api = get_api()
        response = api.jira_cloud_get_contexts_for_field(
            field_id=field_id,
            is_any_issue_type=is_any_issue_type,
            is_global_context=is_global_context,
            context_id=context_id,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_custom_field_context",
        tags={"jira-cloud-schema-field-context"},
    )
    def jira_cloud_create_custom_field_context(
        field_id: str = Field(..., description="The ID of the custom field."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create custom field context"""
        api = get_api()
        response = api.jira_cloud_create_custom_field_context(
            field_id=field_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_custom_field_context",
        tags={"jira-cloud-schema-field-context"},
    )
    def jira_cloud_delete_custom_field_context(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete custom field context"""
        api = get_api()
        response = api.jira_cloud_delete_custom_field_context(
            field_id=field_id,
            context_id=context_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_custom_field_context",
        tags={"jira-cloud-schema-field-context"},
    )
    def jira_cloud_update_custom_field_context(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update custom field context"""
        api = get_api()
        response = api.jira_cloud_update_custom_field_context(
            field_id=field_id,
            context_id=context_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_custom_field_option",
        tags={"jira-cloud-schema-field-option"},
    )
    def jira_cloud_create_custom_field_option(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create custom field options (context)"""
        api = get_api()
        response = api.jira_cloud_create_custom_field_option(
            field_id=field_id,
            context_id=context_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_custom_field_option",
        tags={"jira-cloud-schema-field-option"},
    )
    def jira_cloud_update_custom_field_option(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update custom field options (context)"""
        api = get_api()
        response = api.jira_cloud_update_custom_field_option(
            field_id=field_id,
            context_id=context_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_reorder_custom_field_options",
        tags={"jira-cloud-schema-field-option"},
    )
    def jira_cloud_reorder_custom_field_options(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reorder custom field options (context)"""
        api = get_api()
        response = api.jira_cloud_reorder_custom_field_options(
            field_id=field_id,
            context_id=context_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_custom_field_option",
        tags={"jira-cloud-schema-field-option"},
    )
    def jira_cloud_delete_custom_field_option(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(
            ...,
            description="The ID of the context from which an option should be deleted.",
        ),
        option_id: int = Field(..., description="The ID of the option to delete."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete custom field options (context)"""
        api = get_api()
        response = api.jira_cloud_delete_custom_field_option(
            field_id=field_id,
            context_id=context_id,
            option_id=option_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_replace_custom_field_option",
        tags={"jira-cloud-schema-field-option"},
    )
    def jira_cloud_replace_custom_field_option(
        field_id: str = Field(..., description="The ID of the custom field."),
        option_id: int = Field(
            ..., description="The ID of the option to be deselected."
        ),
        context_id: int = Field(..., description="The ID of the context."),
        replace_with: int | None = Field(
            None,
            description="The ID of the option that will replace the currently selected option.",
        ),
        jql: str | None = Field(
            None,
            description="A JQL query that specifies the issues to be updated. For example, *project=10000*.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Replace custom field options"""
        api = get_api()
        response = api.jira_cloud_replace_custom_field_option(
            replace_with=replace_with,
            jql=jql,
            field_id=field_id,
            option_id=option_id,
            context_id=context_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_contexts_for_field_deprecated",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_get_contexts_for_field_deprecated(
        field_id: str = Field(
            ..., description="The ID of the field to return contexts for."
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
        """Get contexts for a field"""
        api = get_api()
        response = api.jira_cloud_get_contexts_for_field_deprecated(
            field_id=field_id,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_screens_for_field", tags={"jira-cloud-schema-screen"}
    )
    def jira_cloud_get_screens_for_field(
        field_id: str = Field(
            ..., description="The ID of the field to return screens for."
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about screens in the response. This parameter accepts `tab` which returns details about the screen tabs the field is used in.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get screens for a field"""
        api = get_api()
        response = api.jira_cloud_get_screens_for_field(
            field_id=field_id,
            start_at=start_at,
            max_results=max_results,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_custom_field", tags={"jira-cloud-schema-field"})
    def jira_cloud_delete_custom_field(
        id_: str = Field(..., description="The ID of a custom field."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete custom field"""
        api = get_api()
        response = api.jira_cloud_delete_custom_field(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_restore_custom_field", tags={"jira-cloud-schema-field"})
    def jira_cloud_restore_custom_field(
        id_: str = Field(..., description="The ID of a custom field."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Restore custom field from trash"""
        api = get_api()
        response = api.jira_cloud_restore_custom_field(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_trash_custom_field", tags={"jira-cloud-schema-field"})
    def jira_cloud_trash_custom_field(
        id_: str = Field(..., description="The ID of a custom field."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move custom field to trash"""
        api = get_api()
        response = api.jira_cloud_trash_custom_field(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_field_configurations",
        tags={"jira-cloud-schema-field-configuration"},
    )
    def jira_cloud_get_all_field_configurations(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of field configuration IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.",
        ),
        is_default: bool | None = Field(
            None, description="If *true* returns default field configurations only."
        ),
        query: str | None = Field(
            None,
            description="The query string used to match against field configuration names and descriptions.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all field configurations"""
        api = get_api()
        response = api.jira_cloud_get_all_field_configurations(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            is_default=is_default,
            query=query,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_field_configuration",
        tags={"jira-cloud-schema-field-configuration"},
    )
    def jira_cloud_create_field_configuration(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create field configuration"""
        api = get_api()
        response = api.jira_cloud_create_field_configuration(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_field_configuration",
        tags={"jira-cloud-schema-field-configuration"},
    )
    def jira_cloud_delete_field_configuration(
        id_: int = Field(..., description="The ID of the field configuration."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete field configuration"""
        api = get_api()
        response = api.jira_cloud_delete_field_configuration(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_field_configuration",
        tags={"jira-cloud-schema-field-configuration"},
    )
    def jira_cloud_update_field_configuration(
        id_: int = Field(..., description="The ID of the field configuration."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update field configuration"""
        api = get_api()
        response = api.jira_cloud_update_field_configuration(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_field_configuration_items",
        tags={"jira-cloud-schema-field-configuration"},
    )
    def jira_cloud_get_field_configuration_items(
        id_: int = Field(..., description="The ID of the field configuration."),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get field configuration items"""
        api = get_api()
        response = api.jira_cloud_get_field_configuration_items(
            id_=id_,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_field_configuration_items",
        tags={"jira-cloud-schema-field-configuration"},
    )
    def jira_cloud_update_field_configuration_items(
        id_: int = Field(..., description="The ID of the field configuration."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update field configuration items"""
        api = get_api()
        response = api.jira_cloud_update_field_configuration_items(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_field_configuration_schemes",
        tags={"jira-cloud-schema-field-configuration-scheme"},
    )
    def jira_cloud_get_all_field_configuration_schemes(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of field configuration scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all field configuration schemes"""
        api = get_api()
        response = api.jira_cloud_get_all_field_configuration_schemes(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_field_configuration_scheme",
        tags={"jira-cloud-schema-field-configuration-scheme"},
    )
    def jira_cloud_create_field_configuration_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create field configuration scheme"""
        api = get_api()
        response = api.jira_cloud_create_field_configuration_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_field_configuration_scheme_mappings",
        tags={"jira-cloud-schema-field-configuration-scheme"},
    )
    def jira_cloud_get_field_configuration_scheme_mappings(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        field_configuration_scheme_id: list[Any] | None = Field(
            None,
            description="The list of field configuration scheme IDs. To include multiple field configuration schemes separate IDs with ampersand: `fieldConfigurationSchemeId=10000&fieldConfigurationSchemeId=10001`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get field configuration issue type items"""
        api = get_api()
        response = api.jira_cloud_get_field_configuration_scheme_mappings(
            start_at=start_at,
            max_results=max_results,
            field_configuration_scheme_id=field_configuration_scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_field_configuration_scheme",
        tags={"jira-cloud-schema-field-configuration-scheme"},
    )
    def jira_cloud_delete_field_configuration_scheme(
        id_: int = Field(..., description="The ID of the field configuration scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete field configuration scheme"""
        api = get_api()
        response = api.jira_cloud_delete_field_configuration_scheme(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_field_configuration_scheme",
        tags={"jira-cloud-schema-field-configuration-scheme"},
    )
    def jira_cloud_update_field_configuration_scheme(
        id_: int = Field(..., description="The ID of the field configuration scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update field configuration scheme"""
        api = get_api()
        response = api.jira_cloud_update_field_configuration_scheme(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_field_configuration_scheme_mapping",
        tags={"jira-cloud-schema-field-configuration-scheme"},
    )
    def jira_cloud_set_field_configuration_scheme_mapping(
        id_: int = Field(..., description="The ID of the field configuration scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign issue types to field configurations"""
        api = get_api()
        response = api.jira_cloud_set_field_configuration_scheme_mapping(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_security_schemes", tags={"jira-cloud-schema-other"}
    )
    def jira_cloud_search_security_schemes(
        start_at: str | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: str | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of issue security scheme IDs. To include multiple issue security scheme IDs, separate IDs with an ampersand: `id=10000&id=10001`.",
        ),
        project_id: list[Any] | None = Field(
            None,
            description="The list of project IDs. To include multiple project IDs, separate IDs with an ampersand: `projectId=10000&projectId=10001`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search issue security schemes"""
        api = get_api()
        response = api.jira_cloud_search_security_schemes(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_security_scheme", tags={"jira-cloud-schema-other"}
    )
    def jira_cloud_delete_security_scheme(
        scheme_id: str = Field(..., description="The ID of the issue security scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue security scheme"""
        api = get_api()
        response = api.jira_cloud_delete_security_scheme(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_default_screen_scheme",
        tags={"jira-cloud-schema-screen-scheme"},
    )
    def jira_cloud_update_default_screen_scheme(
        issue_type_screen_scheme_id: str = Field(
            ..., description="The ID of the issue type screen scheme."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update issue type screen scheme default screen scheme"""
        api = get_api()
        response = api.jira_cloud_update_default_screen_scheme(
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_field_auto_complete_for_query_string",
        tags={"jira-cloud-schema-field"},
    )
    def jira_cloud_get_field_auto_complete_for_query_string(
        field_name: str | None = Field(None, description="The name of the field."),
        field_value: str | None = Field(
            None, description="The partial field item name entered by the user."
        ),
        predicate_name: str | None = Field(
            None,
            description="The name of the [ CHANGED operator predicate](https://confluence.atlassian.com/x/hQORLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for which the suggestions are generated. The valid predicate operators are *by*, *from*, and *to*.",
        ),
        predicate_value: str | None = Field(
            None, description="The partial predicate item name entered by the user."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get field auto complete suggestions"""
        api = get_api()
        response = api.jira_cloud_get_field_auto_complete_for_query_string(
            field_name=field_name,
            field_value=field_value,
            predicate_name=predicate_name,
            predicate_value=predicate_value,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_notification_schemes",
        tags={"jira-cloud-schema-notification-scheme"},
    )
    def jira_cloud_get_notification_schemes(
        start_at: str | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: str | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None, description="The list of notification schemes IDs to be filtered by"
        ),
        project_id: list[Any] | None = Field(
            None, description="The list of projects IDs to be filtered by"
        ),
        only_default: bool | None = Field(
            None,
            description="When set to true, returns only the default notification scheme. If you provide project IDs not associated with the default, returns an empty page. The default value is false.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `all` Returns all expandable information  *  `field` Returns information about any custom fields assigned to receive an event  *  `group` Returns information about any groups assigned to receive an event  *  `notificationSchemeEvents` Returns a list of event associations. This list is returned for all expandable information  *  `projectRole` Returns information about any project roles assigned to receive an event  *  `user` Returns information about any users assigned to receive an event",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get notification schemes paginated"""
        api = get_api()
        response = api.jira_cloud_get_notification_schemes(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            project_id=project_id,
            only_default=only_default,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_notification_scheme",
        tags={"jira-cloud-schema-notification-scheme"},
    )
    def jira_cloud_create_notification_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create notification scheme"""
        api = get_api()
        response = api.jira_cloud_create_notification_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_notification_scheme",
        tags={"jira-cloud-schema-notification-scheme"},
    )
    def jira_cloud_get_notification_scheme(
        id_: int = Field(
            ...,
            description="The ID of the notification scheme. Use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get) to get a list of notification scheme IDs.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `all` Returns all expandable information  *  `field` Returns information about any custom fields assigned to receive an event  *  `group` Returns information about any groups assigned to receive an event  *  `notificationSchemeEvents` Returns a list of event associations. This list is returned for all expandable information  *  `projectRole` Returns information about any project roles assigned to receive an event  *  `user` Returns information about any users assigned to receive an event",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get notification scheme"""
        api = get_api()
        response = api.jira_cloud_get_notification_scheme(
            id_=id_,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_notification_scheme",
        tags={"jira-cloud-schema-notification-scheme"},
    )
    def jira_cloud_update_notification_scheme(
        id_: str = Field(..., description="The ID of the notification scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update notification scheme"""
        api = get_api()
        response = api.jira_cloud_update_notification_scheme(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_notification_scheme",
        tags={"jira-cloud-schema-notification-scheme"},
    )
    def jira_cloud_delete_notification_scheme(
        notification_scheme_id: str = Field(
            ..., description="The ID of the notification scheme."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete notification scheme"""
        api = get_api()
        response = api.jira_cloud_delete_notification_scheme(
            notification_scheme_id=notification_scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_notification_from_notification_scheme",
        tags={"jira-cloud-schema-notification-scheme"},
    )
    def jira_cloud_remove_notification_from_notification_scheme(
        notification_scheme_id: str = Field(
            ..., description="The ID of the notification scheme."
        ),
        notification_id: str = Field(..., description="The ID of the notification."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove notification from notification scheme"""
        api = get_api()
        response = api.jira_cloud_remove_notification_from_notification_scheme(
            notification_scheme_id=notification_scheme_id,
            notification_id=notification_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_priority", tags={"jira-cloud-schema-priority"})
    def jira_cloud_create_priority(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create priority"""
        api = get_api()
        response = api.jira_cloud_create_priority(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_default_priority", tags={"jira-cloud-schema-priority"}
    )
    def jira_cloud_set_default_priority(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set default priority"""
        api = get_api()
        response = api.jira_cloud_set_default_priority(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_priority", tags={"jira-cloud-schema-priority"})
    def jira_cloud_delete_priority(
        id_: str = Field(..., description="The ID of the issue priority."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete priority"""
        api = get_api()
        response = api.jira_cloud_delete_priority(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_priority", tags={"jira-cloud-schema-priority"})
    def jira_cloud_get_priority(
        id_: str = Field(..., description="The ID of the issue priority."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get priority"""
        api = get_api()
        response = api.jira_cloud_get_priority(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_priority", tags={"jira-cloud-schema-priority"})
    def jira_cloud_update_priority(
        id_: str = Field(..., description="The ID of the issue priority."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update priority"""
        api = get_api()
        response = api.jira_cloud_update_priority(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_priority_schemes",
        tags={"jira-cloud-schema-priority-scheme"},
    )
    def jira_cloud_get_priority_schemes(
        start_at: str | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: str | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        priority_id: list[Any] | None = Field(
            None,
            description="A set of priority IDs to filter by. To include multiple IDs, provide an ampersand-separated list. For example, `priorityId=10000&priorityId=10001`.",
        ),
        scheme_id: list[Any] | None = Field(
            None,
            description="A set of priority scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `schemeId=10000&schemeId=10001`.",
        ),
        scheme_name: str | None = Field(
            None, description="The name of scheme to search for."
        ),
        only_default: bool | None = Field(
            None, description="Whether only the default priority is returned."
        ),
        order_by: str | None = Field(
            None, description="The ordering to return the priority schemes by."
        ),
        expand: str | None = Field(
            None,
            description="A comma separated list of additional information to return. 'priorities' will return priorities associated with the priority scheme. 'projects' will return projects associated with the priority scheme. `expand=priorities,projects`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get priority schemes"""
        api = get_api()
        response = api.jira_cloud_get_priority_schemes(
            start_at=start_at,
            max_results=max_results,
            priority_id=priority_id,
            scheme_id=scheme_id,
            scheme_name=scheme_name,
            only_default=only_default,
            order_by=order_by,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_priority_scheme",
        tags={"jira-cloud-schema-priority-scheme"},
    )
    def jira_cloud_create_priority_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create priority scheme"""
        api = get_api()
        response = api.jira_cloud_create_priority_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_available_priorities_by_priority_scheme",
        tags={"jira-cloud-schema-priority-scheme"},
    )
    def jira_cloud_get_available_priorities_by_priority_scheme(
        scheme_id: str = Field(..., description="The priority scheme ID."),
        start_at: str | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: str | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        query: str | None = Field(
            None, description="The string to query priorities on by name."
        ),
        exclude: list[Any] | None = Field(
            None, description="A list of priority IDs to exclude from the results."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available priorities by priority scheme"""
        api = get_api()
        response = api.jira_cloud_get_available_priorities_by_priority_scheme(
            start_at=start_at,
            max_results=max_results,
            query=query,
            scheme_id=scheme_id,
            exclude=exclude,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_priority_scheme",
        tags={"jira-cloud-schema-priority-scheme"},
    )
    def jira_cloud_delete_priority_scheme(
        scheme_id: int = Field(..., description="The priority scheme ID."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete priority scheme"""
        api = get_api()
        response = api.jira_cloud_delete_priority_scheme(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_priority_scheme",
        tags={"jira-cloud-schema-priority-scheme"},
    )
    def jira_cloud_update_priority_scheme(
        scheme_id: int = Field(..., description="The ID of the priority scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update priority scheme"""
        api = get_api()
        response = api.jira_cloud_update_priority_scheme(
            scheme_id=scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_priorities_by_priority_scheme",
        tags={"jira-cloud-schema-priority-scheme"},
    )
    def jira_cloud_get_priorities_by_priority_scheme(
        scheme_id: str = Field(..., description="The priority scheme ID."),
        start_at: str | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: str | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get priorities by priority scheme"""
        api = get_api()
        response = api.jira_cloud_get_priorities_by_priority_scheme(
            start_at=start_at,
            max_results=max_results,
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_statuses", tags={"jira-cloud-schema-status"})
    def jira_cloud_get_all_statuses(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all statuses for project"""
        api = get_api()
        response = api.jira_cloud_get_all_statuses(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_redaction_status", tags={"jira-cloud-schema-status"})
    def jira_cloud_get_redaction_status(
        job_id: str = Field(..., description="Redaction job id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get redaction status"""
        api = get_api()
        response = api.jira_cloud_get_redaction_status(
            job_id=job_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_resolutions", tags={"jira-cloud-schema-resolution"})
    def jira_cloud_get_resolutions(_ctx: Context | None = None) -> dict[str, Any]:
        """Get resolutions"""
        api = get_api()
        response = api.jira_cloud_get_resolutions()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_resolution", tags={"jira-cloud-schema-resolution"}
    )
    def jira_cloud_create_resolution(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create resolution"""
        api = get_api()
        response = api.jira_cloud_create_resolution(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_default_resolution", tags={"jira-cloud-schema-resolution"}
    )
    def jira_cloud_set_default_resolution(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set default resolution"""
        api = get_api()
        response = api.jira_cloud_set_default_resolution(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_move_resolutions", tags={"jira-cloud-schema-resolution"})
    def jira_cloud_move_resolutions(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move resolutions"""
        api = get_api()
        response = api.jira_cloud_move_resolutions(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_resolutions", tags={"jira-cloud-schema-resolution"}
    )
    def jira_cloud_search_resolutions(
        start_at: str | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: str | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None, description="The list of resolutions IDs to be filtered out"
        ),
        only_default: bool | None = Field(
            None,
            description="When set to true, return default only, when IDs provided, if none of them is default, return empty page. Default value is false",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search resolutions"""
        api = get_api()
        response = api.jira_cloud_search_resolutions(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            only_default=only_default,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_resolution", tags={"jira-cloud-schema-resolution"}
    )
    def jira_cloud_delete_resolution(
        id_: str = Field(..., description="The ID of the issue resolution."),
        replace_with: str = Field(
            ...,
            description="The ID of the issue resolution that will replace the currently selected resolution.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete resolution"""
        api = get_api()
        response = api.jira_cloud_delete_resolution(
            id_=id_,
            replace_with=replace_with,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_resolution", tags={"jira-cloud-schema-resolution"})
    def jira_cloud_get_resolution(
        id_: str = Field(..., description="The ID of the issue resolution value."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get resolution"""
        api = get_api()
        response = api.jira_cloud_get_resolution(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_resolution", tags={"jira-cloud-schema-resolution"}
    )
    def jira_cloud_update_resolution(
        id_: str = Field(..., description="The ID of the issue resolution."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update resolution"""
        api = get_api()
        response = api.jira_cloud_update_resolution(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_screens", tags={"jira-cloud-schema-screen"})
    def jira_cloud_get_screens(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of screen IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.",
        ),
        query_string: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with screen name.",
        ),
        scope: list[Any] | None = Field(
            None,
            description="The scope filter string. To filter by multiple scope, provide an ampersand-separated list. For example, `scope=GLOBAL&scope=PROJECT`.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `id` Sorts by screen ID.  *  `name` Sorts by screen name.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get screens"""
        api = get_api()
        response = api.jira_cloud_get_screens(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            query_string=query_string,
            scope=scope,
            order_by=order_by,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_screen", tags={"jira-cloud-schema-screen"})
    def jira_cloud_create_screen(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create screen"""
        api = get_api()
        response = api.jira_cloud_create_screen(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_add_field_to_default_screen", tags={"jira-cloud-schema-screen"}
    )
    def jira_cloud_add_field_to_default_screen(
        field_id: str = Field(..., description="The ID of the field."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add field to default screen"""
        api = get_api()
        response = api.jira_cloud_add_field_to_default_screen(
            field_id=field_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_screen", tags={"jira-cloud-schema-screen"})
    def jira_cloud_delete_screen(
        screen_id: int = Field(..., description="The ID of the screen."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete screen"""
        api = get_api()
        response = api.jira_cloud_delete_screen(
            screen_id=screen_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_screen", tags={"jira-cloud-schema-screen"})
    def jira_cloud_update_screen(
        screen_id: int = Field(..., description="The ID of the screen."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update screen"""
        api = get_api()
        response = api.jira_cloud_update_screen(
            screen_id=screen_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_available_screen_fields", tags={"jira-cloud-schema-screen"}
    )
    def jira_cloud_get_available_screen_fields(
        screen_id: int = Field(..., description="The ID of the screen."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available screen fields"""
        api = get_api()
        response = api.jira_cloud_get_available_screen_fields(
            screen_id=screen_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_screen_tabs", tags={"jira-cloud-schema-screen-tab"}
    )
    def jira_cloud_get_all_screen_tabs(
        screen_id: int = Field(..., description="The ID of the screen."),
        project_key: str | None = Field(None, description="The key of the project."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all screen tabs"""
        api = get_api()
        response = api.jira_cloud_get_all_screen_tabs(
            screen_id=screen_id,
            project_key=project_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_screen_tab", tags={"jira-cloud-schema-screen-tab"})
    def jira_cloud_add_screen_tab(
        screen_id: int = Field(..., description="The ID of the screen."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create screen tab"""
        api = get_api()
        response = api.jira_cloud_add_screen_tab(
            screen_id=screen_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_screen_tab", tags={"jira-cloud-schema-screen-tab"}
    )
    def jira_cloud_delete_screen_tab(
        screen_id: int = Field(..., description="The ID of the screen."),
        tab_id: int = Field(..., description="The ID of the screen tab."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete screen tab"""
        api = get_api()
        response = api.jira_cloud_delete_screen_tab(
            screen_id=screen_id,
            tab_id=tab_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_rename_screen_tab", tags={"jira-cloud-schema-screen-tab"}
    )
    def jira_cloud_rename_screen_tab(
        screen_id: int = Field(..., description="The ID of the screen."),
        tab_id: int = Field(..., description="The ID of the screen tab."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update screen tab"""
        api = get_api()
        response = api.jira_cloud_rename_screen_tab(
            screen_id=screen_id,
            tab_id=tab_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_screen_tab_fields",
        tags={"jira-cloud-schema-screen-tab-field"},
    )
    def jira_cloud_get_all_screen_tab_fields(
        screen_id: int = Field(..., description="The ID of the screen."),
        tab_id: int = Field(..., description="The ID of the screen tab."),
        project_key: str | None = Field(None, description="The key of the project."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all screen tab fields"""
        api = get_api()
        response = api.jira_cloud_get_all_screen_tab_fields(
            screen_id=screen_id,
            tab_id=tab_id,
            project_key=project_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_add_screen_tab_field",
        tags={"jira-cloud-schema-screen-tab-field"},
    )
    def jira_cloud_add_screen_tab_field(
        screen_id: int = Field(..., description="The ID of the screen."),
        tab_id: int = Field(..., description="The ID of the screen tab."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add screen tab field"""
        api = get_api()
        response = api.jira_cloud_add_screen_tab_field(
            screen_id=screen_id,
            tab_id=tab_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_screen_tab_field",
        tags={"jira-cloud-schema-screen-tab-field"},
    )
    def jira_cloud_remove_screen_tab_field(
        screen_id: int = Field(..., description="The ID of the screen."),
        tab_id: int = Field(..., description="The ID of the screen tab."),
        id_: str = Field(..., description="The ID of the field."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove screen tab field"""
        api = get_api()
        response = api.jira_cloud_remove_screen_tab_field(
            screen_id=screen_id,
            tab_id=tab_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_move_screen_tab_field",
        tags={"jira-cloud-schema-screen-tab-field"},
    )
    def jira_cloud_move_screen_tab_field(
        screen_id: int = Field(..., description="The ID of the screen."),
        tab_id: int = Field(..., description="The ID of the screen tab."),
        id_: str = Field(..., description="The ID of the field."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move screen tab field"""
        api = get_api()
        response = api.jira_cloud_move_screen_tab_field(
            screen_id=screen_id,
            tab_id=tab_id,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_move_screen_tab", tags={"jira-cloud-schema-screen-tab"})
    def jira_cloud_move_screen_tab(
        screen_id: int = Field(..., description="The ID of the screen."),
        tab_id: int = Field(..., description="The ID of the screen tab."),
        pos: int = Field(..., description="The position of tab. The base index is 0."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move screen tab"""
        api = get_api()
        response = api.jira_cloud_move_screen_tab(
            screen_id=screen_id,
            tab_id=tab_id,
            pos=pos,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_screen_schemes", tags={"jira-cloud-schema-screen-scheme"}
    )
    def jira_cloud_get_screen_schemes(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) include additional information in the response. This parameter accepts `issueTypeScreenSchemes` that, for each screen schemes, returns information about the issue type screen scheme the screen scheme is assigned to.",
        ),
        query_string: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with screen scheme name.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `id` Sorts by screen scheme ID.  *  `name` Sorts by screen scheme name.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get screen schemes"""
        api = get_api()
        response = api.jira_cloud_get_screen_schemes(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            expand=expand,
            query_string=query_string,
            order_by=order_by,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_screen_scheme", tags={"jira-cloud-schema-screen-scheme"}
    )
    def jira_cloud_create_screen_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create screen scheme"""
        api = get_api()
        response = api.jira_cloud_create_screen_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_screen_scheme", tags={"jira-cloud-schema-screen-scheme"}
    )
    def jira_cloud_delete_screen_scheme(
        screen_scheme_id: str = Field(..., description="The ID of the screen scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete screen scheme"""
        api = get_api()
        response = api.jira_cloud_delete_screen_scheme(
            screen_scheme_id=screen_scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_screen_scheme", tags={"jira-cloud-schema-screen-scheme"}
    )
    def jira_cloud_update_screen_scheme(
        screen_scheme_id: str = Field(..., description="The ID of the screen scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update screen scheme"""
        api = get_api()
        response = api.jira_cloud_update_screen_scheme(
            screen_scheme_id=screen_scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_statuses", tags={"jira-cloud-schema-status"})
    def jira_cloud_get_statuses(_ctx: Context | None = None) -> dict[str, Any]:
        """Get all statuses"""
        api = get_api()
        response = api.jira_cloud_get_statuses()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_status", tags={"jira-cloud-schema-status"})
    def jira_cloud_get_status(
        id_or_name: str = Field(..., description="The ID or name of the status."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get status"""
        api = get_api()
        response = api.jira_cloud_get_status(
            id_or_name=id_or_name,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_status_categories", tags={"jira-cloud-schema-status"}
    )
    def jira_cloud_get_status_categories(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all status categories"""
        api = get_api()
        response = api.jira_cloud_get_status_categories()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_status_category", tags={"jira-cloud-schema-status"})
    def jira_cloud_get_status_category(
        id_or_key: str = Field(
            ..., description="The ID or key of the status category."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get status category"""
        api = get_api()
        response = api.jira_cloud_get_status_category(
            id_or_key=id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_statuses_by_id", tags={"jira-cloud-schema-status"}
    )
    def jira_cloud_delete_statuses_by_id(
        id_: list[Any] = Field(
            ...,
            description="The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.  Min items `1`, Max items `50`",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk delete Statuses"""
        api = get_api()
        response = api.jira_cloud_delete_statuses_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_statuses_by_id", tags={"jira-cloud-schema-status"})
    def jira_cloud_get_statuses_by_id(
        id_: list[Any] = Field(
            ...,
            description="The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.  Min items `1`, Max items `50`",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk get statuses"""
        api = get_api()
        response = api.jira_cloud_get_statuses_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_statuses", tags={"jira-cloud-schema-status"})
    def jira_cloud_create_statuses(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk create statuses"""
        api = get_api()
        response = api.jira_cloud_create_statuses(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_statuses", tags={"jira-cloud-schema-status"})
    def jira_cloud_update_statuses(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk update statuses"""
        api = get_api()
        response = api.jira_cloud_update_statuses(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_statuses_by_name", tags={"jira-cloud-schema-status"})
    def jira_cloud_get_statuses_by_name(
        name: list[Any] = Field(
            ...,
            description="The list of status names. To include multiple names, provide an ampersand-separated list. For example, name=nameXX&name=nameYY.  Min items `1`, Max items `50`",
        ),
        project_id: str | None = Field(
            None,
            description="The project the status is part of or null for global statuses.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk get statuses by name"""
        api = get_api()
        response = api.jira_cloud_get_statuses_by_name(
            name=name,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_usages_for_status",
        tags={"jira-cloud-schema-workflow"},
    )
    def jira_cloud_get_workflow_usages_for_status(
        status_id: str = Field(
            ..., description="The statusId to fetch workflow usages for"
        ),
        next_page_token: str | None = Field(
            None, description="The cursor for pagination"
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of results to return. Must be an integer between 1 and 200.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow usages by status"""
        api = get_api()
        response = api.jira_cloud_get_workflow_usages_for_status(
            status_id=status_id,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_avatar_image_by_type", tags={"jira-cloud-schema-other"}
    )
    def jira_cloud_get_avatar_image_by_type(
        type_: str = Field(..., description="The icon type of the avatar."),
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
        """Get avatar image by type"""
        api = get_api()
        response = api.jira_cloud_get_avatar_image_by_type(
            type_=type_,
            size=size,
            format=format,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_workflows", tags={"jira-cloud-schema-workflow"})
    def jira_cloud_get_all_workflows(
        workflow_name: str | None = Field(
            None,
            description="The name of the workflow to be returned. Only one workflow can be specified.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all workflows"""
        api = get_api()
        response = api.jira_cloud_get_all_workflows(
            workflow_name=workflow_name,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_workflow", tags={"jira-cloud-schema-workflow"})
    def jira_cloud_create_workflow(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create workflow"""
        api = get_api()
        response = api.jira_cloud_create_workflow(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_read_workflow_from_history",
        tags={"jira-cloud-schema-workflow"},
    )
    def jira_cloud_read_workflow_from_history(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Read workflow version from history"""
        api = get_api()
        response = api.jira_cloud_read_workflow_from_history(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_list_workflow_history", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_list_workflow_history(
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `includeIntermediateWorkflows` Includes intermediate workflow versions that are sometimes created during workflow updates or migrations. By default, these are omitted from the response.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """List workflow history entries"""
        api = get_api()
        response = api.jira_cloud_list_workflow_history(
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflows_paginated", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_get_workflows_paginated(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        workflow_name: list[Any] | None = Field(
            None,
            description="The name of a workflow to return. To include multiple workflows, provide an ampersand-separated list. For example, `workflowName=name1&workflowName=name2`.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `transitions` For each workflow, returns information about the transitions inside the workflow.  *  `transitions.rules` For each workflow transition, returns information about its rules. Transitions are included automatically if this expand is requested.  *  `transitions.properties` For each workflow transition, returns information about its properties. Transitions are included automatically if this expand is requested.  *  `statuses` For each workflow, returns information about the statuses inside the workflow.  *  `statuses.properties` For each workflow status, returns information about its properties. Statuses are included automatically if this expand is requested.  *  `default` For each workflow, returns information about whether this is the default workflow.  *  `schemes` For each workflow, returns information about the workflow schemes the workflow is assigned to.  *  `projects` For each workflow, returns information about the projects the workflow is assigned to, through workflow schemes.  *  `hasDraftWorkflow` For each workflow, returns information about whether the workflow has a draft version.  *  `operations` For each workflow, returns information about the actions that can be undertaken on the workflow.",
        ),
        query_string: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with workflow name.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `name` Sorts by workflow name.  *  `created` Sorts by create time.  *  `updated` Sorts by update time.",
        ),
        is_active: bool | None = Field(
            None, description="Filters active and inactive workflows."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflows paginated"""
        api = get_api()
        response = api.jira_cloud_get_workflows_paginated(
            start_at=start_at,
            max_results=max_results,
            workflow_name=workflow_name,
            expand=expand,
            query_string=query_string,
            order_by=order_by,
            is_active=is_active,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_inactive_workflow", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_delete_inactive_workflow(
        entity_id: str = Field(..., description="The entity ID of the workflow."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete inactive workflow"""
        api = get_api()
        response = api.jira_cloud_delete_inactive_workflow(
            entity_id=entity_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_scheme_usages_for_workflow",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_get_workflow_scheme_usages_for_workflow(
        workflow_id: str = Field(..., description="The workflow ID"),
        next_page_token: str | None = Field(
            None, description="The cursor for pagination"
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of results to return. Must be an integer between 1 and 200.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow schemes which are using a given workflow"""
        api = get_api()
        response = api.jira_cloud_get_workflow_scheme_usages_for_workflow(
            workflow_id=workflow_id,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_read_workflows", tags={"jira-cloud-schema-workflow"})
    def jira_cloud_read_workflows(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk get workflows"""
        api = get_api()
        response = api.jira_cloud_read_workflows(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_workflow_capabilities", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_workflow_capabilities(
        workflow_id: str | None = Field(None, description="Parameter workflowId"),
        project_id: str | None = Field(None, description="Parameter projectId"),
        issue_type_id: str | None = Field(None, description="Parameter issueTypeId"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available workflow capabilities"""
        api = get_api()
        response = api.jira_cloud_workflow_capabilities(
            workflow_id=workflow_id,
            project_id=project_id,
            issue_type_id=issue_type_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_workflows", tags={"jira-cloud-schema-workflow"})
    def jira_cloud_create_workflows(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk create workflows"""
        api = get_api()
        response = api.jira_cloud_create_workflows(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_validate_create_workflows", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_validate_create_workflows(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Validate create workflows"""
        api = get_api()
        response = api.jira_cloud_validate_create_workflows(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_read_workflow_previews", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_read_workflow_previews(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Preview workflow"""
        api = get_api()
        response = api.jira_cloud_read_workflow_previews(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_search_workflows", tags={"jira-cloud-schema-workflow"})
    def jira_cloud_search_workflows(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `values.transitions` Returns the transitions that each workflow is associated with.",
        ),
        query_string: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with workflow name.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `name` Sorts by workflow name.  *  `created` Sorts by create time.  *  `updated` Sorts by update time.",
        ),
        scope: str | None = Field(
            None,
            description="The scope of the workflow. Global for company-managed projects and Project for team-managed projects.",
        ),
        is_active: bool | None = Field(
            None, description="Filters active and inactive workflows."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search workflows"""
        api = get_api()
        response = api.jira_cloud_search_workflows(
            start_at=start_at,
            max_results=max_results,
            expand=expand,
            query_string=query_string,
            order_by=order_by,
            scope=scope,
            is_active=is_active,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_workflows", tags={"jira-cloud-schema-workflow"})
    def jira_cloud_update_workflows(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk update workflows"""
        api = get_api()
        response = api.jira_cloud_update_workflows(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_validate_update_workflows", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_validate_update_workflows(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Validate update workflows"""
        api = get_api()
        response = api.jira_cloud_validate_update_workflows(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_workflow_schemes",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_get_all_workflow_schemes(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all workflow schemes"""
        api = get_api()
        response = api.jira_cloud_get_all_workflow_schemes(
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_workflow_scheme",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_create_workflow_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create workflow scheme"""
        api = get_api()
        response = api.jira_cloud_create_workflow_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_read_workflow_schemes",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_read_workflow_schemes(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk get workflow schemes"""
        api = get_api()
        response = api.jira_cloud_read_workflow_schemes(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_schemes", tags={"jira-cloud-schema-other"})
    def jira_cloud_update_schemes(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update workflow scheme"""
        api = get_api()
        response = api.jira_cloud_update_schemes(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_required_workflow_scheme_mappings",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_get_required_workflow_scheme_mappings(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get required status mappings for workflow scheme update"""
        api = get_api()
        response = api.jira_cloud_get_required_workflow_scheme_mappings(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_workflow_scheme",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_delete_workflow_scheme(
        id_: int = Field(
            ...,
            description="The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as `schemeId`. For example, *schemeId=10301*.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete workflow scheme"""
        api = get_api()
        response = api.jira_cloud_delete_workflow_scheme(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_scheme",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_get_workflow_scheme(
        id_: int = Field(
            ...,
            description="The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as `schemeId`. For example, *schemeId=10301*.",
        ),
        return_draft_if_exists: bool | None = Field(
            None,
            description="Returns the workflow scheme's draft rather than scheme itself, if set to true. If the workflow scheme does not have a draft, then the workflow scheme is returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow scheme"""
        api = get_api()
        response = api.jira_cloud_get_workflow_scheme(
            id_=id_,
            return_draft_if_exists=return_draft_if_exists,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_workflow_scheme",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_update_workflow_scheme(
        id_: int = Field(
            ...,
            description="The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as `schemeId`. For example, *schemeId=10301*.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Classic update workflow scheme"""
        api = get_api()
        response = api.jira_cloud_update_workflow_scheme(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_workflow_scheme_draft_from_parent",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_create_workflow_scheme_draft_from_parent(
        id_: int = Field(
            ...,
            description="The ID of the active workflow scheme that the draft is created from.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_create_workflow_scheme_draft_from_parent(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_default_workflow", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_delete_default_workflow(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        update_draft_if_needed: bool | None = Field(
            None,
            description="Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to `false`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete default workflow"""
        api = get_api()
        response = api.jira_cloud_delete_default_workflow(
            id_=id_,
            update_draft_if_needed=update_draft_if_needed,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_default_workflow", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_get_default_workflow(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        return_draft_if_exists: bool | None = Field(
            None,
            description="Set to `true` to return the default workflow for the workflow scheme's draft rather than scheme itself. If the workflow scheme does not have a draft, then the default workflow for the workflow scheme is returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get default workflow"""
        api = get_api()
        response = api.jira_cloud_get_default_workflow(
            id_=id_,
            return_draft_if_exists=return_draft_if_exists,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_default_workflow", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_update_default_workflow(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update default workflow"""
        api = get_api()
        response = api.jira_cloud_update_default_workflow(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_workflow_scheme_draft",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_delete_workflow_scheme_draft(
        id_: int = Field(
            ...,
            description="The ID of the active workflow scheme that the draft was created from.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_delete_workflow_scheme_draft(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_scheme_draft",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_get_workflow_scheme_draft(
        id_: int = Field(
            ...,
            description="The ID of the active workflow scheme that the draft was created from.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_get_workflow_scheme_draft(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_workflow_scheme_draft",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_update_workflow_scheme_draft(
        id_: int = Field(
            ...,
            description="The ID of the active workflow scheme that the draft was created from.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_update_workflow_scheme_draft(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_draft_default_workflow",
        tags={"jira-cloud-schema-workflow"},
    )
    def jira_cloud_delete_draft_default_workflow(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete draft default workflow"""
        api = get_api()
        response = api.jira_cloud_delete_draft_default_workflow(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_draft_default_workflow",
        tags={"jira-cloud-schema-workflow"},
    )
    def jira_cloud_get_draft_default_workflow(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get draft default workflow"""
        api = get_api()
        response = api.jira_cloud_get_draft_default_workflow(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_draft_default_workflow",
        tags={"jira-cloud-schema-workflow"},
    )
    def jira_cloud_update_draft_default_workflow(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update draft default workflow"""
        api = get_api()
        response = api.jira_cloud_update_draft_default_workflow(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_publish_draft_workflow_scheme",
        tags={"jira-cloud-schema-workflow-scheme"},
    )
    def jira_cloud_publish_draft_workflow_scheme(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        validate_only: bool | None = Field(
            None, description="Whether the request only performs a validation."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Publish draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_publish_draft_workflow_scheme(
            id_=id_,
            validate_only=validate_only,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_draft_workflow_mapping",
        tags={"jira-cloud-schema-workflow"},
    )
    def jira_cloud_delete_draft_workflow_mapping(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        workflow_name: str = Field(..., description="The name of the workflow."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue types for workflow in draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_delete_draft_workflow_mapping(
            id_=id_,
            workflow_name=workflow_name,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_draft_workflow", tags={"jira-cloud-schema-workflow"})
    def jira_cloud_get_draft_workflow(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        workflow_name: str | None = Field(
            None,
            description="The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue types for workflows in draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_get_draft_workflow(
            id_=id_,
            workflow_name=workflow_name,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_draft_workflow_mapping",
        tags={"jira-cloud-schema-workflow"},
    )
    def jira_cloud_update_draft_workflow_mapping(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        workflow_name: str = Field(..., description="The name of the workflow."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set issue types for workflow in workflow scheme"""
        api = get_api()
        response = api.jira_cloud_update_draft_workflow_mapping(
            id_=id_,
            workflow_name=workflow_name,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_workflow_mapping", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_delete_workflow_mapping(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        workflow_name: str = Field(..., description="The name of the workflow."),
        update_draft_if_needed: bool | None = Field(
            None,
            description="Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to `false`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue types for workflow in workflow scheme"""
        api = get_api()
        response = api.jira_cloud_delete_workflow_mapping(
            id_=id_,
            workflow_name=workflow_name,
            update_draft_if_needed=update_draft_if_needed,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_workflow", tags={"jira-cloud-schema-workflow"})
    def jira_cloud_get_workflow(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        workflow_name: str | None = Field(
            None,
            description="The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.",
        ),
        return_draft_if_exists: bool | None = Field(
            None,
            description="Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue types for workflows in workflow scheme"""
        api = get_api()
        response = api.jira_cloud_get_workflow(
            id_=id_,
            workflow_name=workflow_name,
            return_draft_if_exists=return_draft_if_exists,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_workflow_mapping", tags={"jira-cloud-schema-workflow"}
    )
    def jira_cloud_update_workflow_mapping(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        workflow_name: str = Field(..., description="The name of the workflow."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set issue types for workflow in workflow scheme"""
        api = get_api()
        response = api.jira_cloud_update_workflow_mapping(
            id_=id_,
            workflow_name=workflow_name,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_migration_resource_workflow_rule_search_post",
        tags={"jira-cloud-schema-workflow-rule"},
    )
    def jira_cloud_migration_resource_workflow_rule_search_post(
        atlassian_transfer_id: str = Field(
            ..., description="The app migration transfer ID."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow transition rule configurations"""
        api = get_api()
        response = api.jira_cloud_migration_resource_workflow_rule_search_post(
            atlassian_transfer_id=atlassian_transfer_id,
            payload=payload,
        )
        return response.model_dump()
