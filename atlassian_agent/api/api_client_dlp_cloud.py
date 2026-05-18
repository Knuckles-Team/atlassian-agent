# Generated API Client for DLPCloud
from typing import Any

from ..models import Response
from .base import BaseAtlassianClient


class DLPCloudAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def dlp_cloud_create_level(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a new classification level

        Path: /orgs/{org_id}/classification-levels
        Method: POST
        """
        path = f"/orgs/{org_id}/classification-levels"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def dlp_cloud_get_level_list(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all classification levels by org_id

        Path: /orgs/{org_id}/classification-levels
        Method: GET
        """
        path = f"/orgs/{org_id}/classification-levels"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def dlp_cloud_get_level(
        self,
        level_id: str,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a classification level

        Path: /orgs/{org_id}/classification-levels/{levelId}
        Method: GET
        """
        path = f"/orgs/{org_id}/classification-levels/{level_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def dlp_cloud_edit_level(
        self,
        level_id: str,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Edit a classification level

        Path: /orgs/{org_id}/classification-levels/{levelId}
        Method: PUT
        """
        path = f"/orgs/{org_id}/classification-levels/{level_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def dlp_cloud_publish_level(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Publish classification level(s)

        Path: /orgs/{org_id}/classification-levels/publish
        Method: POST
        """
        path = f"/orgs/{org_id}/classification-levels/publish"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def dlp_cloud_archive_level(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Archive a data classification level

        Path: /orgs/{org_id}/classification-levels/archive
        Method: POST
        """
        path = f"/orgs/{org_id}/classification-levels/archive"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def dlp_cloud_restore_level(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Restore a classification level

        Path: /orgs/{org_id}/classification-levels/restore
        Method: POST
        """
        path = f"/orgs/{org_id}/classification-levels/restore"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def dlp_cloud_reorder(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Reorder classification levels

        Path: /orgs/{org_id}/classification-levels/reorder
        Method: POST
        """
        path = f"/orgs/{org_id}/classification-levels/reorder"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )
