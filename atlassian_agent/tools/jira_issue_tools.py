# Generated MCP Tools for JiraCloud - issue
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.jira_cloud_api import JiraCloudAPI
from ..auth import get_base_client


def get_api() -> JiraCloudAPI:
    return JiraCloudAPI(get_base_client())


def register_jira_issue_tools(mcp: FastMCP):
    @mcp.tool(
        name="jira_cloud_get_attachment_content", tags={"jira-cloud-issue-attachment"}
    )
    def jira_cloud_get_attachment_content(
        id_: str = Field(..., description="The ID of the attachment."),
        redirect: bool | None = Field(
            None,
            description="Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to `false` to avoid making multiple requests to download the attachment.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachment content"""
        api = get_api()
        response = api.jira_cloud_get_attachment_content(
            id_=id_,
            redirect=redirect,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_attachment_meta", tags={"jira-cloud-issue-attachment"}
    )
    def jira_cloud_get_attachment_meta(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get Jira attachment settings"""
        api = get_api()
        response = api.jira_cloud_get_attachment_meta()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_attachment_thumbnail", tags={"jira-cloud-issue-attachment"}
    )
    def jira_cloud_get_attachment_thumbnail(
        id_: str = Field(..., description="The ID of the attachment."),
        redirect: bool | None = Field(
            None,
            description="Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to `false` to avoid making multiple requests to download the attachment.",
        ),
        fallback_to_default: bool | None = Field(
            None,
            description="Whether a default thumbnail is returned when the requested thumbnail is not found.",
        ),
        width: int | None = Field(
            None, description="The maximum width to scale the thumbnail to."
        ),
        height: int | None = Field(
            None, description="The maximum height to scale the thumbnail to."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachment thumbnail"""
        api = get_api()
        response = api.jira_cloud_get_attachment_thumbnail(
            id_=id_,
            redirect=redirect,
            fallback_to_default=fallback_to_default,
            width=width,
            height=height,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_attachment", tags={"jira-cloud-issue-attachment"})
    def jira_cloud_remove_attachment(
        id_: str = Field(..., description="The ID of the attachment."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete attachment"""
        api = get_api()
        response = api.jira_cloud_remove_attachment(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_attachment", tags={"jira-cloud-issue-attachment"})
    def jira_cloud_get_attachment(
        id_: str = Field(..., description="The ID of the attachment."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachment metadata"""
        api = get_api()
        response = api.jira_cloud_get_attachment(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_expand_attachment_for_humans",
        tags={"jira-cloud-issue-attachment"},
    )
    def jira_cloud_expand_attachment_for_humans(
        id_: str = Field(..., description="The ID of the attachment."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all metadata for an expanded attachment"""
        api = get_api()
        response = api.jira_cloud_expand_attachment_for_humans(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_expand_attachment_for_machines",
        tags={"jira-cloud-issue-attachment"},
    )
    def jira_cloud_expand_attachment_for_machines(
        id_: str = Field(..., description="The ID of the attachment."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get contents metadata for an expanded attachment"""
        api = get_api()
        response = api.jira_cloud_expand_attachment_for_machines(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_submit_bulk_delete", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_submit_bulk_delete(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk delete issues"""
        api = get_api()
        response = api.jira_cloud_submit_bulk_delete(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_bulk_editable_fields", tags={"jira-cloud-issue-bulk"}
    )
    def jira_cloud_get_bulk_editable_fields(
        issue_ids_or_keys: str = Field(
            ...,
            description="The IDs or keys of the issues to get editable fields from.",
        ),
        search_text: str | None = Field(
            None, description="(Optional)The text to search for in the editable fields."
        ),
        ending_before: str | None = Field(
            None, description="(Optional)The end cursor for use in pagination."
        ),
        starting_after: str | None = Field(
            None, description="(Optional)The start cursor for use in pagination."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get bulk editable fields"""
        api = get_api()
        response = api.jira_cloud_get_bulk_editable_fields(
            issue_ids_or_keys=issue_ids_or_keys,
            search_text=search_text,
            ending_before=ending_before,
            starting_after=starting_after,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_submit_bulk_edit", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_submit_bulk_edit(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk edit issues"""
        api = get_api()
        response = api.jira_cloud_submit_bulk_edit(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_submit_bulk_move", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_submit_bulk_move(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk move issues"""
        api = get_api()
        response = api.jira_cloud_submit_bulk_move(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_available_transitions", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_available_transitions(
        issue_ids_or_keys: str = Field(
            ...,
            description="Comma (,) separated Ids or keys of the issues to get transitions available for them.",
        ),
        ending_before: str | None = Field(
            None, description="(Optional)The end cursor for use in pagination."
        ),
        starting_after: str | None = Field(
            None, description="(Optional)The start cursor for use in pagination."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get available transitions"""
        api = get_api()
        response = api.jira_cloud_get_available_transitions(
            issue_ids_or_keys=issue_ids_or_keys,
            ending_before=ending_before,
            starting_after=starting_after,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_submit_bulk_transition", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_submit_bulk_transition(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk transition issue statuses"""
        api = get_api()
        response = api.jira_cloud_submit_bulk_transition(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_submit_bulk_unwatch", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_submit_bulk_unwatch(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk unwatch issues"""
        api = get_api()
        response = api.jira_cloud_submit_bulk_unwatch(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_submit_bulk_watch", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_submit_bulk_watch(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk watch issues"""
        api = get_api()
        response = api.jira_cloud_submit_bulk_watch(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_bulk_operation_progress", tags={"jira-cloud-issue-bulk"}
    )
    def jira_cloud_get_bulk_operation_progress(
        task_id: str = Field(..., description="The ID of the task."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get bulk issue operation progress"""
        api = get_api()
        response = api.jira_cloud_get_bulk_operation_progress(
            task_id=task_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_bulk_changelogs", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_get_bulk_changelogs(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk fetch changelogs"""
        api = get_api()
        response = api.jira_cloud_get_bulk_changelogs(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_comments_by_ids", tags={"jira-cloud-issue-comment"})
    def jira_cloud_get_comments_by_ids(
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts a comma-separated list. Expand options include:   *  `renderedBody` Returns the comment body rendered in HTML.  *  `properties` Returns the comment's properties.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get comments by IDs"""
        api = get_api()
        response = api.jira_cloud_get_comments_by_ids(
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_comment_property_keys", tags={"jira-cloud-issue-comment"}
    )
    def jira_cloud_get_comment_property_keys(
        comment_id: str = Field(..., description="The ID of the comment."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get comment property keys"""
        api = get_api()
        response = api.jira_cloud_get_comment_property_keys(
            comment_id=comment_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_comment_property", tags={"jira-cloud-issue-comment"}
    )
    def jira_cloud_delete_comment_property(
        comment_id: str = Field(..., description="The ID of the comment."),
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete comment property"""
        api = get_api()
        response = api.jira_cloud_delete_comment_property(
            comment_id=comment_id,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_comment_property", tags={"jira-cloud-issue-comment"})
    def jira_cloud_get_comment_property(
        comment_id: str = Field(..., description="The ID of the comment."),
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get comment property"""
        api = get_api()
        response = api.jira_cloud_get_comment_property(
            comment_id=comment_id,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_comment_property", tags={"jira-cloud-issue-comment"})
    def jira_cloud_set_comment_property(
        comment_id: str = Field(..., description="The ID of the comment."),
        property_key: str = Field(
            ...,
            description="The key of the property. The maximum length is 255 characters.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set comment property"""
        api = get_api()
        response = api.jira_cloud_set_comment_property(
            comment_id=comment_id,
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_component_related_issues", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_component_related_issues(
        id_: str = Field(..., description="The ID of the component."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get component issues count"""
        api = get_api()
        response = api.jira_cloud_get_component_related_issues(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_bulk_edit_dashboards", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_bulk_edit_dashboards(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk edit dashboards"""
        api = get_api()
        response = api.jira_cloud_bulk_edit_dashboards(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_type_mappings_for_contexts",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_issue_type_mappings_for_contexts(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: list[Any] | None = Field(
            None,
            description="The ID of the context. To include multiple contexts, provide an ampersand-separated list. For example, `contextId=10001&contextId=10002`.",
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
        """Get issue types for custom field context"""
        api = get_api()
        response = api.jira_cloud_get_issue_type_mappings_for_contexts(
            field_id=field_id,
            context_id=context_id,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_add_issue_types_to_context", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_add_issue_types_to_context(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add issue types to context"""
        api = get_api()
        response = api.jira_cloud_add_issue_types_to_context(
            field_id=field_id,
            context_id=context_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_issue_types_from_context",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_remove_issue_types_from_context(
        field_id: str = Field(..., description="The ID of the custom field."),
        context_id: int = Field(..., description="The ID of the context."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove issue types from context"""
        api = get_api()
        response = api.jira_cloud_remove_issue_types_from_context(
            field_id=field_id,
            context_id=context_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_issue_field_options", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_all_issue_field_options(
        field_key: str = Field(
            ...,
            description="The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:   *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.  *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `'key': 'teams-add-on__team-issue-field'`",
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
        """Get all issue field options"""
        api = get_api()
        response = api.jira_cloud_get_all_issue_field_options(
            start_at=start_at,
            max_results=max_results,
            field_key=field_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_issue_field_option", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_create_issue_field_option(
        field_key: str = Field(
            ...,
            description="The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:   *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.  *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `'key': 'teams-add-on__team-issue-field'`",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create issue field option"""
        api = get_api()
        response = api.jira_cloud_create_issue_field_option(
            field_key=field_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_selectable_issue_field_options",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_get_selectable_issue_field_options(
        field_key: str = Field(
            ...,
            description="The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:   *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.  *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `'key': 'teams-add-on__team-issue-field'`",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        project_id: int | None = Field(
            None,
            description="Filters the results to options that are only available in the specified project.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get selectable issue field options"""
        api = get_api()
        response = api.jira_cloud_get_selectable_issue_field_options(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
            field_key=field_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_visible_issue_field_options",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_get_visible_issue_field_options(
        field_key: str = Field(
            ...,
            description="The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:   *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.  *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `'key': 'teams-add-on__team-issue-field'`",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        project_id: int | None = Field(
            None,
            description="Filters the results to options that are only available in the specified project.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get visible issue field options"""
        api = get_api()
        response = api.jira_cloud_get_visible_issue_field_options(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
            field_key=field_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_issue_field_option", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_delete_issue_field_option(
        field_key: str = Field(
            ...,
            description="The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:   *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.  *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `'key': 'teams-add-on__team-issue-field'`",
        ),
        option_id: int = Field(..., description="The ID of the option to be deleted."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue field option"""
        api = get_api()
        response = api.jira_cloud_delete_issue_field_option(
            field_key=field_key,
            option_id=option_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_field_option", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue_field_option(
        field_key: str = Field(
            ...,
            description="The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:   *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.  *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `'key': 'teams-add-on__team-issue-field'`",
        ),
        option_id: int = Field(..., description="The ID of the option to be returned."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue field option"""
        api = get_api()
        response = api.jira_cloud_get_issue_field_option(
            field_key=field_key,
            option_id=option_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_issue_field_option", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_update_issue_field_option(
        field_key: str = Field(
            ...,
            description="The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:   *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.  *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `'key': 'teams-add-on__team-issue-field'`",
        ),
        option_id: int = Field(..., description="The ID of the option to be updated."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update issue field option"""
        api = get_api()
        response = api.jira_cloud_update_issue_field_option(
            field_key=field_key,
            option_id=option_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_replace_issue_field_option", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_replace_issue_field_option(
        field_key: str = Field(
            ...,
            description="The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:   *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.  *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `'key': 'teams-add-on__team-issue-field'`",
        ),
        option_id: int = Field(
            ..., description="The ID of the option to be deselected."
        ),
        replace_with: int | None = Field(
            None,
            description="The ID of the option that will replace the currently selected option.",
        ),
        jql: str | None = Field(
            None,
            description="A JQL query that specifies the issues to be updated. For example, *project=10000*.",
        ),
        override_screen_security: bool | None = Field(
            None,
            description="Whether screen security is overridden to enable hidden fields to be edited. Available to Connect and Forge app users with admin permission.",
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Replace issue field option"""
        api = get_api()
        response = api.jira_cloud_replace_issue_field_option(
            replace_with=replace_with,
            jql=jql,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
            field_key=field_key,
            option_id=option_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_filter", tags={"jira-cloud-issue-core"})
    def jira_cloud_create_filter(
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.  *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.",
        ),
        override_share_permissions: bool | None = Field(
            None,
            description="EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be created. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create filter"""
        api = get_api()
        response = api.jira_cloud_create_filter(
            expand=expand,
            override_share_permissions=override_share_permissions,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_favourite_filters", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_favourite_filters(
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.  *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get favorite filters"""
        api = get_api()
        response = api.jira_cloud_get_favourite_filters(
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_my_filters", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_my_filters(
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.  *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.",
        ),
        include_favourites: bool | None = Field(
            None, description="Include the user's favorite filters in the response."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get my filters"""
        api = get_api()
        response = api.jira_cloud_get_my_filters(
            expand=expand,
            include_favourites=include_favourites,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_filters_paginated", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_filters_paginated(
        filter_name: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with `name`.",
        ),
        account_id: str | None = Field(
            None,
            description="User account ID used to return filters with the matching `owner.accountId`. This parameter cannot be used with `owner`.",
        ),
        owner: str | None = Field(
            None,
            description="This parameter is deprecated because of privacy changes. Use `accountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return filters with the matching `owner.name`. This parameter cannot be used with `accountId`.",
        ),
        groupname: str | None = Field(
            None,
            description="As a group's name can change, use of `groupId` is recommended to identify a group. Group name used to returns filters that are shared with a group that matches `sharePermissions.group.groupname`. This parameter cannot be used with the `groupId` parameter.",
        ),
        group_id: str | None = Field(
            None,
            description="Group ID used to returns filters that are shared with a group that matches `sharePermissions.group.groupId`. This parameter cannot be used with the `groupname` parameter.",
        ),
        project_id: int | None = Field(
            None,
            description="Project ID used to returns filters that are shared with a project that matches `sharePermissions.project.id`.",
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of filter IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. Do not exceed 200 filter IDs.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `description` Sorts by filter description. Note that this sorting works independently of whether the expand to display the description field is in use.  *  `favourite_count` Sorts by the count of how many users have this filter as a favorite.  *  `is_favourite` Sorts by whether the filter is marked as a favorite.  *  `id` Sorts by filter ID.  *  `name` Sorts by filter name.  *  `owner` Sorts by the ID of the filter owner.  *  `is_shared` Sorts by whether the filter is shared.",
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
            description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  `description` Returns the description of the filter.  *  `favourite` Returns an indicator of whether the user has set the filter as a favorite.  *  `favouritedCount` Returns a count of how many users have set this filter as a favorite.  *  `jql` Returns the JQL query that the filter uses.  *  `owner` Returns the owner of the filter.  *  `searchUrl` Returns a URL to perform the filter's JQL query.  *  `sharePermissions` Returns the share permissions defined for the filter.  *  `editPermissions` Returns the edit permissions defined for the filter.  *  `isWritable` Returns whether the current user has permission to edit the filter.  *  `approximateLastUsed` \\[Experimental\\] Returns the approximate date and time when the filter was last evaluated.  *  `subscriptions` Returns the users that are subscribed to the filter.  *  `viewUrl` Returns a URL to view the filter.",
        ),
        override_share_permissions: bool | None = Field(
            None,
            description="EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        is_substring_match: bool | None = Field(
            None,
            description="When `true` this will perform a case-insensitive substring match for the provided `filterName`. When `false` the filter name will be searched using [full text search syntax](https://support.atlassian.com/jira-software-cloud/docs/search-for-issues-using-the-text-field/).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search for filters"""
        api = get_api()
        response = api.jira_cloud_get_filters_paginated(
            filter_name=filter_name,
            account_id=account_id,
            owner=owner,
            groupname=groupname,
            group_id=group_id,
            project_id=project_id,
            id_=id_,
            order_by=order_by,
            start_at=start_at,
            max_results=max_results,
            expand=expand,
            override_share_permissions=override_share_permissions,
            is_substring_match=is_substring_match,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_filter", tags={"jira-cloud-issue-core"})
    def jira_cloud_delete_filter(
        id_: int = Field(..., description="The ID of the filter to delete."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete filter"""
        api = get_api()
        response = api.jira_cloud_delete_filter(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_filter", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_filter(
        id_: int = Field(..., description="The ID of the filter to return."),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.  *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.",
        ),
        override_share_permissions: bool | None = Field(
            None,
            description="EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get filter"""
        api = get_api()
        response = api.jira_cloud_get_filter(
            id_=id_,
            expand=expand,
            override_share_permissions=override_share_permissions,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_filter", tags={"jira-cloud-issue-core"})
    def jira_cloud_update_filter(
        id_: int = Field(..., description="The ID of the filter to update."),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.  *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.",
        ),
        override_share_permissions: bool | None = Field(
            None,
            description="EXPERIMENTAL: Whether share permissions are overridden to enable the addition of any share permissions to filters. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update filter"""
        api = get_api()
        response = api.jira_cloud_update_filter(
            id_=id_,
            expand=expand,
            override_share_permissions=override_share_permissions,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_favourite_for_filter", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_delete_favourite_for_filter(
        id_: int = Field(..., description="The ID of the filter."),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.  *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove filter as favorite"""
        api = get_api()
        response = api.jira_cloud_delete_favourite_for_filter(
            id_=id_,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_favourite_for_filter", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_set_favourite_for_filter(
        id_: int = Field(..., description="The ID of the filter."),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.  *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add filter as favorite"""
        api = get_api()
        response = api.jira_cloud_set_favourite_for_filter(
            id_=id_,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_change_filter_owner", tags={"jira-cloud-issue-core"})
    def jira_cloud_change_filter_owner(
        id_: int = Field(..., description="The ID of the filter to update."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Change filter owner"""
        api = get_api()
        response = api.jira_cloud_change_filter_owner(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_bulk_pin_unpin_projects_async", tags={"jira-cloud-issue-bulk"}
    )
    def jira_cloud_bulk_pin_unpin_projects_async(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk pin or unpin issue panel to projects"""
        api = get_api()
        response = api.jira_cloud_bulk_pin_unpin_projects_async(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_bulk_get_groups", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_bulk_get_groups(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        group_id: list[Any] | None = Field(
            None,
            description="The ID of a group. To specify multiple IDs, pass multiple `groupId` parameters. For example, `groupId=5b10a2844c20165700ede21g&groupId=5b10ac8d82e05b22cc7d4ef5`.",
        ),
        group_name: list[Any] | None = Field(
            None,
            description="The name of a group. To specify multiple names, pass multiple `groupName` parameters. For example, `groupName=administrators&groupName=jira-software-users`.",
        ),
        access_type: str | None = Field(
            None,
            description="The access level of a group. Valid values: 'site-admin', 'admin', 'user'.",
        ),
        application_key: str | None = Field(
            None,
            description="The application key of the product user groups to search for. Valid values: 'jira-servicedesk', 'jira-software', 'jira-product-discovery', 'jira-core'.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk get groups"""
        api = get_api()
        response = api.jira_cloud_bulk_get_groups(
            start_at=start_at,
            max_results=max_results,
            group_id=group_id,
            group_name=group_name,
            access_type=access_type,
            application_key=application_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_issue", tags={"jira-cloud-issue-core"})
    def jira_cloud_create_issue(
        update_history: bool | None = Field(
            None,
            description="Whether the project in which the issue is created is added to the user's **Recently viewed** project list, as shown under **Projects** in Jira. When provided, the issue type and request type are added to the user's history for a project. These values are then used to provide defaults on the issue create screen.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create issue"""
        api = get_api()
        response = api.jira_cloud_create_issue(
            update_history=update_history,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_archive_issues_async", tags={"jira-cloud-issue-core"})
    def jira_cloud_archive_issues_async(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Archive issue(s) by JQL"""
        api = get_api()
        response = api.jira_cloud_archive_issues_async(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_archive_issues", tags={"jira-cloud-issue-core"})
    def jira_cloud_archive_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Archive issue(s) by issue ID/key"""
        api = get_api()
        response = api.jira_cloud_archive_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_issues", tags={"jira-cloud-issue-core"})
    def jira_cloud_create_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk create issue"""
        api = get_api()
        response = api.jira_cloud_create_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_bulk_fetch_issues", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_bulk_fetch_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk fetch issues"""
        api = get_api()
        response = api.jira_cloud_bulk_fetch_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_create_issue_meta", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_create_issue_meta(
        project_ids: list[Any] | None = Field(
            None,
            description="List of project IDs. This parameter accepts a comma-separated list. Multiple project IDs can also be provided using an ampersand-separated list. For example, `projectIds=10000,10001&projectIds=10020,10021`. This parameter may be provided with `projectKeys`.",
        ),
        project_keys: list[Any] | None = Field(
            None,
            description="List of project keys. This parameter accepts a comma-separated list. Multiple project keys can also be provided using an ampersand-separated list. For example, `projectKeys=proj1,proj2&projectKeys=proj3`. This parameter may be provided with `projectIds`.",
        ),
        issuetype_ids: list[Any] | None = Field(
            None,
            description="List of issue type IDs. This parameter accepts a comma-separated list. Multiple issue type IDs can also be provided using an ampersand-separated list. For example, `issuetypeIds=10000,10001&issuetypeIds=10020,10021`. This parameter may be provided with `issuetypeNames`.",
        ),
        issuetype_names: list[Any] | None = Field(
            None,
            description="List of issue type names. This parameter accepts a comma-separated list. Multiple issue type names can also be provided using an ampersand-separated list. For example, `issuetypeNames=name1,name2&issuetypeNames=name3`. This parameter may be provided with `issuetypeIds`.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about issue metadata in the response. This parameter accepts `projects.issuetypes.fields`, which returns information about the fields in the issue creation screen for each issue type. Fields hidden from the screen are not returned. Use the information to populate the `fields` and `update` fields in [Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get create issue metadata"""
        api = get_api()
        response = api.jira_cloud_get_create_issue_meta(
            project_ids=project_ids,
            project_keys=project_keys,
            issuetype_ids=issuetype_ids,
            issuetype_names=issuetype_names,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_create_issue_meta_issue_types",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_create_issue_meta_issue_types(
        project_id_or_key: str = Field(
            ..., description="The ID or key of the project."
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
        """Get create metadata issue types for a project"""
        api = get_api()
        response = api.jira_cloud_get_create_issue_meta_issue_types(
            project_id_or_key=project_id_or_key,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_create_issue_meta_issue_type_id",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_create_issue_meta_issue_type_id(
        project_id_or_key: str = Field(
            ..., description="The ID or key of the project."
        ),
        issue_type_id: str = Field(..., description="The issuetype ID."),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get create field metadata for a project and issue type id"""
        api = get_api()
        response = api.jira_cloud_get_create_issue_meta_issue_type_id(
            project_id_or_key=project_id_or_key,
            issue_type_id=issue_type_id,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_limit_report", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue_limit_report(
        is_returning_keys: bool | None = Field(
            None,
            description="Return issue keys instead of issue ids in the response.  Usage: Add `?isReturningKeys=true` to the end of the path to request issue keys.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue limit report"""
        api = get_api()
        response = api.jira_cloud_get_issue_limit_report(
            is_returning_keys=is_returning_keys,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_picker_resource", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_issue_picker_resource(
        query: str | None = Field(
            None,
            description="A string to match against text fields in the issue such as title, description, or comments.",
        ),
        current_jql: str | None = Field(
            None,
            description="A JQL query defining a list of issues to search for the query term. Note that `username` and `userkey` cannot be used as search terms for this parameter, due to privacy reasons. Use `accountId` instead.",
        ),
        current_issue_key: str | None = Field(
            None,
            description="The key of an issue to exclude from search results. For example, the issue the user is viewing when they perform this query.",
        ),
        current_project_id: str | None = Field(
            None,
            description="The ID of a project that suggested issues must belong to.",
        ),
        show_sub_tasks: bool | None = Field(
            None,
            description="Indicate whether to include subtasks in the suggestions list.",
        ),
        show_sub_task_parent: bool | None = Field(
            None,
            description="When `currentIssueKey` is a subtask, whether to include the parent issue in the suggestions if it matches the query.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue picker suggestions"""
        api = get_api()
        response = api.jira_cloud_get_issue_picker_resource(
            query=query,
            current_jql=current_jql,
            current_issue_key=current_issue_key,
            current_project_id=current_project_id,
            show_sub_tasks=show_sub_tasks,
            show_sub_task_parent=show_sub_task_parent,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_bulk_set_issues_properties_list",
        tags={"jira-cloud-issue-bulk"},
    )
    def jira_cloud_bulk_set_issues_properties_list(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk set issues properties by list"""
        api = get_api()
        response = api.jira_cloud_bulk_set_issues_properties_list(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_bulk_set_issue_properties_by_issue",
        tags={"jira-cloud-issue-bulk"},
    )
    def jira_cloud_bulk_set_issue_properties_by_issue(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk set issue properties by issue"""
        api = get_api()
        response = api.jira_cloud_bulk_set_issue_properties_by_issue(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_bulk_delete_issue_property", tags={"jira-cloud-issue-bulk"}
    )
    def jira_cloud_bulk_delete_issue_property(
        property_key: str = Field(..., description="The key of the property."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk delete issue property"""
        api = get_api()
        response = api.jira_cloud_bulk_delete_issue_property(
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_bulk_set_issue_property", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_bulk_set_issue_property(
        property_key: str = Field(
            ...,
            description="The key of the property. The maximum length is 255 characters.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk set issue property"""
        api = get_api()
        response = api.jira_cloud_bulk_set_issue_property(
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_unarchive_issues", tags={"jira-cloud-issue-core"})
    def jira_cloud_unarchive_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Unarchive issue(s) by issue keys/ID"""
        api = get_api()
        response = api.jira_cloud_unarchive_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_is_watching_issue_bulk", tags={"jira-cloud-issue-bulk"}
    )
    def jira_cloud_get_is_watching_issue_bulk(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get is watching issue bulk"""
        api = get_api()
        response = api.jira_cloud_get_is_watching_issue_bulk(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_issue", tags={"jira-cloud-issue-core"})
    def jira_cloud_delete_issue(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        delete_subtasks: str | None = Field(
            None,
            description="Whether the issue's subtasks are deleted when the issue is deleted.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue"""
        api = get_api()
        response = api.jira_cloud_delete_issue(
            issue_id_or_key=issue_id_or_key,
            delete_subtasks=delete_subtasks,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        fields: list[Any] | None = Field(
            None,
            description="A list of fields to return for the issue. This parameter accepts a comma-separated list. Use it to retrieve a subset of fields. Allowed values:   *  `*all` Returns all fields.  *  `*navigable` Returns navigable fields.  *  Any issue field, prefixed with a minus to exclude.  Examples:   *  `summary,comment` Returns only the summary and comments fields.  *  `-description` Returns all (default) fields except description.  *  `*navigable,-comment` Returns all navigable fields except comment.  This parameter may be specified multiple times. For example, `fields=field1,field2& fields=field3`.  Note: All fields are returned by default. This differs from [Search for issues using JQL (GET)](#api-rest-api-3-search-get) and [Search for issues using JQL (POST)](#api-rest-api-3-search-post) where the default is all navigable fields.",
        ),
        fields_by_keys: bool | None = Field(
            None,
            description="Whether fields in `fields` are referenced by keys rather than IDs. This parameter is useful where fields have been added by a connect app and a field's key may differ from its ID.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about the issues in the response. This parameter accepts a comma-separated list. Expand options include:   *  `renderedFields` Returns field values rendered in HTML format.  *  `names` Returns the display name of each field.  *  `schema` Returns the schema describing a field type.  *  `transitions` Returns all possible transitions for the issue.  *  `editmeta` Returns information about how each field can be edited.  *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.  *  `versionedRepresentations` Returns a JSON array for each version of a field's value, with the highest number representing the most recent version. Note: When included in the request, the `fields` parameter is ignored.",
        ),
        properties: list[Any] | None = Field(
            None,
            description="A list of issue properties to return for the issue. This parameter accepts a comma-separated list. Allowed values:   *  `*all` Returns all issue properties.  *  Any issue property key, prefixed with a minus to exclude.  Examples:   *  `*all` Returns all properties.  *  `*all,-prop1` Returns all properties except `prop1`.  *  `prop1,prop2` Returns `prop1` and `prop2` properties.  This parameter may be specified multiple times. For example, `properties=prop1,prop2& properties=prop3`.",
        ),
        update_history: bool | None = Field(
            None,
            description="Whether the project in which the issue is created is added to the user's **Recently viewed** project list, as shown under **Projects** in Jira. This also populates the [JQL issues search](#api-rest-api-3-search-get) `lastViewed` field.",
        ),
        fail_fast: bool | None = Field(
            None,
            description="Whether to fail the request quickly in case of an error while loading fields for an issue. For `failFast=true`, if one field fails, the entire operation fails. For `failFast=false`, the operation will continue even if a field fails. It will return a valid response, but without values for the failed field(s).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue"""
        api = get_api()
        response = api.jira_cloud_get_issue(
            issue_id_or_key=issue_id_or_key,
            fields=fields,
            fields_by_keys=fields_by_keys,
            expand=expand,
            properties=properties,
            update_history=update_history,
            fail_fast=fail_fast,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_edit_issue", tags={"jira-cloud-issue-core"})
    def jira_cloud_edit_issue(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        notify_users: bool | None = Field(
            None,
            description="Whether a notification email about the issue update is sent to all watchers. To disable the notification, administer Jira or administer project permissions are required. If the user doesn't have the necessary permission the request is ignored.",
        ),
        override_screen_security: bool | None = Field(
            None,
            description="Whether screen security is overridden to enable hidden fields to be edited. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        return_issue: bool | None = Field(
            None,
            description="Whether the response should contain the issue with fields edited in this request. The returned issue will have the same format as in the [Get issue API](#api-rest-api-3-issue-issueidorkey-get).",
        ),
        expand: str | None = Field(
            None,
            description="The Get issue API expand parameter to use in the response if the `returnIssue` parameter is `true`.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Edit issue"""
        api = get_api()
        response = api.jira_cloud_edit_issue(
            issue_id_or_key=issue_id_or_key,
            notify_users=notify_users,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
            return_issue=return_issue,
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_assign_issue", tags={"jira-cloud-issue-core"})
    def jira_cloud_assign_issue(
        issue_id_or_key: str = Field(
            ..., description="The ID or key of the issue to be assigned."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign issue"""
        api = get_api()
        response = api.jira_cloud_assign_issue(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_attachment", tags={"jira-cloud-issue-attachment"})
    def jira_cloud_add_attachment(
        issue_id_or_key: str = Field(
            ..., description="The ID or key of the issue that attachments are added to."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add attachment"""
        api = get_api()
        response = api.jira_cloud_add_attachment(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_comments", tags={"jira-cloud-issue-comment"})
    def jira_cloud_get_comments(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field. Accepts *created* to sort comments by their created date.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get comments"""
        api = get_api()
        response = api.jira_cloud_get_comments(
            issue_id_or_key=issue_id_or_key,
            start_at=start_at,
            max_results=max_results,
            order_by=order_by,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_comment", tags={"jira-cloud-issue-comment"})
    def jira_cloud_add_comment(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add comment"""
        api = get_api()
        response = api.jira_cloud_add_comment(
            issue_id_or_key=issue_id_or_key,
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_comment", tags={"jira-cloud-issue-comment"})
    def jira_cloud_delete_comment(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        id_: str = Field(..., description="The ID of the comment."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete comment"""
        api = get_api()
        response = api.jira_cloud_delete_comment(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_comment", tags={"jira-cloud-issue-comment"})
    def jira_cloud_get_comment(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        id_: str = Field(..., description="The ID of the comment."),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get comment"""
        api = get_api()
        response = api.jira_cloud_get_comment(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_comment", tags={"jira-cloud-issue-comment"})
    def jira_cloud_update_comment(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        id_: str = Field(..., description="The ID of the comment."),
        notify_users: bool | None = Field(
            None, description="Whether users are notified when a comment is updated."
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect app users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update comment"""
        api = get_api()
        response = api.jira_cloud_update_comment(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            notify_users=notify_users,
            override_editable_flag=override_editable_flag,
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_edit_issue_meta", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_edit_issue_meta(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        override_screen_security: bool | None = Field(
            None,
            description="Whether hidden fields are returned. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether non-editable fields are returned. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get edit issue metadata"""
        api = get_api()
        response = api.jira_cloud_get_edit_issue_meta(
            issue_id_or_key=issue_id_or_key,
            override_screen_security=override_screen_security,
            override_editable_flag=override_editable_flag,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_property_keys", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue_property_keys(
        issue_id_or_key: str = Field(..., description="The key or ID of the issue."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue property keys"""
        api = get_api()
        response = api.jira_cloud_get_issue_property_keys(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_issue_property", tags={"jira-cloud-issue-core"})
    def jira_cloud_delete_issue_property(
        issue_id_or_key: str = Field(..., description="The key or ID of the issue."),
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue property"""
        api = get_api()
        response = api.jira_cloud_delete_issue_property(
            issue_id_or_key=issue_id_or_key,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_property", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue_property(
        issue_id_or_key: str = Field(..., description="The key or ID of the issue."),
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue property"""
        api = get_api()
        response = api.jira_cloud_get_issue_property(
            issue_id_or_key=issue_id_or_key,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_issue_property", tags={"jira-cloud-issue-core"})
    def jira_cloud_set_issue_property(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        property_key: str = Field(
            ...,
            description="The key of the issue property. The maximum length is 255 characters.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set issue property"""
        api = get_api()
        response = api.jira_cloud_set_issue_property(
            issue_id_or_key=issue_id_or_key,
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_remote_issue_link_by_global_id",
        tags={"jira-cloud-issue-link"},
    )
    def jira_cloud_delete_remote_issue_link_by_global_id(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        global_id: str = Field(
            ..., description="The global ID of a remote issue link."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete remote issue link by global ID"""
        api = get_api()
        response = api.jira_cloud_delete_remote_issue_link_by_global_id(
            issue_id_or_key=issue_id_or_key,
            global_id=global_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_remote_issue_links", tags={"jira-cloud-issue-link"})
    def jira_cloud_get_remote_issue_links(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        global_id: str | None = Field(
            None, description="The global ID of the remote issue link."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get remote issue links"""
        api = get_api()
        response = api.jira_cloud_get_remote_issue_links(
            issue_id_or_key=issue_id_or_key,
            global_id=global_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_or_update_remote_issue_link",
        tags={"jira-cloud-issue-link"},
    )
    def jira_cloud_create_or_update_remote_issue_link(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create or update remote issue link"""
        api = get_api()
        response = api.jira_cloud_create_or_update_remote_issue_link(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_remote_issue_link_by_id", tags={"jira-cloud-issue-link"}
    )
    def jira_cloud_delete_remote_issue_link_by_id(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        link_id: str = Field(..., description="The ID of a remote issue link."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete remote issue link by ID"""
        api = get_api()
        response = api.jira_cloud_delete_remote_issue_link_by_id(
            issue_id_or_key=issue_id_or_key,
            link_id=link_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_remote_issue_link_by_id", tags={"jira-cloud-issue-link"}
    )
    def jira_cloud_get_remote_issue_link_by_id(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        link_id: str = Field(..., description="The ID of the remote issue link."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get remote issue link by ID"""
        api = get_api()
        response = api.jira_cloud_get_remote_issue_link_by_id(
            issue_id_or_key=issue_id_or_key,
            link_id=link_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_remote_issue_link", tags={"jira-cloud-issue-link"}
    )
    def jira_cloud_update_remote_issue_link(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        link_id: str = Field(..., description="The ID of the remote issue link."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update remote issue link by ID"""
        api = get_api()
        response = api.jira_cloud_update_remote_issue_link(
            issue_id_or_key=issue_id_or_key,
            link_id=link_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_transitions", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_transitions(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about transitions in the response. This parameter accepts `transitions.fields`, which returns information about the fields in the transition screen for each transition. Fields hidden from the screen are not returned. Use this information to populate the `fields` and `update` fields in [Transition issue](#api-rest-api-3-issue-issueIdOrKey-transitions-post).",
        ),
        transition_id: str | None = Field(
            None, description="The ID of the transition."
        ),
        skip_remote_only_condition: bool | None = Field(
            None,
            description="Whether transitions with the condition *Hide From User Condition* are included in the response. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).",
        ),
        include_unavailable_transitions: bool | None = Field(
            None,
            description="Whether details of transitions that fail a condition are included in the response",
        ),
        sort_by_ops_bar_and_status: bool | None = Field(
            None,
            description="Whether the transitions are sorted by ops-bar sequence value first then category order (Todo, In Progress, Done) or only by ops-bar sequence value.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get transitions"""
        api = get_api()
        response = api.jira_cloud_get_transitions(
            issue_id_or_key=issue_id_or_key,
            expand=expand,
            transition_id=transition_id,
            skip_remote_only_condition=skip_remote_only_condition,
            include_unavailable_transitions=include_unavailable_transitions,
            sort_by_ops_bar_and_status=sort_by_ops_bar_and_status,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_do_transition", tags={"jira-cloud-issue-core"})
    def jira_cloud_do_transition(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Transition issue"""
        api = get_api()
        response = api.jira_cloud_do_transition(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_remove_watcher", tags={"jira-cloud-issue-core"})
    def jira_cloud_remove_watcher(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        username: str | None = Field(
            None,
            description="This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        account_id: str | None = Field(
            None,
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete watcher"""
        api = get_api()
        response = api.jira_cloud_remove_watcher(
            issue_id_or_key=issue_id_or_key,
            username=username,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_watchers", tags={"jira-cloud-issue-watcher"})
    def jira_cloud_get_issue_watchers(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue watchers"""
        api = get_api()
        response = api.jira_cloud_get_issue_watchers(
            issue_id_or_key=issue_id_or_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_watcher", tags={"jira-cloud-issue-core"})
    def jira_cloud_add_watcher(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add watcher"""
        api = get_api()
        response = api.jira_cloud_add_watcher(
            issue_id_or_key=issue_id_or_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_bulk_delete_worklogs", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_bulk_delete_worklogs(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        adjust_estimate: str | None = Field(
            None,
            description="Defines how to update the issue's time estimate, the options are:   *  `leave` Leaves the estimate unchanged.  *  `auto` Reduces the estimate by the aggregate value of `timeSpent` across all worklogs being deleted.",
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether the work log entries should be removed to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with admin permission can use this flag.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk delete worklogs"""
        api = get_api()
        response = api.jira_cloud_bulk_delete_worklogs(
            issue_id_or_key=issue_id_or_key,
            adjust_estimate=adjust_estimate,
            override_editable_flag=override_editable_flag,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_worklog", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_get_issue_worklog(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        started_after: int | None = Field(
            None,
            description="The worklog start date and time, as a UNIX timestamp in milliseconds, after which worklogs are returned.",
        ),
        started_before: int | None = Field(
            None,
            description="The worklog start date and time, as a UNIX timestamp in milliseconds, before which worklogs are returned.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts`properties`, which returns worklog properties.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue worklogs"""
        api = get_api()
        response = api.jira_cloud_get_issue_worklog(
            issue_id_or_key=issue_id_or_key,
            start_at=start_at,
            max_results=max_results,
            started_after=started_after,
            started_before=started_before,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_add_worklog", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_add_worklog(
        issue_id_or_key: str = Field(..., description="The ID or key the issue."),
        notify_users: bool | None = Field(
            None, description="Whether users watching the issue are notified by email."
        ),
        adjust_estimate: str | None = Field(
            None,
            description="Defines how to update the issue's time estimate, the options are:   *  `new` Sets the estimate to a specific value, defined in `newEstimate`.  *  `leave` Leaves the estimate unchanged.  *  `manual` Reduces the estimate by amount specified in `reduceBy`.  *  `auto` Reduces the estimate by the value of `timeSpent` in the worklog.",
        ),
        new_estimate: str | None = Field(
            None,
            description="The value to set as the issue's remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when `adjustEstimate` is `new`.",
        ),
        reduce_by: str | None = Field(
            None,
            description="The amount to reduce the issue's remaining estimate by, as days (\\#d), hours (\\#h), or minutes (\\#m). For example, *2d*. Required when `adjustEstimate` is `manual`.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about work logs in the response. This parameter accepts `properties`, which returns worklog properties.",
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether the worklog entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can use this flag.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add worklog"""
        api = get_api()
        response = api.jira_cloud_add_worklog(
            issue_id_or_key=issue_id_or_key,
            notify_users=notify_users,
            adjust_estimate=adjust_estimate,
            new_estimate=new_estimate,
            reduce_by=reduce_by,
            expand=expand,
            override_editable_flag=override_editable_flag,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_bulk_move_worklogs", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_bulk_move_worklogs(
        issue_id_or_key: str = Field(..., description="Parameter issueIdOrKey"),
        adjust_estimate: str | None = Field(
            None,
            description="Defines how to update the issues' time estimate, the options are:   *  `leave` Leaves the estimate unchanged.  *  `auto` Reduces the estimate by the aggregate value of `timeSpent` across all worklogs being moved in the source issue, and increases it in the destination issue.",
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether the work log entry should be moved to and from the issues even if the issues are not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with admin permission can use this flag.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk move worklogs"""
        api = get_api()
        response = api.jira_cloud_bulk_move_worklogs(
            issue_id_or_key=issue_id_or_key,
            adjust_estimate=adjust_estimate,
            override_editable_flag=override_editable_flag,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_worklog", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_delete_worklog(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        id_: str = Field(..., description="The ID of the worklog."),
        notify_users: bool | None = Field(
            None, description="Whether users watching the issue are notified by email."
        ),
        adjust_estimate: str | None = Field(
            None,
            description="Defines how to update the issue's time estimate, the options are:   *  `new` Sets the estimate to a specific value, defined in `newEstimate`.  *  `leave` Leaves the estimate unchanged.  *  `manual` Increases the estimate by amount specified in `increaseBy`.  *  `auto` Reduces the estimate by the value of `timeSpent` in the worklog.",
        ),
        new_estimate: str | None = Field(
            None,
            description="The value to set as the issue's remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when `adjustEstimate` is `new`.",
        ),
        increase_by: str | None = Field(
            None,
            description="The amount to increase the issue's remaining estimate by, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when `adjustEstimate` is `manual`.",
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether the work log entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with admin permission can use this flag.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete worklog"""
        api = get_api()
        response = api.jira_cloud_delete_worklog(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            notify_users=notify_users,
            adjust_estimate=adjust_estimate,
            new_estimate=new_estimate,
            increase_by=increase_by,
            override_editable_flag=override_editable_flag,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_worklog", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_get_worklog(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        id_: str = Field(..., description="The ID of the worklog."),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about work logs in the response. This parameter accepts  `properties`, which returns worklog properties.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get worklog"""
        api = get_api()
        response = api.jira_cloud_get_worklog(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_worklog", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_update_worklog(
        issue_id_or_key: str = Field(..., description="The ID or key the issue."),
        id_: str = Field(..., description="The ID of the worklog."),
        notify_users: bool | None = Field(
            None, description="Whether users watching the issue are notified by email."
        ),
        adjust_estimate: str | None = Field(
            None,
            description="Defines how to update the issue's time estimate, the options are:   *  `new` Sets the estimate to a specific value, defined in `newEstimate`.  *  `leave` Leaves the estimate unchanged.  *  `auto` Updates the estimate by the difference between the original and updated value of `timeSpent` or `timeSpentSeconds`.",
        ),
        new_estimate: str | None = Field(
            None,
            description="The value to set as the issue's remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when `adjustEstimate` is `new`.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties`, which returns worklog properties.",
        ),
        override_editable_flag: bool | None = Field(
            None,
            description="Whether the worklog should be added to the issue even if the issue is not editable. For example, because the issue is closed. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can use this flag.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update worklog"""
        api = get_api()
        response = api.jira_cloud_update_worklog(
            issue_id_or_key=issue_id_or_key,
            id_=id_,
            notify_users=notify_users,
            adjust_estimate=adjust_estimate,
            new_estimate=new_estimate,
            expand=expand,
            override_editable_flag=override_editable_flag,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_worklog_property_keys", tags={"jira-cloud-issue-worklog"}
    )
    def jira_cloud_get_worklog_property_keys(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        worklog_id: str = Field(..., description="The ID of the worklog."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get worklog property keys"""
        api = get_api()
        response = api.jira_cloud_get_worklog_property_keys(
            issue_id_or_key=issue_id_or_key,
            worklog_id=worklog_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_worklog_property", tags={"jira-cloud-issue-worklog"}
    )
    def jira_cloud_delete_worklog_property(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        worklog_id: str = Field(..., description="The ID of the worklog."),
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete worklog property"""
        api = get_api()
        response = api.jira_cloud_delete_worklog_property(
            issue_id_or_key=issue_id_or_key,
            worklog_id=worklog_id,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_worklog_property", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_get_worklog_property(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        worklog_id: str = Field(..., description="The ID of the worklog."),
        property_key: str = Field(..., description="The key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get worklog property"""
        api = get_api()
        response = api.jira_cloud_get_worklog_property(
            issue_id_or_key=issue_id_or_key,
            worklog_id=worklog_id,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_worklog_property", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_set_worklog_property(
        issue_id_or_key: str = Field(..., description="The ID or key of the issue."),
        worklog_id: str = Field(..., description="The ID of the worklog."),
        property_key: str = Field(
            ...,
            description="The key of the issue property. The maximum length is 255 characters.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set worklog property"""
        api = get_api()
        response = api.jira_cloud_set_worklog_property(
            issue_id_or_key=issue_id_or_key,
            worklog_id=worklog_id,
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_link_issues", tags={"jira-cloud-issue-core"})
    def jira_cloud_link_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create issue link"""
        api = get_api()
        response = api.jira_cloud_link_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_issue_link", tags={"jira-cloud-issue-core"})
    def jira_cloud_delete_issue_link(
        link_id: str = Field(..., description="The ID of the issue link."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue link"""
        api = get_api()
        response = api.jira_cloud_delete_issue_link(
            link_id=link_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_link", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue_link(
        link_id: str = Field(..., description="The ID of the issue link."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue link"""
        api = get_api()
        response = api.jira_cloud_get_issue_link(
            link_id=link_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_link_types", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue_link_types(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue link types"""
        api = get_api()
        response = api.jira_cloud_get_issue_link_types()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_issue_link_type", tags={"jira-cloud-issue-core"})
    def jira_cloud_create_issue_link_type(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create issue link type"""
        api = get_api()
        response = api.jira_cloud_create_issue_link_type(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_issue_link_type", tags={"jira-cloud-issue-core"})
    def jira_cloud_delete_issue_link_type(
        issue_link_type_id: str = Field(
            ..., description="The ID of the issue link type."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue link type"""
        api = get_api()
        response = api.jira_cloud_delete_issue_link_type(
            issue_link_type_id=issue_link_type_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_link_type", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue_link_type(
        issue_link_type_id: str = Field(
            ..., description="The ID of the issue link type."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue link type"""
        api = get_api()
        response = api.jira_cloud_get_issue_link_type(
            issue_link_type_id=issue_link_type_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_issue_link_type", tags={"jira-cloud-issue-core"})
    def jira_cloud_update_issue_link_type(
        issue_link_type_id: str = Field(
            ..., description="The ID of the issue link type."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update issue link type"""
        api = get_api()
        response = api.jira_cloud_update_issue_link_type(
            issue_link_type_id=issue_link_type_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_export_archived_issues", tags={"jira-cloud-issue-core"})
    def jira_cloud_export_archived_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Export archived issue(s)"""
        api = get_api()
        response = api.jira_cloud_export_archived_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_security_schemes", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_issue_security_schemes(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue security schemes"""
        api = get_api()
        response = api.jira_cloud_get_issue_security_schemes()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_issue_security_scheme", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_create_issue_security_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create issue security scheme"""
        api = get_api()
        response = api.jira_cloud_create_issue_security_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_security_scheme", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_issue_security_scheme(
        id_: int = Field(
            ...,
            description="The ID of the issue security scheme. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) operation to get a list of issue security scheme IDs.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue security scheme"""
        api = get_api()
        response = api.jira_cloud_get_issue_security_scheme(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_issue_security_scheme", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_update_issue_security_scheme(
        id_: str = Field(..., description="The ID of the issue security scheme."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update issue security scheme"""
        api = get_api()
        response = api.jira_cloud_update_issue_security_scheme(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_security_level_members",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_get_issue_security_level_members(
        issue_security_scheme_id: int = Field(
            ...,
            description="The ID of the issue security scheme. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) operation to get a list of issue security scheme IDs.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        issue_security_level_id: list[Any] | None = Field(
            None,
            description="The list of issue security level IDs. To include multiple issue security levels separate IDs with ampersand: `issueSecurityLevelId=10000&issueSecurityLevelId=10001`.",
        ),
        expand: str | None = Field(
            None,
            description="Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `all` Returns all expandable information.  *  `field` Returns information about the custom field granted the permission.  *  `group` Returns information about the group that is granted the permission.  *  `projectRole` Returns information about the project role granted the permission.  *  `user` Returns information about the user who is granted the permission.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue security level members by issue security scheme"""
        api = get_api()
        response = api.jira_cloud_get_issue_security_level_members(
            issue_security_scheme_id=issue_security_scheme_id,
            start_at=start_at,
            max_results=max_results,
            issue_security_level_id=issue_security_level_id,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_all_types", tags={"jira-cloud-issue-core"})
    def jira_cloud_get_issue_all_types(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issue types for user"""
        api = get_api()
        response = api.jira_cloud_get_issue_all_types()
        return response.model_dump()

    @mcp.tool(name="jira_cloud_create_issue_type", tags={"jira-cloud-issue-type"})
    def jira_cloud_create_issue_type(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create issue type"""
        api = get_api()
        response = api.jira_cloud_create_issue_type(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_types_for_project", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_get_issue_types_for_project(
        project_id: int = Field(..., description="The ID of the project."),
        level: int | None = Field(
            None,
            description="The level of the issue type to filter by. Use:   *  `-1` for Subtask.  *  `0` for Base.  *  `1` for Epic.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue types for project"""
        api = get_api()
        response = api.jira_cloud_get_issue_types_for_project(
            project_id=project_id,
            level=level,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_delete_issue_type", tags={"jira-cloud-issue-type"})
    def jira_cloud_delete_issue_type(
        id_: str = Field(..., description="The ID of the issue type."),
        alternative_issue_type_id: str | None = Field(
            None, description="The ID of the replacement issue type."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue type"""
        api = get_api()
        response = api.jira_cloud_delete_issue_type(
            id_=id_,
            alternative_issue_type_id=alternative_issue_type_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_type", tags={"jira-cloud-issue-type"})
    def jira_cloud_get_issue_type(
        id_: str = Field(..., description="The ID of the issue type."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type"""
        api = get_api()
        response = api.jira_cloud_get_issue_type(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_update_issue_type", tags={"jira-cloud-issue-type"})
    def jira_cloud_update_issue_type(
        id_: str = Field(..., description="The ID of the issue type."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update issue type"""
        api = get_api()
        response = api.jira_cloud_update_issue_type(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_alternative_issue_types", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_get_alternative_issue_types(
        id_: str = Field(..., description="The ID of the issue type."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get alternative issue types"""
        api = get_api()
        response = api.jira_cloud_get_alternative_issue_types(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_issue_type_avatar", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_create_issue_type_avatar(
        id_: str = Field(..., description="The ID of the issue type."),
        size: int = Field(
            ..., description="The length of each side of the crop region."
        ),
        x: int | None = Field(
            None,
            description="The X coordinate of the top-left corner of the crop region.",
        ),
        y: int | None = Field(
            None,
            description="The Y coordinate of the top-left corner of the crop region.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Load issue type avatar"""
        api = get_api()
        response = api.jira_cloud_create_issue_type_avatar(
            id_=id_,
            x=x,
            y=y,
            size=size,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_type_property_keys", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_get_issue_type_property_keys(
        issue_type_id: str = Field(..., description="The ID of the issue type."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type property keys"""
        api = get_api()
        response = api.jira_cloud_get_issue_type_property_keys(
            issue_type_id=issue_type_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_issue_type_property", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_delete_issue_type_property(
        issue_type_id: str = Field(..., description="The ID of the issue type."),
        property_key: str = Field(
            ...,
            description="The key of the property. Use [Get issue type property keys](#api-rest-api-3-issuetype-issueTypeId-properties-get) to get a list of all issue type property keys.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue type property"""
        api = get_api()
        response = api.jira_cloud_delete_issue_type_property(
            issue_type_id=issue_type_id,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_issue_type_property", tags={"jira-cloud-issue-type"})
    def jira_cloud_get_issue_type_property(
        issue_type_id: str = Field(..., description="The ID of the issue type."),
        property_key: str = Field(
            ...,
            description="The key of the property. Use [Get issue type property keys](#api-rest-api-3-issuetype-issueTypeId-properties-get) to get a list of all issue type property keys.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type property"""
        api = get_api()
        response = api.jira_cloud_get_issue_type_property(
            issue_type_id=issue_type_id,
            property_key=property_key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_set_issue_type_property", tags={"jira-cloud-issue-type"})
    def jira_cloud_set_issue_type_property(
        issue_type_id: str = Field(..., description="The ID of the issue type."),
        property_key: str = Field(
            ...,
            description="The key of the issue type property. The maximum length is 255 characters.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set issue type property"""
        api = get_api()
        response = api.jira_cloud_set_issue_type_property(
            issue_type_id=issue_type_id,
            property_key=property_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_all_issue_type_schemes", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_get_all_issue_type_schemes(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of issue type schemes IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `name` Sorts by issue type scheme name.  *  `id` Sorts by issue type scheme ID.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `projects` For each issue type schemes, returns information about the projects the issue type scheme is assigned to.  *  `issueTypes` For each issue type schemes, returns information about the issueTypes the issue type scheme have.",
        ),
        query_string: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with issue type scheme name.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all issue type schemes"""
        api = get_api()
        response = api.jira_cloud_get_all_issue_type_schemes(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            order_by=order_by,
            expand=expand,
            query_string=query_string,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_issue_type_scheme", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_create_issue_type_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create issue type scheme"""
        api = get_api()
        response = api.jira_cloud_create_issue_type_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_type_schemes_mapping", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_get_issue_type_schemes_mapping(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        issue_type_scheme_id: list[Any] | None = Field(
            None,
            description="The list of issue type scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `issueTypeSchemeId=10000&issueTypeSchemeId=10001`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type scheme items"""
        api = get_api()
        response = api.jira_cloud_get_issue_type_schemes_mapping(
            start_at=start_at,
            max_results=max_results,
            issue_type_scheme_id=issue_type_scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_type_scheme_for_projects",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_issue_type_scheme_for_projects(
        project_id: list[Any] = Field(
            ...,
            description="The list of project IDs. To include multiple project IDs, provide an ampersand-separated list. For example, `projectId=10000&projectId=10001`.",
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
        """Get issue type schemes for projects"""
        api = get_api()
        response = api.jira_cloud_get_issue_type_scheme_for_projects(
            start_at=start_at,
            max_results=max_results,
            project_id=project_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_assign_issue_type_scheme_to_project",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_assign_issue_type_scheme_to_project(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign issue type scheme to project"""
        api = get_api()
        response = api.jira_cloud_assign_issue_type_scheme_to_project(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_issue_type_scheme", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_delete_issue_type_scheme(
        issue_type_scheme_id: int = Field(
            ..., description="The ID of the issue type scheme."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue type scheme"""
        api = get_api()
        response = api.jira_cloud_delete_issue_type_scheme(
            issue_type_scheme_id=issue_type_scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_issue_type_scheme", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_update_issue_type_scheme(
        issue_type_scheme_id: int = Field(
            ..., description="The ID of the issue type scheme."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update issue type scheme"""
        api = get_api()
        response = api.jira_cloud_update_issue_type_scheme(
            issue_type_scheme_id=issue_type_scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_add_issue_types_to_issue_type_scheme",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_add_issue_types_to_issue_type_scheme(
        issue_type_scheme_id: int = Field(
            ..., description="The ID of the issue type scheme."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add issue types to issue type scheme"""
        api = get_api()
        response = api.jira_cloud_add_issue_types_to_issue_type_scheme(
            issue_type_scheme_id=issue_type_scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_reorder_issue_types_in_issue_type_scheme",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_reorder_issue_types_in_issue_type_scheme(
        issue_type_scheme_id: int = Field(
            ..., description="The ID of the issue type scheme."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Change order of issue types"""
        api = get_api()
        response = api.jira_cloud_reorder_issue_types_in_issue_type_scheme(
            issue_type_scheme_id=issue_type_scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_remove_issue_type_from_issue_type_scheme",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_remove_issue_type_from_issue_type_scheme(
        issue_type_scheme_id: int = Field(
            ..., description="The ID of the issue type scheme."
        ),
        issue_type_id: int = Field(..., description="The ID of the issue type."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove issue type from issue type scheme"""
        api = get_api()
        response = api.jira_cloud_remove_issue_type_from_issue_type_scheme(
            issue_type_scheme_id=issue_type_scheme_id,
            issue_type_id=issue_type_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_type_screen_schemes", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_get_issue_type_screen_schemes(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        id_: list[Any] | None = Field(
            None,
            description="The list of issue type screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.",
        ),
        query_string: str | None = Field(
            None,
            description="String used to perform a case-insensitive partial match with issue type screen scheme name.",
        ),
        order_by: str | None = Field(
            None,
            description="[Order](#ordering) the results by a field:   *  `name` Sorts by issue type screen scheme name.  *  `id` Sorts by issue type screen scheme ID.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts `projects` that, for each issue type screen schemes, returns information about the projects the issue type screen scheme is assigned to.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type screen schemes"""
        api = get_api()
        response = api.jira_cloud_get_issue_type_screen_schemes(
            start_at=start_at,
            max_results=max_results,
            id_=id_,
            query_string=query_string,
            order_by=order_by,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_issue_type_screen_scheme",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_create_issue_type_screen_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create issue type screen scheme"""
        api = get_api()
        response = api.jira_cloud_create_issue_type_screen_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_type_screen_scheme_mappings",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_issue_type_screen_scheme_mappings(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        issue_type_screen_scheme_id: list[Any] | None = Field(
            None,
            description="The list of issue type screen scheme IDs. To include multiple issue type screen schemes, separate IDs with ampersand: `issueTypeScreenSchemeId=10000&issueTypeScreenSchemeId=10001`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type screen scheme items"""
        api = get_api()
        response = api.jira_cloud_get_issue_type_screen_scheme_mappings(
            start_at=start_at,
            max_results=max_results,
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_assign_issue_type_screen_scheme_to_project",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_assign_issue_type_screen_scheme_to_project(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Assign issue type screen scheme to project"""
        api = get_api()
        response = api.jira_cloud_assign_issue_type_screen_scheme_to_project(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_issue_type_screen_scheme",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_delete_issue_type_screen_scheme(
        issue_type_screen_scheme_id: str = Field(
            ..., description="The ID of the issue type screen scheme."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete issue type screen scheme"""
        api = get_api()
        response = api.jira_cloud_delete_issue_type_screen_scheme(
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_issue_type_screen_scheme",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_update_issue_type_screen_scheme(
        issue_type_screen_scheme_id: str = Field(
            ..., description="The ID of the issue type screen scheme."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update issue type screen scheme"""
        api = get_api()
        response = api.jira_cloud_update_issue_type_screen_scheme(
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_append_mappings_for_issue_type_screen_scheme",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_append_mappings_for_issue_type_screen_scheme(
        issue_type_screen_scheme_id: str = Field(
            ..., description="The ID of the issue type screen scheme."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Append mappings to issue type screen scheme"""
        api = get_api()
        response = api.jira_cloud_append_mappings_for_issue_type_screen_scheme(
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_projects_for_issue_type_screen_scheme",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_projects_for_issue_type_screen_scheme(
        issue_type_screen_scheme_id: int = Field(
            ..., description="The ID of the issue type screen scheme."
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        query: str | None = Field(None, description="Parameter query"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue type screen scheme projects"""
        api = get_api()
        response = api.jira_cloud_get_projects_for_issue_type_screen_scheme(
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
            start_at=start_at,
            max_results=max_results,
            query=query,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_match_issues", tags={"jira-cloud-issue-core"})
    def jira_cloud_match_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Check issues against JQL"""
        api = get_api()
        response = api.jira_cloud_match_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_parse_jql_queries", tags={"jira-cloud-issue-core"})
    def jira_cloud_parse_jql_queries(
        validation: str = Field(
            ...,
            description="How to validate the JQL query and treat the validation results. Validation options include:   *  `strict` Returns all errors. If validation fails, the query structure is not returned.  *  `warn` Returns all errors. If validation fails but the JQL query is correctly formed, the query structure is returned.  *  `none` No validation is performed. If JQL query is correctly formed, the query structure is returned.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Parse JQL query"""
        api = get_api()
        response = api.jira_cloud_parse_jql_queries(
            validation=validation,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_sanitise_jql_queries", tags={"jira-cloud-issue-core"})
    def jira_cloud_sanitise_jql_queries(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Sanitize JQL queries"""
        api = get_api()
        response = api.jira_cloud_sanitise_jql_queries(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_bulk_permissions", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_get_bulk_permissions(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get bulk permissions"""
        api = get_api()
        response = api.jira_cloud_get_bulk_permissions(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_issue_security_scheme",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_get_project_issue_security_scheme(
        project_key_or_id: str = Field(
            ..., description="The project ID or project key (case sensitive)."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get project issue security scheme"""
        api = get_api()
        response = api.jira_cloud_get_project_issue_security_scheme(
            project_key_or_id=project_key_or_id,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_bulk_screen_tabs", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_get_bulk_screen_tabs(
        screen_id: list[Any] | None = Field(
            None,
            description="The list of screen IDs. To include multiple screen IDs, provide an ampersand-separated list. For example, `screenId=10000&screenId=10001`.",
        ),
        tab_id: list[Any] | None = Field(
            None,
            description="The list of tab IDs. To include multiple tab IDs, provide an ampersand-separated list. For example, `tabId=10000&tabId=10001`.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_result: int | None = Field(
            None,
            description="The maximum number of items to return per page. The maximum number is 100,",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get bulk screen tabs"""
        api = get_api()
        response = api.jira_cloud_get_bulk_screen_tabs(
            screen_id=screen_id,
            tab_id=tab_id,
            start_at=start_at,
            max_result=max_result,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_for_issues_using_jql", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_search_for_issues_using_jql(
        jql: str | None = Field(
            None,
            description="The [JQL](https://confluence.atlassian.com/x/egORLQ) that defines the search. Note:   *  If no JQL expression is provided, all issues are returned.  *  `username` and `userkey` cannot be used as search terms due to privacy reasons. Use `accountId` instead.  *  If a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of items to return per page. To manage page size, Jira may return fewer items per page where a large number of fields or properties are requested. The greatest number of items returned per page is achieved when requesting `id` or `key` only.",
        ),
        validate_query: str | None = Field(
            None,
            description="Determines how to validate the JQL query and treat the validation results. Supported values are:   *  `strict` Returns a 400 response code if any errors are found, along with a list of all errors (and warnings).  *  `warn` Returns all errors as warnings.  *  `none` No validation is performed.  *  `true` *Deprecated* A legacy synonym for `strict`.  *  `false` *Deprecated* A legacy synonym for `warn`.  Note: If the JQL is not correctly formed a 400 response code is returned, regardless of the `validateQuery` value.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include:   *  `*all` Returns all fields.  *  `*navigable` Returns navigable fields.  *  Any issue field, prefixed with a minus to exclude.  Examples:   *  `summary,comment` Returns only the summary and comments fields.  *  `-description` Returns all navigable (default) fields except description.  *  `*all,-comment` Returns all fields except comments.  This parameter may be specified multiple times. For example, `fields=field1,field2&fields=field3`.  Note: All navigable fields are returned by default. This differs from [GET issue](#api-rest-api-3-issue-issueIdOrKey-get) where the default is all fields.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about issues in the response. This parameter accepts a comma-separated list. Expand options include:   *  `renderedFields` Returns field values rendered in HTML format.  *  `names` Returns the display name of each field.  *  `schema` Returns the schema describing a field type.  *  `transitions` Returns all possible transitions for the issue.  *  `operations` Returns all possible operations for the issue.  *  `editmeta` Returns information about how each field can be edited.  *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.  *  `versionedRepresentations` Instead of `fields`, returns `versionedRepresentations` a JSON array containing each version of a field's value, with the highest numbered item representing the most recent version.",
        ),
        properties: list[Any] | None = Field(
            None,
            description="A list of issue property keys for issue properties to include in the results. This parameter accepts a comma-separated list. Multiple properties can also be provided using an ampersand separated list. For example, `properties=prop1,prop2&properties=prop3`. A maximum of 5 issue property keys can be specified.",
        ),
        fields_by_keys: bool | None = Field(
            None, description="Reference fields by their key (rather than ID)."
        ),
        fail_fast: bool | None = Field(
            None,
            description="Whether to fail the request quickly in case of an error while loading fields for an issue. For `failFast=true`, if one field fails, the entire operation fails. For `failFast=false`, the operation will continue even if a field fails. It will return a valid response, but without values for the failed field(s).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Currently being removed. Search for issues using JQL (GET)"""
        api = get_api()
        response = api.jira_cloud_search_for_issues_using_jql(
            jql=jql,
            start_at=start_at,
            max_results=max_results,
            validate_query=validate_query,
            fields=fields,
            expand=expand,
            properties=properties,
            fields_by_keys=fields_by_keys,
            fail_fast=fail_fast,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_for_issues_using_jql_post",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_search_for_issues_using_jql_post(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Currently being removed. Search for issues using JQL (POST)"""
        api = get_api()
        response = api.jira_cloud_search_for_issues_using_jql_post(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_count_issues", tags={"jira-cloud-issue-core"})
    def jira_cloud_count_issues(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Count issues using JQL"""
        api = get_api()
        response = api.jira_cloud_count_issues(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_and_reconsile_issues_using_jql",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_search_and_reconsile_issues_using_jql(
        jql: str | None = Field(
            None,
            description="A [JQL](https://confluence.atlassian.com/x/egORLQ) expression. For performance reasons, this parameter requires a bounded query. A bounded query is a query with a search restriction.   *  Example of an unbounded query: `order by key desc`.  *  Example of a bounded query: `assignee = currentUser() order by key`.  Additionally, `orderBy` clause can contain a maximum of 7 fields.",
        ),
        next_page_token: str | None = Field(
            None,
            description="The token for a page to fetch that is not the first page. The first page has a `nextPageToken` of `null`. Use the `nextPageToken` to fetch the next page of issues.  Note: The `nextPageToken` field is **not included** in the response for the last page, indicating there is no next page.",
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of items to return per page. To manage page size, API may return fewer items per page where a large number of fields or properties are requested. The greatest number of items returned per page is achieved when requesting `id` or `key` only. It returns max 5000 issues.",
        ),
        fields: list[Any] | None = Field(
            None,
            description="A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include:   *  `*all` Returns all fields.  *  `*navigable` Returns navigable fields.  *  `id` Returns only issue IDs.  *  Any issue field, prefixed with a minus to exclude.  The default is `id`.  Examples:   *  `summary,comment` Returns only the summary and comments fields only.  *  `-description` Returns all navigable (default) fields except description.  *  `*all,-comment` Returns all fields except comments.  Multiple `fields` parameters can be included in a request.  Note: By default, this resource returns IDs only. This differs from [GET issue](#api-rest-api-3-issue-issueIdOrKey-get) where the default is all fields.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about issues in the response. Note that, unlike the majority of instances where `expand` is specified, `expand` is defined as a comma-delimited string of values. The expand options are:   *  `renderedFields` Returns field values rendered in HTML format.  *  `names` Returns the display name of each field.  *  `schema` Returns the schema describing a field type.  *  `transitions` Returns all possible transitions for the issue.  *  `operations` Returns all possible operations for the issue.  *  `editmeta` Returns information about how each field can be edited.  *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.  *  `versionedRepresentations` Instead of `fields`, returns `versionedRepresentations` a JSON array containing each version of a field's value, with the highest numbered item representing the most recent version.  Examples: `'names,changelog'` Returns the display name of each field as well as a list of recent updates to an issue.",
        ),
        properties: list[Any] | None = Field(
            None,
            description="A list of up to 5 issue properties to include in the results. This parameter accepts a comma-separated list.",
        ),
        fields_by_keys: bool | None = Field(
            None,
            description="Reference fields by their key (rather than ID). The default is `false`.",
        ),
        fail_fast: bool | None = Field(
            None,
            description="Fail this request early if we can't retrieve all field data.",
        ),
        reconcile_issues: list[Any] | None = Field(
            None,
            description="Strong consistency issue ids to be reconciled with search results. Accepts max 50 ids. This list of ids should be consistent with each paginated request across different pages.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search for issues using JQL enhanced search (GET)"""
        api = get_api()
        response = api.jira_cloud_search_and_reconsile_issues_using_jql(
            jql=jql,
            next_page_token=next_page_token,
            max_results=max_results,
            fields=fields,
            expand=expand,
            properties=properties,
            fields_by_keys=fields_by_keys,
            fail_fast=fail_fast,
            reconcile_issues=reconcile_issues,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_search_and_reconsile_issues_using_jql_post",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_search_and_reconsile_issues_using_jql_post(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search for issues using JQL enhanced search (POST)"""
        api = get_api()
        response = api.jira_cloud_search_and_reconsile_issues_using_jql_post(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_security_level", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_issue_security_level(
        id_: str = Field(..., description="The ID of the issue security level."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue security level"""
        api = get_api()
        response = api.jira_cloud_get_issue_security_level(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_issue_navigator_default_columns",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_get_issue_navigator_default_columns(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue navigator default columns"""
        api = get_api()
        response = api.jira_cloud_get_issue_navigator_default_columns()
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_issue_navigator_default_columns",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_set_issue_navigator_default_columns(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set issue navigator default columns"""
        api = get_api()
        response = api.jira_cloud_set_issue_navigator_default_columns(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_project_issue_type_usages_for_status",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_project_issue_type_usages_for_status(
        status_id: str = Field(
            ..., description="The statusId to fetch issue type usages for"
        ),
        project_id: str = Field(
            ..., description="The projectId to fetch issue type usages for"
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
        """Get issue type usages by status and project"""
        api = get_api()
        response = api.jira_cloud_get_project_issue_type_usages_for_status(
            status_id=status_id,
            project_id=project_id,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_find_bulk_assignable_users", tags={"jira-cloud-issue-bulk"}
    )
    def jira_cloud_find_bulk_assignable_users(
        project_keys: str = Field(
            ...,
            description="A list of project keys (case sensitive). This parameter accepts a comma-separated list.",
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
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find users assignable to projects"""
        api = get_api()
        response = api.jira_cloud_find_bulk_assignable_users(
            query=query,
            username=username,
            account_id=account_id,
            project_keys=project_keys,
            start_at=start_at,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_bulk_get_users", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_bulk_get_users(
        account_id: list[Any] = Field(
            ...,
            description="The account ID of a user. To specify multiple users, pass multiple `accountId` parameters. For example, `accountId=5b10a2844c20165700ede21g&accountId=5b10ac8d82e05b22cc7d4ef5`.",
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        username: list[Any] | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        key: list[Any] | None = Field(
            None,
            description="This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Bulk get users"""
        api = get_api()
        response = api.jira_cloud_bulk_get_users(
            start_at=start_at,
            max_results=max_results,
            username=username,
            key=key,
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_bulk_get_users_migration", tags={"jira-cloud-issue-bulk"}
    )
    def jira_cloud_bulk_get_users_migration(
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        username: list[Any] | None = Field(
            None,
            description="Username of a user. To specify multiple users, pass multiple copies of this parameter. For example, `username=fred&username=barney`. Required if `key` isn't provided. Cannot be provided if `key` is present.",
        ),
        key: list[Any] | None = Field(
            None,
            description="Key of a user. To specify multiple users, pass multiple copies of this parameter. For example, `key=fred&key=barney`. Required if `username` isn't provided. Cannot be provided if `username` is present.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get account IDs for users"""
        api = get_api()
        response = api.jira_cloud_bulk_get_users_migration(
            start_at=start_at,
            max_results=max_results,
            username=username,
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_user_email_bulk", tags={"jira-cloud-issue-bulk"})
    def jira_cloud_get_user_email_bulk(
        account_id: list[Any] = Field(
            ...,
            description="The account IDs of the users for which emails are required. An `accountId` is an identifier that uniquely identifies the user across all Atlassian products. For example, `5b10ac8d82e05b22cc7d4ef5`. Note, this should be treated as an opaque identifier (that is, do not assume any structure in the value).",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user email bulk"""
        api = get_api()
        response = api.jira_cloud_get_user_email_bulk(
            account_id=account_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_version_related_issues", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_version_related_issues(
        id_: str = Field(..., description="The ID of the version."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version's related issues count"""
        api = get_api()
        response = api.jira_cloud_get_version_related_issues(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_version_unresolved_issues", tags={"jira-cloud-issue-core"}
    )
    def jira_cloud_get_version_unresolved_issues(
        id_: str = Field(..., description="The ID of the version."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get version's unresolved issues count"""
        api = get_api()
        response = api.jira_cloud_get_version_unresolved_issues(
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_transition_rule_configurations",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_get_workflow_transition_rule_configurations(
        types: list[Any] = Field(
            ..., description="The types of the transition rules to return."
        ),
        start_at: int | None = Field(
            None,
            description="The index of the first item to return in a page of results (page offset).",
        ),
        max_results: int | None = Field(
            None, description="The maximum number of items to return per page."
        ),
        keys: list[Any] | None = Field(
            None,
            description="The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return.",
        ),
        workflow_names: list[Any] | None = Field(
            None, description="The list of workflow names to filter by."
        ),
        with_tags: list[Any] | None = Field(
            None, description="The list of `tags` to filter by."
        ),
        draft: bool | None = Field(
            None,
            description="Whether draft or published workflows are returned. If not provided, both workflow types are returned.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information in the response. This parameter accepts `transition`, which, for each rule, returns information about the transition the rule is assigned to.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow transition rule configurations"""
        api = get_api()
        response = api.jira_cloud_get_workflow_transition_rule_configurations(
            start_at=start_at,
            max_results=max_results,
            types=types,
            keys=keys,
            workflow_names=workflow_names,
            with_tags=with_tags,
            draft=draft,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_workflow_transition_property",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_delete_workflow_transition_property(
        transition_id: int = Field(
            ...,
            description="The ID of the transition. To get the ID, view the workflow in text mode in the Jira admin settings. The ID is shown next to the transition.",
        ),
        key: str = Field(
            ...,
            description="The name of the transition property to delete, also known as the name of the property.",
        ),
        workflow_name: str = Field(
            ..., description="The name of the workflow that the transition belongs to."
        ),
        workflow_mode: str | None = Field(
            None,
            description="The workflow status. Set to `live` for inactive workflows or `draft` for draft workflows. Active workflows cannot be edited.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete workflow transition property"""
        api = get_api()
        response = api.jira_cloud_delete_workflow_transition_property(
            transition_id=transition_id,
            key=key,
            workflow_name=workflow_name,
            workflow_mode=workflow_mode,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_transition_properties",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_get_workflow_transition_properties(
        transition_id: int = Field(
            ...,
            description="The ID of the transition. To get the ID, view the workflow in text mode in the Jira administration console. The ID is shown next to the transition.",
        ),
        workflow_name: str = Field(
            ..., description="The name of the workflow that the transition belongs to."
        ),
        include_reserved_keys: bool | None = Field(
            None,
            description="Some properties with keys that have the *jira.* prefix are reserved, which means they are not editable. To include these properties in the results, set this parameter to *true*.",
        ),
        key: str | None = Field(
            None,
            description="The key of the property being returned, also known as the name of the property. If this parameter is not specified, all properties on the transition are returned.",
        ),
        workflow_mode: str | None = Field(
            None,
            description="The workflow status. Set to *live* for active and inactive workflows, or *draft* for draft workflows.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow transition properties"""
        api = get_api()
        response = api.jira_cloud_get_workflow_transition_properties(
            transition_id=transition_id,
            include_reserved_keys=include_reserved_keys,
            key=key,
            workflow_name=workflow_name,
            workflow_mode=workflow_mode,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_create_workflow_transition_property",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_create_workflow_transition_property(
        transition_id: int = Field(
            ...,
            description="The ID of the transition. To get the ID, view the workflow in text mode in the Jira admin settings. The ID is shown next to the transition.",
        ),
        key: str = Field(
            ...,
            description="The key of the property being added, also known as the name of the property. Set this to the same value as the `key` defined in the request body.",
        ),
        workflow_name: str = Field(
            ..., description="The name of the workflow that the transition belongs to."
        ),
        workflow_mode: str | None = Field(
            None,
            description="The workflow status. Set to *live* for inactive workflows or *draft* for draft workflows. Active workflows cannot be edited.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create workflow transition property"""
        api = get_api()
        response = api.jira_cloud_create_workflow_transition_property(
            transition_id=transition_id,
            key=key,
            workflow_name=workflow_name,
            workflow_mode=workflow_mode,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_update_workflow_transition_property",
        tags={"jira-cloud-issue-core"},
    )
    def jira_cloud_update_workflow_transition_property(
        transition_id: int = Field(
            ...,
            description="The ID of the transition. To get the ID, view the workflow in text mode in the Jira admin settings. The ID is shown next to the transition.",
        ),
        key: str = Field(
            ...,
            description="The key of the property being updated, also known as the name of the property. Set this to the same value as the `key` defined in the request body.",
        ),
        workflow_name: str = Field(
            ..., description="The name of the workflow that the transition belongs to."
        ),
        workflow_mode: str | None = Field(
            None,
            description="The workflow status. Set to `live` for inactive workflows or `draft` for draft workflows. Active workflows cannot be edited.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update workflow transition property"""
        api = get_api()
        response = api.jira_cloud_update_workflow_transition_property(
            transition_id=transition_id,
            key=key,
            workflow_name=workflow_name,
            workflow_mode=workflow_mode,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_project_issue_type_usages",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_workflow_project_issue_type_usages(
        workflow_id: str = Field(..., description="The workflow ID"),
        project_id: int = Field(..., description="The project ID"),
        next_page_token: str | None = Field(
            None, description="The cursor for pagination"
        ),
        max_results: int | None = Field(
            None,
            description="The maximum number of results to return. Must be an integer between 1 and 200.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get issue types in a project that are using a given workflow"""
        api = get_api()
        response = api.jira_cloud_get_workflow_project_issue_type_usages(
            workflow_id=workflow_id,
            project_id=project_id,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_workflow_scheme_draft_issue_type",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_delete_workflow_scheme_draft_issue_type(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        issue_type: str = Field(..., description="The ID of the issue type."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete workflow for issue type in draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_delete_workflow_scheme_draft_issue_type(
            id_=id_,
            issue_type=issue_type,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_scheme_draft_issue_type",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_get_workflow_scheme_draft_issue_type(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        issue_type: str = Field(..., description="The ID of the issue type."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow for issue type in draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_get_workflow_scheme_draft_issue_type(
            id_=id_,
            issue_type=issue_type,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_workflow_scheme_draft_issue_type",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_set_workflow_scheme_draft_issue_type(
        id_: int = Field(
            ..., description="The ID of the workflow scheme that the draft belongs to."
        ),
        issue_type: str = Field(..., description="The ID of the issue type."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set workflow for issue type in draft workflow scheme"""
        api = get_api()
        response = api.jira_cloud_set_workflow_scheme_draft_issue_type(
            id_=id_,
            issue_type=issue_type,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_delete_workflow_scheme_issue_type",
        tags={"jira-cloud-issue-type"},
    )
    def jira_cloud_delete_workflow_scheme_issue_type(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        issue_type: str = Field(..., description="The ID of the issue type."),
        update_draft_if_needed: bool | None = Field(
            None,
            description="Set to true to create or update the draft of a workflow scheme and update the mapping in the draft, when the workflow scheme cannot be edited. Defaults to `false`.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete workflow for issue type in workflow scheme"""
        api = get_api()
        response = api.jira_cloud_delete_workflow_scheme_issue_type(
            id_=id_,
            issue_type=issue_type,
            update_draft_if_needed=update_draft_if_needed,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_workflow_scheme_issue_type", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_get_workflow_scheme_issue_type(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        issue_type: str = Field(..., description="The ID of the issue type."),
        return_draft_if_exists: bool | None = Field(
            None,
            description="Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get workflow for issue type in workflow scheme"""
        api = get_api()
        response = api.jira_cloud_get_workflow_scheme_issue_type(
            id_=id_,
            issue_type=issue_type,
            return_draft_if_exists=return_draft_if_exists,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_set_workflow_scheme_issue_type", tags={"jira-cloud-issue-type"}
    )
    def jira_cloud_set_workflow_scheme_issue_type(
        id_: int = Field(..., description="The ID of the workflow scheme."),
        issue_type: str = Field(..., description="The ID of the issue type."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set workflow for issue type in workflow scheme"""
        api = get_api()
        response = api.jira_cloud_set_workflow_scheme_issue_type(
            id_=id_,
            issue_type=issue_type,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_ids_of_worklogs_deleted_since",
        tags={"jira-cloud-issue-worklog"},
    )
    def jira_cloud_get_ids_of_worklogs_deleted_since(
        since: int | None = Field(
            None,
            description="The date and time, as a UNIX timestamp in milliseconds, after which deleted worklogs are returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get IDs of deleted worklogs"""
        api = get_api()
        response = api.jira_cloud_get_ids_of_worklogs_deleted_since(
            since=since,
        )
        return response.model_dump()

    @mcp.tool(name="jira_cloud_get_worklogs_for_ids", tags={"jira-cloud-issue-worklog"})
    def jira_cloud_get_worklogs_for_ids(
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties` that returns the properties of each worklog.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get worklogs"""
        api = get_api()
        response = api.jira_cloud_get_worklogs_for_ids(
            expand=expand,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_ids_of_worklogs_modified_since",
        tags={"jira-cloud-issue-worklog"},
    )
    def jira_cloud_get_ids_of_worklogs_modified_since(
        since: int | None = Field(
            None,
            description="The date and time, as a UNIX timestamp in milliseconds, after which updated worklogs are returned.",
        ),
        expand: str | None = Field(
            None,
            description="Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties` that returns the properties of each worklog.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get IDs of updated worklogs"""
        api = get_api()
        response = api.jira_cloud_get_ids_of_worklogs_modified_since(
            since=since,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(
        name="jira_cloud_get_worklogs_by_issue_id_and_worklog_id",
        tags={"jira-cloud-issue-worklog"},
    )
    def jira_cloud_get_worklogs_by_issue_id_and_worklog_id(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get worklogs by issue id and worklog id"""
        api = get_api()
        response = api.jira_cloud_get_worklogs_by_issue_id_and_worklog_id(
            payload=payload,
        )
        return response.model_dump()
