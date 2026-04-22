# Generated MCP Tools for ConfluenceServer
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.confluence_server_api import ConfluenceServerAPI
from ..auth import get_base_client


def get_api() -> ConfluenceServerAPI:
    return ConfluenceServerAPI(get_base_client())


def register_confluence_server_tools(mcp: FastMCP):
    @mcp.tool(
        name="confluence_server_get_access_mode_status",
        tags={"confluence-server-other"},
    )
    def confluence_server_get_access_mode_status(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get access mode status"""
        api = get_api()
        response = api.confluence_server_get_access_mode_status()
        return response.model_dump()

    @mcp.tool(name="confluence_server_create", tags={"confluence-server-other"})
    def confluence_server_create(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create group"""
        api = get_api()
        response = api.confluence_server_create(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete", tags={"confluence-server-other"})
    def confluence_server_delete(
        group_name: str = Field(..., description="the group name to be deleted"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete group"""
        api = get_api()
        response = api.confluence_server_delete(
            group_name=group_name,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_change_password", tags={"confluence-server-other"}
    )
    def confluence_server_change_password(
        username: str = Field(
            ..., description="the username identifying the given user"
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Change password"""
        api = get_api()
        response = api.confluence_server_change_password(
            username=username,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_create_user", tags={"confluence-server-user"})
    def confluence_server_create_user(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create user"""
        api = get_api()
        response = api.confluence_server_create_user(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete_1", tags={"confluence-server-other"})
    def confluence_server_delete_1(
        username: str = Field(
            ..., description="the username identifying the given user"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete user"""
        api = get_api()
        response = api.confluence_server_delete_1(
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_disable", tags={"confluence-server-other"})
    def confluence_server_disable(
        username: str = Field(
            ..., description="the username identifying the given user"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Disable user"""
        api = get_api()
        response = api.confluence_server_disable(
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_enable", tags={"confluence-server-other"})
    def confluence_server_enable(
        username: str = Field(
            ..., description="the username identifying the given user"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Enable user"""
        api = get_api()
        response = api.confluence_server_enable(
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_attachments", tags={"confluence-server-other"}
    )
    def confluence_server_get_attachments(
        id_: str = Field(
            ..., description="The id of the content the attachment is on."
        ),
        expand: str | None = Field(
            None,
            description="(optional) a comma separated list of properties to expand on the Attachments returned. Optional.",
        ),
        filename: str | None = Field(
            None,
            description="(optional) filter parameter to return only the Attachment with the matching file name.",
        ),
        limit: str | None = Field(
            None,
            description="(optional) how many items should be returned after the start index.",
        ),
        start: str | None = Field(
            None,
            description="(optional) the index of the first item within the result set that should be returned.",
        ),
        media_type: str | None = Field(
            None,
            description="(optional) a comma separated list of properties to expand on the Attachments returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get attachment"""
        api = get_api()
        response = api.confluence_server_get_attachments(
            expand=expand,
            filename=filename,
            limit=limit,
            start=start,
            media_type=media_type,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_attachments", tags={"confluence-server-other"}
    )
    def confluence_server_create_attachments(
        id_: str = Field(
            ..., description="The id of the content the attachment is on."
        ),
        expand: str | None = Field(
            None,
            description="(optional) a comma separated list of properties to expand on the Attachments returned. Optional.",
        ),
        allow_duplicated: str | None = Field(
            None,
            description="(optional) allows to upload an attachment with an existing filename.",
        ),
        status: str | None = Field(
            None,
            description="a string containing the status of the attachments content container, supports current or draft, defaults to current",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create attachments"""
        api = get_api()
        response = api.confluence_server_create_attachments(
            expand=expand,
            id_=id_,
            allow_duplicated=allow_duplicated,
            status=status,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_attachment_extracted_text",
        tags={"confluence-server-other"},
    )
    def confluence_server_get_attachment_extracted_text(
        attachment_id: str = Field(..., description="Parameter attachmentId"),
        id_: str = Field(..., description="Parameter id"),
        limit: int | None = Field(None, description="Parameter limit"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """No description provided."""
        api = get_api()
        response = api.confluence_server_get_attachment_extracted_text(
            limit=limit,
            attachment_id=attachment_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_move", tags={"confluence-server-other"})
    def confluence_server_move(
        attachment_id: str = Field(
            ..., description="the id of the attachment to upload the new file for."
        ),
        id_: str = Field(
            ..., description="The id of the content the attachment is on."
        ),
        new_name: str | None = Field(None, description="Parameter newName"),
        new_content_id: str | None = Field(None, description="Parameter newContentId"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Move attachment"""
        api = get_api()
        response = api.confluence_server_move(
            new_name=new_name,
            new_content_id=new_content_id,
            attachment_id=attachment_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_update", tags={"confluence-server-other"})
    def confluence_server_update(
        attachment_id: str = Field(
            ..., description="the id of the attachment to update."
        ),
        id_: str = Field(
            ..., description="The id of the content the attachment is on."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update non-binary data of an Attachment"""
        api = get_api()
        response = api.confluence_server_update(
            attachment_id=attachment_id,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_remove_attachment", tags={"confluence-server-other"}
    )
    def confluence_server_remove_attachment(
        attachment_id: str = Field(
            ..., description="the id of the attachment to be removed."
        ),
        id_: str = Field(
            ..., description="The id of the content the attachment is on."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove attachment"""
        api = get_api()
        response = api.confluence_server_remove_attachment(
            attachment_id=attachment_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_remove_attachment_version",
        tags={"confluence-server-other"},
    )
    def confluence_server_remove_attachment_version(
        attachment_id: str = Field(
            ..., description="The id of the attachment to be removed."
        ),
        id_: str = Field(
            ..., description="The id of the content the attachment is on."
        ),
        version: int = Field(..., description="Parameter version"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove attachment version"""
        api = get_api()
        response = api.confluence_server_remove_attachment_version(
            attachment_id=attachment_id,
            id_=id_,
            version=version,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_update_data", tags={"confluence-server-other"})
    def confluence_server_update_data(
        attachment_id: str = Field(
            ..., description="the id of the attachment to upload the new file for."
        ),
        id_: str = Field(
            ..., description="The id of the content the attachment is on."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update binary data of an attachment"""
        api = get_api()
        response = api.confluence_server_update_data(
            attachment_id=attachment_id,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_audit_records", tags={"confluence-server-other"}
    )
    def confluence_server_get_audit_records(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """No description provided."""
        api = get_api()
        response = api.confluence_server_get_audit_records()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_cancel_all_queued_jobs",
        tags={"confluence-server-other"},
    )
    def confluence_server_cancel_all_queued_jobs(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Cancel all queued jobs"""
        api = get_api()
        response = api.confluence_server_cancel_all_queued_jobs()
        return response.model_dump()

    @mcp.tool(name="confluence_server_cancel_job", tags={"confluence-server-other"})
    def confluence_server_cancel_job(
        job_id: str = Field(..., description="id of the backup/restore job"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Cancel job"""
        api = get_api()
        response = api.confluence_server_cancel_job(
            job_id=job_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_site_backup_job",
        tags={"confluence-server-other"},
    )
    def confluence_server_create_site_backup_job(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create site backup job"""
        api = get_api()
        response = api.confluence_server_create_site_backup_job(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_site_restore_job",
        tags={"confluence-server-other"},
    )
    def confluence_server_create_site_restore_job(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create site restore job"""
        api = get_api()
        response = api.confluence_server_create_site_restore_job(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_site_restore_job_for_uploaded_backup_file",
        tags={"confluence-server-other"},
    )
    def confluence_server_create_site_restore_job_for_uploaded_backup_file(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create site restore job for upload backup file"""
        api = get_api()
        response = (
            api.confluence_server_create_site_restore_job_for_uploaded_backup_file(
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_space_backup_job",
        tags={"confluence-server-space"},
    )
    def confluence_server_create_space_backup_job(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create space backup job"""
        api = get_api()
        response = api.confluence_server_create_space_backup_job(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_space_restore_job",
        tags={"confluence-server-space"},
    )
    def confluence_server_create_space_restore_job(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create space restore job"""
        api = get_api()
        response = api.confluence_server_create_space_restore_job(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_space_restore_job_for_uploaded_backup_file",
        tags={"confluence-server-space"},
    )
    def confluence_server_create_space_restore_job_for_uploaded_backup_file(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create space restore job for upload backup file"""
        api = get_api()
        response = (
            api.confluence_server_create_space_restore_job_for_uploaded_backup_file(
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_download_backup_file", tags={"confluence-server-other"}
    )
    def confluence_server_download_backup_file(
        job_id: str = Field(..., description="id of the backup/restore job"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Download backup file"""
        api = get_api()
        response = api.confluence_server_download_backup_file(
            job_id=job_id,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_find_jobs", tags={"confluence-server-other"})
    def confluence_server_find_jobs(
        owner: str | None = Field(
            None, description="userName of user who had created a job."
        ),
        space_key: str | None = Field(
            None, description="the key of the Space the User is attempting to view."
        ),
        from_date: str | None = Field(
            None,
            description="minimum job creation date. Supported date format is `yyyy-MM-ddTHH:mm:ss.SSSZ`",
        ),
        job_states: str | None = Field(
            None,
            description="list of job states. Acceptable values: 'QUEUED', 'PROCESSING', 'FINISHED', 'CANCELLING', 'CANCELLED', 'FAILED'",
        ),
        to_date: str | None = Field(
            None,
            description="maximum job create date. Supported date format is `yyyy-MM-ddTHH:mm:ss.SSSZ`",
        ),
        job_operation: str | None = Field(
            None, description="job operation. Acceptable values: 'BACKUP' and 'RESTORE'"
        ),
        limit: str | None = Field(
            None, description="amount of jobs that should be returned"
        ),
        job_scope: str | None = Field(
            None, description="scope of the job. Acceptable values: 'SPACE' and 'SITE'"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find jobs by filters"""
        api = get_api()
        response = api.confluence_server_find_jobs(
            owner=owner,
            space_key=space_key,
            from_date=from_date,
            job_states=job_states,
            to_date=to_date,
            job_operation=job_operation,
            limit=limit,
            job_scope=job_scope,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_files", tags={"confluence-server-other"})
    def confluence_server_get_files(
        job_scope: str | None = Field(
            None,
            description="name of type of restore job (SITE or SPACE or null), if null, all backup files are listed",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get files in restore directory"""
        api = get_api()
        response = api.confluence_server_get_files(
            job_scope=job_scope,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_job", tags={"confluence-server-other"})
    def confluence_server_get_job(
        job_id: str = Field(..., description="id of the backup/restore job"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get job by ID"""
        api = get_api()
        response = api.confluence_server_get_job(
            job_id=job_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_remove_category", tags={"confluence-server-other"}
    )
    def confluence_server_remove_category(
        space_key: str = Field(
            ..., description="The key of the space to remove the category from"
        ),
        category_name: str = Field(
            ..., description="The name of the category to remove"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove a category from a space"""
        api = get_api()
        response = api.confluence_server_remove_category(
            space_key=space_key,
            category_name=category_name,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_children", tags={"confluence-server-content-child"}
    )
    def confluence_server_children(
        id_: str = Field(
            ..., description="The id of the content to retrieve children for"
        ),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the children",
        ),
        limit: str | None = Field(
            None, description="how many items should be returned after the start index"
        ),
        start: str | None = Field(
            None,
            description="the index of the first item within the result set that should be returned",
        ),
        parent_version: int | None = Field(None, description="Parameter parentVersion"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get children of content"""
        api = get_api()
        response = api.confluence_server_children(
            expand=expand,
            limit=limit,
            start=start,
            id_=id_,
            parent_version=parent_version,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_children_of_type",
        tags={"confluence-server-content-child"},
    )
    def confluence_server_children_of_type(
        id_: str = Field(
            ..., description="The id of the content to retrieve children for"
        ),
        type_: str = Field(..., description="a  content type to filter children on."),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the children",
        ),
        limit: str | None = Field(
            None, description="how many items should be returned after the start index"
        ),
        start: str | None = Field(
            None,
            description="the index of the first item within the result set that should be returned",
        ),
        parent_version: int | None = Field(None, description="Parameter parentVersion"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get children of content by type"""
        api = get_api()
        response = api.confluence_server_children_of_type(
            expand=expand,
            limit=limit,
            start=start,
            id_=id_,
            type_=type_,
            parent_version=parent_version,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_comments_of_content", tags={"confluence-server-content"}
    )
    def confluence_server_comments_of_content(
        id_: str = Field(
            ..., description="The id of the content to retrieve children for"
        ),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the children",
        ),
        depth: str | None = Field(
            None,
            description="(optional, default: '') the depth of the comments. Possible values are: '' (ROOT only), 'all'",
        ),
        limit: str | None = Field(
            None, description="how many items should be returned after the start index"
        ),
        start: str | None = Field(
            None,
            description="the index of the first item within the result set that should be returned",
        ),
        location: str | None = Field(
            None,
            description="(optional, default: '' means all) the location of the comments. Possible values are: 'inline', 'footer', 'resolved'. You can define multiple location params. The results will be the comments matched by any location.",
        ),
        parent_version: int | None = Field(None, description="Parameter parentVersion"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get comments of content"""
        api = get_api()
        response = api.confluence_server_comments_of_content(
            expand=expand,
            depth=depth,
            limit=limit,
            start=start,
            location=location,
            id_=id_,
            parent_version=parent_version,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_publish_shared_draft", tags={"confluence-server-other"}
    )
    def confluence_server_publish_shared_draft(
        draft_id: str = Field(..., description="the id of the draft"),
        expand: str | None = Field(
            None,
            description="A comma separated list of properties to expand on the content. Default value: <code>body.storage,history,space,version,ancestors</code>",
        ),
        status: str | None = Field(
            None, description="only support 'draft' status for now."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Publish shared draft"""
        api = get_api()
        response = api.confluence_server_publish_shared_draft(
            expand=expand,
            draft_id=draft_id,
            status=status,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_publish_legacy_draft", tags={"confluence-server-other"}
    )
    def confluence_server_publish_legacy_draft(
        draft_id: str = Field(..., description="the id of the draft"),
        expand: str | None = Field(
            None,
            description="A comma separated list of properties to expand on the content. Default value: <code>body.storage,history,space,version,ancestors</code>",
        ),
        status: str | None = Field(
            None, description="only support 'draft' status for now."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Publish legacy draft"""
        api = get_api()
        response = api.confluence_server_publish_legacy_draft(
            expand=expand,
            draft_id=draft_id,
            status=status,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_convert", tags={"confluence-server-other"})
    def confluence_server_convert(
        to: str = Field(..., description="the representation to convert to."),
        expand: str | None = Field(
            None,
            description="A comma separated list of properties to expand on the content. Default value: <code>body.storage,history,space,version,ancestors</code>",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Convert body representation"""
        api = get_api()
        response = api.confluence_server_convert(
            expand=expand,
            to=to,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_labels", tags={"confluence-server-other"})
    def confluence_server_labels(
        id_: str = Field(
            ..., description="the id of the content to get the labels for"
        ),
        prefix: str | None = Field(
            None, description="the prefixes to filter the labels with."
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits",
        ),
        start: str | None = Field(
            None, description="he start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get labels"""
        api = get_api()
        response = api.confluence_server_labels(
            prefix=prefix,
            limit=limit,
            start=start,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_add_labels", tags={"confluence-server-other"})
    def confluence_server_add_labels(
        id_: str = Field(
            ..., description="the id of the content to get the labels for"
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add Labels"""
        api = get_api()
        response = api.confluence_server_add_labels(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_delete_label_with_query_param",
        tags={"confluence-server-other"},
    )
    def confluence_server_delete_label_with_query_param(
        id_: str = Field(
            ..., description="the id of the content to get the labels for"
        ),
        name: str | None = Field(
            None, description="the name of the label to be removed from the content"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete label with query param"""
        api = get_api()
        response = api.confluence_server_delete_label_with_query_param(
            name=name,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete_label", tags={"confluence-server-other"})
    def confluence_server_delete_label(
        id_: str = Field(
            ..., description="the id of the content to get the labels for"
        ),
        label: str = Field(
            ..., description="the name of the label to be removed from the content"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete label"""
        api = get_api()
        response = api.confluence_server_delete_label(
            id_=id_,
            label=label,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_find_all", tags={"confluence-server-other"})
    def confluence_server_find_all(
        id_: str = Field(..., description="the id of the content"),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the content properties. Default value: <code>version</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find all content properties"""
        api = get_api()
        response = api.confluence_server_find_all(
            expand=expand,
            limit=limit,
            start=start,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_create_1", tags={"confluence-server-other"})
    def confluence_server_create_1(
        id_: str = Field(..., description="the id of the content"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a content property"""
        api = get_api()
        response = api.confluence_server_create_1(
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_find_by_key", tags={"confluence-server-other"})
    def confluence_server_find_by_key(
        id_: str = Field(..., description="the id of the content"),
        key: str = Field(..., description="the key of the content property. Required."),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the content properties. Default value: <code>version</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find content property by key"""
        api = get_api()
        response = api.confluence_server_find_by_key(
            expand=expand,
            limit=limit,
            id_=id_,
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_update_1", tags={"confluence-server-other"})
    def confluence_server_update_1(
        id_: str = Field(..., description="the id of the content"),
        key: str = Field(..., description="the key of the content property. Required."),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the content properties. Default value: <code>version</code>.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content property"""
        api = get_api()
        response = api.confluence_server_update_1(
            expand=expand,
            id_=id_,
            key=key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_create_2", tags={"confluence-server-other"})
    def confluence_server_create_2(
        id_: str = Field(..., description="the id of the content"),
        key: str = Field(..., description="Parameter key"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """No description provided."""
        api = get_api()
        response = api.confluence_server_create_2(
            id_=id_,
            key=key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete_2", tags={"confluence-server-other"})
    def confluence_server_delete_2(
        id_: str = Field(..., description="the id of the content"),
        key: str = Field(..., description="the key of the content property. Required."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content property"""
        api = get_api()
        response = api.confluence_server_delete_2(
            id_=id_,
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_content", tags={"confluence-server-content"})
    def confluence_server_get_content(
        space_key: str | None = Field(
            None, description="the space key to find content under."
        ),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the content. Default value: <code>history,space,version</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of items to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        posting_day: str | None = Field(
            None,
            description="the posting day of the blog post. Required for <code>blogpost</code> type. Format: <code>yyyy-mm-dd</code>. Example: <code>2013-02-13</code>",
        ),
        ids: str | None = Field(None, description="a list of content ids to fetch."),
        title: str | None = Field(
            None,
            description="the title of the page to find. Required for <code>page</code> type.",
        ),
        type_: str | None = Field(
            None,
            description="the content type to return. Default value: <code>page</code>. Valid values: <code>page, blogpost</code>. All types are returned if fetching via list of IDS",
        ),
        status: str | None = Field(
            None,
            description="list of statuses the content to be found is in. Defaults to current is not specified. If set to 'any', content in 'current' and 'trashed' status will be fetched. Does not support 'historical' status for now.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content"""
        api = get_api()
        response = api.confluence_server_get_content(
            space_key=space_key,
            expand=expand,
            limit=limit,
            start=start,
            posting_day=posting_day,
            ids=ids,
            title=title,
            type_=type_,
            status=status,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_content", tags={"confluence-server-content"}
    )
    def confluence_server_create_content(
        expand: str | None = Field(
            None,
            description="comma separated list of properties to expand on the content. Default value: <code>history,space,version</code>",
        ),
        status: str | None = Field(
            None,
            description="list of Content statuses to filter results on.    Default value: <code>[current]</code>.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create content"""
        api = get_api()
        response = api.confluence_server_create_content(
            expand=expand,
            status=status,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_content_by_id", tags={"confluence-server-content"}
    )
    def confluence_server_get_content_by_id(
        id_: str = Field(..., description="the id of the content."),
        expand: str | None = Field(
            None,
            description="A comma separated list of properties to expand on the content. Default value: <code>history,space,version</code>.    We can also specify some extensions such as <code>extensions.inlineProperties</code> (for getting inline comment-specific properties) or <code>extensions.resolution</code> for the resolution status of each comment in the results",
        ),
        version: str | None = Field(None, description="version of the content."),
        status: str | None = Field(
            None,
            description="list of Content statuses to filter results on.    Default value: <code>[current]</code>.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get content by ID"""
        api = get_api()
        response = api.confluence_server_get_content_by_id(
            expand=expand,
            id_=id_,
            version=version,
            status=status,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete_3", tags={"confluence-server-other"})
    def confluence_server_delete_3(
        id_: str = Field(..., description="the id of the content."),
        status: str | None = Field(
            None, description="the status of the content to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content"""
        api = get_api()
        response = api.confluence_server_delete_3(
            id_=id_,
            status=status,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_history", tags={"confluence-server-other"})
    def confluence_server_get_history(
        id_: str = Field(..., description="the id of the content."),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the content. Default value: <code>previousVersion,nextVersion,lastUpdated</code>.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get history of content"""
        api = get_api()
        response = api.confluence_server_get_history(
            expand=expand,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_macro_body_by_hash",
        tags={"confluence-server-other"},
    )
    def confluence_server_get_macro_body_by_hash(
        id_: str = Field(..., description="the id of the content."),
        version: str = Field(
            ..., description="the version of the content which the hash belongs."
        ),
        hash: str = Field(..., description="the macroId to find the correct macro."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get macro body by hash"""
        api = get_api()
        response = api.confluence_server_get_macro_body_by_hash(
            id_=id_,
            version=version,
            hash=hash,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_macro_body_by_macro_id",
        tags={"confluence-server-other"},
    )
    def confluence_server_get_macro_body_by_macro_id(
        macro_id: str = Field(
            ..., description="the macroId to find the correct macro."
        ),
        id_: str = Field(..., description="the id of the content."),
        version: str = Field(
            ..., description="the version of the content which the hash belongs."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get macro body by macro ID"""
        api = get_api()
        response = api.confluence_server_get_macro_body_by_macro_id(
            macro_id=macro_id,
            id_=id_,
            version=version,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_scan_content", tags={"confluence-server-content"})
    def confluence_server_scan_content(
        cursor: str | None = Field(
            None,
            description="the identifier which is used to skip results from a previous query when paginating. Cursor is empty in first request, to move forward or backward use cursor provided in response.",
        ),
        space_key: str | None = Field(
            None, description="the space key to find content under."
        ),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the content. Default value: <code>history,space,version</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of items to return, this may be restricted by fixed system limits.",
        ),
        type_: str | None = Field(
            None,
            description="the content type to return. Default value: <code>page</code>. Valid values: <code>page, blogpost, comment</code>. All types are returned if fetching via list of IDS. Type is only required for first request, latest request will use cursor",
        ),
        status: str | None = Field(
            None,
            description="list of statuses the content to be found is in. Defaults to current is not specified. If set to 'any', content in 'current' and 'trashed' status will be fetched. Does not support 'historical' status for now.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Scan content by space key"""
        api = get_api()
        response = api.confluence_server_scan_content(
            cursor=cursor,
            space_key=space_key,
            expand=expand,
            limit=limit,
            type_=type_,
            status=status,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_search", tags={"confluence-server-other"})
    def confluence_server_search(
        cqlcontext: str | None = Field(
            None,
            description="the context to execute a cql search in, this is the json serialized form of SearchContext",
        ),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the content. Default value: <code>history,space,version</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of items to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        cql: str | None = Field(
            None, description="a cql query string to use to locate content."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search content using CQL"""
        api = get_api()
        response = api.confluence_server_search(
            cqlcontext=cqlcontext,
            expand=expand,
            limit=limit,
            start=start,
            cql=cql,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_update_2", tags={"confluence-server-other"})
    def confluence_server_update_2(
        content_id: str = Field(..., description="the id of the content."),
        async_reconciliation: bool | None = Field(
            None, description="Parameter asyncReconciliation"
        ),
        conflict_policy: str | None = Field(
            None, description="the conflict policy, default value: <code>abort<code>"
        ),
        status: str | None = Field(
            None, description="the existing status of the content to be updated."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update content"""
        api = get_api()
        response = api.confluence_server_update_2(
            async_reconciliation=async_reconciliation,
            conflict_policy=conflict_policy,
            content_id=content_id,
            status=status,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_by_operation", tags={"confluence-server-other"})
    def confluence_server_by_operation(
        id_: str = Field(..., description="The id of the content"),
        expand: str | None = Field(
            None,
            description="A comma separated list of properties to expand on the content properties. Default value: group.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all restrictions by Operation"""
        api = get_api()
        response = api.confluence_server_by_operation(
            expand=expand,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_for_operation", tags={"confluence-server-other"})
    def confluence_server_for_operation(
        operation_key: str = Field(..., description="key of the operation."),
        id_: str = Field(..., description="The id of the content"),
        expand: str | None = Field(
            None,
            description="Aa comma separated list of properties to expand on the content properties. Default value: group.",
        ),
        limit: str | None = Field(None, description="pagination limit."),
        start: str | None = Field(None, description="pagination start."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all restrictions for given operation"""
        api = get_api()
        response = api.confluence_server_for_operation(
            operation_key=operation_key,
            expand=expand,
            limit=limit,
            start=start,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_relevant_view_restrictions",
        tags={"confluence-server-other"},
    )
    def confluence_server_relevant_view_restrictions(
        id_: str = Field(..., description="The id of the content"),
        expand: str | None = Field(
            None,
            description="A comma separated list of properties to expand on the content properties. Default value: relevantViewRestrictions",
        ),
        limit: str | None = Field(
            None, description="pagination limit, Max 50 per page"
        ),
        start: str | None = Field(None, description="pagination start."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all view restriction both direct and inherited."""
        api = get_api()
        response = api.confluence_server_relevant_view_restrictions(
            expand=expand,
            limit=limit,
            start=start,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_update_restrictions", tags={"confluence-server-other"}
    )
    def confluence_server_update_restrictions(
        id_: str = Field(..., description="The id of the content"),
        expand: str | None = Field(
            None,
            description="A comma separated list of properties to expand in the response. Default is <code>restrictions.user, restrictions.group</code> Default value: group.",
        ),
        limit: str | None = Field(None, description="pagination limit."),
        start: str | None = Field(None, description="pagination start."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update restrictions"""
        api = get_api()
        response = api.confluence_server_update_restrictions(
            expand=expand,
            limit=limit,
            start=start,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_delete_content_history",
        tags={"confluence-server-content-history"},
    )
    def confluence_server_delete_content_history(
        id_: str = Field(..., description="The id of the content"),
        version_number: str = Field(
            ..., description="version number starts from 1 up to current version."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete content history"""
        api = get_api()
        response = api.confluence_server_delete_content_history(
            id_=id_,
            version_number=version_number,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_index", tags={"confluence-server-other"})
    def confluence_server_index(
        content_id: str = Field(
            ...,
            description="the ID of the Content the User is attempting to view the watchers for.",
        ),
        limit: str | None = Field(
            None,
            description="The limit of the number of users to return, this may be restricted by fixed system limit.",
        ),
        start: str | None = Field(
            None, description="The start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Fetch users watching a given content"""
        api = get_api()
        response = api.confluence_server_index(
            content_id=content_id,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_descendants", tags={"confluence-server-other"})
    def confluence_server_descendants(
        id_: str = Field(
            ...,
            description="the ID of the Content the User is attempting to view the descendants for.",
        ),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the descendants.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get Descendants"""
        api = get_api()
        response = api.confluence_server_descendants(
            expand=expand,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_descendants_of_type", tags={"confluence-server-other"}
    )
    def confluence_server_descendants_of_type(
        id_: str = Field(
            ...,
            description="the ID of the Content the User is attempting to view the descendants for.",
        ),
        type_: str = Field(..., description="content type to filter descendants on."),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the descendants.",
        ),
        limit: str | None = Field(
            None,
            description="(optional, default: site limit) how many items should be returned after the start index.",
        ),
        start: str | None = Field(
            None,
            description="(optional, default: 0) the index of the first item within the result set that should be returned.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get descendants of type"""
        api = get_api()
        response = api.confluence_server_descendants_of_type(
            expand=expand,
            limit=limit,
            start=start,
            id_=id_,
            type_=type_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_default_color_scheme",
        tags={"confluence-server-other"},
    )
    def confluence_server_get_default_color_scheme(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get default global color scheme"""
        api = get_api()
        response = api.confluence_server_get_default_color_scheme()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_global_color_scheme",
        tags={"confluence-server-other"},
    )
    def confluence_server_get_global_color_scheme(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get global color scheme"""
        api = get_api()
        response = api.confluence_server_get_global_color_scheme()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_update_color_scheme", tags={"confluence-server-other"}
    )
    def confluence_server_update_color_scheme(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set global color scheme"""
        api = get_api()
        response = api.confluence_server_update_color_scheme(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_reset_global_color_scheme",
        tags={"confluence-server-other"},
    )
    def confluence_server_reset_global_color_scheme(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset global color scheme"""
        api = get_api()
        response = api.confluence_server_reset_global_color_scheme()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_all_global_permissions",
        tags={"confluence-server-other"},
    )
    def confluence_server_get_all_global_permissions(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get global permissions"""
        api = get_api()
        response = api.confluence_server_get_all_global_permissions()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_permissions_granted_to_anonymous_users",
        tags={"confluence-server-user"},
    )
    def confluence_server_get_permissions_granted_to_anonymous_users(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Gets the permissions granted to an anonymous user"""
        api = get_api()
        response = api.confluence_server_get_permissions_granted_to_anonymous_users()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_permissions_granted_to_group",
        tags={"confluence-server-group"},
    )
    def confluence_server_get_permissions_granted_to_group(
        group_name: str = Field(..., description="Parameter groupName"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Gets global permissions granted to a group"""
        api = get_api()
        response = api.confluence_server_get_permissions_granted_to_group(
            group_name=group_name,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_permissions_granted_to_unlicensed_users",
        tags={"confluence-server-user"},
    )
    def confluence_server_get_permissions_granted_to_unlicensed_users(
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Gets the permissions granted to an unlicensed users"""
        api = get_api()
        response = api.confluence_server_get_permissions_granted_to_unlicensed_users()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_permissions_granted_to_user",
        tags={"confluence-server-user"},
    )
    def confluence_server_get_permissions_granted_to_user(
        user_key: str = Field(..., description="Parameter userKey"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Gets global permissions granted to a user"""
        api = get_api()
        response = api.confluence_server_get_permissions_granted_to_user(
            user_key=user_key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_find_webhooks", tags={"confluence-server-other"})
    def confluence_server_find_webhooks(
        limit: str | None = Field(
            None,
            description="the limit of the number of items to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return"
        ),
        event: str | None = Field(
            None, description="list of webhook event ids to filter for"
        ),
        statistics: str | None = Field(
            None, description="if statistics should be provided for all found webhooks."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Find webhooks"""
        api = get_api()
        response = api.confluence_server_find_webhooks(
            limit=limit,
            start=start,
            event=event,
            statistics=statistics,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_create_webhook", tags={"confluence-server-other"})
    def confluence_server_create_webhook(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create webhook"""
        api = get_api()
        response = api.confluence_server_create_webhook(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_webhook", tags={"confluence-server-other"})
    def confluence_server_get_webhook(
        webhook_id: str = Field(..., description="id of the webhook"),
        statistics: bool | None = Field(None, description="Parameter statistics"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get webhook"""
        api = get_api()
        response = api.confluence_server_get_webhook(
            webhook_id=webhook_id,
            statistics=statistics,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_update_webhook", tags={"confluence-server-other"})
    def confluence_server_update_webhook(
        webhook_id: str = Field(..., description="the existing webhook id"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update webhook"""
        api = get_api()
        response = api.confluence_server_update_webhook(
            webhook_id=webhook_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete_webhook", tags={"confluence-server-other"})
    def confluence_server_delete_webhook(
        webhook_id: str = Field(
            ..., description="the id of the webhook to be deleted."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete webhook"""
        api = get_api()
        response = api.confluence_server_delete_webhook(
            webhook_id=webhook_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_latest_invocation", tags={"confluence-server-other"}
    )
    def confluence_server_get_latest_invocation(
        webhook_id: str = Field(..., description="id of the webhook"),
        outcomes: str | None = Field(
            None,
            description="the outcome to filter for. Can be SUCCESS, FAILURE, ERROR. None specified means that the all will be considered.",
        ),
        event: str | None = Field(
            None,
            description="the string id of a specific event to retrieve the last invocation for.",
        ),
        outcome: list[Any] | None = Field(None, description="Parameter outcome"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get latest invocations"""
        api = get_api()
        response = api.confluence_server_get_latest_invocation(
            webhook_id=webhook_id,
            outcomes=outcomes,
            event=event,
            outcome=outcome,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_statistics", tags={"confluence-server-other"})
    def confluence_server_get_statistics(
        webhook_id: str = Field(..., description="id of the webhook"),
        event: str | None = Field(
            None,
            description="the string id of a specific event to retrieve the last invocation for.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get statistic"""
        api = get_api()
        response = api.confluence_server_get_statistics(
            webhook_id=webhook_id,
            event=event,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_statistics_summary",
        tags={"confluence-server-other"},
    )
    def confluence_server_get_statistics_summary(
        webhook_id: str = Field(..., description="id of the webhook"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get statistics summary"""
        api = get_api()
        response = api.confluence_server_get_statistics_summary(
            webhook_id=webhook_id,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_test_webhook", tags={"confluence-server-other"})
    def confluence_server_test_webhook(
        url: str = Field(..., description="the url in which to connect to"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Test webhook"""
        api = get_api()
        response = api.confluence_server_test_webhook(
            url=url,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_ancestor_groups", tags={"confluence-server-group"}
    )
    def confluence_server_get_ancestor_groups(
        group_name: str = Field(..., description="Parameter groupName"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group ancestor of a group"""
        api = get_api()
        response = api.confluence_server_get_ancestor_groups(
            group_name=group_name,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_ancestor_groups_by_group_name",
        tags={"confluence-server-group"},
    )
    def confluence_server_get_ancestor_groups_by_group_name(
        group_name: str | None = Field(None, description="Parameter groupName"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group ancestor of a group"""
        api = get_api()
        response = api.confluence_server_get_ancestor_groups_by_group_name(
            group_name=group_name,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_group", tags={"confluence-server-group"})
    def confluence_server_get_group(
        group_name: str = Field(..., description="Parameter groupName"),
        expand: str | None = Field(None, description="Parameter expand"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group by name"""
        api = get_api()
        response = api.confluence_server_get_group(
            expand=expand,
            group_name=group_name,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_group_by_group_name",
        tags={"confluence-server-group"},
    )
    def confluence_server_get_group_by_group_name(
        expand: str | None = Field(None, description="Parameter expand"),
        group_name: str | None = Field(None, description="Parameter groupName"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group by name"""
        api = get_api()
        response = api.confluence_server_get_group_by_group_name(
            expand=expand,
            group_name=group_name,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_groups", tags={"confluence-server-group"})
    def confluence_server_get_groups(
        expand: str | None = Field(None, description="Parameter expand"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get groups"""
        api = get_api()
        response = api.confluence_server_get_groups(
            expand=expand,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_members", tags={"confluence-server-other"})
    def confluence_server_get_members(
        group_name: str = Field(..., description="Parameter groupName"),
        expand: str | None = Field(None, description="Parameter expand"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get members of group"""
        api = get_api()
        response = api.confluence_server_get_members(
            expand=expand,
            group_name=group_name,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_members_by_group_name",
        tags={"confluence-server-group"},
    )
    def confluence_server_get_members_by_group_name(
        expand: str | None = Field(None, description="Parameter expand"),
        group_name: str | None = Field(None, description="Parameter groupName"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get members of group"""
        api = get_api()
        response = api.confluence_server_get_members_by_group_name(
            expand=expand,
            group_name=group_name,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_nested_group_members",
        tags={"confluence-server-group"},
    )
    def confluence_server_get_nested_group_members(
        group_name: str = Field(..., description="Parameter groupName"),
        expand: str | None = Field(None, description="Parameter expand"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group members of group"""
        api = get_api()
        response = api.confluence_server_get_nested_group_members(
            expand=expand,
            group_name=group_name,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_nested_group_members_by_group_name",
        tags={"confluence-server-group"},
    )
    def confluence_server_get_nested_group_members_by_group_name(
        expand: str | None = Field(None, description="Parameter expand"),
        group_name: str | None = Field(None, description="Parameter groupName"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group members of group"""
        api = get_api()
        response = api.confluence_server_get_nested_group_members_by_group_name(
            expand=expand,
            group_name=group_name,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_parent_groups", tags={"confluence-server-group"}
    )
    def confluence_server_get_parent_groups(
        group_name: str = Field(..., description="Parameter groupName"),
        expand: str | None = Field(None, description="Parameter expand"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group parents of a group"""
        api = get_api()
        response = api.confluence_server_get_parent_groups(
            expand=expand,
            group_name=group_name,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_parent_groups_by_group_name",
        tags={"confluence-server-group"},
    )
    def confluence_server_get_parent_groups_by_group_name(
        expand: str | None = Field(None, description="Parameter expand"),
        group_name: str | None = Field(None, description="Parameter groupName"),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get group parents of a group"""
        api = get_api()
        response = api.confluence_server_get_parent_groups_by_group_name(
            expand=expand,
            group_name=group_name,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_index_1", tags={"confluence-server-other"})
    def confluence_server_index_1(_ctx: Context | None = None) -> dict[str, Any]:
        """Get instance metrics"""
        api = get_api()
        response = api.confluence_server_index_1()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_related_labels", tags={"confluence-server-other"}
    )
    def confluence_server_get_related_labels(
        label_name: str = Field(
            ..., description="the name of the label (namespace prefixes permitted)."
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        limit: str | None = Field(
            None,
            description="the maximum number of related labels to return. Default to be 100.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get related labels, currently returning global labels only."""
        api = get_api()
        response = api.confluence_server_get_related_labels(
            start=start,
            limit=limit,
            label_name=label_name,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_recent", tags={"confluence-server-other"})
    def confluence_server_recent(
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get recently used labels"""
        api = get_api()
        response = api.confluence_server_recent(
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_task", tags={"confluence-server-other"})
    def confluence_server_get_task(
        id_: str = Field(..., description="the key of the task to be returned."),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the task.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get task by ID"""
        api = get_api()
        response = api.confluence_server_get_task(
            expand=expand,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_tasks", tags={"confluence-server-other"})
    def confluence_server_get_tasks(
        expand: str | None = Field(
            None,
            description="comma separated list of properties to expand on the tasks.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of items to return, this may be restricted by fixed system limits",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get tasks"""
        api = get_api()
        response = api.confluence_server_get_tasks(
            expand=expand,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_search_1", tags={"confluence-server-other"})
    def confluence_server_search_1(
        cqlcontext: str | None = Field(
            None,
            description="the execution context for CQL functions, provides current space key and content id. If this is not provided some CQL functions will not be available.",
        ),
        expand: str | None = Field(
            None,
            description="the properties to expand on the search result, this may cause database requests for some properties",
        ),
        include_archived_spaces: str | None = Field(
            None,
            description="whether to include content in archived spaces in the result, this defaults to false.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of items to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None, description="he start point of the collection to return."
        ),
        excerpt: str | None = Field(
            None,
            description="the excerpt strategy to apply to the result, one of : indexed, highlight, none. This defaults to highlight.",
        ),
        cql: str | None = Field(
            None,
            description="the CQL query see <a href='https://developer.atlassian.com/confdev/confluence-rest-api/advanced-searching-using-cql'>advanced searching in confluence using CQL</a>",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Search for entities in confluence"""
        api = get_api()
        response = api.confluence_server_search_1(
            cqlcontext=cqlcontext,
            expand=expand,
            include_archived_spaces=include_archived_spaces,
            limit=limit,
            start=start,
            excerpt=excerpt,
            cql=cql,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_index_2", tags={"confluence-server-other"})
    def confluence_server_index_2(_ctx: Context | None = None) -> dict[str, Any]:
        """Get server information"""
        api = get_api()
        response = api.confluence_server_index_2()
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_color_scheme_type", tags={"confluence-server-other"}
    )
    def confluence_server_get_color_scheme_type(
        space_key: str = Field(
            ..., description="Space key of the space to request color scheme type for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get Space color scheme type"""
        api = get_api()
        response = api.confluence_server_get_color_scheme_type(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_update_color_scheme_type",
        tags={"confluence-server-other"},
    )
    def confluence_server_update_color_scheme_type(
        space_key: str = Field(
            ..., description="space key of the space to update color scheme type for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update Space color scheme type"""
        api = get_api()
        response = api.confluence_server_update_color_scheme_type(
            space_key=space_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_space_color_scheme",
        tags={"confluence-server-space"},
    )
    def confluence_server_get_space_color_scheme(
        space_key: str = Field(
            ..., description="space key of the space to request color scheme for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get Space color scheme"""
        api = get_api()
        response = api.confluence_server_get_space_color_scheme(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_update_space_color_scheme",
        tags={"confluence-server-space"},
    )
    def confluence_server_update_space_color_scheme(
        space_key: str = Field(
            ..., description="space key of the space to set color scheme for."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update Space color scheme"""
        api = get_api()
        response = api.confluence_server_update_space_color_scheme(
            space_key=space_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_reset_space_color_scheme",
        tags={"confluence-server-space"},
    )
    def confluence_server_reset_space_color_scheme(
        space_key: str = Field(
            ..., description="Space key of the space to reset color scheme for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Reset Space color scheme"""
        api = get_api()
        response = api.confluence_server_reset_space_color_scheme(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_index_3", tags={"confluence-server-other"})
    def confluence_server_index_3(
        space_key: str = Field(
            ..., description="a string containing the key of the space"
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Fetch all labels"""
        api = get_api()
        response = api.confluence_server_index_3(
            space_key=space_key,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_popular", tags={"confluence-server-other"})
    def confluence_server_popular(
        space_key: str = Field(
            ..., description="a string containing the key of the space"
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get popular labels"""
        api = get_api()
        response = api.confluence_server_popular(
            space_key=space_key,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_recent_1", tags={"confluence-server-other"})
    def confluence_server_recent_1(
        space_key: str = Field(
            ..., description="a string containing the key of the space"
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get recent labels"""
        api = get_api()
        response = api.confluence_server_recent_1(
            space_key=space_key,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_related", tags={"confluence-server-other"})
    def confluence_server_related(
        space_key: str = Field(
            ..., description="a string containing the key of the space"
        ),
        label_name: str = Field(
            ..., description="a string containing the name of the label"
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits",
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get related labels"""
        api = get_api()
        response = api.confluence_server_related(
            space_key=space_key,
            limit=limit,
            start=start,
            label_name=label_name,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_all_space_permissions",
        tags={"confluence-server-space-permission"},
    )
    def confluence_server_get_all_space_permissions(
        space_key: str = Field(..., description="Parameter spaceKey"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get all space permissions"""
        api = get_api()
        response = api.confluence_server_get_all_space_permissions(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_set_permissions", tags={"confluence-server-other"}
    )
    def confluence_server_set_permissions(
        space_key: str = Field(..., description="Parameter spaceKey"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Set permissions to multiple users/groups/anonymous user in the given space"""
        api = get_api()
        response = api.confluence_server_set_permissions(
            space_key=space_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_permissions_granted_to_anonymous_users_1",
        tags={"confluence-server-user"},
    )
    def confluence_server_get_permissions_granted_to_anonymous_users_1(
        space_key: str = Field(..., description="Parameter spaceKey"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Gets the permissions granted to an anonymous user in a space"""
        api = get_api()
        response = api.confluence_server_get_permissions_granted_to_anonymous_users_1(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_permissions_granted_to_group_1",
        tags={"confluence-server-group"},
    )
    def confluence_server_get_permissions_granted_to_group_1(
        space_key: str = Field(..., description="Parameter spaceKey"),
        group_name: str = Field(..., description="Parameter groupName"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Gets the permissions granted to a group in a space"""
        api = get_api()
        response = api.confluence_server_get_permissions_granted_to_group_1(
            space_key=space_key,
            group_name=group_name,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_get_permissions_granted_to_user_1",
        tags={"confluence-server-user"},
    )
    def confluence_server_get_permissions_granted_to_user_1(
        space_key: str = Field(..., description="Parameter spaceKey"),
        user_key: str = Field(..., description="Parameter userKey"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Gets the permissions granted to a user in a space"""
        api = get_api()
        response = api.confluence_server_get_permissions_granted_to_user_1(
            space_key=space_key,
            user_key=user_key,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_grant_permissions_to_anonymous_users",
        tags={"confluence-server-user"},
    )
    def confluence_server_grant_permissions_to_anonymous_users(
        space_key: str = Field(..., description="Parameter spaceKey"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Grants space permissions to anonymous user"""
        api = get_api()
        response = api.confluence_server_grant_permissions_to_anonymous_users(
            space_key=space_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_grant_permissions_to_group",
        tags={"confluence-server-group"},
    )
    def confluence_server_grant_permissions_to_group(
        space_key: str = Field(..., description="Parameter spaceKey"),
        group_name: str = Field(..., description="Parameter groupName"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Grants space permissions to a group"""
        api = get_api()
        response = api.confluence_server_grant_permissions_to_group(
            space_key=space_key,
            group_name=group_name,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_grant_permissions_to_user",
        tags={"confluence-server-user"},
    )
    def confluence_server_grant_permissions_to_user(
        space_key: str = Field(..., description="Parameter spaceKey"),
        user_key: str = Field(..., description="Parameter userKey"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Grants space permissions to a user"""
        api = get_api()
        response = api.confluence_server_grant_permissions_to_user(
            space_key=space_key,
            user_key=user_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_revoke_permissions_from_anonymous_user",
        tags={"confluence-server-user"},
    )
    def confluence_server_revoke_permissions_from_anonymous_user(
        space_key: str = Field(..., description="Parameter spaceKey"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Revoke space permissions from anonymous user"""
        api = get_api()
        response = api.confluence_server_revoke_permissions_from_anonymous_user(
            space_key=space_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_revoke_permissions_from_group",
        tags={"confluence-server-group"},
    )
    def confluence_server_revoke_permissions_from_group(
        space_key: str = Field(..., description="Parameter spaceKey"),
        group_name: str = Field(..., description="Parameter groupName"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Revoke space permissions from a group"""
        api = get_api()
        response = api.confluence_server_revoke_permissions_from_group(
            space_key=space_key,
            group_name=group_name,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_revoke_permissions_from_user",
        tags={"confluence-server-user"},
    )
    def confluence_server_revoke_permissions_from_user(
        space_key: str = Field(..., description="Parameter spaceKey"),
        user_key: str = Field(..., description="Parameter userKey"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Revoke space permissions from a user"""
        api = get_api()
        response = api.confluence_server_revoke_permissions_from_user(
            space_key=space_key,
            user_key=user_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_1", tags={"confluence-server-other"})
    def confluence_server_get_1(
        space_key: str = Field(..., description="The key of the space"),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the space properties. Default value: <code>version</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of items to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None, description="he start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space properties"""
        api = get_api()
        response = api.confluence_server_get_1(
            space_key=space_key,
            expand=expand,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_create_3", tags={"confluence-server-other"})
    def confluence_server_create_3(
        space_key: str = Field(..., description="The key of the space"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a space property"""
        api = get_api()
        response = api.confluence_server_create_3(
            space_key=space_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get", tags={"confluence-server-other"})
    def confluence_server_get(
        space_key: str = Field(..., description="The key of the space"),
        key: str = Field(..., description="Parameter key"),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the space properties. Default value: <code>version</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of items to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None, description="he start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space property by key"""
        api = get_api()
        response = api.confluence_server_get(
            space_key=space_key,
            expand=expand,
            limit=limit,
            start=start,
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_update_3", tags={"confluence-server-other"})
    def confluence_server_update_3(
        space_key: str = Field(..., description="The key of the space"),
        key: str = Field(..., description="the key of the property"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update space property"""
        api = get_api()
        response = api.confluence_server_update_3(
            space_key=space_key,
            key=key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_create_4", tags={"confluence-server-other"})
    def confluence_server_create_4(
        space_key: str = Field(..., description="The key of the space"),
        key: str = Field(..., description="property key of the property to be created"),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a space property with a specific key"""
        api = get_api()
        response = api.confluence_server_create_4(
            space_key=space_key,
            key=key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete_4", tags={"confluence-server-other"})
    def confluence_server_delete_4(
        space_key: str = Field(..., description="The key of the space"),
        key: str = Field(..., description="the key of the property."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete space property"""
        api = get_api()
        response = api.confluence_server_delete_4(
            space_key=space_key,
            key=key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_archive", tags={"confluence-server-other"})
    def confluence_server_archive(
        space_key: str = Field(..., description="the key of the space to update."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Archive space"""
        api = get_api()
        response = api.confluence_server_archive(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_contents", tags={"confluence-server-content"})
    def confluence_server_contents(
        space_key: str = Field(..., description="the key of the space to update."),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the space.",
        ),
        depth: str | None = Field(
            None,
            description="a string indicating if all content, or just the root content of the space is returned. Default value: <code>all</code>. Valid values: <code>all, root</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None, description="he start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get contents in space"""
        api = get_api()
        response = api.confluence_server_contents(
            space_key=space_key,
            expand=expand,
            depth=depth,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_contents_with_type", tags={"confluence-server-content"}
    )
    def confluence_server_contents_with_type(
        space_key: str = Field(..., description="the key of the space to update."),
        type_: str = Field(
            ...,
            description="the type of content to return with the space. Valid values: <code>page, blogpost</code>.",
        ),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the space.",
        ),
        depth: str | None = Field(
            None,
            description="a string indicating if all content, or just the root content of the space is returned. Default value: <code>all</code>. Valid values: <code>all, root</code>.",
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of labels to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None, description="he start point of the collection to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get contents by type"""
        api = get_api()
        response = api.confluence_server_contents_with_type(
            space_key=space_key,
            expand=expand,
            depth=depth,
            limit=limit,
            start=start,
            type_=type_,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_create_private_space", tags={"confluence-server-space"}
    )
    def confluence_server_create_private_space(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create private space"""
        api = get_api()
        response = api.confluence_server_create_private_space(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_spaces", tags={"confluence-server-space"})
    def confluence_server_spaces(
        space_key_single: str | None = Field(
            None, description="Parameter spaceKeySingle"
        ),
        start: str | None = Field(
            None, description="the start point of the collection to return."
        ),
        label: str | None = Field(
            None, description="filter the list of spaces returned by label."
        ),
        favourite: str | None = Field(
            None, description="filter the list of spaces returned by favourites."
        ),
        type_: str | None = Field(
            None,
            description="filter the list of spaces returned by type (global, personal).",
        ),
        space_key: str | None = Field(
            None, description="the key of the space to fetch information from."
        ),
        space_id: list[Any] | None = Field(None, description="Parameter spaceId"),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the spaces.",
        ),
        has_retention_policy: str | None = Field(
            None, description="filter the list of spaces returned by retention policy."
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of spaces to return, this may be restricted by fixed system limits",
        ),
        space_keys: str | None = Field(
            None, description="the keys of the spaces to fetch information from."
        ),
        content_label: str | None = Field(
            None,
            description="filter the list of spaces returned by content containing provided label.",
        ),
        space_ids: str | None = Field(
            None,
            description="the ids of the spaces to fetch information from. Cannot be used in conjunction with spaceKey(s)",
        ),
        status: str | None = Field(
            None,
            description="filter the list of spaces returned by status (current, archived).",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get spaces by key"""
        api = get_api()
        response = api.confluence_server_spaces(
            space_key_single=space_key_single,
            start=start,
            label=label,
            favourite=favourite,
            type_=type_,
            space_key=space_key,
            space_id=space_id,
            expand=expand,
            has_retention_policy=has_retention_policy,
            limit=limit,
            space_keys=space_keys,
            content_label=content_label,
            space_ids=space_ids,
            status=status,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_create_space", tags={"confluence-server-space"})
    def confluence_server_create_space(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Creates a new Space."""
        api = get_api()
        response = api.confluence_server_create_space(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_space", tags={"confluence-server-space"})
    def confluence_server_space(
        space_key: str = Field(..., description="the key of the space to update."),
        expand: str | None = Field(
            None,
            description="a comma separated list of properties to expand on the space.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get space"""
        api = get_api()
        response = api.confluence_server_space(
            space_key=space_key,
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_update_4", tags={"confluence-server-other"})
    def confluence_server_update_4(
        space_key: str = Field(..., description="the key of the space to update."),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update Space"""
        api = get_api()
        response = api.confluence_server_update_4(
            space_key=space_key,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete_5", tags={"confluence-server-other"})
    def confluence_server_delete_5(
        space_key: str = Field(..., description="the key of the space to update."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete Space"""
        api = get_api()
        response = api.confluence_server_delete_5(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_restore", tags={"confluence-server-other"})
    def confluence_server_restore(
        space_key: str = Field(..., description="the key of the space to update."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Restore space"""
        api = get_api()
        response = api.confluence_server_restore(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_trash", tags={"confluence-server-other"})
    def confluence_server_trash(
        space_key: str = Field(..., description="the key of the space to update."),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove all trash contents"""
        api = get_api()
        response = api.confluence_server_trash(
            space_key=space_key,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_index_4", tags={"confluence-server-other"})
    def confluence_server_index_4(
        space_key: str = Field(
            ..., description="the key of the Space the User is attempting to view."
        ),
        limit: int | None = Field(None, description="Parameter limit"),
        start: int | None = Field(None, description="Parameter start"),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Fetch users watching space"""
        api = get_api()
        response = api.confluence_server_index_4(
            space_key=space_key,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_update_5", tags={"confluence-server-other"})
    def confluence_server_update_5(
        group_name: str = Field(
            ..., description="The group name identifying the given group."
        ),
        username: str = Field(
            ..., description="The username identifying the given user."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update user group"""
        api = get_api()
        response = api.confluence_server_update_5(
            group_name=group_name,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_delete_6", tags={"confluence-server-other"})
    def confluence_server_delete_6(
        group_name: str = Field(
            ..., description="The group name identifying the given group."
        ),
        username: str = Field(
            ..., description="The username identifying the given user."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete user group"""
        api = get_api()
        response = api.confluence_server_delete_6(
            group_name=group_name,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_change_password_1", tags={"confluence-server-other"}
    )
    def confluence_server_change_password_1(
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Change password"""
        api = get_api()
        response = api.confluence_server_change_password_1(
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_anonymous", tags={"confluence-server-other"})
    def confluence_server_get_anonymous(
        expand: str | None = Field(
            None, description="properties to expand on the user."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get information about anonymous user type"""
        api = get_api()
        response = api.confluence_server_get_anonymous(
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_current", tags={"confluence-server-other"})
    def confluence_server_get_current(
        expand: str | None = Field(
            None, description="properties to expand on the user."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get current user"""
        api = get_api()
        response = api.confluence_server_get_current(
            expand=expand,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_groups_1", tags={"confluence-server-group"})
    def confluence_server_get_groups_1(
        expand: str | None = Field(
            None, description="properties to expand on the user."
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of users to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None,
            description="the start point of the collection to return. This must be non-negative. Default value is 0.",
        ),
        key: str | None = Field(
            None, description="userkey of the user to request from this resource"
        ),
        username: str | None = Field(
            None, description="userName of the user to get the groups for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get groups"""
        api = get_api()
        response = api.confluence_server_get_groups_1(
            expand=expand,
            limit=limit,
            start=start,
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_user", tags={"confluence-server-user"})
    def confluence_server_get_user(
        expand: str | None = Field(
            None, description="properties to expand on the user."
        ),
        key: str | None = Field(
            None, description="userkey of the user to request from this resource."
        ),
        username: str | None = Field(
            None, description="userName of the user to create the new watcher for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get user"""
        api = get_api()
        response = api.confluence_server_get_user(
            expand=expand,
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(name="confluence_server_get_users", tags={"confluence-server-user"})
    def confluence_server_get_users(
        expand: str | None = Field(
            None, description="properties to expand on the user."
        ),
        limit: str | None = Field(
            None,
            description="the limit of the number of users to return, this may be restricted by fixed system limits.",
        ),
        start: str | None = Field(
            None,
            description="the start point of the collection to return. This must be non-negative. Default value is 0.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get registered users"""
        api = get_api()
        response = api.confluence_server_get_users(
            expand=expand,
            limit=limit,
            start=start,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_is_watching_content", tags={"confluence-server-content"}
    )
    def confluence_server_is_watching_content(
        content_id: str = Field(..., description="id of the content."),
        key: str | None = Field(
            None, description="userkey of the user to check for watching state."
        ),
        username: str | None = Field(
            None, description="username of the user to check for watching state."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get information about content watcher"""
        api = get_api()
        response = api.confluence_server_is_watching_content(
            content_id=content_id,
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_add_content_watcher", tags={"confluence-server-content"}
    )
    def confluence_server_add_content_watcher(
        content_id: str = Field(..., description="id of the content."),
        key: str | None = Field(
            None, description="userkey of the user to check for watching state."
        ),
        username: str | None = Field(
            None, description="username of the user to check for watching state."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add content watcher"""
        api = get_api()
        response = api.confluence_server_add_content_watcher(
            content_id=content_id,
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_remove_content_watcher",
        tags={"confluence-server-content"},
    )
    def confluence_server_remove_content_watcher(
        content_id: str = Field(..., description="id of the content."),
        key: str | None = Field(
            None, description="userkey of the user to check for watching state."
        ),
        username: str | None = Field(
            None, description="username of the user to check for watching state."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove content watcher"""
        api = get_api()
        response = api.confluence_server_remove_content_watcher(
            content_id=content_id,
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_is_watching_space", tags={"confluence-server-space"}
    )
    def confluence_server_is_watching_space(
        space_key: str = Field(..., description="Parameter spaceKey"),
        content_type: str | None = Field(
            None, description="an optional content type to check for watching state."
        ),
        key: str | None = Field(
            None, description="userkey of the user to check for watching state."
        ),
        username: str | None = Field(
            None, description="username of the user to check for watching state."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get information about space watcher"""
        api = get_api()
        response = api.confluence_server_is_watching_space(
            space_key=space_key,
            content_type=content_type,
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_add_space_watch", tags={"confluence-server-space"}
    )
    def confluence_server_add_space_watch(
        space_key: str = Field(..., description="Parameter spaceKey"),
        content_type: str | None = Field(
            None, description="the optional content type to delete the watcher for."
        ),
        key: str | None = Field(
            None, description="userKey of the user to create the new watcher for."
        ),
        username: str | None = Field(
            None, description="userName of the user to create the new watcher for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add space watcher"""
        api = get_api()
        response = api.confluence_server_add_space_watch(
            space_key=space_key,
            content_type=content_type,
            key=key,
            username=username,
        )
        return response.model_dump()

    @mcp.tool(
        name="confluence_server_remove_space_watch", tags={"confluence-server-space"}
    )
    def confluence_server_remove_space_watch(
        space_key: str = Field(..., description="Parameter spaceKey"),
        content_type: str | None = Field(
            None, description="the optional content type to delete the watcher for."
        ),
        key: str | None = Field(
            None, description="userkey of the user to delete the watcher for."
        ),
        username: str | None = Field(
            None, description="username of the user to delete the watcher for."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Remove space watcher"""
        api = get_api()
        response = api.confluence_server_remove_space_watch(
            space_key=space_key,
            content_type=content_type,
            key=key,
            username=username,
        )
        return response.model_dump()
