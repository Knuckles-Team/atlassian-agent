# Generated MCP Tools for JiraCloud - other
from typing import Any, Dict, List, Optional
from pydantic import Field
from fastmcp import FastMCP, Context
from ..api.jira_cloud_api import JiraCloudAPI
from ..auth import get_base_client


def get_api() -> JiraCloudAPI:
    return JiraCloudAPI(get_base_client())


def register_jira_other_tools(mcp: FastMCP):
    @mcp.tool(
        name="jira_cloud_remove_field_association_scheme_item_parameters",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_remove_field_association_scheme_item_parameters(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove field parameters"""
        api = get_api()
        response = api.jira_cloud_remove_field_association_scheme_item_parameters(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_field_association_scheme_item_parameters",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_update_field_association_scheme_item_parameters(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update field parameters"""
        api = get_api()
        response = api.jira_cloud_update_field_association_scheme_item_parameters(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_associate_projects_to_field_association_schemes",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_associate_projects_to_field_association_schemes(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Associate projects to field schemes"""
        api = get_api()
        response = api.jira_cloud_associate_projects_to_field_association_schemes(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_selected_time_tracking_implementation",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_get_selected_time_tracking_implementation(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get selected time tracking provider"""
        api = get_api()
        response = api.jira_cloud_get_selected_time_tracking_implementation()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_select_time_tracking_implementation", tags={"jira-cloud-other"}
    )
    def jira_cloud_select_time_tracking_implementation(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Select time tracking provider"""
        api = get_api()
        response = api.jira_cloud_select_time_tracking_implementation(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_available_time_tracking_implementations",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_get_available_time_tracking_implementations(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all time tracking providers"""
        api = get_api()
        response = api.jira_cloud_get_available_time_tracking_implementations()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_gadgets", tags={"jira-cloud-other"})
    def jira_cloud_get_all_gadgets(
        dashboard_id: int = Field(..., description="The ID of the dashboard."),
        module_key: Optional[List[Any]] = Field(
            None,
            description="The list of gadgets module keys. To include multiple module keys, separate module keys with ampersand: `moduleKey=key:one&moduleKey=key:two`.",
        ),
        uri: Optional[List[Any]] = Field(
            None,
            description="The list of gadgets URIs. To include multiple URIs, separate URIs with ampersand: `uri=/rest/example/uri/1&uri=/rest/example/uri/2`.",
        ),
        gadget_id: Optional[List[Any]] = Field(
            None,
            description="The list of gadgets IDs. To include multiple IDs, separate IDs with ampersand: `gadgetId=10000&gadgetId=10001`.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get gadgets"""
        api = get_api()
        response = api.jira_cloud_get_all_gadgets(
            dashboard_id=dashboard_id,
            module_key=module_key,
            uri=uri,
            gadget_id=gadget_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_gadget", tags={"jira-cloud-other"})
    def jira_cloud_add_gadget(
        dashboard_id: int = Field(..., description="The ID of the dashboard."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Add gadget to dashboard"""
        api = get_api()
        response = api.jira_cloud_add_gadget(
            dashboard_id=dashboard_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_gadget", tags={"jira-cloud-other"})
    def jira_cloud_remove_gadget(
        dashboard_id: int = Field(..., description="The ID of the dashboard."),
        gadget_id: int = Field(..., description="The ID of the gadget."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove gadget from dashboard"""
        api = get_api()
        response = api.jira_cloud_remove_gadget(
            dashboard_id=dashboard_id,
            gadget_id=gadget_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_gadget", tags={"jira-cloud-other"})
    def jira_cloud_update_gadget(
        dashboard_id: int = Field(..., description="The ID of the dashboard."),
        gadget_id: int = Field(..., description="The ID of the gadget."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update gadget on dashboard"""
        api = get_api()
        response = api.jira_cloud_update_gadget(
            dashboard_id=dashboard_id,
            gadget_id=gadget_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_policy", tags={"jira-cloud-other"})
    def jira_cloud_get_policy(_ctx: Optional[Context] = None) -> Dict[str, Any]:
        """Get data policy for the workspace"""
        api = get_api()
        response = api.jira_cloud_get_policy()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_policies", tags={"jira-cloud-other"})
    def jira_cloud_get_policies(
        ids: Optional[str] = Field(
            None,
            description="A list of project identifiers. This parameter accepts a comma-separated list.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get data policy for projects"""
        api = get_api()
        response = api.jira_cloud_get_policies(
            ids=ids,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_events", tags={"jira-cloud-other"})
    def jira_cloud_get_events(_ctx: Optional[Context] = None) -> Dict[str, Any]:
        """Get events"""
        api = get_api()
        response = api.jira_cloud_get_events()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_analyse_expression", tags={"jira-cloud-other"})
    def jira_cloud_analyse_expression(
        check: Optional[str] = Field(
            None,
            description="The check to perform:   *  `syntax` Each expression's syntax is checked to ensure the expression can be parsed. Also, syntactic limits are validated. For example, the expression's length.  *  `type` EXPERIMENTAL. Each expression is type checked and the final type of the expression inferred. Any type errors that would result in the expression failure at runtime are reported. For example, accessing properties that don't exist or passing the wrong number of arguments to functions. Also performs the syntax check.  *  `complexity` EXPERIMENTAL. Determines the formulae for how many [expensive operations](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#expensive-operations) each expression may execute.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Analyse Jira expression"""
        api = get_api()
        response = api.jira_cloud_analyse_expression(
            check=check,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_evaluate_jira_expression", tags={"jira-cloud-other"})
    def jira_cloud_evaluate_jira_expression(
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts `meta.complexity` that returns information about the expression complexity. For example, the number of expensive operations used by the expression and how close the expression is to reaching the [complexity limit](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions). Useful when designing and debugging your expressions.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Currently being removed. Evaluate Jira expression"""
        api = get_api()
        response = api.jira_cloud_evaluate_jira_expression(
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_evaluate_jsis_jira_expression", tags={"jira-cloud-other"}
    )
    def jira_cloud_evaluate_jsis_jira_expression(
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts `meta.complexity` that returns information about the expression complexity. For example, the number of expensive operations used by the expression and how close the expression is to reaching the [complexity limit](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions). Useful when designing and debugging your expressions.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Evaluate Jira expression using enhanced search API"""
        api = get_api()
        response = api.jira_cloud_evaluate_jsis_jira_expression(
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_associations", tags={"jira-cloud-other"})
    def jira_cloud_remove_associations(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove associations"""
        api = get_api()
        response = api.jira_cloud_remove_associations(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_associations", tags={"jira-cloud-other"})
    def jira_cloud_create_associations(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create associations"""
        api = get_api()
        response = api.jira_cloud_create_associations(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_default_values", tags={"jira-cloud-other"})
    def jira_cloud_get_default_values(
        field_id: str = Field(
            ...,
            description="The ID of the custom field, for example `customfield\\_10000`.",
        ),
        context_id: Optional[List[Any]] = Field(
            None, description="The IDs of the contexts."
        ),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get custom field contexts default values"""
        api = get_api()
        response = api.jira_cloud_get_default_values(
            field_id=field_id,
            context_id=context_id,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_default_values", tags={"jira-cloud-other"})
    def jira_cloud_set_default_values(
        field_id: str = Field(..., description="The ID of the custom field."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set custom field contexts default values"""
        api = get_api()
        response = api.jira_cloud_set_default_values(
            field_id=field_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_custom_field_contexts_for_projects_and_issue_types",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_get_custom_field_contexts_for_projects_and_issue_types(
        field_id: str = Field(..., description="The ID of the custom field."),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get custom field contexts for projects and issue types"""
        api = get_api()
        response = (
            api.jira_cloud_get_custom_field_contexts_for_projects_and_issue_types(
                field_id=field_id,
                start_at=start_at,
                max_results=max_results,
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_options_for_context", tags={"jira-cloud-other"})
    def jira_cloud_get_options_for_context(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        option_id: Optional[int] = Field(None, description="The ID of the option."),
        only_options: Optional[bool] = Field(
            None, description="Whether only options are returned."
        ),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get custom field options (context)"""
        api = get_api()
        response = api.jira_cloud_get_options_for_context(
            field_id=field_id,
            context_id=context_id,
            option_id=option_id,
            only_options=only_options,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_field_configuration_scheme_project_mapping",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_get_field_configuration_scheme_project_mapping(
        project_id: List[Any] = Field(
            ...,
            description="The list of project IDs. To include multiple projects, separate IDs with ampersand: `projectId=10000&projectId=10001`.",
        ),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get field configuration schemes for projects"""
        api = get_api()
        response = api.jira_cloud_get_field_configuration_scheme_project_mapping(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_issue_types_from_global_field_configuration_scheme",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_remove_issue_types_from_global_field_configuration_scheme(
        id_: int = Field(..., description="The ID of the field configuration scheme."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove issue types from field configuration scheme"""
        api = get_api()
        response = (
            api.jira_cloud_remove_issue_types_from_global_field_configuration_scheme(
                id_=id_,
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_default_share_scope", tags={"jira-cloud-other"})
    def jira_cloud_get_default_share_scope(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get default share scope"""
        api = get_api()
        response = api.jira_cloud_get_default_share_scope()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_default_share_scope", tags={"jira-cloud-other"})
    def jira_cloud_set_default_share_scope(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set default share scope"""
        api = get_api()
        response = api.jira_cloud_set_default_share_scope(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_reset_columns", tags={"jira-cloud-other"})
    def jira_cloud_reset_columns(
        id_: int = Field(..., description="The ID of the filter."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Reset columns"""
        api = get_api()
        response = api.jira_cloud_reset_columns(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_columns", tags={"jira-cloud-other"})
    def jira_cloud_get_columns(
        id_: int = Field(..., description="The ID of the filter."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get columns"""
        api = get_api()
        response = api.jira_cloud_get_columns(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_columns", tags={"jira-cloud-other"})
    def jira_cloud_set_columns(
        id_: int = Field(..., description="The ID of the filter."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set columns"""
        api = get_api()
        response = api.jira_cloud_set_columns(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_license", tags={"jira-cloud-other"})
    def jira_cloud_get_license(_ctx: Optional[Context] = None) -> Dict[str, Any]:
        """Get license"""
        api = get_api()
        response = api.jira_cloud_get_license()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_change_logs", tags={"jira-cloud-other"})
    def jira_cloud_get_change_logs(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get changelogs"""
        api = get_api()
        response = api.jira_cloud_get_change_logs(
            issue_id_or_key=issue_id_or_key,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_change_logs_by_ids", tags={"jira-cloud-other"})
    def jira_cloud_get_change_logs_by_ids(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get changelogs by IDs"""
        api = get_api()
        response = api.jira_cloud_get_change_logs_by_ids(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_notify", tags={"jira-cloud-other"})
    def jira_cloud_notify(
        issue_id_or_key: str = Field(
            ..., description="ID or key of the issue that the notification is sent for."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Send notification for issue"""
        api = get_api()
        response = api.jira_cloud_notify(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_vote", tags={"jira-cloud-other"})
    def jira_cloud_remove_vote(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete vote"""
        api = get_api()
        response = api.jira_cloud_remove_vote(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_votes", tags={"jira-cloud-other"})
    def jira_cloud_get_votes(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get votes"""
        api = get_api()
        response = api.jira_cloud_get_votes(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_vote", tags={"jira-cloud-other"})
    def jira_cloud_add_vote(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Add vote"""
        api = get_api()
        response = api.jira_cloud_add_vote(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_security_levels", tags={"jira-cloud-other"})
    def jira_cloud_get_security_levels(
        start_at: Optional[str] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[str] = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: Optional[List[Any]] = Field(
            None,
            description="The list of issue security scheme level IDs. To include multiple issue security levels, separate IDs with an ampersand: `id=10000&id=10001`.",
        ),
        scheme_id: Optional[List[Any]] = Field(
            None,
            description="The list of issue security scheme IDs. To include multiple issue security schemes, separate IDs with an ampersand: `schemeId=10000&schemeId=10001`.",
        ),
        only_default: Optional[bool] = Field(
            None,
            description="When set to true, returns multiple default levels for each security scheme containing a default. If you provide scheme and level IDs not associated with the default, returns an empty page. The default value is false.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get issue security levels"""
        api = get_api()
        response = api.jira_cloud_get_security_levels(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            scheme_id=scheme_id,
            only_default=only_default,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_default_levels", tags={"jira-cloud-other"})
    def jira_cloud_set_default_levels(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set default issue security levels"""
        api = get_api()
        response = api.jira_cloud_set_default_levels(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_security_level_members", tags={"jira-cloud-other"})
    def jira_cloud_get_security_level_members(
        start_at: Optional[str] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[str] = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: Optional[List[Any]] = Field(
            None,
            description="The list of issue security level member IDs. To include multiple issue security level members separate IDs with an ampersand: `id=10000&id=10001`.",
        ),
        scheme_id: Optional[List[Any]] = Field(
            None,
            description="The list of issue security scheme IDs. To include multiple issue security schemes separate IDs with an ampersand: `schemeId=10000&schemeId=10001`.",
        ),
        level_id: Optional[List[Any]] = Field(
            None,
            description="The list of issue security level IDs. To include multiple issue security levels separate IDs with an ampersand: `levelId=10000&levelId=10001`.",
        ),
        expand: Optional[str] = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `all` Returns all expandable information  *  `field` Returns information about the custom field granted the permission  *  `group` Returns information about the group that is granted the permission  *  `projectRole` Returns information about the project role granted the permission  *  `user` Returns information about the user who is granted the permission",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get issue security level members"""
        api = get_api()
        response = api.jira_cloud_get_security_level_members(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            scheme_id=scheme_id,
            level_id=level_id,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_security_level", tags={"jira-cloud-other"})
    def jira_cloud_add_security_level(
        scheme_id: str = Field(..., description="The ID of the issue security scheme."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Add issue security levels"""
        api = get_api()
        response = api.jira_cloud_add_security_level(
            scheme_id=scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_level", tags={"jira-cloud-other"})
    def jira_cloud_remove_level(
        scheme_id: str = Field(..., description="The ID of the issue security scheme."),
        level_id: str = Field(
            ..., description="The ID of the issue security level to remove."
        ),
        replace_with: Optional[str] = Field(
            None,
            description="The ID of the issue security level that will replace the currently selected level.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove issue security level"""
        api = get_api()
        response = api.jira_cloud_remove_level(
            scheme_id=scheme_id,
            level_id=level_id,
            replace_with=replace_with,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_security_level", tags={"jira-cloud-other"})
    def jira_cloud_update_security_level(
        scheme_id: str = Field(
            ..., description="The ID of the issue security scheme level belongs to."
        ),
        level_id: str = Field(
            ..., description="The ID of the issue security level to update."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update issue security level"""
        api = get_api()
        response = api.jira_cloud_update_security_level(
            scheme_id=scheme_id,
            level_id=level_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_security_level_members", tags={"jira-cloud-other"})
    def jira_cloud_add_security_level_members(
        scheme_id: str = Field(..., description="The ID of the issue security scheme."),
        level_id: str = Field(..., description="The ID of the issue security level."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Add issue security level members"""
        api = get_api()
        response = api.jira_cloud_add_security_level_members(
            scheme_id=scheme_id,
            level_id=level_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_member_from_security_level", tags={"jira-cloud-other"}
    )
    def jira_cloud_remove_member_from_security_level(
        scheme_id: str = Field(..., description="The ID of the issue security scheme."),
        level_id: str = Field(..., description="The ID of the issue security level."),
        member_id: str = Field(
            ..., description="The ID of the issue security level member to be removed."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove member from issue security level"""
        api = get_api()
        response = api.jira_cloud_remove_member_from_security_level(
            scheme_id=scheme_id,
            level_id=level_id,
            member_id=member_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_type_screen_scheme_project_associations",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_get_issue_type_screen_scheme_project_associations(
        project_id: List[Any] = Field(
            ...,
            description="The list of project IDs. To include multiple projects, separate IDs with ampersand: `projectId=10000&projectId=10001`.",
        ),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get issue type screen schemes for projects"""
        api = get_api()
        response = api.jira_cloud_get_issue_type_screen_scheme_project_associations(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_mappings_from_issue_type_screen_scheme",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_remove_mappings_from_issue_type_screen_scheme(
        issue_type_screen_scheme_id: str = Field(
            ..., description="The ID of the issue type screen scheme."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove mappings from issue type screen scheme"""
        api = get_api()
        response = api.jira_cloud_remove_mappings_from_issue_type_screen_scheme(
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_auto_complete", tags={"jira-cloud-other"})
    def jira_cloud_get_auto_complete(_ctx: Optional[Context] = None) -> Dict[str, Any]:
        """Get field reference data (GET)"""
        api = get_api()
        response = api.jira_cloud_get_auto_complete()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_auto_complete_post", tags={"jira-cloud-other"})
    def jira_cloud_get_auto_complete_post(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get field reference data (POST)"""
        api = get_api()
        response = api.jira_cloud_get_auto_complete_post(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_precomputations", tags={"jira-cloud-other"})
    def jira_cloud_get_precomputations(
        function_key: Optional[List[Any]] = Field(
            None,
            description="The function key in format:   *  Forge: `ari:cloud:ecosystem::extension/[App ID]/[Environment ID]/static/[Function key from manifest]`  *  Connect: `[App key]__[Module key]`",
        ),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        order_by: Optional[str] = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `functionKey` Sorts by the functionKey.  *  `used` Sorts by the used timestamp.  *  `created` Sorts by the created timestamp.  *  `updated` Sorts by the updated timestamp.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get precomputations (apps)"""
        api = get_api()
        response = api.jira_cloud_get_precomputations(
            function_key=function_key,
            start_at=start_at,
            max_results=max_results,
            order_by=order_by,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_precomputations", tags={"jira-cloud-other"})
    def jira_cloud_update_precomputations(
        skip_not_found_precomputations: Optional[bool] = Field(
            None, description="Parameter skipNotFoundPrecomputations"
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update precomputations (apps)"""
        api = get_api()
        response = api.jira_cloud_update_precomputations(
            skip_not_found_precomputations=skip_not_found_precomputations,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_precomputations_by_id", tags={"jira-cloud-other"})
    def jira_cloud_get_precomputations_by_id(
        order_by: Optional[str] = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `functionKey` Sorts by the functionKey.  *  `used` Sorts by the used timestamp.  *  `created` Sorts by the created timestamp.  *  `updated` Sorts by the updated timestamp.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get precomputations by ID (apps)"""
        api = get_api()
        response = api.jira_cloud_get_precomputations_by_id(
            order_by=order_by,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_migrate_queries", tags={"jira-cloud-other"})
    def jira_cloud_migrate_queries(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Convert user identifiers to account IDs in JQL queries"""
        api = get_api()
        response = api.jira_cloud_migrate_queries(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_labels", tags={"jira-cloud-other"})
    def jira_cloud_get_all_labels(
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all labels"""
        api = get_api()
        response = api.jira_cloud_get_all_labels(
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_approximate_license_count", tags={"jira-cloud-other"}
    )
    def jira_cloud_get_approximate_license_count(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get approximate license count"""
        api = get_api()
        response = api.jira_cloud_get_approximate_license_count()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_approximate_application_license_count",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_get_approximate_application_license_count(
        application_key: str = Field(
            ...,
            description="The ID of the application, represents a specific version of Jira.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get approximate application license count"""
        api = get_api()
        response = api.jira_cloud_get_approximate_application_license_count(
            application_key=application_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_preference", tags={"jira-cloud-other"})
    def jira_cloud_remove_preference(
        key: str = Field(..., description="The key of the preference."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete preference"""
        api = get_api()
        response = api.jira_cloud_remove_preference(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_preference", tags={"jira-cloud-other"})
    def jira_cloud_get_preference(
        key: str = Field(..., description="The key of the preference."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get preference"""
        api = get_api()
        response = api.jira_cloud_get_preference(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_preference", tags={"jira-cloud-other"})
    def jira_cloud_set_preference(
        key: str = Field(
            ...,
            description="The key of the preference. The maximum length is 255 characters.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set preference"""
        api = get_api()
        response = api.jira_cloud_set_preference(
            key=key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_locale", tags={"jira-cloud-other"})
    def jira_cloud_get_locale(_ctx: Optional[Context] = None) -> Dict[str, Any]:
        """Get locale"""
        api = get_api()
        response = api.jira_cloud_get_locale()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_locale", tags={"jira-cloud-other"})
    def jira_cloud_set_locale(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set locale"""
        api = get_api()
        response = api.jira_cloud_set_locale(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_notifications", tags={"jira-cloud-other"})
    def jira_cloud_add_notifications(
        id_: str = Field(..., description="The ID of the notification scheme."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Add notifications to notification scheme"""
        api = get_api()
        response = api.jira_cloud_add_notifications(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_plans", tags={"jira-cloud-other"})
    def jira_cloud_get_plans(
        include_trashed: Optional[bool] = Field(
            None, description="Whether to include trashed plans in the results."
        ),
        include_archived: Optional[bool] = Field(
            None, description="Whether to include archived plans in the results."
        ),
        cursor: Optional[str] = Field(
            None,
            description="The cursor to start from. If not provided, the first page will be returned.",
        ),
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of plans to return per page. The maximum value is 50. The default value is 50.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get plans paginated"""
        api = get_api()
        response = api.jira_cloud_get_plans(
            include_trashed=include_trashed,
            include_archived=include_archived,
            cursor=cursor,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_plan", tags={"jira-cloud-other"})
    def jira_cloud_create_plan(
        use_group_id: Optional[bool] = Field(
            None,
            description="Whether to accept group IDs instead of group names. Group names are deprecated.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create plan"""
        api = get_api()
        response = api.jira_cloud_create_plan(
            use_group_id=use_group_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_plan", tags={"jira-cloud-other"})
    def jira_cloud_get_plan(
        plan_id: int = Field(..., description="The ID of the plan."),
        use_group_id: Optional[bool] = Field(
            None,
            description="Whether to return group IDs instead of group names. Group names are deprecated.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get plan"""
        api = get_api()
        response = api.jira_cloud_get_plan(
            plan_id=plan_id,
            use_group_id=use_group_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_plan", tags={"jira-cloud-other"})
    def jira_cloud_update_plan(
        plan_id: int = Field(..., description="The ID of the plan."),
        use_group_id: Optional[bool] = Field(
            None,
            description="Whether to accept group IDs instead of group names. Group names are deprecated.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update plan"""
        api = get_api()
        response = api.jira_cloud_update_plan(
            plan_id=plan_id,
            use_group_id=use_group_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_archive_plan", tags={"jira-cloud-other"})
    def jira_cloud_archive_plan(
        plan_id: int = Field(..., description="The ID of the plan."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Archive plan"""
        api = get_api()
        response = api.jira_cloud_archive_plan(
            plan_id=plan_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_duplicate_plan", tags={"jira-cloud-other"})
    def jira_cloud_duplicate_plan(
        plan_id: int = Field(..., description="The ID of the plan."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Duplicate plan"""
        api = get_api()
        response = api.jira_cloud_duplicate_plan(
            plan_id=plan_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_teams", tags={"jira-cloud-other"})
    def jira_cloud_get_teams(
        plan_id: int = Field(..., description="The ID of the plan."),
        cursor: Optional[str] = Field(
            None,
            description="The cursor to start from. If not provided, the first page will be returned.",
        ),
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of plan teams to return per page. The maximum value is 50. The default value is 50.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get teams in plan paginated"""
        api = get_api()
        response = api.jira_cloud_get_teams(
            plan_id=plan_id,
            cursor=cursor,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_atlassian_team", tags={"jira-cloud-other"})
    def jira_cloud_add_atlassian_team(
        plan_id: int = Field(..., description="The ID of the plan."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Add Atlassian team to plan"""
        api = get_api()
        response = api.jira_cloud_add_atlassian_team(
            plan_id=plan_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_atlassian_team", tags={"jira-cloud-other"})
    def jira_cloud_remove_atlassian_team(
        plan_id: int = Field(..., description="The ID of the plan."),
        atlassian_team_id: str = Field(
            ..., description="The ID of the Atlassian team."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove Atlassian team from plan"""
        api = get_api()
        response = api.jira_cloud_remove_atlassian_team(
            plan_id=plan_id,
            atlassian_team_id=atlassian_team_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_atlassian_team", tags={"jira-cloud-other"})
    def jira_cloud_get_atlassian_team(
        plan_id: int = Field(..., description="The ID of the plan."),
        atlassian_team_id: str = Field(
            ..., description="The ID of the Atlassian team."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get Atlassian team in plan"""
        api = get_api()
        response = api.jira_cloud_get_atlassian_team(
            plan_id=plan_id,
            atlassian_team_id=atlassian_team_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_atlassian_team", tags={"jira-cloud-other"})
    def jira_cloud_update_atlassian_team(
        plan_id: int = Field(..., description="The ID of the plan."),
        atlassian_team_id: str = Field(
            ..., description="The ID of the Atlassian team."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update Atlassian team in plan"""
        api = get_api()
        response = api.jira_cloud_update_atlassian_team(
            plan_id=plan_id,
            atlassian_team_id=atlassian_team_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_plan_only_team", tags={"jira-cloud-other"})
    def jira_cloud_create_plan_only_team(
        plan_id: int = Field(..., description="The ID of the plan."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create plan-only team"""
        api = get_api()
        response = api.jira_cloud_create_plan_only_team(
            plan_id=plan_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_plan_only_team", tags={"jira-cloud-other"})
    def jira_cloud_delete_plan_only_team(
        plan_id: int = Field(..., description="The ID of the plan."),
        plan_only_team_id: int = Field(
            ..., description="The ID of the plan-only team."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete plan-only team"""
        api = get_api()
        response = api.jira_cloud_delete_plan_only_team(
            plan_id=plan_id,
            plan_only_team_id=plan_only_team_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_plan_only_team", tags={"jira-cloud-other"})
    def jira_cloud_get_plan_only_team(
        plan_id: int = Field(..., description="The ID of the plan."),
        plan_only_team_id: int = Field(
            ..., description="The ID of the plan-only team."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get plan-only team"""
        api = get_api()
        response = api.jira_cloud_get_plan_only_team(
            plan_id=plan_id,
            plan_only_team_id=plan_only_team_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_plan_only_team", tags={"jira-cloud-other"})
    def jira_cloud_update_plan_only_team(
        plan_id: int = Field(..., description="The ID of the plan."),
        plan_only_team_id: int = Field(
            ..., description="The ID of the plan-only team."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update plan-only team"""
        api = get_api()
        response = api.jira_cloud_update_plan_only_team(
            plan_id=plan_id,
            plan_only_team_id=plan_only_team_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_trash_plan", tags={"jira-cloud-other"})
    def jira_cloud_trash_plan(
        plan_id: int = Field(..., description="The ID of the plan."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Trash plan"""
        api = get_api()
        response = api.jira_cloud_trash_plan(
            plan_id=plan_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_priorities", tags={"jira-cloud-other"})
    def jira_cloud_get_priorities(_ctx: Optional[Context] = None) -> Dict[str, Any]:
        """Get priorities"""
        api = get_api()
        response = api.jira_cloud_get_priorities()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_move_priorities", tags={"jira-cloud-other"})
    def jira_cloud_move_priorities(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Move priorities"""
        api = get_api()
        response = api.jira_cloud_move_priorities(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_search_priorities", tags={"jira-cloud-other"})
    def jira_cloud_search_priorities(
        start_at: Optional[str] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[str] = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: Optional[List[Any]] = Field(
            None,
            description="The list of priority IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=2&id=3`.",
        ),
        project_id: Optional[List[Any]] = Field(
            None,
            description="The list of projects IDs. To include multiple IDs, provide an ampersand-separated list. For example, `projectId=10010&projectId=10111`.",
        ),
        priority_name: Optional[str] = Field(
            None, description="The name of priority to search for."
        ),
        only_default: Optional[bool] = Field(
            None, description="Whether only the default priority is returned."
        ),
        expand: Optional[str] = Field(
            None,
            description="Use `schemes` to return the associated priority schemes for each priority. Limited to returning first 15 priority schemes per priority.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Search priorities"""
        api = get_api()
        response = api.jira_cloud_search_priorities(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            project_id=project_id,
            priority_name=priority_name,
            only_default=only_default,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_suggested_priorities_for_mappings", tags={"jira-cloud-other"}
    )
    def jira_cloud_suggested_priorities_for_mappings(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Suggested priorities for mappings"""
        api = get_api()
        response = api.jira_cloud_suggested_priorities_for_mappings(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_edit_template", tags={"jira-cloud-other"})
    def jira_cloud_edit_template(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Edit a custom project template"""
        api = get_api()
        response = api.jira_cloud_edit_template(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_live_template", tags={"jira-cloud-other"})
    def jira_cloud_live_template(
        project_id: Optional[str] = Field(
            None,
            description="optional - The \\{@link String\\} containing the project key linked to the custom template to retrieve",
        ),
        template_key: Optional[str] = Field(
            None,
            description="optional - The \\{@link String\\} containing the key of the custom template to retrieve",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Gets a custom project template"""
        api = get_api()
        response = api.jira_cloud_live_template(
            project_id=project_id,
            template_key=template_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_template", tags={"jira-cloud-other"})
    def jira_cloud_remove_template(
        template_key: str = Field(
            ...,
            description="The \\{@link String\\} containing the key of the custom template to remove",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Deletes a custom project template"""
        api = get_api()
        response = api.jira_cloud_remove_template(
            template_key=template_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_save_template", tags={"jira-cloud-other"})
    def jira_cloud_save_template(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Save a custom project template"""
        api = get_api()
        response = api.jira_cloud_save_template(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_recent", tags={"jira-cloud-other"})
    def jira_cloud_get_recent(
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:   *  `description` Returns the project description.  *  `projectKeys` Returns all project keys associated with a project.  *  `lead` Returns information about the project lead.  *  `issueTypes` Returns all issue types associated with the project.  *  `url` Returns the URL associated with the project.  *  `permissions` Returns the permissions associated with the project.  *  `insight` EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project.  *  `*` Returns the project with all available expand options.",
        ),
        properties: Optional[List[Any]] = Field(
            None,
            description="EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list. Invalid property names are ignored.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get recent projects"""
        api = get_api()
        response = api.jira_cloud_get_recent(
            expand=expand,
            properties=properties,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_restore", tags={"jira-cloud-other"})
    def jira_cloud_restore(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Restore deleted or archived project"""
        api = get_api()
        response = api.jira_cloud_restore(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_actor", tags={"jira-cloud-other"})
    def jira_cloud_delete_actor(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        user: Optional[str] = Field(
            None,
            description="The user account ID of the user to remove from the project role.",
        ),
        group: Optional[str] = Field(
            None,
            description="The name of the group to remove from the project role. This parameter cannot be used with the `groupId` parameter. As a group's name can change, use of `groupId` is recommended.",
        ),
        group_id: Optional[str] = Field(
            None,
            description="The ID of the group to remove from the project role. This parameter cannot be used with the `group` parameter.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete actors from project role"""
        api = get_api()
        response = api.jira_cloud_delete_actor(
            project_id_or_key=project_id_or_key,
            id_=id_,
            user=user,
            group=group,
            group_id=group_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_actors", tags={"jira-cloud-other"})
    def jira_cloud_set_actors(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set actors for project role"""
        api = get_api()
        response = api.jira_cloud_set_actors(
            project_id_or_key=project_id_or_key,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_hierarchy", tags={"jira-cloud-other"})
    def jira_cloud_get_hierarchy(
        project_id: int = Field(..., description="The ID of the project."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project issue type hierarchy"""
        api = get_api()
        response = api.jira_cloud_get_hierarchy(
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_redact", tags={"jira-cloud-other"})
    def jira_cloud_redact(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Redact"""
        api = get_api()
        response = api.jira_cloud_redact(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_server_info", tags={"jira-cloud-other"})
    def jira_cloud_get_server_info(_ctx: Optional[Context] = None) -> Dict[str, Any]:
        """Get Jira instance info"""
        api = get_api()
        response = api.jira_cloud_get_server_info()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_search", tags={"jira-cloud-other"})
    def jira_cloud_search(
        project_id: Optional[str] = Field(
            None,
            description="The project the status is part of or null for global statuses.",
        ),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        search_string: Optional[str] = Field(
            None,
            description="Term to match status names against or null to search for all statuses in the search scope.",
        ),
        status_category: Optional[str] = Field(
            None,
            description="Category of the status to filter by. The supported values are: `TODO`, `IN_PROGRESS`, and `DONE`.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Search statuses paginated"""
        api = get_api()
        response = api.jira_cloud_search(
            project_id=project_id,
            start_at=start_at,
            max_results=max_results,
            search_string=search_string,
            status_category=status_category,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_task", tags={"jira-cloud-other"})
    def jira_cloud_get_task(
        task_id: str = Field(..., description="The ID of the task."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get task"""
        api = get_api()
        response = api.jira_cloud_get_task(
            task_id=task_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_cancel_task", tags={"jira-cloud-other"})
    def jira_cloud_cancel_task(
        task_id: str = Field(..., description="The ID of the task."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Cancel task"""
        api = get_api()
        response = api.jira_cloud_cancel_task(
            task_id=task_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_ui_modifications", tags={"jira-cloud-other"})
    def jira_cloud_get_ui_modifications(
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        expand: Optional[str] = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `data` Returns UI modification data.  *  `contexts` Returns UI modification contexts.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get UI modifications"""
        api = get_api()
        response = api.jira_cloud_get_ui_modifications(
            start_at=start_at,
            max_results=max_results,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_ui_modification", tags={"jira-cloud-other"})
    def jira_cloud_create_ui_modification(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create UI modification"""
        api = get_api()
        response = api.jira_cloud_create_ui_modification(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_ui_modification", tags={"jira-cloud-other"})
    def jira_cloud_delete_ui_modification(
        ui_modification_id: str = Field(
            ..., description="The ID of the UI modification."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete UI modification"""
        api = get_api()
        response = api.jira_cloud_delete_ui_modification(
            ui_modification_id=ui_modification_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_ui_modification", tags={"jira-cloud-other"})
    def jira_cloud_update_ui_modification(
        ui_modification_id: str = Field(
            ..., description="The ID of the UI modification."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update UI modification"""
        api = get_api()
        response = api.jira_cloud_update_ui_modification(
            ui_modification_id=ui_modification_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_related_work", tags={"jira-cloud-other"})
    def jira_cloud_get_related_work(
        id_: str = Field(..., description="The ID of the version."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get related work"""
        api = get_api()
        response = api.jira_cloud_get_related_work(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_related_work", tags={"jira-cloud-other"})
    def jira_cloud_create_related_work(
        id_: str = Field(..., description="Parameter id"),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create related work"""
        api = get_api()
        response = api.jira_cloud_create_related_work(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_related_work", tags={"jira-cloud-other"})
    def jira_cloud_update_related_work(
        id_: str = Field(
            ...,
            description="The ID of the version to update the related work on. For the related work id, pass it to the input JSON.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update related work"""
        api = get_api()
        response = api.jira_cloud_update_related_work(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_related_work", tags={"jira-cloud-other"})
    def jira_cloud_delete_related_work(
        version_id: str = Field(
            ...,
            description="The ID of the version that the target related work belongs to.",
        ),
        related_work_id: str = Field(
            ..., description="The ID of the related work to delete."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete related work"""
        api = get_api()
        response = api.jira_cloud_delete_related_work(
            version_id=version_id,
            related_work_id=related_work_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_webhook_by_id", tags={"jira-cloud-other"})
    def jira_cloud_delete_webhook_by_id(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete webhooks by ID"""
        api = get_api()
        response = api.jira_cloud_delete_webhook_by_id(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_dynamic_webhooks_for_app", tags={"jira-cloud-other"})
    def jira_cloud_get_dynamic_webhooks_for_app(
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get dynamic webhooks for app"""
        api = get_api()
        response = api.jira_cloud_get_dynamic_webhooks_for_app(
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_register_dynamic_webhooks", tags={"jira-cloud-other"})
    def jira_cloud_register_dynamic_webhooks(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Register dynamic webhooks"""
        api = get_api()
        response = api.jira_cloud_register_dynamic_webhooks(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_failed_webhooks", tags={"jira-cloud-other"})
    def jira_cloud_get_failed_webhooks(
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of webhooks to return per page. If obeying the maxResults directive would result in records with the same failure time being split across pages, the directive is ignored and all records with the same failure time included on the page.",
        ),
        after: Optional[int] = Field(
            None,
            description="The time after which any webhook failure must have occurred for the record to be returned, expressed as milliseconds since the UNIX epoch.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get failed webhooks"""
        api = get_api()
        response = api.jira_cloud_get_failed_webhooks(
            max_results=max_results,
            after=after,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_refresh_webhooks", tags={"jira-cloud-other"})
    def jira_cloud_refresh_webhooks(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Extend webhook life"""
        api = get_api()
        response = api.jira_cloud_refresh_webhooks(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_workflow_transition_rule_configurations",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_update_workflow_transition_rule_configurations(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update workflow transition rule configurations"""
        api = get_api()
        response = api.jira_cloud_update_workflow_transition_rule_configurations(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_workflow_transition_rule_configurations",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_delete_workflow_transition_rule_configurations(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete workflow transition rule configurations"""
        api = get_api()
        response = api.jira_cloud_delete_workflow_transition_rule_configurations(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_default_editor", tags={"jira-cloud-other"})
    def jira_cloud_get_default_editor(_ctx: Optional[Context] = None) -> Dict[str, Any]:
        """Get the user's default workflow editor"""
        api = get_api()
        response = api.jira_cloud_get_default_editor()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_addon_properties_resource_get_addon_properties_get",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_addon_properties_resource_get_addon_properties_get(
        addon_key: str = Field(
            ..., description="The key of the app, as defined in its descriptor."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get app properties"""
        api = get_api()
        response = api.jira_cloud_addon_properties_resource_get_addon_properties_get(
            addon_key=addon_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_addon_properties_resource_delete_addon_property_delete",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_addon_properties_resource_delete_addon_property_delete(
        addon_key: str = Field(
            ..., description="The key of the app, as defined in its descriptor."
        ),
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete app property"""
        api = get_api()
        response = (
            api.jira_cloud_addon_properties_resource_delete_addon_property_delete(
                addon_key=addon_key,
                property_key=property_key,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_addon_properties_resource_get_addon_property_get",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_addon_properties_resource_get_addon_property_get(
        addon_key: str = Field(
            ..., description="The key of the app, as defined in its descriptor."
        ),
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get app property"""
        api = get_api()
        response = api.jira_cloud_addon_properties_resource_get_addon_property_get(
            addon_key=addon_key,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_addon_properties_resource_put_addon_property_put",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_addon_properties_resource_put_addon_property_put(
        addon_key: str = Field(
            ..., description="The key of the app, as defined in its descriptor."
        ),
        property_key: str = Field(..., description="The key of the property."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set app property"""
        api = get_api()
        response = api.jira_cloud_addon_properties_resource_put_addon_property_put(
            addon_key=addon_key,
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_dynamic_modules_resource_remove_modules_delete",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_dynamic_modules_resource_remove_modules_delete(
        module_key: Optional[List[Any]] = Field(
            None,
            description="The key of the module to remove. To include multiple module keys, provide multiple copies of this parameter. For example, `moduleKey=dynamic-attachment-entity-property&moduleKey=dynamic-select-field`. Nonexistent keys are ignored.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove modules"""
        api = get_api()
        response = api.jira_cloud_dynamic_modules_resource_remove_modules_delete(
            module_key=module_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_dynamic_modules_resource_get_modules_get",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_dynamic_modules_resource_get_modules_get(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get modules"""
        api = get_api()
        response = api.jira_cloud_dynamic_modules_resource_get_modules_get()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_dynamic_modules_resource_register_modules_post",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_dynamic_modules_resource_register_modules_post(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Register modules"""
        api = get_api()
        response = api.jira_cloud_dynamic_modules_resource_register_modules_post(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put(
        atlassian_transfer_id: str = Field(..., description="The ID of the transfer."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Bulk update custom field value"""
        api = get_api()
        response = api.jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put(
            atlassian_transfer_id=atlassian_transfer_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_migration_resource_update_entity_properties_value_put",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_migration_resource_update_entity_properties_value_put(
        atlassian_transfer_id: str = Field(
            ..., description="The app migration transfer ID."
        ),
        entity_type: str = Field(
            ...,
            description="The type indicating the object that contains the entity properties.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Bulk update entity properties"""
        api = get_api()
        response = api.jira_cloud_migration_resource_update_entity_properties_value_put(
            atlassian_transfer_id=atlassian_transfer_id,
            entity_type=entity_type,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get(
        connect_key: str = Field(
            ...,
            description="The key of the Connect app that contains the Jira issue field being migrated.",
        ),
        jira_issue_fields_key: str = Field(
            ..., description="The module key of the Connect issue field being migrated."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get Connect issue field migration task"""
        api = get_api()
        response = api.jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get(
            connect_key=connect_key,
            jira_issue_fields_key=jira_issue_fields_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post(
        connect_key: str = Field(
            ...,
            description="The key of the Connect app that contains the Jira issue field being migrated.",
        ),
        jira_issue_fields_key: str = Field(
            ..., description="The module key of the Connect issue field being migrated."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Submit Connect issue field migration task"""
        api = get_api()
        response = api.jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post(
            connect_key=connect_key,
            jira_issue_fields_key=jira_issue_fields_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_service_registry_resource_services_get",
        tags={"jira-cloud-other"},
    )
    def jira_cloud_service_registry_resource_services_get(
        service_ids: List[Any] = Field(
            ...,
            description="The ID of the services (the strings starting with 'b:' need to be decoded in Base64).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Retrieve the attributes of service registries"""
        api = get_api()
        response = api.jira_cloud_service_registry_resource_services_get(
            service_ids=service_ids,
        )
        return response.model_dump()
