# Generated API Client for JiraCloud
from typing import Any

from ..models import Response
from .base import BaseAtlassianClient


class JiraCloudAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def jira_cloud_get_banner(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get announcement banner configuration

        Path: /rest/api/3/announcementBanner
        Method: GET
        """
        path = "/rest/api/3/announcementBanner"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_banner(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update announcement banner configuration

        Path: /rest/api/3/announcementBanner
        Method: PUT
        """
        path = "/rest/api/3/announcementBanner"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_custom_fields_configurations(
        self,
        id_: list[Any] | None = None,
        field_context_id: list[Any] | None = None,
        issue_id: int | None = None,
        project_key_or_id: str | None = None,
        issue_type_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk get custom field configurations

        Path: /rest/api/3/app/field/context/configuration/list
        Method: POST
        """
        path = "/rest/api/3/app/field/context/configuration/list"
        params = {
            "id": id_,
            "fieldContextId": field_context_id,
            "issueId": issue_id,
            "projectKeyOrId": project_key_or_id,
            "issueTypeId": issue_type_id,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_multiple_custom_field_values(
        self,
        generate_changelog: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update custom fields

        Path: /rest/api/3/app/field/value
        Method: POST
        """
        path = "/rest/api/3/app/field/value"
        params = {
            "generateChangelog": generate_changelog,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_custom_field_configuration(
        self,
        field_id_or_key: str,
        id_: list[Any] | None = None,
        field_context_id: list[Any] | None = None,
        issue_id: int | None = None,
        project_key_or_id: str | None = None,
        issue_type_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom field configurations

        Path: /rest/api/3/app/field/{fieldIdOrKey}/context/configuration
        Method: GET
        """
        path = f"/rest/api/3/app/field/{field_id_or_key}/context/configuration"
        params = {
            "id": id_,
            "fieldContextId": field_context_id,
            "issueId": issue_id,
            "projectKeyOrId": project_key_or_id,
            "issueTypeId": issue_type_id,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_custom_field_configuration(
        self,
        field_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update custom field configurations

        Path: /rest/api/3/app/field/{fieldIdOrKey}/context/configuration
        Method: PUT
        """
        path = f"/rest/api/3/app/field/{field_id_or_key}/context/configuration"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_custom_field_value(
        self,
        field_id_or_key: str,
        generate_changelog: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update custom field value

        Path: /rest/api/3/app/field/{fieldIdOrKey}/value
        Method: PUT
        """
        path = f"/rest/api/3/app/field/{field_id_or_key}/value"
        params = {
            "generateChangelog": generate_changelog,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_application_property(
        self,
        key: str | None = None,
        permission_level: str | None = None,
        key_filter: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get application property

        Path: /rest/api/3/application-properties
        Method: GET
        """
        path = "/rest/api/3/application-properties"
        params = {
            "key": key,
            "permissionLevel": permission_level,
            "keyFilter": key_filter,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_advanced_settings(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get advanced settings

        Path: /rest/api/3/application-properties/advanced-settings
        Method: GET
        """
        path = "/rest/api/3/application-properties/advanced-settings"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_application_property(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set application property

        Path: /rest/api/3/application-properties/{id}
        Method: PUT
        """
        path = f"/rest/api/3/application-properties/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_application_roles(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all application roles

        Path: /rest/api/3/applicationrole
        Method: GET
        """
        path = "/rest/api/3/applicationrole"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_application_role(
        self,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get application role

        Path: /rest/api/3/applicationrole/{key}
        Method: GET
        """
        path = f"/rest/api/3/applicationrole/{key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_attachment_content(
        self,
        id_: str,
        redirect: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachment content

        Path: /rest/api/3/attachment/content/{id}
        Method: GET
        """
        path = f"/rest/api/3/attachment/content/{id_}"
        params = {
            "redirect": redirect,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_attachment_meta(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get Jira attachment settings

        Path: /rest/api/3/attachment/meta
        Method: GET
        """
        path = "/rest/api/3/attachment/meta"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_attachment_thumbnail(
        self,
        id_: str,
        redirect: bool | None = None,
        fallback_to_default: bool | None = None,
        width: int | None = None,
        height: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachment thumbnail

        Path: /rest/api/3/attachment/thumbnail/{id}
        Method: GET
        """
        path = f"/rest/api/3/attachment/thumbnail/{id_}"
        params = {
            "redirect": redirect,
            "fallbackToDefault": fallback_to_default,
            "width": width,
            "height": height,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_attachment(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete attachment

        Path: /rest/api/3/attachment/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/attachment/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_attachment(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachment metadata

        Path: /rest/api/3/attachment/{id}
        Method: GET
        """
        path = f"/rest/api/3/attachment/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_expand_attachment_for_humans(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all metadata for an expanded attachment

        Path: /rest/api/3/attachment/{id}/expand/human
        Method: GET
        """
        path = f"/rest/api/3/attachment/{id_}/expand/human"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_expand_attachment_for_machines(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get contents metadata for an expanded attachment

        Path: /rest/api/3/attachment/{id}/expand/raw
        Method: GET
        """
        path = f"/rest/api/3/attachment/{id_}/expand/raw"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_audit_records(
        self,
        offset: int | None = None,
        limit: int | None = None,
        filter: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get audit records

        Path: /rest/api/3/auditing/record
        Method: GET
        """
        path = "/rest/api/3/auditing/record"
        params = {
            "offset": offset,
            "limit": limit,
            "filter": filter,
            "from": from_,
            "to": to,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_system_avatars(
        self,
        type_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get system avatars by type

        Path: /rest/api/3/avatar/{type}/system
        Method: GET
        """
        path = f"/rest/api/3/avatar/{type_}/system"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_submit_bulk_delete(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk delete issues

        Path: /rest/api/3/bulk/issues/delete
        Method: POST
        """
        path = "/rest/api/3/bulk/issues/delete"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_bulk_editable_fields(
        self,
        issue_ids_or_keys: str,
        search_text: str | None = None,
        ending_before: str | None = None,
        starting_after: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get bulk editable fields

        Path: /rest/api/3/bulk/issues/fields
        Method: GET
        """
        path = "/rest/api/3/bulk/issues/fields"
        params = {
            "issueIdsOrKeys": issue_ids_or_keys,
            "searchText": search_text,
            "endingBefore": ending_before,
            "startingAfter": starting_after,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_submit_bulk_edit(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk edit issues

        Path: /rest/api/3/bulk/issues/fields
        Method: POST
        """
        path = "/rest/api/3/bulk/issues/fields"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_submit_bulk_move(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk move issues

        Path: /rest/api/3/bulk/issues/move
        Method: POST
        """
        path = "/rest/api/3/bulk/issues/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_available_transitions(
        self,
        issue_ids_or_keys: str,
        ending_before: str | None = None,
        starting_after: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get available transitions

        Path: /rest/api/3/bulk/issues/transition
        Method: GET
        """
        path = "/rest/api/3/bulk/issues/transition"
        params = {
            "issueIdsOrKeys": issue_ids_or_keys,
            "endingBefore": ending_before,
            "startingAfter": starting_after,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_submit_bulk_transition(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk transition issue statuses

        Path: /rest/api/3/bulk/issues/transition
        Method: POST
        """
        path = "/rest/api/3/bulk/issues/transition"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_submit_bulk_unwatch(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk unwatch issues

        Path: /rest/api/3/bulk/issues/unwatch
        Method: POST
        """
        path = "/rest/api/3/bulk/issues/unwatch"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_submit_bulk_watch(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk watch issues

        Path: /rest/api/3/bulk/issues/watch
        Method: POST
        """
        path = "/rest/api/3/bulk/issues/watch"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_bulk_operation_progress(
        self,
        task_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get bulk issue operation progress

        Path: /rest/api/3/bulk/queue/{taskId}
        Method: GET
        """
        path = f"/rest/api/3/bulk/queue/{task_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_bulk_changelogs(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk fetch changelogs

        Path: /rest/api/3/changelog/bulkfetch
        Method: POST
        """
        path = "/rest/api/3/changelog/bulkfetch"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_user_data_classification_levels(
        self,
        status: list[Any] | None = None,
        order_by: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all classification levels

        Path: /rest/api/3/classification-levels
        Method: GET
        """
        path = "/rest/api/3/classification-levels"
        params = {
            "status": status,
            "orderBy": order_by,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_comments_by_ids(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get comments by IDs

        Path: /rest/api/3/comment/list
        Method: POST
        """
        path = "/rest/api/3/comment/list"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_comment_property_keys(
        self,
        comment_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get comment property keys

        Path: /rest/api/3/comment/{commentId}/properties
        Method: GET
        """
        path = f"/rest/api/3/comment/{comment_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_comment_property(
        self,
        comment_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete comment property

        Path: /rest/api/3/comment/{commentId}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/api/3/comment/{comment_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_comment_property(
        self,
        comment_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get comment property

        Path: /rest/api/3/comment/{commentId}/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/api/3/comment/{comment_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_comment_property(
        self,
        comment_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set comment property

        Path: /rest/api/3/comment/{commentId}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/api/3/comment/{comment_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_components_for_projects(
        self,
        project_ids_or_keys: list[Any] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        query: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find components for projects

        Path: /rest/api/3/component
        Method: GET
        """
        path = "/rest/api/3/component"
        params = {
            "projectIdsOrKeys": project_ids_or_keys,
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "query": query,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_component(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create component

        Path: /rest/api/3/component
        Method: POST
        """
        path = "/rest/api/3/component"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_component(
        self,
        id_: str,
        move_issues_to: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete component

        Path: /rest/api/3/component/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/component/{id_}"
        params = {
            "moveIssuesTo": move_issues_to,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_component(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get component

        Path: /rest/api/3/component/{id}
        Method: GET
        """
        path = f"/rest/api/3/component/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_component(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update component

        Path: /rest/api/3/component/{id}
        Method: PUT
        """
        path = f"/rest/api/3/component/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_component_related_issues(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get component issues count

        Path: /rest/api/3/component/{id}/relatedIssueCounts
        Method: GET
        """
        path = f"/rest/api/3/component/{id_}/relatedIssueCounts"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_field_association_schemes(
        self,
        project_id: list[Any] | None = None,
        query: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get field schemes

        Path: /rest/api/3/config/fieldschemes
        Method: GET
        """
        path = "/rest/api/3/config/fieldschemes"
        params = {
            "projectId": project_id,
            "query": query,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_field_association_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create field scheme

        Path: /rest/api/3/config/fieldschemes
        Method: POST
        """
        path = "/rest/api/3/config/fieldschemes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_fields_associated_with_schemes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Remove fields associated with field schemes

        Path: /rest/api/3/config/fieldschemes/fields
        Method: DELETE
        """
        path = "/rest/api/3/config/fieldschemes/fields"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_fields_associated_with_schemes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update fields associated with field schemes

        Path: /rest/api/3/config/fieldschemes/fields
        Method: PUT
        """
        path = "/rest/api/3/config/fieldschemes/fields"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_field_association_scheme_item_parameters(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Remove field parameters

        Path: /rest/api/3/config/fieldschemes/fields/parameters
        Method: DELETE
        """
        path = "/rest/api/3/config/fieldschemes/fields/parameters"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_field_association_scheme_item_parameters(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update field parameters

        Path: /rest/api/3/config/fieldschemes/fields/parameters
        Method: PUT
        """
        path = "/rest/api/3/config/fieldschemes/fields/parameters"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_projects_with_field_schemes(
        self,
        project_id: list[Any],
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get projects with field schemes

        Path: /rest/api/3/config/fieldschemes/projects
        Method: GET
        """
        path = "/rest/api/3/config/fieldschemes/projects"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_associate_projects_to_field_association_schemes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Associate projects to field schemes

        Path: /rest/api/3/config/fieldschemes/projects
        Method: PUT
        """
        path = "/rest/api/3/config/fieldschemes/projects"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_field_association_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a field scheme

        Path: /rest/api/3/config/fieldschemes/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/config/fieldschemes/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_field_association_scheme_by_id(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get field scheme

        Path: /rest/api/3/config/fieldschemes/{id}
        Method: GET
        """
        path = f"/rest/api/3/config/fieldschemes/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_field_association_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update field scheme

        Path: /rest/api/3/config/fieldschemes/{id}
        Method: PUT
        """
        path = f"/rest/api/3/config/fieldschemes/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_clone_field_association_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Clone field scheme

        Path: /rest/api/3/config/fieldschemes/{id}/clone
        Method: POST
        """
        path = f"/rest/api/3/config/fieldschemes/{id_}/clone"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_field_association_scheme_fields(
        self,
        id_: int,
        start_at: int | None = None,
        max_results: int | None = None,
        field_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search field scheme fields

        Path: /rest/api/3/config/fieldschemes/{id}/fields
        Method: GET
        """
        path = f"/rest/api/3/config/fieldschemes/{id_}/fields"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "fieldId": field_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_field_association_scheme_item_parameters(
        self,
        id_: int,
        field_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get field parameters

        Path: /rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters
        Method: GET
        """
        path = f"/rest/api/3/config/fieldschemes/{id_}/fields/{field_id}/parameters"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_field_association_scheme_projects(
        self,
        id_: int,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search field scheme projects

        Path: /rest/api/3/config/fieldschemes/{id}/projects
        Method: GET
        """
        path = f"/rest/api/3/config/fieldschemes/{id_}/projects"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_configuration(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get global settings

        Path: /rest/api/3/configuration
        Method: GET
        """
        path = "/rest/api/3/configuration"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_selected_time_tracking_implementation(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get selected time tracking provider

        Path: /rest/api/3/configuration/timetracking
        Method: GET
        """
        path = "/rest/api/3/configuration/timetracking"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_select_time_tracking_implementation(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Select time tracking provider

        Path: /rest/api/3/configuration/timetracking
        Method: PUT
        """
        path = "/rest/api/3/configuration/timetracking"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_available_time_tracking_implementations(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all time tracking providers

        Path: /rest/api/3/configuration/timetracking/list
        Method: GET
        """
        path = "/rest/api/3/configuration/timetracking/list"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_shared_time_tracking_configuration(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get time tracking settings

        Path: /rest/api/3/configuration/timetracking/options
        Method: GET
        """
        path = "/rest/api/3/configuration/timetracking/options"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_shared_time_tracking_configuration(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set time tracking settings

        Path: /rest/api/3/configuration/timetracking/options
        Method: PUT
        """
        path = "/rest/api/3/configuration/timetracking/options"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_custom_field_option(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom field option

        Path: /rest/api/3/customFieldOption/{id}
        Method: GET
        """
        path = f"/rest/api/3/customFieldOption/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_dashboards(
        self,
        filter: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all dashboards

        Path: /rest/api/3/dashboard
        Method: GET
        """
        path = "/rest/api/3/dashboard"
        params = {
            "filter": filter,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_dashboard(
        self,
        extend_admin_permissions: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create dashboard

        Path: /rest/api/3/dashboard
        Method: POST
        """
        path = "/rest/api/3/dashboard"
        params = {
            "extendAdminPermissions": extend_admin_permissions,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_edit_dashboards(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk edit dashboards

        Path: /rest/api/3/dashboard/bulk/edit
        Method: PUT
        """
        path = "/rest/api/3/dashboard/bulk/edit"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_available_dashboard_gadgets(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get available gadgets

        Path: /rest/api/3/dashboard/gadgets
        Method: GET
        """
        path = "/rest/api/3/dashboard/gadgets"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_dashboards_paginated(
        self,
        dashboard_name: str | None = None,
        account_id: str | None = None,
        owner: str | None = None,
        groupname: str | None = None,
        group_id: str | None = None,
        project_id: int | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        status: str | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search for dashboards

        Path: /rest/api/3/dashboard/search
        Method: GET
        """
        path = "/rest/api/3/dashboard/search"
        params = {
            "dashboardName": dashboard_name,
            "accountId": account_id,
            "owner": owner,
            "groupname": groupname,
            "groupId": group_id,
            "projectId": project_id,
            "orderBy": order_by,
            "startAt": start_at,
            "maxResults": max_results,
            "status": status,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_gadgets(
        self,
        dashboard_id: int,
        module_key: list[Any] | None = None,
        uri: list[Any] | None = None,
        gadget_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get gadgets

        Path: /rest/api/3/dashboard/{dashboardId}/gadget
        Method: GET
        """
        path = f"/rest/api/3/dashboard/{dashboard_id}/gadget"
        params = {
            "moduleKey": module_key,
            "uri": uri,
            "gadgetId": gadget_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_gadget(
        self,
        dashboard_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add gadget to dashboard

        Path: /rest/api/3/dashboard/{dashboardId}/gadget
        Method: POST
        """
        path = f"/rest/api/3/dashboard/{dashboard_id}/gadget"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_gadget(
        self,
        dashboard_id: int,
        gadget_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove gadget from dashboard

        Path: /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}
        Method: DELETE
        """
        path = f"/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_gadget(
        self,
        dashboard_id: int,
        gadget_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update gadget on dashboard

        Path: /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}
        Method: PUT
        """
        path = f"/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_dashboard_item_property_keys(
        self,
        dashboard_id: str,
        item_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get dashboard item property keys

        Path: /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties
        Method: GET
        """
        path = f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_dashboard_item_property(
        self,
        dashboard_id: str,
        item_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete dashboard item property

        Path: /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_dashboard_item_property(
        self,
        dashboard_id: str,
        item_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get dashboard item property

        Path: /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_dashboard_item_property(
        self,
        dashboard_id: str,
        item_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set dashboard item property

        Path: /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_dashboard(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete dashboard

        Path: /rest/api/3/dashboard/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/dashboard/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_dashboard(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get dashboard

        Path: /rest/api/3/dashboard/{id}
        Method: GET
        """
        path = f"/rest/api/3/dashboard/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_dashboard(
        self,
        id_: str,
        extend_admin_permissions: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update dashboard

        Path: /rest/api/3/dashboard/{id}
        Method: PUT
        """
        path = f"/rest/api/3/dashboard/{id_}"
        params = {
            "extendAdminPermissions": extend_admin_permissions,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_copy_dashboard(
        self,
        id_: str,
        extend_admin_permissions: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Copy dashboard

        Path: /rest/api/3/dashboard/{id}/copy
        Method: POST
        """
        path = f"/rest/api/3/dashboard/{id_}/copy"
        params = {
            "extendAdminPermissions": extend_admin_permissions,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_policy(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get data policy for the workspace

        Path: /rest/api/3/data-policy
        Method: GET
        """
        path = "/rest/api/3/data-policy"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_policies(
        self,
        ids: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get data policy for projects

        Path: /rest/api/3/data-policy/project
        Method: GET
        """
        path = "/rest/api/3/data-policy/project"
        params = {
            "ids": ids,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_events(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get events

        Path: /rest/api/3/events
        Method: GET
        """
        path = "/rest/api/3/events"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_analyse_expression(
        self,
        check: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Analyse Jira expression

        Path: /rest/api/3/expression/analyse
        Method: POST
        """
        path = "/rest/api/3/expression/analyse"
        params = {
            "check": check,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_evaluate_jira_expression(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Currently being removed. Evaluate Jira expression

        Path: /rest/api/3/expression/eval
        Method: POST
        """
        path = "/rest/api/3/expression/eval"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_evaluate_jsis_jira_expression(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Evaluate Jira expression using enhanced search API

        Path: /rest/api/3/expression/evaluate
        Method: POST
        """
        path = "/rest/api/3/expression/evaluate"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_fields(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get fields

        Path: /rest/api/3/field
        Method: GET
        """
        path = "/rest/api/3/field"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_custom_field(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create custom field

        Path: /rest/api/3/field
        Method: POST
        """
        path = "/rest/api/3/field"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_associations(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Remove associations

        Path: /rest/api/3/field/association
        Method: DELETE
        """
        path = "/rest/api/3/field/association"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_associations(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create associations

        Path: /rest/api/3/field/association
        Method: PUT
        """
        path = "/rest/api/3/field/association"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_fields_paginated(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        type_: list[Any] | None = None,
        id_: list[Any] | None = None,
        query: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        project_ids: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get fields paginated

        Path: /rest/api/3/field/search
        Method: GET
        """
        path = "/rest/api/3/field/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "type": type_,
            "id": id_,
            "query": query,
            "orderBy": order_by,
            "expand": expand,
            "projectIds": project_ids,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_trashed_fields_paginated(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[Any] | None = None,
        query: str | None = None,
        expand: str | None = None,
        order_by: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get fields in trash paginated

        Path: /rest/api/3/field/search/trashed
        Method: GET
        """
        path = "/rest/api/3/field/search/trashed"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "query": query,
            "expand": expand,
            "orderBy": order_by,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_custom_field(
        self,
        field_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update custom field

        Path: /rest/api/3/field/{fieldId}
        Method: PUT
        """
        path = f"/rest/api/3/field/{field_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_field_project_associations(
        self,
        field_id: str,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get field project associations

        Path: /rest/api/3/field/{fieldId}/association/project
        Method: GET
        """
        path = f"/rest/api/3/field/{field_id}/association/project"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_contexts_for_field(
        self,
        field_id: str,
        is_any_issue_type: bool | None = None,
        is_global_context: bool | None = None,
        context_id: list[Any] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom field contexts

        Path: /rest/api/3/field/{fieldId}/context
        Method: GET
        """
        path = f"/rest/api/3/field/{field_id}/context"
        params = {
            "isAnyIssueType": is_any_issue_type,
            "isGlobalContext": is_global_context,
            "contextId": context_id,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_custom_field_context(
        self,
        field_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create custom field context

        Path: /rest/api/3/field/{fieldId}/context
        Method: POST
        """
        path = f"/rest/api/3/field/{field_id}/context"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_default_values(
        self,
        field_id: str,
        context_id: list[Any] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom field contexts default values

        Path: /rest/api/3/field/{fieldId}/context/defaultValue
        Method: GET
        """
        path = f"/rest/api/3/field/{field_id}/context/defaultValue"
        params = {
            "contextId": context_id,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_default_values(
        self,
        field_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set custom field contexts default values

        Path: /rest/api/3/field/{fieldId}/context/defaultValue
        Method: PUT
        """
        path = f"/rest/api/3/field/{field_id}/context/defaultValue"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type_mappings_for_contexts(
        self,
        field_id: str,
        context_id: list[Any] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue types for custom field context

        Path: /rest/api/3/field/{fieldId}/context/issuetypemapping
        Method: GET
        """
        path = f"/rest/api/3/field/{field_id}/context/issuetypemapping"
        params = {
            "contextId": context_id,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_custom_field_contexts_for_projects_and_issue_types(
        self,
        field_id: str,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom field contexts for projects and issue types

        Path: /rest/api/3/field/{fieldId}/context/mapping
        Method: POST
        """
        path = f"/rest/api/3/field/{field_id}/context/mapping"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_context_mapping(
        self,
        field_id: str,
        context_id: list[Any] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project mappings for custom field context

        Path: /rest/api/3/field/{fieldId}/context/projectmapping
        Method: GET
        """
        path = f"/rest/api/3/field/{field_id}/context/projectmapping"
        params = {
            "contextId": context_id,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_custom_field_context(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete custom field context

        Path: /rest/api/3/field/{fieldId}/context/{contextId}
        Method: DELETE
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_custom_field_context(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update custom field context

        Path: /rest/api/3/field/{fieldId}/context/{contextId}
        Method: PUT
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_issue_types_to_context(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add issue types to context

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/issuetype
        Method: PUT
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/issuetype"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_issue_types_from_context(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove issue types from context

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove
        Method: POST
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/issuetype/remove"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_options_for_context(
        self,
        field_id: str,
        context_id: int,
        option_id: int | None = None,
        only_options: bool | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get custom field options (context)

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/option
        Method: GET
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/option"
        params = {
            "optionId": option_id,
            "onlyOptions": only_options,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_custom_field_option(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create custom field options (context)

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/option
        Method: POST
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/option"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_custom_field_option(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update custom field options (context)

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/option
        Method: PUT
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/option"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_reorder_custom_field_options(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reorder custom field options (context)

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/option/move
        Method: PUT
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/option/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_custom_field_option(
        self,
        field_id: str,
        context_id: int,
        option_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete custom field options (context)

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}
        Method: DELETE
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/option/{option_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_replace_custom_field_option(
        self,
        field_id: str,
        option_id: int,
        context_id: int,
        replace_with: int | None = None,
        jql: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Replace custom field options

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue
        Method: DELETE
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/option/{option_id}/issue"
        params = {
            "replaceWith": replace_with,
            "jql": jql,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_assign_projects_to_custom_field_context(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign custom field context to projects

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/project
        Method: PUT
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_custom_field_context_from_projects(
        self,
        field_id: str,
        context_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove custom field context from projects

        Path: /rest/api/3/field/{fieldId}/context/{contextId}/project/remove
        Method: POST
        """
        path = f"/rest/api/3/field/{field_id}/context/{context_id}/project/remove"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_contexts_for_field_deprecated(
        self,
        field_id: str,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get contexts for a field

        Path: /rest/api/3/field/{fieldId}/contexts
        Method: GET
        """
        path = f"/rest/api/3/field/{field_id}/contexts"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_screens_for_field(
        self,
        field_id: str,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get screens for a field

        Path: /rest/api/3/field/{fieldId}/screens
        Method: GET
        """
        path = f"/rest/api/3/field/{field_id}/screens"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_issue_field_options(
        self,
        field_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issue field options

        Path: /rest/api/3/field/{fieldKey}/option
        Method: GET
        """
        path = f"/rest/api/3/field/{field_key}/option"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issue_field_option(
        self,
        field_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create issue field option

        Path: /rest/api/3/field/{fieldKey}/option
        Method: POST
        """
        path = f"/rest/api/3/field/{field_key}/option"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_selectable_issue_field_options(
        self,
        field_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get selectable issue field options

        Path: /rest/api/3/field/{fieldKey}/option/suggestions/edit
        Method: GET
        """
        path = f"/rest/api/3/field/{field_key}/option/suggestions/edit"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_visible_issue_field_options(
        self,
        field_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get visible issue field options

        Path: /rest/api/3/field/{fieldKey}/option/suggestions/search
        Method: GET
        """
        path = f"/rest/api/3/field/{field_key}/option/suggestions/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue_field_option(
        self,
        field_key: str,
        option_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue field option

        Path: /rest/api/3/field/{fieldKey}/option/{optionId}
        Method: DELETE
        """
        path = f"/rest/api/3/field/{field_key}/option/{option_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_field_option(
        self,
        field_key: str,
        option_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue field option

        Path: /rest/api/3/field/{fieldKey}/option/{optionId}
        Method: GET
        """
        path = f"/rest/api/3/field/{field_key}/option/{option_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_issue_field_option(
        self,
        field_key: str,
        option_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update issue field option

        Path: /rest/api/3/field/{fieldKey}/option/{optionId}
        Method: PUT
        """
        path = f"/rest/api/3/field/{field_key}/option/{option_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_replace_issue_field_option(
        self,
        field_key: str,
        option_id: int,
        replace_with: int | None = None,
        jql: str | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Replace issue field option

        Path: /rest/api/3/field/{fieldKey}/option/{optionId}/issue
        Method: DELETE
        """
        path = f"/rest/api/3/field/{field_key}/option/{option_id}/issue"
        params = {
            "replaceWith": replace_with,
            "jql": jql,
            "overrideScreenSecurity": override_screen_security,
            "overrideEditableFlag": override_editable_flag,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_custom_field(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete custom field

        Path: /rest/api/3/field/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/field/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_restore_custom_field(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Restore custom field from trash

        Path: /rest/api/3/field/{id}/restore
        Method: POST
        """
        path = f"/rest/api/3/field/{id_}/restore"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_trash_custom_field(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move custom field to trash

        Path: /rest/api/3/field/{id}/trash
        Method: POST
        """
        path = f"/rest/api/3/field/{id_}/trash"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_field_configurations(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[Any] | None = None,
        is_default: bool | None = None,
        query: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all field configurations

        Path: /rest/api/3/fieldconfiguration
        Method: GET
        """
        path = "/rest/api/3/fieldconfiguration"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "isDefault": is_default,
            "query": query,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_field_configuration(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create field configuration

        Path: /rest/api/3/fieldconfiguration
        Method: POST
        """
        path = "/rest/api/3/fieldconfiguration"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_field_configuration(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete field configuration

        Path: /rest/api/3/fieldconfiguration/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/fieldconfiguration/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_field_configuration(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update field configuration

        Path: /rest/api/3/fieldconfiguration/{id}
        Method: PUT
        """
        path = f"/rest/api/3/fieldconfiguration/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_field_configuration_items(
        self,
        id_: int,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get field configuration items

        Path: /rest/api/3/fieldconfiguration/{id}/fields
        Method: GET
        """
        path = f"/rest/api/3/fieldconfiguration/{id_}/fields"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_field_configuration_items(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update field configuration items

        Path: /rest/api/3/fieldconfiguration/{id}/fields
        Method: PUT
        """
        path = f"/rest/api/3/fieldconfiguration/{id_}/fields"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_field_configuration_schemes(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all field configuration schemes

        Path: /rest/api/3/fieldconfigurationscheme
        Method: GET
        """
        path = "/rest/api/3/fieldconfigurationscheme"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_field_configuration_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create field configuration scheme

        Path: /rest/api/3/fieldconfigurationscheme
        Method: POST
        """
        path = "/rest/api/3/fieldconfigurationscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_field_configuration_scheme_mappings(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        field_configuration_scheme_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get field configuration issue type items

        Path: /rest/api/3/fieldconfigurationscheme/mapping
        Method: GET
        """
        path = "/rest/api/3/fieldconfigurationscheme/mapping"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "fieldConfigurationSchemeId": field_configuration_scheme_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_field_configuration_scheme_project_mapping(
        self,
        project_id: list[Any],
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get field configuration schemes for projects

        Path: /rest/api/3/fieldconfigurationscheme/project
        Method: GET
        """
        path = "/rest/api/3/fieldconfigurationscheme/project"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_assign_field_configuration_scheme_to_project(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Assign field configuration scheme to project

        Path: /rest/api/3/fieldconfigurationscheme/project
        Method: PUT
        """
        path = "/rest/api/3/fieldconfigurationscheme/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_field_configuration_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete field configuration scheme

        Path: /rest/api/3/fieldconfigurationscheme/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/fieldconfigurationscheme/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_field_configuration_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update field configuration scheme

        Path: /rest/api/3/fieldconfigurationscheme/{id}
        Method: PUT
        """
        path = f"/rest/api/3/fieldconfigurationscheme/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_field_configuration_scheme_mapping(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign issue types to field configurations

        Path: /rest/api/3/fieldconfigurationscheme/{id}/mapping
        Method: PUT
        """
        path = f"/rest/api/3/fieldconfigurationscheme/{id_}/mapping"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_issue_types_from_global_field_configuration_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove issue types from field configuration scheme

        Path: /rest/api/3/fieldconfigurationscheme/{id}/mapping/delete
        Method: POST
        """
        path = f"/rest/api/3/fieldconfigurationscheme/{id_}/mapping/delete"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_filter(
        self,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create filter

        Path: /rest/api/3/filter
        Method: POST
        """
        path = "/rest/api/3/filter"
        params = {
            "expand": expand,
            "overrideSharePermissions": override_share_permissions,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_default_share_scope(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get default share scope

        Path: /rest/api/3/filter/defaultShareScope
        Method: GET
        """
        path = "/rest/api/3/filter/defaultShareScope"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_default_share_scope(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set default share scope

        Path: /rest/api/3/filter/defaultShareScope
        Method: PUT
        """
        path = "/rest/api/3/filter/defaultShareScope"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_favourite_filters(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get favorite filters

        Path: /rest/api/3/filter/favourite
        Method: GET
        """
        path = "/rest/api/3/filter/favourite"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_my_filters(
        self,
        expand: str | None = None,
        include_favourites: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get my filters

        Path: /rest/api/3/filter/my
        Method: GET
        """
        path = "/rest/api/3/filter/my"
        params = {
            "expand": expand,
            "includeFavourites": include_favourites,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_filters_paginated(
        self,
        filter_name: str | None = None,
        account_id: str | None = None,
        owner: str | None = None,
        groupname: str | None = None,
        group_id: str | None = None,
        project_id: int | None = None,
        id_: list[Any] | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        is_substring_match: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search for filters

        Path: /rest/api/3/filter/search
        Method: GET
        """
        path = "/rest/api/3/filter/search"
        params = {
            "filterName": filter_name,
            "accountId": account_id,
            "owner": owner,
            "groupname": groupname,
            "groupId": group_id,
            "projectId": project_id,
            "id": id_,
            "orderBy": order_by,
            "startAt": start_at,
            "maxResults": max_results,
            "expand": expand,
            "overrideSharePermissions": override_share_permissions,
            "isSubstringMatch": is_substring_match,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_filter(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete filter

        Path: /rest/api/3/filter/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/filter/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_filter(
        self,
        id_: int,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get filter

        Path: /rest/api/3/filter/{id}
        Method: GET
        """
        path = f"/rest/api/3/filter/{id_}"
        params = {
            "expand": expand,
            "overrideSharePermissions": override_share_permissions,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_filter(
        self,
        id_: int,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update filter

        Path: /rest/api/3/filter/{id}
        Method: PUT
        """
        path = f"/rest/api/3/filter/{id_}"
        params = {
            "expand": expand,
            "overrideSharePermissions": override_share_permissions,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_reset_columns(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset columns

        Path: /rest/api/3/filter/{id}/columns
        Method: DELETE
        """
        path = f"/rest/api/3/filter/{id_}/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_columns(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get columns

        Path: /rest/api/3/filter/{id}/columns
        Method: GET
        """
        path = f"/rest/api/3/filter/{id_}/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_columns(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set columns

        Path: /rest/api/3/filter/{id}/columns
        Method: PUT
        """
        path = f"/rest/api/3/filter/{id_}/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_favourite_for_filter(
        self,
        id_: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove filter as favorite

        Path: /rest/api/3/filter/{id}/favourite
        Method: DELETE
        """
        path = f"/rest/api/3/filter/{id_}/favourite"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_favourite_for_filter(
        self,
        id_: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add filter as favorite

        Path: /rest/api/3/filter/{id}/favourite
        Method: PUT
        """
        path = f"/rest/api/3/filter/{id_}/favourite"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_change_filter_owner(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Change filter owner

        Path: /rest/api/3/filter/{id}/owner
        Method: PUT
        """
        path = f"/rest/api/3/filter/{id_}/owner"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_share_permissions(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get share permissions

        Path: /rest/api/3/filter/{id}/permission
        Method: GET
        """
        path = f"/rest/api/3/filter/{id_}/permission"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_share_permission(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add share permission

        Path: /rest/api/3/filter/{id}/permission
        Method: POST
        """
        path = f"/rest/api/3/filter/{id_}/permission"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_share_permission(
        self,
        id_: int,
        permission_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete share permission

        Path: /rest/api/3/filter/{id}/permission/{permissionId}
        Method: DELETE
        """
        path = f"/rest/api/3/filter/{id_}/permission/{permission_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_share_permission(
        self,
        id_: int,
        permission_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get share permission

        Path: /rest/api/3/filter/{id}/permission/{permissionId}
        Method: GET
        """
        path = f"/rest/api/3/filter/{id_}/permission/{permission_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_pin_unpin_projects_async(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk pin or unpin issue panel to projects

        Path: /rest/api/3/forge/panel/action/bulk/async
        Method: POST
        """
        path = "/rest/api/3/forge/panel/action/bulk/async"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_group(
        self,
        groupname: str | None = None,
        group_id: str | None = None,
        swap_group: str | None = None,
        swap_group_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove group

        Path: /rest/api/3/group
        Method: DELETE
        """
        path = "/rest/api/3/group"
        params = {
            "groupname": groupname,
            "groupId": group_id,
            "swapGroup": swap_group,
            "swapGroupId": swap_group_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_group(
        self,
        groupname: str | None = None,
        group_id: str | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group

        Path: /rest/api/3/group
        Method: GET
        """
        path = "/rest/api/3/group"
        params = {
            "groupname": groupname,
            "groupId": group_id,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_group(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create group

        Path: /rest/api/3/group
        Method: POST
        """
        path = "/rest/api/3/group"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_get_groups(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        group_id: list[Any] | None = None,
        group_name: list[Any] | None = None,
        access_type: str | None = None,
        application_key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk get groups

        Path: /rest/api/3/group/bulk
        Method: GET
        """
        path = "/rest/api/3/group/bulk"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "groupId": group_id,
            "groupName": group_name,
            "accessType": access_type,
            "applicationKey": application_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_users_from_group(
        self,
        groupname: str | None = None,
        group_id: str | None = None,
        include_inactive_users: bool | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get users from group

        Path: /rest/api/3/group/member
        Method: GET
        """
        path = "/rest/api/3/group/member"
        params = {
            "groupname": groupname,
            "groupId": group_id,
            "includeInactiveUsers": include_inactive_users,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_user_from_group(
        self,
        account_id: str,
        groupname: str | None = None,
        group_id: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove user from group

        Path: /rest/api/3/group/user
        Method: DELETE
        """
        path = "/rest/api/3/group/user"
        params = {
            "groupname": groupname,
            "groupId": group_id,
            "username": username,
            "accountId": account_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_user_to_group(
        self,
        groupname: str | None = None,
        group_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add user to group

        Path: /rest/api/3/group/user
        Method: POST
        """
        path = "/rest/api/3/group/user"
        params = {
            "groupname": groupname,
            "groupId": group_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_groups(
        self,
        account_id: str | None = None,
        query: str | None = None,
        exclude: list[Any] | None = None,
        exclude_id: list[Any] | None = None,
        max_results: int | None = None,
        case_insensitive: bool | None = None,
        user_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find groups

        Path: /rest/api/3/groups/picker
        Method: GET
        """
        path = "/rest/api/3/groups/picker"
        params = {
            "accountId": account_id,
            "query": query,
            "exclude": exclude,
            "excludeId": exclude_id,
            "maxResults": max_results,
            "caseInsensitive": case_insensitive,
            "userName": user_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_users_and_groups(
        self,
        query: str,
        max_results: int | None = None,
        show_avatar: bool | None = None,
        field_id: str | None = None,
        project_id: list[Any] | None = None,
        issue_type_id: list[Any] | None = None,
        avatar_size: str | None = None,
        case_insensitive: bool | None = None,
        exclude_connect_addons: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users and groups

        Path: /rest/api/3/groupuserpicker
        Method: GET
        """
        path = "/rest/api/3/groupuserpicker"
        params = {
            "query": query,
            "maxResults": max_results,
            "showAvatar": show_avatar,
            "fieldId": field_id,
            "projectId": project_id,
            "issueTypeId": issue_type_id,
            "avatarSize": avatar_size,
            "caseInsensitive": case_insensitive,
            "excludeConnectAddons": exclude_connect_addons,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_license(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get license

        Path: /rest/api/3/instance/license
        Method: GET
        """
        path = "/rest/api/3/instance/license"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issue(
        self,
        update_history: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create issue

        Path: /rest/api/3/issue
        Method: POST
        """
        path = "/rest/api/3/issue"
        params = {
            "updateHistory": update_history,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_archive_issues_async(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Archive issue(s) by JQL

        Path: /rest/api/3/issue/archive
        Method: POST
        """
        path = "/rest/api/3/issue/archive"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_archive_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Archive issue(s) by issue ID/key

        Path: /rest/api/3/issue/archive
        Method: PUT
        """
        path = "/rest/api/3/issue/archive"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk create issue

        Path: /rest/api/3/issue/bulk
        Method: POST
        """
        path = "/rest/api/3/issue/bulk"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_fetch_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk fetch issues

        Path: /rest/api/3/issue/bulkfetch
        Method: POST
        """
        path = "/rest/api/3/issue/bulkfetch"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_create_issue_meta(
        self,
        project_ids: list[Any] | None = None,
        project_keys: list[Any] | None = None,
        issuetype_ids: list[Any] | None = None,
        issuetype_names: list[Any] | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get create issue metadata

        Path: /rest/api/3/issue/createmeta
        Method: GET
        """
        path = "/rest/api/3/issue/createmeta"
        params = {
            "projectIds": project_ids,
            "projectKeys": project_keys,
            "issuetypeIds": issuetype_ids,
            "issuetypeNames": issuetype_names,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_create_issue_meta_issue_types(
        self,
        project_id_or_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get create metadata issue types for a project

        Path: /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes
        Method: GET
        """
        path = f"/rest/api/3/issue/createmeta/{project_id_or_key}/issuetypes"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_create_issue_meta_issue_type_id(
        self,
        project_id_or_key: str,
        issue_type_id: str,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get create field metadata for a project and issue type id

        Path: /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}
        Method: GET
        """
        path = f"/rest/api/3/issue/createmeta/{project_id_or_key}/issuetypes/{issue_type_id}"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_limit_report(
        self,
        is_returning_keys: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue limit report

        Path: /rest/api/3/issue/limit/report
        Method: GET
        """
        path = "/rest/api/3/issue/limit/report"
        params = {
            "isReturningKeys": is_returning_keys,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_picker_resource(
        self,
        query: str | None = None,
        current_jql: str | None = None,
        current_issue_key: str | None = None,
        current_project_id: str | None = None,
        show_sub_tasks: bool | None = None,
        show_sub_task_parent: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue picker suggestions

        Path: /rest/api/3/issue/picker
        Method: GET
        """
        path = "/rest/api/3/issue/picker"
        params = {
            "query": query,
            "currentJQL": current_jql,
            "currentIssueKey": current_issue_key,
            "currentProjectId": current_project_id,
            "showSubTasks": show_sub_tasks,
            "showSubTaskParent": show_sub_task_parent,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_set_issues_properties_list(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk set issues properties by list

        Path: /rest/api/3/issue/properties
        Method: POST
        """
        path = "/rest/api/3/issue/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_set_issue_properties_by_issue(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk set issue properties by issue

        Path: /rest/api/3/issue/properties/multi
        Method: POST
        """
        path = "/rest/api/3/issue/properties/multi"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_delete_issue_property(
        self,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk delete issue property

        Path: /rest/api/3/issue/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/api/3/issue/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_set_issue_property(
        self,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk set issue property

        Path: /rest/api/3/issue/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/api/3/issue/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_unarchive_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Unarchive issue(s) by issue keys/ID

        Path: /rest/api/3/issue/unarchive
        Method: PUT
        """
        path = "/rest/api/3/issue/unarchive"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_is_watching_issue_bulk(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get is watching issue bulk

        Path: /rest/api/3/issue/watching
        Method: POST
        """
        path = "/rest/api/3/issue/watching"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue(
        self,
        issue_id_or_key: str,
        delete_subtasks: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue

        Path: /rest/api/3/issue/{issueIdOrKey}
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}"
        params = {
            "deleteSubtasks": delete_subtasks,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue(
        self,
        issue_id_or_key: str,
        fields: list[Any] | None = None,
        fields_by_keys: bool | None = None,
        expand: str | None = None,
        properties: list[Any] | None = None,
        update_history: bool | None = None,
        fail_fast: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue

        Path: /rest/api/3/issue/{issueIdOrKey}
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}"
        params = {
            "fields": fields,
            "fieldsByKeys": fields_by_keys,
            "expand": expand,
            "properties": properties,
            "updateHistory": update_history,
            "failFast": fail_fast,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_edit_issue(
        self,
        issue_id_or_key: str,
        notify_users: bool | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        return_issue: bool | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Edit issue

        Path: /rest/api/3/issue/{issueIdOrKey}
        Method: PUT
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}"
        params = {
            "notifyUsers": notify_users,
            "overrideScreenSecurity": override_screen_security,
            "overrideEditableFlag": override_editable_flag,
            "returnIssue": return_issue,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_assign_issue(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign issue

        Path: /rest/api/3/issue/{issueIdOrKey}/assignee
        Method: PUT
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/assignee"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_attachment(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add attachment

        Path: /rest/api/3/issue/{issueIdOrKey}/attachments
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/attachments"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_change_logs(
        self,
        issue_id_or_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get changelogs

        Path: /rest/api/3/issue/{issueIdOrKey}/changelog
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/changelog"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_change_logs_by_ids(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get changelogs by IDs

        Path: /rest/api/3/issue/{issueIdOrKey}/changelog/list
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/changelog/list"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_comments(
        self,
        issue_id_or_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get comments

        Path: /rest/api/3/issue/{issueIdOrKey}/comment
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/comment"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_comment(
        self,
        issue_id_or_key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add comment

        Path: /rest/api/3/issue/{issueIdOrKey}/comment
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/comment"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_comment(
        self,
        issue_id_or_key: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete comment

        Path: /rest/api/3/issue/{issueIdOrKey}/comment/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_comment(
        self,
        issue_id_or_key: str,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get comment

        Path: /rest/api/3/issue/{issueIdOrKey}/comment/{id}
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_comment(
        self,
        issue_id_or_key: str,
        id_: str,
        notify_users: bool | None = None,
        override_editable_flag: bool | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update comment

        Path: /rest/api/3/issue/{issueIdOrKey}/comment/{id}
        Method: PUT
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}"
        params = {
            "notifyUsers": notify_users,
            "overrideEditableFlag": override_editable_flag,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_edit_issue_meta(
        self,
        issue_id_or_key: str,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get edit issue metadata

        Path: /rest/api/3/issue/{issueIdOrKey}/editmeta
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/editmeta"
        params = {
            "overrideScreenSecurity": override_screen_security,
            "overrideEditableFlag": override_editable_flag,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_notify(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Send notification for issue

        Path: /rest/api/3/issue/{issueIdOrKey}/notify
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/notify"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_property_keys(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue property keys

        Path: /rest/api/3/issue/{issueIdOrKey}/properties
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue_property(
        self,
        issue_id_or_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue property

        Path: /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_property(
        self,
        issue_id_or_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue property

        Path: /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_issue_property(
        self,
        issue_id_or_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set issue property

        Path: /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_remote_issue_link_by_global_id(
        self,
        issue_id_or_key: str,
        global_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete remote issue link by global ID

        Path: /rest/api/3/issue/{issueIdOrKey}/remotelink
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/remotelink"
        params = {
            "globalId": global_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_remote_issue_links(
        self,
        issue_id_or_key: str,
        global_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get remote issue links

        Path: /rest/api/3/issue/{issueIdOrKey}/remotelink
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/remotelink"
        params = {
            "globalId": global_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_or_update_remote_issue_link(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create or update remote issue link

        Path: /rest/api/3/issue/{issueIdOrKey}/remotelink
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/remotelink"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_remote_issue_link_by_id(
        self,
        issue_id_or_key: str,
        link_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete remote issue link by ID

        Path: /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_remote_issue_link_by_id(
        self,
        issue_id_or_key: str,
        link_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get remote issue link by ID

        Path: /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_remote_issue_link(
        self,
        issue_id_or_key: str,
        link_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update remote issue link by ID

        Path: /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}
        Method: PUT
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_transitions(
        self,
        issue_id_or_key: str,
        expand: str | None = None,
        transition_id: str | None = None,
        skip_remote_only_condition: bool | None = None,
        include_unavailable_transitions: bool | None = None,
        sort_by_ops_bar_and_status: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get transitions

        Path: /rest/api/3/issue/{issueIdOrKey}/transitions
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/transitions"
        params = {
            "expand": expand,
            "transitionId": transition_id,
            "skipRemoteOnlyCondition": skip_remote_only_condition,
            "includeUnavailableTransitions": include_unavailable_transitions,
            "sortByOpsBarAndStatus": sort_by_ops_bar_and_status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_do_transition(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Transition issue

        Path: /rest/api/3/issue/{issueIdOrKey}/transitions
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/transitions"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_vote(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete vote

        Path: /rest/api/3/issue/{issueIdOrKey}/votes
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/votes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_votes(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get votes

        Path: /rest/api/3/issue/{issueIdOrKey}/votes
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/votes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_vote(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add vote

        Path: /rest/api/3/issue/{issueIdOrKey}/votes
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/votes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_watcher(
        self,
        issue_id_or_key: str,
        username: str | None = None,
        account_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete watcher

        Path: /rest/api/3/issue/{issueIdOrKey}/watchers
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/watchers"
        params = {
            "username": username,
            "accountId": account_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_watchers(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue watchers

        Path: /rest/api/3/issue/{issueIdOrKey}/watchers
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/watchers"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_watcher(
        self,
        issue_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add watcher

        Path: /rest/api/3/issue/{issueIdOrKey}/watchers
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/watchers"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_delete_worklogs(
        self,
        issue_id_or_key: str,
        adjust_estimate: str | None = None,
        override_editable_flag: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk delete worklogs

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog"
        params = {
            "adjustEstimate": adjust_estimate,
            "overrideEditableFlag": override_editable_flag,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_worklog(
        self,
        issue_id_or_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        started_after: int | None = None,
        started_before: int | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue worklogs

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "startedAfter": started_after,
            "startedBefore": started_before,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_worklog(
        self,
        issue_id_or_key: str,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        reduce_by: str | None = None,
        expand: str | None = None,
        override_editable_flag: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add worklog

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog"
        params = {
            "notifyUsers": notify_users,
            "adjustEstimate": adjust_estimate,
            "newEstimate": new_estimate,
            "reduceBy": reduce_by,
            "expand": expand,
            "overrideEditableFlag": override_editable_flag,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_move_worklogs(
        self,
        issue_id_or_key: str,
        adjust_estimate: str | None = None,
        override_editable_flag: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk move worklogs

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog/move
        Method: POST
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog/move"
        params = {
            "adjustEstimate": adjust_estimate,
            "overrideEditableFlag": override_editable_flag,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_worklog(
        self,
        issue_id_or_key: str,
        id_: str,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        increase_by: str | None = None,
        override_editable_flag: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete worklog

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}"
        params = {
            "notifyUsers": notify_users,
            "adjustEstimate": adjust_estimate,
            "newEstimate": new_estimate,
            "increaseBy": increase_by,
            "overrideEditableFlag": override_editable_flag,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_worklog(
        self,
        issue_id_or_key: str,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get worklog

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog/{id}
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_worklog(
        self,
        issue_id_or_key: str,
        id_: str,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        expand: str | None = None,
        override_editable_flag: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update worklog

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog/{id}
        Method: PUT
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}"
        params = {
            "notifyUsers": notify_users,
            "adjustEstimate": adjust_estimate,
            "newEstimate": new_estimate,
            "expand": expand,
            "overrideEditableFlag": override_editable_flag,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_worklog_property_keys(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get worklog property keys

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_worklog_property(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete worklog property

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_worklog_property(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get worklog property

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_worklog_property(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set worklog property

        Path: /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_link_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create issue link

        Path: /rest/api/3/issueLink
        Method: POST
        """
        path = "/rest/api/3/issueLink"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue_link(
        self,
        link_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue link

        Path: /rest/api/3/issueLink/{linkId}
        Method: DELETE
        """
        path = f"/rest/api/3/issueLink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_link(
        self,
        link_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue link

        Path: /rest/api/3/issueLink/{linkId}
        Method: GET
        """
        path = f"/rest/api/3/issueLink/{link_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_link_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get issue link types

        Path: /rest/api/3/issueLinkType
        Method: GET
        """
        path = "/rest/api/3/issueLinkType"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issue_link_type(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create issue link type

        Path: /rest/api/3/issueLinkType
        Method: POST
        """
        path = "/rest/api/3/issueLinkType"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue_link_type(
        self,
        issue_link_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue link type

        Path: /rest/api/3/issueLinkType/{issueLinkTypeId}
        Method: DELETE
        """
        path = f"/rest/api/3/issueLinkType/{issue_link_type_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_link_type(
        self,
        issue_link_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue link type

        Path: /rest/api/3/issueLinkType/{issueLinkTypeId}
        Method: GET
        """
        path = f"/rest/api/3/issueLinkType/{issue_link_type_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_issue_link_type(
        self,
        issue_link_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update issue link type

        Path: /rest/api/3/issueLinkType/{issueLinkTypeId}
        Method: PUT
        """
        path = f"/rest/api/3/issueLinkType/{issue_link_type_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_export_archived_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Export archived issue(s)

        Path: /rest/api/3/issues/archive/export
        Method: PUT
        """
        path = "/rest/api/3/issues/archive/export"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_security_schemes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get issue security schemes

        Path: /rest/api/3/issuesecurityschemes
        Method: GET
        """
        path = "/rest/api/3/issuesecurityschemes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issue_security_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create issue security scheme

        Path: /rest/api/3/issuesecurityschemes
        Method: POST
        """
        path = "/rest/api/3/issuesecurityschemes"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_security_levels(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[Any] | None = None,
        scheme_id: list[Any] | None = None,
        only_default: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue security levels

        Path: /rest/api/3/issuesecurityschemes/level
        Method: GET
        """
        path = "/rest/api/3/issuesecurityschemes/level"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "schemeId": scheme_id,
            "onlyDefault": only_default,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_default_levels(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set default issue security levels

        Path: /rest/api/3/issuesecurityschemes/level/default
        Method: PUT
        """
        path = "/rest/api/3/issuesecurityschemes/level/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_security_level_members(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[Any] | None = None,
        scheme_id: list[Any] | None = None,
        level_id: list[Any] | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue security level members

        Path: /rest/api/3/issuesecurityschemes/level/member
        Method: GET
        """
        path = "/rest/api/3/issuesecurityschemes/level/member"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "schemeId": scheme_id,
            "levelId": level_id,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_projects_using_security_schemes(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        issue_security_scheme_id: list[Any] | None = None,
        project_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get projects using issue security schemes

        Path: /rest/api/3/issuesecurityschemes/project
        Method: GET
        """
        path = "/rest/api/3/issuesecurityschemes/project"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "issueSecuritySchemeId": issue_security_scheme_id,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_associate_schemes_to_projects(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Associate security scheme to project

        Path: /rest/api/3/issuesecurityschemes/project
        Method: PUT
        """
        path = "/rest/api/3/issuesecurityschemes/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_security_schemes(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[Any] | None = None,
        project_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search issue security schemes

        Path: /rest/api/3/issuesecurityschemes/search
        Method: GET
        """
        path = "/rest/api/3/issuesecurityschemes/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_security_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue security scheme

        Path: /rest/api/3/issuesecurityschemes/{id}
        Method: GET
        """
        path = f"/rest/api/3/issuesecurityschemes/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_issue_security_scheme(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update issue security scheme

        Path: /rest/api/3/issuesecurityschemes/{id}
        Method: PUT
        """
        path = f"/rest/api/3/issuesecurityschemes/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_security_level_members(
        self,
        issue_security_scheme_id: int,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_security_level_id: list[Any] | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue security level members by issue security scheme

        Path: /rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members
        Method: GET
        """
        path = f"/rest/api/3/issuesecurityschemes/{issue_security_scheme_id}/members"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "issueSecurityLevelId": issue_security_level_id,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_security_scheme(
        self,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue security scheme

        Path: /rest/api/3/issuesecurityschemes/{schemeId}
        Method: DELETE
        """
        path = f"/rest/api/3/issuesecurityschemes/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_security_level(
        self,
        scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add issue security levels

        Path: /rest/api/3/issuesecurityschemes/{schemeId}/level
        Method: PUT
        """
        path = f"/rest/api/3/issuesecurityschemes/{scheme_id}/level"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_level(
        self,
        scheme_id: str,
        level_id: str,
        replace_with: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove issue security level

        Path: /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}
        Method: DELETE
        """
        path = f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}"
        params = {
            "replaceWith": replace_with,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_security_level(
        self,
        scheme_id: str,
        level_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update issue security level

        Path: /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}
        Method: PUT
        """
        path = f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_security_level_members(
        self,
        scheme_id: str,
        level_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add issue security level members

        Path: /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member
        Method: PUT
        """
        path = f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_member_from_security_level(
        self,
        scheme_id: str,
        level_id: str,
        member_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove member from issue security level

        Path: /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}
        Method: DELETE
        """
        path = f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member/{member_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_all_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all issue types for user

        Path: /rest/api/3/issuetype
        Method: GET
        """
        path = "/rest/api/3/issuetype"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issue_type(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create issue type

        Path: /rest/api/3/issuetype
        Method: POST
        """
        path = "/rest/api/3/issuetype"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_types_for_project(
        self,
        project_id: int,
        level: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue types for project

        Path: /rest/api/3/issuetype/project
        Method: GET
        """
        path = "/rest/api/3/issuetype/project"
        params = {
            "projectId": project_id,
            "level": level,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue_type(
        self,
        id_: str,
        alternative_issue_type_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue type

        Path: /rest/api/3/issuetype/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/issuetype/{id_}"
        params = {
            "alternativeIssueTypeId": alternative_issue_type_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type

        Path: /rest/api/3/issuetype/{id}
        Method: GET
        """
        path = f"/rest/api/3/issuetype/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_issue_type(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update issue type

        Path: /rest/api/3/issuetype/{id}
        Method: PUT
        """
        path = f"/rest/api/3/issuetype/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_alternative_issue_types(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get alternative issue types

        Path: /rest/api/3/issuetype/{id}/alternatives
        Method: GET
        """
        path = f"/rest/api/3/issuetype/{id_}/alternatives"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issue_type_avatar(
        self,
        id_: str,
        size: int,
        x: int | None = None,
        y: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Load issue type avatar

        Path: /rest/api/3/issuetype/{id}/avatar2
        Method: POST
        """
        path = f"/rest/api/3/issuetype/{id_}/avatar2"
        params = {
            "x": x,
            "y": y,
            "size": size,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type_property_keys(
        self,
        issue_type_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type property keys

        Path: /rest/api/3/issuetype/{issueTypeId}/properties
        Method: GET
        """
        path = f"/rest/api/3/issuetype/{issue_type_id}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue_type_property(
        self,
        issue_type_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue type property

        Path: /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type_property(
        self,
        issue_type_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type property

        Path: /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_issue_type_property(
        self,
        issue_type_id: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set issue type property

        Path: /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_issue_type_schemes(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[Any] | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all issue type schemes

        Path: /rest/api/3/issuetypescheme
        Method: GET
        """
        path = "/rest/api/3/issuetypescheme"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "orderBy": order_by,
            "expand": expand,
            "queryString": query_string,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issue_type_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create issue type scheme

        Path: /rest/api/3/issuetypescheme
        Method: POST
        """
        path = "/rest/api/3/issuetypescheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type_schemes_mapping(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_type_scheme_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type scheme items

        Path: /rest/api/3/issuetypescheme/mapping
        Method: GET
        """
        path = "/rest/api/3/issuetypescheme/mapping"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "issueTypeSchemeId": issue_type_scheme_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type_scheme_for_projects(
        self,
        project_id: list[Any],
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type schemes for projects

        Path: /rest/api/3/issuetypescheme/project
        Method: GET
        """
        path = "/rest/api/3/issuetypescheme/project"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_assign_issue_type_scheme_to_project(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Assign issue type scheme to project

        Path: /rest/api/3/issuetypescheme/project
        Method: PUT
        """
        path = "/rest/api/3/issuetypescheme/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue type scheme

        Path: /rest/api/3/issuetypescheme/{issueTypeSchemeId}
        Method: DELETE
        """
        path = f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update issue type scheme

        Path: /rest/api/3/issuetypescheme/{issueTypeSchemeId}
        Method: PUT
        """
        path = f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_issue_types_to_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add issue types to issue type scheme

        Path: /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype
        Method: PUT
        """
        path = f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_reorder_issue_types_in_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Change order of issue types

        Path: /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move
        Method: PUT
        """
        path = f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_issue_type_from_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove issue type from issue type scheme

        Path: /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}
        Method: DELETE
        """
        path = f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/{issue_type_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type_screen_schemes(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[Any] | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type screen schemes

        Path: /rest/api/3/issuetypescreenscheme
        Method: GET
        """
        path = "/rest/api/3/issuetypescreenscheme"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "queryString": query_string,
            "orderBy": order_by,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_issue_type_screen_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create issue type screen scheme

        Path: /rest/api/3/issuetypescreenscheme
        Method: POST
        """
        path = "/rest/api/3/issuetypescreenscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type_screen_scheme_mappings(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_type_screen_scheme_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type screen scheme items

        Path: /rest/api/3/issuetypescreenscheme/mapping
        Method: GET
        """
        path = "/rest/api/3/issuetypescreenscheme/mapping"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "issueTypeScreenSchemeId": issue_type_screen_scheme_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_type_screen_scheme_project_associations(
        self,
        project_id: list[Any],
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type screen schemes for projects

        Path: /rest/api/3/issuetypescreenscheme/project
        Method: GET
        """
        path = "/rest/api/3/issuetypescreenscheme/project"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_assign_issue_type_screen_scheme_to_project(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Assign issue type screen scheme to project

        Path: /rest/api/3/issuetypescreenscheme/project
        Method: PUT
        """
        path = "/rest/api/3/issuetypescreenscheme/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue type screen scheme

        Path: /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}
        Method: DELETE
        """
        path = f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update issue type screen scheme

        Path: /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}
        Method: PUT
        """
        path = f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_append_mappings_for_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Append mappings to issue type screen scheme

        Path: /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping
        Method: PUT
        """
        path = (
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping"
        )
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_default_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update issue type screen scheme default screen scheme

        Path: /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default
        Method: PUT
        """
        path = f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_mappings_from_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove mappings from issue type screen scheme

        Path: /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove
        Method: POST
        """
        path = f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping/remove"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_projects_for_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: int,
        start_at: int | None = None,
        max_results: int | None = None,
        query: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type screen scheme projects

        Path: /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project
        Method: GET
        """
        path = (
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/project"
        )
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "query": query,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_auto_complete(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get field reference data (GET)

        Path: /rest/api/3/jql/autocompletedata
        Method: GET
        """
        path = "/rest/api/3/jql/autocompletedata"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_auto_complete_post(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get field reference data (POST)

        Path: /rest/api/3/jql/autocompletedata
        Method: POST
        """
        path = "/rest/api/3/jql/autocompletedata"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_field_auto_complete_for_query_string(
        self,
        field_name: str | None = None,
        field_value: str | None = None,
        predicate_name: str | None = None,
        predicate_value: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get field auto complete suggestions

        Path: /rest/api/3/jql/autocompletedata/suggestions
        Method: GET
        """
        path = "/rest/api/3/jql/autocompletedata/suggestions"
        params = {
            "fieldName": field_name,
            "fieldValue": field_value,
            "predicateName": predicate_name,
            "predicateValue": predicate_value,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_precomputations(
        self,
        function_key: list[Any] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get precomputations (apps)

        Path: /rest/api/3/jql/function/computation
        Method: GET
        """
        path = "/rest/api/3/jql/function/computation"
        params = {
            "functionKey": function_key,
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_precomputations(
        self,
        skip_not_found_precomputations: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update precomputations (apps)

        Path: /rest/api/3/jql/function/computation
        Method: POST
        """
        path = "/rest/api/3/jql/function/computation"
        params = {
            "skipNotFoundPrecomputations": skip_not_found_precomputations,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_precomputations_by_id(
        self,
        order_by: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get precomputations by ID (apps)

        Path: /rest/api/3/jql/function/computation/search
        Method: POST
        """
        path = "/rest/api/3/jql/function/computation/search"
        params = {
            "orderBy": order_by,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_match_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Check issues against JQL

        Path: /rest/api/3/jql/match
        Method: POST
        """
        path = "/rest/api/3/jql/match"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_parse_jql_queries(
        self,
        validation: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Parse JQL query

        Path: /rest/api/3/jql/parse
        Method: POST
        """
        path = "/rest/api/3/jql/parse"
        params = {
            "validation": validation,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_migrate_queries(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Convert user identifiers to account IDs in JQL queries

        Path: /rest/api/3/jql/pdcleaner
        Method: POST
        """
        path = "/rest/api/3/jql/pdcleaner"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_sanitise_jql_queries(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Sanitize JQL queries

        Path: /rest/api/3/jql/sanitize
        Method: POST
        """
        path = "/rest/api/3/jql/sanitize"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_labels(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all labels

        Path: /rest/api/3/label
        Method: GET
        """
        path = "/rest/api/3/label"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_approximate_license_count(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get approximate license count

        Path: /rest/api/3/license/approximateLicenseCount
        Method: GET
        """
        path = "/rest/api/3/license/approximateLicenseCount"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_approximate_application_license_count(
        self,
        application_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get approximate application license count

        Path: /rest/api/3/license/approximateLicenseCount/product/{applicationKey}
        Method: GET
        """
        path = f"/rest/api/3/license/approximateLicenseCount/product/{application_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_my_permissions(
        self,
        project_key: str | None = None,
        project_id: str | None = None,
        issue_key: str | None = None,
        issue_id: str | None = None,
        permissions: str | None = None,
        project_uuid: str | None = None,
        project_configuration_uuid: str | None = None,
        comment_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get my permissions

        Path: /rest/api/3/mypermissions
        Method: GET
        """
        path = "/rest/api/3/mypermissions"
        params = {
            "projectKey": project_key,
            "projectId": project_id,
            "issueKey": issue_key,
            "issueId": issue_id,
            "permissions": permissions,
            "projectUuid": project_uuid,
            "projectConfigurationUuid": project_configuration_uuid,
            "commentId": comment_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_preference(
        self,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete preference

        Path: /rest/api/3/mypreferences
        Method: DELETE
        """
        path = "/rest/api/3/mypreferences"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_preference(
        self,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get preference

        Path: /rest/api/3/mypreferences
        Method: GET
        """
        path = "/rest/api/3/mypreferences"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_preference(
        self,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set preference

        Path: /rest/api/3/mypreferences
        Method: PUT
        """
        path = "/rest/api/3/mypreferences"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_locale(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get locale

        Path: /rest/api/3/mypreferences/locale
        Method: GET
        """
        path = "/rest/api/3/mypreferences/locale"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_locale(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set locale

        Path: /rest/api/3/mypreferences/locale
        Method: PUT
        """
        path = "/rest/api/3/mypreferences/locale"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_current_user(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get current user

        Path: /rest/api/3/myself
        Method: GET
        """
        path = "/rest/api/3/myself"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_notification_schemes(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[Any] | None = None,
        project_id: list[Any] | None = None,
        only_default: bool | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get notification schemes paginated

        Path: /rest/api/3/notificationscheme
        Method: GET
        """
        path = "/rest/api/3/notificationscheme"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "projectId": project_id,
            "onlyDefault": only_default,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_notification_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create notification scheme

        Path: /rest/api/3/notificationscheme
        Method: POST
        """
        path = "/rest/api/3/notificationscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_notification_scheme_to_project_mappings(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        notification_scheme_id: list[Any] | None = None,
        project_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get projects using notification schemes paginated

        Path: /rest/api/3/notificationscheme/project
        Method: GET
        """
        path = "/rest/api/3/notificationscheme/project"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "notificationSchemeId": notification_scheme_id,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_notification_scheme(
        self,
        id_: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get notification scheme

        Path: /rest/api/3/notificationscheme/{id}
        Method: GET
        """
        path = f"/rest/api/3/notificationscheme/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_notification_scheme(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update notification scheme

        Path: /rest/api/3/notificationscheme/{id}
        Method: PUT
        """
        path = f"/rest/api/3/notificationscheme/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_notifications(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add notifications to notification scheme

        Path: /rest/api/3/notificationscheme/{id}/notification
        Method: PUT
        """
        path = f"/rest/api/3/notificationscheme/{id_}/notification"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_notification_scheme(
        self,
        notification_scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete notification scheme

        Path: /rest/api/3/notificationscheme/{notificationSchemeId}
        Method: DELETE
        """
        path = f"/rest/api/3/notificationscheme/{notification_scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_notification_from_notification_scheme(
        self,
        notification_scheme_id: str,
        notification_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove notification from notification scheme

        Path: /rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}
        Method: DELETE
        """
        path = f"/rest/api/3/notificationscheme/{notification_scheme_id}/notification/{notification_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_permissions(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all permissions

        Path: /rest/api/3/permissions
        Method: GET
        """
        path = "/rest/api/3/permissions"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_bulk_permissions(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get bulk permissions

        Path: /rest/api/3/permissions/check
        Method: POST
        """
        path = "/rest/api/3/permissions/check"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_permitted_projects(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get permitted projects

        Path: /rest/api/3/permissions/project
        Method: POST
        """
        path = "/rest/api/3/permissions/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_permission_schemes(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all permission schemes

        Path: /rest/api/3/permissionscheme
        Method: GET
        """
        path = "/rest/api/3/permissionscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_permission_scheme(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create permission scheme

        Path: /rest/api/3/permissionscheme
        Method: POST
        """
        path = "/rest/api/3/permissionscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_permission_scheme(
        self,
        scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete permission scheme

        Path: /rest/api/3/permissionscheme/{schemeId}
        Method: DELETE
        """
        path = f"/rest/api/3/permissionscheme/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_permission_scheme(
        self,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permission scheme

        Path: /rest/api/3/permissionscheme/{schemeId}
        Method: GET
        """
        path = f"/rest/api/3/permissionscheme/{scheme_id}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_permission_scheme(
        self,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update permission scheme

        Path: /rest/api/3/permissionscheme/{schemeId}
        Method: PUT
        """
        path = f"/rest/api/3/permissionscheme/{scheme_id}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_permission_scheme_grants(
        self,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permission scheme grants

        Path: /rest/api/3/permissionscheme/{schemeId}/permission
        Method: GET
        """
        path = f"/rest/api/3/permissionscheme/{scheme_id}/permission"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_permission_grant(
        self,
        scheme_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create permission grant

        Path: /rest/api/3/permissionscheme/{schemeId}/permission
        Method: POST
        """
        path = f"/rest/api/3/permissionscheme/{scheme_id}/permission"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_permission_scheme_entity(
        self,
        scheme_id: int,
        permission_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete permission scheme grant

        Path: /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}
        Method: DELETE
        """
        path = f"/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_permission_scheme_grant(
        self,
        scheme_id: int,
        permission_id: int,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get permission scheme grant

        Path: /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}
        Method: GET
        """
        path = f"/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_plans(
        self,
        include_trashed: bool | None = None,
        include_archived: bool | None = None,
        cursor: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get plans paginated

        Path: /rest/api/3/plans/plan
        Method: GET
        """
        path = "/rest/api/3/plans/plan"
        params = {
            "includeTrashed": include_trashed,
            "includeArchived": include_archived,
            "cursor": cursor,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_plan(
        self,
        use_group_id: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create plan

        Path: /rest/api/3/plans/plan
        Method: POST
        """
        path = "/rest/api/3/plans/plan"
        params = {
            "useGroupId": use_group_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_plan(
        self,
        plan_id: int,
        use_group_id: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get plan

        Path: /rest/api/3/plans/plan/{planId}
        Method: GET
        """
        path = f"/rest/api/3/plans/plan/{plan_id}"
        params = {
            "useGroupId": use_group_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_plan(
        self,
        plan_id: int,
        use_group_id: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update plan

        Path: /rest/api/3/plans/plan/{planId}
        Method: PUT
        """
        path = f"/rest/api/3/plans/plan/{plan_id}"
        params = {
            "useGroupId": use_group_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_archive_plan(
        self,
        plan_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Archive plan

        Path: /rest/api/3/plans/plan/{planId}/archive
        Method: PUT
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/archive"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_duplicate_plan(
        self,
        plan_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Duplicate plan

        Path: /rest/api/3/plans/plan/{planId}/duplicate
        Method: POST
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/duplicate"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_teams(
        self,
        plan_id: int,
        cursor: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get teams in plan paginated

        Path: /rest/api/3/plans/plan/{planId}/team
        Method: GET
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team"
        params = {
            "cursor": cursor,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_atlassian_team(
        self,
        plan_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add Atlassian team to plan

        Path: /rest/api/3/plans/plan/{planId}/team/atlassian
        Method: POST
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team/atlassian"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_atlassian_team(
        self,
        plan_id: int,
        atlassian_team_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove Atlassian team from plan

        Path: /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}
        Method: DELETE
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_atlassian_team(
        self,
        plan_id: int,
        atlassian_team_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get Atlassian team in plan

        Path: /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}
        Method: GET
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_atlassian_team(
        self,
        plan_id: int,
        atlassian_team_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update Atlassian team in plan

        Path: /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}
        Method: PUT
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_plan_only_team(
        self,
        plan_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create plan-only team

        Path: /rest/api/3/plans/plan/{planId}/team/planonly
        Method: POST
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team/planonly"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_plan_only_team(
        self,
        plan_id: int,
        plan_only_team_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete plan-only team

        Path: /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}
        Method: DELETE
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_plan_only_team(
        self,
        plan_id: int,
        plan_only_team_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get plan-only team

        Path: /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}
        Method: GET
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_plan_only_team(
        self,
        plan_id: int,
        plan_only_team_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update plan-only team

        Path: /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}
        Method: PUT
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_trash_plan(
        self,
        plan_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Trash plan

        Path: /rest/api/3/plans/plan/{planId}/trash
        Method: PUT
        """
        path = f"/rest/api/3/plans/plan/{plan_id}/trash"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_priorities(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get priorities

        Path: /rest/api/3/priority
        Method: GET
        """
        path = "/rest/api/3/priority"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_priority(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create priority

        Path: /rest/api/3/priority
        Method: POST
        """
        path = "/rest/api/3/priority"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_default_priority(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set default priority

        Path: /rest/api/3/priority/default
        Method: PUT
        """
        path = "/rest/api/3/priority/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_move_priorities(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Move priorities

        Path: /rest/api/3/priority/move
        Method: PUT
        """
        path = "/rest/api/3/priority/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_priorities(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[Any] | None = None,
        project_id: list[Any] | None = None,
        priority_name: str | None = None,
        only_default: bool | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search priorities

        Path: /rest/api/3/priority/search
        Method: GET
        """
        path = "/rest/api/3/priority/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "projectId": project_id,
            "priorityName": priority_name,
            "onlyDefault": only_default,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_priority(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete priority

        Path: /rest/api/3/priority/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/priority/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_priority(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get priority

        Path: /rest/api/3/priority/{id}
        Method: GET
        """
        path = f"/rest/api/3/priority/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_priority(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update priority

        Path: /rest/api/3/priority/{id}
        Method: PUT
        """
        path = f"/rest/api/3/priority/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_priority_schemes(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        priority_id: list[Any] | None = None,
        scheme_id: list[Any] | None = None,
        scheme_name: str | None = None,
        only_default: bool | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get priority schemes

        Path: /rest/api/3/priorityscheme
        Method: GET
        """
        path = "/rest/api/3/priorityscheme"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "priorityId": priority_id,
            "schemeId": scheme_id,
            "schemeName": scheme_name,
            "onlyDefault": only_default,
            "orderBy": order_by,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_priority_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create priority scheme

        Path: /rest/api/3/priorityscheme
        Method: POST
        """
        path = "/rest/api/3/priorityscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_suggested_priorities_for_mappings(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Suggested priorities for mappings

        Path: /rest/api/3/priorityscheme/mappings
        Method: POST
        """
        path = "/rest/api/3/priorityscheme/mappings"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_available_priorities_by_priority_scheme(
        self,
        scheme_id: str,
        start_at: str | None = None,
        max_results: str | None = None,
        query: str | None = None,
        exclude: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get available priorities by priority scheme

        Path: /rest/api/3/priorityscheme/priorities/available
        Method: GET
        """
        path = "/rest/api/3/priorityscheme/priorities/available"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "query": query,
            "schemeId": scheme_id,
            "exclude": exclude,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_priority_scheme(
        self,
        scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete priority scheme

        Path: /rest/api/3/priorityscheme/{schemeId}
        Method: DELETE
        """
        path = f"/rest/api/3/priorityscheme/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_priority_scheme(
        self,
        scheme_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update priority scheme

        Path: /rest/api/3/priorityscheme/{schemeId}
        Method: PUT
        """
        path = f"/rest/api/3/priorityscheme/{scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_priorities_by_priority_scheme(
        self,
        scheme_id: str,
        start_at: str | None = None,
        max_results: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get priorities by priority scheme

        Path: /rest/api/3/priorityscheme/{schemeId}/priorities
        Method: GET
        """
        path = f"/rest/api/3/priorityscheme/{scheme_id}/priorities"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_projects_by_priority_scheme(
        self,
        scheme_id: str,
        start_at: str | None = None,
        max_results: str | None = None,
        project_id: list[Any] | None = None,
        query: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get projects by priority scheme

        Path: /rest/api/3/priorityscheme/{schemeId}/projects
        Method: GET
        """
        path = f"/rest/api/3/priorityscheme/{scheme_id}/projects"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
            "query": query,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_projects(
        self,
        expand: str | None = None,
        recent: int | None = None,
        properties: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all projects

        Path: /rest/api/3/project
        Method: GET
        """
        path = "/rest/api/3/project"
        params = {
            "expand": expand,
            "recent": recent,
            "properties": properties,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_project(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create project

        Path: /rest/api/3/project
        Method: POST
        """
        path = "/rest/api/3/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_project_with_custom_template(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create custom project

        Path: /rest/api/3/project-template
        Method: POST
        """
        path = "/rest/api/3/project-template"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_edit_template(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Edit a custom project template

        Path: /rest/api/3/project-template/edit-template
        Method: PUT
        """
        path = "/rest/api/3/project-template/edit-template"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_live_template(
        self,
        project_id: str | None = None,
        template_key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Gets a custom project template

        Path: /rest/api/3/project-template/live-template
        Method: GET
        """
        path = "/rest/api/3/project-template/live-template"
        params = {
            "projectId": project_id,
            "templateKey": template_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_template(
        self,
        template_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Deletes a custom project template

        Path: /rest/api/3/project-template/remove-template
        Method: DELETE
        """
        path = "/rest/api/3/project-template/remove-template"
        params = {
            "templateKey": template_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_save_template(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Save a custom project template

        Path: /rest/api/3/project-template/save-template
        Method: POST
        """
        path = "/rest/api/3/project-template/save-template"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_recent(
        self,
        expand: str | None = None,
        properties: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get recent projects

        Path: /rest/api/3/project/recent
        Method: GET
        """
        path = "/rest/api/3/project/recent"
        params = {
            "expand": expand,
            "properties": properties,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_projects(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        id_: list[Any] | None = None,
        keys: list[Any] | None = None,
        query: str | None = None,
        type_key: str | None = None,
        category_id: int | None = None,
        action: str | None = None,
        expand: str | None = None,
        status: list[Any] | None = None,
        properties: list[Any] | None = None,
        property_query: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get projects paginated

        Path: /rest/api/3/project/search
        Method: GET
        """
        path = "/rest/api/3/project/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "id": id_,
            "keys": keys,
            "query": query,
            "typeKey": type_key,
            "categoryId": category_id,
            "action": action,
            "expand": expand,
            "status": status,
            "properties": properties,
            "propertyQuery": property_query,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_project_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all project types

        Path: /rest/api/3/project/type
        Method: GET
        """
        path = "/rest/api/3/project/type"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_accessible_project_types(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get licensed project types

        Path: /rest/api/3/project/type/accessible
        Method: GET
        """
        path = "/rest/api/3/project/type/accessible"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_type_by_key(
        self,
        project_type_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project type by key

        Path: /rest/api/3/project/type/{projectTypeKey}
        Method: GET
        """
        path = f"/rest/api/3/project/type/{project_type_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_accessible_project_type_by_key(
        self,
        project_type_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get accessible project type by key

        Path: /rest/api/3/project/type/{projectTypeKey}/accessible
        Method: GET
        """
        path = f"/rest/api/3/project/type/{project_type_key}/accessible"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_project(
        self,
        project_id_or_key: str,
        enable_undo: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete project

        Path: /rest/api/3/project/{projectIdOrKey}
        Method: DELETE
        """
        path = f"/rest/api/3/project/{project_id_or_key}"
        params = {
            "enableUndo": enable_undo,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project(
        self,
        project_id_or_key: str,
        expand: str | None = None,
        properties: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project

        Path: /rest/api/3/project/{projectIdOrKey}
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}"
        params = {
            "expand": expand,
            "properties": properties,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_project(
        self,
        project_id_or_key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update project

        Path: /rest/api/3/project/{projectIdOrKey}
        Method: PUT
        """
        path = f"/rest/api/3/project/{project_id_or_key}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_archive_project(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Archive project

        Path: /rest/api/3/project/{projectIdOrKey}/archive
        Method: POST
        """
        path = f"/rest/api/3/project/{project_id_or_key}/archive"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_project_avatar(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set project avatar

        Path: /rest/api/3/project/{projectIdOrKey}/avatar
        Method: PUT
        """
        path = f"/rest/api/3/project/{project_id_or_key}/avatar"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_project_avatar(
        self,
        project_id_or_key: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete project avatar

        Path: /rest/api/3/project/{projectIdOrKey}/avatar/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/project/{project_id_or_key}/avatar/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_project_avatar(
        self,
        project_id_or_key: str,
        x: int | None = None,
        y: int | None = None,
        size: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Load project avatar

        Path: /rest/api/3/project/{projectIdOrKey}/avatar2
        Method: POST
        """
        path = f"/rest/api/3/project/{project_id_or_key}/avatar2"
        params = {
            "x": x,
            "y": y,
            "size": size,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_project_avatars(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all project avatars

        Path: /rest/api/3/project/{projectIdOrKey}/avatars
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/avatars"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_classification_config(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the classification configuration for a project

        Path: /rest/api/3/project/{projectIdOrKey}/classification-config
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/classification-config"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_default_project_classification(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove the default data classification level from a project

        Path: /rest/api/3/project/{projectIdOrKey}/classification-level/default
        Method: DELETE
        """
        path = f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_default_project_classification(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the default data classification level of a project

        Path: /rest/api/3/project/{projectIdOrKey}/classification-level/default
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_default_project_classification(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update the default data classification level of a project

        Path: /rest/api/3/project/{projectIdOrKey}/classification-level/default
        Method: PUT
        """
        path = f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_components_paginated(
        self,
        project_id_or_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        component_source: str | None = None,
        query: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project components paginated

        Path: /rest/api/3/project/{projectIdOrKey}/component
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/component"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "componentSource": component_source,
            "query": query,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_components(
        self,
        project_id_or_key: str,
        component_source: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project components

        Path: /rest/api/3/project/{projectIdOrKey}/components
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/components"
        params = {
            "componentSource": component_source,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_project_asynchronously(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete project asynchronously

        Path: /rest/api/3/project/{projectIdOrKey}/delete
        Method: POST
        """
        path = f"/rest/api/3/project/{project_id_or_key}/delete"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_features_for_project(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project features

        Path: /rest/api/3/project/{projectIdOrKey}/features
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/features"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_toggle_feature_for_project(
        self,
        project_id_or_key: str,
        feature_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set project feature state

        Path: /rest/api/3/project/{projectIdOrKey}/features/{featureKey}
        Method: PUT
        """
        path = f"/rest/api/3/project/{project_id_or_key}/features/{feature_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_property_keys(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project property keys

        Path: /rest/api/3/project/{projectIdOrKey}/properties
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_project_property(
        self,
        project_id_or_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete project property

        Path: /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_property(
        self,
        project_id_or_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project property

        Path: /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_project_property(
        self,
        project_id_or_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set project property

        Path: /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_restore(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Restore deleted or archived project

        Path: /rest/api/3/project/{projectIdOrKey}/restore
        Method: POST
        """
        path = f"/rest/api/3/project/{project_id_or_key}/restore"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_roles(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project roles for project

        Path: /rest/api/3/project/{projectIdOrKey}/role
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/role"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_actor(
        self,
        project_id_or_key: str,
        id_: int,
        user: str | None = None,
        group: str | None = None,
        group_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete actors from project role

        Path: /rest/api/3/project/{projectIdOrKey}/role/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/project/{project_id_or_key}/role/{id_}"
        params = {
            "user": user,
            "group": group,
            "groupId": group_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_role(
        self,
        project_id_or_key: str,
        id_: int,
        exclude_inactive_users: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project role for project

        Path: /rest/api/3/project/{projectIdOrKey}/role/{id}
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/role/{id_}"
        params = {
            "excludeInactiveUsers": exclude_inactive_users,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_actor_users(
        self,
        project_id_or_key: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add actors to project role

        Path: /rest/api/3/project/{projectIdOrKey}/role/{id}
        Method: POST
        """
        path = f"/rest/api/3/project/{project_id_or_key}/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_actors(
        self,
        project_id_or_key: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set actors for project role

        Path: /rest/api/3/project/{projectIdOrKey}/role/{id}
        Method: PUT
        """
        path = f"/rest/api/3/project/{project_id_or_key}/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_role_details(
        self,
        project_id_or_key: str,
        current_member: bool | None = None,
        exclude_connect_addons: bool | None = None,
        exclude_other_service_roles: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project role details

        Path: /rest/api/3/project/{projectIdOrKey}/roledetails
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/roledetails"
        params = {
            "currentMember": current_member,
            "excludeConnectAddons": exclude_connect_addons,
            "excludeOtherServiceRoles": exclude_other_service_roles,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_statuses(
        self,
        project_id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all statuses for project

        Path: /rest/api/3/project/{projectIdOrKey}/statuses
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/statuses"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_versions_paginated(
        self,
        project_id_or_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        query: str | None = None,
        status: str | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project versions paginated

        Path: /rest/api/3/project/{projectIdOrKey}/version
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/version"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "query": query,
            "status": status,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_versions(
        self,
        project_id_or_key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project versions

        Path: /rest/api/3/project/{projectIdOrKey}/versions
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id_or_key}/versions"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_email(
        self,
        project_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project's sender email

        Path: /rest/api/3/project/{projectId}/email
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id}/email"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_project_email(
        self,
        project_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set project's sender email

        Path: /rest/api/3/project/{projectId}/email
        Method: PUT
        """
        path = f"/rest/api/3/project/{project_id}/email"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_hierarchy(
        self,
        project_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project issue type hierarchy

        Path: /rest/api/3/project/{projectId}/hierarchy
        Method: GET
        """
        path = f"/rest/api/3/project/{project_id}/hierarchy"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_issue_security_scheme(
        self,
        project_key_or_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project issue security scheme

        Path: /rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme
        Method: GET
        """
        path = f"/rest/api/3/project/{project_key_or_id}/issuesecuritylevelscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_notification_scheme_for_project(
        self,
        project_key_or_id: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project notification scheme

        Path: /rest/api/3/project/{projectKeyOrId}/notificationscheme
        Method: GET
        """
        path = f"/rest/api/3/project/{project_key_or_id}/notificationscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_assigned_permission_scheme(
        self,
        project_key_or_id: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get assigned permission scheme

        Path: /rest/api/3/project/{projectKeyOrId}/permissionscheme
        Method: GET
        """
        path = f"/rest/api/3/project/{project_key_or_id}/permissionscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_assign_permission_scheme(
        self,
        project_key_or_id: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign permission scheme

        Path: /rest/api/3/project/{projectKeyOrId}/permissionscheme
        Method: PUT
        """
        path = f"/rest/api/3/project/{project_key_or_id}/permissionscheme"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_security_levels_for_project(
        self,
        project_key_or_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project issue security levels

        Path: /rest/api/3/project/{projectKeyOrId}/securitylevel
        Method: GET
        """
        path = f"/rest/api/3/project/{project_key_or_id}/securitylevel"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_project_categories(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all project categories

        Path: /rest/api/3/projectCategory
        Method: GET
        """
        path = "/rest/api/3/projectCategory"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_project_category(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create project category

        Path: /rest/api/3/projectCategory
        Method: POST
        """
        path = "/rest/api/3/projectCategory"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_project_category(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete project category

        Path: /rest/api/3/projectCategory/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/projectCategory/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_category_by_id(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project category by ID

        Path: /rest/api/3/projectCategory/{id}
        Method: GET
        """
        path = f"/rest/api/3/projectCategory/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_project_category(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update project category

        Path: /rest/api/3/projectCategory/{id}
        Method: PUT
        """
        path = f"/rest/api/3/projectCategory/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_fields(
        self,
        project_id: list[Any],
        work_type_id: list[Any],
        start_at: int | None = None,
        max_results: int | None = None,
        field_id: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get fields for projects

        Path: /rest/api/3/projects/fields
        Method: GET
        """
        path = "/rest/api/3/projects/fields"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "projectId": project_id,
            "workTypeId": work_type_id,
            "fieldId": field_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_validate_project_key(
        self,
        key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Validate project key

        Path: /rest/api/3/projectvalidate/key
        Method: GET
        """
        path = "/rest/api/3/projectvalidate/key"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_valid_project_key(
        self,
        key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get valid project key

        Path: /rest/api/3/projectvalidate/validProjectKey
        Method: GET
        """
        path = "/rest/api/3/projectvalidate/validProjectKey"
        params = {
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_valid_project_name(
        self,
        name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get valid project name

        Path: /rest/api/3/projectvalidate/validProjectName
        Method: GET
        """
        path = "/rest/api/3/projectvalidate/validProjectName"
        params = {
            "name": name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_redact(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Redact

        Path: /rest/api/3/redact
        Method: POST
        """
        path = "/rest/api/3/redact"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_redaction_status(
        self,
        job_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get redaction status

        Path: /rest/api/3/redact/status/{jobId}
        Method: GET
        """
        path = f"/rest/api/3/redact/status/{job_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_resolutions(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get resolutions

        Path: /rest/api/3/resolution
        Method: GET
        """
        path = "/rest/api/3/resolution"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_resolution(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create resolution

        Path: /rest/api/3/resolution
        Method: POST
        """
        path = "/rest/api/3/resolution"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_default_resolution(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set default resolution

        Path: /rest/api/3/resolution/default
        Method: PUT
        """
        path = "/rest/api/3/resolution/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_move_resolutions(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Move resolutions

        Path: /rest/api/3/resolution/move
        Method: PUT
        """
        path = "/rest/api/3/resolution/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_resolutions(
        self,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[Any] | None = None,
        only_default: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search resolutions

        Path: /rest/api/3/resolution/search
        Method: GET
        """
        path = "/rest/api/3/resolution/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "onlyDefault": only_default,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_resolution(
        self,
        id_: str,
        replace_with: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete resolution

        Path: /rest/api/3/resolution/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/resolution/{id_}"
        params = {
            "replaceWith": replace_with,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_resolution(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get resolution

        Path: /rest/api/3/resolution/{id}
        Method: GET
        """
        path = f"/rest/api/3/resolution/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_resolution(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update resolution

        Path: /rest/api/3/resolution/{id}
        Method: PUT
        """
        path = f"/rest/api/3/resolution/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_project_roles(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all project roles

        Path: /rest/api/3/role
        Method: GET
        """
        path = "/rest/api/3/role"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_project_role(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create project role

        Path: /rest/api/3/role
        Method: POST
        """
        path = "/rest/api/3/role"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_project_role(
        self,
        id_: int,
        swap: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete project role

        Path: /rest/api/3/role/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/role/{id_}"
        params = {
            "swap": swap,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_role_by_id(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project role by ID

        Path: /rest/api/3/role/{id}
        Method: GET
        """
        path = f"/rest/api/3/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_partial_update_project_role(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Partial update project role

        Path: /rest/api/3/role/{id}
        Method: POST
        """
        path = f"/rest/api/3/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_fully_update_project_role(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Fully update project role

        Path: /rest/api/3/role/{id}
        Method: PUT
        """
        path = f"/rest/api/3/role/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_project_role_actors_from_role(
        self,
        id_: int,
        user: str | None = None,
        group_id: str | None = None,
        group: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete default actors from project role

        Path: /rest/api/3/role/{id}/actors
        Method: DELETE
        """
        path = f"/rest/api/3/role/{id_}/actors"
        params = {
            "user": user,
            "groupId": group_id,
            "group": group,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_role_actors_for_role(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get default actors for project role

        Path: /rest/api/3/role/{id}/actors
        Method: GET
        """
        path = f"/rest/api/3/role/{id_}/actors"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_project_role_actors_to_role(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add default actors to project role

        Path: /rest/api/3/role/{id}/actors
        Method: POST
        """
        path = f"/rest/api/3/role/{id_}/actors"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_screens(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[Any] | None = None,
        query_string: str | None = None,
        scope: list[Any] | None = None,
        order_by: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get screens

        Path: /rest/api/3/screens
        Method: GET
        """
        path = "/rest/api/3/screens"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "queryString": query_string,
            "scope": scope,
            "orderBy": order_by,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_screen(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create screen

        Path: /rest/api/3/screens
        Method: POST
        """
        path = "/rest/api/3/screens"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_field_to_default_screen(
        self,
        field_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add field to default screen

        Path: /rest/api/3/screens/addToDefault/{fieldId}
        Method: POST
        """
        path = f"/rest/api/3/screens/addToDefault/{field_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_bulk_screen_tabs(
        self,
        screen_id: list[Any] | None = None,
        tab_id: list[Any] | None = None,
        start_at: int | None = None,
        max_result: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get bulk screen tabs

        Path: /rest/api/3/screens/tabs
        Method: GET
        """
        path = "/rest/api/3/screens/tabs"
        params = {
            "screenId": screen_id,
            "tabId": tab_id,
            "startAt": start_at,
            "maxResult": max_result,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_screen(
        self,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete screen

        Path: /rest/api/3/screens/{screenId}
        Method: DELETE
        """
        path = f"/rest/api/3/screens/{screen_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_screen(
        self,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update screen

        Path: /rest/api/3/screens/{screenId}
        Method: PUT
        """
        path = f"/rest/api/3/screens/{screen_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_available_screen_fields(
        self,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get available screen fields

        Path: /rest/api/3/screens/{screenId}/availableFields
        Method: GET
        """
        path = f"/rest/api/3/screens/{screen_id}/availableFields"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_screen_tabs(
        self,
        screen_id: int,
        project_key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all screen tabs

        Path: /rest/api/3/screens/{screenId}/tabs
        Method: GET
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs"
        params = {
            "projectKey": project_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_screen_tab(
        self,
        screen_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create screen tab

        Path: /rest/api/3/screens/{screenId}/tabs
        Method: POST
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_screen_tab(
        self,
        screen_id: int,
        tab_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete screen tab

        Path: /rest/api/3/screens/{screenId}/tabs/{tabId}
        Method: DELETE
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_rename_screen_tab(
        self,
        screen_id: int,
        tab_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update screen tab

        Path: /rest/api/3/screens/{screenId}/tabs/{tabId}
        Method: PUT
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_screen_tab_fields(
        self,
        screen_id: int,
        tab_id: int,
        project_key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all screen tab fields

        Path: /rest/api/3/screens/{screenId}/tabs/{tabId}/fields
        Method: GET
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields"
        params = {
            "projectKey": project_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_add_screen_tab_field(
        self,
        screen_id: int,
        tab_id: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add screen tab field

        Path: /rest/api/3/screens/{screenId}/tabs/{tabId}/fields
        Method: POST
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_screen_tab_field(
        self,
        screen_id: int,
        tab_id: int,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove screen tab field

        Path: /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_move_screen_tab_field(
        self,
        screen_id: int,
        tab_id: int,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move screen tab field

        Path: /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move
        Method: POST
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id_}/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_move_screen_tab(
        self,
        screen_id: int,
        tab_id: int,
        pos: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move screen tab

        Path: /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}
        Method: POST
        """
        path = f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/move/{pos}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_screen_schemes(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[Any] | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get screen schemes

        Path: /rest/api/3/screenscheme
        Method: GET
        """
        path = "/rest/api/3/screenscheme"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "id": id_,
            "expand": expand,
            "queryString": query_string,
            "orderBy": order_by,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_screen_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create screen scheme

        Path: /rest/api/3/screenscheme
        Method: POST
        """
        path = "/rest/api/3/screenscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_screen_scheme(
        self,
        screen_scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete screen scheme

        Path: /rest/api/3/screenscheme/{screenSchemeId}
        Method: DELETE
        """
        path = f"/rest/api/3/screenscheme/{screen_scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_screen_scheme(
        self,
        screen_scheme_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update screen scheme

        Path: /rest/api/3/screenscheme/{screenSchemeId}
        Method: PUT
        """
        path = f"/rest/api/3/screenscheme/{screen_scheme_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_for_issues_using_jql(
        self,
        jql: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        validate_query: str | None = None,
        fields: list[Any] | None = None,
        expand: str | None = None,
        properties: list[Any] | None = None,
        fields_by_keys: bool | None = None,
        fail_fast: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Currently being removed. Search for issues using JQL (GET)

        Path: /rest/api/3/search
        Method: GET
        """
        path = "/rest/api/3/search"
        params = {
            "jql": jql,
            "startAt": start_at,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": fields,
            "expand": expand,
            "properties": properties,
            "fieldsByKeys": fields_by_keys,
            "failFast": fail_fast,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_for_issues_using_jql_post(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Currently being removed. Search for issues using JQL (POST)

        Path: /rest/api/3/search
        Method: POST
        """
        path = "/rest/api/3/search"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_count_issues(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Count issues using JQL

        Path: /rest/api/3/search/approximate-count
        Method: POST
        """
        path = "/rest/api/3/search/approximate-count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_and_reconsile_issues_using_jql(
        self,
        jql: str | None = None,
        next_page_token: str | None = None,
        max_results: int | None = None,
        fields: list[Any] | None = None,
        expand: str | None = None,
        properties: list[Any] | None = None,
        fields_by_keys: bool | None = None,
        fail_fast: bool | None = None,
        reconcile_issues: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search for issues using JQL enhanced search (GET)

        Path: /rest/api/3/search/jql
        Method: GET
        """
        path = "/rest/api/3/search/jql"
        params = {
            "jql": jql,
            "nextPageToken": next_page_token,
            "maxResults": max_results,
            "fields": fields,
            "expand": expand,
            "properties": properties,
            "fieldsByKeys": fields_by_keys,
            "failFast": fail_fast,
            "reconcileIssues": reconcile_issues,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_and_reconsile_issues_using_jql_post(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Search for issues using JQL enhanced search (POST)

        Path: /rest/api/3/search/jql
        Method: POST
        """
        path = "/rest/api/3/search/jql"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_security_level(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue security level

        Path: /rest/api/3/securitylevel/{id}
        Method: GET
        """
        path = f"/rest/api/3/securitylevel/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_server_info(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get Jira instance info

        Path: /rest/api/3/serverInfo
        Method: GET
        """
        path = "/rest/api/3/serverInfo"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_issue_navigator_default_columns(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get issue navigator default columns

        Path: /rest/api/3/settings/columns
        Method: GET
        """
        path = "/rest/api/3/settings/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_issue_navigator_default_columns(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set issue navigator default columns

        Path: /rest/api/3/settings/columns
        Method: PUT
        """
        path = "/rest/api/3/settings/columns"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_statuses(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all statuses

        Path: /rest/api/3/status
        Method: GET
        """
        path = "/rest/api/3/status"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_status(
        self,
        id_or_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get status

        Path: /rest/api/3/status/{idOrName}
        Method: GET
        """
        path = f"/rest/api/3/status/{id_or_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_status_categories(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get all status categories

        Path: /rest/api/3/statuscategory
        Method: GET
        """
        path = "/rest/api/3/statuscategory"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_status_category(
        self,
        id_or_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get status category

        Path: /rest/api/3/statuscategory/{idOrKey}
        Method: GET
        """
        path = f"/rest/api/3/statuscategory/{id_or_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_statuses_by_id(
        self,
        id_: list[Any],
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk delete Statuses

        Path: /rest/api/3/statuses
        Method: DELETE
        """
        path = "/rest/api/3/statuses"
        params = {
            "id": id_,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_statuses_by_id(
        self,
        id_: list[Any],
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk get statuses

        Path: /rest/api/3/statuses
        Method: GET
        """
        path = "/rest/api/3/statuses"
        params = {
            "id": id_,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_statuses(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk create statuses

        Path: /rest/api/3/statuses
        Method: POST
        """
        path = "/rest/api/3/statuses"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_statuses(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk update statuses

        Path: /rest/api/3/statuses
        Method: PUT
        """
        path = "/rest/api/3/statuses"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_statuses_by_name(
        self,
        name: list[Any],
        project_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk get statuses by name

        Path: /rest/api/3/statuses/byNames
        Method: GET
        """
        path = "/rest/api/3/statuses/byNames"
        params = {
            "name": name,
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search(
        self,
        project_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        search_string: str | None = None,
        status_category: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search statuses paginated

        Path: /rest/api/3/statuses/search
        Method: GET
        """
        path = "/rest/api/3/statuses/search"
        params = {
            "projectId": project_id,
            "startAt": start_at,
            "maxResults": max_results,
            "searchString": search_string,
            "statusCategory": status_category,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_issue_type_usages_for_status(
        self,
        status_id: str,
        project_id: str,
        next_page_token: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue type usages by status and project

        Path: /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages
        Method: GET
        """
        path = f"/rest/api/3/statuses/{status_id}/project/{project_id}/issueTypeUsages"
        params = {
            "nextPageToken": next_page_token,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_usages_for_status(
        self,
        status_id: str,
        next_page_token: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get project usages by status

        Path: /rest/api/3/statuses/{statusId}/projectUsages
        Method: GET
        """
        path = f"/rest/api/3/statuses/{status_id}/projectUsages"
        params = {
            "nextPageToken": next_page_token,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_usages_for_status(
        self,
        status_id: str,
        next_page_token: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow usages by status

        Path: /rest/api/3/statuses/{statusId}/workflowUsages
        Method: GET
        """
        path = f"/rest/api/3/statuses/{status_id}/workflowUsages"
        params = {
            "nextPageToken": next_page_token,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_task(
        self,
        task_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get task

        Path: /rest/api/3/task/{taskId}
        Method: GET
        """
        path = f"/rest/api/3/task/{task_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_cancel_task(
        self,
        task_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Cancel task

        Path: /rest/api/3/task/{taskId}/cancel
        Method: POST
        """
        path = f"/rest/api/3/task/{task_id}/cancel"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_ui_modifications(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get UI modifications

        Path: /rest/api/3/uiModifications
        Method: GET
        """
        path = "/rest/api/3/uiModifications"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_ui_modification(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create UI modification

        Path: /rest/api/3/uiModifications
        Method: POST
        """
        path = "/rest/api/3/uiModifications"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_ui_modification(
        self,
        ui_modification_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete UI modification

        Path: /rest/api/3/uiModifications/{uiModificationId}
        Method: DELETE
        """
        path = f"/rest/api/3/uiModifications/{ui_modification_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_ui_modification(
        self,
        ui_modification_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update UI modification

        Path: /rest/api/3/uiModifications/{uiModificationId}
        Method: PUT
        """
        path = f"/rest/api/3/uiModifications/{ui_modification_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_avatars(
        self,
        type_: str,
        entity_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get avatars

        Path: /rest/api/3/universal_avatar/type/{type}/owner/{entityId}
        Method: GET
        """
        path = f"/rest/api/3/universal_avatar/type/{type_}/owner/{entity_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_store_avatar(
        self,
        type_: str,
        entity_id: str,
        size: int,
        x: int | None = None,
        y: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Load avatar

        Path: /rest/api/3/universal_avatar/type/{type}/owner/{entityId}
        Method: POST
        """
        path = f"/rest/api/3/universal_avatar/type/{type_}/owner/{entity_id}"
        params = {
            "x": x,
            "y": y,
            "size": size,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_avatar(
        self,
        type_: str,
        owning_object_id: str,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete avatar

        Path: /rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/universal_avatar/type/{type_}/owner/{owning_object_id}/avatar/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_avatar_image_by_type(
        self,
        type_: str,
        size: str | None = None,
        format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get avatar image by type

        Path: /rest/api/3/universal_avatar/view/type/{type}
        Method: GET
        """
        path = f"/rest/api/3/universal_avatar/view/type/{type_}"
        params = {
            "size": size,
            "format": format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_avatar_image_by_id(
        self,
        type_: str,
        id_: int,
        size: str | None = None,
        format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get avatar image by ID

        Path: /rest/api/3/universal_avatar/view/type/{type}/avatar/{id}
        Method: GET
        """
        path = f"/rest/api/3/universal_avatar/view/type/{type_}/avatar/{id_}"
        params = {
            "size": size,
            "format": format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_avatar_image_by_owner(
        self,
        type_: str,
        entity_id: str,
        size: str | None = None,
        format: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get avatar image by owner

        Path: /rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}
        Method: GET
        """
        path = f"/rest/api/3/universal_avatar/view/type/{type_}/owner/{entity_id}"
        params = {
            "size": size,
            "format": format,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_remove_user(
        self,
        account_id: str,
        username: str | None = None,
        key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete user

        Path: /rest/api/3/user
        Method: DELETE
        """
        path = "/rest/api/3/user"
        params = {
            "accountId": account_id,
            "username": username,
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_user(
        self,
        account_id: str | None = None,
        username: str | None = None,
        key: str | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user

        Path: /rest/api/3/user
        Method: GET
        """
        path = "/rest/api/3/user"
        params = {
            "accountId": account_id,
            "username": username,
            "key": key,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_user(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create user

        Path: /rest/api/3/user
        Method: POST
        """
        path = "/rest/api/3/user"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_bulk_assignable_users(
        self,
        project_keys: str,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users assignable to projects

        Path: /rest/api/3/user/assignable/multiProjectSearch
        Method: GET
        """
        path = "/rest/api/3/user/assignable/multiProjectSearch"
        params = {
            "query": query,
            "username": username,
            "accountId": account_id,
            "projectKeys": project_keys,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_assignable_users(
        self,
        query: str | None = None,
        session_id: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        project: str | None = None,
        issue_key: str | None = None,
        issue_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        action_descriptor_id: int | None = None,
        recommend: bool | None = None,
        account_type: list[Any] | None = None,
        app_type: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users assignable to issues

        Path: /rest/api/3/user/assignable/search
        Method: GET
        """
        path = "/rest/api/3/user/assignable/search"
        params = {
            "query": query,
            "sessionId": session_id,
            "username": username,
            "accountId": account_id,
            "project": project,
            "issueKey": issue_key,
            "issueId": issue_id,
            "startAt": start_at,
            "maxResults": max_results,
            "actionDescriptorId": action_descriptor_id,
            "recommend": recommend,
            "accountType": account_type,
            "appType": app_type,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_get_users(
        self,
        account_id: list[Any],
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[Any] | None = None,
        key: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk get users

        Path: /rest/api/3/user/bulk
        Method: GET
        """
        path = "/rest/api/3/user/bulk"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "username": username,
            "key": key,
            "accountId": account_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_bulk_get_users_migration(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[Any] | None = None,
        key: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get account IDs for users

        Path: /rest/api/3/user/bulk/migration
        Method: GET
        """
        path = "/rest/api/3/user/bulk/migration"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "username": username,
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_reset_user_columns(
        self,
        account_id: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset user default columns

        Path: /rest/api/3/user/columns
        Method: DELETE
        """
        path = "/rest/api/3/user/columns"
        params = {
            "accountId": account_id,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_user_default_columns(
        self,
        account_id: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user default columns

        Path: /rest/api/3/user/columns
        Method: GET
        """
        path = "/rest/api/3/user/columns"
        params = {
            "accountId": account_id,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_user_columns(
        self,
        account_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set user default columns

        Path: /rest/api/3/user/columns
        Method: PUT
        """
        path = "/rest/api/3/user/columns"
        params = {
            "accountId": account_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_user_email(
        self,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user email

        Path: /rest/api/3/user/email
        Method: GET
        """
        path = "/rest/api/3/user/email"
        params = {
            "accountId": account_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_user_email_bulk(
        self,
        account_id: list[Any],
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user email bulk

        Path: /rest/api/3/user/email/bulk
        Method: GET
        """
        path = "/rest/api/3/user/email/bulk"
        params = {
            "accountId": account_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_user_groups(
        self,
        account_id: str,
        username: str | None = None,
        key: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user groups

        Path: /rest/api/3/user/groups
        Method: GET
        """
        path = "/rest/api/3/user/groups"
        params = {
            "accountId": account_id,
            "username": username,
            "key": key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_users_with_all_permissions(
        self,
        permissions: str,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        issue_key: str | None = None,
        project_key: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users with permissions

        Path: /rest/api/3/user/permission/search
        Method: GET
        """
        path = "/rest/api/3/user/permission/search"
        params = {
            "query": query,
            "username": username,
            "accountId": account_id,
            "permissions": permissions,
            "issueKey": issue_key,
            "projectKey": project_key,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_users_for_picker(
        self,
        query: str,
        max_results: int | None = None,
        show_avatar: bool | None = None,
        exclude: list[Any] | None = None,
        exclude_account_ids: list[Any] | None = None,
        avatar_size: str | None = None,
        exclude_connect_users: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users for picker

        Path: /rest/api/3/user/picker
        Method: GET
        """
        path = "/rest/api/3/user/picker"
        params = {
            "query": query,
            "maxResults": max_results,
            "showAvatar": show_avatar,
            "exclude": exclude,
            "excludeAccountIds": exclude_account_ids,
            "avatarSize": avatar_size,
            "excludeConnectUsers": exclude_connect_users,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_user_property_keys(
        self,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user property keys

        Path: /rest/api/3/user/properties
        Method: GET
        """
        path = "/rest/api/3/user/properties"
        params = {
            "accountId": account_id,
            "userKey": user_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_user_property(
        self,
        property_key: str,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete user property

        Path: /rest/api/3/user/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/api/3/user/properties/{property_key}"
        params = {
            "accountId": account_id,
            "userKey": user_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_user_property(
        self,
        property_key: str,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user property

        Path: /rest/api/3/user/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/api/3/user/properties/{property_key}"
        params = {
            "accountId": account_id,
            "userKey": user_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_user_property(
        self,
        property_key: str,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set user property

        Path: /rest/api/3/user/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/api/3/user/properties/{property_key}"
        params = {
            "accountId": account_id,
            "userKey": user_key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_users(
        self,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        property: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users

        Path: /rest/api/3/user/search
        Method: GET
        """
        path = "/rest/api/3/user/search"
        params = {
            "query": query,
            "username": username,
            "accountId": account_id,
            "startAt": start_at,
            "maxResults": max_results,
            "property": property,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_users_by_query(
        self,
        query: str,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users by query

        Path: /rest/api/3/user/search/query
        Method: GET
        """
        path = "/rest/api/3/user/search/query"
        params = {
            "query": query,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_user_keys_by_query(
        self,
        query: str,
        start_at: int | None = None,
        max_result: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find user keys by query

        Path: /rest/api/3/user/search/query/key
        Method: GET
        """
        path = "/rest/api/3/user/search/query/key"
        params = {
            "query": query,
            "startAt": start_at,
            "maxResult": max_result,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_find_users_with_browse_permission(
        self,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        issue_key: str | None = None,
        project_key: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find users with browse permission

        Path: /rest/api/3/user/viewissue/search
        Method: GET
        """
        path = "/rest/api/3/user/viewissue/search"
        params = {
            "query": query,
            "username": username,
            "accountId": account_id,
            "issueKey": issue_key,
            "projectKey": project_key,
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_users_default(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all users default

        Path: /rest/api/3/users
        Method: GET
        """
        path = "/rest/api/3/users"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_users(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all users

        Path: /rest/api/3/users/search
        Method: GET
        """
        path = "/rest/api/3/users/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_version(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create version

        Path: /rest/api/3/version
        Method: POST
        """
        path = "/rest/api/3/version"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_version(
        self,
        id_: str,
        move_fix_issues_to: str | None = None,
        move_affected_issues_to: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete version

        Path: /rest/api/3/version/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/version/{id_}"
        params = {
            "moveFixIssuesTo": move_fix_issues_to,
            "moveAffectedIssuesTo": move_affected_issues_to,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_version(
        self,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version

        Path: /rest/api/3/version/{id}
        Method: GET
        """
        path = f"/rest/api/3/version/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_version(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update version

        Path: /rest/api/3/version/{id}
        Method: PUT
        """
        path = f"/rest/api/3/version/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_merge_versions(
        self,
        id_: str,
        move_issues_to: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Merge versions

        Path: /rest/api/3/version/{id}/mergeto/{moveIssuesTo}
        Method: PUT
        """
        path = f"/rest/api/3/version/{id_}/mergeto/{move_issues_to}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_move_version(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move version

        Path: /rest/api/3/version/{id}/move
        Method: POST
        """
        path = f"/rest/api/3/version/{id_}/move"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_version_related_issues(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version's related issues count

        Path: /rest/api/3/version/{id}/relatedIssueCounts
        Method: GET
        """
        path = f"/rest/api/3/version/{id_}/relatedIssueCounts"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_related_work(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get related work

        Path: /rest/api/3/version/{id}/relatedwork
        Method: GET
        """
        path = f"/rest/api/3/version/{id_}/relatedwork"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_related_work(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create related work

        Path: /rest/api/3/version/{id}/relatedwork
        Method: POST
        """
        path = f"/rest/api/3/version/{id_}/relatedwork"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_related_work(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update related work

        Path: /rest/api/3/version/{id}/relatedwork
        Method: PUT
        """
        path = f"/rest/api/3/version/{id_}/relatedwork"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_and_replace_version(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete and replace version

        Path: /rest/api/3/version/{id}/removeAndSwap
        Method: POST
        """
        path = f"/rest/api/3/version/{id_}/removeAndSwap"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_version_unresolved_issues(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get version's unresolved issues count

        Path: /rest/api/3/version/{id}/unresolvedIssueCount
        Method: GET
        """
        path = f"/rest/api/3/version/{id_}/unresolvedIssueCount"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_related_work(
        self,
        version_id: str,
        related_work_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete related work

        Path: /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}
        Method: DELETE
        """
        path = f"/rest/api/3/version/{version_id}/relatedwork/{related_work_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_webhook_by_id(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Delete webhooks by ID

        Path: /rest/api/3/webhook
        Method: DELETE
        """
        path = "/rest/api/3/webhook"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_dynamic_webhooks_for_app(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get dynamic webhooks for app

        Path: /rest/api/3/webhook
        Method: GET
        """
        path = "/rest/api/3/webhook"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_register_dynamic_webhooks(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Register dynamic webhooks

        Path: /rest/api/3/webhook
        Method: POST
        """
        path = "/rest/api/3/webhook"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_failed_webhooks(
        self,
        max_results: int | None = None,
        after: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get failed webhooks

        Path: /rest/api/3/webhook/failed
        Method: GET
        """
        path = "/rest/api/3/webhook/failed"
        params = {
            "maxResults": max_results,
            "after": after,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_refresh_webhooks(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Extend webhook life

        Path: /rest/api/3/webhook/refresh
        Method: PUT
        """
        path = "/rest/api/3/webhook/refresh"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_workflows(
        self,
        workflow_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all workflows

        Path: /rest/api/3/workflow
        Method: GET
        """
        path = "/rest/api/3/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_workflow(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create workflow

        Path: /rest/api/3/workflow
        Method: POST
        """
        path = "/rest/api/3/workflow"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_read_workflow_from_history(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Read workflow version from history

        Path: /rest/api/3/workflow/history
        Method: POST
        """
        path = "/rest/api/3/workflow/history"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_list_workflow_history(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """List workflow history entries

        Path: /rest/api/3/workflow/history/list
        Method: POST
        """
        path = "/rest/api/3/workflow/history/list"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_transition_rule_configurations(
        self,
        types: list[Any],
        start_at: int | None = None,
        max_results: int | None = None,
        keys: list[Any] | None = None,
        workflow_names: list[Any] | None = None,
        with_tags: list[Any] | None = None,
        draft: bool | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow transition rule configurations

        Path: /rest/api/3/workflow/rule/config
        Method: GET
        """
        path = "/rest/api/3/workflow/rule/config"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "types": types,
            "keys": keys,
            "workflowNames": workflow_names,
            "withTags": with_tags,
            "draft": draft,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_workflow_transition_rule_configurations(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update workflow transition rule configurations

        Path: /rest/api/3/workflow/rule/config
        Method: PUT
        """
        path = "/rest/api/3/workflow/rule/config"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_workflow_transition_rule_configurations(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Delete workflow transition rule configurations

        Path: /rest/api/3/workflow/rule/config/delete
        Method: PUT
        """
        path = "/rest/api/3/workflow/rule/config/delete"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflows_paginated(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        workflow_name: list[Any] | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        is_active: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflows paginated

        Path: /rest/api/3/workflow/search
        Method: GET
        """
        path = "/rest/api/3/workflow/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "workflowName": workflow_name,
            "expand": expand,
            "queryString": query_string,
            "orderBy": order_by,
            "isActive": is_active,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_workflow_transition_property(
        self,
        transition_id: int,
        key: str,
        workflow_name: str,
        workflow_mode: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete workflow transition property

        Path: /rest/api/3/workflow/transitions/{transitionId}/properties
        Method: DELETE
        """
        path = f"/rest/api/3/workflow/transitions/{transition_id}/properties"
        params = {
            "key": key,
            "workflowName": workflow_name,
            "workflowMode": workflow_mode,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_transition_properties(
        self,
        transition_id: int,
        workflow_name: str,
        include_reserved_keys: bool | None = None,
        key: str | None = None,
        workflow_mode: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow transition properties

        Path: /rest/api/3/workflow/transitions/{transitionId}/properties
        Method: GET
        """
        path = f"/rest/api/3/workflow/transitions/{transition_id}/properties"
        params = {
            "includeReservedKeys": include_reserved_keys,
            "key": key,
            "workflowName": workflow_name,
            "workflowMode": workflow_mode,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_workflow_transition_property(
        self,
        transition_id: int,
        key: str,
        workflow_name: str,
        workflow_mode: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create workflow transition property

        Path: /rest/api/3/workflow/transitions/{transitionId}/properties
        Method: POST
        """
        path = f"/rest/api/3/workflow/transitions/{transition_id}/properties"
        params = {
            "key": key,
            "workflowName": workflow_name,
            "workflowMode": workflow_mode,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_workflow_transition_property(
        self,
        transition_id: int,
        key: str,
        workflow_name: str,
        workflow_mode: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update workflow transition property

        Path: /rest/api/3/workflow/transitions/{transitionId}/properties
        Method: PUT
        """
        path = f"/rest/api/3/workflow/transitions/{transition_id}/properties"
        params = {
            "key": key,
            "workflowName": workflow_name,
            "workflowMode": workflow_mode,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_inactive_workflow(
        self,
        entity_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete inactive workflow

        Path: /rest/api/3/workflow/{entityId}
        Method: DELETE
        """
        path = f"/rest/api/3/workflow/{entity_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_project_issue_type_usages(
        self,
        workflow_id: str,
        project_id: int,
        next_page_token: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue types in a project that are using a given workflow

        Path: /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages
        Method: GET
        """
        path = (
            f"/rest/api/3/workflow/{workflow_id}/project/{project_id}/issueTypeUsages"
        )
        params = {
            "nextPageToken": next_page_token,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_usages_for_workflow(
        self,
        workflow_id: str,
        next_page_token: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get projects using a given workflow

        Path: /rest/api/3/workflow/{workflowId}/projectUsages
        Method: GET
        """
        path = f"/rest/api/3/workflow/{workflow_id}/projectUsages"
        params = {
            "nextPageToken": next_page_token,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_scheme_usages_for_workflow(
        self,
        workflow_id: str,
        next_page_token: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow schemes which are using a given workflow

        Path: /rest/api/3/workflow/{workflowId}/workflowSchemes
        Method: GET
        """
        path = f"/rest/api/3/workflow/{workflow_id}/workflowSchemes"
        params = {
            "nextPageToken": next_page_token,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_read_workflows(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk get workflows

        Path: /rest/api/3/workflows
        Method: POST
        """
        path = "/rest/api/3/workflows"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_workflow_capabilities(
        self,
        workflow_id: str | None = None,
        project_id: str | None = None,
        issue_type_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get available workflow capabilities

        Path: /rest/api/3/workflows/capabilities
        Method: GET
        """
        path = "/rest/api/3/workflows/capabilities"
        params = {
            "workflowId": workflow_id,
            "projectId": project_id,
            "issueTypeId": issue_type_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_workflows(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk create workflows

        Path: /rest/api/3/workflows/create
        Method: POST
        """
        path = "/rest/api/3/workflows/create"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_validate_create_workflows(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Validate create workflows

        Path: /rest/api/3/workflows/create/validation
        Method: POST
        """
        path = "/rest/api/3/workflows/create/validation"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_default_editor(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get the user's default workflow editor

        Path: /rest/api/3/workflows/defaultEditor
        Method: GET
        """
        path = "/rest/api/3/workflows/defaultEditor"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_read_workflow_previews(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Preview workflow

        Path: /rest/api/3/workflows/preview
        Method: POST
        """
        path = "/rest/api/3/workflows/preview"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_search_workflows(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        scope: str | None = None,
        is_active: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search workflows

        Path: /rest/api/3/workflows/search
        Method: GET
        """
        path = "/rest/api/3/workflows/search"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
            "expand": expand,
            "queryString": query_string,
            "orderBy": order_by,
            "scope": scope,
            "isActive": is_active,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_workflows(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk update workflows

        Path: /rest/api/3/workflows/update
        Method: POST
        """
        path = "/rest/api/3/workflows/update"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_validate_update_workflows(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Validate update workflows

        Path: /rest/api/3/workflows/update/validation
        Method: POST
        """
        path = "/rest/api/3/workflows/update/validation"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_all_workflow_schemes(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all workflow schemes

        Path: /rest/api/3/workflowscheme
        Method: GET
        """
        path = "/rest/api/3/workflowscheme"
        params = {
            "startAt": start_at,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_workflow_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create workflow scheme

        Path: /rest/api/3/workflowscheme
        Method: POST
        """
        path = "/rest/api/3/workflowscheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_scheme_project_associations(
        self,
        project_id: list[Any],
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow scheme project associations

        Path: /rest/api/3/workflowscheme/project
        Method: GET
        """
        path = "/rest/api/3/workflowscheme/project"
        params = {
            "projectId": project_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_assign_scheme_to_project(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Assign workflow scheme to project

        Path: /rest/api/3/workflowscheme/project
        Method: PUT
        """
        path = "/rest/api/3/workflowscheme/project"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_switch_workflow_scheme_for_project(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Switch workflow scheme for project

        Path: /rest/api/3/workflowscheme/project/switch
        Method: POST
        """
        path = "/rest/api/3/workflowscheme/project/switch"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_read_workflow_schemes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Bulk get workflow schemes

        Path: /rest/api/3/workflowscheme/read
        Method: POST
        """
        path = "/rest/api/3/workflowscheme/read"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_schemes(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Update workflow scheme

        Path: /rest/api/3/workflowscheme/update
        Method: POST
        """
        path = "/rest/api/3/workflowscheme/update"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_required_workflow_scheme_mappings(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get required status mappings for workflow scheme update

        Path: /rest/api/3/workflowscheme/update/mappings
        Method: POST
        """
        path = "/rest/api/3/workflowscheme/update/mappings"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_workflow_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete workflow scheme

        Path: /rest/api/3/workflowscheme/{id}
        Method: DELETE
        """
        path = f"/rest/api/3/workflowscheme/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_scheme(
        self,
        id_: int,
        return_draft_if_exists: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow scheme

        Path: /rest/api/3/workflowscheme/{id}
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{id_}"
        params = {
            "returnDraftIfExists": return_draft_if_exists,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_workflow_scheme(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Classic update workflow scheme

        Path: /rest/api/3/workflowscheme/{id}
        Method: PUT
        """
        path = f"/rest/api/3/workflowscheme/{id_}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_create_workflow_scheme_draft_from_parent(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/createdraft
        Method: POST
        """
        path = f"/rest/api/3/workflowscheme/{id_}/createdraft"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_default_workflow(
        self,
        id_: int,
        update_draft_if_needed: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete default workflow

        Path: /rest/api/3/workflowscheme/{id}/default
        Method: DELETE
        """
        path = f"/rest/api/3/workflowscheme/{id_}/default"
        params = {
            "updateDraftIfNeeded": update_draft_if_needed,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_default_workflow(
        self,
        id_: int,
        return_draft_if_exists: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get default workflow

        Path: /rest/api/3/workflowscheme/{id}/default
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{id_}/default"
        params = {
            "returnDraftIfExists": return_draft_if_exists,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_default_workflow(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update default workflow

        Path: /rest/api/3/workflowscheme/{id}/default
        Method: PUT
        """
        path = f"/rest/api/3/workflowscheme/{id_}/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_workflow_scheme_draft(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft
        Method: DELETE
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_scheme_draft(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_workflow_scheme_draft(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft
        Method: PUT
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_draft_default_workflow(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete draft default workflow

        Path: /rest/api/3/workflowscheme/{id}/draft/default
        Method: DELETE
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_draft_default_workflow(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get draft default workflow

        Path: /rest/api/3/workflowscheme/{id}/draft/default
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_draft_default_workflow(
        self,
        id_: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update draft default workflow

        Path: /rest/api/3/workflowscheme/{id}/draft/default
        Method: PUT
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_workflow_scheme_draft_issue_type(
        self,
        id_: int,
        issue_type: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete workflow for issue type in draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}
        Method: DELETE
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_scheme_draft_issue_type(
        self,
        id_: int,
        issue_type: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow for issue type in draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_workflow_scheme_draft_issue_type(
        self,
        id_: int,
        issue_type: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set workflow for issue type in draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}
        Method: PUT
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_publish_draft_workflow_scheme(
        self,
        id_: int,
        validate_only: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Publish draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft/publish
        Method: POST
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/publish"
        params = {
            "validateOnly": validate_only,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_draft_workflow_mapping(
        self,
        id_: int,
        workflow_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue types for workflow in draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft/workflow
        Method: DELETE
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_draft_workflow(
        self,
        id_: int,
        workflow_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue types for workflows in draft workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft/workflow
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_draft_workflow_mapping(
        self,
        id_: int,
        workflow_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set issue types for workflow in workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/draft/workflow
        Method: PUT
        """
        path = f"/rest/api/3/workflowscheme/{id_}/draft/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_workflow_scheme_issue_type(
        self,
        id_: int,
        issue_type: str,
        update_draft_if_needed: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete workflow for issue type in workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/issuetype/{issueType}
        Method: DELETE
        """
        path = f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}"
        params = {
            "updateDraftIfNeeded": update_draft_if_needed,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow_scheme_issue_type(
        self,
        id_: int,
        issue_type: str,
        return_draft_if_exists: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow for issue type in workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/issuetype/{issueType}
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}"
        params = {
            "returnDraftIfExists": return_draft_if_exists,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_set_workflow_scheme_issue_type(
        self,
        id_: int,
        issue_type: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set workflow for issue type in workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/issuetype/{issueType}
        Method: PUT
        """
        path = f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_workflow_mapping(
        self,
        id_: int,
        workflow_name: str,
        update_draft_if_needed: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete issue types for workflow in workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/workflow
        Method: DELETE
        """
        path = f"/rest/api/3/workflowscheme/{id_}/workflow"
        params = {
            "workflowName": workflow_name,
            "updateDraftIfNeeded": update_draft_if_needed,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_workflow(
        self,
        id_: int,
        workflow_name: str | None = None,
        return_draft_if_exists: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get issue types for workflows in workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/workflow
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{id_}/workflow"
        params = {
            "workflowName": workflow_name,
            "returnDraftIfExists": return_draft_if_exists,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_update_workflow_mapping(
        self,
        id_: int,
        workflow_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set issue types for workflow in workflow scheme

        Path: /rest/api/3/workflowscheme/{id}/workflow
        Method: PUT
        """
        path = f"/rest/api/3/workflowscheme/{id_}/workflow"
        params = {
            "workflowName": workflow_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_project_usages_for_workflow_scheme(
        self,
        workflow_scheme_id: str,
        next_page_token: str | None = None,
        max_results: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get projects which are using a given workflow scheme

        Path: /rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages
        Method: GET
        """
        path = f"/rest/api/3/workflowscheme/{workflow_scheme_id}/projectUsages"
        params = {
            "nextPageToken": next_page_token,
            "maxResults": max_results,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_ids_of_worklogs_deleted_since(
        self,
        since: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get IDs of deleted worklogs

        Path: /rest/api/3/worklog/deleted
        Method: GET
        """
        path = "/rest/api/3/worklog/deleted"
        params = {
            "since": since,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_worklogs_for_ids(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get worklogs

        Path: /rest/api/3/worklog/list
        Method: POST
        """
        path = "/rest/api/3/worklog/list"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_ids_of_worklogs_modified_since(
        self,
        since: int | None = None,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get IDs of updated worklogs

        Path: /rest/api/3/worklog/updated
        Method: GET
        """
        path = "/rest/api/3/worklog/updated"
        params = {
            "since": since,
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_addon_properties_resource_get_addon_properties_get(
        self,
        addon_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get app properties

        Path: /rest/atlassian-connect/1/addons/{addonKey}/properties
        Method: GET
        """
        path = f"/rest/atlassian-connect/1/addons/{addon_key}/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_addon_properties_resource_delete_addon_property_delete(
        self,
        addon_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete app property

        Path: /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_addon_properties_resource_get_addon_property_get(
        self,
        addon_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get app property

        Path: /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_addon_properties_resource_put_addon_property_put(
        self,
        addon_key: str,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set app property

        Path: /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_dynamic_modules_resource_remove_modules_delete(
        self,
        module_key: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove modules

        Path: /rest/atlassian-connect/1/app/module/dynamic
        Method: DELETE
        """
        path = "/rest/atlassian-connect/1/app/module/dynamic"
        params = {
            "moduleKey": module_key,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_dynamic_modules_resource_get_modules_get(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get modules

        Path: /rest/atlassian-connect/1/app/module/dynamic
        Method: GET
        """
        path = "/rest/atlassian-connect/1/app/module/dynamic"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_dynamic_modules_resource_register_modules_post(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Register modules

        Path: /rest/atlassian-connect/1/app/module/dynamic
        Method: POST
        """
        path = "/rest/atlassian-connect/1/app/module/dynamic"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put(
        self,
        atlassian_transfer_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk update custom field value

        Path: /rest/atlassian-connect/1/migration/field
        Method: PUT
        """
        path = "/rest/atlassian-connect/1/migration/field"
        params = {
            "Atlassian-Transfer-Id": atlassian_transfer_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_migration_resource_update_entity_properties_value_put(
        self,
        atlassian_transfer_id: str,
        entity_type: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk update entity properties

        Path: /rest/atlassian-connect/1/migration/properties/{entityType}
        Method: PUT
        """
        path = f"/rest/atlassian-connect/1/migration/properties/{entity_type}"
        params = {
            "Atlassian-Transfer-Id": atlassian_transfer_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_migration_resource_workflow_rule_search_post(
        self,
        atlassian_transfer_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get workflow transition rule configurations

        Path: /rest/atlassian-connect/1/migration/workflow/rule/search
        Method: POST
        """
        path = "/rest/atlassian-connect/1/migration/workflow/rule/search"
        params = {
            "Atlassian-Transfer-Id": atlassian_transfer_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get(
        self,
        connect_key: str,
        jira_issue_fields_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get Connect issue field migration task

        Path: /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task
        Method: GET
        """
        path = f"/rest/atlassian-connect/1/migration/{connect_key}/{jira_issue_fields_key}/task"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post(
        self,
        connect_key: str,
        jira_issue_fields_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Submit Connect issue field migration task

        Path: /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task
        Method: POST
        """
        path = f"/rest/atlassian-connect/1/migration/{connect_key}/{jira_issue_fields_key}/task"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def jira_cloud_service_registry_resource_services_get(
        self,
        service_ids: list[Any],
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Retrieve the attributes of service registries

        Path: /rest/atlassian-connect/1/service-registry
        Method: GET
        """
        path = "/rest/atlassian-connect/1/service-registry"
        params = {
            "serviceIds": service_ids,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_forge_app_property_keys(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get app property keys (Forge)

        Path: /rest/forge/1/app/properties
        Method: GET
        """
        path = "/rest/forge/1/app/properties"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_delete_forge_app_property(
        self,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete app property (Forge)

        Path: /rest/forge/1/app/properties/{propertyKey}
        Method: DELETE
        """
        path = f"/rest/forge/1/app/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_forge_app_property(
        self,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get app property (Forge)

        Path: /rest/forge/1/app/properties/{propertyKey}
        Method: GET
        """
        path = f"/rest/forge/1/app/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def jira_cloud_put_forge_app_property(
        self,
        property_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set app property (Forge)

        Path: /rest/forge/1/app/properties/{propertyKey}
        Method: PUT
        """
        path = f"/rest/forge/1/app/properties/{property_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def jira_cloud_get_worklogs_by_issue_id_and_worklog_id(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get worklogs by issue id and worklog id

        Path: /rest/internal/api/latest/worklog/bulk
        Method: POST
        """
        path = "/rest/internal/api/latest/worklog/bulk"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )
