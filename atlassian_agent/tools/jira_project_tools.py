# Generated MCP Tools for JiraCloud - project
from typing import Any, Dict, List, Optional
from pydantic import Field
from fastmcp import FastMCP, Context
from ..api.jira_cloud_api import JiraCloudAPI
from ..auth import get_base_client


def get_api() -> JiraCloudAPI:
    return JiraCloudAPI(get_base_client())


def register_jira_project_tools(mcp: FastMCP):
    @mcp.tool(
        name="jira_cloud_find_components_for_projects",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_find_components_for_projects(
        project_ids_or_keys: Optional[List[Any]] = Field(
            None, description="The project IDs and/or project keys (case sensitive)."
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
            description="[Order](#ordering) the results by a field:   *  `description` Sorts by the component description.  *  `name` Sorts by component name.",
        ),
        query: Optional[str] = Field(
            None,
            description="Filter the results using a literal string. Components with a matching `name` or `description` are returned (case insensitive).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Find components for projects"""
        api = get_api()
        response = api.jira_cloud_find_components_for_projects(
            project_ids_or_keys=project_ids_or_keys,
            start_at=start_at,
            max_results=max_results,
            order_by=order_by,
            query=query,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_component", tags={"jira-cloud-project"})
    def jira_cloud_create_component(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create component"""
        api = get_api()
        response = api.jira_cloud_create_component(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_component", tags={"jira-cloud-project"})
    def jira_cloud_delete_component(
        id_: str = Field(..., description="The ID of the component."),
        move_issues_to: Optional[str] = Field(
            None,
            description="The ID of the component to replace the deleted component. If this value is null no replacement is made.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete component"""
        api = get_api()
        response = api.jira_cloud_delete_component(
            id_=id_,
            move_issues_to=move_issues_to,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_component", tags={"jira-cloud-project"})
    def jira_cloud_get_component(
        id_: str = Field(..., description="The ID of the component."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get component"""
        api = get_api()
        response = api.jira_cloud_get_component(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_component", tags={"jira-cloud-project"})
    def jira_cloud_update_component(
        id_: str = Field(..., description="The ID of the component."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update component"""
        api = get_api()
        response = api.jira_cloud_update_component(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_projects_with_field_schemes", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_projects_with_field_schemes(
        project_id: List[Any] = Field(
            ..., description="List of project ids to filter the results by."
        ),
        start_at: Optional[int] = Field(
            None,
            description="The starting index of the returned projects. Base index: 0.",
        ),
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of projects to return per page, maximum allowed value is 100.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get projects with field schemes"""
        api = get_api()
        response = api.jira_cloud_get_projects_with_field_schemes(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_field_association_scheme_projects",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_search_field_association_scheme_projects(
        id_: int = Field(
            ..., description="The scheme id to search for associated projects"
        ),
        start_at: Optional[int] = Field(
            None,
            description="The starting index of the returned projects. Base index: 0.",
        ),
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of projects to return per page, maximum allowed value is 100.",
        ),
        project_id: Optional[List[Any]] = Field(
            None,
            description="The project Ids to filter by, if empty then all projects belonging to a field association scheme will be returned",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Search field scheme projects"""
        api = get_api()
        response = api.jira_cloud_search_field_association_scheme_projects(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_field_project_associations", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_field_project_associations(
        field_id: str = Field(
            ..., description="The ID of the field, for example `customfield_10000`."
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
        """Get field project associations"""
        api = get_api()
        response = api.jira_cloud_get_field_project_associations(
            field_id=field_id,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_context_mapping", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_project_context_mapping(
        field_id: str = Field(
            ...,
            description="The ID of the custom field, for example `customfield\\_10000`.",
        ),
        context_id: Optional[List[Any]] = Field(
            None,
            description="The list of context IDs. To include multiple context, separate IDs with ampersand: `contextId=10000&contextId=10001`.",
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
        """Get project mappings for custom field context"""
        api = get_api()
        response = api.jira_cloud_get_project_context_mapping(
            field_id=field_id,
            context_id=context_id,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_assign_projects_to_custom_field_context",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_assign_projects_to_custom_field_context(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Assign custom field context to projects"""
        api = get_api()
        response = api.jira_cloud_assign_projects_to_custom_field_context(
            field_id=field_id,
            context_id=context_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_custom_field_context_from_projects",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_remove_custom_field_context_from_projects(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove custom field context from projects"""
        api = get_api()
        response = api.jira_cloud_remove_custom_field_context_from_projects(
            field_id=field_id,
            context_id=context_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_assign_field_configuration_scheme_to_project",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_assign_field_configuration_scheme_to_project(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Assign field configuration scheme to project"""
        api = get_api()
        response = api.jira_cloud_assign_field_configuration_scheme_to_project(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_projects_using_security_schemes",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_search_projects_using_security_schemes(
        start_at: Optional[str] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[str] = Field(
            None, description="The maximum number of items to return per page."
        ),
        issue_security_scheme_id: Optional[List[Any]] = Field(
            None, description="The list of security scheme IDs to be filtered out."
        ),
        project_id: Optional[List[Any]] = Field(
            None, description="The list of project IDs to be filtered out."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get projects using issue security schemes"""
        api = get_api()
        response = api.jira_cloud_search_projects_using_security_schemes(
            start_at=start_at,
            max_results=max_results,
            issue_security_scheme_id=issue_security_scheme_id,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_associate_schemes_to_projects", tags={"jira-cloud-project"}
    )
    def jira_cloud_associate_schemes_to_projects(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Associate security scheme to project"""
        api = get_api()
        response = api.jira_cloud_associate_schemes_to_projects(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_notification_scheme_to_project_mappings",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_notification_scheme_to_project_mappings(
        start_at: Optional[str] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[str] = Field(
            None, description="The maximum number of items to return per page."
        ),
        notification_scheme_id: Optional[List[Any]] = Field(
            None, description="The list of notifications scheme IDs to be filtered out"
        ),
        project_id: Optional[List[Any]] = Field(
            None, description="The list of project IDs to be filtered out"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get projects using notification schemes paginated"""
        api = get_api()
        response = api.jira_cloud_get_notification_scheme_to_project_mappings(
            start_at=start_at,
            max_results=max_results,
            notification_scheme_id=notification_scheme_id,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_permitted_projects", tags={"jira-cloud-project"})
    def jira_cloud_get_permitted_projects(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get permitted projects"""
        api = get_api()
        response = api.jira_cloud_get_permitted_projects(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_projects_by_priority_scheme", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_projects_by_priority_scheme(
        scheme_id: str = Field(..., description="The priority scheme ID."),
        start_at: Optional[str] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[str] = Field(
            None, description="The maximum number of items to return per page."
        ),
        project_id: Optional[List[Any]] = Field(
            None,
            description="The project IDs to filter by. For example, `projectId=10000&projectId=10001`.",
        ),
        query: Optional[str] = Field(
            None, description="The string to query projects on by name."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get projects by priority scheme"""
        api = get_api()
        response = api.jira_cloud_get_projects_by_priority_scheme(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
            scheme_id=scheme_id,
            query=query,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_projects", tags={"jira-cloud-project"})
    def jira_cloud_get_all_projects(
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:   *  `description` Returns the project description.  *  `issueTypes` Returns all issue types associated with the project.  *  `lead` Returns information about the project lead.  *  `projectKeys` Returns all project keys associated with the project.",
        ),
        recent: Optional[int] = Field(
            None,
            description="Returns the user's most recently accessed projects. You may specify the number of results to return up to a maximum of 20. If access is anonymous, then the recently accessed projects are based on the current HTTP session.",
        ),
        properties: Optional[List[Any]] = Field(
            None,
            description="A list of project properties to return for the project. This parameter accepts a comma-separated list.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all projects"""
        api = get_api()
        response = api.jira_cloud_get_all_projects(
            expand=expand,
            recent=recent,
            properties=properties,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_project", tags={"jira-cloud-project"})
    def jira_cloud_create_project(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create project"""
        api = get_api()
        response = api.jira_cloud_create_project(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_project_with_custom_template",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_create_project_with_custom_template(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create custom project"""
        api = get_api()
        response = api.jira_cloud_create_project_with_custom_template(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_search_projects", tags={"jira-cloud-project"})
    def jira_cloud_search_projects(
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of items to return per page. Must be less than or equal to 100. If a value greater than 100 is provided, the `maxResults` parameter will default to 100.",
        ),
        order_by: Optional[str] = Field(
            None,
            description="[Order](#ordering) the results by a field.   *  `category` Sorts by project category. A complete list of category IDs is found using [Get all project categories](#api-rest-api-3-projectCategory-get).  *  `issueCount` Sorts by the total number of issues in each project.  *  `key` Sorts by project key.  *  `lastIssueUpdatedTime` Sorts by the last issue update time.  *  `name` Sorts by project name.  *  `owner` Sorts by project lead.  *  `archivedDate` EXPERIMENTAL. Sorts by project archived date.  *  `deletedDate` EXPERIMENTAL. Sorts by project deleted date.",
        ),
        id_: Optional[List[Any]] = Field(
            None,
            description="The project IDs to filter the results by. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. Up to 50 project IDs can be provided.",
        ),
        keys: Optional[List[Any]] = Field(
            None,
            description="The project keys to filter the results by. To include multiple keys, provide an ampersand-separated list. For example, `keys=PA&keys=PB`. Up to 50 project keys can be provided.",
        ),
        query: Optional[str] = Field(
            None,
            description="Filter the results using a literal string. Projects with a matching `key` or `name` are returned (case insensitive).",
        ),
        type_key: Optional[str] = Field(
            None,
            description="Orders results by the [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes). This parameter accepts a comma-separated list. Valid values are `business`, `service_desk`, and `software`.",
        ),
        category_id: Optional[int] = Field(
            None,
            description="The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation.",
        ),
        action: Optional[str] = Field(
            None,
            description="Filter results by projects for which the user can:   *  `view` the project, meaning that they have one of the following permissions:           *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.      *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.      *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  `browse` the project, meaning that they have the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  `edit` the project, meaning that they have one of the following permissions:           *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.      *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  `create` the project, meaning that they have the *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue is created.",
        ),
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:   *  `description` Returns the project description.  *  `projectKeys` Returns all project keys associated with a project.  *  `lead` Returns information about the project lead.  *  `issueTypes` Returns all issue types associated with the project.  *  `url` Returns the URL associated with the project.  *  `insight` EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project.",
        ),
        status: Optional[List[Any]] = Field(
            None,
            description="EXPERIMENTAL. Filter results by project status:   *  `live` Search live projects.  *  `archived` Search archived projects.  *  `deleted` Search deleted projects, those in the recycle bin.",
        ),
        properties: Optional[List[Any]] = Field(
            None,
            description="EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list.",
        ),
        property_query: Optional[str] = Field(
            None,
            description="EXPERIMENTAL. A query string used to search properties. The query string cannot be specified using a JSON object. For example, to search for the value of `nested` from `{'something':{'nested':1,'other':2}}` use `[thepropertykey].something.nested=1`. Note that the propertyQuery key is enclosed in square brackets to enable searching where the propertyQuery key includes dot (.) or equals (=) characters. Note that `thepropertykey` is only returned when included in `properties`.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get projects paginated"""
        api = get_api()
        response = api.jira_cloud_search_projects(
            start_at=start_at,
            max_results=max_results,
            order_by=order_by,
            id_=id_,
            keys=keys,
            query=query,
            type_key=type_key,
            category_id=category_id,
            action=action,
            expand=expand,
            status=status,
            properties=properties,
            property_query=property_query,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_project_types", tags={"jira-cloud-project"})
    def jira_cloud_get_all_project_types(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all project types"""
        api = get_api()
        response = api.jira_cloud_get_all_project_types()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_accessible_project_types", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_all_accessible_project_types(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get licensed project types"""
        api = get_api()
        response = api.jira_cloud_get_all_accessible_project_types()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_type_by_key", tags={"jira-cloud-project"})
    def jira_cloud_get_project_type_by_key(
        project_type_key: str = Field(..., description="The key of the project type."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project type by key"""
        api = get_api()
        response = api.jira_cloud_get_project_type_by_key(
            project_type_key=project_type_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_accessible_project_type_by_key",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_accessible_project_type_by_key(
        project_type_key: str = Field(..., description="The key of the project type."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get accessible project type by key"""
        api = get_api()
        response = api.jira_cloud_get_accessible_project_type_by_key(
            project_type_key=project_type_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_project", tags={"jira-cloud-project"})
    def jira_cloud_delete_project(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        enable_undo: Optional[bool] = Field(
            None,
            description="Whether this project is placed in the Jira recycle bin where it will be available for restoration.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete project"""
        api = get_api()
        response = api.jira_cloud_delete_project(
            project_id_or_key=project_id_or_key,
            enable_undo=enable_undo,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project", tags={"jira-cloud-project"})
    def jira_cloud_get_project(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that the project description, issue types, and project lead are included in all responses by default. Expand options include:   *  `description` The project description.  *  `issueTypes` The issue types associated with the project.  *  `lead` The project lead.  *  `projectKeys` All project keys associated with the project.  *  `issueTypeHierarchy` The project issue type hierarchy.",
        ),
        properties: Optional[List[Any]] = Field(
            None,
            description="A list of project properties to return for the project. This parameter accepts a comma-separated list.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project"""
        api = get_api()
        response = api.jira_cloud_get_project(
            project_id_or_key=project_id_or_key,
            expand=expand,
            properties=properties,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_project", tags={"jira-cloud-project"})
    def jira_cloud_update_project(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that the project description, issue types, and project lead are included in all responses by default. Expand options include:   *  `description` The project description.  *  `issueTypes` The issue types associated with the project.  *  `lead` The project lead.  *  `projectKeys` All project keys associated with the project.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update project"""
        api = get_api()
        response = api.jira_cloud_update_project(
            project_id_or_key=project_id_or_key,
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_archive_project", tags={"jira-cloud-project"})
    def jira_cloud_archive_project(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Archive project"""
        api = get_api()
        response = api.jira_cloud_archive_project(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_project_avatar", tags={"jira-cloud-project"})
    def jira_cloud_update_project_avatar(
        project_id_or_key: str = Field(
            ..., description="The ID or (case-sensitive) key of the project."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set project avatar"""
        api = get_api()
        response = api.jira_cloud_update_project_avatar(
            project_id_or_key=project_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_project_avatar", tags={"jira-cloud-project"})
    def jira_cloud_delete_project_avatar(
        project_id_or_key: str = Field(
            ..., description="The project ID or (case-sensitive) key."
        ),
        id_: int = Field(..., description="The ID of the avatar."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete project avatar"""
        api = get_api()
        response = api.jira_cloud_delete_project_avatar(
            project_id_or_key=project_id_or_key,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_project_avatar", tags={"jira-cloud-project"})
    def jira_cloud_create_project_avatar(
        project_id_or_key: str = Field(
            ..., description="The ID or (case-sensitive) key of the project."
        ),
        x: Optional[int] = Field(
            None,
            description="The X coordinate of the top-left corner of the crop region.",
        ),
        y: Optional[int] = Field(
            None,
            description="The Y coordinate of the top-left corner of the crop region.",
        ),
        size: Optional[int] = Field(
            None, description="The length of each side of the crop region."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Load project avatar"""
        api = get_api()
        response = api.jira_cloud_create_project_avatar(
            project_id_or_key=project_id_or_key,
            x=x,
            y=y,
            size=size,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_project_avatars", tags={"jira-cloud-project"})
    def jira_cloud_get_all_project_avatars(
        project_id_or_key: str = Field(
            ..., description="The ID or (case-sensitive) key of the project."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all project avatars"""
        api = get_api()
        response = api.jira_cloud_get_all_project_avatars(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_classification_config", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_project_classification_config(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case-sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get the classification configuration for a project"""
        api = get_api()
        response = api.jira_cloud_get_project_classification_config(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_default_project_classification",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_remove_default_project_classification(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case-sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Remove the default data classification level from a project"""
        api = get_api()
        response = api.jira_cloud_remove_default_project_classification(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_default_project_classification",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_default_project_classification(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case-sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get the default data classification level of a project"""
        api = get_api()
        response = api.jira_cloud_get_default_project_classification(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_default_project_classification",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_update_default_project_classification(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case-sensitive)."
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update the default data classification level of a project"""
        api = get_api()
        response = api.jira_cloud_update_default_project_classification(
            project_id_or_key=project_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_components_paginated",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_project_components_paginated(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
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
            description="[Order](#ordering) the results by a field:   *  `description` Sorts by the component description.  *  `issueCount` Sorts by the count of issues associated with the component.  *  `lead` Sorts by the user key of the component's project lead.  *  `name` Sorts by component name.",
        ),
        component_source: Optional[str] = Field(
            None,
            description="The source of the components to return. Can be `jira` (default), `compass` or `auto`. When `auto` is specified, the API will return connected Compass components if the project is opted into Compass, otherwise it will return Jira components. Defaults to `jira`.",
        ),
        query: Optional[str] = Field(
            None,
            description="Filter the results using a literal string. Components with a matching `name` or `description` are returned (case insensitive).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project components paginated"""
        api = get_api()
        response = api.jira_cloud_get_project_components_paginated(
            project_id_or_key=project_id_or_key,
            start_at=start_at,
            max_results=max_results,
            order_by=order_by,
            component_source=component_source,
            query=query,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_components", tags={"jira-cloud-project"})
    def jira_cloud_get_project_components(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        component_source: Optional[str] = Field(
            None,
            description="The source of the components to return. Can be `jira` (default), `compass` or `auto`. When `auto` is specified, the API will return connected Compass components if the project is opted into Compass, otherwise it will return Jira components. Defaults to `jira`.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project components"""
        api = get_api()
        response = api.jira_cloud_get_project_components(
            project_id_or_key=project_id_or_key,
            component_source=component_source,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_project_asynchronously", tags={"jira-cloud-project"}
    )
    def jira_cloud_delete_project_asynchronously(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete project asynchronously"""
        api = get_api()
        response = api.jira_cloud_delete_project_asynchronously(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_features_for_project", tags={"jira-cloud-project"})
    def jira_cloud_get_features_for_project(
        project_id_or_key: str = Field(
            ..., description="The ID or (case-sensitive) key of the project."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project features"""
        api = get_api()
        response = api.jira_cloud_get_features_for_project(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_toggle_feature_for_project", tags={"jira-cloud-project"})
    def jira_cloud_toggle_feature_for_project(
        project_id_or_key: str = Field(
            ..., description="The ID or (case-sensitive) key of the project."
        ),
        feature_key: str = Field(..., description="The key of the feature."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set project feature state"""
        api = get_api()
        response = api.jira_cloud_toggle_feature_for_project(
            project_id_or_key=project_id_or_key,
            feature_key=feature_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_property_keys", tags={"jira-cloud-project"})
    def jira_cloud_get_project_property_keys(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project property keys"""
        api = get_api()
        response = api.jira_cloud_get_project_property_keys(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_project_property", tags={"jira-cloud-project"})
    def jira_cloud_delete_project_property(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        property_key: str = Field(
            ...,
            description="The project property key. Use [Get project property keys](#api-rest-api-3-project-projectIdOrKey-properties-get) to get a list of all project property keys.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete project property"""
        api = get_api()
        response = api.jira_cloud_delete_project_property(
            project_id_or_key=project_id_or_key,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_property", tags={"jira-cloud-project"})
    def jira_cloud_get_project_property(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        property_key: str = Field(
            ...,
            description="The project property key. Use [Get project property keys](#api-rest-api-3-project-projectIdOrKey-properties-get) to get a list of all project property keys.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project property"""
        api = get_api()
        response = api.jira_cloud_get_project_property(
            project_id_or_key=project_id_or_key,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_project_property", tags={"jira-cloud-project"})
    def jira_cloud_set_project_property(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        property_key: str = Field(
            ...,
            description="The key of the project property. The maximum length is 255 characters.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set project property"""
        api = get_api()
        response = api.jira_cloud_set_project_property(
            project_id_or_key=project_id_or_key,
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_roles", tags={"jira-cloud-project"})
    def jira_cloud_get_project_roles(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project roles for project"""
        api = get_api()
        response = api.jira_cloud_get_project_roles(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_role", tags={"jira-cloud-project"})
    def jira_cloud_get_project_role(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        exclude_inactive_users: Optional[bool] = Field(
            None, description="Exclude inactive users."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project role for project"""
        api = get_api()
        response = api.jira_cloud_get_project_role(
            project_id_or_key=project_id_or_key,
            id_=id_,
            exclude_inactive_users=exclude_inactive_users,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_role_details", tags={"jira-cloud-project"})
    def jira_cloud_get_project_role_details(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        current_member: Optional[bool] = Field(
            None,
            description="Whether the roles should be filtered to include only those the user is assigned to.",
        ),
        exclude_connect_addons: Optional[bool] = Field(
            None, description="Parameter excludeConnectAddons"
        ),
        exclude_other_service_roles: Optional[bool] = Field(
            None,
            description="Do not return the default JSM company-managed space from CSM spaces, or the default CSM roles from JSM spaces.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project role details"""
        api = get_api()
        response = api.jira_cloud_get_project_role_details(
            project_id_or_key=project_id_or_key,
            current_member=current_member,
            exclude_connect_addons=exclude_connect_addons,
            exclude_other_service_roles=exclude_other_service_roles,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_versions_paginated",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_project_versions_paginated(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
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
            description="[Order](#ordering) the results by a field:   *  `description` Sorts by version description.  *  `name` Sorts by version name.  *  `releaseDate` Sorts by release date, starting with the oldest date. Versions with no release date are listed last.  *  `sequence` Sorts by the order of appearance in the user interface.  *  `startDate` Sorts by start date, starting with the oldest date. Versions with no start date are listed last.",
        ),
        query: Optional[str] = Field(
            None,
            description="Filter the results using a literal string. Versions with matching `name` or `description` are returned (case insensitive).",
        ),
        status: Optional[str] = Field(
            None,
            description="A list of status values used to filter the results by version status. This parameter accepts a comma-separated list. The status values are `released`, `unreleased`, and `archived`.",
        ),
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `issuesstatus` Returns the number of issues in each status category for each version.  *  `operations` Returns actions that can be performed on the specified version.  *  `driver` Returns the Atlassian account ID of the version driver.  *  `approvers` Returns a list containing the approvers for this version.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project versions paginated"""
        api = get_api()
        response = api.jira_cloud_get_project_versions_paginated(
            project_id_or_key=project_id_or_key,
            start_at=start_at,
            max_results=max_results,
            order_by=order_by,
            query=query,
            status=status,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_versions", tags={"jira-cloud-project"})
    def jira_cloud_get_project_versions(
        project_id_or_key: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts `operations`, which returns actions that can be performed on the version.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project versions"""
        api = get_api()
        response = api.jira_cloud_get_project_versions(
            project_id_or_key=project_id_or_key,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_email", tags={"jira-cloud-project"})
    def jira_cloud_get_project_email(
        project_id: int = Field(..., description="The project ID."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project's sender email"""
        api = get_api()
        response = api.jira_cloud_get_project_email(
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_project_email", tags={"jira-cloud-project"})
    def jira_cloud_update_project_email(
        project_id: int = Field(..., description="The project ID."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Set project's sender email"""
        api = get_api()
        response = api.jira_cloud_update_project_email(
            project_id=project_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_notification_scheme_for_project",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_notification_scheme_for_project(
        project_key_or_id: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `all` Returns all expandable information  *  `field` Returns information about any custom fields assigned to receive an event  *  `group` Returns information about any groups assigned to receive an event  *  `notificationSchemeEvents` Returns a list of event associations. This list is returned for all expandable information  *  `projectRole` Returns information about any project roles assigned to receive an event  *  `user` Returns information about any users assigned to receive an event",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project notification scheme"""
        api = get_api()
        response = api.jira_cloud_get_notification_scheme_for_project(
            project_key_or_id=project_key_or_id,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_security_levels_for_project", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_security_levels_for_project(
        project_key_or_id: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project issue security levels"""
        api = get_api()
        response = api.jira_cloud_get_security_levels_for_project(
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_project_categories", tags={"jira-cloud-project"})
    def jira_cloud_get_all_project_categories(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all project categories"""
        api = get_api()
        response = api.jira_cloud_get_all_project_categories()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_project_category", tags={"jira-cloud-project"})
    def jira_cloud_create_project_category(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create project category"""
        api = get_api()
        response = api.jira_cloud_create_project_category(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_project_category", tags={"jira-cloud-project"})
    def jira_cloud_remove_project_category(
        id_: int = Field(..., description="ID of the project category to delete."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete project category"""
        api = get_api()
        response = api.jira_cloud_remove_project_category(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_category_by_id",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_project_category_by_id(
        id_: int = Field(..., description="The ID of the project category."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project category by ID"""
        api = get_api()
        response = api.jira_cloud_get_project_category_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_project_category", tags={"jira-cloud-project"})
    def jira_cloud_update_project_category(
        id_: int = Field(..., description="Parameter id"),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update project category"""
        api = get_api()
        response = api.jira_cloud_update_project_category(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_fields", tags={"jira-cloud-project"})
    def jira_cloud_get_project_fields(
        project_id: List[Any] = Field(
            ..., description="The IDs of projects to return fields for."
        ),
        work_type_id: List[Any] = Field(
            ..., description="The IDs of work types (issue types) to return fields for."
        ),
        start_at: Optional[int] = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: Optional[int] = Field(
            None, description="The maximum number of items to return per page."
        ),
        field_id: Optional[List[Any]] = Field(
            None,
            description="The IDs of fields to return. If not provided, all fields are returned.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get fields for projects"""
        api = get_api()
        response = api.jira_cloud_get_project_fields(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
            work_type_id=work_type_id,
            field_id=field_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_validate_project_key", tags={"jira-cloud-project"})
    def jira_cloud_validate_project_key(
        key: Optional[str] = Field(None, description="The project key."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Validate project key"""
        api = get_api()
        response = api.jira_cloud_validate_project_key(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_valid_project_key", tags={"jira-cloud-project"})
    def jira_cloud_get_valid_project_key(
        key: Optional[str] = Field(None, description="The project key."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get valid project key"""
        api = get_api()
        response = api.jira_cloud_get_valid_project_key(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_valid_project_name", tags={"jira-cloud-project"})
    def jira_cloud_get_valid_project_name(
        name: str = Field(..., description="The project name."),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get valid project name"""
        api = get_api()
        response = api.jira_cloud_get_valid_project_name(
            name=name,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_all_project_roles", tags={"jira-cloud-project"})
    def jira_cloud_get_all_project_roles(
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all project roles"""
        api = get_api()
        response = api.jira_cloud_get_all_project_roles()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_project_role", tags={"jira-cloud-project"})
    def jira_cloud_create_project_role(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create project role"""
        api = get_api()
        response = api.jira_cloud_create_project_role(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_project_role", tags={"jira-cloud-project"})
    def jira_cloud_delete_project_role(
        id_: int = Field(
            ...,
            description="The ID of the project role to delete. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        swap: Optional[int] = Field(
            None,
            description="The ID of the project role that will replace the one being deleted. The swap will attempt to swap the role in schemes (notifications, permissions, issue security), workflows, worklogs and comments.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete project role"""
        api = get_api()
        response = api.jira_cloud_delete_project_role(
            id_=id_,
            swap=swap,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_project_role_by_id", tags={"jira-cloud-project"})
    def jira_cloud_get_project_role_by_id(
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project role by ID"""
        api = get_api()
        response = api.jira_cloud_get_project_role_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_partial_update_project_role", tags={"jira-cloud-project"}
    )
    def jira_cloud_partial_update_project_role(
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Partial update project role"""
        api = get_api()
        response = api.jira_cloud_partial_update_project_role(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_fully_update_project_role", tags={"jira-cloud-project"})
    def jira_cloud_fully_update_project_role(
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Fully update project role"""
        api = get_api()
        response = api.jira_cloud_fully_update_project_role(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_project_role_actors_from_role",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_delete_project_role_actors_from_role(
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        user: Optional[str] = Field(
            None,
            description="The user account ID of the user to remove as a default actor.",
        ),
        group_id: Optional[str] = Field(
            None,
            description="The group ID of the group to be removed as a default actor. This parameter cannot be used with the `group` parameter.",
        ),
        group: Optional[str] = Field(
            None,
            description="The group name of the group to be removed as a default actor.This parameter cannot be used with the `groupId` parameter. As a group's name can change, use of `groupId` is recommended.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete default actors from project role"""
        api = get_api()
        response = api.jira_cloud_delete_project_role_actors_from_role(
            id_=id_,
            user=user,
            group_id=group_id,
            group=group,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_role_actors_for_role",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_project_role_actors_for_role(
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get default actors for project role"""
        api = get_api()
        response = api.jira_cloud_get_project_role_actors_for_role(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_add_project_role_actors_to_role",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_add_project_role_actors_to_role(
        id_: int = Field(
            ...,
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Add default actors to project role"""
        api = get_api()
        response = api.jira_cloud_add_project_role_actors_to_role(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_usages_for_status", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_project_usages_for_status(
        status_id: str = Field(
            ..., description="The statusId to fetch project usages for"
        ),
        next_page_token: Optional[str] = Field(
            None, description="The cursor for pagination"
        ),
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of results to return. Must be an integer between 1 and 200.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get project usages by status"""
        api = get_api()
        response = api.jira_cloud_get_project_usages_for_status(
            status_id=status_id,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_version", tags={"jira-cloud-project"})
    def jira_cloud_create_version(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create version"""
        api = get_api()
        response = api.jira_cloud_create_version(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_version", tags={"jira-cloud-project"})
    def jira_cloud_delete_version(
        id_: str = Field(..., description="The ID of the version."),
        move_fix_issues_to: Optional[str] = Field(
            None,
            description="The ID of the version to update `fixVersion` to when the field contains the deleted version. The replacement version must be in the same project as the version being deleted and cannot be the version being deleted.",
        ),
        move_affected_issues_to: Optional[str] = Field(
            None,
            description="The ID of the version to update `affectedVersion` to when the field contains the deleted version. The replacement version must be in the same project as the version being deleted and cannot be the version being deleted.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete version"""
        api = get_api()
        response = api.jira_cloud_delete_version(
            id_=id_,
            move_fix_issues_to=move_fix_issues_to,
            move_affected_issues_to=move_affected_issues_to,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_version", tags={"jira-cloud-project"})
    def jira_cloud_get_version(
        id_: str = Field(..., description="The ID of the version."),
        expand: Optional[str] = Field(
            None,
            description="Use [expand](#expansion) to include additional information about version in the response. This parameter accepts a comma-separated list. Expand options include:   *  `operations` Returns the list of operations available for this version.  *  `issuesstatus` Returns the count of issues in this version for each of the status categories *to do*, *in progress*, *done*, and *unmapped*. The *unmapped* property represents the number of issues with a status other than *to do*, *in progress*, and *done*.  *  `driver` Returns the Atlassian account ID of the version driver.  *  `approvers` Returns a list containing the Atlassian account IDs of approvers for this version.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get version"""
        api = get_api()
        response = api.jira_cloud_get_version(
            id_=id_,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_version", tags={"jira-cloud-project"})
    def jira_cloud_update_version(
        id_: str = Field(..., description="The ID of the version."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update version"""
        api = get_api()
        response = api.jira_cloud_update_version(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_merge_versions", tags={"jira-cloud-project"})
    def jira_cloud_merge_versions(
        id_: str = Field(..., description="The ID of the version to delete."),
        move_issues_to: str = Field(
            ..., description="The ID of the version to merge into."
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Merge versions"""
        api = get_api()
        response = api.jira_cloud_merge_versions(
            id_=id_,
            move_issues_to=move_issues_to,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_move_version", tags={"jira-cloud-project"})
    def jira_cloud_move_version(
        id_: str = Field(..., description="The ID of the version to be moved."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Move version"""
        api = get_api()
        response = api.jira_cloud_move_version(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_and_replace_version",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_delete_and_replace_version(
        id_: str = Field(..., description="The ID of the version."),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete and replace version"""
        api = get_api()
        response = api.jira_cloud_delete_and_replace_version(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_usages_for_workflow", tags={"jira-cloud-project"}
    )
    def jira_cloud_get_project_usages_for_workflow(
        workflow_id: str = Field(..., description="The workflow ID"),
        next_page_token: Optional[str] = Field(
            None, description="The cursor for pagination"
        ),
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of results to return. Must be an integer between 1 and 200.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get projects using a given workflow"""
        api = get_api()
        response = api.jira_cloud_get_project_usages_for_workflow(
            workflow_id=workflow_id,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_scheme_project_associations",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_workflow_scheme_project_associations(
        project_id: List[Any] = Field(
            ...,
            description="The ID of a project to return the workflow schemes for. To include multiple projects, provide an ampersand-Jim: oneseparated list. For example, `projectId=10000&projectId=10001`.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get workflow scheme project associations"""
        api = get_api()
        response = api.jira_cloud_get_workflow_scheme_project_associations(
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_assign_scheme_to_project", tags={"jira-cloud-project"})
    def jira_cloud_assign_scheme_to_project(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Assign workflow scheme to project"""
        api = get_api()
        response = api.jira_cloud_assign_scheme_to_project(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_switch_workflow_scheme_for_project",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_switch_workflow_scheme_for_project(
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Switch workflow scheme for project"""
        api = get_api()
        response = api.jira_cloud_switch_workflow_scheme_for_project(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_usages_for_workflow_scheme",
        tags={"jira-cloud-project"},
    )
    def jira_cloud_get_project_usages_for_workflow_scheme(
        workflow_scheme_id: str = Field(..., description="The workflow scheme ID"),
        next_page_token: Optional[str] = Field(
            None, description="The cursor for pagination"
        ),
        max_results: Optional[int] = Field(
            None,
            description="The maximum number of results to return. Must be an integer between 1 and 200.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get projects which are using a given workflow scheme"""
        api = get_api()
        response = api.jira_cloud_get_project_usages_for_workflow_scheme(
            workflow_scheme_id=workflow_scheme_id,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return response.model_dump()
