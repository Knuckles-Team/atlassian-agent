# Generated API Client for ControlCloud
from typing import Any, Dict, Optional
from .base import BaseAtlassianClient
from ..models import Response


class ControlCloudAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def control_cloud_ap_is_get_policies(
        self,
        org_id: str,
        cursor: Optional[str] = None,
        type_: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get list of policies

        Path: /admin/control/v1/orgs/{org_id}/policies
        Method: GET
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies"
        params = {
            "cursor": cursor,
            "type": type_,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_create_policy(
        self,
        org_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Create a new policy

        Path: /admin/control/v1/orgs/{org_id}/policies
        Method: POST
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_get_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get single policy

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}
        Method: GET
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_update_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Update single policy

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}
        Method: PUT
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_delete_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete single policy

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}
        Method: DELETE
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_get_policies_v2(
        self,
        org_id: str,
        cursor: Optional[str] = None,
        type_: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get list of policies V2

        Path: /admin/control/v2/orgs/{org_id}/policies
        Method: GET
        """
        path = f"/admin/control/v2/orgs/{org_id}/policies"
        params = {
            "cursor": cursor,
            "type": type_,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_create_policy_v2(
        self,
        org_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Create a new policy V2

        Path: /admin/control/v2/orgs/{org_id}/policies
        Method: POST
        """
        path = f"/admin/control/v2/orgs/{org_id}/policies"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_get_policy_v2(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get single policy V2

        Path: /admin/control/v2/orgs/{org_id}/policies/{policyId}
        Method: GET
        """
        path = f"/admin/control/v2/orgs/{org_id}/policies/{policy_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_update_policy_v2(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Update single policy V2

        Path: /admin/control/v2/orgs/{org_id}/policies/{policyId}
        Method: PUT
        """
        path = f"/admin/control/v2/orgs/{org_id}/policies/{policy_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_publish_draft_policies(
        self,
        org_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Publish data security policies

        Path: /admin/control/v2/orgs/{org_id}/policies/publishDraftPolicies
        Method: POST
        """
        path = f"/admin/control/v2/orgs/{org_id}/policies/publishDraftPolicies"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_get_resources(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get list of resources associated with a policy

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}/resources
        Method: GET
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}/resources"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_create_resource(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Create a new policy resource

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}/resources
        Method: POST
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}/resources"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_delete_resources(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete all policy resources

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}/resources
        Method: DELETE
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}/resources"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_update_resource(
        self,
        org_id: str,
        policy_id: str,
        resource_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Update single policy resource

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}/resources/{resourceId}
        Method: PUT
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}/resources/{resource_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_delete_resource(
        self,
        org_id: str,
        policy_id: str,
        resource_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete single policy resource

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}/resources/{resourceId}
        Method: DELETE
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}/resources/{resource_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_get_resources_v2(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get list of resources associated with a policy V2

        Path: /admin/control/v2/orgs/{org_id}/policies/{policyId}/resources
        Method: GET
        """
        path = f"/admin/control/v2/orgs/{org_id}/policies/{policy_id}/resources"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_attach_detach_resources_v2(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Add or remove policy resources V2

        Path: /admin/control/v2/orgs/{org_id}/policies/{policyId}/resources
        Method: POST
        """
        path = f"/admin/control/v2/orgs/{org_id}/policies/{policy_id}/resources"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_delete_resources_v2(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete all policy resources V2

        Path: /admin/control/v2/orgs/{org_id}/policies/{policyId}/resources
        Method: DELETE
        """
        path = f"/admin/control/v2/orgs/{org_id}/policies/{policy_id}/resources"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_validate_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Validate a policy

        Path: /admin/control/v1/orgs/{org_id}/policies/{policyId}/validate
        Method: GET
        """
        path = f"/admin/control/v1/orgs/{org_id}/policies/{policy_id}/validate"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_add_users_to_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Add users to a policy

        Path: /admin/control/v1/orgs/{org_id}/auth-policy/{policyId}/add-users
        Method: POST
        """
        path = f"/admin/control/v1/orgs/{org_id}/auth-policy/{policy_id}/add-users"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_get_task_status(
        self,
        org_id: str,
        task_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get the status of a task

        Path: /admin/control/v1/orgs/{org_id}/auth-policy/task/{taskId}
        Method: GET
        """
        path = f"/admin/control/v1/orgs/{org_id}/auth-policy/task/{task_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def control_cloud_ap_is_bulk_fetch_auth_policy(
        self,
        org_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get policy information for managed users

        Path: /admin/control/v1/orgs/{org_id}/users/auth-policies/bulk-fetch
        Method: POST
        """
        path = f"/admin/control/v1/orgs/{org_id}/users/auth-policies/bulk-fetch"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )
