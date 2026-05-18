# Generated API Client for ConfluenceServer
from typing import Any

from ..models import Response
from .base import BaseAtlassianClient


class ConfluenceServerAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def confluence_server_get_access_mode_status(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get access mode status

        Path: /rest/api/accessmode
        Method: GET
        """
        path = "/rest/api/accessmode"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_create(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create group

        Path: /rest/api/admin/group
        Method: POST
        """
        path = "/rest/api/admin/group"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete(
        self,
        group_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete group

        Path: /rest/api/admin/group/{groupName}
        Method: DELETE
        """
        path = f"/rest/api/admin/group/{group_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_change_password(
        self,
        username: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Change password

        Path: /rest/api/admin/user/{username}/password
        Method: POST
        """
        path = f"/rest/api/admin/user/{username}/password"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_user(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create user

        Path: /rest/api/admin/user
        Method: POST
        """
        path = "/rest/api/admin/user"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_1(
        self,
        username: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete user

        Path: /rest/api/admin/user/{username}
        Method: DELETE
        """
        path = f"/rest/api/admin/user/{username}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_disable(
        self,
        username: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Disable user

        Path: /rest/api/admin/user/{username}/disable
        Method: PUT
        """
        path = f"/rest/api/admin/user/{username}/disable"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_enable(
        self,
        username: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Enable user

        Path: /rest/api/admin/user/{username}/enable
        Method: PUT
        """
        path = f"/rest/api/admin/user/{username}/enable"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_attachments(
        self,
        id_: str,
        expand: str | None = None,
        filename: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        media_type: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get attachment

        Path: /rest/api/content/{id}/child/attachment
        Method: GET
        """
        path = f"/rest/api/content/{id_}/child/attachment"
        params = {
            "expand": expand,
            "filename": filename,
            "limit": limit,
            "start": start,
            "mediaType": media_type,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_attachments(
        self,
        id_: str,
        expand: str | None = None,
        allow_duplicated: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create attachments

        Path: /rest/api/content/{id}/child/attachment
        Method: POST
        """
        path = f"/rest/api/content/{id_}/child/attachment"
        params = {
            "expand": expand,
            "allowDuplicated": allow_duplicated,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_attachment_extracted_text(
        self,
        attachment_id: str,
        id_: str,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """No description provided.

        Path: /rest/api/content/{id}/child/attachment/{attachmentId}/extractedtext
        Method: GET
        """
        path = f"/rest/api/content/{id_}/child/attachment/{attachment_id}/extractedtext"
        params = {
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_move(
        self,
        attachment_id: str,
        id_: str,
        new_name: str | None = None,
        new_content_id: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Move attachment

        Path: /rest/api/content/{id}/child/attachment/{attachmentId}/move
        Method: POST
        """
        path = f"/rest/api/content/{id_}/child/attachment/{attachment_id}/move"
        params = {
            "newName": new_name,
            "newContentId": new_content_id,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_update(
        self,
        attachment_id: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update non-binary data of an Attachment

        Path: /rest/api/content/{id}/child/attachment/{attachmentId}
        Method: PUT
        """
        path = f"/rest/api/content/{id_}/child/attachment/{attachment_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_remove_attachment(
        self,
        attachment_id: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove attachment

        Path: /rest/api/content/{id}/child/attachment/{attachmentId}
        Method: DELETE
        """
        path = f"/rest/api/content/{id_}/child/attachment/{attachment_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_remove_attachment_version(
        self,
        attachment_id: str,
        id_: str,
        version: int,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove attachment version

        Path: /rest/api/content/{id}/child/attachment/{attachmentId}/version/{version}
        Method: DELETE
        """
        path = f"/rest/api/content/{id_}/child/attachment/{attachment_id}/version/{version}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_data(
        self,
        attachment_id: str,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update binary data of an attachment

        Path: /rest/api/content/{id}/child/attachment/{attachmentId}/data
        Method: POST
        """
        path = f"/rest/api/content/{id_}/child/attachment/{attachment_id}/data"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_audit_records(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """No description provided.

        Path: /rest/api/audit
        Method: GET
        """
        path = "/rest/api/audit"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_cancel_all_queued_jobs(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Cancel all queued jobs

        Path: /rest/api/backup-restore/jobs/clear-queue
        Method: PUT
        """
        path = "/rest/api/backup-restore/jobs/clear-queue"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_cancel_job(
        self,
        job_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Cancel job

        Path: /rest/api/backup-restore/jobs/{jobId}/cancel
        Method: PUT
        """
        path = f"/rest/api/backup-restore/jobs/{job_id}/cancel"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_site_backup_job(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create site backup job

        Path: /rest/api/backup-restore/backup/site
        Method: POST
        """
        path = "/rest/api/backup-restore/backup/site"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_site_restore_job(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create site restore job

        Path: /rest/api/backup-restore/restore/site
        Method: POST
        """
        path = "/rest/api/backup-restore/restore/site"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_site_restore_job_for_uploaded_backup_file(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create site restore job for upload backup file

        Path: /rest/api/backup-restore/restore/site/upload
        Method: POST
        """
        path = "/rest/api/backup-restore/restore/site/upload"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_space_backup_job(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create space backup job

        Path: /rest/api/backup-restore/backup/space
        Method: POST
        """
        path = "/rest/api/backup-restore/backup/space"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_space_restore_job(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create space restore job

        Path: /rest/api/backup-restore/restore/space
        Method: POST
        """
        path = "/rest/api/backup-restore/restore/space"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_space_restore_job_for_uploaded_backup_file(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create space restore job for upload backup file

        Path: /rest/api/backup-restore/restore/space/upload
        Method: POST
        """
        path = "/rest/api/backup-restore/restore/space/upload"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_download_backup_file(
        self,
        job_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Download backup file

        Path: /rest/api/backup-restore/jobs/{jobId}/download
        Method: GET
        """
        path = f"/rest/api/backup-restore/jobs/{job_id}/download"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_find_jobs(
        self,
        owner: str | None = None,
        space_key: str | None = None,
        from_date: str | None = None,
        job_states: str | None = None,
        to_date: str | None = None,
        job_operation: str | None = None,
        limit: str | None = None,
        job_scope: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find jobs by filters

        Path: /rest/api/backup-restore/jobs
        Method: GET
        """
        path = "/rest/api/backup-restore/jobs"
        params = {
            "owner": owner,
            "spaceKey": space_key,
            "fromDate": from_date,
            "jobStates": job_states,
            "toDate": to_date,
            "jobOperation": job_operation,
            "limit": limit,
            "jobScope": job_scope,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_files(
        self,
        job_scope: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get files in restore directory

        Path: /rest/api/backup-restore/restore/files
        Method: GET
        """
        path = "/rest/api/backup-restore/restore/files"
        params = {
            "jobScope": job_scope,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_job(
        self,
        job_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get job by ID

        Path: /rest/api/backup-restore/jobs/{jobId}
        Method: GET
        """
        path = f"/rest/api/backup-restore/jobs/{job_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_remove_category(
        self,
        space_key: str,
        category_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove a category from a space

        Path: /rest/api/space/{spaceKey}/category/{categoryName}
        Method: DELETE
        """
        path = f"/rest/api/space/{space_key}/category/{category_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_children(
        self,
        id_: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        parent_version: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get children of content

        Path: /rest/api/content/{id}/child
        Method: GET
        """
        path = f"/rest/api/content/{id_}/child"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
            "parentVersion": parent_version,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_children_of_type(
        self,
        id_: str,
        type_: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        parent_version: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get children of content by type

        Path: /rest/api/content/{id}/child/{type}
        Method: GET
        """
        path = f"/rest/api/content/{id_}/child/{type_}"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
            "parentVersion": parent_version,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_comments_of_content(
        self,
        id_: str,
        expand: str | None = None,
        depth: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        location: str | None = None,
        parent_version: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get comments of content

        Path: /rest/api/content/{id}/child/comment
        Method: GET
        """
        path = f"/rest/api/content/{id_}/child/comment"
        params = {
            "expand": expand,
            "depth": depth,
            "limit": limit,
            "start": start,
            "location": location,
            "parentVersion": parent_version,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_publish_shared_draft(
        self,
        draft_id: str,
        expand: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Publish shared draft

        Path: /rest/api/content/blueprint/instance/{draftId}
        Method: PUT
        """
        path = f"/rest/api/content/blueprint/instance/{draft_id}"
        params = {
            "expand": expand,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_publish_legacy_draft(
        self,
        draft_id: str,
        expand: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Publish legacy draft

        Path: /rest/api/content/blueprint/instance/{draftId}
        Method: POST
        """
        path = f"/rest/api/content/blueprint/instance/{draft_id}"
        params = {
            "expand": expand,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_convert(
        self,
        to: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Convert body representation

        Path: /rest/api/contentbody/convert/{to}
        Method: POST
        """
        path = f"/rest/api/contentbody/convert/{to}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_labels(
        self,
        id_: str,
        prefix: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get labels

        Path: /rest/api/content/{id}/label
        Method: GET
        """
        path = f"/rest/api/content/{id_}/label"
        params = {
            "prefix": prefix,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_add_labels(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add Labels

        Path: /rest/api/content/{id}/label
        Method: POST
        """
        path = f"/rest/api/content/{id_}/label"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_label_with_query_param(
        self,
        id_: str,
        name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete label with query param

        Path: /rest/api/content/{id}/label
        Method: DELETE
        """
        path = f"/rest/api/content/{id_}/label"
        params = {
            "name": name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_label(
        self,
        id_: str,
        label: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete label

        Path: /rest/api/content/{id}/label/{label}
        Method: DELETE
        """
        path = f"/rest/api/content/{id_}/label/{label}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_find_all(
        self,
        id_: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find all content properties

        Path: /rest/api/content/{id}/property
        Method: GET
        """
        path = f"/rest/api/content/{id_}/property"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_1(
        self,
        id_: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a content property

        Path: /rest/api/content/{id}/property
        Method: POST
        """
        path = f"/rest/api/content/{id_}/property"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_find_by_key(
        self,
        id_: str,
        key: str,
        expand: str | None = None,
        limit: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find content property by key

        Path: /rest/api/content/{id}/property/{key}
        Method: GET
        """
        path = f"/rest/api/content/{id_}/property/{key}"
        params = {
            "expand": expand,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_1(
        self,
        id_: str,
        key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content property

        Path: /rest/api/content/{id}/property/{key}
        Method: PUT
        """
        path = f"/rest/api/content/{id_}/property/{key}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_2(
        self,
        id_: str,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """No description provided.

        Path: /rest/api/content/{id}/property/{key}
        Method: POST
        """
        path = f"/rest/api/content/{id_}/property/{key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_2(
        self,
        id_: str,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content property

        Path: /rest/api/content/{id}/property/{key}
        Method: DELETE
        """
        path = f"/rest/api/content/{id_}/property/{key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_content(
        self,
        space_key: str | None = None,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        posting_day: str | None = None,
        ids: str | None = None,
        title: str | None = None,
        type_: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content

        Path: /rest/api/content
        Method: GET
        """
        path = "/rest/api/content"
        params = {
            "spaceKey": space_key,
            "expand": expand,
            "limit": limit,
            "start": start,
            "postingDay": posting_day,
            "ids": ids,
            "title": title,
            "type": type_,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_content(
        self,
        expand: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create content

        Path: /rest/api/content
        Method: POST
        """
        path = "/rest/api/content"
        params = {
            "expand": expand,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_content_by_id(
        self,
        id_: str,
        expand: str | None = None,
        version: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get content by ID

        Path: /rest/api/content/{id}
        Method: GET
        """
        path = f"/rest/api/content/{id_}"
        params = {
            "expand": expand,
            "version": version,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_3(
        self,
        id_: str,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content

        Path: /rest/api/content/{id}
        Method: DELETE
        """
        path = f"/rest/api/content/{id_}"
        params = {
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_history(
        self,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get history of content

        Path: /rest/api/content/{id}/history
        Method: GET
        """
        path = f"/rest/api/content/{id_}/history"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_macro_body_by_hash(
        self,
        id_: str,
        version: str,
        hash: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get macro body by hash

        Path: /rest/api/content/{id}/history/{version}/macro/hash/{hash}
        Method: GET
        """
        path = f"/rest/api/content/{id_}/history/{version}/macro/hash/{hash}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_macro_body_by_macro_id(
        self,
        macro_id: str,
        id_: str,
        version: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get macro body by macro ID

        Path: /rest/api/content/{id}/history/{version}/macro/id/{macroId}
        Method: GET
        """
        path = f"/rest/api/content/{id_}/history/{version}/macro/id/{macro_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_scan_content(
        self,
        cursor: str | None = None,
        space_key: str | None = None,
        expand: str | None = None,
        limit: str | None = None,
        type_: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Scan content by space key

        Path: /rest/api/content/scan
        Method: GET
        """
        path = "/rest/api/content/scan"
        params = {
            "cursor": cursor,
            "spaceKey": space_key,
            "expand": expand,
            "limit": limit,
            "type": type_,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_search(
        self,
        cqlcontext: str | None = None,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        cql: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search content using CQL

        Path: /rest/api/content/search
        Method: GET
        """
        path = "/rest/api/content/search"
        params = {
            "cqlcontext": cqlcontext,
            "expand": expand,
            "limit": limit,
            "start": start,
            "cql": cql,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_2(
        self,
        content_id: str,
        async_reconciliation: bool | None = None,
        conflict_policy: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update content

        Path: /rest/api/content/{contentId}
        Method: PUT
        """
        path = f"/rest/api/content/{content_id}"
        params = {
            "asyncReconciliation": async_reconciliation,
            "conflictPolicy": conflict_policy,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_by_operation(
        self,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all restrictions by Operation

        Path: /rest/api/content/{id}/restriction/byOperation
        Method: GET
        """
        path = f"/rest/api/content/{id_}/restriction/byOperation"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_for_operation(
        self,
        operation_key: str,
        id_: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all restrictions for given operation

        Path: /rest/api/content/{id}/restriction/byOperation/{operationKey}
        Method: GET
        """
        path = f"/rest/api/content/{id_}/restriction/byOperation/{operation_key}"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_relevant_view_restrictions(
        self,
        id_: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all view restriction both direct and inherited.

        Path: /rest/api/content/{id}/restriction/relevantViewRestrictions
        Method: GET
        """
        path = f"/rest/api/content/{id_}/restriction/relevantViewRestrictions"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_restrictions(
        self,
        id_: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update restrictions

        Path: /rest/api/content/{id}/restriction
        Method: PUT
        """
        path = f"/rest/api/content/{id_}/restriction"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_content_history(
        self,
        id_: str,
        version_number: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete content history

        Path: /rest/api/content/{id}/version/{versionNumber}
        Method: DELETE
        """
        path = f"/rest/api/content/{id_}/version/{version_number}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_index(
        self,
        content_id: str,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Fetch users watching a given content

        Path: /rest/api/content/{contentId}/watchers
        Method: GET
        """
        path = f"/rest/api/content/{content_id}/watchers"
        params = {
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_descendants(
        self,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get Descendants

        Path: /rest/api/content/{id}/descendant
        Method: GET
        """
        path = f"/rest/api/content/{id_}/descendant"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_descendants_of_type(
        self,
        id_: str,
        type_: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get descendants of type

        Path: /rest/api/content/{id}/descendant/{type}
        Method: GET
        """
        path = f"/rest/api/content/{id_}/descendant/{type_}"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_default_color_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get default global color scheme

        Path: /rest/api/color-scheme/default
        Method: GET
        """
        path = "/rest/api/color-scheme/default"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_global_color_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get global color scheme

        Path: /rest/api/color-scheme
        Method: GET
        """
        path = "/rest/api/color-scheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_color_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Set global color scheme

        Path: /rest/api/color-scheme
        Method: PUT
        """
        path = "/rest/api/color-scheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_reset_global_color_scheme(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Reset global color scheme

        Path: /rest/api/color-scheme/reset
        Method: PUT
        """
        path = "/rest/api/color-scheme/reset"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_all_global_permissions(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get global permissions

        Path: /rest/api/permissions
        Method: GET
        """
        path = "/rest/api/permissions"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_permissions_granted_to_anonymous_users(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Gets the permissions granted to an anonymous user

        Path: /rest/api/permissions/anonymous
        Method: GET
        """
        path = "/rest/api/permissions/anonymous"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_permissions_granted_to_group(
        self,
        group_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Gets global permissions granted to a group

        Path: /rest/api/permissions/group/{groupName}
        Method: GET
        """
        path = f"/rest/api/permissions/group/{group_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_permissions_granted_to_unlicensed_users(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Gets the permissions granted to an unlicensed users

        Path: /rest/api/permissions/unlicensed
        Method: GET
        """
        path = "/rest/api/permissions/unlicensed"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_permissions_granted_to_user(
        self,
        user_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Gets global permissions granted to a user

        Path: /rest/api/permissions/user/{userKey}
        Method: GET
        """
        path = f"/rest/api/permissions/user/{user_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_find_webhooks(
        self,
        limit: str | None = None,
        start: str | None = None,
        event: str | None = None,
        statistics: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Find webhooks

        Path: /rest/api/webhooks
        Method: GET
        """
        path = "/rest/api/webhooks"
        params = {
            "limit": limit,
            "start": start,
            "event": event,
            "statistics": statistics,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_webhook(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create webhook

        Path: /rest/api/webhooks
        Method: POST
        """
        path = "/rest/api/webhooks"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_webhook(
        self,
        webhook_id: str,
        statistics: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get webhook

        Path: /rest/api/webhooks/{webhookId}
        Method: GET
        """
        path = f"/rest/api/webhooks/{webhook_id}"
        params = {
            "statistics": statistics,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_webhook(
        self,
        webhook_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update webhook

        Path: /rest/api/webhooks/{webhookId}
        Method: PUT
        """
        path = f"/rest/api/webhooks/{webhook_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_webhook(
        self,
        webhook_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete webhook

        Path: /rest/api/webhooks/{webhookId}
        Method: DELETE
        """
        path = f"/rest/api/webhooks/{webhook_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_latest_invocation(
        self,
        webhook_id: str,
        outcomes: str | None = None,
        event: str | None = None,
        outcome: list[Any] | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get latest invocations

        Path: /rest/api/webhooks/{webhookId}/latest
        Method: GET
        """
        path = f"/rest/api/webhooks/{webhook_id}/latest"
        params = {
            "outcomes": outcomes,
            "event": event,
            "outcome": outcome,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_statistics(
        self,
        webhook_id: str,
        event: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get statistic

        Path: /rest/api/webhooks/{webhookId}/statistics
        Method: GET
        """
        path = f"/rest/api/webhooks/{webhook_id}/statistics"
        params = {
            "event": event,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_statistics_summary(
        self,
        webhook_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get statistics summary

        Path: /rest/api/webhooks/{webhookId}/statistics/summary
        Method: GET
        """
        path = f"/rest/api/webhooks/{webhook_id}/statistics/summary"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_test_webhook(
        self,
        url: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Test webhook

        Path: /rest/api/webhooks/test
        Method: POST
        """
        path = "/rest/api/webhooks/test"
        params = {
            "url": url,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_ancestor_groups(
        self,
        group_name: str,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group ancestor of a group

        Path: /rest/api/group/{groupName}/groupancestor
        Method: GET
        """
        path = f"/rest/api/group/{group_name}/groupancestor"
        params = {
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_ancestor_groups_by_group_name(
        self,
        group_name: str | None = None,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group ancestor of a group

        Path: /rest/api/group/groupancestor
        Method: GET
        """
        path = "/rest/api/group/groupancestor"
        params = {
            "groupName": group_name,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_group(
        self,
        group_name: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group by name

        Path: /rest/api/group/{groupName}
        Method: GET
        """
        path = f"/rest/api/group/{group_name}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_group_by_group_name(
        self,
        expand: str | None = None,
        group_name: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group by name

        Path: /rest/api/group/info
        Method: GET
        """
        path = "/rest/api/group/info"
        params = {
            "expand": expand,
            "groupName": group_name,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_groups(
        self,
        expand: str | None = None,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get groups

        Path: /rest/api/group
        Method: GET
        """
        path = "/rest/api/group"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_members(
        self,
        group_name: str,
        expand: str | None = None,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get members of group

        Path: /rest/api/group/{groupName}/member
        Method: GET
        """
        path = f"/rest/api/group/{group_name}/member"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_members_by_group_name(
        self,
        expand: str | None = None,
        group_name: str | None = None,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get members of group

        Path: /rest/api/group/member
        Method: GET
        """
        path = "/rest/api/group/member"
        params = {
            "expand": expand,
            "groupName": group_name,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_nested_group_members(
        self,
        group_name: str,
        expand: str | None = None,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group members of group

        Path: /rest/api/group/{groupName}/groupmember
        Method: GET
        """
        path = f"/rest/api/group/{group_name}/groupmember"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_nested_group_members_by_group_name(
        self,
        expand: str | None = None,
        group_name: str | None = None,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group members of group

        Path: /rest/api/group/groupmember
        Method: GET
        """
        path = "/rest/api/group/groupmember"
        params = {
            "expand": expand,
            "groupName": group_name,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_parent_groups(
        self,
        group_name: str,
        expand: str | None = None,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group parents of a group

        Path: /rest/api/group/{groupName}/groupparent
        Method: GET
        """
        path = f"/rest/api/group/{group_name}/groupparent"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_parent_groups_by_group_name(
        self,
        expand: str | None = None,
        group_name: str | None = None,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group parents of a group

        Path: /rest/api/group/groupparent
        Method: GET
        """
        path = "/rest/api/group/groupparent"
        params = {
            "expand": expand,
            "groupName": group_name,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_index_1(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get instance metrics

        Path: /rest/api/instance-metrics
        Method: GET
        """
        path = "/rest/api/instance-metrics"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_related_labels(
        self,
        label_name: str,
        start: str | None = None,
        limit: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get related labels, currently returning global labels only.

        Path: /rest/api/label/{labelName}/related
        Method: GET
        """
        path = f"/rest/api/label/{label_name}/related"
        params = {
            "start": start,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_recent(
        self,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get recently used labels

        Path: /rest/api/label/recent
        Method: GET
        """
        path = "/rest/api/label/recent"
        params = {
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_task(
        self,
        id_: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get task by ID

        Path: /rest/api/longtask/{id}
        Method: GET
        """
        path = f"/rest/api/longtask/{id_}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_tasks(
        self,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get tasks

        Path: /rest/api/longtask
        Method: GET
        """
        path = "/rest/api/longtask"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_search_1(
        self,
        cqlcontext: str | None = None,
        expand: str | None = None,
        include_archived_spaces: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        excerpt: str | None = None,
        cql: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search for entities in confluence

        Path: /rest/api/search
        Method: GET
        """
        path = "/rest/api/search"
        params = {
            "cqlcontext": cqlcontext,
            "expand": expand,
            "includeArchivedSpaces": include_archived_spaces,
            "limit": limit,
            "start": start,
            "excerpt": excerpt,
            "cql": cql,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_index_2(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Get server information

        Path: /rest/api/server-information
        Method: GET
        """
        path = "/rest/api/server-information"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_color_scheme_type(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get Space color scheme type

        Path: /rest/api/space/{spaceKey}/color-scheme/type
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/color-scheme/type"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_color_scheme_type(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update Space color scheme type

        Path: /rest/api/space/{spaceKey}/color-scheme/type
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/color-scheme/type"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_space_color_scheme(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get Space color scheme

        Path: /rest/api/space/{spaceKey}/color-scheme
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/color-scheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_space_color_scheme(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update Space color scheme

        Path: /rest/api/space/{spaceKey}/color-scheme
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/color-scheme"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_reset_space_color_scheme(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reset Space color scheme

        Path: /rest/api/space/{spaceKey}/color-scheme/reset
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/color-scheme/reset"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_index_3(
        self,
        space_key: str,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Fetch all labels

        Path: /rest/api/space/{spaceKey}/labels
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/labels"
        params = {
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_popular(
        self,
        space_key: str,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get popular labels

        Path: /rest/api/space/{spaceKey}/labels/popular
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/labels/popular"
        params = {
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_recent_1(
        self,
        space_key: str,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get recent labels

        Path: /rest/api/space/{spaceKey}/labels/recent
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/labels/recent"
        params = {
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_related(
        self,
        space_key: str,
        label_name: str,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get related labels

        Path: /rest/api/space/{spaceKey}/labels/{labelName}/related
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/labels/{label_name}/related"
        params = {
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_all_space_permissions(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all space permissions

        Path: /rest/api/space/{spaceKey}/permissions
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/permissions"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_set_permissions(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Set permissions to multiple users/groups/anonymous user in the given space

        Path: /rest/api/space/{spaceKey}/permissions
        Method: POST
        """
        path = f"/rest/api/space/{space_key}/permissions"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_permissions_granted_to_anonymous_users_1(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Gets the permissions granted to an anonymous user in a space

        Path: /rest/api/space/{spaceKey}/permissions/anonymous
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/permissions/anonymous"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_permissions_granted_to_group_1(
        self,
        space_key: str,
        group_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Gets the permissions granted to a group in a space

        Path: /rest/api/space/{spaceKey}/permissions/group/{groupName}
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/permissions/group/{group_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_permissions_granted_to_user_1(
        self,
        space_key: str,
        user_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Gets the permissions granted to a user in a space

        Path: /rest/api/space/{spaceKey}/permissions/user/{userKey}
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/permissions/user/{user_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_grant_permissions_to_anonymous_users(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Grants space permissions to anonymous user

        Path: /rest/api/space/{spaceKey}/permissions/anonymous/grant
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/permissions/anonymous/grant"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_grant_permissions_to_group(
        self,
        space_key: str,
        group_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Grants space permissions to a group

        Path: /rest/api/space/{spaceKey}/permissions/group/{groupName}/grant
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/permissions/group/{group_name}/grant"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_grant_permissions_to_user(
        self,
        space_key: str,
        user_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Grants space permissions to a user

        Path: /rest/api/space/{spaceKey}/permissions/user/{userKey}/grant
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/permissions/user/{user_key}/grant"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_revoke_permissions_from_anonymous_user(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Revoke space permissions from anonymous user

        Path: /rest/api/space/{spaceKey}/permissions/anonymous/revoke
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/permissions/anonymous/revoke"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_revoke_permissions_from_group(
        self,
        space_key: str,
        group_name: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Revoke space permissions from a group

        Path: /rest/api/space/{spaceKey}/permissions/group/{groupName}/revoke
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/permissions/group/{group_name}/revoke"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_revoke_permissions_from_user(
        self,
        space_key: str,
        user_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Revoke space permissions from a user

        Path: /rest/api/space/{spaceKey}/permissions/user/{userKey}/revoke
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/permissions/user/{user_key}/revoke"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_1(
        self,
        space_key: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space properties

        Path: /rest/api/space/{spaceKey}/property
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/property"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_3(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a space property

        Path: /rest/api/space/{spaceKey}/property
        Method: POST
        """
        path = f"/rest/api/space/{space_key}/property"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_get(
        self,
        space_key: str,
        key: str,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space property by key

        Path: /rest/api/space/{spaceKey}/property/{key}
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/property/{key}"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_3(
        self,
        space_key: str,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update space property

        Path: /rest/api/space/{spaceKey}/property/{key}
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/property/{key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_4(
        self,
        space_key: str,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a space property with a specific key

        Path: /rest/api/space/{spaceKey}/property/{key}
        Method: POST
        """
        path = f"/rest/api/space/{space_key}/property/{key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_4(
        self,
        space_key: str,
        key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete space property

        Path: /rest/api/space/{spaceKey}/property/{key}
        Method: DELETE
        """
        path = f"/rest/api/space/{space_key}/property/{key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_archive(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Archive space

        Path: /rest/api/space/{spaceKey}/archive
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/archive"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_contents(
        self,
        space_key: str,
        expand: str | None = None,
        depth: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get contents in space

        Path: /rest/api/space/{spaceKey}/content
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/content"
        params = {
            "expand": expand,
            "depth": depth,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_contents_with_type(
        self,
        space_key: str,
        type_: str,
        expand: str | None = None,
        depth: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get contents by type

        Path: /rest/api/space/{spaceKey}/content/{type}
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/content/{type_}"
        params = {
            "expand": expand,
            "depth": depth,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_private_space(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Create private space

        Path: /rest/api/space/_private
        Method: POST
        """
        path = "/rest/api/space/_private"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_spaces(
        self,
        space_key_single: str | None = None,
        start: str | None = None,
        label: str | None = None,
        favourite: str | None = None,
        type_: str | None = None,
        space_key: str | None = None,
        space_id: list[Any] | None = None,
        expand: str | None = None,
        has_retention_policy: str | None = None,
        limit: str | None = None,
        space_keys: str | None = None,
        content_label: str | None = None,
        space_ids: str | None = None,
        status: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get spaces by key

        Path: /rest/api/space
        Method: GET
        """
        path = "/rest/api/space"
        params = {
            "spaceKeySingle": space_key_single,
            "start": start,
            "label": label,
            "favourite": favourite,
            "type": type_,
            "spaceKey": space_key,
            "spaceId": space_id,
            "expand": expand,
            "hasRetentionPolicy": has_retention_policy,
            "limit": limit,
            "spaceKeys": space_keys,
            "contentLabel": content_label,
            "spaceIds": space_ids,
            "status": status,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_create_space(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Creates a new Space.

        Path: /rest/api/space
        Method: POST
        """
        path = "/rest/api/space"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_space(
        self,
        space_key: str,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get space

        Path: /rest/api/space/{spaceKey}
        Method: GET
        """
        path = f"/rest/api/space/{space_key}"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_4(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update Space

        Path: /rest/api/space/{spaceKey}
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_5(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete Space

        Path: /rest/api/space/{spaceKey}
        Method: DELETE
        """
        path = f"/rest/api/space/{space_key}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_restore(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Restore space

        Path: /rest/api/space/{spaceKey}/restore
        Method: PUT
        """
        path = f"/rest/api/space/{space_key}/restore"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_trash(
        self,
        space_key: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove all trash contents

        Path: /rest/api/space/{spaceKey}/trash
        Method: DELETE
        """
        path = f"/rest/api/space/{space_key}/trash"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_index_4(
        self,
        space_key: str,
        limit: int | None = None,
        start: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Fetch users watching space

        Path: /rest/api/space/{spaceKey}/watchers
        Method: GET
        """
        path = f"/rest/api/space/{space_key}/watchers"
        params = {
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_update_5(
        self,
        group_name: str,
        username: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update user group

        Path: /rest/api/user/{username}/group/{groupName}
        Method: PUT
        """
        path = f"/rest/api/user/{username}/group/{group_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def confluence_server_delete_6(
        self,
        group_name: str,
        username: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete user group

        Path: /rest/api/user/{username}/group/{groupName}
        Method: DELETE
        """
        path = f"/rest/api/user/{username}/group/{group_name}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_change_password_1(
        self, payload: dict[str, Any] | None = None, _max_pages: int | None = None
    ) -> Response:
        """Change password

        Path: /rest/api/user/current/password
        Method: POST
        """
        path = "/rest/api/user/current/password"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_anonymous(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get information about anonymous user type

        Path: /rest/api/user/anonymous
        Method: GET
        """
        path = "/rest/api/user/anonymous"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_current(
        self,
        expand: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get current user

        Path: /rest/api/user/current
        Method: GET
        """
        path = "/rest/api/user/current"
        params = {
            "expand": expand,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_groups_1(
        self,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get groups

        Path: /rest/api/user/memberof
        Method: GET
        """
        path = "/rest/api/user/memberof"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_user(
        self,
        expand: str | None = None,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user

        Path: /rest/api/user
        Method: GET
        """
        path = "/rest/api/user"
        params = {
            "expand": expand,
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_get_users(
        self,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get registered users

        Path: /rest/api/user/list
        Method: GET
        """
        path = "/rest/api/user/list"
        params = {
            "expand": expand,
            "limit": limit,
            "start": start,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_is_watching_content(
        self,
        content_id: str,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get information about content watcher

        Path: /rest/api/user/watch/content/{contentId}
        Method: GET
        """
        path = f"/rest/api/user/watch/content/{content_id}"
        params = {
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_add_content_watcher(
        self,
        content_id: str,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add content watcher

        Path: /rest/api/user/watch/content/{contentId}
        Method: POST
        """
        path = f"/rest/api/user/watch/content/{content_id}"
        params = {
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_remove_content_watcher(
        self,
        content_id: str,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove content watcher

        Path: /rest/api/user/watch/content/{contentId}
        Method: DELETE
        """
        path = f"/rest/api/user/watch/content/{content_id}"
        params = {
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def confluence_server_is_watching_space(
        self,
        space_key: str,
        content_type: str | None = None,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get information about space watcher

        Path: /rest/api/user/watch/space/{spaceKey}
        Method: GET
        """
        path = f"/rest/api/user/watch/space/{space_key}"
        params = {
            "contentType": content_type,
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def confluence_server_add_space_watch(
        self,
        space_key: str,
        content_type: str | None = None,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add space watcher

        Path: /rest/api/user/watch/space/{spaceKey}
        Method: POST
        """
        path = f"/rest/api/user/watch/space/{space_key}"
        params = {
            "contentType": content_type,
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def confluence_server_remove_space_watch(
        self,
        space_key: str,
        content_type: str | None = None,
        key: str | None = None,
        username: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove space watcher

        Path: /rest/api/user/watch/space/{spaceKey}
        Method: DELETE
        """
        path = f"/rest/api/user/watch/space/{space_key}"
        params = {
            "contentType": content_type,
            "key": key,
            "username": username,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )
