# Generated MCP Tools for JiraServer
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.jira_server_api import JiraServerAPI
from ..auth import get_base_client


def get_api() -> JiraServerAPI:
    return JiraServerAPI(get_base_client())


def register_jira_server_tools(mcp: FastMCP):
    @mcp.tool(name="jira_server_move_issues_to_backlog", tags={"jira-server-other"})
    def jira_server_move_issues_to_backlog(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update issues to move them to the backlog"""
        api = get_api()
        response = api.jira_server_move_issues_to_backlog(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_boards", tags={"jira-server-agile-board"})
    def jira_server_get_all_boards(
        max_results: int | None = Field(
            None,
            description="The maximum number of boards to return per page. Default: 50.",
        ),
        name: str | None = Field(
            None,
            description="Filters results to boards that match or partially match the specified name.",
        ),
        project_key_or_id: str | None = Field(
            None,
            description="Filters results to boards that are relevant to a project.",
        ),
        type_: str | None = Field(
            None,
            description="Filters results to boards of the specified type. Valid values: scrum, kanban.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned boards. Base index: 0.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all boards"""
        api = get_api()
        response = api.jira_server_get_all_boards(
            max_results=max_results,
            name=name,
            project_key_or_id=project_key_or_id,
            type_=type_,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_board", tags={"jira-server-agile-board"})
    def jira_server_create_board(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new board"""
        api = get_api()
        response = api.jira_server_create_board(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_board", tags={"jira-server-agile-board"})
    def jira_server_get_board(
        board_id: int = Field(..., description="The Id of the requested board."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a single board"""
        api = get_api()
        response = api.jira_server_get_board(
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_board", tags={"jira-server-agile-board"})
    def jira_server_delete_board(
        board_id: int = Field(..., description="id of the board to be deleted"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete the board"""
        api = get_api()
        response = api.jira_server_delete_board(
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issues_for_backlog", tags={"jira-server-other"})
    def jira_server_get_issues_for_backlog(
        board_id: int = Field(
            ..., description="The Id of the board that contains the requested issues."
        ),
        expand: str | None = Field(
            None, description="This parameter is currently not used."
        ),
        jql: str | None = Field(
            None,
            description="Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of issues to return per page. Default: 50.",
        ),
        validate_query: bool | None = Field(
            None,
            description="Specifies whether to validate the JQL query or not. Default: true.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned issues. Base index: 0.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issues from the board's backlog"""
        api = get_api()
        response = api.jira_server_get_issues_for_backlog(
            expand=expand,
            jql=jql,
            max_results=max_results,
            validate_query=validate_query,
            board_id=board_id,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_configuration", tags={"jira-server-other"})
    def jira_server_get_configuration(
        board_id: int = Field(
            ..., description="The id of the board for which configuration is requested."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the board configuration"""
        api = get_api()
        response = api.jira_server_get_configuration(
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_epics", tags={"jira-server-agile-epic"})
    def jira_server_get_epics(
        board_id: int = Field(
            ..., description="The Id of the board that contains the requested epics."
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of epics to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details.",
        ),
        done: str | None = Field(
            None,
            description="Filters results to epics that are either done or not done. Valid values: true, false.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned epics. Base index: 0. See the 'Pagination' section at the top of this page for more details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all epics from the board"""
        api = get_api()
        response = api.jira_server_get_epics(
            max_results=max_results,
            board_id=board_id,
            done=done,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issues_without_epic", tags={"jira-server-agile-epic"}
    )
    def jira_server_get_issues_without_epic(
        board_id: int = Field(
            ..., description="The Id of the board that contains the requested issues."
        ),
        expand: str | None = Field(
            None, description="A comma-separated list of the parameters to expand."
        ),
        jql: str | None = Field(
            None,
            description="Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of issues to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details. Note, the total number of issues returned is limited by the property 'jira.search.views.default.max' in your JIRA instance. If you exceed this limit, your results will be truncated.",
        ),
        validate_query: bool | None = Field(
            None,
            description="Specifies whether to validate the JQL query or not. Default: true.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issues without an epic"""
        api = get_api()
        response = api.jira_server_get_issues_without_epic(
            expand=expand,
            jql=jql,
            max_results=max_results,
            validate_query=validate_query,
            board_id=board_id,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issues_for_epic", tags={"jira-server-agile-epic"})
    def jira_server_get_issues_for_epic(
        epic_id: int = Field(
            ..., description="The Id of the epic that contains the requested issues."
        ),
        board_id: int = Field(
            ..., description="The Id of the board that contains the requested issues."
        ),
        expand: str | None = Field(
            None, description="A comma-separated list of the parameters to expand."
        ),
        jql: str | None = Field(
            None,
            description="Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of issues to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details. Note, the total number of issues returned is limited by the property 'jira.search.views.default.max' in your JIRA instance. If you exceed this limit, your results will be truncated.",
        ),
        validate_query: bool | None = Field(
            None,
            description="Specifies whether to validate the JQL query or not. Default: true.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issues for a specific epic"""
        api = get_api()
        response = api.jira_server_get_issues_for_epic(
            expand=expand,
            jql=jql,
            epic_id=epic_id,
            max_results=max_results,
            validate_query=validate_query,
            board_id=board_id,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issues_for_board", tags={"jira-server-agile-board"})
    def jira_server_get_issues_for_board(
        board_id: int = Field(
            ..., description="The Id of the board that contains the requested issues."
        ),
        expand: str | None = Field(
            None, description="This parameter is currently not used."
        ),
        jql: str | None = Field(
            None,
            description="Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of issues to return per page. Default: 50.",
        ),
        validate_query: bool | None = Field(
            None,
            description="Specifies whether to validate the JQL query or not. Default: true.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned issues. Base index: 0.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issues from a board"""
        api = get_api()
        response = api.jira_server_get_issues_for_board(
            expand=expand,
            jql=jql,
            max_results=max_results,
            validate_query=validate_query,
            board_id=board_id,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_projects", tags={"jira-server-project"})
    def jira_server_get_projects(
        board_id: int = Field(
            ..., description="The Id of the board that contains returned projects."
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of projects to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned projects. Base index: 0. See the 'Pagination' section at the top of this page for more details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all projects associated with the board"""
        api = get_api()
        response = api.jira_server_get_projects(
            max_results=max_results,
            board_id=board_id,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_properties_keys", tags={"jira-server-other"})
    def jira_server_get_properties_keys(
        board_id: str = Field(
            ...,
            description="The id of the board from which property keys will be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all properties keys for a board"""
        api = get_api()
        response = api.jira_server_get_properties_keys(
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_property", tags={"jira-server-other"})
    def jira_server_get_property(
        property_key: str = Field(
            ..., description="The key of the property to return."
        ),
        board_id: str = Field(
            ...,
            description="The id of the board from which the property will be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a property from a board"""
        api = get_api()
        response = api.jira_server_get_property(
            property_key=property_key,
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_property", tags={"jira-server-other"})
    def jira_server_set_property(
        property_key: str = Field(..., description="The key of the board's property."),
        board_id: str = Field(
            ..., description="The id of the board on which the property will be set."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a board's property"""
        api = get_api()
        response = api.jira_server_set_property(
            property_key=property_key,
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_property", tags={"jira-server-other"})
    def jira_server_delete_property(
        property_key: str = Field(
            ..., description="The key of the property to remove."
        ),
        board_id: str = Field(
            ...,
            description="The id of the board from which the property will be removed.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a property from a board"""
        api = get_api()
        response = api.jira_server_delete_property(
            property_key=property_key,
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_refined_velocity", tags={"jira-server-other"})
    def jira_server_get_refined_velocity(
        board_id: int = Field(
            ...,
            description="The id of the board from which the settings will be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the value of the refined velocity setting"""
        api = get_api()
        response = api.jira_server_get_refined_velocity(
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_refined_velocity", tags={"jira-server-other"})
    def jira_server_set_refined_velocity(
        board_id: int = Field(
            ..., description="The id of the board on which the property will be set."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update the board's refined velocity setting"""
        api = get_api()
        response = api.jira_server_set_refined_velocity(
            board_id=board_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_sprints", tags={"jira-server-agile-sprint"})
    def jira_server_get_all_sprints(
        board_id: int = Field(
            ..., description="The Id of the board that contains the requested sprints."
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of sprints to return per page. Default: 50.",
        ),
        state: str | None = Field(
            None,
            description="Filters results to sprints in specified states. Valid values: future, active, closed. You can define multiple states separated by commas, e.g. state=active,closed",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned sprints. Base index: 0.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all sprints from a board"""
        api = get_api()
        response = api.jira_server_get_all_sprints(
            max_results=max_results,
            board_id=board_id,
            state=state,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issues_for_sprint", tags={"jira-server-agile-sprint"}
    )
    def jira_server_get_issues_for_sprint(
        sprint_id: int = Field(
            ..., description="The Id of the sprint that contains requested issues."
        ),
        board_id: int = Field(
            ..., description="The Id of the board that contains requested issues."
        ),
        expand: str | None = Field(
            None, description="A comma-separated list of the parameters to expand."
        ),
        jql: str | None = Field(
            None,
            description="Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of sprints to return per page. Default: 50.",
        ),
        validate_query: bool | None = Field(
            None,
            description="Specifies whether to validate the JQL query or not. Default: true.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issues for a sprint"""
        api = get_api()
        response = api.jira_server_get_issues_for_sprint(
            sprint_id=sprint_id,
            expand=expand,
            jql=jql,
            max_results=max_results,
            validate_query=validate_query,
            board_id=board_id,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_versions", tags={"jira-server-other"})
    def jira_server_get_all_versions(
        board_id: int = Field(
            ..., description="The Id of the board that contains the requested versions."
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of versions to return per page. Default: 50.",
        ),
        released: str | None = Field(
            None,
            description="Filters results to versions that are either released or unreleased. Valid values: true, false.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned versions. Base index: 0.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all versions from a board"""
        api = get_api()
        response = api.jira_server_get_all_versions(
            max_results=max_results,
            board_id=board_id,
            released=released,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issues_without_epic_1", tags={"jira-server-agile-epic"}
    )
    def jira_server_get_issues_without_epic_1(
        expand: str | None = Field(
            None, description="A comma-separated list of the parameters to expand."
        ),
        jql: str | None = Field(
            None,
            description="Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of issues to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details. Note, the total number of issues returned is limited by the property 'jira.search.views.default.max'. in your JIRA instance. If you exceed this limit, your results will be truncated.",
        ),
        validate_query: bool | None = Field(
            None,
            description="Specifies whether to validate the JQL query or not. Default: true.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issues without an epic"""
        api = get_api()
        response = api.jira_server_get_issues_without_epic_1(
            expand=expand,
            jql=jql,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_remove_issues_from_epic", tags={"jira-server-agile-epic"}
    )
    def jira_server_remove_issues_from_epic(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove issues from any epic"""
        api = get_api()
        response = api.jira_server_remove_issues_from_epic(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_epic", tags={"jira-server-agile-epic"})
    def jira_server_get_epic(
        epic_id_or_key: str = Field(
            ..., description="The id or key of the requested epic."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get an epic by id or key"""
        api = get_api()
        response = api.jira_server_get_epic(
            epic_id_or_key=epic_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_partially_update_epic", tags={"jira-server-agile-epic"})
    def jira_server_partially_update_epic(
        epic_id_or_key: str = Field(
            ..., description="The id or key of the epic to update."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update an epic's details"""
        api = get_api()
        response = api.jira_server_partially_update_epic(
            epic_id_or_key=epic_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issues_for_epic_1", tags={"jira-server-agile-epic"})
    def jira_server_get_issues_for_epic_1(
        epic_id_or_key: str = Field(
            ...,
            description="The id or key of the epic that contains the requested issues.",
        ),
        expand: str | None = Field(
            None, description="A comma-separated list of the parameters to expand."
        ),
        jql: str | None = Field(
            None,
            description="Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of issues to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details. Note, the total number of issues returned is limited by the property 'jira.search.views.default.max'. in your JIRA instance. If you exceed this limit, your results will be truncated.",
        ),
        validate_query: bool | None = Field(
            None,
            description="Specifies whether to validate the JQL query or not. Default: true.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issues for a specific epic"""
        api = get_api()
        response = api.jira_server_get_issues_for_epic_1(
            expand=expand,
            jql=jql,
            max_results=max_results,
            validate_query=validate_query,
            epic_id_or_key=epic_id_or_key,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_move_issues_to_epic", tags={"jira-server-agile-epic"})
    def jira_server_move_issues_to_epic(
        epic_id_or_key: str = Field(
            ...,
            description="The id or key of the epic that you want to assign issues to.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move issues to a specific epic"""
        api = get_api()
        response = api.jira_server_move_issues_to_epic(
            epic_id_or_key=epic_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_rank_epics", tags={"jira-server-agile-epic"})
    def jira_server_rank_epics(
        epic_id_or_key: str = Field(
            ..., description="The id or key of the epic to rank."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Rank an epic relative to another"""
        api = get_api()
        response = api.jira_server_rank_epics(
            epic_id_or_key=epic_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_rank_issues", tags={"jira-server-other"})
    def jira_server_rank_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Rank issues before or after a given issue"""
        api = get_api()
        response = api.jira_server_rank_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue", tags={"jira-server-other"})
    def jira_server_get_issue(
        issue_id_or_key: str = Field(
            ..., description="The Id or key of the requested issue."
        ),
        expand: str | None = Field(
            None, description="A comma-separated list of the parameters to expand."
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        update_history: bool | None = Field(
            None,
            description="A boolean indicating whether the issue retrieved by this method should be added to the current user's issue history.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a single issue with Agile fields"""
        api = get_api()
        response = api.jira_server_get_issue(
            expand=expand,
            issue_id_or_key=issue_id_or_key,
            fields=fields,
            update_history=update_history,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issue_estimation_for_board",
        tags={"jira-server-agile-board"},
    )
    def jira_server_get_issue_estimation_for_board(
        issue_id_or_key: str = Field(
            ..., description="The Id or key of the requested issue."
        ),
        board_id: int | None = Field(
            None,
            description="The id of the board required to determine which field is used for estimation.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the estimation of an issue for a board"""
        api = get_api()
        response = api.jira_server_get_issue_estimation_for_board(
            issue_id_or_key=issue_id_or_key,
            board_id=board_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_estimate_issue_for_board", tags={"jira-server-agile-board"}
    )
    def jira_server_estimate_issue_for_board(
        issue_id_or_key: str = Field(
            ..., description="The Id or key of the requested issue."
        ),
        board_id: int | None = Field(
            None,
            description="The id of the board required to determine which field is used for estimation.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update the estimation of an issue for a board"""
        api = get_api()
        response = api.jira_server_estimate_issue_for_board(
            issue_id_or_key=issue_id_or_key,
            board_id=board_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_sprint", tags={"jira-server-agile-sprint"})
    def jira_server_create_sprint(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a future sprint"""
        api = get_api()
        response = api.jira_server_create_sprint(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_unmap_sprints", tags={"jira-server-agile-sprint"})
    def jira_server_unmap_sprints(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Unmap sprints from being synced"""
        api = get_api()
        response = api.jira_server_unmap_sprints(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_unmap_all_sprints", tags={"jira-server-agile-sprint"})
    def jira_server_unmap_all_sprints(_ctx: Context | None = None) -> dict[str, Any]:
        """Unmap all sprints from being synced"""
        api = get_api()
        response = api.jira_server_unmap_all_sprints()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_sprint", tags={"jira-server-agile-sprint"})
    def jira_server_get_sprint(
        sprint_id: int = Field(..., description="The Id of the requested sprint."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get sprint by id"""
        api = get_api()
        response = api.jira_server_get_sprint(
            sprint_id=sprint_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_sprint", tags={"jira-server-agile-sprint"})
    def jira_server_update_sprint(
        sprint_id: int = Field(..., description="The Id of the sprint to update."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a sprint fully"""
        api = get_api()
        response = api.jira_server_update_sprint(
            sprint_id=sprint_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_partially_update_sprint", tags={"jira-server-agile-sprint"}
    )
    def jira_server_partially_update_sprint(
        sprint_id: int = Field(..., description="The Id of the sprint to update."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Partially update a sprint"""
        api = get_api()
        response = api.jira_server_partially_update_sprint(
            sprint_id=sprint_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_sprint", tags={"jira-server-agile-sprint"})
    def jira_server_delete_sprint(
        sprint_id: int = Field(..., description="The Id of the sprint to delete."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a sprint"""
        api = get_api()
        response = api.jira_server_delete_sprint(
            sprint_id=sprint_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issues_for_sprint_1", tags={"jira-server-agile-sprint"}
    )
    def jira_server_get_issues_for_sprint_1(
        sprint_id: int = Field(
            ..., description="The Id of the sprint that contains the requested issues."
        ),
        expand: str | None = Field(
            None, description="A comma-separated list of the parameters to expand."
        ),
        jql: str | None = Field(
            None,
            description="Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of issues to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details. Note, the total number of issues returned is limited by the property 'jira.search.views.default.max' in your JIRA instance. If you exceed this limit, your results will be truncated.",
        ),
        validate_query: bool | None = Field(
            None,
            description="Specifies whether to validate the JQL query or not. Default: true.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="The list of fields to return for each issue. By default, all navigable and Agile fields are returned.",
        ),
        start_at: int | None = Field(
            None,
            description="The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issues in a sprint"""
        api = get_api()
        response = api.jira_server_get_issues_for_sprint_1(
            sprint_id=sprint_id,
            expand=expand,
            jql=jql,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_move_issues_to_sprint", tags={"jira-server-agile-sprint"}
    )
    def jira_server_move_issues_to_sprint(
        sprint_id: int = Field(
            ..., description="The Id of the sprint that you want to assign issues to."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move issues to a sprint"""
        api = get_api()
        response = api.jira_server_move_issues_to_sprint(
            sprint_id=sprint_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_properties_keys_1", tags={"jira-server-other"})
    def jira_server_get_properties_keys_1(
        sprint_id: str = Field(
            ...,
            description="The id of the sprint from which property keys will be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all properties keys for a sprint"""
        api = get_api()
        response = api.jira_server_get_properties_keys_1(
            sprint_id=sprint_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_property_1", tags={"jira-server-other"})
    def jira_server_get_property_1(
        property_key: str = Field(
            ..., description="The key of the property to return."
        ),
        sprint_id: str = Field(
            ...,
            description="The id of the sprint from which the property will be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a property for a sprint"""
        api = get_api()
        response = api.jira_server_get_property_1(
            property_key=property_key,
            sprint_id=sprint_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_property_1", tags={"jira-server-other"})
    def jira_server_set_property_1(
        property_key: str = Field(
            ...,
            description="The key of the sprint's property. The maximum length of the key is 255 bytes.",
        ),
        sprint_id: str = Field(
            ..., description="The id of the sprint on which the property will be set."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a sprint's property"""
        api = get_api()
        response = api.jira_server_set_property_1(
            property_key=property_key,
            sprint_id=sprint_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_property_1", tags={"jira-server-other"})
    def jira_server_delete_property_1(
        property_key: str = Field(
            ..., description="The key of the property to remove."
        ),
        sprint_id: str = Field(
            ...,
            description="The id of the sprint from which the property will be removed.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a sprint's property"""
        api = get_api()
        response = api.jira_server_delete_property_1(
            property_key=property_key,
            sprint_id=sprint_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_swap_sprint", tags={"jira-server-agile-sprint"})
    def jira_server_swap_sprint(
        sprint_id: int = Field(..., description="The Id of the sprint to swap."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Swap the position of two sprints"""
        api = get_api()
        response = api.jira_server_swap_sprint(
            sprint_id=sprint_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_application_property", tags={"jira-server-other"})
    def jira_server_get_application_property(
        permission_level: str = Field(
            ...,
            description="when fetching a list specifies the permission level of all items in the list see {@link com.atlassian.jira.bc.admin.ApplicationPropertiesService.EditPermissionLevel}",
        ),
        key: str = Field(..., description="a String containing the property key."),
        key_filter: str | None = Field(
            None,
            description="when fetching a list allows the list to be filtered by the property's start of key e.g. 'jira.lf.*' would fetch only those permissions that are editable and whose keys start with      *                        'jira.lf.'. This is a regex.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get an application property by key"""
        api = get_api()
        response = api.jira_server_get_application_property(
            permission_level=permission_level,
            key_filter=key_filter,
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_advanced_settings", tags={"jira-server-other"})
    def jira_server_get_advanced_settings(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all advanced settings properties"""
        api = get_api()
        response = api.jira_server_get_advanced_settings()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_set_property_via_restful_table", tags={"jira-server-screen"}
    )
    def jira_server_set_property_via_restful_table(
        id_: str = Field(..., description="a String containing the property key."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update an application property"""
        api = get_api()
        response = api.jira_server_set_property_via_restful_table(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all", tags={"jira-server-other"})
    def jira_server_get_all(_ctx: Context | None = None) -> dict[str, Any]:
        """Get all application roles in the system"""
        api = get_api()
        response = api.jira_server_get_all()
        return response.model_dump()

    @mcp.tool(name="jira_server_put_bulk", tags={"jira-server-other"})
    def jira_server_put_bulk(
        if_match: str | None = Field(None, description="Parameter If-Match"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update application roles"""
        api = get_api()
        response = api.jira_server_put_bulk(
            if_match=if_match,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_4", tags={"jira-server-other"})
    def jira_server_get_4(
        key: str = Field(..., description="the key of the role to use."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get application role by key"""
        api = get_api()
        response = api.jira_server_get_4(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_put_2", tags={"jira-server-other"})
    def jira_server_put_2(
        key: str = Field(..., description="the key of the role to update."),
        if_match: str | None = Field(None, description="Parameter If-Match"),
        version_hash: str | None = Field(
            None, description="the hash of the version to update. Optional Param"
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update application role"""
        api = get_api()
        response = api.jira_server_put_2(
            if_match=if_match,
            version_hash=version_hash,
            key=key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_attachment_meta", tags={"jira-server-issue-attachment"}
    )
    def jira_server_get_attachment_meta(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachment capabilities"""
        api = get_api()
        response = api.jira_server_get_attachment_meta()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_attachment", tags={"jira-server-issue-attachment"})
    def jira_server_get_attachment(
        id_: str = Field(..., description="id of the attachment to view"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the meta-data for an attachment, including the URI of the actual attached file"""
        api = get_api()
        response = api.jira_server_get_attachment(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_remove_attachment", tags={"jira-server-issue-attachment"}
    )
    def jira_server_remove_attachment(
        id_: str = Field(..., description="id of the attachment to remove"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete an attachment from an issue"""
        api = get_api()
        response = api.jira_server_remove_attachment(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_expand_for_humans", tags={"jira-server-other"})
    def jira_server_expand_for_humans(
        id_: str = Field(..., description="the id of the attachment to expand."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get human-readable attachment expansion"""
        api = get_api()
        response = api.jira_server_expand_for_humans(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_expand_for_machines", tags={"jira-server-other"})
    def jira_server_expand_for_machines(
        id_: str = Field(..., description="the id of the attachment to expand."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get raw attachment expansion"""
        api = get_api()
        response = api.jira_server_expand_for_machines(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_system_avatars", tags={"jira-server-system"})
    def jira_server_get_all_system_avatars(
        type_: str = Field(..., description="the avatar type"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all system avatars"""
        api = get_api()
        response = api.jira_server_get_all_system_avatars(
            type_=type_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_request_current_index_from_node",
        tags={"jira-server-admin-index"},
    )
    def jira_server_request_current_index_from_node(
        node_id: str = Field(..., description="ID of the node to request index from"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Request node index snapshot"""
        api = get_api()
        response = api.jira_server_request_current_index_from_node(
            node_id=node_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_node", tags={"jira-server-other"})
    def jira_server_delete_node(
        node_id: str = Field(..., description="ID of the node to delete"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a cluster node"""
        api = get_api()
        response = api.jira_server_delete_node(
            node_id=node_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_change_node_state_to_offline", tags={"jira-server-other"}
    )
    def jira_server_change_node_state_to_offline(
        node_id: str = Field(..., description="ID of the node to change state"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update node state to offline"""
        api = get_api()
        response = api.jira_server_change_node_state_to_offline(
            node_id=node_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_nodes", tags={"jira-server-other"})
    def jira_server_get_all_nodes(_ctx: Context | None = None) -> dict[str, Any]:
        """Get all cluster nodes"""
        api = get_api()
        response = api.jira_server_get_all_nodes()
        return response.model_dump()

    @mcp.tool(name="jira_server_approve_upgrade", tags={"jira-server-admin-upgrade"})
    def jira_server_approve_upgrade(_ctx: Context | None = None) -> dict[str, Any]:
        """Approve cluster upgrade"""
        api = get_api()
        response = api.jira_server_approve_upgrade()
        return response.model_dump()

    @mcp.tool(name="jira_server_cancel_upgrade", tags={"jira-server-admin-upgrade"})
    def jira_server_cancel_upgrade(_ctx: Context | None = None) -> dict[str, Any]:
        """Cancel cluster upgrade"""
        api = get_api()
        response = api.jira_server_cancel_upgrade()
        return response.model_dump()

    @mcp.tool(name="jira_server_acknowledge_errors", tags={"jira-server-other"})
    def jira_server_acknowledge_errors(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Retry cluster upgrade"""
        api = get_api()
        response = api.jira_server_acknowledge_errors()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_set_ready_to_upgrade", tags={"jira-server-admin-upgrade"}
    )
    def jira_server_set_ready_to_upgrade(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Start cluster upgrade"""
        api = get_api()
        response = api.jira_server_set_ready_to_upgrade()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_state", tags={"jira-server-other"})
    def jira_server_get_state(_ctx: Context | None = None) -> dict[str, Any]:
        """Get cluster upgrade state"""
        api = get_api()
        response = api.jira_server_get_state()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_properties_keys_1_2", tags={"jira-server-other"})
    def jira_server_get_properties_keys_1_2(
        comment_id: str = Field(
            ..., description="the comment from which keys will be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get properties keys of a comment"""
        api = get_api()
        response = api.jira_server_get_properties_keys_1_2(
            comment_id=comment_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_comment_property", tags={"jira-server-other"})
    def jira_server_get_comment_property(
        property_key: str = Field(
            ..., description="the key of the property to return."
        ),
        comment_id: str = Field(
            ..., description="the comment from which the property will be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a property from a comment"""
        api = get_api()
        response = api.jira_server_get_comment_property(
            property_key=property_key,
            comment_id=comment_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_property_1_2", tags={"jira-server-other"})
    def jira_server_set_property_1_2(
        property_key: str = Field(
            ...,
            description="the key of the comment's property. The maximum length of the key is 255 bytes.",
        ),
        comment_id: str = Field(
            ..., description="the comment on which the property will be set."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set a property on a comment"""
        api = get_api()
        response = api.jira_server_set_property_1_2(
            property_key=property_key,
            comment_id=comment_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_property_2", tags={"jira-server-other"})
    def jira_server_delete_property_2(
        property_key: str = Field(
            ..., description="the key of the property to remove."
        ),
        comment_id: str = Field(
            ..., description="the comment from which the property will be removed."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a property from a comment"""
        api = get_api()
        response = api.jira_server_delete_property_2(
            property_key=property_key,
            comment_id=comment_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_component", tags={"jira-server-other"})
    def jira_server_create_component(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create component"""
        api = get_api()
        response = api.jira_server_create_component(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_paginated_components", tags={"jira-server-other"})
    def jira_server_get_paginated_components(
        max_results: str | None = Field(
            None, description="the maximum number of components to return"
        ),
        query: str | None = Field(
            None, description="the string that components names will be matched with"
        ),
        project_ids: str | None = Field(
            None, description="the set of project ids to filter components"
        ),
        start_at: str | None = Field(
            None, description="the index of the first components to return"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get paginated components"""
        api = get_api()
        response = api.jira_server_get_paginated_components(
            max_results=max_results,
            query=query,
            project_ids=project_ids,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_component", tags={"jira-server-other"})
    def jira_server_get_component(
        id_: str = Field(..., description="a String containing the component key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get project component"""
        api = get_api()
        response = api.jira_server_get_component(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_component", tags={"jira-server-other"})
    def jira_server_update_component(
        id_: str = Field(..., description="The component to delete."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a component"""
        api = get_api()
        response = api.jira_server_update_component(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete", tags={"jira-server-other"})
    def jira_server_delete(
        id_: str = Field(..., description="The component to delete."),
        move_issues_to: str | None = Field(
            None,
            description="The new component applied to issues whose 'id' component will be deleted. If this value is null, then the 'id' component is simply removed from the related issues.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a project component"""
        api = get_api()
        response = api.jira_server_delete(
            move_issues_to=move_issues_to,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_component_related_issues", tags={"jira-server-other"}
    )
    def jira_server_get_component_related_issues(
        id_: str = Field(..., description="a String containing the component id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get component related issues"""
        api = get_api()
        response = api.jira_server_get_component_related_issues(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_configuration_1", tags={"jira-server-other"})
    def jira_server_get_configuration_1(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get Jira configuration details"""
        api = get_api()
        response = api.jira_server_get_configuration_1()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_custom_field_option", tags={"jira-server-field"})
    def jira_server_get_custom_field_option(
        id_: str = Field(
            ..., description="a String containing an Custom Field Option id."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom field option by ID"""
        api = get_api()
        response = api.jira_server_get_custom_field_option(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_custom_fields", tags={"jira-server-field"})
    def jira_server_get_custom_fields(
        sort_column: str | None = Field(
            None, description="The column by which to sort the returned custom fields."
        ),
        types: str | None = Field(
            None,
            description="A list of custom field types to filter the custom fields.",
        ),
        search: str | None = Field(
            None, description="A query string used to search custom fields."
        ),
        max_results: str | None = Field(
            None, description="The maximum number of custom fields to return."
        ),
        sort_order: str | None = Field(
            None, description="The order in which to sort the returned custom fields."
        ),
        screen_ids: str | None = Field(
            None, description="A list of screen IDs to filter the custom fields."
        ),
        last_value_update: str | None = Field(
            None, description="The last value update to filter the custom fields."
        ),
        project_ids: str | None = Field(
            None, description="A list of project IDs to filter the custom fields."
        ),
        start_at: str | None = Field(
            None, description="The starting index of the returned custom fields."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom fields with pagination"""
        api = get_api()
        response = api.jira_server_get_custom_fields(
            sort_column=sort_column,
            types=types,
            search=search,
            max_results=max_results,
            sort_order=sort_order,
            screen_ids=screen_ids,
            last_value_update=last_value_update,
            project_ids=project_ids,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_bulk_delete_custom_fields", tags={"jira-server-field"})
    def jira_server_bulk_delete_custom_fields(
        ids: str = Field(..., description="A list of custom field IDs to delete."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete custom fields in bulk"""
        api = get_api()
        response = api.jira_server_bulk_delete_custom_fields(
            ids=ids,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_custom_field_options", tags={"jira-server-field"})
    def jira_server_get_custom_field_options(
        custom_field_id: str = Field(..., description="The ID of the custom field."),
        max_results: str | None = Field(
            None, description="The maximum number of results to return."
        ),
        issue_type_ids: str | None = Field(
            None, description="A list of issue type IDs in a context."
        ),
        query: str | None = Field(None, description="A string used to filter options."),
        sort_by_option_name: str | None = Field(
            None, description="Flag to sort options by their names."
        ),
        use_all_contexts: str | None = Field(
            None,
            description="Flag to fetch all options regardless of context, project IDs, or issue type IDs.",
        ),
        page: str | None = Field(None, description="The page of options to return."),
        project_ids: str | None = Field(
            None, description="A list of project IDs in a context."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get custom field options"""
        api = get_api()
        response = api.jira_server_get_custom_field_options(
            max_results=max_results,
            issue_type_ids=issue_type_ids,
            query=query,
            sort_by_option_name=sort_by_option_name,
            custom_field_id=custom_field_id,
            use_all_contexts=use_all_contexts,
            page=page,
            project_ids=project_ids,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_list", tags={"jira-server-other"})
    def jira_server_list(
        filter: str | None = Field(
            None,
            description="An optional filter that is applied to the list of dashboards.",
        ),
        max_results: str | None = Field(
            None,
            description="A hint as to the maximum number of dashboards to return in each call.",
        ),
        start_at: str | None = Field(
            None, description="The index of the first dashboard to return (0-based)."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all dashboards with optional filtering"""
        api = get_api()
        response = api.jira_server_list(
            filter=filter,
            max_results=max_results,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_dashboard_item_properties_keys",
        tags={"jira-server-other"},
    )
    def jira_server_get_dashboard_item_properties_keys(
        item_id: str = Field(
            ..., description="The dashboard item from which keys will be returned."
        ),
        dashboard_id: str = Field(..., description="The dashboard id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all properties keys for a dashboard item"""
        api = get_api()
        response = api.jira_server_get_dashboard_item_properties_keys(
            item_id=item_id,
            dashboard_id=dashboard_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_property_1_2", tags={"jira-server-other"})
    def jira_server_get_property_1_2(
        property_key: str = Field(
            ..., description="The key of the property to return."
        ),
        item_id: str = Field(
            ...,
            description="The dashboard item from which the property will be returned.",
        ),
        dashboard_id: str = Field(..., description="The dashboard id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a property from a dashboard item"""
        api = get_api()
        response = api.jira_server_get_property_1_2(
            property_key=property_key,
            item_id=item_id,
            dashboard_id=dashboard_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_set_dashboard_item_property", tags={"jira-server-other"}
    )
    def jira_server_set_dashboard_item_property(
        property_key: str = Field(
            ...,
            description="The key of the dashboard item's property. The maximum length of the key is 255 bytes.",
        ),
        item_id: str = Field(
            ..., description="The dashboard item on which the property will be set."
        ),
        dashboard_id: str = Field(..., description="The dashboard id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set a property on a dashboard item"""
        api = get_api()
        response = api.jira_server_set_dashboard_item_property(
            property_key=property_key,
            item_id=item_id,
            dashboard_id=dashboard_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_property_1_2", tags={"jira-server-other"})
    def jira_server_delete_property_1_2(
        property_key: str = Field(
            ..., description="The key of the property to remove."
        ),
        item_id: str = Field(
            ...,
            description="The dashboard item from which the property will be removed.",
        ),
        dashboard_id: str = Field(..., description="The dashboard id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a property from a dashboard item"""
        api = get_api()
        response = api.jira_server_delete_property_1_2(
            property_key=property_key,
            item_id=item_id,
            dashboard_id=dashboard_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_dashboard", tags={"jira-server-agile-board"})
    def jira_server_get_dashboard(
        id_: str = Field(..., description="The dashboard id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a single dashboard by ID"""
        api = get_api()
        response = api.jira_server_get_dashboard(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_download_email_templates", tags={"jira-server-other"})
    def jira_server_download_email_templates(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get email templates as zip file"""
        api = get_api()
        response = api.jira_server_download_email_templates()
        return response.model_dump()

    @mcp.tool(name="jira_server_upload_email_templates", tags={"jira-server-other"})
    def jira_server_upload_email_templates(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update email templates with zip file"""
        api = get_api()
        response = api.jira_server_upload_email_templates(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_apply_email_templates", tags={"jira-server-other"})
    def jira_server_apply_email_templates(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update email templates with previously uploaded pack"""
        api = get_api()
        response = api.jira_server_apply_email_templates()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_revert_email_templates_to_default", tags={"jira-server-other"}
    )
    def jira_server_revert_email_templates_to_default(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update email templates to default"""
        api = get_api()
        response = api.jira_server_revert_email_templates_to_default()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_email_types", tags={"jira-server-other"})
    def jira_server_get_email_types(_ctx: Context | None = None) -> dict[str, Any]:
        """Get email types for templates"""
        api = get_api()
        response = api.jira_server_get_email_types()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_fields", tags={"jira-server-field"})
    def jira_server_get_fields(_ctx: Context | None = None) -> dict[str, Any]:
        """Get all fields, both System and Custom"""
        api = get_api()
        response = api.jira_server_get_fields()
        return response.model_dump()

    @mcp.tool(name="jira_server_create_custom_field", tags={"jira-server-field"})
    def jira_server_create_custom_field(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a custom field using a definition"""
        api = get_api()
        response = api.jira_server_create_custom_field(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_filter", tags={"jira-server-filter"})
    def jira_server_create_filter(
        expand: str | None = Field(None, description="Parameter expand"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new filter"""
        api = get_api()
        response = api.jira_server_create_filter(
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_default_share_scope", tags={"jira-server-other"})
    def jira_server_get_default_share_scope(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get default share scope"""
        api = get_api()
        response = api.jira_server_get_default_share_scope()
        return response.model_dump()

    @mcp.tool(name="jira_server_set_default_share_scope", tags={"jira-server-other"})
    def jira_server_set_default_share_scope(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set default share scope"""
        api = get_api()
        response = api.jira_server_set_default_share_scope(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_favourite_filters", tags={"jira-server-filter"})
    def jira_server_get_favourite_filters(
        expand: str | None = Field(None, description="Parameter expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get favourite filters"""
        api = get_api()
        response = api.jira_server_get_favourite_filters(
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_filter", tags={"jira-server-filter"})
    def jira_server_get_filter(
        id_: str = Field(..., description="The filter id."),
        expand: str | None = Field(None, description="Parameter expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a filter by ID"""
        api = get_api()
        response = api.jira_server_get_filter(
            expand=expand,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_edit_filter", tags={"jira-server-filter"})
    def jira_server_edit_filter(
        id_: str = Field(..., description="The filter id."),
        expand: str | None = Field(None, description="Parameter expand"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update an existing filter"""
        api = get_api()
        response = api.jira_server_edit_filter(
            expand=expand,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_filter", tags={"jira-server-filter"})
    def jira_server_delete_filter(
        id_: str = Field(..., description="The ID of the filter to delete."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a filter"""
        api = get_api()
        response = api.jira_server_delete_filter(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_default_columns_1", tags={"jira-server-other"})
    def jira_server_default_columns_1(
        id_: str = Field(..., description="The filter id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get default columns for filter"""
        api = get_api()
        response = api.jira_server_default_columns_1(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_columns_1", tags={"jira-server-other"})
    def jira_server_set_columns_1(
        id_: str = Field(..., description="The filter id."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set default columns for filter"""
        api = get_api()
        response = api.jira_server_set_columns_1(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_reset_columns_1", tags={"jira-server-other"})
    def jira_server_reset_columns_1(
        id_: str = Field(..., description="The filter id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset columns for filter"""
        api = get_api()
        response = api.jira_server_reset_columns_1(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_share_permissions", tags={"jira-server-permission"})
    def jira_server_get_share_permissions(
        id_: str = Field(..., description="The filter id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all share permissions of filter"""
        api = get_api()
        response = api.jira_server_get_share_permissions(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_share_permission", tags={"jira-server-permission"})
    def jira_server_add_share_permission(
        id_: str = Field(..., description="The filter id."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add share permissions to filter"""
        api = get_api()
        response = api.jira_server_add_share_permission(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_share_permission", tags={"jira-server-permission"}
    )
    def jira_server_delete_share_permission(
        permission_id: str = Field(..., description="The permission id."),
        id_: str = Field(..., description="The filter id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove share permissions from filter"""
        api = get_api()
        response = api.jira_server_delete_share_permission(
            permission_id=permission_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_share_permission", tags={"jira-server-permission"})
    def jira_server_get_share_permission(
        permission_id: str = Field(..., description="The permission id."),
        id_: str = Field(..., description="The filter id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a single share permission of filter"""
        api = get_api()
        response = api.jira_server_get_share_permission(
            permission_id=permission_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_group", tags={"jira-server-group"})
    def jira_server_create_group(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a group with given parameters"""
        api = get_api()
        response = api.jira_server_create_group(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_remove_group", tags={"jira-server-group"})
    def jira_server_remove_group(
        groupname: str = Field(..., description="The name of the group to delete."),
        swap_group: str | None = Field(
            None, description="A different group to transfer the restrictions to."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a specified group"""
        api = get_api()
        response = api.jira_server_remove_group(
            groupname=groupname,
            swap_group=swap_group,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_users_from_group", tags={"jira-server-user"})
    def jira_server_get_users_from_group(
        groupname: str = Field(..., description="The group name."),
        include_inactive_users: str | None = Field(
            None, description="Include inactive users."
        ),
        max_results: str | None = Field(
            None, description="The maximum number of users to return."
        ),
        start_at: str | None = Field(
            None, description="The index of the first user in group to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get users from a specified group"""
        api = get_api()
        response = api.jira_server_get_users_from_group(
            include_inactive_users=include_inactive_users,
            max_results=max_results,
            groupname=groupname,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_user_to_group", tags={"jira-server-user"})
    def jira_server_add_user_to_group(
        groupname: str = Field(..., description="A name of requested group."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add a user to a specified group"""
        api = get_api()
        response = api.jira_server_add_user_to_group(
            groupname=groupname,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_remove_user_from_group", tags={"jira-server-user"})
    def jira_server_remove_user_from_group(
        groupname: str = Field(..., description="A name of requested group."),
        username: str = Field(..., description="User to remove from a group"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove a user from a specified group"""
        api = get_api()
        response = api.jira_server_remove_user_from_group(
            groupname=groupname,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_find_groups", tags={"jira-server-group"})
    def jira_server_find_groups(
        max_results: str | None = Field(
            None, description="Maximum number of results to return"
        ),
        query: str | None = Field(None, description="A String to match groups against"),
        exclude: str | None = Field(None, description="List of groups to exclude"),
        user_name: str | None = Field(None, description="Username for the context"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get groups matching a query"""
        api = get_api()
        response = api.jira_server_find_groups(
            max_results=max_results,
            query=query,
            exclude=exclude,
            user_name=user_name,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_find_users_and_groups", tags={"jira-server-user"})
    def jira_server_find_users_and_groups(
        issue_type_id: str | None = Field(
            None,
            description="The list of issue type ids to further restrict the search",
        ),
        max_results: str | None = Field(
            None, description="The maximum number of users to return"
        ),
        query: str | None = Field(
            None, description="A string used to search username, Name or e-mail address"
        ),
        show_avatar: str | None = Field(None, description="Show avatar"),
        project_id: str | None = Field(
            None, description="The list of project ids to further restrict the search"
        ),
        field_id: str | None = Field(None, description="The custom field id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get users and groups matching query with highlighting"""
        api = get_api()
        response = api.jira_server_find_users_and_groups(
            issue_type_id=issue_type_id,
            max_results=max_results,
            query=query,
            show_avatar=show_avatar,
            project_id=project_id,
            field_id=field_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_list_index_snapshot", tags={"jira-server-admin-index"})
    def jira_server_list_index_snapshot(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of available index snapshots"""
        api = get_api()
        response = api.jira_server_list_index_snapshot()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_index_snapshot", tags={"jira-server-admin-index"}
    )
    def jira_server_create_index_snapshot(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create index snapshot if not in progress"""
        api = get_api()
        response = api.jira_server_create_index_snapshot()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_is_index_snapshot_running", tags={"jira-server-admin-index"}
    )
    def jira_server_is_index_snapshot_running(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get index snapshot creation status"""
        api = get_api()
        response = api.jira_server_is_index_snapshot_running()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_index_summary", tags={"jira-server-admin-index"})
    def jira_server_get_index_summary(_ctx: Context | None = None) -> dict[str, Any]:
        """Get index condition summary"""
        api = get_api()
        response = api.jira_server_get_index_summary()
        return response.model_dump()

    @mcp.tool(name="jira_server_create_issue", tags={"jira-server-other"})
    def jira_server_create_issue(
        update_history: bool | None = Field(
            None, description="Parameter updateHistory"
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create an issue or sub-task from json"""
        api = get_api()
        response = api.jira_server_create_issue(
            update_history=update_history,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_archive_issues", tags={"jira-server-other"})
    def jira_server_archive_issues(
        notify_users: str | None = Field(
            None,
            description="Send the email with notification that the issue was updated to users that watch it. Admin or project admin permissions are required to disable the notification.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Archive list of issues"""
        api = get_api()
        response = api.jira_server_archive_issues(
            notify_users=notify_users,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_issues", tags={"jira-server-other"})
    def jira_server_create_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create an issue or sub-task from json - bulk operation."""
        api = get_api()
        response = api.jira_server_create_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_create_issue_meta_project_issue_types",
        tags={"jira-server-issue-type"},
    )
    def jira_server_get_create_issue_meta_project_issue_types(
        project_id_or_key: str = Field(..., description="Project id or key"),
        max_results: str | None = Field(
            None, description="How many results on the page should be included"
        ),
        start_at: str | None = Field(None, description="The page offset"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get metadata for project issue types"""
        api = get_api()
        response = api.jira_server_get_create_issue_meta_project_issue_types(
            project_id_or_key=project_id_or_key,
            max_results=max_results,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_create_issue_meta_fields", tags={"jira-server-field"}
    )
    def jira_server_get_create_issue_meta_fields(
        issue_type_id: str = Field(..., description="Issue type id"),
        project_id_or_key: str = Field(..., description="Project id or key"),
        max_results: str | None = Field(
            None, description="How many results on the page should be included"
        ),
        start_at: str | None = Field(None, description="The page offset"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get metadata for issue types used for creating issues"""
        api = get_api()
        response = api.jira_server_get_create_issue_meta_fields(
            issue_type_id=issue_type_id,
            project_id_or_key=project_id_or_key,
            max_results=max_results,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_picker_resource", tags={"jira-server-other"})
    def jira_server_get_issue_picker_resource(
        current_project_id: str | None = Field(
            None,
            description="the id of the project in context of which the request is executed",
        ),
        query: str | None = Field(None, description="the query"),
        current_issue_key: str | None = Field(
            None,
            description="the key of the issue in context of which the request is executed",
        ),
        show_sub_tasks: str | None = Field(
            None,
            description="if set to false, subtasks will not be included in the list",
        ),
        current_jql: str | None = Field(
            None, description="the JQL in context of which the request is executed"
        ),
        show_sub_task_parent: str | None = Field(
            None,
            description="if set to false and request is executed in context of a subtask, the parent issue will not be included in the auto-completion result, even if it matches the query",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get suggested issues for auto-completion"""
        api = get_api()
        response = api.jira_server_get_issue_picker_resource(
            current_project_id=current_project_id,
            query=query,
            current_issue_key=current_issue_key,
            show_sub_tasks=show_sub_tasks,
            current_jql=current_jql,
            show_sub_task_parent=show_sub_task_parent,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_reciprocal_remote_issue_link",
        tags={"jira-server-issue-link"},
    )
    def jira_server_create_reciprocal_remote_issue_link(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create reciprocal remote issue link"""
        api = get_api()
        response = api.jira_server_create_reciprocal_remote_issue_link(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_2", tags={"jira-server-other"})
    def jira_server_get_issue_2(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        expand: str | None = Field(
            None,
            description="The expand param is used to include, hidden by default, parts of response. This can be used to include: renderedFields, names, schema, transitions, operations, editmeta, changelog, versionedRepresentations.",
        ),
        fields: str | None = Field(
            None,
            description="The list of fields to return for the issue. By default, all fields are returned.",
        ),
        update_history: str | None = Field(
            None,
            description="The updateHistory param adds the issues retrieved by this method to the current user's issue history",
        ),
        properties: str | None = Field(
            None,
            description="The list of properties to return for the issue. By default no properties are returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue for key"""
        api = get_api()
        response = api.jira_server_get_issue_2(
            expand=expand,
            issue_id_or_key=issue_id_or_key,
            fields=fields,
            update_history=update_history,
            properties=properties,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_edit_issue", tags={"jira-server-other"})
    def jira_server_edit_issue(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        notify_users: str | None = Field(
            None,
            description="Send the email with notification that the issue was updated to users that watch it. Admin or project admin permissions are required to disable the notification.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Edit an issue from a JSON representation"""
        api = get_api()
        response = api.jira_server_edit_issue(
            issue_id_or_key=issue_id_or_key,
            notify_users=notify_users,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_issue", tags={"jira-server-other"})
    def jira_server_delete_issue(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        delete_subtasks: str | None = Field(
            None,
            description="A String of true or false indicating that any subtasks should also be deleted. If the issue has no subtasks this parameter is ignored. If the issue has subtasks and this parameter is missing or false, then the issue will not be deleted and an error will be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete an issue"""
        api = get_api()
        response = api.jira_server_delete_issue(
            delete_subtasks=delete_subtasks,
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_archive_issue", tags={"jira-server-other"})
    def jira_server_archive_issue(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        notify_users: str | None = Field(
            None,
            description="Send the email with notification that the issue was updated to users that watch it. Admin or project admin permissions are required to disable the notification.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Archive an issue"""
        api = get_api()
        response = api.jira_server_archive_issue(
            issue_id_or_key=issue_id_or_key,
            notify_users=notify_users,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_assign", tags={"jira-server-other"})
    def jira_server_assign(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign an issue to a user"""
        api = get_api()
        response = api.jira_server_assign(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_attachment", tags={"jira-server-issue-attachment"})
    def jira_server_add_attachment(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add one or more attachments to an issue"""
        api = get_api()
        response = api.jira_server_add_attachment(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_comments", tags={"jira-server-issue-comment"})
    def jira_server_get_comments(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        expand: str | None = Field(
            None,
            description="Optional flags: renderedBody (provides body rendered in HTML)",
        ),
        max_results: str | None = Field(
            None,
            description="How many results on the page should be included. Defaults to 50.",
        ),
        order_by: str | None = Field(None, description="Ordering of the results"),
        start_at: str | None = Field(
            None, description="The page offset, if not specified then defaults to 0"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get comments for an issue"""
        api = get_api()
        response = api.jira_server_get_comments(
            expand=expand,
            max_results=max_results,
            issue_id_or_key=issue_id_or_key,
            order_by=order_by,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_comment", tags={"jira-server-issue-comment"})
    def jira_server_add_comment(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        expand: str | None = Field(
            None,
            description="Optional flags: renderedBody (provides body rendered in HTML)",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add a comment"""
        api = get_api()
        response = api.jira_server_add_comment(
            expand=expand,
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_comment", tags={"jira-server-issue-comment"})
    def jira_server_get_comment(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        id_: str = Field(..., description="Comment id"),
        expand: str | None = Field(
            None,
            description="Optional flags: renderedBody (provides body rendered in HTML)",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a comment by id"""
        api = get_api()
        response = api.jira_server_get_comment(
            expand=expand,
            issue_id_or_key=issue_id_or_key,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_comment", tags={"jira-server-issue-comment"})
    def jira_server_update_comment(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        id_: str = Field(..., description="Comment id"),
        expand: str | None = Field(
            None,
            description="Optional flags: renderedBody (provides body rendered in HTML)",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a comment"""
        api = get_api()
        response = api.jira_server_update_comment(
            expand=expand,
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_comment", tags={"jira-server-issue-comment"})
    def jira_server_delete_comment(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        id_: str = Field(..., description="Comment id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a comment"""
        api = get_api()
        response = api.jira_server_delete_comment(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_pin_comment", tags={"jira-server-issue-comment"})
    def jira_server_set_pin_comment(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        id_: str = Field(..., description="Comment id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Pin a comment"""
        api = get_api()
        response = api.jira_server_set_pin_comment(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_edit_issue_meta", tags={"jira-server-other"})
    def jira_server_get_edit_issue_meta(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get metadata for issue types used for editing issues"""
        api = get_api()
        response = api.jira_server_get_edit_issue_meta(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_notify", tags={"jira-server-other"})
    def jira_server_notify(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Send notification to recipients"""
        api = get_api()
        response = api.jira_server_notify(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_pinned_comments", tags={"jira-server-issue-comment"}
    )
    def jira_server_get_pinned_comments(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get pinned comments for an issue"""
        api = get_api()
        response = api.jira_server_get_pinned_comments(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_properties_keys", tags={"jira-server-other"})
    def jira_server_get_issue_properties_keys(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get keys of all properties for an issue"""
        api = get_api()
        response = api.jira_server_get_issue_properties_keys(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_property_3", tags={"jira-server-other"})
    def jira_server_get_property_3(
        property_key: str = Field(..., description="The key of the property to return"),
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the value of a specific property from an issue"""
        api = get_api()
        response = api.jira_server_get_property_3(
            property_key=property_key,
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_issue_property", tags={"jira-server-other"})
    def jira_server_set_issue_property(
        property_key: str = Field(..., description="The key of the issue's property"),
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update the value of a specific issue's property"""
        api = get_api()
        response = api.jira_server_set_issue_property(
            property_key=property_key,
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_property_3", tags={"jira-server-other"})
    def jira_server_delete_property_3(
        property_key: str = Field(..., description="The key of the property to remove"),
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a property from an issue"""
        api = get_api()
        response = api.jira_server_delete_property_3(
            property_key=property_key,
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_remote_issue_links", tags={"jira-server-issue-link"}
    )
    def jira_server_get_remote_issue_links(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        global_id: str | None = Field(
            None, description="Global id of the remote issue link"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get remote issue links for an issue"""
        api = get_api()
        response = api.jira_server_get_remote_issue_links(
            issue_id_or_key=issue_id_or_key,
            global_id=global_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_or_update_remote_issue_link",
        tags={"jira-server-issue-link"},
    )
    def jira_server_create_or_update_remote_issue_link(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create or update remote issue link"""
        api = get_api()
        response = api.jira_server_create_or_update_remote_issue_link(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_remote_issue_link_by_global_id",
        tags={"jira-server-issue-link"},
    )
    def jira_server_delete_remote_issue_link_by_global_id(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        global_id: str = Field(..., description="Global id of the remote issue link"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete remote issue link"""
        api = get_api()
        response = api.jira_server_delete_remote_issue_link_by_global_id(
            issue_id_or_key=issue_id_or_key,
            global_id=global_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_remote_issue_link_by_id", tags={"jira-server-issue-link"}
    )
    def jira_server_get_remote_issue_link_by_id(
        link_id: str = Field(..., description="Id of the remote issue link"),
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a remote issue link by its id"""
        api = get_api()
        response = api.jira_server_get_remote_issue_link_by_id(
            link_id=link_id,
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_remote_issue_link", tags={"jira-server-issue-link"}
    )
    def jira_server_update_remote_issue_link(
        link_id: str = Field(..., description="Id of the remote issue link"),
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update remote issue link"""
        api = get_api()
        response = api.jira_server_update_remote_issue_link(
            link_id=link_id,
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_remote_issue_link_by_id",
        tags={"jira-server-issue-link"},
    )
    def jira_server_delete_remote_issue_link_by_id(
        link_id: str = Field(..., description="Id of the remote issue link"),
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete remote issue link by id"""
        api = get_api()
        response = api.jira_server_delete_remote_issue_link_by_id(
            link_id=link_id,
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_restore_issue", tags={"jira-server-other"})
    def jira_server_restore_issue(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        notify_users: str | None = Field(
            None,
            description="Send the email with notification that the issue was updated to users that watch it. Admin or project admin permissions are required to disable the notification.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Restore an archived issue"""
        api = get_api()
        response = api.jira_server_restore_issue(
            issue_id_or_key=issue_id_or_key,
            notify_users=notify_users,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_sub_tasks", tags={"jira-server-issue-subtask"})
    def jira_server_get_sub_tasks(
        issue_id_or_key: str = Field(..., description="The parent issue's key or id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get an issue's subtask list"""
        api = get_api()
        response = api.jira_server_get_sub_tasks(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_can_move_sub_task", tags={"jira-server-issue-subtask"})
    def jira_server_can_move_sub_task(
        issue_id_or_key: str = Field(..., description="The parent issue's key or id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Check if a subtask can be moved"""
        api = get_api()
        response = api.jira_server_can_move_sub_task(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_move_sub_tasks", tags={"jira-server-issue-subtask"})
    def jira_server_move_sub_tasks(
        issue_id_or_key: str = Field(..., description="The parent issue's key or id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reorder an issue's subtasks"""
        api = get_api()
        response = api.jira_server_move_sub_tasks(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_transitions", tags={"jira-server-issue-transition"})
    def jira_server_get_transitions(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        transition_id: str | None = Field(None, description="Transition id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of transitions possible for an issue"""
        api = get_api()
        response = api.jira_server_get_transitions(
            transition_id=transition_id,
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_do_transition", tags={"jira-server-issue-transition"})
    def jira_server_do_transition(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Perform a transition on an issue"""
        api = get_api()
        response = api.jira_server_do_transition(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_votes", tags={"jira-server-issue-vote"})
    def jira_server_get_votes(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get votes for issue"""
        api = get_api()
        response = api.jira_server_get_votes(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_vote", tags={"jira-server-issue-vote"})
    def jira_server_add_vote(
        issue_id_or_key: str = Field(..., description="Issue id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add vote to issue"""
        api = get_api()
        response = api.jira_server_add_vote(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_remove_vote", tags={"jira-server-issue-vote"})
    def jira_server_remove_vote(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove vote from issue"""
        api = get_api()
        response = api.jira_server_remove_vote(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_watchers", tags={"jira-server-issue-watcher"})
    def jira_server_get_issue_watchers(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of watchers of issue"""
        api = get_api()
        response = api.jira_server_get_issue_watchers(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_watcher_1", tags={"jira-server-issue-watcher"})
    def jira_server_add_watcher_1(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        user_name: str | None = Field(
            None,
            description="The name of the user to add to the watcher list. If no name is specified, the current user is added.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add a user as watcher"""
        api = get_api()
        response = api.jira_server_add_watcher_1(
            issue_id_or_key=issue_id_or_key,
            user_name=user_name,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_remove_watcher_1", tags={"jira-server-issue-watcher"})
    def jira_server_remove_watcher_1(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        user_name: str | None = Field(
            None, description="The name of the user to remove from the watcher list."
        ),
        username: str | None = Field(None, description="Parameter username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete watcher from issue"""
        api = get_api()
        response = api.jira_server_remove_watcher_1(
            issue_id_or_key=issue_id_or_key,
            user_name=user_name,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_worklog", tags={"jira-server-issue-worklog"})
    def jira_server_get_issue_worklog(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get worklogs for an issue"""
        api = get_api()
        response = api.jira_server_get_issue_worklog(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_worklog", tags={"jira-server-issue-worklog"})
    def jira_server_add_worklog(
        issue_id_or_key: str = Field(
            ...,
            description="a string containing the issue id or key the worklog will be added to",
        ),
        new_estimate: str | None = Field(
            None,
            description="Required when 'new' is selected for adjustEstimate. e.g. '2d'",
        ),
        adjust_estimate: str | None = Field(
            None,
            description="Allows you to provide specific instructions to update the remaining time estimate of the issue. Valid values are: new, leave, manual, auto",
        ),
        reduce_by: str | None = Field(
            None,
            description="Required when 'manual' is selected for adjustEstimate. e.g. '2d'",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add a worklog entry"""
        api = get_api()
        response = api.jira_server_add_worklog(
            new_estimate=new_estimate,
            adjust_estimate=adjust_estimate,
            reduce_by=reduce_by,
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_worklog", tags={"jira-server-issue-worklog"})
    def jira_server_get_worklog(
        issue_id_or_key: str = Field(..., description="Issue id or key"),
        id_: str = Field(..., description="Worklog id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a worklog by id"""
        api = get_api()
        response = api.jira_server_get_worklog(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_worklog", tags={"jira-server-issue-worklog"})
    def jira_server_update_worklog(
        issue_id_or_key: str = Field(
            ...,
            description="a string containing the issue id or key the worklog belongs to",
        ),
        id_: str = Field(..., description="id of the worklog to be updated"),
        new_estimate: str | None = Field(
            None, description="required when 'new' is selected for adjustEstimate"
        ),
        adjust_estimate: str | None = Field(
            None,
            description="allows you to provide specific instructions to update the remaining time estimate of the issue. Valid values are: new, leave, auto",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a worklog entry"""
        api = get_api()
        response = api.jira_server_update_worklog(
            new_estimate=new_estimate,
            adjust_estimate=adjust_estimate,
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_worklog", tags={"jira-server-issue-worklog"})
    def jira_server_delete_worklog(
        issue_id_or_key: str = Field(
            ...,
            description="a string containing the issue id or key the worklog belongs to",
        ),
        id_: str = Field(..., description="Id of the worklog to be deleted"),
        new_estimate: str | None = Field(
            None,
            description="Required when 'new' is selected for adjustEstimate. e.g. '2d'",
        ),
        adjust_estimate: str | None = Field(
            None,
            description="Allows you to provide specific instructions to update the remaining time estimate of the issue. Valid values are: new, leave, manual, auto",
        ),
        increase_by: str | None = Field(
            None,
            description="Required when 'manual' is selected for adjustEstimate. e.g. '2d'",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a worklog entry"""
        api = get_api()
        response = api.jira_server_delete_worklog(
            new_estimate=new_estimate,
            adjust_estimate=adjust_estimate,
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            increase_by=increase_by,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_link_issues", tags={"jira-server-other"})
    def jira_server_link_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create an issue link between two issues"""
        api = get_api()
        response = api.jira_server_link_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_link", tags={"jira-server-issue-link-type"})
    def jira_server_get_issue_link(
        link_id: str = Field(..., description="The issue link id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get an issue link with the specified id"""
        api = get_api()
        response = api.jira_server_get_issue_link(
            link_id=link_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_issue_link", tags={"jira-server-issue-link-type"}
    )
    def jira_server_delete_issue_link(
        link_id: str = Field(..., description="The issue link id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete an issue link with the specified id"""
        api = get_api()
        response = api.jira_server_delete_issue_link(
            link_id=link_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issue_link_types", tags={"jira-server-issue-link-type"}
    )
    def jira_server_get_issue_link_types(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of available issue link types"""
        api = get_api()
        response = api.jira_server_get_issue_link_types()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_issue_link_type", tags={"jira-server-issue-link-type"}
    )
    def jira_server_create_issue_link_type(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new issue link type"""
        api = get_api()
        response = api.jira_server_create_issue_link_type(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_reset_order", tags={"jira-server-other"})
    def jira_server_reset_order(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset the order of issue link types alphabetically."""
        api = get_api()
        response = api.jira_server_reset_order(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issue_link_type", tags={"jira-server-issue-link-type"}
    )
    def jira_server_get_issue_link_type(
        issue_link_type_id: str = Field(..., description="The issue link type id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get information about an issue link type"""
        api = get_api()
        response = api.jira_server_get_issue_link_type(
            issue_link_type_id=issue_link_type_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_issue_link_type", tags={"jira-server-issue-link-type"}
    )
    def jira_server_update_issue_link_type(
        issue_link_type_id: str = Field(..., description="The issue link type id."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update the specified issue link type"""
        api = get_api()
        response = api.jira_server_update_issue_link_type(
            issue_link_type_id=issue_link_type_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_issue_link_type", tags={"jira-server-issue-link-type"}
    )
    def jira_server_delete_issue_link_type(
        issue_link_type_id: str = Field(..., description="The issue link type id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete the specified issue link type"""
        api = get_api()
        response = api.jira_server_delete_issue_link_type(
            issue_link_type_id=issue_link_type_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_move_issue_link_type", tags={"jira-server-issue-link-type"}
    )
    def jira_server_move_issue_link_type(
        issue_link_type_id: str = Field(
            ..., description="Id of the issue link type to move."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update the order of the issue link type."""
        api = get_api()
        response = api.jira_server_move_issue_link_type(
            issue_link_type_id=issue_link_type_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_security_schemes", tags={"jira-server-other"})
    def jira_server_get_issue_security_schemes(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issue security schemes"""
        api = get_api()
        response = api.jira_server_get_issue_security_schemes()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_security_scheme", tags={"jira-server-other"})
    def jira_server_get_issue_security_scheme(
        id_: str = Field(..., description="The issue security scheme id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get specific issue security scheme by id"""
        api = get_api()
        response = api.jira_server_get_issue_security_scheme(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_all_types", tags={"jira-server-other"})
    def jira_server_get_issue_all_types(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of all issue types visible to user"""
        api = get_api()
        response = api.jira_server_get_issue_all_types()
        return response.model_dump()

    @mcp.tool(name="jira_server_create_issue_type", tags={"jira-server-issue-type"})
    def jira_server_create_issue_type(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create an issue type from JSON representation"""
        api = get_api()
        response = api.jira_server_create_issue_type(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_paginated_issue_types", tags={"jira-server-issue-type"}
    )
    def jira_server_get_paginated_issue_types(
        x_requested_with: str | None = Field(
            None, description="Parameter X-Requested-With"
        ),
        max_results: int | None = Field(
            None, description="The maximum number of issue types to return."
        ),
        query: str | None = Field(
            None, description="The string that issue type names will be matched with."
        ),
        project_ids: list[Any] | None = Field(
            None, description="The set of project ids to filter issue types."
        ),
        start_at: int | None = Field(
            None, description="The index of the first issue type to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get paginated list of filtered issue types"""
        api = get_api()
        response = api.jira_server_get_paginated_issue_types(
            x_requested_with=x_requested_with,
            max_results=max_results,
            query=query,
            project_ids=project_ids,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_type_1", tags={"jira-server-issue-type"})
    def jira_server_get_issue_type_1(
        id_: str = Field(..., description="The issue type id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get full representation of issue type by id"""
        api = get_api()
        response = api.jira_server_get_issue_type_1(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_issue_type", tags={"jira-server-issue-type"})
    def jira_server_update_issue_type(
        id_: str = Field(..., description="The issue type id."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update specified issue type from JSON representation"""
        api = get_api()
        response = api.jira_server_update_issue_type(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_issue_type_1", tags={"jira-server-issue-type"})
    def jira_server_delete_issue_type_1(
        id_: str = Field(..., description="The issue type id."),
        alternative_issue_type_id: str = Field(
            ...,
            description="The id of an issue type to which issues associated with the removed issue type will be migrated.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete specified issue type and migrate associated issues"""
        api = get_api()
        response = api.jira_server_delete_issue_type_1(
            id_=id_,
            alternative_issue_type_id=alternative_issue_type_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_alternative_issue_types", tags={"jira-server-issue-type"}
    )
    def jira_server_get_alternative_issue_types(
        id_: str = Field(..., description="The issue type id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of alternative issue types for given id"""
        api = get_api()
        response = api.jira_server_get_alternative_issue_types(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_avatar_from_temporary", tags={"jira-server-other"}
    )
    def jira_server_create_avatar_from_temporary(
        id_: str = Field(..., description="The issue type id."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Convert temporary avatar into a real avatar"""
        api = get_api()
        response = api.jira_server_create_avatar_from_temporary(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_store_temporary_avatar_using_multi_part",
        tags={"jira-server-other"},
    )
    def jira_server_store_temporary_avatar_using_multi_part(
        id_: str = Field(..., description="The issue type id."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create temporary avatar using multipart for issue type"""
        api = get_api()
        response = api.jira_server_store_temporary_avatar_using_multi_part(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_property_keys", tags={"jira-server-other"})
    def jira_server_get_property_keys(
        issue_type_id: str = Field(
            ..., description="The issue type from which the keys will be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all properties keys for issue type"""
        api = get_api()
        response = api.jira_server_get_property_keys(
            issue_type_id=issue_type_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_property_4", tags={"jira-server-other"})
    def jira_server_get_property_4(
        property_key: str = Field(
            ..., description="The key of the property to return."
        ),
        issue_type_id: str = Field(
            ..., description="The issue type from which the property will be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get value of specified issue type's property"""
        api = get_api()
        response = api.jira_server_get_property_4(
            property_key=property_key,
            issue_type_id=issue_type_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_property_3", tags={"jira-server-other"})
    def jira_server_set_property_3(
        property_key: str = Field(
            ...,
            description="The key of the issue type's property. The maximum length of the key is 255 bytes",
        ),
        issue_type_id: str = Field(
            ..., description="The issue type on which the property will be set."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update specified issue type's property"""
        api = get_api()
        response = api.jira_server_set_property_3(
            property_key=property_key,
            issue_type_id=issue_type_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_property_4", tags={"jira-server-other"})
    def jira_server_delete_property_4(
        property_key: str = Field(
            ..., description="The key of the property to remove."
        ),
        issue_type_id: str = Field(
            ..., description="The issue type from which the property will be removed."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete specified issue type's property"""
        api = get_api()
        response = api.jira_server_delete_property_4(
            property_key=property_key,
            issue_type_id=issue_type_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_all_issue_type_schemes",
        tags={"jira-server-issue-type-scheme"},
    )
    def jira_server_get_all_issue_type_schemes(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of all issue type schemes visible to user"""
        api = get_api()
        response = api.jira_server_get_all_issue_type_schemes()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_issue_type_scheme",
        tags={"jira-server-issue-type-scheme"},
    )
    def jira_server_create_issue_type_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create an issue type scheme from JSON representation"""
        api = get_api()
        response = api.jira_server_create_issue_type_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issue_type_scheme", tags={"jira-server-issue-type-scheme"}
    )
    def jira_server_get_issue_type_scheme(
        scheme_id: str = Field(
            ..., description="A String containing an issue type scheme's id."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get full representation of issue type scheme by id"""
        api = get_api()
        response = api.jira_server_get_issue_type_scheme(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_issue_type_scheme",
        tags={"jira-server-issue-type-scheme"},
    )
    def jira_server_update_issue_type_scheme(
        scheme_id: str = Field(
            ..., description="The id of the issue type scheme to update."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update specified issue type scheme from JSON representation"""
        api = get_api()
        response = api.jira_server_update_issue_type_scheme(
            scheme_id=scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_issue_type_scheme",
        tags={"jira-server-issue-type-scheme"},
    )
    def jira_server_delete_issue_type_scheme(
        scheme_id: str = Field(
            ..., description="The id of the issue type scheme to remove."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete specified issue type scheme"""
        api = get_api()
        response = api.jira_server_delete_issue_type_scheme(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_associated_projects", tags={"jira-server-project"})
    def jira_server_get_associated_projects(
        scheme_id: str = Field(
            ...,
            description="Id of the issue type scheme whose projects we're accessing",
        ),
        expand: str | None = Field(None, description="Parameter expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all of the associated projects for specified scheme"""
        api = get_api()
        response = api.jira_server_get_associated_projects(
            expand=expand,
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_set_project_associations_for_scheme",
        tags={"jira-server-project"},
    )
    def jira_server_set_project_associations_for_scheme(
        scheme_id: str = Field(
            ...,
            description="The id of the issue type scheme whose project associations we're replacing.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set project associations for scheme"""
        api = get_api()
        response = api.jira_server_set_project_associations_for_scheme(
            scheme_id=scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_add_project_associations_to_scheme",
        tags={"jira-server-project"},
    )
    def jira_server_add_project_associations_to_scheme(
        scheme_id: str = Field(
            ...,
            description="The id of the issue type scheme whose project associations we're adding to.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add project associations to scheme"""
        api = get_api()
        response = api.jira_server_add_project_associations_to_scheme(
            scheme_id=scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_remove_all_project_associations", tags={"jira-server-project"}
    )
    def jira_server_remove_all_project_associations(
        scheme_id: str = Field(
            ...,
            description="The id of the issue type scheme whose project associations we're removing",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove all project associations for specified scheme"""
        api = get_api()
        response = api.jira_server_remove_all_project_associations(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_remove_project_association", tags={"jira-server-project"}
    )
    def jira_server_remove_project_association(
        proj_id_or_key: str = Field(
            ...,
            description="The id or key of the project that is to be un-associated with the issue type scheme",
        ),
        scheme_id: str = Field(
            ...,
            description="The id of the issue type scheme whose project association we're removing",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove given project association for specified scheme"""
        api = get_api()
        response = api.jira_server_remove_project_association(
            proj_id_or_key=proj_id_or_key,
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_auto_complete", tags={"jira-server-other"})
    def jira_server_get_auto_complete(_ctx: Context | None = None) -> dict[str, Any]:
        """Get auto complete data for JQL searches"""
        api = get_api()
        response = api.jira_server_get_auto_complete()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_field_auto_complete_for_query_string",
        tags={"jira-server-field"},
    )
    def jira_server_get_field_auto_complete_for_query_string(
        predicate_value: str | None = Field(
            None,
            description="The portion of the predicate value that has already been provided by the user.",
        ),
        predicate_name: str | None = Field(
            None,
            description="The predicate for which the suggestions are generated. Suggestions are generated only for: 'by', 'from' and 'to'.",
        ),
        field_name: str | None = Field(
            None, description="The field name for which the suggestions are generated."
        ),
        field_value: str | None = Field(
            None,
            description="The portion of the field value that has already been provided by the user.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get auto complete suggestions for JQL search"""
        api = get_api()
        response = api.jira_server_get_field_auto_complete_for_query_string(
            predicate_value=predicate_value,
            predicate_name=predicate_name,
            field_name=field_name,
            field_value=field_value,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_validate", tags={"jira-server-other"})
    def jira_server_validate(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Validate a Jira license"""
        api = get_api()
        response = api.jira_server_validate(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_is_app_monitoring_enabled", tags={"jira-server-other"})
    def jira_server_is_app_monitoring_enabled(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get App Monitoring status"""
        api = get_api()
        response = api.jira_server_is_app_monitoring_enabled()
        return response.model_dump()

    @mcp.tool(name="jira_server_set_app_monitoring_enabled", tags={"jira-server-other"})
    def jira_server_set_app_monitoring_enabled(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update App Monitoring status"""
        api = get_api()
        response = api.jira_server_set_app_monitoring_enabled(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_is_ipd_monitoring_enabled", tags={"jira-server-other"})
    def jira_server_is_ipd_monitoring_enabled(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get if IPD Monitoring is enabled"""
        api = get_api()
        response = api.jira_server_is_ipd_monitoring_enabled()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_set_app_monitoring_enabled_1", tags={"jira-server-other"}
    )
    def jira_server_set_app_monitoring_enabled_1(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update IPD Monitoring status"""
        api = get_api()
        response = api.jira_server_set_app_monitoring_enabled_1(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_are_metrics_exposed", tags={"jira-server-other"})
    def jira_server_are_metrics_exposed(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Check if JMX metrics are being exposed"""
        api = get_api()
        response = api.jira_server_are_metrics_exposed()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_available_metrics", tags={"jira-server-other"})
    def jira_server_get_available_metrics(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the available JMX metrics"""
        api = get_api()
        response = api.jira_server_get_available_metrics()
        return response.model_dump()

    @mcp.tool(name="jira_server_start", tags={"jira-server-other"})
    def jira_server_start(_ctx: Context | None = None) -> dict[str, Any]:
        """Start exposing JMX metrics"""
        api = get_api()
        response = api.jira_server_start()
        return response.model_dump()

    @mcp.tool(name="jira_server_stop", tags={"jira-server-other"})
    def jira_server_stop(_ctx: Context | None = None) -> dict[str, Any]:
        """Stop exposing JMX metrics"""
        api = get_api()
        response = api.jira_server_stop()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_permissions", tags={"jira-server-permission"})
    def jira_server_get_permissions(
        issue_id: str | None = Field(
            None, description="id of the issue to scope returned permissions for."
        ),
        project_key: str | None = Field(
            None, description="key of project to scope returned permissions for."
        ),
        issue_key: str | None = Field(
            None, description="key of the issue to scope returned permissions for."
        ),
        project_id: str | None = Field(
            None, description="id of project to scope returned permissions for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get permissions for the logged in user"""
        api = get_api()
        response = api.jira_server_get_permissions(
            issue_id=issue_id,
            project_key=project_key,
            issue_key=issue_key,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_preference", tags={"jira-server-other"})
    def jira_server_get_preference(
        key: str | None = Field(
            None, description="Key of the preference to be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user preference by key"""
        api = get_api()
        response = api.jira_server_get_preference(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_preference", tags={"jira-server-other"})
    def jira_server_set_preference(
        key: str | None = Field(None, description="Key of the preference to be set."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update user preference"""
        api = get_api()
        response = api.jira_server_set_preference(
            key=key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_remove_preference", tags={"jira-server-other"})
    def jira_server_remove_preference(
        key: str | None = Field(
            None, description="Key of the preference to be removed."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete user preference"""
        api = get_api()
        response = api.jira_server_remove_preference(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_user", tags={"jira-server-user"})
    def jira_server_get_user(_ctx: Context | None = None) -> dict[str, Any]:
        """Get currently logged user"""
        api = get_api()
        response = api.jira_server_get_user()
        return response.model_dump()

    @mcp.tool(name="jira_server_update_user", tags={"jira-server-user"})
    def jira_server_update_user(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update currently logged user"""
        api = get_api()
        response = api.jira_server_update_user(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_change_my_password", tags={"jira-server-other"})
    def jira_server_change_my_password(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update caller password"""
        api = get_api()
        response = api.jira_server_change_my_password(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_notification_schemes", tags={"jira-server-other"})
    def jira_server_get_notification_schemes(
        expand: str | None = Field(
            None,
            description="Optional information to be expanded in the response: group, user, projectRole or field.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of notification schemes to return (max 50).",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first notification scheme to return (0 based).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get paginated notification schemes"""
        api = get_api()
        response = api.jira_server_get_notification_schemes(
            expand=expand,
            max_results=max_results,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_notification_scheme", tags={"jira-server-other"})
    def jira_server_get_notification_scheme(
        id_: int = Field(
            ..., description="The id of the notification scheme to retrieve"
        ),
        expand: str | None = Field(
            None,
            description="Optional information to be expanded in the response: group, user, projectRole or field.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get full notification scheme details"""
        api = get_api()
        response = api.jira_server_get_notification_scheme(
            expand=expand,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_password_policy", tags={"jira-server-other"})
    def jira_server_get_password_policy(
        has_old_password: bool | None = Field(
            None,
            description="Whether or not the user will be required to enter their current password.  Use false (the default) if this is a new user or if an administrator is forcibly changing another user's password.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get current password policy requirements"""
        api = get_api()
        response = api.jira_server_get_password_policy(
            has_old_password=has_old_password,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_policy_check_create_user", tags={"jira-server-user"})
    def jira_server_policy_check_create_user(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get reasons for password policy disallowance on user creation"""
        api = get_api()
        response = api.jira_server_policy_check_create_user(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_policy_check_update_user", tags={"jira-server-user"})
    def jira_server_policy_check_update_user(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get reasons for password policy disallowance on user password update"""
        api = get_api()
        response = api.jira_server_policy_check_update_user(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_permissions", tags={"jira-server-permission"})
    def jira_server_get_all_permissions(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all permissions present in Jira instance"""
        api = get_api()
        response = api.jira_server_get_all_permissions()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_permission_schemes",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_get_permission_schemes(
        expand: str | None = Field(
            None,
            description="Use expand to include full beans in the response. This parameter accepts a comma-separated list of expandable elements. Use 'permissions' to include permissions in the response.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all permission schemes"""
        api = get_api()
        response = api.jira_server_get_permission_schemes(
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_permission_scheme",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_create_permission_scheme(
        expand: str | None = Field(
            None,
            description="Use expand to include full beans in the response. This parameter accepts a comma-separated list of expandable elements. Use 'permissions' to include permissions in the response.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new permission scheme"""
        api = get_api()
        response = api.jira_server_create_permission_scheme(
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_scheme_attribute", tags={"jira-server-other"})
    def jira_server_get_scheme_attribute(
        permission_scheme_id: int = Field(
            ..., description="The id of the permission scheme."
        ),
        attribute_key: str = Field(
            ..., description="The key of the permission scheme attribute."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get scheme attribute by key"""
        api = get_api()
        response = api.jira_server_get_scheme_attribute(
            permission_scheme_id=permission_scheme_id,
            attribute_key=attribute_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_scheme_attribute", tags={"jira-server-other"})
    def jira_server_set_scheme_attribute(
        permission_scheme_id: int = Field(
            ..., description="The id of the permission scheme."
        ),
        key: str = Field(
            ..., description="The key of the permission scheme attribute."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update or insert a scheme attribute"""
        api = get_api()
        response = api.jira_server_set_scheme_attribute(
            permission_scheme_id=permission_scheme_id,
            key=key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_permission_scheme", tags={"jira-server-permission-scheme"}
    )
    def jira_server_get_permission_scheme(
        scheme_id: int = Field(..., description="The id of the permission scheme."),
        expand: str | None = Field(
            None,
            description="Use expand to include full beans in the response. This parameter accepts a comma-separated list of expandable elements. Use 'permissions' to include permissions in the response.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a permission scheme by ID"""
        api = get_api()
        response = api.jira_server_get_permission_scheme(
            expand=expand,
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_permission_scheme",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_update_permission_scheme(
        scheme_id: int = Field(..., description="The id of the permission scheme."),
        expand: str | None = Field(
            None,
            description="Use expand to include full beans in the response. This parameter accepts a comma-separated list of expandable elements. Use 'permissions' to include permissions in the response.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a permission scheme"""
        api = get_api()
        response = api.jira_server_update_permission_scheme(
            expand=expand,
            scheme_id=scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_permission_scheme",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_delete_permission_scheme(
        scheme_id: int = Field(..., description="The id of the permission scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a permission scheme by ID"""
        api = get_api()
        response = api.jira_server_delete_permission_scheme(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_permission_scheme_grants",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_get_permission_scheme_grants(
        scheme_id: int = Field(..., description="The id of the permission scheme."),
        expand: str | None = Field(
            None,
            description="Use expand to include full beans in the response. This parameter accepts a comma-separated list of expandable elements. Use 'permissions' to include permissions in the response.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all permission grants of a scheme"""
        api = get_api()
        response = api.jira_server_get_permission_scheme_grants(
            expand=expand,
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_permission_grant", tags={"jira-server-permission"}
    )
    def jira_server_create_permission_grant(
        scheme_id: int = Field(..., description="The id of the permission scheme."),
        expand: str | None = Field(
            None,
            description="Use expand to include full beans in the response. This parameter accepts a comma-separated list of expandable elements. Use 'permissions' to include permissions in the response.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a permission grant in a scheme"""
        api = get_api()
        response = api.jira_server_create_permission_grant(
            expand=expand,
            scheme_id=scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_permission_scheme_grant",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_get_permission_scheme_grant(
        permission_id: int = Field(..., description="The id of the permission grant."),
        scheme_id: int = Field(..., description="The id of the permission scheme."),
        expand: str | None = Field(
            None,
            description="Use expand to include full beans in the response. This parameter accepts a comma-separated list of expandable elements. Use 'permissions' to include permissions in the response.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a permission grant by ID"""
        api = get_api()
        response = api.jira_server_get_permission_scheme_grant(
            permission_id=permission_id,
            expand=expand,
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_permission_scheme_entity",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_delete_permission_scheme_entity(
        permission_id: int = Field(..., description="The id of the permission grant."),
        scheme_id: int = Field(..., description="The id of the permission scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a permission grant from a scheme"""
        api = get_api()
        response = api.jira_server_delete_permission_scheme_entity(
            permission_id=permission_id,
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_priorities", tags={"jira-server-other"})
    def jira_server_get_priorities(_ctx: Context | None = None) -> dict[str, Any]:
        """Get all issue priorities"""
        api = get_api()
        response = api.jira_server_get_priorities()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_priorities_1", tags={"jira-server-other"})
    def jira_server_get_priorities_1(
        max_results: int | None = Field(
            None,
            description="how many results on the page should be included. Defaults to 100",
        ),
        query: str | None = Field(
            None, description="query that should match priority name or its translation"
        ),
        project_ids: list[Any] | None = Field(
            None, description="the list of project ids to filter priorities"
        ),
        start_at: int | None = Field(
            None, description="the page offset, if not specified then defaults to 0"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get paginated issue priorities"""
        api = get_api()
        response = api.jira_server_get_priorities_1(
            max_results=max_results,
            query=query,
            project_ids=project_ids,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_priority", tags={"jira-server-priority"})
    def jira_server_get_priority(
        id_: str = Field(..., description="a String containing the priority id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get an issue priority by ID"""
        api = get_api()
        response = api.jira_server_get_priority(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_priority_schemes", tags={"jira-server-priority-scheme"}
    )
    def jira_server_get_priority_schemes(
        max_results: int | None = Field(
            None,
            description="how many results on the page should be included. Defaults to 100, maximum is 1000.",
        ),
        start_at: int | None = Field(
            None, description="the page offset, if not specified then defaults to 0"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all priority schemes"""
        api = get_api()
        response = api.jira_server_get_priority_schemes(
            max_results=max_results,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_priority_scheme", tags={"jira-server-priority-scheme"}
    )
    def jira_server_create_priority_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create new priority scheme"""
        api = get_api()
        response = api.jira_server_create_priority_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_priority_scheme", tags={"jira-server-priority-scheme"}
    )
    def jira_server_get_priority_scheme(
        scheme_id: int = Field(..., description="id of priority scheme to get"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a priority scheme by ID"""
        api = get_api()
        response = api.jira_server_get_priority_scheme(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_priority_scheme", tags={"jira-server-priority-scheme"}
    )
    def jira_server_update_priority_scheme(
        scheme_id: int = Field(..., description="id of the priority scheme to update"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a priority scheme"""
        api = get_api()
        response = api.jira_server_update_priority_scheme(
            scheme_id=scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_priority_scheme", tags={"jira-server-priority-scheme"}
    )
    def jira_server_delete_priority_scheme(
        scheme_id: int = Field(..., description="Id of priority scheme to delete"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a priority scheme"""
        api = get_api()
        response = api.jira_server_delete_priority_scheme(
            scheme_id=scheme_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_projects", tags={"jira-server-project"})
    def jira_server_get_all_projects(
        include_archived: bool | None = Field(
            None,
            description="Whether to include archived projects in response, default: false",
        ),
        expand: str | None = Field(None, description="Parameters to expand"),
        recent: int | None = Field(
            None,
            description="If this parameter is set then only projects recently accessed by the current user (if not logged in then based on HTTP session) will be returned (maximum count limited to the specified number but no more than 20)",
        ),
        browse_archive: bool | None = Field(
            None,
            description="Whether to include only projects where current user can browse archive",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all visible projects"""
        api = get_api()
        response = api.jira_server_get_all_projects(
            include_archived=include_archived,
            expand=expand,
            recent=recent,
            browse_archive=browse_archive,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_project", tags={"jira-server-project"})
    def jira_server_create_project(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new project"""
        api = get_api()
        response = api.jira_server_create_project(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_project_types", tags={"jira-server-project"})
    def jira_server_get_all_project_types(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all project types"""
        api = get_api()
        response = api.jira_server_get_all_project_types()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_project_type_by_key", tags={"jira-server-project"})
    def jira_server_get_project_type_by_key(
        project_type_key: str = Field(..., description="The key of the project type"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get project type by key"""
        api = get_api()
        response = api.jira_server_get_project_type_by_key(
            project_type_key=project_type_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_accessible_project_type_by_key",
        tags={"jira-server-project"},
    )
    def jira_server_get_accessible_project_type_by_key(
        project_type_key: str = Field(..., description="The key of the project type"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get project type by key"""
        api = get_api()
        response = api.jira_server_get_accessible_project_type_by_key(
            project_type_key=project_type_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_project", tags={"jira-server-project"})
    def jira_server_get_project(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        expand: str | None = Field(None, description="Parameters to expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a project by ID or key"""
        api = get_api()
        response = api.jira_server_get_project(
            expand=expand,
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_project", tags={"jira-server-project"})
    def jira_server_update_project(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        expand: str | None = Field(None, description="Parameters to expand"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a project"""
        api = get_api()
        response = api.jira_server_update_project(
            expand=expand,
            project_id_or_key=project_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_project", tags={"jira-server-project"})
    def jira_server_delete_project(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a project"""
        api = get_api()
        response = api.jira_server_delete_project(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_archive_project", tags={"jira-server-project"})
    def jira_server_archive_project(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Archive a project"""
        api = get_api()
        response = api.jira_server_archive_project(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_project_avatar", tags={"jira-server-project-avatar"}
    )
    def jira_server_update_project_avatar(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update project avatar"""
        api = get_api()
        response = api.jira_server_update_project_avatar(
            project_id_or_key=project_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_avatar_from_temporary_1", tags={"jira-server-other"}
    )
    def jira_server_create_avatar_from_temporary_1(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create avatar from temporary"""
        api = get_api()
        response = api.jira_server_create_avatar_from_temporary_1(
            project_id_or_key=project_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_store_temporary_avatar_using_multi_part_1",
        tags={"jira-server-other"},
    )
    def jira_server_store_temporary_avatar_using_multi_part_1(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Store temporary avatar using multipart"""
        api = get_api()
        response = api.jira_server_store_temporary_avatar_using_multi_part_1(
            project_id_or_key=project_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_avatar", tags={"jira-server-other"})
    def jira_server_delete_avatar(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        id_: int = Field(..., description="Database id for avatar"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete an avatar"""
        api = get_api()
        response = api.jira_server_delete_avatar(
            project_id_or_key=project_id_or_key,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_avatars", tags={"jira-server-other"})
    def jira_server_get_all_avatars(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all avatars for a project"""
        api = get_api()
        response = api.jira_server_get_all_avatars(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_project_components",
        tags={"jira-server-project-component"},
    )
    def jira_server_get_project_components(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get project components"""
        api = get_api()
        response = api.jira_server_get_project_components(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_properties_keys_3", tags={"jira-server-other"})
    def jira_server_get_properties_keys_3(
        project_id_or_key: str = Field(
            ..., description="The project from which keys will be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get keys of all properties for project"""
        api = get_api()
        response = api.jira_server_get_properties_keys_3(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_property_5", tags={"jira-server-other"})
    def jira_server_get_property_5(
        property_key: str = Field(
            ..., description="The key of the property to return."
        ),
        project_id_or_key: str = Field(
            ..., description="The project from which the property will be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get value of property from project"""
        api = get_api()
        response = api.jira_server_get_property_5(
            property_key=property_key,
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_property_4", tags={"jira-server-other"})
    def jira_server_set_property_4(
        property_key: str = Field(
            ...,
            description="The key of the project's property. The maximum length of the key is 255 bytes.",
        ),
        project_id_or_key: str = Field(
            ..., description="The project on which the property will be set."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set value of specified project's property"""
        api = get_api()
        response = api.jira_server_set_property_4(
            property_key=property_key,
            project_id_or_key=project_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_property_5", tags={"jira-server-other"})
    def jira_server_delete_property_5(
        property_key: str = Field(
            ..., description="The key of the property to remove."
        ),
        project_id_or_key: str = Field(
            ..., description="The project from which the property will be removed."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete property from project"""
        api = get_api()
        response = api.jira_server_delete_property_5(
            property_key=property_key,
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_restore_project", tags={"jira-server-project"})
    def jira_server_restore_project(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Restore an archived project"""
        api = get_api()
        response = api.jira_server_restore_project(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_project_roles", tags={"jira-server-project-role"})
    def jira_server_get_project_roles(
        project_id_or_key: str = Field(
            ..., description="The project id or project key"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all roles in project"""
        api = get_api()
        response = api.jira_server_get_project_roles(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_project_role", tags={"jira-server-project-role"})
    def jira_server_get_project_role(
        project_id_or_key: str = Field(
            ..., description="The project id or project key"
        ),
        id_: int = Field(..., description="The project role id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get details for a project role"""
        api = get_api()
        response = api.jira_server_get_project_role(
            project_id_or_key=project_id_or_key,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_actors", tags={"jira-server-other"})
    def jira_server_set_actors(
        project_id_or_key: str = Field(
            ..., description="The project id or project key"
        ),
        id_: int = Field(..., description="The project role id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update project role with actors"""
        api = get_api()
        response = api.jira_server_set_actors(
            project_id_or_key=project_id_or_key,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_actor_users", tags={"jira-server-user"})
    def jira_server_add_actor_users(
        project_id_or_key: str = Field(
            ..., description="The project id or project key"
        ),
        id_: int = Field(..., description="The project role id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add actor to project role"""
        api = get_api()
        response = api.jira_server_add_actor_users(
            project_id_or_key=project_id_or_key,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_actor", tags={"jira-server-other"})
    def jira_server_delete_actor(
        project_id_or_key: str = Field(
            ..., description="The project id or project key"
        ),
        id_: int = Field(..., description="The project role id"),
        user: str | None = Field(
            None,
            description="The user name of the user to remove from the project role. Use either user or group, but not both",
        ),
        group: str | None = Field(
            None,
            description="The group name to remove from the project role. Use either user or group, but not both",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete actors from project role"""
        api = get_api()
        response = api.jira_server_delete_actor(
            project_id_or_key=project_id_or_key,
            id_=id_,
            user=user,
            group=group,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_statuses", tags={"jira-server-other"})
    def jira_server_get_all_statuses(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issue types with statuses for a project"""
        api = get_api()
        response = api.jira_server_get_all_statuses(
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_project_type", tags={"jira-server-project"})
    def jira_server_update_project_type(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        new_project_type_key: str = Field(
            ..., description="The key of the new project type"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update project type"""
        api = get_api()
        response = api.jira_server_update_project_type(
            project_id_or_key=project_id_or_key,
            new_project_type_key=new_project_type_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_project_versions_paginated", tags={"jira-server-project"}
    )
    def jira_server_get_project_versions_paginated(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        expand: str | None = Field(None, description="Parameters to expand"),
        max_results: int | None = Field(
            None,
            description="How many results on the page should be included. Defaults to 50",
        ),
        order_by: str | None = Field(None, description="Ordering of the results"),
        start_at: int | None = Field(
            None, description="The page offset, if not specified then defaults to 0"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get paginated project versions"""
        api = get_api()
        response = api.jira_server_get_project_versions_paginated(
            expand=expand,
            project_id_or_key=project_id_or_key,
            max_results=max_results,
            order_by=order_by,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_project_versions", tags={"jira-server-project"})
    def jira_server_get_project_versions(
        project_id_or_key: str = Field(..., description="Project id or project key"),
        expand: str | None = Field(None, description="Parameters to expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get project versions"""
        api = get_api()
        response = api.jira_server_get_project_versions(
            expand=expand,
            project_id_or_key=project_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issue_security_scheme_1", tags={"jira-server-other"}
    )
    def jira_server_get_issue_security_scheme_1(
        project_key_or_id: str = Field(
            ..., description="The project id or project key"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue security scheme for project"""
        api = get_api()
        response = api.jira_server_get_issue_security_scheme_1(
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_notification_scheme_1", tags={"jira-server-other"})
    def jira_server_get_notification_scheme_1(
        project_key_or_id: str = Field(..., description="Key or id of the project"),
        expand: str | None = Field(
            None,
            description="Optional information to be expanded in the response: group, user, projectRole or field.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get notification scheme associated with the project"""
        api = get_api()
        response = api.jira_server_get_notification_scheme_1(
            expand=expand,
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_assigned_permission_scheme",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_get_assigned_permission_scheme(
        project_key_or_id: str = Field(..., description="Key or id of the project"),
        expand: str | None = Field(
            None,
            description="Use expand to include additional information about permission schemes in the response. This parameter accepts a comma-separated list of expandable options. Expand options include: all and field.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get assigned permission scheme"""
        api = get_api()
        response = api.jira_server_get_assigned_permission_scheme(
            expand=expand,
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_assign_permission_scheme",
        tags={"jira-server-permission-scheme"},
    )
    def jira_server_assign_permission_scheme(
        project_key_or_id: str = Field(..., description="Key or id of the project"),
        expand: str | None = Field(
            None,
            description="Use expand to include additional information about permission schemes in the response. This parameter accepts a comma-separated list of expandable options. Expand options include: all and field.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign permission scheme to project"""
        api = get_api()
        response = api.jira_server_assign_permission_scheme(
            expand=expand,
            project_key_or_id=project_key_or_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_assigned_priority_scheme",
        tags={"jira-server-priority-scheme"},
    )
    def jira_server_get_assigned_priority_scheme(
        project_key_or_id: str = Field(..., description="Key or id of the project"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get assigned priority scheme"""
        api = get_api()
        response = api.jira_server_get_assigned_priority_scheme(
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_assign_priority_scheme", tags={"jira-server-priority-scheme"}
    )
    def jira_server_assign_priority_scheme(
        project_key_or_id: str = Field(..., description="Key or id of the project"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign project with priority scheme"""
        api = get_api()
        response = api.jira_server_assign_priority_scheme(
            project_key_or_id=project_key_or_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_unassign_priority_scheme",
        tags={"jira-server-priority-scheme"},
    )
    def jira_server_unassign_priority_scheme(
        scheme_id: int = Field(
            ..., description="Object that contains an id of the scheme"
        ),
        project_key_or_id: str = Field(..., description="Key or id of the project"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Unassign project from priority scheme"""
        api = get_api()
        response = api.jira_server_unassign_priority_scheme(
            scheme_id=scheme_id,
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_security_levels_for_project", tags={"jira-server-project"}
    )
    def jira_server_get_security_levels_for_project(
        project_key_or_id: str = Field(
            ..., description="Key or id of project to list the security levels for"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all security levels for project"""
        api = get_api()
        response = api.jira_server_get_security_levels_for_project(
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_workflow_scheme_for_project", tags={"jira-server-project"}
    )
    def jira_server_get_workflow_scheme_for_project(
        project_key_or_id: str = Field(..., description="The key or id of the project"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow scheme for project"""
        api = get_api()
        response = api.jira_server_get_workflow_scheme_for_project(
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_all_project_categories", tags={"jira-server-project"}
    )
    def jira_server_get_all_project_categories(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all project categories"""
        api = get_api()
        response = api.jira_server_get_all_project_categories()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_project_category",
        tags={"jira-server-project-category"},
    )
    def jira_server_create_project_category(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create project category"""
        api = get_api()
        response = api.jira_server_create_project_category(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_project_category_by_id",
        tags={"jira-server-project-category"},
    )
    def jira_server_get_project_category_by_id(
        id_: int = Field(..., description="A project category id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get project category by ID"""
        api = get_api()
        response = api.jira_server_get_project_category_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_project_category",
        tags={"jira-server-project-category"},
    )
    def jira_server_update_project_category(
        id_: int = Field(..., description="Id of the project category to modify."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update project category"""
        api = get_api()
        response = api.jira_server_update_project_category(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_remove_project_category",
        tags={"jira-server-project-category"},
    )
    def jira_server_remove_project_category(
        id_: int = Field(..., description="Id of the project category to delete."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete project category"""
        api = get_api()
        response = api.jira_server_remove_project_category(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_search_for_projects", tags={"jira-server-project"})
    def jira_server_search_for_projects(
        max_results: int | None = Field(
            None,
            description="Maximum number of matches to return. Zero means a default limit of 100 and negative numbers return no results.",
        ),
        query: str | None = Field(
            None,
            description="A sequence of characters expected to be found in the word-prefix of project name and/or key.",
        ),
        allow_empty_query: bool | None = Field(
            None,
            description="If true, and the query is empty, the method will return first results limited to the value of 'maxResults' or default limit of 100.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get projects matching query"""
        api = get_api()
        response = api.jira_server_search_for_projects(
            max_results=max_results,
            query=query,
            allow_empty_query=allow_empty_query,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_project_1", tags={"jira-server-project"})
    def jira_server_get_project_1(
        key: str | None = Field(None, description="The project key"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get project key validation"""
        api = get_api()
        response = api.jira_server_get_project_1(
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_reindex_info", tags={"jira-server-admin-index"})
    def jira_server_get_reindex_info(
        task_id: int | None = Field(
            None,
            description="The id of an indexing task you wish to obtain details on. If omitted, then defaults to the standard behaviour and returns information on the active reindex task, or the last task to run if no reindex is taking place.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get reindex information"""
        api = get_api()
        response = api.jira_server_get_reindex_info(
            task_id=task_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_reindex", tags={"jira-server-admin-index"})
    def jira_server_reindex(
        index_change_history: bool | None = Field(
            None,
            description="Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.",
        ),
        type_: str | None = Field(
            None,
            description="Case insensitive String indicating type of reindex. If omitted, then defaults to BACKGROUND_PREFERRED. Not relevant for Search Platform that only supports BACKGROUND reindexing e.g. OpenSearch.",
        ),
        index_worklogs: bool | None = Field(
            None,
            description="Indicates that worklogs should also be reindexed. Not relevant for foreground reindex, where worklogs are always reindexed.",
        ),
        index_comments: bool | None = Field(
            None,
            description="Indicates that comments should also be reindexed. Not relevant for foreground reindex, where comments are always reindexed.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Start a reindex operation"""
        api = get_api()
        response = api.jira_server_reindex(
            index_change_history=index_change_history,
            type_=type_,
            index_worklogs=index_worklogs,
            index_comments=index_comments,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_reindex_issues", tags={"jira-server-admin-index"})
    def jira_server_reindex_issues(
        issue_id: list[Any] | None = Field(
            None, description="The IDs or keys of one or more issues to reindex."
        ),
        index_change_history: bool | None = Field(
            None, description="Indicates that changeHistory should also be reindexed."
        ),
        index_worklogs: bool | None = Field(
            None, description="Indicates that worklogs should also be reindexed."
        ),
        index_comments: bool | None = Field(
            None, description="Indicates that comments should also be reindexed."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reindex individual issues"""
        api = get_api()
        response = api.jira_server_reindex_issues(
            issue_id=issue_id,
            index_change_history=index_change_history,
            index_worklogs=index_worklogs,
            index_comments=index_comments,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_reindex_progress", tags={"jira-server-admin-index"})
    def jira_server_get_reindex_progress(
        task_id: int | None = Field(
            None,
            description="The id of an indexing task you wish to obtain details on. If omitted, then defaults to the standard behaviour and returns information on the active reindex task, or the last task to run if no reindex is taking place.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get reindex progress"""
        api = get_api()
        response = api.jira_server_get_reindex_progress(
            task_id=task_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_process_requests", tags={"jira-server-other"})
    def jira_server_process_requests(_ctx: Context | None = None) -> dict[str, Any]:
        """Execute pending reindex requests"""
        api = get_api()
        response = api.jira_server_process_requests()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_progress_bulk", tags={"jira-server-other"})
    def jira_server_get_progress_bulk(
        request_id: list[Any] | None = Field(
            None, description="The reindex request IDs."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get progress of multiple reindex requests"""
        api = get_api()
        response = api.jira_server_get_progress_bulk(
            request_id=request_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_progress", tags={"jira-server-other"})
    def jira_server_get_progress(
        request_id: int = Field(..., description="The reindex request ID."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get progress of a single reindex request"""
        api = get_api()
        response = api.jira_server_get_progress(
            request_id=request_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_resolutions", tags={"jira-server-resolution"})
    def jira_server_get_resolutions(_ctx: Context | None = None) -> dict[str, Any]:
        """Get all resolutions"""
        api = get_api()
        response = api.jira_server_get_resolutions()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_paginated_resolutions", tags={"jira-server-resolution"}
    )
    def jira_server_get_paginated_resolutions(
        max_results: int | None = Field(
            None, description="The maximum number of statuses to return."
        ),
        query: str | None = Field(
            None, description="The string that status names will be matched with."
        ),
        start_at: int | None = Field(
            None, description="The index of the first status to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get paginated filtered resolutions"""
        api = get_api()
        response = api.jira_server_get_paginated_resolutions(
            max_results=max_results,
            query=query,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_resolution", tags={"jira-server-resolution"})
    def jira_server_get_resolution(
        id_: str = Field(..., description="A String containing the resolution id."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a resolution by ID"""
        api = get_api()
        response = api.jira_server_get_resolution(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_project_roles_1", tags={"jira-server-project-role"})
    def jira_server_get_project_roles_1(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all project roles"""
        api = get_api()
        response = api.jira_server_get_project_roles_1()
        return response.model_dump()

    @mcp.tool(name="jira_server_create_project_role", tags={"jira-server-project-role"})
    def jira_server_create_project_role(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new project role"""
        api = get_api()
        response = api.jira_server_create_project_role(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_project_roles_by_id", tags={"jira-server-project-role"}
    )
    def jira_server_get_project_roles_by_id(
        id_: int = Field(..., description="The role id"), _ctx: Context | None = None
    ) -> dict[str, Any]:
        """Get a specific project role"""
        api = get_api()
        response = api.jira_server_get_project_roles_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_fully_update_project_role", tags={"jira-server-project-role"}
    )
    def jira_server_fully_update_project_role(
        id_: int = Field(..., description="The role id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Fully updates a role's name and description"""
        api = get_api()
        response = api.jira_server_fully_update_project_role(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_partial_update_project_role",
        tags={"jira-server-project-role"},
    )
    def jira_server_partial_update_project_role(
        id_: int = Field(..., description="The role id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Partially updates a role's name or description"""
        api = get_api()
        response = api.jira_server_partial_update_project_role(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_project_role", tags={"jira-server-project-role"})
    def jira_server_delete_project_role(
        id_: int = Field(..., description="The role id"),
        swap: int | None = Field(
            None,
            description="If given, removes a role even if it is used in scheme by replacing the role with the given one",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Deletes a role"""
        api = get_api()
        response = api.jira_server_delete_project_role(
            swap=swap,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_project_role_actors_for_role",
        tags={"jira-server-project-role"},
    )
    def jira_server_get_project_role_actors_for_role(
        id_: int = Field(..., description="The role id"), _ctx: Context | None = None
    ) -> dict[str, Any]:
        """Get default actors for a role"""
        api = get_api()
        response = api.jira_server_get_project_role_actors_for_role(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_add_project_role_actors_to_role",
        tags={"jira-server-project-role"},
    )
    def jira_server_add_project_role_actors_to_role(
        id_: int = Field(..., description="The role id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Adds default actors to a role"""
        api = get_api()
        response = api.jira_server_add_project_role_actors_to_role(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_project_role_actors_from_role",
        tags={"jira-server-project-role"},
    )
    def jira_server_delete_project_role_actors_from_role(
        id_: int = Field(..., description="The role id to remove the actors from"),
        user: str | None = Field(
            None, description="If given, removes an actor from given role"
        ),
        group: str | None = Field(
            None, description="If given, removes an actor from given role"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Removes default actor from a role"""
        api = get_api()
        response = api.jira_server_delete_project_role_actors_from_role(
            id_=id_,
            user=user,
            group=group,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_screens", tags={"jira-server-screen"})
    def jira_server_get_all_screens(
        search: str | None = Field(None, description="Parameter search"),
        expand: str | None = Field(None, description="Parameter expand"),
        max_results: str | None = Field(None, description="Parameter maxResults"),
        start_at: str | None = Field(None, description="Parameter startAt"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available field screens"""
        api = get_api()
        response = api.jira_server_get_all_screens(
            search=search,
            expand=expand,
            max_results=max_results,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_add_field_to_default_screen", tags={"jira-server-screen"}
    )
    def jira_server_add_field_to_default_screen(
        field_id: str = Field(..., description="Parameter fieldId"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add field to default screen"""
        api = get_api()
        response = api.jira_server_add_field_to_default_screen(
            field_id=field_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_fields_to_add", tags={"jira-server-field"})
    def jira_server_get_fields_to_add(
        screen_id: int = Field(..., description="id of screen"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available fields for screen"""
        api = get_api()
        response = api.jira_server_get_fields_to_add(
            screen_id=screen_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_tabs", tags={"jira-server-screen"})
    def jira_server_get_all_tabs(
        screen_id: int = Field(..., description="id of screen"),
        project_key: str | None = Field(
            None, description="the key of the project; this parameter is optional"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all tabs for a screen"""
        api = get_api()
        response = api.jira_server_get_all_tabs(
            screen_id=screen_id,
            project_key=project_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_tab", tags={"jira-server-screen"})
    def jira_server_add_tab(
        screen_id: int = Field(..., description="id of screen"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create tab for a screen"""
        api = get_api()
        response = api.jira_server_add_tab(
            screen_id=screen_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_rename_tab", tags={"jira-server-screen"})
    def jira_server_rename_tab(
        tab_id: int = Field(..., description="id of tab"),
        screen_id: int = Field(..., description="id of screen"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Rename a tab on a screen"""
        api = get_api()
        response = api.jira_server_rename_tab(
            tab_id=tab_id,
            screen_id=screen_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_tab", tags={"jira-server-screen"})
    def jira_server_delete_tab(
        tab_id: int = Field(..., description="id of tab"),
        screen_id: int = Field(..., description="id of screen"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a tab from a screen"""
        api = get_api()
        response = api.jira_server_delete_tab(
            tab_id=tab_id,
            screen_id=screen_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_fields", tags={"jira-server-field"})
    def jira_server_get_all_fields(
        tab_id: int = Field(..., description="id of tab"),
        screen_id: int = Field(..., description="id of screen"),
        project_key: str | None = Field(
            None, description="the key of the project; this parameter is optional"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all fields for a tab"""
        api = get_api()
        response = api.jira_server_get_all_fields(
            tab_id=tab_id,
            screen_id=screen_id,
            project_key=project_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_add_field", tags={"jira-server-field"})
    def jira_server_add_field(
        tab_id: int = Field(..., description="id of tab"),
        screen_id: int = Field(..., description="id of screen"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add field to a tab"""
        api = get_api()
        response = api.jira_server_add_field(
            tab_id=tab_id,
            screen_id=screen_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_remove_field", tags={"jira-server-field"})
    def jira_server_remove_field(
        tab_id: int = Field(..., description="id of tab"),
        screen_id: int = Field(..., description="id of screen"),
        id_: str = Field(..., description="id of field"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove field from tab"""
        api = get_api()
        response = api.jira_server_remove_field(
            tab_id=tab_id,
            screen_id=screen_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_move_field", tags={"jira-server-field"})
    def jira_server_move_field(
        tab_id: int = Field(..., description="id of tab"),
        screen_id: int = Field(..., description="id of screen"),
        id_: str = Field(..., description="id of field"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move field on a tab"""
        api = get_api()
        response = api.jira_server_move_field(
            tab_id=tab_id,
            screen_id=screen_id,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_show_when_empty_indicator", tags={"jira-server-other"}
    )
    def jira_server_update_show_when_empty_indicator(
        tab_id: int = Field(..., description="id of tab"),
        screen_id: int = Field(..., description="id of screen"),
        new_value: bool = Field(
            ..., description="new value of 'showWhenEmptyIndicator'"
        ),
        id_: str = Field(..., description="id of field"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update 'showWhenEmptyIndicator' for a field"""
        api = get_api()
        response = api.jira_server_update_show_when_empty_indicator(
            tab_id=tab_id,
            screen_id=screen_id,
            new_value=new_value,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_move_tab", tags={"jira-server-screen"})
    def jira_server_move_tab(
        tab_id: int = Field(..., description="id of tab"),
        screen_id: int = Field(..., description="id of screen"),
        pos: int = Field(..., description="position of tab"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move tab position"""
        api = get_api()
        response = api.jira_server_move_tab(
            tab_id=tab_id,
            screen_id=screen_id,
            pos=pos,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_search_1", tags={"jira-server-search"})
    def jira_server_search_1(
        expand: str | None = Field(
            None, description="A comma-separated list of the parameters to expand"
        ),
        jql: str | None = Field(None, description="a JQL query string"),
        max_results: int | None = Field(
            None, description="the maximum number of issues to return (defaults to 50)"
        ),
        validate_query: bool | None = Field(
            None, description="whether to validate the JQL query"
        ),
        fields: list[Any] | None = Field(
            None, description="the list of fields to return for each issue"
        ),
        start_at: int | None = Field(
            None, description="the index of the first issue to return (0-based)"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issues using JQL"""
        api = get_api()
        response = api.jira_server_search_1(
            expand=expand,
            jql=jql,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_search_using_search_request", tags={"jira-server-search"}
    )
    def jira_server_search_using_search_request(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Perform search with JQL"""
        api = get_api()
        response = api.jira_server_search_using_search_request(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_error", tags={"jira-server-other"})
    def jira_server_get_error(_ctx: Context | None = None) -> dict[str, Any]:
        """No description provided."""
        api = get_api()
        response = api.jira_server_get_error()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_max_aggregation_buckets", tags={"jira-server-other"}
    )
    def jira_server_get_max_aggregation_buckets(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get maximum aggregation buckets"""
        api = get_api()
        response = api.jira_server_get_max_aggregation_buckets()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_max_result_window", tags={"jira-server-other"})
    def jira_server_get_max_result_window(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get maximum result window"""
        api = get_api()
        response = api.jira_server_get_max_result_window()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issuesecuritylevel", tags={"jira-server-other"})
    def jira_server_get_issuesecuritylevel(
        id_: str = Field(..., description="An issue security level id"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get a security level by ID"""
        api = get_api()
        response = api.jira_server_get_issuesecuritylevel(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_server_info", tags={"jira-server-system"})
    def jira_server_get_server_info(_ctx: Context | None = None) -> dict[str, Any]:
        """Get general information about the current Jira server"""
        api = get_api()
        response = api.jira_server_get_server_info()
        return response.model_dump()

    @mcp.tool(name="jira_server_set_base_url", tags={"jira-server-other"})
    def jira_server_set_base_url(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update base URL for Jira instance"""
        api = get_api()
        response = api.jira_server_set_base_url(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_issue_navigator_default_columns",
        tags={"jira-server-other"},
    )
    def jira_server_get_issue_navigator_default_columns(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get default system columns for issue navigator"""
        api = get_api()
        response = api.jira_server_get_issue_navigator_default_columns()
        return response.model_dump()

    @mcp.tool(
        name="jira_server_set_issue_navigator_default_columns_form",
        tags={"jira-server-other"},
    )
    def jira_server_set_issue_navigator_default_columns_form(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set default system columns for issue navigator using form"""
        api = get_api()
        response = api.jira_server_set_issue_navigator_default_columns_form(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_statuses", tags={"jira-server-other"})
    def jira_server_get_statuses(_ctx: Context | None = None) -> dict[str, Any]:
        """Get all statuses"""
        api = get_api()
        response = api.jira_server_get_statuses()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_paginated_statuses", tags={"jira-server-other"})
    def jira_server_get_paginated_statuses(
        issue_type_ids: list[Any] | None = Field(
            None, description="The list of issue type ids to filter statuses."
        ),
        max_results: int | None = Field(
            None, description="The maximum number of statuses to return."
        ),
        query: str | None = Field(
            None, description="The string that status names will be matched with."
        ),
        project_ids: list[Any] | None = Field(
            None, description="The list of project ids to filter statuses."
        ),
        start_at: int | None = Field(
            None, description="The index of the first status to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get paginated filtered statuses"""
        api = get_api()
        response = api.jira_server_get_paginated_statuses(
            issue_type_ids=issue_type_ids,
            max_results=max_results,
            query=query,
            project_ids=project_ids,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_status", tags={"jira-server-other"})
    def jira_server_get_status(
        id_or_name: str = Field(
            ..., description="A numeric Status id or a status name"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get status by ID or name"""
        api = get_api()
        response = api.jira_server_get_status(
            id_or_name=id_or_name,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_status_categories", tags={"jira-server-other"})
    def jira_server_get_status_categories(
        request: str | None = Field(None, description="a Request"),
        uri_info: str | None = Field(None, description="a UriInfo"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all status categories"""
        api = get_api()
        response = api.jira_server_get_status_categories(
            request=request,
            uri_info=uri_info,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_status_category", tags={"jira-server-other"})
    def jira_server_get_status_category(
        id_or_key: str = Field(
            ..., description="A numeric StatusCategory id or a status category key"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get status category by ID or key"""
        api = get_api()
        response = api.jira_server_get_status_category(
            id_or_key=id_or_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_all_terminology_entries", tags={"jira-server-other"}
    )
    def jira_server_get_all_terminology_entries(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all defined names for 'epic' and 'sprint'"""
        api = get_api()
        response = api.jira_server_get_all_terminology_entries()
        return response.model_dump()

    @mcp.tool(name="jira_server_set_terminology_entries", tags={"jira-server-other"})
    def jira_server_set_terminology_entries(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update epic/sprint names from original to new"""
        api = get_api()
        response = api.jira_server_set_terminology_entries(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_terminology_entry", tags={"jira-server-other"})
    def jira_server_get_terminology_entry(
        original_name: str = Field(
            ..., description="A numeric StatusCategory id or a status category key"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get epic or sprint name by original name"""
        api = get_api()
        response = api.jira_server_get_terminology_entry(
            original_name=original_name,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_avatars", tags={"jira-server-other"})
    def jira_server_get_avatars(
        type_: str = Field(..., description="Parameter type"),
        owning_object_id: str = Field(..., description="Parameter owningObjectId"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all avatars for a type and owner"""
        api = get_api()
        response = api.jira_server_get_avatars(
            type_=type_,
            owning_object_id=owning_object_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_avatar_from_temporary_2", tags={"jira-server-other"}
    )
    def jira_server_create_avatar_from_temporary_2(
        type_: str = Field(..., description="Parameter type"),
        owning_object_id: str = Field(
            ..., description="Entity id where to change avatar"
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create avatar from temporary"""
        api = get_api()
        response = api.jira_server_create_avatar_from_temporary_2(
            type_=type_,
            owning_object_id=owning_object_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_avatar_1", tags={"jira-server-other"})
    def jira_server_delete_avatar_1(
        id_: int = Field(..., description="database id for avatar"),
        type_: str = Field(..., description="Parameter type"),
        owning_object_id: str = Field(
            ..., description="Entity id where to change avatar"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete avatar by ID"""
        api = get_api()
        response = api.jira_server_delete_avatar_1(
            id_=id_,
            type_=type_,
            owning_object_id=owning_object_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_store_temporary_avatar_using_multi_part_2",
        tags={"jira-server-other"},
    )
    def jira_server_store_temporary_avatar_using_multi_part_2(
        type_: str = Field(..., description="Parameter type"),
        owning_object_id: str = Field(
            ..., description="Entity id where to change avatar"
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create temporary avatar using multipart upload"""
        api = get_api()
        response = api.jira_server_store_temporary_avatar_using_multi_part_2(
            type_=type_,
            owning_object_id=owning_object_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_upgrade_result", tags={"jira-server-admin-upgrade"})
    def jira_server_get_upgrade_result(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get result of the last upgrade task"""
        api = get_api()
        response = api.jira_server_get_upgrade_result()
        return response.model_dump()

    @mcp.tool(name="jira_server_run_upgrades_now", tags={"jira-server-admin-upgrade"})
    def jira_server_run_upgrades_now(_ctx: Context | None = None) -> dict[str, Any]:
        """Run pending upgrade tasks"""
        api = get_api()
        response = api.jira_server_run_upgrades_now()
        return response.model_dump()

    @mcp.tool(name="jira_server_get_user_1", tags={"jira-server-user"})
    def jira_server_get_user_1(
        include_deleted: bool | None = Field(
            None,
            description="whether deleted users should be returned (flag available to users with global ADMIN rights)",
        ),
        key: str | None = Field(None, description="user key"),
        username: str | None = Field(None, description="the username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user by username or key"""
        api = get_api()
        response = api.jira_server_get_user_1(
            include_deleted=include_deleted,
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_user_1", tags={"jira-server-user"})
    def jira_server_update_user_1(
        key: str | None = Field(None, description="user key"),
        username: str | None = Field(None, description="the username"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update user details"""
        api = get_api()
        response = api.jira_server_update_user_1(
            key=key,
            username=username,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_user", tags={"jira-server-user"})
    def jira_server_create_user(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create new user"""
        api = get_api()
        response = api.jira_server_create_user(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_remove_user", tags={"jira-server-user"})
    def jira_server_remove_user(
        key: str | None = Field(None, description="user key"),
        username: str | None = Field(None, description="the username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete user"""
        api = get_api()
        response = api.jira_server_remove_user(
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_a11y_personal_settings", tags={"jira-server-other"})
    def jira_server_get_a11y_personal_settings(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available accessibility personal settings"""
        api = get_api()
        response = api.jira_server_get_a11y_personal_settings()
        return response.model_dump()

    @mcp.tool(name="jira_server_validate_user_anonymization", tags={"jira-server-user"})
    def jira_server_validate_user_anonymization(
        expand: str | None = Field(
            None, description="Parameter used to include parts of the response."
        ),
        user_key: str | None = Field(
            None, description="The key of the user to validate anonymization for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get validation for user anonymization"""
        api = get_api()
        response = api.jira_server_validate_user_anonymization(
            expand=expand,
            user_key=user_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_schedule_user_anonymization", tags={"jira-server-user"})
    def jira_server_schedule_user_anonymization(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Schedule user anonymization"""
        api = get_api()
        response = api.jira_server_schedule_user_anonymization(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_progress_1", tags={"jira-server-other"})
    def jira_server_get_progress_1(
        task_id: int | None = Field(
            None,
            description="The id of a user anonymization task you wish to obtain details on.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user anonymization progress"""
        api = get_api()
        response = api.jira_server_get_progress_1(
            task_id=task_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_validate_user_anonymization_rerun", tags={"jira-server-user"}
    )
    def jira_server_validate_user_anonymization_rerun(
        expand: str | None = Field(
            None, description="Parameter used to include parts of the response."
        ),
        old_user_key: str | None = Field(
            None,
            description="User key before anonymization, only needed when current value is anonymized. If there is no old key, e.g. because the user was already created using the new key generation strategy, provide a value equal to the current key.",
        ),
        old_user_name: str | None = Field(
            None,
            description="User name before anonymization, only needed when the current value is anonymized. If there is no old name, provide a value equal to the current name.",
        ),
        user_key: str | None = Field(
            None, description="The key of the user to validate anonymization for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get validation for user anonymization rerun"""
        api = get_api()
        response = api.jira_server_validate_user_anonymization_rerun(
            expand=expand,
            old_user_key=old_user_key,
            old_user_name=old_user_name,
            user_key=user_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_schedule_user_anonymization_rerun", tags={"jira-server-user"}
    )
    def jira_server_schedule_user_anonymization_rerun(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Schedule user anonymization rerun"""
        api = get_api()
        response = api.jira_server_schedule_user_anonymization_rerun(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_unlock_anonymization", tags={"jira-server-other"})
    def jira_server_unlock_anonymization(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete stale user anonymization task"""
        api = get_api()
        response = api.jira_server_unlock_anonymization()
        return response.model_dump()

    @mcp.tool(name="jira_server_add_user_to_application_1", tags={"jira-server-user"})
    def jira_server_add_user_to_application_1(
        application_key: str | None = Field(None, description="application key"),
        username: str | None = Field(None, description="username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add user to application"""
        api = get_api()
        response = api.jira_server_add_user_to_application_1(
            application_key=application_key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_remove_user_from_application_1", tags={"jira-server-user"}
    )
    def jira_server_remove_user_from_application_1(
        application_key: str | None = Field(None, description="application key"),
        username: str | None = Field(None, description="username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove user from application"""
        api = get_api()
        response = api.jira_server_remove_user_from_application_1(
            application_key=application_key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_find_bulk_assignable_users", tags={"jira-server-user"})
    def jira_server_find_bulk_assignable_users(
        max_results: int | None = Field(
            None,
            description="The maximum number of users to return (defaults to 50). The maximum allowed value is 100 (The combination of maxResults and startAt is limited to the first 100 results). If you specify a value that is higher than this number, your search results will be truncated. If you send a request with startAt=98 and maxResults=20, it will only return 2 users.",
        ),
        project_keys: str | None = Field(
            None,
            description="the keys of the projects we are finding assignable users for, comma-separated",
        ),
        username: str | None = Field(None, description="the username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find bulk assignable users"""
        api = get_api()
        response = api.jira_server_find_bulk_assignable_users(
            max_results=max_results,
            project_keys=project_keys,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_find_assignable_users_1", tags={"jira-server-user"})
    def jira_server_find_assignable_users_1(
        issue_key: str | None = Field(
            None,
            description="the issue key for the issue being edited we need to find assignable users for.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of users to return (defaults to 50). The maximum allowed value is 100 (The combination of maxResults and startAt is limited to the first 100 results). If you specify a value that is higher than this number, your search results will be truncated. If you send a request with startAt=98 and maxResults=20, it will only return 2 users.",
        ),
        project: str | None = Field(None, description="Parameter project"),
        action_descriptor_id: int | None = Field(
            None, description="Parameter actionDescriptorId"
        ),
        username: str | None = Field(None, description="the username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find assignable users by username"""
        api = get_api()
        response = api.jira_server_find_assignable_users_1(
            issue_key=issue_key,
            max_results=max_results,
            project=project,
            action_descriptor_id=action_descriptor_id,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_user_avatar_1", tags={"jira-server-user-avatar"})
    def jira_server_update_user_avatar_1(
        username: str | None = Field(None, description="username"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update user avatar"""
        api = get_api()
        response = api.jira_server_update_user_avatar_1(
            username=username,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_avatar_from_temporary_3", tags={"jira-server-other"}
    )
    def jira_server_create_avatar_from_temporary_3(
        username: str | None = Field(None, description="username"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create avatar from temporary"""
        api = get_api()
        response = api.jira_server_create_avatar_from_temporary_3(
            username=username,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_store_temporary_avatar_using_multi_part_3",
        tags={"jira-server-other"},
    )
    def jira_server_store_temporary_avatar_using_multi_part_3(
        username: str | None = Field(None, description="username"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Store temporary avatar using multipart"""
        api = get_api()
        response = api.jira_server_store_temporary_avatar_using_multi_part_3(
            username=username,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_avatar_2", tags={"jira-server-other"})
    def jira_server_delete_avatar_2(
        id_: int = Field(..., description="database id for avatar"),
        username: str | None = Field(None, description="username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete avatar"""
        api = get_api()
        response = api.jira_server_delete_avatar_2(
            id_=id_,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_avatars_1", tags={"jira-server-other"})
    def jira_server_get_all_avatars_1(
        username: str | None = Field(None, description="username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all avatars for user"""
        api = get_api()
        response = api.jira_server_get_all_avatars_1(
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_default_columns", tags={"jira-server-other"})
    def jira_server_default_columns(
        username: str | None = Field(None, description="username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get default columns for user"""
        api = get_api()
        response = api.jira_server_default_columns(
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_columns_url_encoded", tags={"jira-server-other"})
    def jira_server_set_columns_url_encoded(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set default columns for user"""
        api = get_api()
        response = api.jira_server_set_columns_url_encoded(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_reset_columns", tags={"jira-server-other"})
    def jira_server_reset_columns(
        username: str | None = Field(None, description="username"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset default columns to system default"""
        api = get_api()
        response = api.jira_server_reset_columns(
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_duplicated_users_count", tags={"jira-server-user"})
    def jira_server_get_duplicated_users_count(
        flush: bool | None = Field(
            None,
            description="if set to true forces cache flush, user must be sysadmin for this parameter to have an effect.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get duplicated users count"""
        api = get_api()
        response = api.jira_server_get_duplicated_users_count(
            flush=flush,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_duplicated_users_mapping", tags={"jira-server-user"}
    )
    def jira_server_get_duplicated_users_mapping(
        flush: bool | None = Field(
            None,
            description="if set to true forces cache flush, user must be sysadmin for this parameter to have an effect.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get duplicated users mapping"""
        api = get_api()
        response = api.jira_server_get_duplicated_users_mapping(
            flush=flush,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_user_list", tags={"jira-server-user"})
    def jira_server_get_user_list(
        cursor: int | None = Field(
            None,
            description="The position in the stream to continue iterating over all users.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of users to return per page (defaults to 2000).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """List all users"""
        api = get_api()
        response = api.jira_server_get_user_list(
            cursor=cursor,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_change_user_password", tags={"jira-server-user"})
    def jira_server_change_user_password(
        key: str | None = Field(None, description="user key"),
        username: str | None = Field(None, description="the username"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update user password"""
        api = get_api()
        response = api.jira_server_change_user_password(
            key=key,
            username=username,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_find_users_with_all_permissions", tags={"jira-server-user"}
    )
    def jira_server_find_users_with_all_permissions(
        project_key: str | None = Field(
            None,
            description="the optional project key to search for users with if no issueKey is supplied.",
        ),
        issue_key: str | None = Field(
            None,
            description="the issue key for the issue for which returned users have specified permissions.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of users to return (defaults to 50). The maximum allowed value is 100 (The combination of maxResults and startAt is limited to the first 100 results). If you specify a value that is higher than this number, your search results will be truncated. If you send a request with startAt=98 and maxResults=20, it will only return 2 users.",
        ),
        permissions: str | None = Field(
            None,
            description="comma separated list of permissions for project or issue returned users must have",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first user to return (0-based). Please note that the startAt parameter will be deprecated in a future release of Jira 10.3.x",
        ),
        username: str | None = Field(
            None,
            description="the username filter, list includes all users if unspecified",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users with all specified permissions"""
        api = get_api()
        response = api.jira_server_find_users_with_all_permissions(
            project_key=project_key,
            issue_key=issue_key,
            max_results=max_results,
            permissions=permissions,
            start_at=start_at,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_find_users_for_picker", tags={"jira-server-user"})
    def jira_server_find_users_for_picker(
        max_results: int | None = Field(
            None,
            description="The maximum number of users to return (defaults to 50). The maximum allowed value is 100 (The combination of maxResults and startAt is limited to the first 100 results). If you specify a value that is higher than this number, your search results will be truncated. If you send a request with startAt=98 and maxResults=20, it will only return 2 users.",
        ),
        query: str | None = Field(
            None, description="A string used to search username, Name or e-mail address"
        ),
        exclude: list[Any] | None = Field(
            None, description="List of users to be excluded from the search results"
        ),
        show_avatar: bool | None = Field(
            None, description="If true, then avatars are included in the results"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users for picker by query"""
        api = get_api()
        response = api.jira_server_find_users_for_picker(
            max_results=max_results,
            query=query,
            exclude=exclude,
            show_avatar=show_avatar,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_properties_keys_4", tags={"jira-server-other"})
    def jira_server_get_properties_keys_4(
        user_key: str | None = Field(
            None, description="Key of the user whose properties are to be returned"
        ),
        username: str | None = Field(
            None, description="Username of the user whose properties are to be returned"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get keys of all properties for a user"""
        api = get_api()
        response = api.jira_server_get_properties_keys_4(
            user_key=user_key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_property_6", tags={"jira-server-other"})
    def jira_server_get_property_6(
        property_key: str = Field(..., description="The key of the user's property"),
        user_key: str | None = Field(
            None, description="Key of the user whose property is to be returned"
        ),
        username: str | None = Field(
            None, description="Username of the user whose property is to be returned"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the value of a specified user's property"""
        api = get_api()
        response = api.jira_server_get_property_6(
            property_key=property_key,
            user_key=user_key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_property_5", tags={"jira-server-other"})
    def jira_server_set_property_5(
        property_key: str = Field(
            ...,
            description="The key of the user's property. The maximum length of the key is 255 bytes.",
        ),
        user_key: str | None = Field(
            None, description="Key of the user whose property is to be set"
        ),
        username: str | None = Field(
            None, description="Username of the user whose property is to be set"
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set the value of a specified user's property"""
        api = get_api()
        response = api.jira_server_set_property_5(
            property_key=property_key,
            user_key=user_key,
            username=username,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_property_6", tags={"jira-server-other"})
    def jira_server_delete_property_6(
        property_key: str = Field(..., description="The key of the user's property"),
        user_key: str | None = Field(
            None, description="Key of the user whose property is to be removed"
        ),
        username: str | None = Field(
            None, description="Username of the user whose property is to be removed"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a specified user's property"""
        api = get_api()
        response = api.jira_server_delete_property_6(
            property_key=property_key,
            user_key=user_key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_find_users", tags={"jira-server-user"})
    def jira_server_find_users(
        include_inactive: bool | None = Field(
            None,
            description="If true, then inactive users are included in the results (default false)",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of users to return (defaults to 50). The maximum allowed value is 100 (The combination of maxResults and startAt is limited to the first 100 results). If you specify a value that is higher than this number, your search results will be truncated. If you send a request with startAt=98 and maxResults=20, it will only return 2 users.",
        ),
        include_active: bool | None = Field(
            None,
            description="If true, then active users are included in the results (default true)",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first user to return (0-based). Please note that the startAt parameter will be deprecated in a future release of Jira 10.3.x",
        ),
        username: str | None = Field(
            None,
            description="A query string used to search username, name or e-mail address",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users by username"""
        api = get_api()
        response = api.jira_server_find_users(
            include_inactive=include_inactive,
            max_results=max_results,
            include_active=include_active,
            start_at=start_at,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_session", tags={"jira-server-other"})
    def jira_server_delete_session(
        username: str = Field(..., description="a String containing username."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete user session"""
        api = get_api()
        response = api.jira_server_delete_session(
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_find_users_with_browse_permission", tags={"jira-server-user"}
    )
    def jira_server_find_users_with_browse_permission(
        project_key: str | None = Field(
            None,
            description="the optional project key to search for users with if no issueKey is supplied.",
        ),
        issue_key: str | None = Field(
            None,
            description="the issue key for the issue being edited we need to find viewable users for.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of users to return (defaults to 50). The maximum allowed value is 100 (The combination of maxResults and startAt is limited to the first 100 results). If you specify a value that is higher than this number, your search results will be truncated. If you send a request with startAt=98 and maxResults=20, it will only return 2 users.",
        ),
        username: str | None = Field(
            None, description="the username filter, no users returned if left blank"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users with browse permission"""
        api = get_api()
        response = api.jira_server_find_users_with_browse_permission(
            project_key=project_key,
            issue_key=issue_key,
            max_results=max_results,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_paginated_versions", tags={"jira-server-other"})
    def jira_server_get_paginated_versions(
        max_results: int | None = Field(
            None, description="maximum number of versions to return"
        ),
        query: str | None = Field(
            None, description="string that version names will be matched with"
        ),
        project_ids: list[Any] | None = Field(
            None, description="set of project IDs to filter versions with"
        ),
        start_at: int | None = Field(
            None, description="index of the first version to return"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get paginated versions"""
        api = get_api()
        response = api.jira_server_get_paginated_versions(
            max_results=max_results,
            query=query,
            project_ids=project_ids,
            start_at=start_at,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_version", tags={"jira-server-other"})
    def jira_server_create_version(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create new version"""
        api = get_api()
        response = api.jira_server_create_version(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_remote_version_links", tags={"jira-server-other"})
    def jira_server_get_remote_version_links(
        global_id: str | None = Field(
            None, description="The id of the remote issue link to be returned."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get remote version links by global ID"""
        api = get_api()
        response = api.jira_server_get_remote_version_links(
            global_id=global_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_version", tags={"jira-server-other"})
    def jira_server_get_version(
        id_: str = Field(..., description="ID of the version."),
        expand: str | None = Field(None, description="Parameter expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version details"""
        api = get_api()
        response = api.jira_server_get_version(
            expand=expand,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_version", tags={"jira-server-other"})
    def jira_server_update_version(
        id_: str = Field(..., description="ID of the version."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update version details"""
        api = get_api()
        response = api.jira_server_update_version(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_merge", tags={"jira-server-other"})
    def jira_server_merge(
        move_issues_to: str = Field(
            ...,
            description="The version to set fixVersion to on issues where the deleted version is the fix version, If null then the fixVersion is removed.",
        ),
        id_: str = Field(
            ...,
            description="The version that will be merged to version moveIssuesTo and removed",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Merge versions"""
        api = get_api()
        response = api.jira_server_merge(
            move_issues_to=move_issues_to,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_move_version", tags={"jira-server-other"})
    def jira_server_move_version(
        id_: str = Field(..., description="ID of the version."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Modify version's sequence"""
        api = get_api()
        response = api.jira_server_move_version(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_version_related_issues", tags={"jira-server-other"})
    def jira_server_get_version_related_issues(
        id_: str = Field(..., description="ID of the version."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version related issues count"""
        api = get_api()
        response = api.jira_server_get_version_related_issues(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_1", tags={"jira-server-other"})
    def jira_server_delete_1(
        id_: str = Field(..., description="The version to delete"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete version and replace values"""
        api = get_api()
        response = api.jira_server_delete_1(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_version_unresolved_issues", tags={"jira-server-other"}
    )
    def jira_server_get_version_unresolved_issues(
        id_: str = Field(..., description="ID of the version."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version unresolved issues count"""
        api = get_api()
        response = api.jira_server_get_version_unresolved_issues(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_remote_version_links_by_version_id",
        tags={"jira-server-other"},
    )
    def jira_server_get_remote_version_links_by_version_id(
        version_id: str = Field(..., description="ID of the version."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get remote version links by version ID"""
        api = get_api()
        response = api.jira_server_get_remote_version_links_by_version_id(
            version_id=version_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_or_update_remote_version_link",
        tags={"jira-server-other"},
    )
    def jira_server_create_or_update_remote_version_link(
        version_id: str = Field(..., description="ID of the version."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create or update remote version link without global ID"""
        api = get_api()
        response = api.jira_server_create_or_update_remote_version_link(
            version_id=version_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_remote_version_links_by_version_id",
        tags={"jira-server-other"},
    )
    def jira_server_delete_remote_version_links_by_version_id(
        version_id: str = Field(..., description="ID of the version."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete all remote version links for version"""
        api = get_api()
        response = api.jira_server_delete_remote_version_links_by_version_id(
            version_id=version_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_remote_version_link", tags={"jira-server-other"})
    def jira_server_get_remote_version_link(
        version_id: str = Field(..., description="ID of the version."),
        global_id: str = Field(
            ...,
            description="The id of the remote issue link to be returned. If (not provided) all remote links for the issue are returned. Remote version links follow the same general rules that Issue Links do, except that they are permitted to use any arbitrary well-formed JSON data format with no restrictions imposed.  It is recommended, but not required, that they follow the same format used for Remote Issue Links, as described at <a href='https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links'>https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links</a>.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get specific remote version link"""
        api = get_api()
        response = api.jira_server_get_remote_version_link(
            version_id=version_id,
            global_id=global_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_create_or_update_remote_version_link_1",
        tags={"jira-server-other"},
    )
    def jira_server_create_or_update_remote_version_link_1(
        version_id: str = Field(..., description="ID of the version."),
        global_id: str = Field(
            ..., description="The id of the remote issue link to be created or updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create or update remote version link with global ID"""
        api = get_api()
        response = api.jira_server_create_or_update_remote_version_link_1(
            version_id=version_id,
            global_id=global_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_remote_version_link", tags={"jira-server-other"})
    def jira_server_delete_remote_version_link(
        version_id: str = Field(..., description="ID of the version."),
        global_id: str = Field(
            ..., description="The id of the remote issue link to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete specific remote version link"""
        api = get_api()
        response = api.jira_server_delete_remote_version_link(
            version_id=version_id,
            global_id=global_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_all_workflows", tags={"jira-server-workflow"})
    def jira_server_get_all_workflows(
        workflow_name: str | None = Field(
            None,
            description="an optional String containing workflow name. If not passed then all workflows are returned",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all workflows"""
        api = get_api()
        response = api.jira_server_get_all_workflows(
            workflow_name=workflow_name,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_scheme", tags={"jira-server-other"})
    def jira_server_create_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new workflow scheme"""
        api = get_api()
        response = api.jira_server_create_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_by_id", tags={"jira-server-other"})
    def jira_server_get_by_id(
        id_: int = Field(..., description="The id of the scheme."),
        return_draft_if_exists: bool | None = Field(
            None,
            description="When true indicates that a scheme's draft, if it exists, should be queried instead of the scheme itself.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get requested workflow scheme by ID"""
        api = get_api()
        response = api.jira_server_get_by_id(
            id_=id_,
            return_draft_if_exists=return_draft_if_exists,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update", tags={"jira-server-other"})
    def jira_server_update(
        id_: int = Field(..., description="The id of the scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a specified workflow scheme"""
        api = get_api()
        response = api.jira_server_update(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_scheme", tags={"jira-server-other"})
    def jira_server_delete_scheme(
        id_: int = Field(..., description="The id of the scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete the specified workflow scheme"""
        api = get_api()
        response = api.jira_server_delete_scheme(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_create_draft_for_parent", tags={"jira-server-other"})
    def jira_server_create_draft_for_parent(
        id_: int = Field(..., description="The id of the parent scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a draft for a workflow scheme"""
        api = get_api()
        response = api.jira_server_create_draft_for_parent(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_default", tags={"jira-server-other"})
    def jira_server_get_default(
        id_: int = Field(..., description="The id of the scheme."),
        return_draft_if_exists: bool | None = Field(
            None,
            description="When true indicates that a scheme's draft, if it exists, should be queried instead of the scheme itself.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get default workflow for a scheme"""
        api = get_api()
        response = api.jira_server_get_default(
            id_=id_,
            return_draft_if_exists=return_draft_if_exists,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_default", tags={"jira-server-other"})
    def jira_server_update_default(
        id_: int = Field(..., description="The id of the scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update default workflow for a scheme"""
        api = get_api()
        response = api.jira_server_update_default(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_default", tags={"jira-server-other"})
    def jira_server_delete_default(
        id_: int = Field(..., description="The id of the scheme."),
        update_draft_if_needed: bool | None = Field(
            None,
            description="When true will create and return a draft when the workflow scheme cannot be edited (e.g. when it is being used by a project).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove default workflow from a scheme"""
        api = get_api()
        response = api.jira_server_delete_default(
            update_draft_if_needed=update_draft_if_needed,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_draft_by_id", tags={"jira-server-other"})
    def jira_server_get_draft_by_id(
        id_: int = Field(..., description="The id of the parent scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get requested draft workflow scheme by ID"""
        api = get_api()
        response = api.jira_server_get_draft_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_draft", tags={"jira-server-other"})
    def jira_server_update_draft(
        id_: int = Field(..., description="The id of the parent scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a draft workflow scheme"""
        api = get_api()
        response = api.jira_server_update_draft(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_draft_by_id", tags={"jira-server-other"})
    def jira_server_delete_draft_by_id(
        id_: int = Field(..., description="The id of the parent scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete the specified draft workflow scheme"""
        api = get_api()
        response = api.jira_server_delete_draft_by_id(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_draft_default", tags={"jira-server-other"})
    def jira_server_get_draft_default(
        id_: int = Field(..., description="The id of the parent scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get default workflow for a draft scheme"""
        api = get_api()
        response = api.jira_server_get_draft_default(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_draft_default", tags={"jira-server-other"})
    def jira_server_update_draft_default(
        id_: int = Field(..., description="The id of the parent scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update default workflow for a draft scheme"""
        api = get_api()
        response = api.jira_server_update_draft_default(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_draft_default", tags={"jira-server-other"})
    def jira_server_delete_draft_default(
        id_: int = Field(..., description="The id of the parent scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove default workflow from a draft scheme"""
        api = get_api()
        response = api.jira_server_delete_draft_default(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_draft_issue_type", tags={"jira-server-issue-type"})
    def jira_server_get_draft_issue_type(
        issue_type: str = Field(..., description="The issue type to query."),
        id_: int = Field(..., description="The id of the parent scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type mapping for a draft scheme"""
        api = get_api()
        response = api.jira_server_get_draft_issue_type(
            issue_type=issue_type,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_draft_issue_type", tags={"jira-server-issue-type"})
    def jira_server_set_draft_issue_type(
        issue_type: str = Field(..., description="The issue type being set."),
        id_: int = Field(..., description="The id of the parent scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set an issue type mapping for a draft scheme"""
        api = get_api()
        response = api.jira_server_set_draft_issue_type(
            issue_type=issue_type,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_draft_issue_type", tags={"jira-server-issue-type"}
    )
    def jira_server_delete_draft_issue_type(
        issue_type: str = Field(..., description="The issue type to remove."),
        id_: int = Field(..., description="The parent of the draft scheme."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete an issue type mapping from a draft scheme"""
        api = get_api()
        response = api.jira_server_delete_draft_issue_type(
            issue_type=issue_type,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_draft_workflow", tags={"jira-server-workflow"})
    def jira_server_get_draft_workflow(
        id_: int = Field(..., description="The id of the parent scheme."),
        workflow_name: str | None = Field(
            None,
            description="The workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get draft workflow mappings"""
        api = get_api()
        response = api.jira_server_get_draft_workflow(
            workflow_name=workflow_name,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_update_draft_workflow_mapping", tags={"jira-server-workflow"}
    )
    def jira_server_update_draft_workflow_mapping(
        id_: int = Field(..., description="The id of the parent scheme."),
        workflow_name: str | None = Field(
            None, description="The name of the workflow mapping to update."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a workflow mapping in a draft scheme"""
        api = get_api()
        response = api.jira_server_update_draft_workflow_mapping(
            workflow_name=workflow_name,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_delete_draft_workflow_mapping", tags={"jira-server-workflow"}
    )
    def jira_server_delete_draft_workflow_mapping(
        id_: int = Field(..., description="The id of the parent scheme."),
        workflow_name: str | None = Field(
            None, description="The name of the workflow to delete."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a workflow mapping from a draft scheme"""
        api = get_api()
        response = api.jira_server_delete_draft_workflow_mapping(
            workflow_name=workflow_name,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_issue_type", tags={"jira-server-issue-type"})
    def jira_server_get_issue_type(
        issue_type: str = Field(..., description="The issue type to query."),
        id_: int = Field(..., description="The id of the scheme."),
        return_draft_if_exists: bool | None = Field(
            None,
            description="When true indicates that a scheme's draft, if it exists, should be queried instead of the scheme itself.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type mapping for a scheme"""
        api = get_api()
        response = api.jira_server_get_issue_type(
            issue_type=issue_type,
            id_=id_,
            return_draft_if_exists=return_draft_if_exists,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_set_issue_type", tags={"jira-server-issue-type"})
    def jira_server_set_issue_type(
        issue_type: str = Field(..., description="The issue type being set."),
        id_: int = Field(..., description="The id of the scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set an issue type mapping for a scheme"""
        api = get_api()
        response = api.jira_server_set_issue_type(
            issue_type=issue_type,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_issue_type", tags={"jira-server-issue-type"})
    def jira_server_delete_issue_type(
        issue_type: str = Field(..., description="The issue type to remove."),
        id_: int = Field(..., description="The id of the scheme."),
        update_draft_if_needed: bool | None = Field(
            None,
            description="When true will create and return a draft when the workflow scheme cannot be edited (e.g. when it is being used by a project).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete an issue type mapping from a scheme"""
        api = get_api()
        response = api.jira_server_delete_issue_type(
            issue_type=issue_type,
            update_draft_if_needed=update_draft_if_needed,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_get_workflow", tags={"jira-server-workflow"})
    def jira_server_get_workflow(
        id_: int = Field(..., description="The id of the scheme."),
        workflow_name: str | None = Field(
            None,
            description="The workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.",
        ),
        return_draft_if_exists: bool | None = Field(
            None,
            description="When true indicates that a scheme's draft, if it exists, should be queried instead of the scheme itself.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow mappings for a scheme"""
        api = get_api()
        response = api.jira_server_get_workflow(
            workflow_name=workflow_name,
            id_=id_,
            return_draft_if_exists=return_draft_if_exists,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_update_workflow_mapping", tags={"jira-server-workflow"})
    def jira_server_update_workflow_mapping(
        id_: int = Field(..., description="The id of the scheme."),
        workflow_name: str | None = Field(
            None, description="The name of the workflow mapping to update."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update a workflow mapping in a scheme"""
        api = get_api()
        response = api.jira_server_update_workflow_mapping(
            workflow_name=workflow_name,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_delete_workflow_mapping", tags={"jira-server-workflow"})
    def jira_server_delete_workflow_mapping(
        id_: int = Field(..., description="The id of the scheme."),
        update_draft_if_needed: bool | None = Field(
            None,
            description="Flag to indicate if a draft should be created if necessary to delete the workflow from the scheme.",
        ),
        workflow_name: str | None = Field(
            None, description="The name of the workflow to delete."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete a workflow mapping from a scheme"""
        api = get_api()
        response = api.jira_server_delete_workflow_mapping(
            update_draft_if_needed=update_draft_if_needed,
            workflow_name=workflow_name,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_ids_of_worklogs_deleted_since",
        tags={"jira-server-issue-worklog"},
    )
    def jira_server_get_ids_of_worklogs_deleted_since(
        since: int | None = Field(
            None,
            description="a date time in unix timestamp format since when deleted worklogs will be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Returns worklogs deleted since given time."""
        api = get_api()
        response = api.jira_server_get_ids_of_worklogs_deleted_since(
            since=since,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_worklogs_for_ids", tags={"jira-server-issue-worklog"}
    )
    def jira_server_get_worklogs_for_ids(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Returns worklogs for given ids."""
        api = get_api()
        response = api.jira_server_get_worklogs_for_ids(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_server_get_ids_of_worklogs_modified_since",
        tags={"jira-server-issue-worklog"},
    )
    def jira_server_get_ids_of_worklogs_modified_since(
        since: int | None = Field(
            None,
            description="a date time in unix timestamp format since when updated worklogs will be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Returns worklogs updated since given time."""
        api = get_api()
        response = api.jira_server_get_ids_of_worklogs_modified_since(
            since=since,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_current_user", tags={"jira-server-user"})
    def jira_server_current_user(_ctx: Context | None = None) -> dict[str, Any]:
        """Get current user session information"""
        api = get_api()
        response = api.jira_server_current_user()
        return response.model_dump()

    @mcp.tool(name="jira_server_login", tags={"jira-server-system"})
    def jira_server_login(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create new user session"""
        api = get_api()
        response = api.jira_server_login(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_server_logout", tags={"jira-server-system"})
    def jira_server_logout(_ctx: Context | None = None) -> dict[str, Any]:
        """Delete current user session"""
        api = get_api()
        response = api.jira_server_logout()
        return response.model_dump()

    @mcp.tool(name="jira_server_release", tags={"jira-server-other"})
    def jira_server_release(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Invalidate the current WebSudo session"""
        api = get_api()
        response = api.jira_server_release(
            payload=payload,
        )
        return response.model_dump()
