# Generated API Client for OrgCloud
from typing import Any

from ..models import Response
from .base import BaseAtlassianClient


class OrgCloudAPI:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    def org_cloud_get_orgs(
        self,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get organizations

        Path: /v1/orgs
        Method: GET
        """
        path = "/v1/orgs"
        params = {
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_org_by_id(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get an organization by ID

        Path: /v1/orgs/{org_id}
        Method: GET
        """
        path = f"/v1/orgs/{org_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_directory_users(
        self,
        org_id: str,
        directory_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get users in an organization

        Path: /v2/orgs/{org_id}/directories/{directoryId}/users
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/users"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_directory_user_details(
        self,
        org_id: str,
        directory_id: str,
        user_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get details of a user in a directory

        Path: /v2/orgs/{org_id}/directories/{directoryId}/users/{userId}
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/users/{user_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_users(
        self,
        org_id: str,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get managed accounts in an organization

        Path: /v1/orgs/{org_id}/users
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/users"
        params = {
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v2_orgs_org_id_users_invite(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Invite users to an organization

        Path: /v2/orgs/{org_id}/users/invite
        Method: POST
        """
        path = f"/v2/orgs/{org_id}/users/invite"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_user_role_assignments(
        self,
        org_id: str,
        directory_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user role assignments

        Path: /v2/orgs/{org_id}/directories/{directoryId}/users/{accountId}/role-assignments
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/users/{account_id}/role-assignments"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_assign_role(
        self,
        org_id: str,
        user_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Grant user access

        Path: /v1/orgs/{org_id}/users/{userId}/roles/assign
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/users/{user_id}/roles/assign"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_revoke_role(
        self,
        org_id: str,
        user_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Revoke user access

        Path: /v1/orgs/{org_id}/users/{userId}/roles/revoke
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/users/{user_id}/roles/revoke"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend(
        self,
        org_id: str,
        directory_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Suspend user access in directory

        Path: /v2/orgs/{org_id}/directories/{directoryId}/users/{accountId}/suspend
        Method: POST
        """
        path = (
            f"/v2/orgs/{org_id}/directories/{directory_id}/users/{account_id}/suspend"
        )
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore(
        self,
        org_id: str,
        directory_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Restore user access in directory

        Path: /v2/orgs/{org_id}/directories/{directoryId}/users/{accountId}/restore
        Method: POST
        """
        path = (
            f"/v2/orgs/{org_id}/directories/{directory_id}/users/{account_id}/restore"
        )
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id(
        self,
        org_id: str,
        directory_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove user from directory

        Path: /v2/orgs/{org_id}/directories/{directoryId}/users/{accountId}
        Method: DELETE
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/users/{account_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign(
        self,
        org_id: str,
        user_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign organization-level role

        Path: /v1/orgs/{org_id}/users/{userId}/role-assignments/assign
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/users/{user_id}/role-assignments/assign"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke(
        self,
        org_id: str,
        user_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove organization-level role

        Path: /v1/orgs/{org_id}/users/{userId}/role-assignments/revoke
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/users/{user_id}/role-assignments/revoke"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_directory_users_count(
        self,
        org_id: str,
        directory_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get count of users in an organization

        Path: /v2/orgs/{org_id}/directories/{directoryId}/users/count
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/users/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_user_stats(
        self,
        org_id: str,
        directory_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get user stats in an organization

        Path: /v2/orgs/{org_id}/directories/{directoryId}/users/stats
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/users/stats"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates(
        self,
        org_id: str,
        account_id: str,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """User’s last active dates

        Path: /v1/orgs/{org_id}/directory/users/{accountId}/last-active-dates
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/directory/users/{account_id}/last-active-dates"
        params = {
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_search_users(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search for users in an organization

        Path: /v1/orgs/{org_id}/users/search
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/users/search"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v1_orgs_org_id_users_invite(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Invite user to org

        Path: /v1/orgs/{org_id}/users/invite
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/users/invite"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access(
        self,
        org_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Suspend user access

        Path: /v1/orgs/{org_id}/directory/users/{accountId}/suspend-access
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/directory/users/{account_id}/suspend-access"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access(
        self,
        org_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Restore user access

        Path: /v1/orgs/{org_id}/directory/users/{accountId}/restore-access
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/directory/users/{account_id}/restore-access"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_delete_v1_orgs_org_id_directory_users_account_id(
        self,
        org_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove user access

        Path: /v1/orgs/{org_id}/directory/users/{accountId}
        Method: DELETE
        """
        path = f"/v1/orgs/{org_id}/directory/users/{account_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_groups(
        self,
        org_id: str,
        directory_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get groups in an organization

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v2_orgs_org_id_directories_directory_id_groups(
        self,
        org_id: str,
        directory_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create group

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups
        Method: POST
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_group_role_assignments(
        self,
        org_id: str,
        directory_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group role assignments

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/{groupId}/role-assignments
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/{group_id}/role-assignments"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign(
        self,
        org_id: str,
        directory_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Grant access to group

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/{groupId}/role-assignments/assign
        Method: POST
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/{group_id}/role-assignments/assign"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke(
        self,
        org_id: str,
        directory_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove access from group

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/{groupId}/role-assignments/revoke'
        Method: POST
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/{group_id}/role-assignments/revoke"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships(
        self,
        org_id: str,
        directory_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add user to group

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/{groupId}/memberships
        Method: POST
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/{group_id}/memberships"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id(
        self,
        org_id: str,
        directory_id: str,
        group_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove user from group

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/{groupId}/memberships/{accountId}"
        Method: DELETE
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/{group_id}/memberships/{account_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id(
        self,
        org_id: str,
        directory_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete group

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/{groupId}
        Method: DELETE
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/{group_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_group(
        self,
        org_id: str,
        directory_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group details

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/{groupId}
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/{group_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_groups_count(
        self,
        org_id: str,
        directory_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get the count of groups in an organization

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/count
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/count"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_groups_stats(
        self,
        org_id: str,
        directory_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get group stats

        Path: /v2/orgs/{org_id}/directories/{directoryId}/groups/stats
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories/{directory_id}/groups/stats"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_search_groups(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Search for groups within an organization

        Path: /v1/orgs/{org_id}/groups/search
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/groups/search"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v1_orgs_org_id_directory_groups(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create group

        Path: /v1/orgs/{org_id}/directory/groups
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/directory/groups"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_delete_v1_orgs_org_id_directory_groups_group_id(
        self,
        org_id: str,
        group_id: str,
        force_if_not_empty: bool | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete group

        Path: /v1/orgs/{org_id}/directory/groups/{groupId}
        Method: DELETE
        """
        path = f"/v1/orgs/{org_id}/directory/groups/{group_id}"
        params = {
            "forceIfNotEmpty": force_if_not_empty,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def org_cloud_assign_role_to_group(
        self,
        org_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Assign roles to a group

        Path: /v1/orgs/{org_id}/directory/groups/{groupId}/roles/assign
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/directory/groups/{group_id}/roles/assign"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_revoke_role_to_group(
        self,
        org_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Revoke roles from a group

        Path: /v1/orgs/{org_id}/directory/groups/{groupId}/roles/revoke
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/directory/groups/{group_id}/roles/revoke"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships(
        self,
        org_id: str,
        group_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add user to group

        Path: /v1/orgs/{org_id}/directory/groups/{groupId}/memberships
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/directory/groups/{group_id}/memberships"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id(
        self,
        org_id: str,
        group_id: str,
        account_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Remove user from group

        Path: /v1/orgs/{org_id}/directory/groups/{groupId}/memberships/{accountId}
        Method: DELETE
        """
        path = f"/v1/orgs/{org_id}/directory/groups/{group_id}/memberships/{account_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_directories_for_org(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get directories in an organization

        Path: /v2/orgs/{org_id}/directories
        Method: GET
        """
        path = f"/v2/orgs/{org_id}/directories"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_domains(
        self,
        org_id: str,
        cursor: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get domains in an organization

        Path: /v1/orgs/{org_id}/domains
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/domains"
        params = {
            "cursor": cursor,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_domain_by_id(
        self,
        org_id: str,
        domain_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get domain by ID

        Path: /v1/orgs/{org_id}/domains/{domainId}
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/domains/{domain_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_events(
        self,
        org_id: str,
        cursor: str | None = None,
        q: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        action: str | None = None,
        actor: list[Any] | None = None,
        ip: list[Any] | None = None,
        product: list[Any] | None = None,
        location: str | None = None,
        limit: int | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Query audit log events

        Path: /v1/orgs/{org_id}/events
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/events"
        params = {
            "cursor": cursor,
            "q": q,
            "from": from_,
            "to": to,
            "action": action,
            "actor": actor,
            "ip": ip,
            "product": product,
            "location": location,
            "limit": limit,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_poll_events(
        self,
        org_id: str,
        cursor: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        sort_order: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Poll audit log events

        Path: /v1/orgs/{org_id}/events-stream
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/events-stream"
        params = {
            "cursor": cursor,
            "from": from_,
            "to": to,
            "limit": limit,
            "sortOrder": sort_order,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_event_by_id(
        self,
        org_id: str,
        event_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get an event by ID

        Path: /v1/orgs/{org_id}/events/{eventId}
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/events/{event_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_event_actions(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get list of event actions

        Path: /v1/orgs/{org_id}/event-actions
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/event-actions"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_policies(
        self,
        org_id: str,
        cursor: str | None = None,
        type_: str | None = None,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get list of policies

        Path: /v1/orgs/{org_id}/policies
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/policies"
        params = {
            "cursor": cursor,
            "type": type_,
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_create_policy(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Create a policy

        Path: /v1/orgs/{org_id}/policies
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/policies"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_get_policy_by_id(
        self,
        org_id: str,
        policy_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get a policy by ID

        Path: /v1/orgs/{org_id}/policies/{policyId}
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/policies/{policy_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_update_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update a policy

        Path: /v1/orgs/{org_id}/policies/{policyId}
        Method: PUT
        """
        path = f"/v1/orgs/{org_id}/policies/{policy_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def org_cloud_delete_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete a policy

        Path: /v1/orgs/{org_id}/policies/{policyId}
        Method: DELETE
        """
        path = f"/v1/orgs/{org_id}/policies/{policy_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def org_cloud_add_resource_to_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Add Resource to Policy

        Path: /v1/orgs/{org_id}/policies/{policyId}/resources
        Method: POST
        """
        path = f"/v1/orgs/{org_id}/policies/{policy_id}/resources"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )

    def org_cloud_update_policy_resource(
        self,
        org_id: str,
        policy_id: str,
        resource_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Update Policy Resource

        Path: /v1/orgs/{org_id}/policies/{policyId}/resources/{resourceId}
        Method: PUT
        """
        path = f"/v1/orgs/{org_id}/policies/{policy_id}/resources/{resource_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "PUT", path, params=params, json=payload if payload else None
        )

    def org_cloud_delete_policy_resource(
        self,
        org_id: str,
        policy_id: str,
        resource_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Delete Policy Resource

        Path: /v1/orgs/{org_id}/policies/{policyId}/resources/{resourceId}
        Method: DELETE
        """
        path = f"/v1/orgs/{org_id}/policies/{policy_id}/resources/{resource_id}"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "DELETE", path, params=params, json=payload if payload else None
        )

    def org_cloud_validate_policy(
        self,
        org_id: str,
        policy_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Validate Policy

        Path: /v1/orgs/{org_id}/policies/{policyId}/validate
        Method: GET
        """
        path = f"/v1/orgs/{org_id}/policies/{policy_id}/validate"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "GET", path, params=params, json=payload if payload else None
        )

    def org_cloud_query_workspaces_v2(
        self,
        org_id: str,
        payload: dict[str, Any] | None = None,
        _max_pages: int | None = None,
    ) -> Response:
        """Get list of workspaces

        Path: /v2/orgs/{org_id}/workspaces
        Method: POST
        """
        path = f"/v2/orgs/{org_id}/workspaces"
        params: dict[str, Any] = {}
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(
            "POST", path, params=params, json=payload if payload else None
        )
