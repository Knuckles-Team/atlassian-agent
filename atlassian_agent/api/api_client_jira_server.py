# Generated API Client for JiraServer
from typing import Any

from ..models import Response
from .base import BaseAtlassianClient


class JiraServerAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def jira_server_move_issues_to_backlog(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update issues to move them to the backlog

        Path: /agile/1.0/backlog/issue
        Method: POST
        """
        path = "/agile/1.0/backlog/issue"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_boards(
        self,
        max_results: int | None = None,
        name: str | None = None,
        project_key_or_id: str | None = None,
        type_: str | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all boards

        Path: /agile/1.0/board
        Method: GET
        """
        path = "/agile/1.0/board"
        params = {
            "maxResults": max_results,
            "name": name,
            "projectKeyOrId": project_key_or_id,
            "type": type_,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_board(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a new board

        Path: /agile/1.0/board
        Method: POST
        """
        path = "/agile/1.0/board"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_board(
        self,
        board_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a single board

        Path: /agile/1.0/board/{boardId}
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_board(
        self,
        board_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete the board

        Path: /agile/1.0/board/{boardId}
        Method: DELETE
        """
        path = f"/agile/1.0/board/{board_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issues_for_backlog(
        self,
        board_id: int,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issues from the board's backlog

        Path: /agile/1.0/board/{boardId}/backlog
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/backlog"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_configuration(
        self,
        board_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the board configuration

        Path: /agile/1.0/board/{boardId}/configuration
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/configuration"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_epics(
        self,
        board_id: int,
        max_results: int | None = None,
        done: str | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all epics from the board

        Path: /agile/1.0/board/{boardId}/epic
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/epic"
        params = {
            "maxResults": max_results,
            "done": done,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issues_without_epic(
        self,
        board_id: int,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issues without an epic

        Path: /agile/1.0/board/{boardId}/epic/none/issue
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/epic/none/issue"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issues_for_epic(
        self,
        epic_id: int,
        board_id: int,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issues for a specific epic

        Path: /agile/1.0/board/{boardId}/epic/{epicId}/issue
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/epic/{epic_id}/issue"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issues_for_board(
        self,
        board_id: int,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issues from a board

        Path: /agile/1.0/board/{boardId}/issue
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/issue"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_projects(
        self,
        board_id: int,
        max_results: int | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all projects associated with the board

        Path: /agile/1.0/board/{boardId}/project
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/project"
        params = {
            "maxResults": max_results,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_properties_keys(
        self,
        board_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all properties keys for a board

        Path: /agile/1.0/board/{boardId}/properties
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_property(
        self,
        property_key: str,
        board_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a property from a board

        Path: /agile/1.0/board/{boardId}/properties/{propertyKey}
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_property(
        self,
        property_key: str,
        board_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a board's property

        Path: /agile/1.0/board/{boardId}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/agile/1.0/board/{board_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_property(
        self,
        property_key: str,
        board_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a property from a board

        Path: /agile/1.0/board/{boardId}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/agile/1.0/board/{board_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_refined_velocity(
        self,
        board_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the value of the refined velocity setting

        Path: /agile/1.0/board/{boardId}/settings/refined-velocity
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/settings/refined-velocity"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_refined_velocity(
        self,
        board_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update the board's refined velocity setting

        Path: /agile/1.0/board/{boardId}/settings/refined-velocity
        Method: PUT
        """
        path = f"/agile/1.0/board/{board_id}/settings/refined-velocity"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_sprints(
        self,
        board_id: int,
        max_results: int | None = None,
        state: str | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all sprints from a board

        Path: /agile/1.0/board/{boardId}/sprint
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/sprint"
        params = {
            "maxResults": max_results,
            "state": state,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issues_for_sprint(
        self,
        sprint_id: int,
        board_id: int,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issues for a sprint

        Path: /agile/1.0/board/{boardId}/sprint/{sprintId}/issue
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/sprint/{sprint_id}/issue"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_versions(
        self,
        board_id: int,
        max_results: int | None = None,
        released: str | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all versions from a board

        Path: /agile/1.0/board/{boardId}/version
        Method: GET
        """
        path = f"/agile/1.0/board/{board_id}/version"
        params = {
            "maxResults": max_results,
            "released": released,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issues_without_epic_1(
        self,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issues without an epic

        Path: /agile/1.0/epic/none/issue
        Method: GET
        """
        path = "/agile/1.0/epic/none/issue"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_issues_from_epic(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Remove issues from any epic

        Path: /agile/1.0/epic/none/issue
        Method: POST
        """
        path = "/agile/1.0/epic/none/issue"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_epic(
        self,
        epic_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get an epic by id or key

        Path: /agile/1.0/epic/{epicIdOrKey}
        Method: GET
        """
        path = f"/agile/1.0/epic/{epic_id_or_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_partially_update_epic(
        self,
        epic_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update an epic's details

        Path: /agile/1.0/epic/{epicIdOrKey}
        Method: POST
        """
        path = f"/agile/1.0/epic/{epic_id_or_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issues_for_epic_1(
        self,
        epic_id_or_key: str,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issues for a specific epic

        Path: /agile/1.0/epic/{epicIdOrKey}/issue
        Method: GET
        """
        path = f"/agile/1.0/epic/{epic_id_or_key}/issue"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_move_issues_to_epic(
        self,
        epic_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move issues to a specific epic

        Path: /agile/1.0/epic/{epicIdOrKey}/issue
        Method: POST
        """
        path = f"/agile/1.0/epic/{epic_id_or_key}/issue"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_rank_epics(
        self,
        epic_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Rank an epic relative to another

        Path: /agile/1.0/epic/{epicIdOrKey}/rank
        Method: PUT
        """
        path = f"/agile/1.0/epic/{epic_id_or_key}/rank"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_rank_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Rank issues before or after a given issue

        Path: /agile/1.0/issue/rank
        Method: PUT
        """
        path = "/agile/1.0/issue/rank"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue(
        self,
        issue_id_or_key: str,
        expand: str | None = None,
        fields: list[Any] | None = None,
        update_history: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a single issue with Agile fields

        Path: /agile/1.0/issue/{issueIdOrKey}
        Method: GET
        """
        path = f"/agile/1.0/issue/{issue_id_or_key}"
        params = {
            "expand": expand,
            "fields": fields,
            "updateHistory": update_history,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_estimation_for_board(
        self,
        issue_id_or_key: str,
        board_id: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the estimation of an issue for a board

        Path: /agile/1.0/issue/{issueIdOrKey}/estimation
        Method: GET
        """
        path = f"/agile/1.0/issue/{issue_id_or_key}/estimation"
        params = {
            "boardId": board_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_estimate_issue_for_board(
        self,
        issue_id_or_key: str,
        board_id: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update the estimation of an issue for a board

        Path: /agile/1.0/issue/{issueIdOrKey}/estimation
        Method: PUT
        """
        path = f"/agile/1.0/issue/{issue_id_or_key}/estimation"
        params = {
            "boardId": board_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_create_sprint(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a future sprint

        Path: /agile/1.0/sprint
        Method: POST
        """
        path = "/agile/1.0/sprint"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_unmap_sprints(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Unmap sprints from being synced

        Path: /agile/1.0/sprint/unmap
        Method: PUT
        """
        path = "/agile/1.0/sprint/unmap"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_unmap_all_sprints(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Unmap all sprints from being synced

        Path: /agile/1.0/sprint/unmap-all
        Method: PUT
        """
        path = "/agile/1.0/sprint/unmap-all"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_sprint(
        self,
        sprint_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get sprint by id

        Path: /agile/1.0/sprint/{sprintId}
        Method: GET
        """
        path = f"/agile/1.0/sprint/{sprint_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_sprint(
        self,
        sprint_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a sprint fully

        Path: /agile/1.0/sprint/{sprintId}
        Method: PUT
        """
        path = f"/agile/1.0/sprint/{sprint_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_partially_update_sprint(
        self,
        sprint_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Partially update a sprint

        Path: /agile/1.0/sprint/{sprintId}
        Method: POST
        """
        path = f"/agile/1.0/sprint/{sprint_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_sprint(
        self,
        sprint_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a sprint

        Path: /agile/1.0/sprint/{sprintId}
        Method: DELETE
        """
        path = f"/agile/1.0/sprint/{sprint_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issues_for_sprint_1(
        self,
        sprint_id: int,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issues in a sprint

        Path: /agile/1.0/sprint/{sprintId}/issue
        Method: GET
        """
        path = f"/agile/1.0/sprint/{sprint_id}/issue"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_move_issues_to_sprint(
        self,
        sprint_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move issues to a sprint

        Path: /agile/1.0/sprint/{sprintId}/issue
        Method: POST
        """
        path = f"/agile/1.0/sprint/{sprint_id}/issue"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_properties_keys_1(
        self,
        sprint_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all properties keys for a sprint

        Path: /agile/1.0/sprint/{sprintId}/properties
        Method: GET
        """
        path = f"/agile/1.0/sprint/{sprint_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_property_1(
        self,
        property_key: str,
        sprint_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a property for a sprint

        Path: /agile/1.0/sprint/{sprintId}/properties/{propertyKey}
        Method: GET
        """
        path = f"/agile/1.0/sprint/{sprint_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_property_1(
        self,
        property_key: str,
        sprint_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a sprint's property

        Path: /agile/1.0/sprint/{sprintId}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/agile/1.0/sprint/{sprint_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_property_1(
        self,
        property_key: str,
        sprint_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a sprint's property

        Path: /agile/1.0/sprint/{sprintId}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/agile/1.0/sprint/{sprint_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_swap_sprint(
        self,
        sprint_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Swap the position of two sprints

        Path: /agile/1.0/sprint/{sprintId}/swap
        Method: POST
        """
        path = f"/agile/1.0/sprint/{sprint_id}/swap"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_application_property(
        self,
        permission_level: str,
        key: str,
        key_filter: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get an application property by key

        Path: /api/2/application-properties
        Method: GET
        """
        path = "/api/2/application-properties"
        params = {
            "permissionLevel": permission_level,
            "keyFilter": key_filter,
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_advanced_settings(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all advanced settings properties

        Path: /api/2/application-properties/advanced-settings
        Method: GET
        """
        path = "/api/2/application-properties/advanced-settings"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_property_via_restful_table(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update an application property

        Path: /api/2/application-properties/{id}
        Method: PUT
        """
        path = f"/api/2/application-properties/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all application roles in the system

        Path: /api/2/applicationrole
        Method: GET
        """
        path = "/api/2/applicationrole"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_put_bulk(
        self,
        if_match: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update application roles

        Path: /api/2/applicationrole
        Method: PUT
        """
        path = "/api/2/applicationrole"
        params = {
            "If-Match": if_match,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_4(
        self,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get application role by key

        Path: /api/2/applicationrole/{key}
        Method: GET
        """
        path = f"/api/2/applicationrole/{key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_put_2(
        self,
        key: str,
        if_match: str | None = None,
        version_hash: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update application role

        Path: /api/2/applicationrole/{key}
        Method: PUT
        """
        path = f"/api/2/applicationrole/{key}"
        params = {
            "If-Match": if_match,
            "versionHash": version_hash,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_attachment_meta(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get attachment capabilities

        Path: /api/2/attachment/meta
        Method: GET
        """
        path = "/api/2/attachment/meta"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_attachment(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the meta-data for an attachment, including the URI of the actual attached file

        Path: /api/2/attachment/{id}
        Method: GET
        """
        path = f"/api/2/attachment/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_attachment(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete an attachment from an issue

        Path: /api/2/attachment/{id}
        Method: DELETE
        """
        path = f"/api/2/attachment/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_expand_for_humans(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get human-readable attachment expansion

        Path: /api/2/attachment/{id}/expand/human
        Method: GET
        """
        path = f"/api/2/attachment/{id_}/expand/human"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_expand_for_machines(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get raw attachment expansion

        Path: /api/2/attachment/{id}/expand/raw
        Method: GET
        """
        path = f"/api/2/attachment/{id_}/expand/raw"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_system_avatars(
        self,
        type_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all system avatars

        Path: /api/2/avatar/{type}/system
        Method: GET
        """
        path = f"/api/2/avatar/{type_}/system"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_request_current_index_from_node(
        self,
        node_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Request node index snapshot

        Path: /api/2/cluster/index-snapshot/{nodeId}
        Method: PUT
        """
        path = f"/api/2/cluster/index-snapshot/{node_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_node(
        self,
        node_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a cluster node

        Path: /api/2/cluster/node/{nodeId}
        Method: DELETE
        """
        path = f"/api/2/cluster/node/{node_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_change_node_state_to_offline(
        self,
        node_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update node state to offline

        Path: /api/2/cluster/node/{nodeId}/offline
        Method: PUT
        """
        path = f"/api/2/cluster/node/{node_id}/offline"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_nodes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all cluster nodes

        Path: /api/2/cluster/nodes
        Method: GET
        """
        path = "/api/2/cluster/nodes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_approve_upgrade(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Approve cluster upgrade

        Path: /api/2/cluster/zdu/approve
        Method: POST
        """
        path = "/api/2/cluster/zdu/approve"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_cancel_upgrade(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Cancel cluster upgrade

        Path: /api/2/cluster/zdu/cancel
        Method: POST
        """
        path = "/api/2/cluster/zdu/cancel"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_acknowledge_errors(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Retry cluster upgrade

        Path: /api/2/cluster/zdu/retryUpgrade
        Method: POST
        """
        path = "/api/2/cluster/zdu/retryUpgrade"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_set_ready_to_upgrade(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Start cluster upgrade

        Path: /api/2/cluster/zdu/start
        Method: POST
        """
        path = "/api/2/cluster/zdu/start"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_state(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get cluster upgrade state

        Path: /api/2/cluster/zdu/state
        Method: GET
        """
        path = "/api/2/cluster/zdu/state"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_properties_keys_1_2(
        self,
        comment_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get properties keys of a comment

        Path: /api/2/comment/{commentId}/properties
        Method: GET
        """
        path = f"/api/2/comment/{comment_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_comment_property(
        self,
        property_key: str,
        comment_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a property from a comment

        Path: /api/2/comment/{commentId}/properties/{propertyKey}
        Method: GET
        """
        path = f"/api/2/comment/{comment_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_property_1_2(
        self,
        property_key: str,
        comment_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set a property on a comment

        Path: /api/2/comment/{commentId}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/api/2/comment/{comment_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_property_2(
        self,
        property_key: str,
        comment_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a property from a comment

        Path: /api/2/comment/{commentId}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/api/2/comment/{comment_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_create_component(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create component

        Path: /api/2/component
        Method: POST
        """
        path = "/api/2/component"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_paginated_components(
        self,
        max_results: str | None = None,
        query: str | None = None,
        project_ids: str | None = None,
        start_at: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get paginated components

        Path: /api/2/component/page
        Method: GET
        """
        path = "/api/2/component/page"
        params = {
            "maxResults": max_results,
            "query": query,
            "projectIds": project_ids,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_component(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project component

        Path: /api/2/component/{id}
        Method: GET
        """
        path = f"/api/2/component/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_component(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a component

        Path: /api/2/component/{id}
        Method: PUT
        """
        path = f"/api/2/component/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete(
        self,
        id_: str,
        move_issues_to: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a project component

        Path: /api/2/component/{id}
        Method: DELETE
        """
        path = f"/api/2/component/{id_}"
        params = {
            "moveIssuesTo": move_issues_to,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_component_related_issues(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get component related issues

        Path: /api/2/component/{id}/relatedIssueCounts
        Method: GET
        """
        path = f"/api/2/component/{id_}/relatedIssueCounts"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_configuration_1(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get Jira configuration details

        Path: /api/2/configuration
        Method: GET
        """
        path = "/api/2/configuration"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_custom_field_option(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom field option by ID

        Path: /api/2/customFieldOption/{id}
        Method: GET
        """
        path = f"/api/2/customFieldOption/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_custom_fields(
        self,
        sort_column: str | None = None,
        types: str | None = None,
        search: str | None = None,
        max_results: str | None = None,
        sort_order: str | None = None,
        screen_ids: str | None = None,
        last_value_update: str | None = None,
        project_ids: str | None = None,
        start_at: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom fields with pagination

        Path: /api/2/customFields
        Method: GET
        """
        path = "/api/2/customFields"
        params = {
            "sortColumn": sort_column,
            "types": types,
            "search": search,
            "maxResults": max_results,
            "sortOrder": sort_order,
            "screenIds": screen_ids,
            "lastValueUpdate": last_value_update,
            "projectIds": project_ids,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_bulk_delete_custom_fields(
        self,
        ids: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete custom fields in bulk

        Path: /api/2/customFields
        Method: DELETE
        """
        path = "/api/2/customFields"
        params = {
            "ids": ids,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_custom_field_options(
        self,
        custom_field_id: str,
        max_results: str | None = None,
        issue_type_ids: str | None = None,
        query: str | None = None,
        sort_by_option_name: str | None = None,
        use_all_contexts: str | None = None,
        page: str | None = None,
        project_ids: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom field options

        Path: /api/2/customFields/{customFieldId}/options
        Method: GET
        """
        path = f"/api/2/customFields/{custom_field_id}/options"
        params = {
            "maxResults": max_results,
            "issueTypeIds": issue_type_ids,
            "query": query,
            "sortByOptionName": sort_by_option_name,
            "useAllContexts": use_all_contexts,
            "page": page,
            "projectIds": project_ids,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_list(
        self,
        filter: str | None = None,
        max_results: str | None = None,
        start_at: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all dashboards with optional filtering

        Path: /api/2/dashboard
        Method: GET
        """
        path = "/api/2/dashboard"
        params = {
            "filter": filter,
            "maxResults": max_results,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_dashboard_item_properties_keys(
        self,
        item_id: str,
        dashboard_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all properties keys for a dashboard item

        Path: /api/2/dashboard/{dashboardId}/items/{itemId}/properties
        Method: GET
        """
        path = f"/api/2/dashboard/{dashboard_id}/items/{item_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_property_1_2(
        self,
        property_key: str,
        item_id: str,
        dashboard_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a property from a dashboard item

        Path: /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
        Method: GET
        """
        path = (
            f"/api/2/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        )
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_dashboard_item_property(
        self,
        property_key: str,
        item_id: str,
        dashboard_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set a property on a dashboard item

        Path: /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
        Method: PUT
        """
        path = (
            f"/api/2/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        )
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_property_1_2(
        self,
        property_key: str,
        item_id: str,
        dashboard_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a property from a dashboard item

        Path: /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
        Method: DELETE
        """
        path = (
            f"/api/2/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        )
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_dashboard(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a single dashboard by ID

        Path: /api/2/dashboard/{id}
        Method: GET
        """
        path = f"/api/2/dashboard/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_download_email_templates(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get email templates as zip file

        Path: /api/2/email-templates
        Method: GET
        """
        path = "/api/2/email-templates"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_upload_email_templates(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update email templates with zip file

        Path: /api/2/email-templates
        Method: POST
        """
        path = "/api/2/email-templates"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_apply_email_templates(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update email templates with previously uploaded pack

        Path: /api/2/email-templates/apply
        Method: POST
        """
        path = "/api/2/email-templates/apply"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_revert_email_templates_to_default(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update email templates to default

        Path: /api/2/email-templates/revert
        Method: POST
        """
        path = "/api/2/email-templates/revert"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_email_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get email types for templates

        Path: /api/2/email-templates/types
        Method: GET
        """
        path = "/api/2/email-templates/types"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_fields(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all fields, both System and Custom

        Path: /api/2/field
        Method: GET
        """
        path = "/api/2/field"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_custom_field(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a custom field using a definition

        Path: /api/2/field
        Method: POST
        """
        path = "/api/2/field"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_create_filter(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a new filter

        Path: /api/2/filter
        Method: POST
        """
        path = "/api/2/filter"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_default_share_scope(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get default share scope

        Path: /api/2/filter/defaultShareScope
        Method: GET
        """
        path = "/api/2/filter/defaultShareScope"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_default_share_scope(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set default share scope

        Path: /api/2/filter/defaultShareScope
        Method: PUT
        """
        path = "/api/2/filter/defaultShareScope"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_favourite_filters(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get favourite filters

        Path: /api/2/filter/favourite
        Method: GET
        """
        path = "/api/2/filter/favourite"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_filter(
        self,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a filter by ID

        Path: /api/2/filter/{id}
        Method: GET
        """
        path = f"/api/2/filter/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_edit_filter(
        self,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update an existing filter

        Path: /api/2/filter/{id}
        Method: PUT
        """
        path = f"/api/2/filter/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_filter(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a filter

        Path: /api/2/filter/{id}
        Method: DELETE
        """
        path = f"/api/2/filter/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_default_columns_1(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get default columns for filter

        Path: /api/2/filter/{id}/columns
        Method: GET
        """
        path = f"/api/2/filter/{id_}/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_columns_1(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set default columns for filter

        Path: /api/2/filter/{id}/columns
        Method: PUT
        """
        path = f"/api/2/filter/{id_}/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_reset_columns_1(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset columns for filter

        Path: /api/2/filter/{id}/columns
        Method: DELETE
        """
        path = f"/api/2/filter/{id_}/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_share_permissions(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all share permissions of filter

        Path: /api/2/filter/{id}/permission
        Method: GET
        """
        path = f"/api/2/filter/{id_}/permission"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_share_permission(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add share permissions to filter

        Path: /api/2/filter/{id}/permission
        Method: POST
        """
        path = f"/api/2/filter/{id_}/permission"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_share_permission(
        self,
        permission_id: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove share permissions from filter

        Path: /api/2/filter/{id}/permission/{permission-id}
        Method: DELETE
        """
        path = f"/api/2/filter/{id_}/permission/{permission_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_share_permission(
        self,
        permission_id: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a single share permission of filter

        Path: /api/2/filter/{id}/permission/{permissionId}
        Method: GET
        """
        path = f"/api/2/filter/{id_}/permission/{permission_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_group(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a group with given parameters

        Path: /api/2/group
        Method: POST
        """
        path = "/api/2/group"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_group(
        self,
        groupname: str,
        swap_group: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a specified group

        Path: /api/2/group
        Method: DELETE
        """
        path = "/api/2/group"
        params = {
            "groupname": groupname,
            "swapGroup": swap_group,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_users_from_group(
        self,
        groupname: str,
        include_inactive_users: str | None = None,
        max_results: str | None = None,
        start_at: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get users from a specified group

        Path: /api/2/group/member
        Method: GET
        """
        path = "/api/2/group/member"
        params = {
            "includeInactiveUsers": include_inactive_users,
            "maxResults": max_results,
            "groupname": groupname,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_user_to_group(
        self,
        groupname: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add a user to a specified group

        Path: /api/2/group/user
        Method: POST
        """
        path = "/api/2/group/user"
        params = {
            "groupname": groupname,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_user_from_group(
        self,
        groupname: str,
        username: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove a user from a specified group

        Path: /api/2/group/user
        Method: DELETE
        """
        path = "/api/2/group/user"
        params = {
            "groupname": groupname,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_find_groups(
        self,
        max_results: str | None = None,
        query: str | None = None,
        exclude: str | None = None,
        user_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get groups matching a query

        Path: /api/2/groups/picker
        Method: GET
        """
        path = "/api/2/groups/picker"
        params = {
            "maxResults": max_results,
            "query": query,
            "exclude": exclude,
            "userName": user_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_find_users_and_groups(
        self,
        issue_type_id: str | None = None,
        max_results: str | None = None,
        query: str | None = None,
        show_avatar: str | None = None,
        project_id: str | None = None,
        field_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get users and groups matching query with highlighting

        Path: /api/2/groupuserpicker
        Method: GET
        """
        path = "/api/2/groupuserpicker"
        params = {
            "issueTypeId": issue_type_id,
            "maxResults": max_results,
            "query": query,
            "showAvatar": show_avatar,
            "projectId": project_id,
            "fieldId": field_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_list_index_snapshot(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get list of available index snapshots

        Path: /api/2/index-snapshot
        Method: GET
        """
        path = "/api/2/index-snapshot"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_index_snapshot(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create index snapshot if not in progress

        Path: /api/2/index-snapshot
        Method: POST
        """
        path = "/api/2/index-snapshot"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_is_index_snapshot_running(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get index snapshot creation status

        Path: /api/2/index-snapshot/isRunning
        Method: GET
        """
        path = "/api/2/index-snapshot/isRunning"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_index_summary(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get index condition summary

        Path: /api/2/index/summary
        Method: GET
        """
        path = "/api/2/index/summary"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_issue(
        self,
        update_history: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create an issue or sub-task from json

        Path: /api/2/issue
        Method: POST
        """
        path = "/api/2/issue"
        params = {
            "updateHistory": update_history,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_archive_issues(
        self,
        notify_users: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Archive list of issues

        Path: /api/2/issue/archive
        Method: POST
        """
        path = "/api/2/issue/archive"
        params = {
            "notifyUsers": notify_users,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_create_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create an issue or sub-task from json - bulk operation.

        Path: /api/2/issue/bulk
        Method: POST
        """
        path = "/api/2/issue/bulk"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_create_issue_meta_project_issue_types(
        self,
        project_id_or_key: str,
        max_results: str | None = None,
        start_at: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get metadata for project issue types

        Path: /api/2/issue/createmeta/{projectIdOrKey}/issuetypes
        Method: GET
        """
        path = f"/api/2/issue/createmeta/{project_id_or_key}/issuetypes"
        params = {
            "maxResults": max_results,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_create_issue_meta_fields(
        self,
        issue_type_id: str,
        project_id_or_key: str,
        max_results: str | None = None,
        start_at: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get metadata for issue types used for creating issues

        Path: /api/2/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}
        Method: GET
        """
        path = f"/api/2/issue/createmeta/{project_id_or_key}/issuetypes/{issue_type_id}"
        params = {
            "maxResults": max_results,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_picker_resource(
        self,
        current_project_id: str | None = None,
        query: str | None = None,
        current_issue_key: str | None = None,
        show_sub_tasks: str | None = None,
        current_jql: str | None = None,
        show_sub_task_parent: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get suggested issues for auto-completion

        Path: /api/2/issue/picker
        Method: GET
        """
        path = "/api/2/issue/picker"
        params = {
            "currentProjectId": current_project_id,
            "query": query,
            "currentIssueKey": current_issue_key,
            "showSubTasks": show_sub_tasks,
            "currentJQL": current_jql,
            "showSubTaskParent": show_sub_task_parent,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_reciprocal_remote_issue_link(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create reciprocal remote issue link

        Path: /api/2/issue/remotelink/reciprocal
        Method: POST
        """
        path = "/api/2/issue/remotelink/reciprocal"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_2(
        self,
        issue_id_or_key: str,
        expand: str | None = None,
        fields: str | None = None,
        update_history: str | None = None,
        properties: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue for key

        Path: /api/2/issue/{issueIdOrKey}
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}"
        params = {
            "expand": expand,
            "fields": fields,
            "updateHistory": update_history,
            "properties": properties,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_edit_issue(
        self,
        issue_id_or_key: str,
        notify_users: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Edit an issue from a JSON representation

        Path: /api/2/issue/{issueIdOrKey}
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}"
        params = {
            "notifyUsers": notify_users,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_issue(
        self,
        issue_id_or_key: str,
        delete_subtasks: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete an issue

        Path: /api/2/issue/{issueIdOrKey}
        Method: DELETE
        """
        path = f"/api/2/issue/{issue_id_or_key}"
        params = {
            "deleteSubtasks": delete_subtasks,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_archive_issue(
        self,
        issue_id_or_key: str,
        notify_users: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Archive an issue

        Path: /api/2/issue/{issueIdOrKey}/archive
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}/archive"
        params = {
            "notifyUsers": notify_users,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_assign(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign an issue to a user

        Path: /api/2/issue/{issueIdOrKey}/assignee
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}/assignee"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_add_attachment(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add one or more attachments to an issue

        Path: /api/2/issue/{issueIdOrKey}/attachments
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/attachments"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_comments(
        self,
        issue_id_or_key: str,
        expand: str | None = None,
        max_results: str | None = None,
        order_by: str | None = None,
        start_at: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get comments for an issue

        Path: /api/2/issue/{issueIdOrKey}/comment
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/comment"
        params = {
            "expand": expand,
            "maxResults": max_results,
            "orderBy": order_by,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_comment(
        self,
        issue_id_or_key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add a comment

        Path: /api/2/issue/{issueIdOrKey}/comment
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/comment"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_comment(
        self,
        issue_id_or_key: str,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a comment by id

        Path: /api/2/issue/{issueIdOrKey}/comment/{id}
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/comment/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_comment(
        self,
        issue_id_or_key: str,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a comment

        Path: /api/2/issue/{issueIdOrKey}/comment/{id}
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}/comment/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_comment(
        self,
        issue_id_or_key: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a comment

        Path: /api/2/issue/{issueIdOrKey}/comment/{id}
        Method: DELETE
        """
        path = f"/api/2/issue/{issue_id_or_key}/comment/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_set_pin_comment(
        self,
        issue_id_or_key: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Pin a comment

        Path: /api/2/issue/{issueIdOrKey}/comment/{id}/pin
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}/comment/{id_}/pin"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_edit_issue_meta(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get metadata for issue types used for editing issues

        Path: /api/2/issue/{issueIdOrKey}/editmeta
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/editmeta"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_notify(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Send notification to recipients

        Path: /api/2/issue/{issueIdOrKey}/notify
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/notify"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_pinned_comments(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get pinned comments for an issue

        Path: /api/2/issue/{issueIdOrKey}/pinned-comments
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/pinned-comments"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_properties_keys(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get keys of all properties for an issue

        Path: /api/2/issue/{issueIdOrKey}/properties
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_property_3(
        self,
        property_key: str,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the value of a specific property from an issue

        Path: /api/2/issue/{issueIdOrKey}/properties/{propertyKey}
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_issue_property(
        self,
        property_key: str,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update the value of a specific issue's property

        Path: /api/2/issue/{issueIdOrKey}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_property_3(
        self,
        property_key: str,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a property from an issue

        Path: /api/2/issue/{issueIdOrKey}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/api/2/issue/{issue_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_remote_issue_links(
        self,
        issue_id_or_key: str,
        global_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get remote issue links for an issue

        Path: /api/2/issue/{issueIdOrKey}/remotelink
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/remotelink"
        params = {
            "globalId": global_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_or_update_remote_issue_link(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create or update remote issue link

        Path: /api/2/issue/{issueIdOrKey}/remotelink
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/remotelink"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_remote_issue_link_by_global_id(
        self,
        issue_id_or_key: str,
        global_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete remote issue link

        Path: /api/2/issue/{issueIdOrKey}/remotelink
        Method: DELETE
        """
        path = f"/api/2/issue/{issue_id_or_key}/remotelink"
        params = {
            "globalId": global_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_remote_issue_link_by_id(
        self,
        link_id: str,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a remote issue link by its id

        Path: /api/2/issue/{issueIdOrKey}/remotelink/{linkId}
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/remotelink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_remote_issue_link(
        self,
        link_id: str,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update remote issue link

        Path: /api/2/issue/{issueIdOrKey}/remotelink/{linkId}
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}/remotelink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_remote_issue_link_by_id(
        self,
        link_id: str,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete remote issue link by id

        Path: /api/2/issue/{issueIdOrKey}/remotelink/{linkId}
        Method: DELETE
        """
        path = f"/api/2/issue/{issue_id_or_key}/remotelink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_restore_issue(
        self,
        issue_id_or_key: str,
        notify_users: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Restore an archived issue

        Path: /api/2/issue/{issueIdOrKey}/restore
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}/restore"
        params = {
            "notifyUsers": notify_users,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_sub_tasks(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get an issue's subtask list

        Path: /api/2/issue/{issueIdOrKey}/subtask
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/subtask"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_can_move_sub_task(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Check if a subtask can be moved

        Path: /api/2/issue/{issueIdOrKey}/subtask/move
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/subtask/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_move_sub_tasks(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reorder an issue's subtasks

        Path: /api/2/issue/{issueIdOrKey}/subtask/move
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/subtask/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_transitions(
        self,
        issue_id_or_key: str,
        transition_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get list of transitions possible for an issue

        Path: /api/2/issue/{issueIdOrKey}/transitions
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/transitions"
        params = {
            "transitionId": transition_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_do_transition(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Perform a transition on an issue

        Path: /api/2/issue/{issueIdOrKey}/transitions
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/transitions"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_votes(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get votes for issue

        Path: /api/2/issue/{issueIdOrKey}/votes
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/votes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_vote(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add vote to issue

        Path: /api/2/issue/{issueIdOrKey}/votes
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/votes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_vote(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove vote from issue

        Path: /api/2/issue/{issueIdOrKey}/votes
        Method: DELETE
        """
        path = f"/api/2/issue/{issue_id_or_key}/votes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_watchers(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get list of watchers of issue

        Path: /api/2/issue/{issueIdOrKey}/watchers
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/watchers"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_watcher_1(
        self,
        issue_id_or_key: str,
        user_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add a user as watcher

        Path: /api/2/issue/{issueIdOrKey}/watchers
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/watchers"
        params = {
            "userName": user_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_watcher_1(
        self,
        issue_id_or_key: str,
        user_name: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete watcher from issue

        Path: /api/2/issue/{issueIdOrKey}/watchers
        Method: DELETE
        """
        path = f"/api/2/issue/{issue_id_or_key}/watchers"
        params = {
            "userName": user_name,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_worklog(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get worklogs for an issue

        Path: /api/2/issue/{issueIdOrKey}/worklog
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/worklog"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_worklog(
        self,
        issue_id_or_key: str,
        new_estimate: str | None = None,
        adjust_estimate: str | None = None,
        reduce_by: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add a worklog entry

        Path: /api/2/issue/{issueIdOrKey}/worklog
        Method: POST
        """
        path = f"/api/2/issue/{issue_id_or_key}/worklog"
        params = {
            "newEstimate": new_estimate,
            "adjustEstimate": adjust_estimate,
            "reduceBy": reduce_by,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_worklog(
        self,
        issue_id_or_key: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a worklog by id

        Path: /api/2/issue/{issueIdOrKey}/worklog/{id}
        Method: GET
        """
        path = f"/api/2/issue/{issue_id_or_key}/worklog/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_worklog(
        self,
        issue_id_or_key: str,
        id_: str,
        new_estimate: str | None = None,
        adjust_estimate: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a worklog entry

        Path: /api/2/issue/{issueIdOrKey}/worklog/{id}
        Method: PUT
        """
        path = f"/api/2/issue/{issue_id_or_key}/worklog/{id_}"
        params = {
            "newEstimate": new_estimate,
            "adjustEstimate": adjust_estimate,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_worklog(
        self,
        issue_id_or_key: str,
        id_: str,
        new_estimate: str | None = None,
        adjust_estimate: str | None = None,
        increase_by: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a worklog entry

        Path: /api/2/issue/{issueIdOrKey}/worklog/{id}
        Method: DELETE
        """
        path = f"/api/2/issue/{issue_id_or_key}/worklog/{id_}"
        params = {
            "newEstimate": new_estimate,
            "adjustEstimate": adjust_estimate,
            "increaseBy": increase_by,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_link_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create an issue link between two issues

        Path: /api/2/issueLink
        Method: POST
        """
        path = "/api/2/issueLink"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_link(
        self,
        link_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get an issue link with the specified id

        Path: /api/2/issueLink/{linkId}
        Method: GET
        """
        path = f"/api/2/issueLink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_issue_link(
        self,
        link_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete an issue link with the specified id

        Path: /api/2/issueLink/{linkId}
        Method: DELETE
        """
        path = f"/api/2/issueLink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_link_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get list of available issue link types

        Path: /api/2/issueLinkType
        Method: GET
        """
        path = "/api/2/issueLinkType"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_issue_link_type(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a new issue link type

        Path: /api/2/issueLinkType
        Method: POST
        """
        path = "/api/2/issueLinkType"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_reset_order(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Reset the order of issue link types alphabetically.

        Path: /api/2/issueLinkType/order
        Method: PUT
        """
        path = "/api/2/issueLinkType/order"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_link_type(
        self,
        issue_link_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get information about an issue link type

        Path: /api/2/issueLinkType/{issueLinkTypeId}
        Method: GET
        """
        path = f"/api/2/issueLinkType/{issue_link_type_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_issue_link_type(
        self,
        issue_link_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update the specified issue link type

        Path: /api/2/issueLinkType/{issueLinkTypeId}
        Method: PUT
        """
        path = f"/api/2/issueLinkType/{issue_link_type_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_issue_link_type(
        self,
        issue_link_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete the specified issue link type

        Path: /api/2/issueLinkType/{issueLinkTypeId}
        Method: DELETE
        """
        path = f"/api/2/issueLinkType/{issue_link_type_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_move_issue_link_type(
        self,
        issue_link_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update the order of the issue link type.

        Path: /api/2/issueLinkType/{issueLinkTypeId}/order
        Method: PUT
        """
        path = f"/api/2/issueLinkType/{issue_link_type_id}/order"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_security_schemes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all issue security schemes

        Path: /api/2/issuesecurityschemes
        Method: GET
        """
        path = "/api/2/issuesecurityschemes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_security_scheme(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get specific issue security scheme by id

        Path: /api/2/issuesecurityschemes/{id}
        Method: GET
        """
        path = f"/api/2/issuesecurityschemes/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_all_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get list of all issue types visible to user

        Path: /api/2/issuetype
        Method: GET
        """
        path = "/api/2/issuetype"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_issue_type(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create an issue type from JSON representation

        Path: /api/2/issuetype
        Method: POST
        """
        path = "/api/2/issuetype"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_paginated_issue_types(
        self,
        x_requested_with: str | None = None,
        max_results: int | None = None,
        query: str | None = None,
        project_ids: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get paginated list of filtered issue types

        Path: /api/2/issuetype/page
        Method: GET
        """
        path = "/api/2/issuetype/page"
        params = {
            "X-Requested-With": x_requested_with,
            "maxResults": max_results,
            "query": query,
            "projectIds": project_ids,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_type_1(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get full representation of issue type by id

        Path: /api/2/issuetype/{id}
        Method: GET
        """
        path = f"/api/2/issuetype/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_issue_type(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update specified issue type from JSON representation

        Path: /api/2/issuetype/{id}
        Method: PUT
        """
        path = f"/api/2/issuetype/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_issue_type_1(
        self,
        id_: str,
        alternative_issue_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete specified issue type and migrate associated issues

        Path: /api/2/issuetype/{id}
        Method: DELETE
        """
        path = f"/api/2/issuetype/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_alternative_issue_types(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get list of alternative issue types for given id

        Path: /api/2/issuetype/{id}/alternatives
        Method: GET
        """
        path = f"/api/2/issuetype/{id_}/alternatives"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_avatar_from_temporary(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Convert temporary avatar into a real avatar

        Path: /api/2/issuetype/{id}/avatar
        Method: POST
        """
        path = f"/api/2/issuetype/{id_}/avatar"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_store_temporary_avatar_using_multi_part(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create temporary avatar using multipart for issue type

        Path: /api/2/issuetype/{id}/avatar/temporary
        Method: POST
        """
        path = f"/api/2/issuetype/{id_}/avatar/temporary"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_property_keys(
        self,
        issue_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all properties keys for issue type

        Path: /api/2/issuetype/{issueTypeId}/properties
        Method: GET
        """
        path = f"/api/2/issuetype/{issue_type_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_property_4(
        self,
        property_key: str,
        issue_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get value of specified issue type's property

        Path: /api/2/issuetype/{issueTypeId}/properties/{propertyKey}
        Method: GET
        """
        path = f"/api/2/issuetype/{issue_type_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_property_3(
        self,
        property_key: str,
        issue_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update specified issue type's property

        Path: /api/2/issuetype/{issueTypeId}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/api/2/issuetype/{issue_type_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_property_4(
        self,
        property_key: str,
        issue_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete specified issue type's property

        Path: /api/2/issuetype/{issueTypeId}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/api/2/issuetype/{issue_type_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_issue_type_schemes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get list of all issue type schemes visible to user

        Path: /api/2/issuetypescheme
        Method: GET
        """
        path = "/api/2/issuetypescheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_issue_type_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create an issue type scheme from JSON representation

        Path: /api/2/issuetypescheme
        Method: POST
        """
        path = "/api/2/issuetypescheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_type_scheme(
        self,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get full representation of issue type scheme by id

        Path: /api/2/issuetypescheme/{schemeId}
        Method: GET
        """
        path = f"/api/2/issuetypescheme/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_issue_type_scheme(
        self,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update specified issue type scheme from JSON representation

        Path: /api/2/issuetypescheme/{schemeId}
        Method: PUT
        """
        path = f"/api/2/issuetypescheme/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_issue_type_scheme(
        self,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete specified issue type scheme

        Path: /api/2/issuetypescheme/{schemeId}
        Method: DELETE
        """
        path = f"/api/2/issuetypescheme/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_associated_projects(
        self,
        scheme_id: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all of the associated projects for specified scheme

        Path: /api/2/issuetypescheme/{schemeId}/associations
        Method: GET
        """
        path = f"/api/2/issuetypescheme/{scheme_id}/associations"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_project_associations_for_scheme(
        self,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set project associations for scheme

        Path: /api/2/issuetypescheme/{schemeId}/associations
        Method: PUT
        """
        path = f"/api/2/issuetypescheme/{scheme_id}/associations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_add_project_associations_to_scheme(
        self,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add project associations to scheme

        Path: /api/2/issuetypescheme/{schemeId}/associations
        Method: POST
        """
        path = f"/api/2/issuetypescheme/{scheme_id}/associations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_all_project_associations(
        self,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove all project associations for specified scheme

        Path: /api/2/issuetypescheme/{schemeId}/associations
        Method: DELETE
        """
        path = f"/api/2/issuetypescheme/{scheme_id}/associations"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_project_association(
        self,
        proj_id_or_key: str,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove given project association for specified scheme

        Path: /api/2/issuetypescheme/{schemeId}/associations/{projIdOrKey}
        Method: DELETE
        """
        path = f"/api/2/issuetypescheme/{scheme_id}/associations/{proj_id_or_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_auto_complete(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get auto complete data for JQL searches

        Path: /api/2/jql/autocompletedata
        Method: GET
        """
        path = "/api/2/jql/autocompletedata"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_field_auto_complete_for_query_string(
        self,
        predicate_value: str | None = None,
        predicate_name: str | None = None,
        field_name: str | None = None,
        field_value: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get auto complete suggestions for JQL search

        Path: /api/2/jql/autocompletedata/suggestions
        Method: GET
        """
        path = "/api/2/jql/autocompletedata/suggestions"
        params = {
            "predicateValue": predicate_value,
            "predicateName": predicate_name,
            "fieldName": field_name,
            "fieldValue": field_value,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_validate(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Validate a Jira license

        Path: /api/2/licenseValidator
        Method: POST
        """
        path = "/api/2/licenseValidator"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_is_app_monitoring_enabled(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get App Monitoring status

        Path: /api/2/monitoring/app
        Method: GET
        """
        path = "/api/2/monitoring/app"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_app_monitoring_enabled(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update App Monitoring status

        Path: /api/2/monitoring/app
        Method: POST
        """
        path = "/api/2/monitoring/app"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_is_ipd_monitoring_enabled(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get if IPD Monitoring is enabled

        Path: /api/2/monitoring/ipd
        Method: GET
        """
        path = "/api/2/monitoring/ipd"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_app_monitoring_enabled_1(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update IPD Monitoring status

        Path: /api/2/monitoring/ipd
        Method: POST
        """
        path = "/api/2/monitoring/ipd"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_are_metrics_exposed(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Check if JMX metrics are being exposed

        Path: /api/2/monitoring/jmx/areMetricsExposed
        Method: GET
        """
        path = "/api/2/monitoring/jmx/areMetricsExposed"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_available_metrics(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get the available JMX metrics

        Path: /api/2/monitoring/jmx/getAvailableMetrics
        Method: GET
        """
        path = "/api/2/monitoring/jmx/getAvailableMetrics"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_start(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Start exposing JMX metrics

        Path: /api/2/monitoring/jmx/startExposing
        Method: POST
        """
        path = "/api/2/monitoring/jmx/startExposing"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_stop(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Stop exposing JMX metrics

        Path: /api/2/monitoring/jmx/stopExposing
        Method: POST
        """
        path = "/api/2/monitoring/jmx/stopExposing"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_permissions(
        self,
        issue_id: str | None = None,
        project_key: str | None = None,
        issue_key: str | None = None,
        project_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permissions for the logged in user

        Path: /api/2/mypermissions
        Method: GET
        """
        path = "/api/2/mypermissions"
        params = {
            "issueId": issue_id,
            "projectKey": project_key,
            "issueKey": issue_key,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_preference(
        self,
        key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user preference by key

        Path: /api/2/mypreferences
        Method: GET
        """
        path = "/api/2/mypreferences"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_preference(
        self,
        key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update user preference

        Path: /api/2/mypreferences
        Method: PUT
        """
        path = "/api/2/mypreferences"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_preference(
        self,
        key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete user preference

        Path: /api/2/mypreferences
        Method: DELETE
        """
        path = "/api/2/mypreferences"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_user(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get currently logged user

        Path: /api/2/myself
        Method: GET
        """
        path = "/api/2/myself"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_user(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update currently logged user

        Path: /api/2/myself
        Method: PUT
        """
        path = "/api/2/myself"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_change_my_password(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update caller password

        Path: /api/2/myself/password
        Method: PUT
        """
        path = "/api/2/myself/password"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_notification_schemes(
        self,
        expand: str | None = None,
        max_results: int | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get paginated notification schemes

        Path: /api/2/notificationscheme
        Method: GET
        """
        path = "/api/2/notificationscheme"
        params = {
            "expand": expand,
            "maxResults": max_results,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_notification_scheme(
        self,
        id_: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get full notification scheme details

        Path: /api/2/notificationscheme/{id}
        Method: GET
        """
        path = f"/api/2/notificationscheme/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_password_policy(
        self,
        has_old_password: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get current password policy requirements

        Path: /api/2/password/policy
        Method: GET
        """
        path = "/api/2/password/policy"
        params = {
            "hasOldPassword": has_old_password,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_policy_check_create_user(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get reasons for password policy disallowance on user creation

        Path: /api/2/password/policy/createUser
        Method: POST
        """
        path = "/api/2/password/policy/createUser"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_policy_check_update_user(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get reasons for password policy disallowance on user password update

        Path: /api/2/password/policy/updateUser
        Method: POST
        """
        path = "/api/2/password/policy/updateUser"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_permissions(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all permissions present in Jira instance

        Path: /api/2/permissions
        Method: GET
        """
        path = "/api/2/permissions"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_permission_schemes(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all permission schemes

        Path: /api/2/permissionscheme
        Method: GET
        """
        path = "/api/2/permissionscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_permission_scheme(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a new permission scheme

        Path: /api/2/permissionscheme
        Method: POST
        """
        path = "/api/2/permissionscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_scheme_attribute(
        self,
        permission_scheme_id: int,
        attribute_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get scheme attribute by key

        Path: /api/2/permissionscheme/{permissionSchemeId}/attribute/{attributeKey}
        Method: GET
        """
        path = (
            f"/api/2/permissionscheme/{permission_scheme_id}/attribute/{attribute_key}"
        )
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_scheme_attribute(
        self,
        permission_scheme_id: int,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update or insert a scheme attribute

        Path: /api/2/permissionscheme/{permissionSchemeId}/attribute/{key}
        Method: PUT
        """
        path = f"/api/2/permissionscheme/{permission_scheme_id}/attribute/{key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_permission_scheme(
        self,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a permission scheme by ID

        Path: /api/2/permissionscheme/{schemeId}
        Method: GET
        """
        path = f"/api/2/permissionscheme/{scheme_id}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_permission_scheme(
        self,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a permission scheme

        Path: /api/2/permissionscheme/{schemeId}
        Method: PUT
        """
        path = f"/api/2/permissionscheme/{scheme_id}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_permission_scheme(
        self,
        scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a permission scheme by ID

        Path: /api/2/permissionscheme/{schemeId}
        Method: DELETE
        """
        path = f"/api/2/permissionscheme/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_permission_scheme_grants(
        self,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all permission grants of a scheme

        Path: /api/2/permissionscheme/{schemeId}/permission
        Method: GET
        """
        path = f"/api/2/permissionscheme/{scheme_id}/permission"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_permission_grant(
        self,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a permission grant in a scheme

        Path: /api/2/permissionscheme/{schemeId}/permission
        Method: POST
        """
        path = f"/api/2/permissionscheme/{scheme_id}/permission"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_permission_scheme_grant(
        self,
        permission_id: int,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a permission grant by ID

        Path: /api/2/permissionscheme/{schemeId}/permission/{permissionId}
        Method: GET
        """
        path = f"/api/2/permissionscheme/{scheme_id}/permission/{permission_id}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_permission_scheme_entity(
        self,
        permission_id: int,
        scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a permission grant from a scheme

        Path: /api/2/permissionscheme/{schemeId}/permission/{permissionId}
        Method: DELETE
        """
        path = f"/api/2/permissionscheme/{scheme_id}/permission/{permission_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_priorities(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all issue priorities

        Path: /api/2/priority
        Method: GET
        """
        path = "/api/2/priority"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_priorities_1(
        self,
        max_results: int | None = None,
        query: str | None = None,
        project_ids: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get paginated issue priorities

        Path: /api/2/priority/page
        Method: GET
        """
        path = "/api/2/priority/page"
        params = {
            "maxResults": max_results,
            "query": query,
            "projectIds": project_ids,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_priority(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get an issue priority by ID

        Path: /api/2/priority/{id}
        Method: GET
        """
        path = f"/api/2/priority/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_priority_schemes(
        self,
        max_results: int | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all priority schemes

        Path: /api/2/priorityschemes
        Method: GET
        """
        path = "/api/2/priorityschemes"
        params = {
            "maxResults": max_results,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_priority_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create new priority scheme

        Path: /api/2/priorityschemes
        Method: POST
        """
        path = "/api/2/priorityschemes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_priority_scheme(
        self,
        scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a priority scheme by ID

        Path: /api/2/priorityschemes/{schemeId}
        Method: GET
        """
        path = f"/api/2/priorityschemes/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_priority_scheme(
        self,
        scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a priority scheme

        Path: /api/2/priorityschemes/{schemeId}
        Method: PUT
        """
        path = f"/api/2/priorityschemes/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_priority_scheme(
        self,
        scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a priority scheme

        Path: /api/2/priorityschemes/{schemeId}
        Method: DELETE
        """
        path = f"/api/2/priorityschemes/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_projects(
        self,
        include_archived: bool | None = None,
        expand: str | None = None,
        recent: int | None = None,
        browse_archive: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all visible projects

        Path: /api/2/project
        Method: GET
        """
        path = "/api/2/project"
        params = {
            "includeArchived": include_archived,
            "expand": expand,
            "recent": recent,
            "browseArchive": browse_archive,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_project(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a new project

        Path: /api/2/project
        Method: POST
        """
        path = "/api/2/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_project_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all project types

        Path: /api/2/project/type
        Method: GET
        """
        path = "/api/2/project/type"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_type_by_key(
        self,
        project_type_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project type by key

        Path: /api/2/project/type/{projectTypeKey}
        Method: GET
        """
        path = f"/api/2/project/type/{project_type_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_accessible_project_type_by_key(
        self,
        project_type_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project type by key

        Path: /api/2/project/type/{projectTypeKey}/accessible
        Method: GET
        """
        path = f"/api/2/project/type/{project_type_key}/accessible"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project(
        self,
        project_id_or_key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a project by ID or key

        Path: /api/2/project/{projectIdOrKey}
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_project(
        self,
        project_id_or_key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a project

        Path: /api/2/project/{projectIdOrKey}
        Method: PUT
        """
        path = f"/api/2/project/{project_id_or_key}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_project(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a project

        Path: /api/2/project/{projectIdOrKey}
        Method: DELETE
        """
        path = f"/api/2/project/{project_id_or_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_archive_project(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Archive a project

        Path: /api/2/project/{projectIdOrKey}/archive
        Method: PUT
        """
        path = f"/api/2/project/{project_id_or_key}/archive"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_update_project_avatar(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update project avatar

        Path: /api/2/project/{projectIdOrKey}/avatar
        Method: PUT
        """
        path = f"/api/2/project/{project_id_or_key}/avatar"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_create_avatar_from_temporary_1(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create avatar from temporary

        Path: /api/2/project/{projectIdOrKey}/avatar
        Method: POST
        """
        path = f"/api/2/project/{project_id_or_key}/avatar"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_store_temporary_avatar_using_multi_part_1(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Store temporary avatar using multipart

        Path: /api/2/project/{projectIdOrKey}/avatar/temporary
        Method: POST
        """
        path = f"/api/2/project/{project_id_or_key}/avatar/temporary"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_avatar(
        self,
        project_id_or_key: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete an avatar

        Path: /api/2/project/{projectIdOrKey}/avatar/{id}
        Method: DELETE
        """
        path = f"/api/2/project/{project_id_or_key}/avatar/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_avatars(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all avatars for a project

        Path: /api/2/project/{projectIdOrKey}/avatars
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/avatars"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_components(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project components

        Path: /api/2/project/{projectIdOrKey}/components
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/components"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_properties_keys_3(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get keys of all properties for project

        Path: /api/2/project/{projectIdOrKey}/properties
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_property_5(
        self,
        property_key: str,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get value of property from project

        Path: /api/2/project/{projectIdOrKey}/properties/{propertyKey}
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_property_4(
        self,
        property_key: str,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set value of specified project's property

        Path: /api/2/project/{projectIdOrKey}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/api/2/project/{project_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_property_5(
        self,
        property_key: str,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete property from project

        Path: /api/2/project/{projectIdOrKey}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/api/2/project/{project_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_restore_project(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Restore an archived project

        Path: /api/2/project/{projectIdOrKey}/restore
        Method: PUT
        """
        path = f"/api/2/project/{project_id_or_key}/restore"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_roles(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all roles in project

        Path: /api/2/project/{projectIdOrKey}/role
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/role"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_role(
        self,
        project_id_or_key: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get details for a project role

        Path: /api/2/project/{projectIdOrKey}/role/{id}
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_actors(
        self,
        project_id_or_key: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update project role with actors

        Path: /api/2/project/{projectIdOrKey}/role/{id}
        Method: PUT
        """
        path = f"/api/2/project/{project_id_or_key}/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_add_actor_users(
        self,
        project_id_or_key: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add actor to project role

        Path: /api/2/project/{projectIdOrKey}/role/{id}
        Method: POST
        """
        path = f"/api/2/project/{project_id_or_key}/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_actor(
        self,
        project_id_or_key: str,
        id_: int,
        user: str | None = None,
        group: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete actors from project role

        Path: /api/2/project/{projectIdOrKey}/role/{id}
        Method: DELETE
        """
        path = f"/api/2/project/{project_id_or_key}/role/{id_}"
        params = {
            "user": user,
            "group": group,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_statuses(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issue types with statuses for a project

        Path: /api/2/project/{projectIdOrKey}/statuses
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/statuses"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_project_type(
        self,
        project_id_or_key: str,
        new_project_type_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update project type

        Path: /api/2/project/{projectIdOrKey}/type/{newProjectTypeKey}
        Method: PUT
        """
        path = f"/api/2/project/{project_id_or_key}/type/{new_project_type_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_versions_paginated(
        self,
        project_id_or_key: str,
        expand: str | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get paginated project versions

        Path: /api/2/project/{projectIdOrKey}/version
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/version"
        params = {
            "expand": expand,
            "maxResults": max_results,
            "orderBy": order_by,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_versions(
        self,
        project_id_or_key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project versions

        Path: /api/2/project/{projectIdOrKey}/versions
        Method: GET
        """
        path = f"/api/2/project/{project_id_or_key}/versions"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_security_scheme_1(
        self,
        project_key_or_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue security scheme for project

        Path: /api/2/project/{projectKeyOrId}/issuesecuritylevelscheme
        Method: GET
        """
        path = f"/api/2/project/{project_key_or_id}/issuesecuritylevelscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_notification_scheme_1(
        self,
        project_key_or_id: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get notification scheme associated with the project

        Path: /api/2/project/{projectKeyOrId}/notificationscheme
        Method: GET
        """
        path = f"/api/2/project/{project_key_or_id}/notificationscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_assigned_permission_scheme(
        self,
        project_key_or_id: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get assigned permission scheme

        Path: /api/2/project/{projectKeyOrId}/permissionscheme
        Method: GET
        """
        path = f"/api/2/project/{project_key_or_id}/permissionscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_assign_permission_scheme(
        self,
        project_key_or_id: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign permission scheme to project

        Path: /api/2/project/{projectKeyOrId}/permissionscheme
        Method: PUT
        """
        path = f"/api/2/project/{project_key_or_id}/permissionscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_assigned_priority_scheme(
        self,
        project_key_or_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get assigned priority scheme

        Path: /api/2/project/{projectKeyOrId}/priorityscheme
        Method: GET
        """
        path = f"/api/2/project/{project_key_or_id}/priorityscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_assign_priority_scheme(
        self,
        project_key_or_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign project with priority scheme

        Path: /api/2/project/{projectKeyOrId}/priorityscheme
        Method: PUT
        """
        path = f"/api/2/project/{project_key_or_id}/priorityscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_unassign_priority_scheme(
        self,
        scheme_id: int,
        project_key_or_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Unassign project from priority scheme

        Path: /api/2/project/{projectKeyOrId}/priorityscheme/{schemeId}
        Method: DELETE
        """
        path = f"/api/2/project/{project_key_or_id}/priorityscheme/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_security_levels_for_project(
        self,
        project_key_or_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all security levels for project

        Path: /api/2/project/{projectKeyOrId}/securitylevel
        Method: GET
        """
        path = f"/api/2/project/{project_key_or_id}/securitylevel"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_workflow_scheme_for_project(
        self,
        project_key_or_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow scheme for project

        Path: /api/2/project/{projectKeyOrId}/workflowscheme
        Method: GET
        """
        path = f"/api/2/project/{project_key_or_id}/workflowscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_project_categories(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all project categories

        Path: /api/2/projectCategory
        Method: GET
        """
        path = "/api/2/projectCategory"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_project_category(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create project category

        Path: /api/2/projectCategory
        Method: POST
        """
        path = "/api/2/projectCategory"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_category_by_id(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project category by ID

        Path: /api/2/projectCategory/{id}
        Method: GET
        """
        path = f"/api/2/projectCategory/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_project_category(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update project category

        Path: /api/2/projectCategory/{id}
        Method: PUT
        """
        path = f"/api/2/projectCategory/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_project_category(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete project category

        Path: /api/2/projectCategory/{id}
        Method: DELETE
        """
        path = f"/api/2/projectCategory/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_search_for_projects(
        self,
        max_results: int | None = None,
        query: str | None = None,
        allow_empty_query: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get projects matching query

        Path: /api/2/projects/picker
        Method: GET
        """
        path = "/api/2/projects/picker"
        params = {
            "maxResults": max_results,
            "query": query,
            "allowEmptyQuery": allow_empty_query,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_1(
        self,
        key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project key validation

        Path: /api/2/projectvalidate/key
        Method: GET
        """
        path = "/api/2/projectvalidate/key"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_reindex_info(
        self,
        task_id: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get reindex information

        Path: /api/2/reindex
        Method: GET
        """
        path = "/api/2/reindex"
        params = {
            "taskId": task_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_reindex(
        self,
        index_change_history: bool | None = None,
        type_: str | None = None,
        index_worklogs: bool | None = None,
        index_comments: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Start a reindex operation

        Path: /api/2/reindex
        Method: POST
        """
        path = "/api/2/reindex"
        params = {
            "indexChangeHistory": index_change_history,
            "type": type_,
            "indexWorklogs": index_worklogs,
            "indexComments": index_comments,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_reindex_issues(
        self,
        issue_id: list[Any] | None = None,
        index_change_history: bool | None = None,
        index_worklogs: bool | None = None,
        index_comments: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reindex individual issues

        Path: /api/2/reindex/issue
        Method: POST
        """
        path = "/api/2/reindex/issue"
        params = {
            "issueId": issue_id,
            "indexChangeHistory": index_change_history,
            "indexWorklogs": index_worklogs,
            "indexComments": index_comments,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_reindex_progress(
        self,
        task_id: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get reindex progress

        Path: /api/2/reindex/progress
        Method: GET
        """
        path = "/api/2/reindex/progress"
        params = {
            "taskId": task_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_process_requests(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Execute pending reindex requests

        Path: /api/2/reindex/request
        Method: POST
        """
        path = "/api/2/reindex/request"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_progress_bulk(
        self,
        request_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get progress of multiple reindex requests

        Path: /api/2/reindex/request/bulk
        Method: GET
        """
        path = "/api/2/reindex/request/bulk"
        params = {
            "requestId": request_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_progress(
        self,
        request_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get progress of a single reindex request

        Path: /api/2/reindex/request/{requestId}
        Method: GET
        """
        path = f"/api/2/reindex/request/{request_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_resolutions(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all resolutions

        Path: /api/2/resolution
        Method: GET
        """
        path = "/api/2/resolution"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_paginated_resolutions(
        self,
        max_results: int | None = None,
        query: str | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get paginated filtered resolutions

        Path: /api/2/resolution/page
        Method: GET
        """
        path = "/api/2/resolution/page"
        params = {
            "maxResults": max_results,
            "query": query,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_resolution(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a resolution by ID

        Path: /api/2/resolution/{id}
        Method: GET
        """
        path = f"/api/2/resolution/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_roles_1(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all project roles

        Path: /api/2/role
        Method: GET
        """
        path = "/api/2/role"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_project_role(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a new project role

        Path: /api/2/role
        Method: POST
        """
        path = "/api/2/role"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_roles_by_id(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a specific project role

        Path: /api/2/role/{id}
        Method: GET
        """
        path = f"/api/2/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_fully_update_project_role(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Fully updates a role's name and description

        Path: /api/2/role/{id}
        Method: PUT
        """
        path = f"/api/2/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_partial_update_project_role(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Partially updates a role's name or description

        Path: /api/2/role/{id}
        Method: POST
        """
        path = f"/api/2/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_project_role(
        self,
        id_: int,
        swap: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Deletes a role

        Path: /api/2/role/{id}
        Method: DELETE
        """
        path = f"/api/2/role/{id_}"
        params = {
            "swap": swap,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_project_role_actors_for_role(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get default actors for a role

        Path: /api/2/role/{id}/actors
        Method: GET
        """
        path = f"/api/2/role/{id_}/actors"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_project_role_actors_to_role(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Adds default actors to a role

        Path: /api/2/role/{id}/actors
        Method: POST
        """
        path = f"/api/2/role/{id_}/actors"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_project_role_actors_from_role(
        self,
        id_: int,
        user: str | None = None,
        group: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Removes default actor from a role

        Path: /api/2/role/{id}/actors
        Method: DELETE
        """
        path = f"/api/2/role/{id_}/actors"
        params = {
            "user": user,
            "group": group,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_screens(
        self,
        search: str | None = None,
        expand: str | None = None,
        max_results: str | None = None,
        start_at: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get available field screens

        Path: /api/2/screens
        Method: GET
        """
        path = "/api/2/screens"
        params = {
            "search": search,
            "expand": expand,
            "maxResults": max_results,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_field_to_default_screen(
        self,
        field_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add field to default screen

        Path: /api/2/screens/addToDefault/{fieldId}
        Method: POST
        """
        path = f"/api/2/screens/addToDefault/{field_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_fields_to_add(
        self,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get available fields for screen

        Path: /api/2/screens/{screenId}/availableFields
        Method: GET
        """
        path = f"/api/2/screens/{screen_id}/availableFields"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_tabs(
        self,
        screen_id: int,
        project_key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all tabs for a screen

        Path: /api/2/screens/{screenId}/tabs
        Method: GET
        """
        path = f"/api/2/screens/{screen_id}/tabs"
        params = {
            "projectKey": project_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_tab(
        self,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create tab for a screen

        Path: /api/2/screens/{screenId}/tabs
        Method: POST
        """
        path = f"/api/2/screens/{screen_id}/tabs"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_rename_tab(
        self,
        tab_id: int,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Rename a tab on a screen

        Path: /api/2/screens/{screenId}/tabs/{tabId}
        Method: PUT
        """
        path = f"/api/2/screens/{screen_id}/tabs/{tab_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_tab(
        self,
        tab_id: int,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a tab from a screen

        Path: /api/2/screens/{screenId}/tabs/{tabId}
        Method: DELETE
        """
        path = f"/api/2/screens/{screen_id}/tabs/{tab_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_fields(
        self,
        tab_id: int,
        screen_id: int,
        project_key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all fields for a tab

        Path: /api/2/screens/{screenId}/tabs/{tabId}/fields
        Method: GET
        """
        path = f"/api/2/screens/{screen_id}/tabs/{tab_id}/fields"
        params = {
            "projectKey": project_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_add_field(
        self,
        tab_id: int,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add field to a tab

        Path: /api/2/screens/{screenId}/tabs/{tabId}/fields
        Method: POST
        """
        path = f"/api/2/screens/{screen_id}/tabs/{tab_id}/fields"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_field(
        self,
        tab_id: int,
        screen_id: int,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove field from tab

        Path: /api/2/screens/{screenId}/tabs/{tabId}/fields/{id}
        Method: DELETE
        """
        path = f"/api/2/screens/{screen_id}/tabs/{tab_id}/fields/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_move_field(
        self,
        tab_id: int,
        screen_id: int,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move field on a tab

        Path: /api/2/screens/{screenId}/tabs/{tabId}/fields/{id}/move
        Method: POST
        """
        path = f"/api/2/screens/{screen_id}/tabs/{tab_id}/fields/{id_}/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_update_show_when_empty_indicator(
        self,
        tab_id: int,
        screen_id: int,
        new_value: bool,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update 'showWhenEmptyIndicator' for a field

        Path: /api/2/screens/{screenId}/tabs/{tabId}/fields/{id}/updateShowWhenEmptyIndicator/{newValue}
        Method: PUT
        """
        path = f"/api/2/screens/{screen_id}/tabs/{tab_id}/fields/{id_}/updateShowWhenEmptyIndicator/{new_value}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_move_tab(
        self,
        tab_id: int,
        screen_id: int,
        pos: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move tab position

        Path: /api/2/screens/{screenId}/tabs/{tabId}/move/{pos}
        Method: POST
        """
        path = f"/api/2/screens/{screen_id}/tabs/{tab_id}/move/{pos}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_search_1(
        self,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issues using JQL

        Path: /api/2/search
        Method: GET
        """
        path = "/api/2/search"
        params = {
            "expand": expand,
            "jql": jql,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_search_using_search_request(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Perform search with JQL

        Path: /api/2/search
        Method: POST
        """
        path = "/api/2/search"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_error(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """No description provided.

        Path: /api/2/search/error/lookup
        Method: GET
        """
        path = "/api/2/search/error/lookup"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_max_aggregation_buckets(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get maximum aggregation buckets

        Path: /api/2/searchLimits/maxAggregationBuckets
        Method: GET
        """
        path = "/api/2/searchLimits/maxAggregationBuckets"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_max_result_window(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get maximum result window

        Path: /api/2/searchLimits/maxResultWindow
        Method: GET
        """
        path = "/api/2/searchLimits/maxResultWindow"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issuesecuritylevel(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a security level by ID

        Path: /api/2/securitylevel/{id}
        Method: GET
        """
        path = f"/api/2/securitylevel/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_server_info(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get general information about the current Jira server

        Path: /api/2/serverInfo
        Method: GET
        """
        path = "/api/2/serverInfo"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_base_url(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update base URL for Jira instance

        Path: /api/2/settings/baseUrl
        Method: PUT
        """
        path = "/api/2/settings/baseUrl"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_navigator_default_columns(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get default system columns for issue navigator

        Path: /api/2/settings/columns
        Method: GET
        """
        path = "/api/2/settings/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_issue_navigator_default_columns_form(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set default system columns for issue navigator using form

        Path: /api/2/settings/columns
        Method: PUT
        """
        path = "/api/2/settings/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_get_statuses(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all statuses

        Path: /api/2/status
        Method: GET
        """
        path = "/api/2/status"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_paginated_statuses(
        self,
        issue_type_ids: list[Any] | None = None,
        max_results: int | None = None,
        query: str | None = None,
        project_ids: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get paginated filtered statuses

        Path: /api/2/status/page
        Method: GET
        """
        path = "/api/2/status/page"
        params = {
            "issueTypeIds": issue_type_ids,
            "maxResults": max_results,
            "query": query,
            "projectIds": project_ids,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_status(
        self,
        id_or_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get status by ID or name

        Path: /api/2/status/{idOrName}
        Method: GET
        """
        path = f"/api/2/status/{id_or_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_status_categories(
        self,
        request: str | None = None,
        uri_info: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all status categories

        Path: /api/2/statuscategory
        Method: GET
        """
        path = "/api/2/statuscategory"
        params = {
            "request": request,
            "uriInfo": uri_info,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_status_category(
        self,
        id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get status category by ID or key

        Path: /api/2/statuscategory/{idOrKey}
        Method: GET
        """
        path = f"/api/2/statuscategory/{id_or_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_terminology_entries(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all defined names for 'epic' and 'sprint'

        Path: /api/2/terminology/entries
        Method: GET
        """
        path = "/api/2/terminology/entries"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_terminology_entries(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update epic/sprint names from original to new

        Path: /api/2/terminology/entries
        Method: POST
        """
        path = "/api/2/terminology/entries"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_terminology_entry(
        self,
        original_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get epic or sprint name by original name

        Path: /api/2/terminology/entries/{originalName}
        Method: GET
        """
        path = f"/api/2/terminology/entries/{original_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_avatars(
        self,
        type_: str,
        owning_object_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all avatars for a type and owner

        Path: /api/2/universal_avatar/type/{type}/owner/{owningObjectId}
        Method: GET
        """
        path = f"/api/2/universal_avatar/type/{type_}/owner/{owning_object_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_avatar_from_temporary_2(
        self,
        type_: str,
        owning_object_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create avatar from temporary

        Path: /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/avatar
        Method: POST
        """
        path = f"/api/2/universal_avatar/type/{type_}/owner/{owning_object_id}/avatar"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_avatar_1(
        self,
        id_: int,
        type_: str,
        owning_object_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete avatar by ID

        Path: /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}
        Method: DELETE
        """
        path = f"/api/2/universal_avatar/type/{type_}/owner/{owning_object_id}/avatar/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_store_temporary_avatar_using_multi_part_2(
        self,
        type_: str,
        owning_object_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create temporary avatar using multipart upload

        Path: /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/temp
        Method: POST
        """
        path = f"/api/2/universal_avatar/type/{type_}/owner/{owning_object_id}/temp"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_upgrade_result(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get result of the last upgrade task

        Path: /api/2/upgrade
        Method: GET
        """
        path = "/api/2/upgrade"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_run_upgrades_now(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Run pending upgrade tasks

        Path: /api/2/upgrade
        Method: POST
        """
        path = "/api/2/upgrade"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_user_1(
        self,
        include_deleted: bool | None = None,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user by username or key

        Path: /api/2/user
        Method: GET
        """
        path = "/api/2/user"
        params = {
            "includeDeleted": include_deleted,
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_user_1(
        self,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update user details

        Path: /api/2/user
        Method: PUT
        """
        path = "/api/2/user"
        params = {
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_create_user(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create new user

        Path: /api/2/user
        Method: POST
        """
        path = "/api/2/user"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_user(
        self,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete user

        Path: /api/2/user
        Method: DELETE
        """
        path = "/api/2/user"
        params = {
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_a11y_personal_settings(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get available accessibility personal settings

        Path: /api/2/user/a11y/personal-settings
        Method: GET
        """
        path = "/api/2/user/a11y/personal-settings"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_validate_user_anonymization(
        self,
        expand: str | None = None,
        user_key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get validation for user anonymization

        Path: /api/2/user/anonymization
        Method: GET
        """
        path = "/api/2/user/anonymization"
        params = {
            "expand": expand,
            "userKey": user_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_schedule_user_anonymization(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Schedule user anonymization

        Path: /api/2/user/anonymization
        Method: POST
        """
        path = "/api/2/user/anonymization"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_progress_1(
        self,
        task_id: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user anonymization progress

        Path: /api/2/user/anonymization/progress
        Method: GET
        """
        path = "/api/2/user/anonymization/progress"
        params = {
            "taskId": task_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_validate_user_anonymization_rerun(
        self,
        expand: str | None = None,
        old_user_key: str | None = None,
        old_user_name: str | None = None,
        user_key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get validation for user anonymization rerun

        Path: /api/2/user/anonymization/rerun
        Method: GET
        """
        path = "/api/2/user/anonymization/rerun"
        params = {
            "expand": expand,
            "oldUserKey": old_user_key,
            "oldUserName": old_user_name,
            "userKey": user_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_schedule_user_anonymization_rerun(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Schedule user anonymization rerun

        Path: /api/2/user/anonymization/rerun
        Method: POST
        """
        path = "/api/2/user/anonymization/rerun"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_unlock_anonymization(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Delete stale user anonymization task

        Path: /api/2/user/anonymization/unlock
        Method: DELETE
        """
        path = "/api/2/user/anonymization/unlock"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_add_user_to_application_1(
        self,
        application_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add user to application

        Path: /api/2/user/application
        Method: POST
        """
        path = "/api/2/user/application"
        params = {
            "applicationKey": application_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_remove_user_from_application_1(
        self,
        application_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove user from application

        Path: /api/2/user/application
        Method: DELETE
        """
        path = "/api/2/user/application"
        params = {
            "applicationKey": application_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_find_bulk_assignable_users(
        self,
        max_results: int | None = None,
        project_keys: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find bulk assignable users

        Path: /api/2/user/assignable/multiProjectSearch
        Method: GET
        """
        path = "/api/2/user/assignable/multiProjectSearch"
        params = {
            "maxResults": max_results,
            "projectKeys": project_keys,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_find_assignable_users_1(
        self,
        issue_key: str | None = None,
        max_results: int | None = None,
        project: str | None = None,
        action_descriptor_id: int | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find assignable users by username

        Path: /api/2/user/assignable/search
        Method: GET
        """
        path = "/api/2/user/assignable/search"
        params = {
            "issueKey": issue_key,
            "maxResults": max_results,
            "project": project,
            "actionDescriptorId": action_descriptor_id,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_user_avatar_1(
        self,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update user avatar

        Path: /api/2/user/avatar
        Method: PUT
        """
        path = "/api/2/user/avatar"
        params = {
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_create_avatar_from_temporary_3(
        self,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create avatar from temporary

        Path: /api/2/user/avatar
        Method: POST
        """
        path = "/api/2/user/avatar"
        params = {
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_store_temporary_avatar_using_multi_part_3(
        self,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Store temporary avatar using multipart

        Path: /api/2/user/avatar/temporary
        Method: POST
        """
        path = "/api/2/user/avatar/temporary"
        params = {
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_avatar_2(
        self,
        id_: int,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete avatar

        Path: /api/2/user/avatar/{id}
        Method: DELETE
        """
        path = f"/api/2/user/avatar/{id_}"
        params = {
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_avatars_1(
        self,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all avatars for user

        Path: /api/2/user/avatars
        Method: GET
        """
        path = "/api/2/user/avatars"
        params = {
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_default_columns(
        self,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get default columns for user

        Path: /api/2/user/columns
        Method: GET
        """
        path = "/api/2/user/columns"
        params = {
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_columns_url_encoded(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set default columns for user

        Path: /api/2/user/columns
        Method: PUT
        """
        path = "/api/2/user/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_reset_columns(
        self,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset default columns to system default

        Path: /api/2/user/columns
        Method: DELETE
        """
        path = "/api/2/user/columns"
        params = {
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_duplicated_users_count(
        self,
        flush: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get duplicated users count

        Path: /api/2/user/duplicated/count
        Method: GET
        """
        path = "/api/2/user/duplicated/count"
        params = {
            "flush": flush,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_duplicated_users_mapping(
        self,
        flush: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get duplicated users mapping

        Path: /api/2/user/duplicated/list
        Method: GET
        """
        path = "/api/2/user/duplicated/list"
        params = {
            "flush": flush,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_user_list(
        self,
        cursor: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """List all users

        Path: /api/2/user/list
        Method: GET
        """
        path = "/api/2/user/list"
        params = {
            "cursor": cursor,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_change_user_password(
        self,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update user password

        Path: /api/2/user/password
        Method: PUT
        """
        path = "/api/2/user/password"
        params = {
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_find_users_with_all_permissions(
        self,
        project_key: str | None = None,
        issue_key: str | None = None,
        max_results: int | None = None,
        permissions: str | None = None,
        start_at: int | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users with all specified permissions

        Path: /api/2/user/permission/search
        Method: GET
        """
        path = "/api/2/user/permission/search"
        params = {
            "projectKey": project_key,
            "issueKey": issue_key,
            "maxResults": max_results,
            "permissions": permissions,
            "startAt": start_at,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_find_users_for_picker(
        self,
        max_results: int | None = None,
        query: str | None = None,
        exclude: list[Any] | None = None,
        show_avatar: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users for picker by query

        Path: /api/2/user/picker
        Method: GET
        """
        path = "/api/2/user/picker"
        params = {
            "maxResults": max_results,
            "query": query,
            "exclude": exclude,
            "showAvatar": show_avatar,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_properties_keys_4(
        self,
        user_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get keys of all properties for a user

        Path: /api/2/user/properties
        Method: GET
        """
        path = "/api/2/user/properties"
        params = {
            "userKey": user_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_property_6(
        self,
        property_key: str,
        user_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the value of a specified user's property

        Path: /api/2/user/properties/{propertyKey}
        Method: GET
        """
        path = f"/api/2/user/properties/{property_key}"
        params = {
            "userKey": user_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_property_5(
        self,
        property_key: str,
        user_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set the value of a specified user's property

        Path: /api/2/user/properties/{propertyKey}
        Method: PUT
        """
        path = f"/api/2/user/properties/{property_key}"
        params = {
            "userKey": user_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_property_6(
        self,
        property_key: str,
        user_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a specified user's property

        Path: /api/2/user/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/api/2/user/properties/{property_key}"
        params = {
            "userKey": user_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_find_users(
        self,
        include_inactive: bool | None = None,
        max_results: int | None = None,
        include_active: bool | None = None,
        start_at: int | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users by username

        Path: /api/2/user/search
        Method: GET
        """
        path = "/api/2/user/search"
        params = {
            "includeInactive": include_inactive,
            "maxResults": max_results,
            "includeActive": include_active,
            "startAt": start_at,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_session(
        self,
        username: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete user session

        Path: /api/2/user/session/{username}
        Method: DELETE
        """
        path = f"/api/2/user/session/{username}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_find_users_with_browse_permission(
        self,
        project_key: str | None = None,
        issue_key: str | None = None,
        max_results: int | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users with browse permission

        Path: /api/2/user/viewissue/search
        Method: GET
        """
        path = "/api/2/user/viewissue/search"
        params = {
            "projectKey": project_key,
            "issueKey": issue_key,
            "maxResults": max_results,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_paginated_versions(
        self,
        max_results: int | None = None,
        query: str | None = None,
        project_ids: list[Any] | None = None,
        start_at: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get paginated versions

        Path: /api/2/version
        Method: GET
        """
        path = "/api/2/version"
        params = {
            "maxResults": max_results,
            "query": query,
            "projectIds": project_ids,
            "startAt": start_at,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_version(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create new version

        Path: /api/2/version
        Method: POST
        """
        path = "/api/2/version"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_remote_version_links(
        self,
        global_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get remote version links by global ID

        Path: /api/2/version/remotelink
        Method: GET
        """
        path = "/api/2/version/remotelink"
        params = {
            "globalId": global_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_version(
        self,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version details

        Path: /api/2/version/{id}
        Method: GET
        """
        path = f"/api/2/version/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_version(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update version details

        Path: /api/2/version/{id}
        Method: PUT
        """
        path = f"/api/2/version/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_merge(
        self,
        move_issues_to: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Merge versions

        Path: /api/2/version/{id}/mergeto/{moveIssuesTo}
        Method: PUT
        """
        path = f"/api/2/version/{id_}/mergeto/{move_issues_to}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_move_version(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Modify version's sequence

        Path: /api/2/version/{id}/move
        Method: POST
        """
        path = f"/api/2/version/{id_}/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_version_related_issues(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version related issues count

        Path: /api/2/version/{id}/relatedIssueCounts
        Method: GET
        """
        path = f"/api/2/version/{id_}/relatedIssueCounts"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_1(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete version and replace values

        Path: /api/2/version/{id}/removeAndSwap
        Method: POST
        """
        path = f"/api/2/version/{id_}/removeAndSwap"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_version_unresolved_issues(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version unresolved issues count

        Path: /api/2/version/{id}/unresolvedIssueCount
        Method: GET
        """
        path = f"/api/2/version/{id_}/unresolvedIssueCount"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_remote_version_links_by_version_id(
        self,
        version_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get remote version links by version ID

        Path: /api/2/version/{versionId}/remotelink
        Method: GET
        """
        path = f"/api/2/version/{version_id}/remotelink"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_or_update_remote_version_link(
        self,
        version_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create or update remote version link without global ID

        Path: /api/2/version/{versionId}/remotelink
        Method: POST
        """
        path = f"/api/2/version/{version_id}/remotelink"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_remote_version_links_by_version_id(
        self,
        version_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete all remote version links for version

        Path: /api/2/version/{versionId}/remotelink
        Method: DELETE
        """
        path = f"/api/2/version/{version_id}/remotelink"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_remote_version_link(
        self,
        version_id: str,
        global_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get specific remote version link

        Path: /api/2/version/{versionId}/remotelink/{globalId}
        Method: GET
        """
        path = f"/api/2/version/{version_id}/remotelink/{global_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_or_update_remote_version_link_1(
        self,
        version_id: str,
        global_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create or update remote version link with global ID

        Path: /api/2/version/{versionId}/remotelink/{globalId}
        Method: POST
        """
        path = f"/api/2/version/{version_id}/remotelink/{global_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_remote_version_link(
        self,
        version_id: str,
        global_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete specific remote version link

        Path: /api/2/version/{versionId}/remotelink/{globalId}
        Method: DELETE
        """
        path = f"/api/2/version/{version_id}/remotelink/{global_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_all_workflows(
        self,
        workflow_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all workflows

        Path: /api/2/workflow
        Method: GET
        """
        path = "/api/2/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_create_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create a new workflow scheme

        Path: /api/2/workflowscheme
        Method: POST
        """
        path = "/api/2/workflowscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_by_id(
        self,
        id_: int,
        return_draft_if_exists: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get requested workflow scheme by ID

        Path: /api/2/workflowscheme/{id}
        Method: GET
        """
        path = f"/api/2/workflowscheme/{id_}"
        params = {
            "returnDraftIfExists": return_draft_if_exists,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a specified workflow scheme

        Path: /api/2/workflowscheme/{id}
        Method: PUT
        """
        path = f"/api/2/workflowscheme/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete the specified workflow scheme

        Path: /api/2/workflowscheme/{id}
        Method: DELETE
        """
        path = f"/api/2/workflowscheme/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_create_draft_for_parent(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a draft for a workflow scheme

        Path: /api/2/workflowscheme/{id}/createdraft
        Method: POST
        """
        path = f"/api/2/workflowscheme/{id_}/createdraft"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_default(
        self,
        id_: int,
        return_draft_if_exists: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get default workflow for a scheme

        Path: /api/2/workflowscheme/{id}/default
        Method: GET
        """
        path = f"/api/2/workflowscheme/{id_}/default"
        params = {
            "returnDraftIfExists": return_draft_if_exists,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_default(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update default workflow for a scheme

        Path: /api/2/workflowscheme/{id}/default
        Method: PUT
        """
        path = f"/api/2/workflowscheme/{id_}/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_default(
        self,
        id_: int,
        update_draft_if_needed: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove default workflow from a scheme

        Path: /api/2/workflowscheme/{id}/default
        Method: DELETE
        """
        path = f"/api/2/workflowscheme/{id_}/default"
        params = {
            "updateDraftIfNeeded": update_draft_if_needed,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_draft_by_id(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get requested draft workflow scheme by ID

        Path: /api/2/workflowscheme/{id}/draft
        Method: GET
        """
        path = f"/api/2/workflowscheme/{id_}/draft"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_draft(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a draft workflow scheme

        Path: /api/2/workflowscheme/{id}/draft
        Method: PUT
        """
        path = f"/api/2/workflowscheme/{id_}/draft"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_draft_by_id(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete the specified draft workflow scheme

        Path: /api/2/workflowscheme/{id}/draft
        Method: DELETE
        """
        path = f"/api/2/workflowscheme/{id_}/draft"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_draft_default(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get default workflow for a draft scheme

        Path: /api/2/workflowscheme/{id}/draft/default
        Method: GET
        """
        path = f"/api/2/workflowscheme/{id_}/draft/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_draft_default(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update default workflow for a draft scheme

        Path: /api/2/workflowscheme/{id}/draft/default
        Method: PUT
        """
        path = f"/api/2/workflowscheme/{id_}/draft/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_draft_default(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove default workflow from a draft scheme

        Path: /api/2/workflowscheme/{id}/draft/default
        Method: DELETE
        """
        path = f"/api/2/workflowscheme/{id_}/draft/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_draft_issue_type(
        self,
        issue_type: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type mapping for a draft scheme

        Path: /api/2/workflowscheme/{id}/draft/issuetype/{issueType}
        Method: GET
        """
        path = f"/api/2/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_draft_issue_type(
        self,
        issue_type: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set an issue type mapping for a draft scheme

        Path: /api/2/workflowscheme/{id}/draft/issuetype/{issueType}
        Method: PUT
        """
        path = f"/api/2/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_draft_issue_type(
        self,
        issue_type: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete an issue type mapping from a draft scheme

        Path: /api/2/workflowscheme/{id}/draft/issuetype/{issueType}
        Method: DELETE
        """
        path = f"/api/2/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_draft_workflow(
        self,
        id_: int,
        workflow_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get draft workflow mappings

        Path: /api/2/workflowscheme/{id}/draft/workflow
        Method: GET
        """
        path = f"/api/2/workflowscheme/{id_}/draft/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_draft_workflow_mapping(
        self,
        id_: int,
        workflow_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a workflow mapping in a draft scheme

        Path: /api/2/workflowscheme/{id}/draft/workflow
        Method: PUT
        """
        path = f"/api/2/workflowscheme/{id_}/draft/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_draft_workflow_mapping(
        self,
        id_: int,
        workflow_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a workflow mapping from a draft scheme

        Path: /api/2/workflowscheme/{id}/draft/workflow
        Method: DELETE
        """
        path = f"/api/2/workflowscheme/{id_}/draft/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_issue_type(
        self,
        issue_type: str,
        id_: int,
        return_draft_if_exists: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type mapping for a scheme

        Path: /api/2/workflowscheme/{id}/issuetype/{issueType}
        Method: GET
        """
        path = f"/api/2/workflowscheme/{id_}/issuetype/{issue_type}"
        params = {
            "returnDraftIfExists": return_draft_if_exists,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_set_issue_type(
        self,
        issue_type: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set an issue type mapping for a scheme

        Path: /api/2/workflowscheme/{id}/issuetype/{issueType}
        Method: PUT
        """
        path = f"/api/2/workflowscheme/{id_}/issuetype/{issue_type}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_issue_type(
        self,
        issue_type: str,
        id_: int,
        update_draft_if_needed: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete an issue type mapping from a scheme

        Path: /api/2/workflowscheme/{id}/issuetype/{issueType}
        Method: DELETE
        """
        path = f"/api/2/workflowscheme/{id_}/issuetype/{issue_type}"
        params = {
            "updateDraftIfNeeded": update_draft_if_needed,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_workflow(
        self,
        id_: int,
        workflow_name: str | None = None,
        return_draft_if_exists: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow mappings for a scheme

        Path: /api/2/workflowscheme/{id}/workflow
        Method: GET
        """
        path = f"/api/2/workflowscheme/{id_}/workflow"
        params = {
            "workflowName": workflow_name,
            "returnDraftIfExists": return_draft_if_exists,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_update_workflow_mapping(
        self,
        id_: int,
        workflow_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a workflow mapping in a scheme

        Path: /api/2/workflowscheme/{id}/workflow
        Method: PUT
        """
        path = f"/api/2/workflowscheme/{id_}/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_server_delete_workflow_mapping(
        self,
        id_: int,
        update_draft_if_needed: bool | None = None,
        workflow_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a workflow mapping from a scheme

        Path: /api/2/workflowscheme/{id}/workflow
        Method: DELETE
        """
        path = f"/api/2/workflowscheme/{id_}/workflow"
        params = {
            "updateDraftIfNeeded": update_draft_if_needed,
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_get_ids_of_worklogs_deleted_since(
        self,
        since: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Returns worklogs deleted since given time.

        Path: /api/2/worklog/deleted
        Method: GET
        """
        path = "/api/2/worklog/deleted"
        params = {
            "since": since,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_get_worklogs_for_ids(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Returns worklogs for given ids.

        Path: /api/2/worklog/list
        Method: POST
        """
        path = "/api/2/worklog/list"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_get_ids_of_worklogs_modified_since(
        self,
        since: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Returns worklogs updated since given time.

        Path: /api/2/worklog/updated
        Method: GET
        """
        path = "/api/2/worklog/updated"
        params = {
            "since": since,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_current_user(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get current user session information

        Path: /auth/1/session
        Method: GET
        """
        path = "/auth/1/session"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_server_login(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create new user session

        Path: /auth/1/session
        Method: POST
        """
        path = "/auth/1/session"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_server_logout(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Delete current user session

        Path: /auth/1/session
        Method: DELETE
        """
        path = "/auth/1/session"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_server_release(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Invalidate the current WebSudo session

        Path: /auth/1/websudo
        Method: DELETE
        """
        path = "/auth/1/websudo"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )
