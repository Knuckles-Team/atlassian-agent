# Generated API Client for UserMgmtCloud
from typing import Any, Dict, List, Optional
from .base import BaseAtlassianClient
from ..models import Response


class UserMgmtCloudAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def user_mgmt_cloud_get_users_account_id_manage(
        self,
        account_id: str,
        privileges: Optional[List[Any]] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get user management permissions

        Path: /users/{account_id}/manage
        Method: GET
        """
        path = f"/users/{account_id}/manage"
        params = {
            "privileges": privileges,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_get_users_account_id_manage_profile(
        self,
        account_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get profile

        Path: /users/{account_id}/manage/profile
        Method: GET
        """
        path = f"/users/{account_id}/manage/profile"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_patch_users_account_id_manage_profile(
        self,
        account_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Update profile

        Path: /users/{account_id}/manage/profile
        Method: PATCH
        """
        path = f"/users/{account_id}/manage/profile"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PATCH", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_put_users_account_id_manage_email(
        self,
        account_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Set email

        Path: /users/{account_id}/manage/email
        Method: PUT
        """
        path = f"/users/{account_id}/manage/email"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_get_users_account_id_manage_api_tokens(
        self,
        account_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get API tokens

        Path: /users/{account_id}/manage/api-tokens
        Method: GET
        """
        path = f"/users/{account_id}/manage/api-tokens"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id(
        self,
        account_id: str,
        token_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete API token

        Path: /users/{account_id}/manage/api-tokens/{tokenId}
        Method: DELETE
        """
        path = f"/users/{account_id}/manage/api-tokens/{token_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable(
        self,
        account_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Deactivate a user

        Path: /users/{account_id}/manage/lifecycle/disable
        Method: POST
        """
        path = f"/users/{account_id}/manage/lifecycle/disable"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable(
        self,
        account_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Activate a user

        Path: /users/{account_id}/manage/lifecycle/enable
        Method: POST
        """
        path = f"/users/{account_id}/manage/lifecycle/enable"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete(
        self,
        account_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete account

        Path: /users/{account_id}/manage/lifecycle/delete
        Method: POST
        """
        path = f"/users/{account_id}/manage/lifecycle/delete"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete(
        self,
        account_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Cancel delete account

        Path: /users/{account_id}/manage/lifecycle/cancel-delete
        Method: POST
        """
        path = f"/users/{account_id}/manage/lifecycle/cancel-delete"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )
