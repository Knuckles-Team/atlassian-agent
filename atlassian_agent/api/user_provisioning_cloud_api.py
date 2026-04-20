# Generated API Client for UserProvisioningCloud
from typing import Any, Dict, Optional
from .base import BaseAtlassianClient
from ..models import Response


class UserProvisioningCloudAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def user_provisioning_cloud_get(
        self,
        directory_id: str,
        id_: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get a group by ID

        Path: /scim/directory/{directoryId}/Groups/{id}
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/Groups/{id_}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_put(
        self,
        directory_id: str,
        id_: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Update a group by ID

        Path: /scim/directory/{directoryId}/Groups/{id}
        Method: PUT
        """
        path = f"/scim/directory/{directory_id}/Groups/{id_}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_delete_a_group(
        self,
        directory_id: str,
        id_: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete a group by ID

        Path: /scim/directory/{directoryId}/Groups/{id}
        Method: DELETE
        """
        path = f"/scim/directory/{directory_id}/Groups/{id_}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_patch(
        self,
        directory_id: str,
        id_: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Update a group by ID (PATCH)

        Path: /scim/directory/{directoryId}/Groups/{id}
        Method: PATCH
        """
        path = f"/scim/directory/{directory_id}/Groups/{id_}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PATCH", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_all_groups_from_an_active_directory(
        self,
        directory_id: str,
        filter: Optional[str] = None,
        start_index: Optional[int] = None,
        count: Optional[int] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get groups

        Path: /scim/directory/{directoryId}/Groups
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/Groups"
        params = {
            "filter": filter,
            "startIndex": start_index,
            "count": count,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_create_a_group_in_active_directory(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Create a group

        Path: /scim/directory/{directoryId}/Groups
        Method: POST
        """
        path = f"/scim/directory/{directory_id}/Groups"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_schemas(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get all schemas

        Path: /scim/directory/{directoryId}/Schemas
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/Schemas"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_resource_types(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get resource types

        Path: /scim/directory/{directoryId}/ResourceTypes
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/ResourceTypes"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_user_resource_type(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get user resource types

        Path: /scim/directory/{directoryId}/ResourceTypes/User
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/ResourceTypes/User"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_group_resource_type(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get group resource types

        Path: /scim/directory/{directoryId}/ResourceTypes/Group
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/ResourceTypes/Group"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_user_schemas(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get user schemas

        Path: /scim/directory/{directoryId}/Schemas/urn:ietf:params:scim:schemas:core:2.0:User
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/Schemas/urn:ietf:params:scim:schemas:core:2.0:User"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_group_schemas(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get group schemas

        Path: /scim/directory/{directoryId}/Schemas/urn:ietf:params:scim:schemas:core:2.0:Group
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/Schemas/urn:ietf:params:scim:schemas:core:2.0:Group"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_extension_user_schemas(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get user enterprise extension schemas

        Path: /scim/directory/{directoryId}/Schemas/urn:ietf:params:scim:schemas:extension:enterprise:2.0:User
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/Schemas/urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_config(
        self,
        directory_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get feature metadata

        Path: /scim/directory/{directoryId}/ServiceProviderConfig
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/ServiceProviderConfig"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_a_user_from_active_directory(
        self,
        directory_id: str,
        user_id: str,
        attributes: Optional[str] = None,
        excluded_attributes: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get a user by ID

        Path: /scim/directory/{directoryId}/Users/{userId}
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/Users/{user_id}"
        params = {
            "attributes": attributes,
            "excludedAttributes": excluded_attributes,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_update_user_information_in_an_active_directory(
        self,
        directory_id: str,
        user_id: str,
        attributes: Optional[str] = None,
        excluded_attributes: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Update user via user attributes

        Path: /scim/directory/{directoryId}/Users/{userId}
        Method: PUT
        """
        path = f"/scim/directory/{directory_id}/Users/{user_id}"
        params = {
            "attributes": attributes,
            "excludedAttributes": excluded_attributes,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_delete_a_user_from_an_active_directory(
        self,
        directory_id: str,
        user_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete a user

        Path: /scim/directory/{directoryId}/Users/{userId}
        Method: DELETE
        """
        path = f"/scim/directory/{directory_id}/Users/{user_id}"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_patch_user_information_in_an_active_directory(
        self,
        directory_id: str,
        user_id: str,
        attributes: Optional[str] = None,
        excluded_attributes: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Update user by ID (PATCH)

        Path: /scim/directory/{directoryId}/Users/{userId}
        Method: PATCH
        """
        path = f"/scim/directory/{directory_id}/Users/{user_id}"
        params = {
            "attributes": attributes,
            "excludedAttributes": excluded_attributes,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PATCH", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_users_from_an_active_directory(
        self,
        directory_id: str,
        attributes: Optional[str] = None,
        excluded_attributes: Optional[str] = None,
        filter: Optional[str] = None,
        start_index: Optional[int] = None,
        count: Optional[int] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get users

        Path: /scim/directory/{directoryId}/Users
        Method: GET
        """
        path = f"/scim/directory/{directory_id}/Users"
        params = {
            "attributes": attributes,
            "excludedAttributes": excluded_attributes,
            "filter": filter,
            "startIndex": start_index,
            "count": count,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_create_a_user_in_an_active_directory(
        self,
        directory_id: str,
        attributes: Optional[str] = None,
        excluded_attributes: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Create a user

        Path: /scim/directory/{directoryId}/Users
        Method: POST
        """
        path = f"/scim/directory/{directory_id}/Users"
        params = {
            "attributes": attributes,
            "excludedAttributes": excluded_attributes,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db(
        self,
        org_id: str,
        aaid: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Delete user in SCIM DB

        Path: /admin/user-provisioning/v1/org/{org_id}/user/{AAID}/onlyDeleteUserInDB
        Method: DELETE
        """
        path = (
            f"/admin/user-provisioning/v1/org/{org_id}/user/{aaid}/onlyDeleteUserInDB"
        )
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_scim_links(
        self,
        org_id: str,
        aa_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get SCIM links for an account

        Path: /admin/user-provisioning/v1/org/{org_id}/user/{aaId}/get-scim-links
        Method: GET
        """
        path = f"/admin/user-provisioning/v1/org/{org_id}/user/{aa_id}/get-scim-links"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_get_scim_links_by_email(
        self,
        org_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Get SCIM Links for an email

        Path: /admin/user-provisioning/v1/org/{org_id}/get-scim-links-for-email
        Method: POST
        """
        path = f"/admin/user-provisioning/v1/org/{org_id}/get-scim-links-for-email"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def user_provisioning_cloud_unlink_scim_user(
        self,
        org_id: str,
        scim_directory_id: str,
        scim_user_id: str,
        payload: Optional[Dict[str, Any]] = None,
        _max_pages: Optional[int] = None,
    ) -> Response:
        """Unlink a SCIM user from their Atlassian account

        Path: /admin/user-provisioning/v1/org/{org_id}/scimDirectoryId/{scimDirectoryId}/scimUserId/{scimUserId}/unlink
        Method: PATCH
        """
        path = f"/admin/user-provisioning/v1/org/{org_id}/scimDirectoryId/{scim_directory_id}/scimUserId/{scim_user_id}/unlink"
        params = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PATCH", path, params=params, json=payload if payload else None
        )
