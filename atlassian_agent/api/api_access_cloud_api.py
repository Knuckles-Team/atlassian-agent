# Generated API Client for APIAccessCloud
from typing import Any

from ..models import Response
from .base import BaseAtlassianClient


class APIAccessCloudAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def api_access_cloud_get_all_api_tokens_by_org_id(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all API tokens in an org

        Path: /orgs/{org_id}/api-tokens
        Method: GET
        """
        path = f"/orgs/{org_id}/api-tokens"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def api_access_cloud_bulk_revoke_api_tokens(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Bulk revoke API tokens in an organization

        Path: /orgs/{org_id}/api-tokens
        Method: DELETE
        """
        path = f"/orgs/{org_id}/api-tokens"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def api_access_cloud_get_api_token_count_by_org_id(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get API token count in an org

        Path: /orgs/{org_id}/api-tokens/count
        Method: GET
        """
        path = f"/orgs/{org_id}/api-tokens/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def api_access_cloud_count_service_account_api_tokens(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get service account API token count in an org

        Path: /orgs/{org_id}/service-accounts/count
        Method: POST
        """
        path = f"/orgs/{org_id}/service-accounts/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def api_access_cloud_get_service_account_api_token(
        self,
        org_id: str,
        account_id: str,
        token_label: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all service account API tokens in an org

        Path: /orgs/{org_id}/service-accounts/{accountId}/api-tokens
        Method: GET
        """
        path = f"/orgs/{org_id}/service-accounts/{account_id}/api-tokens"
        params = {
            "tokenLabel": token_label,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def api_access_cloud_revoke_api_tokens(
        self,
        org_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Revoke all API tokens for a service account

        Path: /orgs/{org_id}/service-accounts/{accountId}/api-tokens
        Method: DELETE
        """
        path = f"/orgs/{org_id}/service-accounts/{account_id}/api-tokens"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def api_access_cloud_get_api_key_count_by_org_id(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get API key count in an org

        Path: /orgs/{org_id}/api-keys/count
        Method: GET
        """
        path = f"/orgs/{org_id}/api-keys/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def api_access_cloud_get_all_api_keys_by_org_id(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get all API keys in an org

        Path: /orgs/{org_id}/api-keys
        Method: GET
        """
        path = f"/orgs/{org_id}/api-keys"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def api_access_cloud_revoke_api_key(
        self,
        org_id: str,
        api_key_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Revoke an API key for an org

        Path: /orgs/{org_id}/api-keys/revoke/{apiKeyId}
        Method: PATCH
        """
        path = f"/orgs/{org_id}/api-keys/revoke/{api_key_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PATCH", path, params=params, json=payload if payload else None
        )
