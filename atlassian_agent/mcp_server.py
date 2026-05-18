#!/usr/bin/python
import warnings

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import logging
import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from atlassian_agent.auth import (  # type: ignore
    get_admin_cloud_client,
    get_api_access_cloud_client,
    get_confluence_cloud_client,
    get_confluence_server_client,
    get_control_cloud_client,
    get_dlp_cloud_client,
    get_jira_cloud_client,
    get_jira_server_client,
    get_org_cloud_client,
    get_user_mgmt_cloud_client,
    get_user_provisioning_cloud_client,
)

__version__ = "0.10.0"

logger = get_logger(name="atlassian-agent")
logger.setLevel(logging.INFO)


def register_atlassian_control_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-control"})
    async def atlassian_atlassian_control(
        action: str = Field(
            description="Action to perform. Must be one of: 'control_cloud_ap_is_get_policies', 'control_cloud_ap_is_create_policy', 'control_cloud_ap_is_get_policy', 'control_cloud_ap_is_update_policy', 'control_cloud_ap_is_delete_policy', 'control_cloud_ap_is_get_policies_v2', 'control_cloud_ap_is_create_policy_v2', 'control_cloud_ap_is_get_policy_v2', 'control_cloud_ap_is_update_policy_v2', 'control_cloud_ap_is_publish_draft_policies', 'control_cloud_ap_is_get_resources', 'control_cloud_ap_is_create_resource', 'control_cloud_ap_is_delete_resources', 'control_cloud_ap_is_update_resource', 'control_cloud_ap_is_delete_resource', 'control_cloud_ap_is_get_resources_v2', 'control_cloud_ap_is_attach_detach_resources_v2', 'control_cloud_ap_is_delete_resources_v2', 'control_cloud_ap_is_validate_policy', 'control_cloud_ap_is_add_users_to_policy', 'control_cloud_ap_is_get_task_status', 'control_cloud_ap_is_bulk_fetch_auth_policy'"
        ),
        client=Depends(get_control_cloud_client),
    ) -> dict:
        """Manage atlassian control operations.

        Actions:
          - 'control_cloud_ap_is_get_policies': Call control_cloud_ap_is_get_policies
          - 'control_cloud_ap_is_create_policy': Call control_cloud_ap_is_create_policy
          - 'control_cloud_ap_is_get_policy': Call control_cloud_ap_is_get_policy
          - 'control_cloud_ap_is_update_policy': Call control_cloud_ap_is_update_policy
          - 'control_cloud_ap_is_delete_policy': Call control_cloud_ap_is_delete_policy
          - 'control_cloud_ap_is_get_policies_v2': Call control_cloud_ap_is_get_policies_v2
          - 'control_cloud_ap_is_create_policy_v2': Call control_cloud_ap_is_create_policy_v2
          - 'control_cloud_ap_is_get_policy_v2': Call control_cloud_ap_is_get_policy_v2
          - 'control_cloud_ap_is_update_policy_v2': Call control_cloud_ap_is_update_policy_v2
          - 'control_cloud_ap_is_publish_draft_policies': Call control_cloud_ap_is_publish_draft_policies
          - 'control_cloud_ap_is_get_resources': Call control_cloud_ap_is_get_resources
          - 'control_cloud_ap_is_create_resource': Call control_cloud_ap_is_create_resource
          - 'control_cloud_ap_is_delete_resources': Call control_cloud_ap_is_delete_resources
          - 'control_cloud_ap_is_update_resource': Call control_cloud_ap_is_update_resource
          - 'control_cloud_ap_is_delete_resource': Call control_cloud_ap_is_delete_resource
          - 'control_cloud_ap_is_get_resources_v2': Call control_cloud_ap_is_get_resources_v2
          - 'control_cloud_ap_is_attach_detach_resources_v2': Call control_cloud_ap_is_attach_detach_resources_v2
          - 'control_cloud_ap_is_delete_resources_v2': Call control_cloud_ap_is_delete_resources_v2
          - 'control_cloud_ap_is_validate_policy': Call control_cloud_ap_is_validate_policy
          - 'control_cloud_ap_is_add_users_to_policy': Call control_cloud_ap_is_add_users_to_policy
          - 'control_cloud_ap_is_get_task_status': Call control_cloud_ap_is_get_task_status
          - 'control_cloud_ap_is_bulk_fetch_auth_policy': Call control_cloud_ap_is_bulk_fetch_auth_policy
        """
        kwargs: dict[str, Any]
        if action == "control_cloud_ap_is_get_policies":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_get_policies(**kwargs)
        if action == "control_cloud_ap_is_create_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_create_policy(**kwargs)
        if action == "control_cloud_ap_is_get_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_get_policy(**kwargs)
        if action == "control_cloud_ap_is_update_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_update_policy(**kwargs)
        if action == "control_cloud_ap_is_delete_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_delete_policy(**kwargs)
        if action == "control_cloud_ap_is_get_policies_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_get_policies_v2(**kwargs)
        if action == "control_cloud_ap_is_create_policy_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_create_policy_v2(**kwargs)
        if action == "control_cloud_ap_is_get_policy_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_get_policy_v2(**kwargs)
        if action == "control_cloud_ap_is_update_policy_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_update_policy_v2(**kwargs)
        if action == "control_cloud_ap_is_publish_draft_policies":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_publish_draft_policies(**kwargs)
        if action == "control_cloud_ap_is_get_resources":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_get_resources(**kwargs)
        if action == "control_cloud_ap_is_create_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_create_resource(**kwargs)
        if action == "control_cloud_ap_is_delete_resources":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_delete_resources(**kwargs)
        if action == "control_cloud_ap_is_update_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_update_resource(**kwargs)
        if action == "control_cloud_ap_is_delete_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_delete_resource(**kwargs)
        if action == "control_cloud_ap_is_get_resources_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_get_resources_v2(**kwargs)
        if action == "control_cloud_ap_is_attach_detach_resources_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_attach_detach_resources_v2(**kwargs)
        if action == "control_cloud_ap_is_delete_resources_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_delete_resources_v2(**kwargs)
        if action == "control_cloud_ap_is_validate_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_validate_policy(**kwargs)
        if action == "control_cloud_ap_is_add_users_to_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_add_users_to_policy(**kwargs)
        if action == "control_cloud_ap_is_get_task_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_get_task_status(**kwargs)
        if action == "control_cloud_ap_is_bulk_fetch_auth_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.control_cloud_ap_is_bulk_fetch_auth_policy(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: control_cloud_ap_is_get_policies', 'control_cloud_ap_is_create_policy', 'control_cloud_ap_is_get_policy', 'control_cloud_ap_is_update_policy', 'control_cloud_ap_is_delete_policy', 'control_cloud_ap_is_get_policies_v2', 'control_cloud_ap_is_create_policy_v2', 'control_cloud_ap_is_get_policy_v2', 'control_cloud_ap_is_update_policy_v2', 'control_cloud_ap_is_publish_draft_policies', 'control_cloud_ap_is_get_resources', 'control_cloud_ap_is_create_resource', 'control_cloud_ap_is_delete_resources', 'control_cloud_ap_is_update_resource', 'control_cloud_ap_is_delete_resource', 'control_cloud_ap_is_get_resources_v2', 'control_cloud_ap_is_attach_detach_resources_v2', 'control_cloud_ap_is_delete_resources_v2', 'control_cloud_ap_is_validate_policy', 'control_cloud_ap_is_add_users_to_policy', 'control_cloud_ap_is_get_task_status', 'control_cloud_ap_is_bulk_fetch_auth_policy"
        )


def register_atlassian_org_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-org"})
    async def atlassian_atlassian_org(
        action: str = Field(
            description="Action to perform. Must be one of: 'org_cloud_get_orgs', 'org_cloud_get_org_by_id', 'org_cloud_get_directory_users', 'org_cloud_get_directory_user_details', 'org_cloud_get_users', 'org_cloud_post_v2_orgs_org_id_users_invite', 'org_cloud_get_user_role_assignments', 'org_cloud_assign_role', 'org_cloud_revoke_role', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore', 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id', 'org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign', 'org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke', 'org_cloud_get_directory_users_count', 'org_cloud_get_user_stats', 'org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates', 'org_cloud_search_users', 'org_cloud_post_v1_orgs_org_id_users_invite', 'org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access', 'org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access', 'org_cloud_delete_v1_orgs_org_id_directory_users_account_id', 'org_cloud_get_groups', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups', 'org_cloud_get_group_role_assignments', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships', 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id', 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id', 'org_cloud_get_group', 'org_cloud_get_groups_count', 'org_cloud_get_groups_stats', 'org_cloud_search_groups', 'org_cloud_post_v1_orgs_org_id_directory_groups', 'org_cloud_delete_v1_orgs_org_id_directory_groups_group_id', 'org_cloud_assign_role_to_group', 'org_cloud_revoke_role_to_group', 'org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships', 'org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id', 'org_cloud_get_directories_for_org', 'org_cloud_get_domains', 'org_cloud_get_domain_by_id', 'org_cloud_get_events', 'org_cloud_poll_events', 'org_cloud_get_event_by_id', 'org_cloud_get_event_actions', 'org_cloud_get_policies', 'org_cloud_create_policy', 'org_cloud_get_policy_by_id', 'org_cloud_update_policy', 'org_cloud_delete_policy', 'org_cloud_add_resource_to_policy', 'org_cloud_update_policy_resource', 'org_cloud_delete_policy_resource', 'org_cloud_validate_policy', 'org_cloud_query_workspaces_v2'"
        ),
        client=Depends(get_org_cloud_client),
    ) -> dict:
        """Manage atlassian org operations.

        Actions:
          - 'org_cloud_get_orgs': Call org_cloud_get_orgs
          - 'org_cloud_get_org_by_id': Call org_cloud_get_org_by_id
          - 'org_cloud_get_directory_users': Call org_cloud_get_directory_users
          - 'org_cloud_get_directory_user_details': Call org_cloud_get_directory_user_details
          - 'org_cloud_get_users': Call org_cloud_get_users
          - 'org_cloud_post_v2_orgs_org_id_users_invite': Call org_cloud_post_v2_orgs_org_id_users_invite
          - 'org_cloud_get_user_role_assignments': Call org_cloud_get_user_role_assignments
          - 'org_cloud_assign_role': Call org_cloud_assign_role
          - 'org_cloud_revoke_role': Call org_cloud_revoke_role
          - 'org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend': Call org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend
          - 'org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore': Call org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore
          - 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id': Call org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id
          - 'org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign': Call org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign
          - 'org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke': Call org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke
          - 'org_cloud_get_directory_users_count': Call org_cloud_get_directory_users_count
          - 'org_cloud_get_user_stats': Call org_cloud_get_user_stats
          - 'org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates': Call org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates
          - 'org_cloud_search_users': Call org_cloud_search_users
          - 'org_cloud_post_v1_orgs_org_id_users_invite': Call org_cloud_post_v1_orgs_org_id_users_invite
          - 'org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access': Call org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access
          - 'org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access': Call org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access
          - 'org_cloud_delete_v1_orgs_org_id_directory_users_account_id': Call org_cloud_delete_v1_orgs_org_id_directory_users_account_id
          - 'org_cloud_get_groups': Call org_cloud_get_groups
          - 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups': Call org_cloud_post_v2_orgs_org_id_directories_directory_id_groups
          - 'org_cloud_get_group_role_assignments': Call org_cloud_get_group_role_assignments
          - 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign': Call org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign
          - 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke': Call org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke
          - 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships': Call org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships
          - 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id': Call org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id
          - 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id': Call org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id
          - 'org_cloud_get_group': Call org_cloud_get_group
          - 'org_cloud_get_groups_count': Call org_cloud_get_groups_count
          - 'org_cloud_get_groups_stats': Call org_cloud_get_groups_stats
          - 'org_cloud_search_groups': Call org_cloud_search_groups
          - 'org_cloud_post_v1_orgs_org_id_directory_groups': Call org_cloud_post_v1_orgs_org_id_directory_groups
          - 'org_cloud_delete_v1_orgs_org_id_directory_groups_group_id': Call org_cloud_delete_v1_orgs_org_id_directory_groups_group_id
          - 'org_cloud_assign_role_to_group': Call org_cloud_assign_role_to_group
          - 'org_cloud_revoke_role_to_group': Call org_cloud_revoke_role_to_group
          - 'org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships': Call org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships
          - 'org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id': Call org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id
          - 'org_cloud_get_directories_for_org': Call org_cloud_get_directories_for_org
          - 'org_cloud_get_domains': Call org_cloud_get_domains
          - 'org_cloud_get_domain_by_id': Call org_cloud_get_domain_by_id
          - 'org_cloud_get_events': Call org_cloud_get_events
          - 'org_cloud_poll_events': Call org_cloud_poll_events
          - 'org_cloud_get_event_by_id': Call org_cloud_get_event_by_id
          - 'org_cloud_get_event_actions': Call org_cloud_get_event_actions
          - 'org_cloud_get_policies': Call org_cloud_get_policies
          - 'org_cloud_create_policy': Call org_cloud_create_policy
          - 'org_cloud_get_policy_by_id': Call org_cloud_get_policy_by_id
          - 'org_cloud_update_policy': Call org_cloud_update_policy
          - 'org_cloud_delete_policy': Call org_cloud_delete_policy
          - 'org_cloud_add_resource_to_policy': Call org_cloud_add_resource_to_policy
          - 'org_cloud_update_policy_resource': Call org_cloud_update_policy_resource
          - 'org_cloud_delete_policy_resource': Call org_cloud_delete_policy_resource
          - 'org_cloud_validate_policy': Call org_cloud_validate_policy
          - 'org_cloud_query_workspaces_v2': Call org_cloud_query_workspaces_v2
        """
        kwargs: dict[str, Any]
        if action == "org_cloud_get_orgs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_orgs(**kwargs)
        if action == "org_cloud_get_org_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_org_by_id(**kwargs)
        if action == "org_cloud_get_directory_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_directory_users(**kwargs)
        if action == "org_cloud_get_directory_user_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_directory_user_details(**kwargs)
        if action == "org_cloud_get_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_users(**kwargs)
        if action == "org_cloud_post_v2_orgs_org_id_users_invite":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v2_orgs_org_id_users_invite(**kwargs)
        if action == "org_cloud_get_user_role_assignments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_user_role_assignments(**kwargs)
        if action == "org_cloud_assign_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_assign_role(**kwargs)
        if action == "org_cloud_revoke_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_revoke_role(**kwargs)
        if (
            action
            == "org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend(
                **kwargs
            )
        if (
            action
            == "org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore(
                **kwargs
            )
        if (
            action
            == "org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id(
                **kwargs
            )
        if (
            action
            == "org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign(
                **kwargs
            )
        if (
            action
            == "org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke(
                **kwargs
            )
        if action == "org_cloud_get_directory_users_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_directory_users_count(**kwargs)
        if action == "org_cloud_get_user_stats":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_user_stats(**kwargs)
        if (
            action
            == "org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates(
                **kwargs
            )
        if action == "org_cloud_search_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_search_users(**kwargs)
        if action == "org_cloud_post_v1_orgs_org_id_users_invite":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v1_orgs_org_id_users_invite(**kwargs)
        if (
            action
            == "org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access(
                **kwargs
            )
        if (
            action
            == "org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access(
                **kwargs
            )
        if action == "org_cloud_delete_v1_orgs_org_id_directory_users_account_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_delete_v1_orgs_org_id_directory_users_account_id(
                **kwargs
            )
        if action == "org_cloud_get_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_groups(**kwargs)
        if action == "org_cloud_post_v2_orgs_org_id_directories_directory_id_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v2_orgs_org_id_directories_directory_id_groups(
                **kwargs
            )
        if action == "org_cloud_get_group_role_assignments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_group_role_assignments(**kwargs)
        if (
            action
            == "org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign(
                **kwargs
            )
        if (
            action
            == "org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke(
                **kwargs
            )
        if (
            action
            == "org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships(
                **kwargs
            )
        if (
            action
            == "org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id(
                **kwargs
            )
        if (
            action
            == "org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id(
                **kwargs
            )
        if action == "org_cloud_get_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_group(**kwargs)
        if action == "org_cloud_get_groups_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_groups_count(**kwargs)
        if action == "org_cloud_get_groups_stats":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_groups_stats(**kwargs)
        if action == "org_cloud_search_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_search_groups(**kwargs)
        if action == "org_cloud_post_v1_orgs_org_id_directory_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v1_orgs_org_id_directory_groups(**kwargs)
        if action == "org_cloud_delete_v1_orgs_org_id_directory_groups_group_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_delete_v1_orgs_org_id_directory_groups_group_id(
                **kwargs
            )
        if action == "org_cloud_assign_role_to_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_assign_role_to_group(**kwargs)
        if action == "org_cloud_revoke_role_to_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_revoke_role_to_group(**kwargs)
        if (
            action
            == "org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships(
                **kwargs
            )
        if (
            action
            == "org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id(
                **kwargs
            )
        if action == "org_cloud_get_directories_for_org":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_directories_for_org(**kwargs)
        if action == "org_cloud_get_domains":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_domains(**kwargs)
        if action == "org_cloud_get_domain_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_domain_by_id(**kwargs)
        if action == "org_cloud_get_events":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_events(**kwargs)
        if action == "org_cloud_poll_events":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_poll_events(**kwargs)
        if action == "org_cloud_get_event_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_event_by_id(**kwargs)
        if action == "org_cloud_get_event_actions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_event_actions(**kwargs)
        if action == "org_cloud_get_policies":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_policies(**kwargs)
        if action == "org_cloud_create_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_create_policy(**kwargs)
        if action == "org_cloud_get_policy_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_get_policy_by_id(**kwargs)
        if action == "org_cloud_update_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_update_policy(**kwargs)
        if action == "org_cloud_delete_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_delete_policy(**kwargs)
        if action == "org_cloud_add_resource_to_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_add_resource_to_policy(**kwargs)
        if action == "org_cloud_update_policy_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_update_policy_resource(**kwargs)
        if action == "org_cloud_delete_policy_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_delete_policy_resource(**kwargs)
        if action == "org_cloud_validate_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_validate_policy(**kwargs)
        if action == "org_cloud_query_workspaces_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.org_cloud_query_workspaces_v2(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: org_cloud_get_orgs', 'org_cloud_get_org_by_id', 'org_cloud_get_directory_users', 'org_cloud_get_directory_user_details', 'org_cloud_get_users', 'org_cloud_post_v2_orgs_org_id_users_invite', 'org_cloud_get_user_role_assignments', 'org_cloud_assign_role', 'org_cloud_revoke_role', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore', 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id', 'org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign', 'org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke', 'org_cloud_get_directory_users_count', 'org_cloud_get_user_stats', 'org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates', 'org_cloud_search_users', 'org_cloud_post_v1_orgs_org_id_users_invite', 'org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access', 'org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access', 'org_cloud_delete_v1_orgs_org_id_directory_users_account_id', 'org_cloud_get_groups', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups', 'org_cloud_get_group_role_assignments', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke', 'org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships', 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id', 'org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id', 'org_cloud_get_group', 'org_cloud_get_groups_count', 'org_cloud_get_groups_stats', 'org_cloud_search_groups', 'org_cloud_post_v1_orgs_org_id_directory_groups', 'org_cloud_delete_v1_orgs_org_id_directory_groups_group_id', 'org_cloud_assign_role_to_group', 'org_cloud_revoke_role_to_group', 'org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships', 'org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id', 'org_cloud_get_directories_for_org', 'org_cloud_get_domains', 'org_cloud_get_domain_by_id', 'org_cloud_get_events', 'org_cloud_poll_events', 'org_cloud_get_event_by_id', 'org_cloud_get_event_actions', 'org_cloud_get_policies', 'org_cloud_create_policy', 'org_cloud_get_policy_by_id', 'org_cloud_update_policy', 'org_cloud_delete_policy', 'org_cloud_add_resource_to_policy', 'org_cloud_update_policy_resource', 'org_cloud_delete_policy_resource', 'org_cloud_validate_policy', 'org_cloud_query_workspaces_v2"
        )


def register_jira_server_other_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-other"})
    async def atlassian_jira_server_other(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_move_issues_to_backlog', 'jira_server_get_issues_for_backlog', 'jira_server_get_configuration', 'jira_server_get_properties_keys', 'jira_server_get_property', 'jira_server_set_property', 'jira_server_delete_property', 'jira_server_get_refined_velocity', 'jira_server_set_refined_velocity', 'jira_server_get_all_versions', 'jira_server_rank_issues', 'jira_server_get_issue', 'jira_server_get_properties_keys_1', 'jira_server_get_property_1', 'jira_server_set_property_1', 'jira_server_delete_property_1', 'jira_server_get_application_property', 'jira_server_get_advanced_settings', 'jira_server_get_all', 'jira_server_put_bulk', 'jira_server_get_4', 'jira_server_put_2', 'jira_server_expand_for_humans', 'jira_server_expand_for_machines', 'jira_server_delete_node', 'jira_server_change_node_state_to_offline', 'jira_server_get_all_nodes', 'jira_server_acknowledge_errors', 'jira_server_get_state', 'jira_server_get_properties_keys_1_2', 'jira_server_get_comment_property', 'jira_server_set_property_1_2', 'jira_server_delete_property_2', 'jira_server_create_component', 'jira_server_get_paginated_components', 'jira_server_get_component', 'jira_server_update_component', 'jira_server_delete', 'jira_server_get_component_related_issues', 'jira_server_get_configuration_1', 'jira_server_list', 'jira_server_get_dashboard_item_properties_keys', 'jira_server_get_property_1_2', 'jira_server_set_dashboard_item_property', 'jira_server_delete_property_1_2', 'jira_server_download_email_templates', 'jira_server_upload_email_templates', 'jira_server_apply_email_templates', 'jira_server_revert_email_templates_to_default', 'jira_server_get_email_types', 'jira_server_get_default_share_scope', 'jira_server_set_default_share_scope', 'jira_server_default_columns_1', 'jira_server_set_columns_1', 'jira_server_reset_columns_1', 'jira_server_create_issue', 'jira_server_archive_issues', 'jira_server_create_issues', 'jira_server_get_issue_picker_resource', 'jira_server_get_issue_2', 'jira_server_edit_issue', 'jira_server_delete_issue', 'jira_server_archive_issue', 'jira_server_assign', 'jira_server_get_edit_issue_meta', 'jira_server_notify', 'jira_server_get_issue_properties_keys', 'jira_server_get_property_3', 'jira_server_set_issue_property', 'jira_server_delete_property_3', 'jira_server_restore_issue', 'jira_server_link_issues', 'jira_server_reset_order', 'jira_server_get_issue_security_schemes', 'jira_server_get_issue_security_scheme', 'jira_server_get_issue_all_types', 'jira_server_create_avatar_from_temporary', 'jira_server_store_temporary_avatar_using_multi_part', 'jira_server_get_property_keys', 'jira_server_get_property_4', 'jira_server_set_property_3', 'jira_server_delete_property_4', 'jira_server_get_auto_complete', 'jira_server_validate', 'jira_server_is_app_monitoring_enabled', 'jira_server_set_app_monitoring_enabled', 'jira_server_is_ipd_monitoring_enabled', 'jira_server_set_app_monitoring_enabled_1', 'jira_server_are_metrics_exposed', 'jira_server_get_available_metrics', 'jira_server_start', 'jira_server_stop', 'jira_server_get_preference', 'jira_server_set_preference', 'jira_server_remove_preference', 'jira_server_change_my_password', 'jira_server_get_notification_schemes', 'jira_server_get_notification_scheme', 'jira_server_get_password_policy', 'jira_server_get_scheme_attribute', 'jira_server_set_scheme_attribute', 'jira_server_get_priorities', 'jira_server_get_priorities_1', 'jira_server_create_avatar_from_temporary_1', 'jira_server_store_temporary_avatar_using_multi_part_1', 'jira_server_delete_avatar', 'jira_server_get_all_avatars', 'jira_server_get_properties_keys_3', 'jira_server_get_property_5', 'jira_server_set_property_4', 'jira_server_delete_property_5', 'jira_server_set_actors', 'jira_server_delete_actor', 'jira_server_get_all_statuses', 'jira_server_get_issue_security_scheme_1', 'jira_server_get_notification_scheme_1', 'jira_server_process_requests', 'jira_server_get_progress_bulk', 'jira_server_get_progress', 'jira_server_update_show_when_empty_indicator', 'jira_server_get_error', 'jira_server_get_max_aggregation_buckets', 'jira_server_get_max_result_window', 'jira_server_get_issuesecuritylevel', 'jira_server_set_base_url', 'jira_server_get_issue_navigator_default_columns', 'jira_server_set_issue_navigator_default_columns_form', 'jira_server_get_statuses', 'jira_server_get_paginated_statuses', 'jira_server_get_status', 'jira_server_get_status_categories', 'jira_server_get_status_category', 'jira_server_get_all_terminology_entries', 'jira_server_set_terminology_entries', 'jira_server_get_terminology_entry', 'jira_server_get_avatars', 'jira_server_create_avatar_from_temporary_2', 'jira_server_delete_avatar_1', 'jira_server_store_temporary_avatar_using_multi_part_2', 'jira_server_get_a11y_personal_settings', 'jira_server_get_progress_1', 'jira_server_unlock_anonymization', 'jira_server_create_avatar_from_temporary_3', 'jira_server_store_temporary_avatar_using_multi_part_3', 'jira_server_delete_avatar_2', 'jira_server_get_all_avatars_1', 'jira_server_default_columns', 'jira_server_set_columns_url_encoded', 'jira_server_reset_columns', 'jira_server_get_properties_keys_4', 'jira_server_get_property_6', 'jira_server_set_property_5', 'jira_server_delete_property_6', 'jira_server_delete_session', 'jira_server_get_paginated_versions', 'jira_server_create_version', 'jira_server_get_remote_version_links', 'jira_server_get_version', 'jira_server_update_version', 'jira_server_merge', 'jira_server_move_version', 'jira_server_get_version_related_issues', 'jira_server_delete_1', 'jira_server_get_version_unresolved_issues', 'jira_server_get_remote_version_links_by_version_id', 'jira_server_create_or_update_remote_version_link', 'jira_server_delete_remote_version_links_by_version_id', 'jira_server_get_remote_version_link', 'jira_server_create_or_update_remote_version_link_1', 'jira_server_delete_remote_version_link', 'jira_server_create_scheme', 'jira_server_get_by_id', 'jira_server_update', 'jira_server_delete_scheme', 'jira_server_create_draft_for_parent', 'jira_server_get_default', 'jira_server_update_default', 'jira_server_delete_default', 'jira_server_get_draft_by_id', 'jira_server_update_draft', 'jira_server_delete_draft_by_id', 'jira_server_get_draft_default', 'jira_server_update_draft_default', 'jira_server_delete_draft_default', 'jira_server_release'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server other operations.

        Actions:
          - 'jira_server_move_issues_to_backlog': Call jira_server_move_issues_to_backlog
          - 'jira_server_get_issues_for_backlog': Call jira_server_get_issues_for_backlog
          - 'jira_server_get_configuration': Call jira_server_get_configuration
          - 'jira_server_get_properties_keys': Call jira_server_get_properties_keys
          - 'jira_server_get_property': Call jira_server_get_property
          - 'jira_server_set_property': Call jira_server_set_property
          - 'jira_server_delete_property': Call jira_server_delete_property
          - 'jira_server_get_refined_velocity': Call jira_server_get_refined_velocity
          - 'jira_server_set_refined_velocity': Call jira_server_set_refined_velocity
          - 'jira_server_get_all_versions': Call jira_server_get_all_versions
          - 'jira_server_rank_issues': Call jira_server_rank_issues
          - 'jira_server_get_issue': Call jira_server_get_issue
          - 'jira_server_get_properties_keys_1': Call jira_server_get_properties_keys_1
          - 'jira_server_get_property_1': Call jira_server_get_property_1
          - 'jira_server_set_property_1': Call jira_server_set_property_1
          - 'jira_server_delete_property_1': Call jira_server_delete_property_1
          - 'jira_server_get_application_property': Call jira_server_get_application_property
          - 'jira_server_get_advanced_settings': Call jira_server_get_advanced_settings
          - 'jira_server_get_all': Call jira_server_get_all
          - 'jira_server_put_bulk': Call jira_server_put_bulk
          - 'jira_server_get_4': Call jira_server_get_4
          - 'jira_server_put_2': Call jira_server_put_2
          - 'jira_server_expand_for_humans': Call jira_server_expand_for_humans
          - 'jira_server_expand_for_machines': Call jira_server_expand_for_machines
          - 'jira_server_delete_node': Call jira_server_delete_node
          - 'jira_server_change_node_state_to_offline': Call jira_server_change_node_state_to_offline
          - 'jira_server_get_all_nodes': Call jira_server_get_all_nodes
          - 'jira_server_acknowledge_errors': Call jira_server_acknowledge_errors
          - 'jira_server_get_state': Call jira_server_get_state
          - 'jira_server_get_properties_keys_1_2': Call jira_server_get_properties_keys_1_2
          - 'jira_server_get_comment_property': Call jira_server_get_comment_property
          - 'jira_server_set_property_1_2': Call jira_server_set_property_1_2
          - 'jira_server_delete_property_2': Call jira_server_delete_property_2
          - 'jira_server_create_component': Call jira_server_create_component
          - 'jira_server_get_paginated_components': Call jira_server_get_paginated_components
          - 'jira_server_get_component': Call jira_server_get_component
          - 'jira_server_update_component': Call jira_server_update_component
          - 'jira_server_delete': Call jira_server_delete
          - 'jira_server_get_component_related_issues': Call jira_server_get_component_related_issues
          - 'jira_server_get_configuration_1': Call jira_server_get_configuration_1
          - 'jira_server_list': Call jira_server_list
          - 'jira_server_get_dashboard_item_properties_keys': Call jira_server_get_dashboard_item_properties_keys
          - 'jira_server_get_property_1_2': Call jira_server_get_property_1_2
          - 'jira_server_set_dashboard_item_property': Call jira_server_set_dashboard_item_property
          - 'jira_server_delete_property_1_2': Call jira_server_delete_property_1_2
          - 'jira_server_download_email_templates': Call jira_server_download_email_templates
          - 'jira_server_upload_email_templates': Call jira_server_upload_email_templates
          - 'jira_server_apply_email_templates': Call jira_server_apply_email_templates
          - 'jira_server_revert_email_templates_to_default': Call jira_server_revert_email_templates_to_default
          - 'jira_server_get_email_types': Call jira_server_get_email_types
          - 'jira_server_get_default_share_scope': Call jira_server_get_default_share_scope
          - 'jira_server_set_default_share_scope': Call jira_server_set_default_share_scope
          - 'jira_server_default_columns_1': Call jira_server_default_columns_1
          - 'jira_server_set_columns_1': Call jira_server_set_columns_1
          - 'jira_server_reset_columns_1': Call jira_server_reset_columns_1
          - 'jira_server_create_issue': Call jira_server_create_issue
          - 'jira_server_archive_issues': Call jira_server_archive_issues
          - 'jira_server_create_issues': Call jira_server_create_issues
          - 'jira_server_get_issue_picker_resource': Call jira_server_get_issue_picker_resource
          - 'jira_server_get_issue_2': Call jira_server_get_issue_2
          - 'jira_server_edit_issue': Call jira_server_edit_issue
          - 'jira_server_delete_issue': Call jira_server_delete_issue
          - 'jira_server_archive_issue': Call jira_server_archive_issue
          - 'jira_server_assign': Call jira_server_assign
          - 'jira_server_get_edit_issue_meta': Call jira_server_get_edit_issue_meta
          - 'jira_server_notify': Call jira_server_notify
          - 'jira_server_get_issue_properties_keys': Call jira_server_get_issue_properties_keys
          - 'jira_server_get_property_3': Call jira_server_get_property_3
          - 'jira_server_set_issue_property': Call jira_server_set_issue_property
          - 'jira_server_delete_property_3': Call jira_server_delete_property_3
          - 'jira_server_restore_issue': Call jira_server_restore_issue
          - 'jira_server_link_issues': Call jira_server_link_issues
          - 'jira_server_reset_order': Call jira_server_reset_order
          - 'jira_server_get_issue_security_schemes': Call jira_server_get_issue_security_schemes
          - 'jira_server_get_issue_security_scheme': Call jira_server_get_issue_security_scheme
          - 'jira_server_get_issue_all_types': Call jira_server_get_issue_all_types
          - 'jira_server_create_avatar_from_temporary': Call jira_server_create_avatar_from_temporary
          - 'jira_server_store_temporary_avatar_using_multi_part': Call jira_server_store_temporary_avatar_using_multi_part
          - 'jira_server_get_property_keys': Call jira_server_get_property_keys
          - 'jira_server_get_property_4': Call jira_server_get_property_4
          - 'jira_server_set_property_3': Call jira_server_set_property_3
          - 'jira_server_delete_property_4': Call jira_server_delete_property_4
          - 'jira_server_get_auto_complete': Call jira_server_get_auto_complete
          - 'jira_server_validate': Call jira_server_validate
          - 'jira_server_is_app_monitoring_enabled': Call jira_server_is_app_monitoring_enabled
          - 'jira_server_set_app_monitoring_enabled': Call jira_server_set_app_monitoring_enabled
          - 'jira_server_is_ipd_monitoring_enabled': Call jira_server_is_ipd_monitoring_enabled
          - 'jira_server_set_app_monitoring_enabled_1': Call jira_server_set_app_monitoring_enabled_1
          - 'jira_server_are_metrics_exposed': Call jira_server_are_metrics_exposed
          - 'jira_server_get_available_metrics': Call jira_server_get_available_metrics
          - 'jira_server_start': Call jira_server_start
          - 'jira_server_stop': Call jira_server_stop
          - 'jira_server_get_preference': Call jira_server_get_preference
          - 'jira_server_set_preference': Call jira_server_set_preference
          - 'jira_server_remove_preference': Call jira_server_remove_preference
          - 'jira_server_change_my_password': Call jira_server_change_my_password
          - 'jira_server_get_notification_schemes': Call jira_server_get_notification_schemes
          - 'jira_server_get_notification_scheme': Call jira_server_get_notification_scheme
          - 'jira_server_get_password_policy': Call jira_server_get_password_policy
          - 'jira_server_get_scheme_attribute': Call jira_server_get_scheme_attribute
          - 'jira_server_set_scheme_attribute': Call jira_server_set_scheme_attribute
          - 'jira_server_get_priorities': Call jira_server_get_priorities
          - 'jira_server_get_priorities_1': Call jira_server_get_priorities_1
          - 'jira_server_create_avatar_from_temporary_1': Call jira_server_create_avatar_from_temporary_1
          - 'jira_server_store_temporary_avatar_using_multi_part_1': Call jira_server_store_temporary_avatar_using_multi_part_1
          - 'jira_server_delete_avatar': Call jira_server_delete_avatar
          - 'jira_server_get_all_avatars': Call jira_server_get_all_avatars
          - 'jira_server_get_properties_keys_3': Call jira_server_get_properties_keys_3
          - 'jira_server_get_property_5': Call jira_server_get_property_5
          - 'jira_server_set_property_4': Call jira_server_set_property_4
          - 'jira_server_delete_property_5': Call jira_server_delete_property_5
          - 'jira_server_set_actors': Call jira_server_set_actors
          - 'jira_server_delete_actor': Call jira_server_delete_actor
          - 'jira_server_get_all_statuses': Call jira_server_get_all_statuses
          - 'jira_server_get_issue_security_scheme_1': Call jira_server_get_issue_security_scheme_1
          - 'jira_server_get_notification_scheme_1': Call jira_server_get_notification_scheme_1
          - 'jira_server_process_requests': Call jira_server_process_requests
          - 'jira_server_get_progress_bulk': Call jira_server_get_progress_bulk
          - 'jira_server_get_progress': Call jira_server_get_progress
          - 'jira_server_update_show_when_empty_indicator': Call jira_server_update_show_when_empty_indicator
          - 'jira_server_get_error': Call jira_server_get_error
          - 'jira_server_get_max_aggregation_buckets': Call jira_server_get_max_aggregation_buckets
          - 'jira_server_get_max_result_window': Call jira_server_get_max_result_window
          - 'jira_server_get_issuesecuritylevel': Call jira_server_get_issuesecuritylevel
          - 'jira_server_set_base_url': Call jira_server_set_base_url
          - 'jira_server_get_issue_navigator_default_columns': Call jira_server_get_issue_navigator_default_columns
          - 'jira_server_set_issue_navigator_default_columns_form': Call jira_server_set_issue_navigator_default_columns_form
          - 'jira_server_get_statuses': Call jira_server_get_statuses
          - 'jira_server_get_paginated_statuses': Call jira_server_get_paginated_statuses
          - 'jira_server_get_status': Call jira_server_get_status
          - 'jira_server_get_status_categories': Call jira_server_get_status_categories
          - 'jira_server_get_status_category': Call jira_server_get_status_category
          - 'jira_server_get_all_terminology_entries': Call jira_server_get_all_terminology_entries
          - 'jira_server_set_terminology_entries': Call jira_server_set_terminology_entries
          - 'jira_server_get_terminology_entry': Call jira_server_get_terminology_entry
          - 'jira_server_get_avatars': Call jira_server_get_avatars
          - 'jira_server_create_avatar_from_temporary_2': Call jira_server_create_avatar_from_temporary_2
          - 'jira_server_delete_avatar_1': Call jira_server_delete_avatar_1
          - 'jira_server_store_temporary_avatar_using_multi_part_2': Call jira_server_store_temporary_avatar_using_multi_part_2
          - 'jira_server_get_a11y_personal_settings': Call jira_server_get_a11y_personal_settings
          - 'jira_server_get_progress_1': Call jira_server_get_progress_1
          - 'jira_server_unlock_anonymization': Call jira_server_unlock_anonymization
          - 'jira_server_create_avatar_from_temporary_3': Call jira_server_create_avatar_from_temporary_3
          - 'jira_server_store_temporary_avatar_using_multi_part_3': Call jira_server_store_temporary_avatar_using_multi_part_3
          - 'jira_server_delete_avatar_2': Call jira_server_delete_avatar_2
          - 'jira_server_get_all_avatars_1': Call jira_server_get_all_avatars_1
          - 'jira_server_default_columns': Call jira_server_default_columns
          - 'jira_server_set_columns_url_encoded': Call jira_server_set_columns_url_encoded
          - 'jira_server_reset_columns': Call jira_server_reset_columns
          - 'jira_server_get_properties_keys_4': Call jira_server_get_properties_keys_4
          - 'jira_server_get_property_6': Call jira_server_get_property_6
          - 'jira_server_set_property_5': Call jira_server_set_property_5
          - 'jira_server_delete_property_6': Call jira_server_delete_property_6
          - 'jira_server_delete_session': Call jira_server_delete_session
          - 'jira_server_get_paginated_versions': Call jira_server_get_paginated_versions
          - 'jira_server_create_version': Call jira_server_create_version
          - 'jira_server_get_remote_version_links': Call jira_server_get_remote_version_links
          - 'jira_server_get_version': Call jira_server_get_version
          - 'jira_server_update_version': Call jira_server_update_version
          - 'jira_server_merge': Call jira_server_merge
          - 'jira_server_move_version': Call jira_server_move_version
          - 'jira_server_get_version_related_issues': Call jira_server_get_version_related_issues
          - 'jira_server_delete_1': Call jira_server_delete_1
          - 'jira_server_get_version_unresolved_issues': Call jira_server_get_version_unresolved_issues
          - 'jira_server_get_remote_version_links_by_version_id': Call jira_server_get_remote_version_links_by_version_id
          - 'jira_server_create_or_update_remote_version_link': Call jira_server_create_or_update_remote_version_link
          - 'jira_server_delete_remote_version_links_by_version_id': Call jira_server_delete_remote_version_links_by_version_id
          - 'jira_server_get_remote_version_link': Call jira_server_get_remote_version_link
          - 'jira_server_create_or_update_remote_version_link_1': Call jira_server_create_or_update_remote_version_link_1
          - 'jira_server_delete_remote_version_link': Call jira_server_delete_remote_version_link
          - 'jira_server_create_scheme': Call jira_server_create_scheme
          - 'jira_server_get_by_id': Call jira_server_get_by_id
          - 'jira_server_update': Call jira_server_update
          - 'jira_server_delete_scheme': Call jira_server_delete_scheme
          - 'jira_server_create_draft_for_parent': Call jira_server_create_draft_for_parent
          - 'jira_server_get_default': Call jira_server_get_default
          - 'jira_server_update_default': Call jira_server_update_default
          - 'jira_server_delete_default': Call jira_server_delete_default
          - 'jira_server_get_draft_by_id': Call jira_server_get_draft_by_id
          - 'jira_server_update_draft': Call jira_server_update_draft
          - 'jira_server_delete_draft_by_id': Call jira_server_delete_draft_by_id
          - 'jira_server_get_draft_default': Call jira_server_get_draft_default
          - 'jira_server_update_draft_default': Call jira_server_update_draft_default
          - 'jira_server_delete_draft_default': Call jira_server_delete_draft_default
          - 'jira_server_release': Call jira_server_release
        """
        kwargs: dict[str, Any]
        if action == "jira_server_move_issues_to_backlog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_move_issues_to_backlog(**kwargs)
        if action == "jira_server_get_issues_for_backlog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issues_for_backlog(**kwargs)
        if action == "jira_server_get_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_configuration(**kwargs)
        if action == "jira_server_get_properties_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_properties_keys(**kwargs)
        if action == "jira_server_get_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_property(**kwargs)
        if action == "jira_server_set_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_property(**kwargs)
        if action == "jira_server_delete_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_property(**kwargs)
        if action == "jira_server_get_refined_velocity":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_refined_velocity(**kwargs)
        if action == "jira_server_set_refined_velocity":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_refined_velocity(**kwargs)
        if action == "jira_server_get_all_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_versions(**kwargs)
        if action == "jira_server_rank_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_rank_issues(**kwargs)
        if action == "jira_server_get_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue(**kwargs)
        if action == "jira_server_get_properties_keys_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_properties_keys_1(**kwargs)
        if action == "jira_server_get_property_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_property_1(**kwargs)
        if action == "jira_server_set_property_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_property_1(**kwargs)
        if action == "jira_server_delete_property_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_property_1(**kwargs)
        if action == "jira_server_get_application_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_application_property(**kwargs)
        if action == "jira_server_get_advanced_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_advanced_settings(**kwargs)
        if action == "jira_server_get_all":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all(**kwargs)
        if action == "jira_server_put_bulk":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_put_bulk(**kwargs)
        if action == "jira_server_get_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_4(**kwargs)
        if action == "jira_server_put_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_put_2(**kwargs)
        if action == "jira_server_expand_for_humans":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_expand_for_humans(**kwargs)
        if action == "jira_server_expand_for_machines":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_expand_for_machines(**kwargs)
        if action == "jira_server_delete_node":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_node(**kwargs)
        if action == "jira_server_change_node_state_to_offline":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_change_node_state_to_offline(**kwargs)
        if action == "jira_server_get_all_nodes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_nodes(**kwargs)
        if action == "jira_server_acknowledge_errors":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_acknowledge_errors(**kwargs)
        if action == "jira_server_get_state":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_state(**kwargs)
        if action == "jira_server_get_properties_keys_1_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_properties_keys_1_2(**kwargs)
        if action == "jira_server_get_comment_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_comment_property(**kwargs)
        if action == "jira_server_set_property_1_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_property_1_2(**kwargs)
        if action == "jira_server_delete_property_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_property_2(**kwargs)
        if action == "jira_server_create_component":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_component(**kwargs)
        if action == "jira_server_get_paginated_components":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_paginated_components(**kwargs)
        if action == "jira_server_get_component":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_component(**kwargs)
        if action == "jira_server_update_component":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_component(**kwargs)
        if action == "jira_server_delete":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete(**kwargs)
        if action == "jira_server_get_component_related_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_component_related_issues(**kwargs)
        if action == "jira_server_get_configuration_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_configuration_1(**kwargs)
        if action == "jira_server_list":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_list(**kwargs)
        if action == "jira_server_get_dashboard_item_properties_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_dashboard_item_properties_keys(**kwargs)
        if action == "jira_server_get_property_1_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_property_1_2(**kwargs)
        if action == "jira_server_set_dashboard_item_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_dashboard_item_property(**kwargs)
        if action == "jira_server_delete_property_1_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_property_1_2(**kwargs)
        if action == "jira_server_download_email_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_download_email_templates(**kwargs)
        if action == "jira_server_upload_email_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_upload_email_templates(**kwargs)
        if action == "jira_server_apply_email_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_apply_email_templates(**kwargs)
        if action == "jira_server_revert_email_templates_to_default":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_revert_email_templates_to_default(**kwargs)
        if action == "jira_server_get_email_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_email_types(**kwargs)
        if action == "jira_server_get_default_share_scope":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_default_share_scope(**kwargs)
        if action == "jira_server_set_default_share_scope":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_default_share_scope(**kwargs)
        if action == "jira_server_default_columns_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_default_columns_1(**kwargs)
        if action == "jira_server_set_columns_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_columns_1(**kwargs)
        if action == "jira_server_reset_columns_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_reset_columns_1(**kwargs)
        if action == "jira_server_create_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_issue(**kwargs)
        if action == "jira_server_archive_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_archive_issues(**kwargs)
        if action == "jira_server_create_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_issues(**kwargs)
        if action == "jira_server_get_issue_picker_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_picker_resource(**kwargs)
        if action == "jira_server_get_issue_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_2(**kwargs)
        if action == "jira_server_edit_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_edit_issue(**kwargs)
        if action == "jira_server_delete_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_issue(**kwargs)
        if action == "jira_server_archive_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_archive_issue(**kwargs)
        if action == "jira_server_assign":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_assign(**kwargs)
        if action == "jira_server_get_edit_issue_meta":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_edit_issue_meta(**kwargs)
        if action == "jira_server_notify":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_notify(**kwargs)
        if action == "jira_server_get_issue_properties_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_properties_keys(**kwargs)
        if action == "jira_server_get_property_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_property_3(**kwargs)
        if action == "jira_server_set_issue_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_issue_property(**kwargs)
        if action == "jira_server_delete_property_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_property_3(**kwargs)
        if action == "jira_server_restore_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_restore_issue(**kwargs)
        if action == "jira_server_link_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_link_issues(**kwargs)
        if action == "jira_server_reset_order":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_reset_order(**kwargs)
        if action == "jira_server_get_issue_security_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_security_schemes(**kwargs)
        if action == "jira_server_get_issue_security_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_security_scheme(**kwargs)
        if action == "jira_server_get_issue_all_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_all_types(**kwargs)
        if action == "jira_server_create_avatar_from_temporary":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_avatar_from_temporary(**kwargs)
        if action == "jira_server_store_temporary_avatar_using_multi_part":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_store_temporary_avatar_using_multi_part(**kwargs)
        if action == "jira_server_get_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_property_keys(**kwargs)
        if action == "jira_server_get_property_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_property_4(**kwargs)
        if action == "jira_server_set_property_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_property_3(**kwargs)
        if action == "jira_server_delete_property_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_property_4(**kwargs)
        if action == "jira_server_get_auto_complete":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_auto_complete(**kwargs)
        if action == "jira_server_validate":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_validate(**kwargs)
        if action == "jira_server_is_app_monitoring_enabled":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_is_app_monitoring_enabled(**kwargs)
        if action == "jira_server_set_app_monitoring_enabled":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_app_monitoring_enabled(**kwargs)
        if action == "jira_server_is_ipd_monitoring_enabled":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_is_ipd_monitoring_enabled(**kwargs)
        if action == "jira_server_set_app_monitoring_enabled_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_app_monitoring_enabled_1(**kwargs)
        if action == "jira_server_are_metrics_exposed":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_are_metrics_exposed(**kwargs)
        if action == "jira_server_get_available_metrics":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_available_metrics(**kwargs)
        if action == "jira_server_start":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_start(**kwargs)
        if action == "jira_server_stop":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_stop(**kwargs)
        if action == "jira_server_get_preference":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_preference(**kwargs)
        if action == "jira_server_set_preference":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_preference(**kwargs)
        if action == "jira_server_remove_preference":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_preference(**kwargs)
        if action == "jira_server_change_my_password":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_change_my_password(**kwargs)
        if action == "jira_server_get_notification_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_notification_schemes(**kwargs)
        if action == "jira_server_get_notification_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_notification_scheme(**kwargs)
        if action == "jira_server_get_password_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_password_policy(**kwargs)
        if action == "jira_server_get_scheme_attribute":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_scheme_attribute(**kwargs)
        if action == "jira_server_set_scheme_attribute":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_scheme_attribute(**kwargs)
        if action == "jira_server_get_priorities":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_priorities(**kwargs)
        if action == "jira_server_get_priorities_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_priorities_1(**kwargs)
        if action == "jira_server_create_avatar_from_temporary_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_avatar_from_temporary_1(**kwargs)
        if action == "jira_server_store_temporary_avatar_using_multi_part_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_store_temporary_avatar_using_multi_part_1(
                **kwargs
            )
        if action == "jira_server_delete_avatar":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_avatar(**kwargs)
        if action == "jira_server_get_all_avatars":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_avatars(**kwargs)
        if action == "jira_server_get_properties_keys_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_properties_keys_3(**kwargs)
        if action == "jira_server_get_property_5":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_property_5(**kwargs)
        if action == "jira_server_set_property_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_property_4(**kwargs)
        if action == "jira_server_delete_property_5":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_property_5(**kwargs)
        if action == "jira_server_set_actors":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_actors(**kwargs)
        if action == "jira_server_delete_actor":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_actor(**kwargs)
        if action == "jira_server_get_all_statuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_statuses(**kwargs)
        if action == "jira_server_get_issue_security_scheme_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_security_scheme_1(**kwargs)
        if action == "jira_server_get_notification_scheme_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_notification_scheme_1(**kwargs)
        if action == "jira_server_process_requests":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_process_requests(**kwargs)
        if action == "jira_server_get_progress_bulk":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_progress_bulk(**kwargs)
        if action == "jira_server_get_progress":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_progress(**kwargs)
        if action == "jira_server_update_show_when_empty_indicator":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_show_when_empty_indicator(**kwargs)
        if action == "jira_server_get_error":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_error(**kwargs)
        if action == "jira_server_get_max_aggregation_buckets":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_max_aggregation_buckets(**kwargs)
        if action == "jira_server_get_max_result_window":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_max_result_window(**kwargs)
        if action == "jira_server_get_issuesecuritylevel":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issuesecuritylevel(**kwargs)
        if action == "jira_server_set_base_url":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_base_url(**kwargs)
        if action == "jira_server_get_issue_navigator_default_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_navigator_default_columns(**kwargs)
        if action == "jira_server_set_issue_navigator_default_columns_form":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_issue_navigator_default_columns_form(**kwargs)
        if action == "jira_server_get_statuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_statuses(**kwargs)
        if action == "jira_server_get_paginated_statuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_paginated_statuses(**kwargs)
        if action == "jira_server_get_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_status(**kwargs)
        if action == "jira_server_get_status_categories":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_status_categories(**kwargs)
        if action == "jira_server_get_status_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_status_category(**kwargs)
        if action == "jira_server_get_all_terminology_entries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_terminology_entries(**kwargs)
        if action == "jira_server_set_terminology_entries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_terminology_entries(**kwargs)
        if action == "jira_server_get_terminology_entry":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_terminology_entry(**kwargs)
        if action == "jira_server_get_avatars":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_avatars(**kwargs)
        if action == "jira_server_create_avatar_from_temporary_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_avatar_from_temporary_2(**kwargs)
        if action == "jira_server_delete_avatar_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_avatar_1(**kwargs)
        if action == "jira_server_store_temporary_avatar_using_multi_part_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_store_temporary_avatar_using_multi_part_2(
                **kwargs
            )
        if action == "jira_server_get_a11y_personal_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_a11y_personal_settings(**kwargs)
        if action == "jira_server_get_progress_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_progress_1(**kwargs)
        if action == "jira_server_unlock_anonymization":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_unlock_anonymization(**kwargs)
        if action == "jira_server_create_avatar_from_temporary_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_avatar_from_temporary_3(**kwargs)
        if action == "jira_server_store_temporary_avatar_using_multi_part_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_store_temporary_avatar_using_multi_part_3(
                **kwargs
            )
        if action == "jira_server_delete_avatar_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_avatar_2(**kwargs)
        if action == "jira_server_get_all_avatars_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_avatars_1(**kwargs)
        if action == "jira_server_default_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_default_columns(**kwargs)
        if action == "jira_server_set_columns_url_encoded":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_columns_url_encoded(**kwargs)
        if action == "jira_server_reset_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_reset_columns(**kwargs)
        if action == "jira_server_get_properties_keys_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_properties_keys_4(**kwargs)
        if action == "jira_server_get_property_6":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_property_6(**kwargs)
        if action == "jira_server_set_property_5":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_property_5(**kwargs)
        if action == "jira_server_delete_property_6":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_property_6(**kwargs)
        if action == "jira_server_delete_session":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_session(**kwargs)
        if action == "jira_server_get_paginated_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_paginated_versions(**kwargs)
        if action == "jira_server_create_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_version(**kwargs)
        if action == "jira_server_get_remote_version_links":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_remote_version_links(**kwargs)
        if action == "jira_server_get_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_version(**kwargs)
        if action == "jira_server_update_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_version(**kwargs)
        if action == "jira_server_merge":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_merge(**kwargs)
        if action == "jira_server_move_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_move_version(**kwargs)
        if action == "jira_server_get_version_related_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_version_related_issues(**kwargs)
        if action == "jira_server_delete_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_1(**kwargs)
        if action == "jira_server_get_version_unresolved_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_version_unresolved_issues(**kwargs)
        if action == "jira_server_get_remote_version_links_by_version_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_remote_version_links_by_version_id(**kwargs)
        if action == "jira_server_create_or_update_remote_version_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_or_update_remote_version_link(**kwargs)
        if action == "jira_server_delete_remote_version_links_by_version_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_remote_version_links_by_version_id(
                **kwargs
            )
        if action == "jira_server_get_remote_version_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_remote_version_link(**kwargs)
        if action == "jira_server_create_or_update_remote_version_link_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_or_update_remote_version_link_1(**kwargs)
        if action == "jira_server_delete_remote_version_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_remote_version_link(**kwargs)
        if action == "jira_server_create_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_scheme(**kwargs)
        if action == "jira_server_get_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_by_id(**kwargs)
        if action == "jira_server_update":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update(**kwargs)
        if action == "jira_server_delete_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_scheme(**kwargs)
        if action == "jira_server_create_draft_for_parent":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_draft_for_parent(**kwargs)
        if action == "jira_server_get_default":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_default(**kwargs)
        if action == "jira_server_update_default":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_default(**kwargs)
        if action == "jira_server_delete_default":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_default(**kwargs)
        if action == "jira_server_get_draft_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_draft_by_id(**kwargs)
        if action == "jira_server_update_draft":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_draft(**kwargs)
        if action == "jira_server_delete_draft_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_draft_by_id(**kwargs)
        if action == "jira_server_get_draft_default":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_draft_default(**kwargs)
        if action == "jira_server_update_draft_default":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_draft_default(**kwargs)
        if action == "jira_server_delete_draft_default":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_draft_default(**kwargs)
        if action == "jira_server_release":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_release(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_move_issues_to_backlog', 'jira_server_get_issues_for_backlog', 'jira_server_get_configuration', 'jira_server_get_properties_keys', 'jira_server_get_property', 'jira_server_set_property', 'jira_server_delete_property', 'jira_server_get_refined_velocity', 'jira_server_set_refined_velocity', 'jira_server_get_all_versions', 'jira_server_rank_issues', 'jira_server_get_issue', 'jira_server_get_properties_keys_1', 'jira_server_get_property_1', 'jira_server_set_property_1', 'jira_server_delete_property_1', 'jira_server_get_application_property', 'jira_server_get_advanced_settings', 'jira_server_get_all', 'jira_server_put_bulk', 'jira_server_get_4', 'jira_server_put_2', 'jira_server_expand_for_humans', 'jira_server_expand_for_machines', 'jira_server_delete_node', 'jira_server_change_node_state_to_offline', 'jira_server_get_all_nodes', 'jira_server_acknowledge_errors', 'jira_server_get_state', 'jira_server_get_properties_keys_1_2', 'jira_server_get_comment_property', 'jira_server_set_property_1_2', 'jira_server_delete_property_2', 'jira_server_create_component', 'jira_server_get_paginated_components', 'jira_server_get_component', 'jira_server_update_component', 'jira_server_delete', 'jira_server_get_component_related_issues', 'jira_server_get_configuration_1', 'jira_server_list', 'jira_server_get_dashboard_item_properties_keys', 'jira_server_get_property_1_2', 'jira_server_set_dashboard_item_property', 'jira_server_delete_property_1_2', 'jira_server_download_email_templates', 'jira_server_upload_email_templates', 'jira_server_apply_email_templates', 'jira_server_revert_email_templates_to_default', 'jira_server_get_email_types', 'jira_server_get_default_share_scope', 'jira_server_set_default_share_scope', 'jira_server_default_columns_1', 'jira_server_set_columns_1', 'jira_server_reset_columns_1', 'jira_server_create_issue', 'jira_server_archive_issues', 'jira_server_create_issues', 'jira_server_get_issue_picker_resource', 'jira_server_get_issue_2', 'jira_server_edit_issue', 'jira_server_delete_issue', 'jira_server_archive_issue', 'jira_server_assign', 'jira_server_get_edit_issue_meta', 'jira_server_notify', 'jira_server_get_issue_properties_keys', 'jira_server_get_property_3', 'jira_server_set_issue_property', 'jira_server_delete_property_3', 'jira_server_restore_issue', 'jira_server_link_issues', 'jira_server_reset_order', 'jira_server_get_issue_security_schemes', 'jira_server_get_issue_security_scheme', 'jira_server_get_issue_all_types', 'jira_server_create_avatar_from_temporary', 'jira_server_store_temporary_avatar_using_multi_part', 'jira_server_get_property_keys', 'jira_server_get_property_4', 'jira_server_set_property_3', 'jira_server_delete_property_4', 'jira_server_get_auto_complete', 'jira_server_validate', 'jira_server_is_app_monitoring_enabled', 'jira_server_set_app_monitoring_enabled', 'jira_server_is_ipd_monitoring_enabled', 'jira_server_set_app_monitoring_enabled_1', 'jira_server_are_metrics_exposed', 'jira_server_get_available_metrics', 'jira_server_start', 'jira_server_stop', 'jira_server_get_preference', 'jira_server_set_preference', 'jira_server_remove_preference', 'jira_server_change_my_password', 'jira_server_get_notification_schemes', 'jira_server_get_notification_scheme', 'jira_server_get_password_policy', 'jira_server_get_scheme_attribute', 'jira_server_set_scheme_attribute', 'jira_server_get_priorities', 'jira_server_get_priorities_1', 'jira_server_create_avatar_from_temporary_1', 'jira_server_store_temporary_avatar_using_multi_part_1', 'jira_server_delete_avatar', 'jira_server_get_all_avatars', 'jira_server_get_properties_keys_3', 'jira_server_get_property_5', 'jira_server_set_property_4', 'jira_server_delete_property_5', 'jira_server_set_actors', 'jira_server_delete_actor', 'jira_server_get_all_statuses', 'jira_server_get_issue_security_scheme_1', 'jira_server_get_notification_scheme_1', 'jira_server_process_requests', 'jira_server_get_progress_bulk', 'jira_server_get_progress', 'jira_server_update_show_when_empty_indicator', 'jira_server_get_error', 'jira_server_get_max_aggregation_buckets', 'jira_server_get_max_result_window', 'jira_server_get_issuesecuritylevel', 'jira_server_set_base_url', 'jira_server_get_issue_navigator_default_columns', 'jira_server_set_issue_navigator_default_columns_form', 'jira_server_get_statuses', 'jira_server_get_paginated_statuses', 'jira_server_get_status', 'jira_server_get_status_categories', 'jira_server_get_status_category', 'jira_server_get_all_terminology_entries', 'jira_server_set_terminology_entries', 'jira_server_get_terminology_entry', 'jira_server_get_avatars', 'jira_server_create_avatar_from_temporary_2', 'jira_server_delete_avatar_1', 'jira_server_store_temporary_avatar_using_multi_part_2', 'jira_server_get_a11y_personal_settings', 'jira_server_get_progress_1', 'jira_server_unlock_anonymization', 'jira_server_create_avatar_from_temporary_3', 'jira_server_store_temporary_avatar_using_multi_part_3', 'jira_server_delete_avatar_2', 'jira_server_get_all_avatars_1', 'jira_server_default_columns', 'jira_server_set_columns_url_encoded', 'jira_server_reset_columns', 'jira_server_get_properties_keys_4', 'jira_server_get_property_6', 'jira_server_set_property_5', 'jira_server_delete_property_6', 'jira_server_delete_session', 'jira_server_get_paginated_versions', 'jira_server_create_version', 'jira_server_get_remote_version_links', 'jira_server_get_version', 'jira_server_update_version', 'jira_server_merge', 'jira_server_move_version', 'jira_server_get_version_related_issues', 'jira_server_delete_1', 'jira_server_get_version_unresolved_issues', 'jira_server_get_remote_version_links_by_version_id', 'jira_server_create_or_update_remote_version_link', 'jira_server_delete_remote_version_links_by_version_id', 'jira_server_get_remote_version_link', 'jira_server_create_or_update_remote_version_link_1', 'jira_server_delete_remote_version_link', 'jira_server_create_scheme', 'jira_server_get_by_id', 'jira_server_update', 'jira_server_delete_scheme', 'jira_server_create_draft_for_parent', 'jira_server_get_default', 'jira_server_update_default', 'jira_server_delete_default', 'jira_server_get_draft_by_id', 'jira_server_update_draft', 'jira_server_delete_draft_by_id', 'jira_server_get_draft_default', 'jira_server_update_draft_default', 'jira_server_delete_draft_default', 'jira_server_release"
        )


def register_jira_server_agile_board_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-agile-board"})
    async def atlassian_jira_server_agile_board(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_all_boards', 'jira_server_create_board', 'jira_server_get_board', 'jira_server_delete_board', 'jira_server_get_issues_for_board', 'jira_server_get_issue_estimation_for_board', 'jira_server_estimate_issue_for_board', 'jira_server_get_dashboard'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server agile board operations.

        Actions:
          - 'jira_server_get_all_boards': Call jira_server_get_all_boards
          - 'jira_server_create_board': Call jira_server_create_board
          - 'jira_server_get_board': Call jira_server_get_board
          - 'jira_server_delete_board': Call jira_server_delete_board
          - 'jira_server_get_issues_for_board': Call jira_server_get_issues_for_board
          - 'jira_server_get_issue_estimation_for_board': Call jira_server_get_issue_estimation_for_board
          - 'jira_server_estimate_issue_for_board': Call jira_server_estimate_issue_for_board
          - 'jira_server_get_dashboard': Call jira_server_get_dashboard
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_all_boards":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_boards(**kwargs)
        if action == "jira_server_create_board":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_board(**kwargs)
        if action == "jira_server_get_board":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_board(**kwargs)
        if action == "jira_server_delete_board":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_board(**kwargs)
        if action == "jira_server_get_issues_for_board":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issues_for_board(**kwargs)
        if action == "jira_server_get_issue_estimation_for_board":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_estimation_for_board(**kwargs)
        if action == "jira_server_estimate_issue_for_board":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_estimate_issue_for_board(**kwargs)
        if action == "jira_server_get_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_dashboard(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_all_boards', 'jira_server_create_board', 'jira_server_get_board', 'jira_server_delete_board', 'jira_server_get_issues_for_board', 'jira_server_get_issue_estimation_for_board', 'jira_server_estimate_issue_for_board', 'jira_server_get_dashboard"
        )


def register_jira_server_agile_epic_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-agile-epic"})
    async def atlassian_jira_server_agile_epic(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_epics', 'jira_server_get_issues_without_epic', 'jira_server_get_issues_for_epic', 'jira_server_get_issues_without_epic_1', 'jira_server_remove_issues_from_epic', 'jira_server_get_epic', 'jira_server_partially_update_epic', 'jira_server_get_issues_for_epic_1', 'jira_server_move_issues_to_epic', 'jira_server_rank_epics'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server agile epic operations.

        Actions:
          - 'jira_server_get_epics': Call jira_server_get_epics
          - 'jira_server_get_issues_without_epic': Call jira_server_get_issues_without_epic
          - 'jira_server_get_issues_for_epic': Call jira_server_get_issues_for_epic
          - 'jira_server_get_issues_without_epic_1': Call jira_server_get_issues_without_epic_1
          - 'jira_server_remove_issues_from_epic': Call jira_server_remove_issues_from_epic
          - 'jira_server_get_epic': Call jira_server_get_epic
          - 'jira_server_partially_update_epic': Call jira_server_partially_update_epic
          - 'jira_server_get_issues_for_epic_1': Call jira_server_get_issues_for_epic_1
          - 'jira_server_move_issues_to_epic': Call jira_server_move_issues_to_epic
          - 'jira_server_rank_epics': Call jira_server_rank_epics
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_epics":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_epics(**kwargs)
        if action == "jira_server_get_issues_without_epic":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issues_without_epic(**kwargs)
        if action == "jira_server_get_issues_for_epic":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issues_for_epic(**kwargs)
        if action == "jira_server_get_issues_without_epic_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issues_without_epic_1(**kwargs)
        if action == "jira_server_remove_issues_from_epic":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_issues_from_epic(**kwargs)
        if action == "jira_server_get_epic":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_epic(**kwargs)
        if action == "jira_server_partially_update_epic":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_partially_update_epic(**kwargs)
        if action == "jira_server_get_issues_for_epic_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issues_for_epic_1(**kwargs)
        if action == "jira_server_move_issues_to_epic":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_move_issues_to_epic(**kwargs)
        if action == "jira_server_rank_epics":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_rank_epics(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_epics', 'jira_server_get_issues_without_epic', 'jira_server_get_issues_for_epic', 'jira_server_get_issues_without_epic_1', 'jira_server_remove_issues_from_epic', 'jira_server_get_epic', 'jira_server_partially_update_epic', 'jira_server_get_issues_for_epic_1', 'jira_server_move_issues_to_epic', 'jira_server_rank_epics"
        )


def register_jira_server_project_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-project"})
    async def atlassian_jira_server_project(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_projects', 'jira_server_get_associated_projects', 'jira_server_set_project_associations_for_scheme', 'jira_server_add_project_associations_to_scheme', 'jira_server_remove_all_project_associations', 'jira_server_remove_project_association', 'jira_server_get_all_projects', 'jira_server_create_project', 'jira_server_get_all_project_types', 'jira_server_get_project_type_by_key', 'jira_server_get_accessible_project_type_by_key', 'jira_server_get_project', 'jira_server_update_project', 'jira_server_delete_project', 'jira_server_archive_project', 'jira_server_restore_project', 'jira_server_update_project_type', 'jira_server_get_project_versions_paginated', 'jira_server_get_project_versions', 'jira_server_get_security_levels_for_project', 'jira_server_get_workflow_scheme_for_project', 'jira_server_get_all_project_categories', 'jira_server_search_for_projects', 'jira_server_get_project_1'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server project operations.

        Actions:
          - 'jira_server_get_projects': Call jira_server_get_projects
          - 'jira_server_get_associated_projects': Call jira_server_get_associated_projects
          - 'jira_server_set_project_associations_for_scheme': Call jira_server_set_project_associations_for_scheme
          - 'jira_server_add_project_associations_to_scheme': Call jira_server_add_project_associations_to_scheme
          - 'jira_server_remove_all_project_associations': Call jira_server_remove_all_project_associations
          - 'jira_server_remove_project_association': Call jira_server_remove_project_association
          - 'jira_server_get_all_projects': Call jira_server_get_all_projects
          - 'jira_server_create_project': Call jira_server_create_project
          - 'jira_server_get_all_project_types': Call jira_server_get_all_project_types
          - 'jira_server_get_project_type_by_key': Call jira_server_get_project_type_by_key
          - 'jira_server_get_accessible_project_type_by_key': Call jira_server_get_accessible_project_type_by_key
          - 'jira_server_get_project': Call jira_server_get_project
          - 'jira_server_update_project': Call jira_server_update_project
          - 'jira_server_delete_project': Call jira_server_delete_project
          - 'jira_server_archive_project': Call jira_server_archive_project
          - 'jira_server_restore_project': Call jira_server_restore_project
          - 'jira_server_update_project_type': Call jira_server_update_project_type
          - 'jira_server_get_project_versions_paginated': Call jira_server_get_project_versions_paginated
          - 'jira_server_get_project_versions': Call jira_server_get_project_versions
          - 'jira_server_get_security_levels_for_project': Call jira_server_get_security_levels_for_project
          - 'jira_server_get_workflow_scheme_for_project': Call jira_server_get_workflow_scheme_for_project
          - 'jira_server_get_all_project_categories': Call jira_server_get_all_project_categories
          - 'jira_server_search_for_projects': Call jira_server_search_for_projects
          - 'jira_server_get_project_1': Call jira_server_get_project_1
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_projects(**kwargs)
        if action == "jira_server_get_associated_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_associated_projects(**kwargs)
        if action == "jira_server_set_project_associations_for_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_project_associations_for_scheme(**kwargs)
        if action == "jira_server_add_project_associations_to_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_project_associations_to_scheme(**kwargs)
        if action == "jira_server_remove_all_project_associations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_all_project_associations(**kwargs)
        if action == "jira_server_remove_project_association":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_project_association(**kwargs)
        if action == "jira_server_get_all_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_projects(**kwargs)
        if action == "jira_server_create_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_project(**kwargs)
        if action == "jira_server_get_all_project_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_project_types(**kwargs)
        if action == "jira_server_get_project_type_by_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_type_by_key(**kwargs)
        if action == "jira_server_get_accessible_project_type_by_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_accessible_project_type_by_key(**kwargs)
        if action == "jira_server_get_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project(**kwargs)
        if action == "jira_server_update_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_project(**kwargs)
        if action == "jira_server_delete_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_project(**kwargs)
        if action == "jira_server_archive_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_archive_project(**kwargs)
        if action == "jira_server_restore_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_restore_project(**kwargs)
        if action == "jira_server_update_project_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_project_type(**kwargs)
        if action == "jira_server_get_project_versions_paginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_versions_paginated(**kwargs)
        if action == "jira_server_get_project_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_versions(**kwargs)
        if action == "jira_server_get_security_levels_for_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_security_levels_for_project(**kwargs)
        if action == "jira_server_get_workflow_scheme_for_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_workflow_scheme_for_project(**kwargs)
        if action == "jira_server_get_all_project_categories":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_project_categories(**kwargs)
        if action == "jira_server_search_for_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_search_for_projects(**kwargs)
        if action == "jira_server_get_project_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_1(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_projects', 'jira_server_get_associated_projects', 'jira_server_set_project_associations_for_scheme', 'jira_server_add_project_associations_to_scheme', 'jira_server_remove_all_project_associations', 'jira_server_remove_project_association', 'jira_server_get_all_projects', 'jira_server_create_project', 'jira_server_get_all_project_types', 'jira_server_get_project_type_by_key', 'jira_server_get_accessible_project_type_by_key', 'jira_server_get_project', 'jira_server_update_project', 'jira_server_delete_project', 'jira_server_archive_project', 'jira_server_restore_project', 'jira_server_update_project_type', 'jira_server_get_project_versions_paginated', 'jira_server_get_project_versions', 'jira_server_get_security_levels_for_project', 'jira_server_get_workflow_scheme_for_project', 'jira_server_get_all_project_categories', 'jira_server_search_for_projects', 'jira_server_get_project_1"
        )


def register_jira_server_agile_sprint_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-agile-sprint"})
    async def atlassian_jira_server_agile_sprint(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_all_sprints', 'jira_server_get_issues_for_sprint', 'jira_server_create_sprint', 'jira_server_unmap_sprints', 'jira_server_unmap_all_sprints', 'jira_server_get_sprint', 'jira_server_update_sprint', 'jira_server_partially_update_sprint', 'jira_server_delete_sprint', 'jira_server_get_issues_for_sprint_1', 'jira_server_move_issues_to_sprint', 'jira_server_swap_sprint'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server agile sprint operations.

        Actions:
          - 'jira_server_get_all_sprints': Call jira_server_get_all_sprints
          - 'jira_server_get_issues_for_sprint': Call jira_server_get_issues_for_sprint
          - 'jira_server_create_sprint': Call jira_server_create_sprint
          - 'jira_server_unmap_sprints': Call jira_server_unmap_sprints
          - 'jira_server_unmap_all_sprints': Call jira_server_unmap_all_sprints
          - 'jira_server_get_sprint': Call jira_server_get_sprint
          - 'jira_server_update_sprint': Call jira_server_update_sprint
          - 'jira_server_partially_update_sprint': Call jira_server_partially_update_sprint
          - 'jira_server_delete_sprint': Call jira_server_delete_sprint
          - 'jira_server_get_issues_for_sprint_1': Call jira_server_get_issues_for_sprint_1
          - 'jira_server_move_issues_to_sprint': Call jira_server_move_issues_to_sprint
          - 'jira_server_swap_sprint': Call jira_server_swap_sprint
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_all_sprints":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_sprints(**kwargs)
        if action == "jira_server_get_issues_for_sprint":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issues_for_sprint(**kwargs)
        if action == "jira_server_create_sprint":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_sprint(**kwargs)
        if action == "jira_server_unmap_sprints":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_unmap_sprints(**kwargs)
        if action == "jira_server_unmap_all_sprints":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_unmap_all_sprints(**kwargs)
        if action == "jira_server_get_sprint":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_sprint(**kwargs)
        if action == "jira_server_update_sprint":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_sprint(**kwargs)
        if action == "jira_server_partially_update_sprint":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_partially_update_sprint(**kwargs)
        if action == "jira_server_delete_sprint":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_sprint(**kwargs)
        if action == "jira_server_get_issues_for_sprint_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issues_for_sprint_1(**kwargs)
        if action == "jira_server_move_issues_to_sprint":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_move_issues_to_sprint(**kwargs)
        if action == "jira_server_swap_sprint":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_swap_sprint(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_all_sprints', 'jira_server_get_issues_for_sprint', 'jira_server_create_sprint', 'jira_server_unmap_sprints', 'jira_server_unmap_all_sprints', 'jira_server_get_sprint', 'jira_server_update_sprint', 'jira_server_partially_update_sprint', 'jira_server_delete_sprint', 'jira_server_get_issues_for_sprint_1', 'jira_server_move_issues_to_sprint', 'jira_server_swap_sprint"
        )


def register_jira_server_screen_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-screen"})
    async def atlassian_jira_server_screen(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_set_property_via_restful_table', 'jira_server_get_all_screens', 'jira_server_add_field_to_default_screen', 'jira_server_get_all_tabs', 'jira_server_add_tab', 'jira_server_rename_tab', 'jira_server_delete_tab', 'jira_server_move_tab'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server screen operations.

        Actions:
          - 'jira_server_set_property_via_restful_table': Call jira_server_set_property_via_restful_table
          - 'jira_server_get_all_screens': Call jira_server_get_all_screens
          - 'jira_server_add_field_to_default_screen': Call jira_server_add_field_to_default_screen
          - 'jira_server_get_all_tabs': Call jira_server_get_all_tabs
          - 'jira_server_add_tab': Call jira_server_add_tab
          - 'jira_server_rename_tab': Call jira_server_rename_tab
          - 'jira_server_delete_tab': Call jira_server_delete_tab
          - 'jira_server_move_tab': Call jira_server_move_tab
        """
        kwargs: dict[str, Any]
        if action == "jira_server_set_property_via_restful_table":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_property_via_restful_table(**kwargs)
        if action == "jira_server_get_all_screens":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_screens(**kwargs)
        if action == "jira_server_add_field_to_default_screen":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_field_to_default_screen(**kwargs)
        if action == "jira_server_get_all_tabs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_tabs(**kwargs)
        if action == "jira_server_add_tab":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_tab(**kwargs)
        if action == "jira_server_rename_tab":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_rename_tab(**kwargs)
        if action == "jira_server_delete_tab":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_tab(**kwargs)
        if action == "jira_server_move_tab":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_move_tab(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_set_property_via_restful_table', 'jira_server_get_all_screens', 'jira_server_add_field_to_default_screen', 'jira_server_get_all_tabs', 'jira_server_add_tab', 'jira_server_rename_tab', 'jira_server_delete_tab', 'jira_server_move_tab"
        )


def register_jira_server_issue_attachment_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-attachment"})
    async def atlassian_jira_server_issue_attachment(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_attachment_meta', 'jira_server_get_attachment', 'jira_server_remove_attachment', 'jira_server_add_attachment'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue attachment operations.

        Actions:
          - 'jira_server_get_attachment_meta': Call jira_server_get_attachment_meta
          - 'jira_server_get_attachment': Call jira_server_get_attachment
          - 'jira_server_remove_attachment': Call jira_server_remove_attachment
          - 'jira_server_add_attachment': Call jira_server_add_attachment
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_attachment_meta":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_attachment_meta(**kwargs)
        if action == "jira_server_get_attachment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_attachment(**kwargs)
        if action == "jira_server_remove_attachment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_attachment(**kwargs)
        if action == "jira_server_add_attachment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_attachment(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_attachment_meta', 'jira_server_get_attachment', 'jira_server_remove_attachment', 'jira_server_add_attachment"
        )


def register_jira_server_system_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-system"})
    async def atlassian_jira_server_system(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_all_system_avatars', 'jira_server_get_server_info', 'jira_server_login', 'jira_server_logout'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server system operations.

        Actions:
          - 'jira_server_get_all_system_avatars': Call jira_server_get_all_system_avatars
          - 'jira_server_get_server_info': Call jira_server_get_server_info
          - 'jira_server_login': Call jira_server_login
          - 'jira_server_logout': Call jira_server_logout
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_all_system_avatars":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_system_avatars(**kwargs)
        if action == "jira_server_get_server_info":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_server_info(**kwargs)
        if action == "jira_server_login":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_login(**kwargs)
        if action == "jira_server_logout":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_logout(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_all_system_avatars', 'jira_server_get_server_info', 'jira_server_login', 'jira_server_logout"
        )


def register_jira_server_admin_index_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-admin-index"})
    async def atlassian_jira_server_admin_index(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_request_current_index_from_node', 'jira_server_list_index_snapshot', 'jira_server_create_index_snapshot', 'jira_server_is_index_snapshot_running', 'jira_server_get_index_summary', 'jira_server_get_reindex_info', 'jira_server_reindex', 'jira_server_reindex_issues', 'jira_server_get_reindex_progress'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server admin index operations.

        Actions:
          - 'jira_server_request_current_index_from_node': Call jira_server_request_current_index_from_node
          - 'jira_server_list_index_snapshot': Call jira_server_list_index_snapshot
          - 'jira_server_create_index_snapshot': Call jira_server_create_index_snapshot
          - 'jira_server_is_index_snapshot_running': Call jira_server_is_index_snapshot_running
          - 'jira_server_get_index_summary': Call jira_server_get_index_summary
          - 'jira_server_get_reindex_info': Call jira_server_get_reindex_info
          - 'jira_server_reindex': Call jira_server_reindex
          - 'jira_server_reindex_issues': Call jira_server_reindex_issues
          - 'jira_server_get_reindex_progress': Call jira_server_get_reindex_progress
        """
        kwargs: dict[str, Any]
        if action == "jira_server_request_current_index_from_node":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_request_current_index_from_node(**kwargs)
        if action == "jira_server_list_index_snapshot":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_list_index_snapshot(**kwargs)
        if action == "jira_server_create_index_snapshot":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_index_snapshot(**kwargs)
        if action == "jira_server_is_index_snapshot_running":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_is_index_snapshot_running(**kwargs)
        if action == "jira_server_get_index_summary":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_index_summary(**kwargs)
        if action == "jira_server_get_reindex_info":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_reindex_info(**kwargs)
        if action == "jira_server_reindex":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_reindex(**kwargs)
        if action == "jira_server_reindex_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_reindex_issues(**kwargs)
        if action == "jira_server_get_reindex_progress":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_reindex_progress(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_request_current_index_from_node', 'jira_server_list_index_snapshot', 'jira_server_create_index_snapshot', 'jira_server_is_index_snapshot_running', 'jira_server_get_index_summary', 'jira_server_get_reindex_info', 'jira_server_reindex', 'jira_server_reindex_issues', 'jira_server_get_reindex_progress"
        )


def register_jira_server_admin_upgrade_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-admin-upgrade"})
    async def atlassian_jira_server_admin_upgrade(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_approve_upgrade', 'jira_server_cancel_upgrade', 'jira_server_set_ready_to_upgrade', 'jira_server_get_upgrade_result', 'jira_server_run_upgrades_now'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server admin upgrade operations.

        Actions:
          - 'jira_server_approve_upgrade': Call jira_server_approve_upgrade
          - 'jira_server_cancel_upgrade': Call jira_server_cancel_upgrade
          - 'jira_server_set_ready_to_upgrade': Call jira_server_set_ready_to_upgrade
          - 'jira_server_get_upgrade_result': Call jira_server_get_upgrade_result
          - 'jira_server_run_upgrades_now': Call jira_server_run_upgrades_now
        """
        kwargs: dict[str, Any]
        if action == "jira_server_approve_upgrade":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_approve_upgrade(**kwargs)
        if action == "jira_server_cancel_upgrade":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_cancel_upgrade(**kwargs)
        if action == "jira_server_set_ready_to_upgrade":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_ready_to_upgrade(**kwargs)
        if action == "jira_server_get_upgrade_result":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_upgrade_result(**kwargs)
        if action == "jira_server_run_upgrades_now":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_run_upgrades_now(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_approve_upgrade', 'jira_server_cancel_upgrade', 'jira_server_set_ready_to_upgrade', 'jira_server_get_upgrade_result', 'jira_server_run_upgrades_now"
        )


def register_jira_server_field_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-field"})
    async def atlassian_jira_server_field(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_custom_field_option', 'jira_server_get_custom_fields', 'jira_server_bulk_delete_custom_fields', 'jira_server_get_custom_field_options', 'jira_server_get_fields', 'jira_server_create_custom_field', 'jira_server_get_create_issue_meta_fields', 'jira_server_get_field_auto_complete_for_query_string', 'jira_server_get_fields_to_add', 'jira_server_get_all_fields', 'jira_server_add_field', 'jira_server_remove_field', 'jira_server_move_field'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server field operations.

        Actions:
          - 'jira_server_get_custom_field_option': Call jira_server_get_custom_field_option
          - 'jira_server_get_custom_fields': Call jira_server_get_custom_fields
          - 'jira_server_bulk_delete_custom_fields': Call jira_server_bulk_delete_custom_fields
          - 'jira_server_get_custom_field_options': Call jira_server_get_custom_field_options
          - 'jira_server_get_fields': Call jira_server_get_fields
          - 'jira_server_create_custom_field': Call jira_server_create_custom_field
          - 'jira_server_get_create_issue_meta_fields': Call jira_server_get_create_issue_meta_fields
          - 'jira_server_get_field_auto_complete_for_query_string': Call jira_server_get_field_auto_complete_for_query_string
          - 'jira_server_get_fields_to_add': Call jira_server_get_fields_to_add
          - 'jira_server_get_all_fields': Call jira_server_get_all_fields
          - 'jira_server_add_field': Call jira_server_add_field
          - 'jira_server_remove_field': Call jira_server_remove_field
          - 'jira_server_move_field': Call jira_server_move_field
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_custom_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_custom_field_option(**kwargs)
        if action == "jira_server_get_custom_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_custom_fields(**kwargs)
        if action == "jira_server_bulk_delete_custom_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_bulk_delete_custom_fields(**kwargs)
        if action == "jira_server_get_custom_field_options":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_custom_field_options(**kwargs)
        if action == "jira_server_get_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_fields(**kwargs)
        if action == "jira_server_create_custom_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_custom_field(**kwargs)
        if action == "jira_server_get_create_issue_meta_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_create_issue_meta_fields(**kwargs)
        if action == "jira_server_get_field_auto_complete_for_query_string":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_field_auto_complete_for_query_string(**kwargs)
        if action == "jira_server_get_fields_to_add":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_fields_to_add(**kwargs)
        if action == "jira_server_get_all_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_fields(**kwargs)
        if action == "jira_server_add_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_field(**kwargs)
        if action == "jira_server_remove_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_field(**kwargs)
        if action == "jira_server_move_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_move_field(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_custom_field_option', 'jira_server_get_custom_fields', 'jira_server_bulk_delete_custom_fields', 'jira_server_get_custom_field_options', 'jira_server_get_fields', 'jira_server_create_custom_field', 'jira_server_get_create_issue_meta_fields', 'jira_server_get_field_auto_complete_for_query_string', 'jira_server_get_fields_to_add', 'jira_server_get_all_fields', 'jira_server_add_field', 'jira_server_remove_field', 'jira_server_move_field"
        )


def register_jira_server_filter_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-filter"})
    async def atlassian_jira_server_filter(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_create_filter', 'jira_server_get_favourite_filters', 'jira_server_get_filter', 'jira_server_edit_filter', 'jira_server_delete_filter'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server filter operations.

        Actions:
          - 'jira_server_create_filter': Call jira_server_create_filter
          - 'jira_server_get_favourite_filters': Call jira_server_get_favourite_filters
          - 'jira_server_get_filter': Call jira_server_get_filter
          - 'jira_server_edit_filter': Call jira_server_edit_filter
          - 'jira_server_delete_filter': Call jira_server_delete_filter
        """
        kwargs: dict[str, Any]
        if action == "jira_server_create_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_filter(**kwargs)
        if action == "jira_server_get_favourite_filters":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_favourite_filters(**kwargs)
        if action == "jira_server_get_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_filter(**kwargs)
        if action == "jira_server_edit_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_edit_filter(**kwargs)
        if action == "jira_server_delete_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_filter(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_create_filter', 'jira_server_get_favourite_filters', 'jira_server_get_filter', 'jira_server_edit_filter', 'jira_server_delete_filter"
        )


def register_jira_server_permission_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-permission"})
    async def atlassian_jira_server_permission(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_share_permissions', 'jira_server_add_share_permission', 'jira_server_delete_share_permission', 'jira_server_get_share_permission', 'jira_server_get_permissions', 'jira_server_get_all_permissions', 'jira_server_create_permission_grant'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server permission operations.

        Actions:
          - 'jira_server_get_share_permissions': Call jira_server_get_share_permissions
          - 'jira_server_add_share_permission': Call jira_server_add_share_permission
          - 'jira_server_delete_share_permission': Call jira_server_delete_share_permission
          - 'jira_server_get_share_permission': Call jira_server_get_share_permission
          - 'jira_server_get_permissions': Call jira_server_get_permissions
          - 'jira_server_get_all_permissions': Call jira_server_get_all_permissions
          - 'jira_server_create_permission_grant': Call jira_server_create_permission_grant
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_share_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_share_permissions(**kwargs)
        if action == "jira_server_add_share_permission":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_share_permission(**kwargs)
        if action == "jira_server_delete_share_permission":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_share_permission(**kwargs)
        if action == "jira_server_get_share_permission":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_share_permission(**kwargs)
        if action == "jira_server_get_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_permissions(**kwargs)
        if action == "jira_server_get_all_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_permissions(**kwargs)
        if action == "jira_server_create_permission_grant":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_permission_grant(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_share_permissions', 'jira_server_add_share_permission', 'jira_server_delete_share_permission', 'jira_server_get_share_permission', 'jira_server_get_permissions', 'jira_server_get_all_permissions', 'jira_server_create_permission_grant"
        )


def register_jira_server_group_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-group"})
    async def atlassian_jira_server_group(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_create_group', 'jira_server_remove_group', 'jira_server_find_groups'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server group operations.

        Actions:
          - 'jira_server_create_group': Call jira_server_create_group
          - 'jira_server_remove_group': Call jira_server_remove_group
          - 'jira_server_find_groups': Call jira_server_find_groups
        """
        kwargs: dict[str, Any]
        if action == "jira_server_create_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_group(**kwargs)
        if action == "jira_server_remove_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_group(**kwargs)
        if action == "jira_server_find_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_find_groups(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_create_group', 'jira_server_remove_group', 'jira_server_find_groups"
        )


def register_jira_server_user_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-user"})
    async def atlassian_jira_server_user(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_users_from_group', 'jira_server_add_user_to_group', 'jira_server_remove_user_from_group', 'jira_server_find_users_and_groups', 'jira_server_get_user', 'jira_server_update_user', 'jira_server_policy_check_create_user', 'jira_server_policy_check_update_user', 'jira_server_add_actor_users', 'jira_server_get_user_1', 'jira_server_update_user_1', 'jira_server_create_user', 'jira_server_remove_user', 'jira_server_validate_user_anonymization', 'jira_server_schedule_user_anonymization', 'jira_server_validate_user_anonymization_rerun', 'jira_server_schedule_user_anonymization_rerun', 'jira_server_add_user_to_application_1', 'jira_server_remove_user_from_application_1', 'jira_server_find_bulk_assignable_users', 'jira_server_find_assignable_users_1', 'jira_server_get_duplicated_users_count', 'jira_server_get_duplicated_users_mapping', 'jira_server_get_user_list', 'jira_server_change_user_password', 'jira_server_find_users_with_all_permissions', 'jira_server_find_users_for_picker', 'jira_server_find_users', 'jira_server_find_users_with_browse_permission', 'jira_server_current_user'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server user operations.

        Actions:
          - 'jira_server_get_users_from_group': Call jira_server_get_users_from_group
          - 'jira_server_add_user_to_group': Call jira_server_add_user_to_group
          - 'jira_server_remove_user_from_group': Call jira_server_remove_user_from_group
          - 'jira_server_find_users_and_groups': Call jira_server_find_users_and_groups
          - 'jira_server_get_user': Call jira_server_get_user
          - 'jira_server_update_user': Call jira_server_update_user
          - 'jira_server_policy_check_create_user': Call jira_server_policy_check_create_user
          - 'jira_server_policy_check_update_user': Call jira_server_policy_check_update_user
          - 'jira_server_add_actor_users': Call jira_server_add_actor_users
          - 'jira_server_get_user_1': Call jira_server_get_user_1
          - 'jira_server_update_user_1': Call jira_server_update_user_1
          - 'jira_server_create_user': Call jira_server_create_user
          - 'jira_server_remove_user': Call jira_server_remove_user
          - 'jira_server_validate_user_anonymization': Call jira_server_validate_user_anonymization
          - 'jira_server_schedule_user_anonymization': Call jira_server_schedule_user_anonymization
          - 'jira_server_validate_user_anonymization_rerun': Call jira_server_validate_user_anonymization_rerun
          - 'jira_server_schedule_user_anonymization_rerun': Call jira_server_schedule_user_anonymization_rerun
          - 'jira_server_add_user_to_application_1': Call jira_server_add_user_to_application_1
          - 'jira_server_remove_user_from_application_1': Call jira_server_remove_user_from_application_1
          - 'jira_server_find_bulk_assignable_users': Call jira_server_find_bulk_assignable_users
          - 'jira_server_find_assignable_users_1': Call jira_server_find_assignable_users_1
          - 'jira_server_get_duplicated_users_count': Call jira_server_get_duplicated_users_count
          - 'jira_server_get_duplicated_users_mapping': Call jira_server_get_duplicated_users_mapping
          - 'jira_server_get_user_list': Call jira_server_get_user_list
          - 'jira_server_change_user_password': Call jira_server_change_user_password
          - 'jira_server_find_users_with_all_permissions': Call jira_server_find_users_with_all_permissions
          - 'jira_server_find_users_for_picker': Call jira_server_find_users_for_picker
          - 'jira_server_find_users': Call jira_server_find_users
          - 'jira_server_find_users_with_browse_permission': Call jira_server_find_users_with_browse_permission
          - 'jira_server_current_user': Call jira_server_current_user
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_users_from_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_users_from_group(**kwargs)
        if action == "jira_server_add_user_to_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_user_to_group(**kwargs)
        if action == "jira_server_remove_user_from_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_user_from_group(**kwargs)
        if action == "jira_server_find_users_and_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_find_users_and_groups(**kwargs)
        if action == "jira_server_get_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_user(**kwargs)
        if action == "jira_server_update_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_user(**kwargs)
        if action == "jira_server_policy_check_create_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_policy_check_create_user(**kwargs)
        if action == "jira_server_policy_check_update_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_policy_check_update_user(**kwargs)
        if action == "jira_server_add_actor_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_actor_users(**kwargs)
        if action == "jira_server_get_user_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_user_1(**kwargs)
        if action == "jira_server_update_user_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_user_1(**kwargs)
        if action == "jira_server_create_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_user(**kwargs)
        if action == "jira_server_remove_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_user(**kwargs)
        if action == "jira_server_validate_user_anonymization":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_validate_user_anonymization(**kwargs)
        if action == "jira_server_schedule_user_anonymization":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_schedule_user_anonymization(**kwargs)
        if action == "jira_server_validate_user_anonymization_rerun":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_validate_user_anonymization_rerun(**kwargs)
        if action == "jira_server_schedule_user_anonymization_rerun":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_schedule_user_anonymization_rerun(**kwargs)
        if action == "jira_server_add_user_to_application_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_user_to_application_1(**kwargs)
        if action == "jira_server_remove_user_from_application_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_user_from_application_1(**kwargs)
        if action == "jira_server_find_bulk_assignable_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_find_bulk_assignable_users(**kwargs)
        if action == "jira_server_find_assignable_users_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_find_assignable_users_1(**kwargs)
        if action == "jira_server_get_duplicated_users_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_duplicated_users_count(**kwargs)
        if action == "jira_server_get_duplicated_users_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_duplicated_users_mapping(**kwargs)
        if action == "jira_server_get_user_list":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_user_list(**kwargs)
        if action == "jira_server_change_user_password":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_change_user_password(**kwargs)
        if action == "jira_server_find_users_with_all_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_find_users_with_all_permissions(**kwargs)
        if action == "jira_server_find_users_for_picker":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_find_users_for_picker(**kwargs)
        if action == "jira_server_find_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_find_users(**kwargs)
        if action == "jira_server_find_users_with_browse_permission":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_find_users_with_browse_permission(**kwargs)
        if action == "jira_server_current_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_current_user(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_users_from_group', 'jira_server_add_user_to_group', 'jira_server_remove_user_from_group', 'jira_server_find_users_and_groups', 'jira_server_get_user', 'jira_server_update_user', 'jira_server_policy_check_create_user', 'jira_server_policy_check_update_user', 'jira_server_add_actor_users', 'jira_server_get_user_1', 'jira_server_update_user_1', 'jira_server_create_user', 'jira_server_remove_user', 'jira_server_validate_user_anonymization', 'jira_server_schedule_user_anonymization', 'jira_server_validate_user_anonymization_rerun', 'jira_server_schedule_user_anonymization_rerun', 'jira_server_add_user_to_application_1', 'jira_server_remove_user_from_application_1', 'jira_server_find_bulk_assignable_users', 'jira_server_find_assignable_users_1', 'jira_server_get_duplicated_users_count', 'jira_server_get_duplicated_users_mapping', 'jira_server_get_user_list', 'jira_server_change_user_password', 'jira_server_find_users_with_all_permissions', 'jira_server_find_users_for_picker', 'jira_server_find_users', 'jira_server_find_users_with_browse_permission', 'jira_server_current_user"
        )


def register_jira_server_issue_type_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-type"})
    async def atlassian_jira_server_issue_type(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_create_issue_meta_project_issue_types', 'jira_server_create_issue_type', 'jira_server_get_paginated_issue_types', 'jira_server_get_issue_type_1', 'jira_server_update_issue_type', 'jira_server_delete_issue_type_1', 'jira_server_get_alternative_issue_types', 'jira_server_get_draft_issue_type', 'jira_server_set_draft_issue_type', 'jira_server_delete_draft_issue_type', 'jira_server_get_issue_type', 'jira_server_set_issue_type', 'jira_server_delete_issue_type'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue type operations.

        Actions:
          - 'jira_server_get_create_issue_meta_project_issue_types': Call jira_server_get_create_issue_meta_project_issue_types
          - 'jira_server_create_issue_type': Call jira_server_create_issue_type
          - 'jira_server_get_paginated_issue_types': Call jira_server_get_paginated_issue_types
          - 'jira_server_get_issue_type_1': Call jira_server_get_issue_type_1
          - 'jira_server_update_issue_type': Call jira_server_update_issue_type
          - 'jira_server_delete_issue_type_1': Call jira_server_delete_issue_type_1
          - 'jira_server_get_alternative_issue_types': Call jira_server_get_alternative_issue_types
          - 'jira_server_get_draft_issue_type': Call jira_server_get_draft_issue_type
          - 'jira_server_set_draft_issue_type': Call jira_server_set_draft_issue_type
          - 'jira_server_delete_draft_issue_type': Call jira_server_delete_draft_issue_type
          - 'jira_server_get_issue_type': Call jira_server_get_issue_type
          - 'jira_server_set_issue_type': Call jira_server_set_issue_type
          - 'jira_server_delete_issue_type': Call jira_server_delete_issue_type
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_create_issue_meta_project_issue_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_create_issue_meta_project_issue_types(
                **kwargs
            )
        if action == "jira_server_create_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_issue_type(**kwargs)
        if action == "jira_server_get_paginated_issue_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_paginated_issue_types(**kwargs)
        if action == "jira_server_get_issue_type_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_type_1(**kwargs)
        if action == "jira_server_update_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_issue_type(**kwargs)
        if action == "jira_server_delete_issue_type_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_issue_type_1(**kwargs)
        if action == "jira_server_get_alternative_issue_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_alternative_issue_types(**kwargs)
        if action == "jira_server_get_draft_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_draft_issue_type(**kwargs)
        if action == "jira_server_set_draft_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_draft_issue_type(**kwargs)
        if action == "jira_server_delete_draft_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_draft_issue_type(**kwargs)
        if action == "jira_server_get_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_type(**kwargs)
        if action == "jira_server_set_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_issue_type(**kwargs)
        if action == "jira_server_delete_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_issue_type(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_create_issue_meta_project_issue_types', 'jira_server_create_issue_type', 'jira_server_get_paginated_issue_types', 'jira_server_get_issue_type_1', 'jira_server_update_issue_type', 'jira_server_delete_issue_type_1', 'jira_server_get_alternative_issue_types', 'jira_server_get_draft_issue_type', 'jira_server_set_draft_issue_type', 'jira_server_delete_draft_issue_type', 'jira_server_get_issue_type', 'jira_server_set_issue_type', 'jira_server_delete_issue_type"
        )


def register_jira_server_issue_link_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-link"})
    async def atlassian_jira_server_issue_link(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_create_reciprocal_remote_issue_link', 'jira_server_get_remote_issue_links', 'jira_server_create_or_update_remote_issue_link', 'jira_server_delete_remote_issue_link_by_global_id', 'jira_server_get_remote_issue_link_by_id', 'jira_server_update_remote_issue_link', 'jira_server_delete_remote_issue_link_by_id'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue link operations.

        Actions:
          - 'jira_server_create_reciprocal_remote_issue_link': Call jira_server_create_reciprocal_remote_issue_link
          - 'jira_server_get_remote_issue_links': Call jira_server_get_remote_issue_links
          - 'jira_server_create_or_update_remote_issue_link': Call jira_server_create_or_update_remote_issue_link
          - 'jira_server_delete_remote_issue_link_by_global_id': Call jira_server_delete_remote_issue_link_by_global_id
          - 'jira_server_get_remote_issue_link_by_id': Call jira_server_get_remote_issue_link_by_id
          - 'jira_server_update_remote_issue_link': Call jira_server_update_remote_issue_link
          - 'jira_server_delete_remote_issue_link_by_id': Call jira_server_delete_remote_issue_link_by_id
        """
        kwargs: dict[str, Any]
        if action == "jira_server_create_reciprocal_remote_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_reciprocal_remote_issue_link(**kwargs)
        if action == "jira_server_get_remote_issue_links":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_remote_issue_links(**kwargs)
        if action == "jira_server_create_or_update_remote_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_or_update_remote_issue_link(**kwargs)
        if action == "jira_server_delete_remote_issue_link_by_global_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_remote_issue_link_by_global_id(**kwargs)
        if action == "jira_server_get_remote_issue_link_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_remote_issue_link_by_id(**kwargs)
        if action == "jira_server_update_remote_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_remote_issue_link(**kwargs)
        if action == "jira_server_delete_remote_issue_link_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_remote_issue_link_by_id(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_create_reciprocal_remote_issue_link', 'jira_server_get_remote_issue_links', 'jira_server_create_or_update_remote_issue_link', 'jira_server_delete_remote_issue_link_by_global_id', 'jira_server_get_remote_issue_link_by_id', 'jira_server_update_remote_issue_link', 'jira_server_delete_remote_issue_link_by_id"
        )


def register_jira_server_issue_comment_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-comment"})
    async def atlassian_jira_server_issue_comment(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_comments', 'jira_server_add_comment', 'jira_server_get_comment', 'jira_server_update_comment', 'jira_server_delete_comment', 'jira_server_set_pin_comment', 'jira_server_get_pinned_comments'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue comment operations.

        Actions:
          - 'jira_server_get_comments': Call jira_server_get_comments
          - 'jira_server_add_comment': Call jira_server_add_comment
          - 'jira_server_get_comment': Call jira_server_get_comment
          - 'jira_server_update_comment': Call jira_server_update_comment
          - 'jira_server_delete_comment': Call jira_server_delete_comment
          - 'jira_server_set_pin_comment': Call jira_server_set_pin_comment
          - 'jira_server_get_pinned_comments': Call jira_server_get_pinned_comments
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_comments(**kwargs)
        if action == "jira_server_add_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_comment(**kwargs)
        if action == "jira_server_get_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_comment(**kwargs)
        if action == "jira_server_update_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_comment(**kwargs)
        if action == "jira_server_delete_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_comment(**kwargs)
        if action == "jira_server_set_pin_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_set_pin_comment(**kwargs)
        if action == "jira_server_get_pinned_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_pinned_comments(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_comments', 'jira_server_add_comment', 'jira_server_get_comment', 'jira_server_update_comment', 'jira_server_delete_comment', 'jira_server_set_pin_comment', 'jira_server_get_pinned_comments"
        )


def register_jira_server_issue_subtask_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-subtask"})
    async def atlassian_jira_server_issue_subtask(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_sub_tasks', 'jira_server_can_move_sub_task', 'jira_server_move_sub_tasks'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue subtask operations.

        Actions:
          - 'jira_server_get_sub_tasks': Call jira_server_get_sub_tasks
          - 'jira_server_can_move_sub_task': Call jira_server_can_move_sub_task
          - 'jira_server_move_sub_tasks': Call jira_server_move_sub_tasks
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_sub_tasks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_sub_tasks(**kwargs)
        if action == "jira_server_can_move_sub_task":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_can_move_sub_task(**kwargs)
        if action == "jira_server_move_sub_tasks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_move_sub_tasks(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_sub_tasks', 'jira_server_can_move_sub_task', 'jira_server_move_sub_tasks"
        )


def register_jira_server_issue_transition_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-transition"})
    async def atlassian_jira_server_issue_transition(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_transitions', 'jira_server_do_transition'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue transition operations.

        Actions:
          - 'jira_server_get_transitions': Call jira_server_get_transitions
          - 'jira_server_do_transition': Call jira_server_do_transition
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_transitions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_transitions(**kwargs)
        if action == "jira_server_do_transition":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_do_transition(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_transitions', 'jira_server_do_transition"
        )


def register_jira_server_issue_vote_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-vote"})
    async def atlassian_jira_server_issue_vote(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_votes', 'jira_server_add_vote', 'jira_server_remove_vote'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue vote operations.

        Actions:
          - 'jira_server_get_votes': Call jira_server_get_votes
          - 'jira_server_add_vote': Call jira_server_add_vote
          - 'jira_server_remove_vote': Call jira_server_remove_vote
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_votes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_votes(**kwargs)
        if action == "jira_server_add_vote":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_vote(**kwargs)
        if action == "jira_server_remove_vote":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_vote(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_votes', 'jira_server_add_vote', 'jira_server_remove_vote"
        )


def register_jira_server_issue_watcher_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-watcher"})
    async def atlassian_jira_server_issue_watcher(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_issue_watchers', 'jira_server_add_watcher_1', 'jira_server_remove_watcher_1'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue watcher operations.

        Actions:
          - 'jira_server_get_issue_watchers': Call jira_server_get_issue_watchers
          - 'jira_server_add_watcher_1': Call jira_server_add_watcher_1
          - 'jira_server_remove_watcher_1': Call jira_server_remove_watcher_1
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_issue_watchers":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_watchers(**kwargs)
        if action == "jira_server_add_watcher_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_watcher_1(**kwargs)
        if action == "jira_server_remove_watcher_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_watcher_1(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_issue_watchers', 'jira_server_add_watcher_1', 'jira_server_remove_watcher_1"
        )


def register_jira_server_issue_worklog_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-worklog"})
    async def atlassian_jira_server_issue_worklog(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_issue_worklog', 'jira_server_add_worklog', 'jira_server_get_worklog', 'jira_server_update_worklog', 'jira_server_delete_worklog', 'jira_server_get_ids_of_worklogs_deleted_since', 'jira_server_get_worklogs_for_ids', 'jira_server_get_ids_of_worklogs_modified_since'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue worklog operations.

        Actions:
          - 'jira_server_get_issue_worklog': Call jira_server_get_issue_worklog
          - 'jira_server_add_worklog': Call jira_server_add_worklog
          - 'jira_server_get_worklog': Call jira_server_get_worklog
          - 'jira_server_update_worklog': Call jira_server_update_worklog
          - 'jira_server_delete_worklog': Call jira_server_delete_worklog
          - 'jira_server_get_ids_of_worklogs_deleted_since': Call jira_server_get_ids_of_worklogs_deleted_since
          - 'jira_server_get_worklogs_for_ids': Call jira_server_get_worklogs_for_ids
          - 'jira_server_get_ids_of_worklogs_modified_since': Call jira_server_get_ids_of_worklogs_modified_since
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_issue_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_worklog(**kwargs)
        if action == "jira_server_add_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_worklog(**kwargs)
        if action == "jira_server_get_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_worklog(**kwargs)
        if action == "jira_server_update_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_worklog(**kwargs)
        if action == "jira_server_delete_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_worklog(**kwargs)
        if action == "jira_server_get_ids_of_worklogs_deleted_since":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_ids_of_worklogs_deleted_since(**kwargs)
        if action == "jira_server_get_worklogs_for_ids":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_worklogs_for_ids(**kwargs)
        if action == "jira_server_get_ids_of_worklogs_modified_since":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_ids_of_worklogs_modified_since(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_issue_worklog', 'jira_server_add_worklog', 'jira_server_get_worklog', 'jira_server_update_worklog', 'jira_server_delete_worklog', 'jira_server_get_ids_of_worklogs_deleted_since', 'jira_server_get_worklogs_for_ids', 'jira_server_get_ids_of_worklogs_modified_since"
        )


def register_jira_server_issue_link_type_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-link-type"})
    async def atlassian_jira_server_issue_link_type(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_issue_link', 'jira_server_delete_issue_link', 'jira_server_get_issue_link_types', 'jira_server_create_issue_link_type', 'jira_server_get_issue_link_type', 'jira_server_update_issue_link_type', 'jira_server_delete_issue_link_type', 'jira_server_move_issue_link_type'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue link type operations.

        Actions:
          - 'jira_server_get_issue_link': Call jira_server_get_issue_link
          - 'jira_server_delete_issue_link': Call jira_server_delete_issue_link
          - 'jira_server_get_issue_link_types': Call jira_server_get_issue_link_types
          - 'jira_server_create_issue_link_type': Call jira_server_create_issue_link_type
          - 'jira_server_get_issue_link_type': Call jira_server_get_issue_link_type
          - 'jira_server_update_issue_link_type': Call jira_server_update_issue_link_type
          - 'jira_server_delete_issue_link_type': Call jira_server_delete_issue_link_type
          - 'jira_server_move_issue_link_type': Call jira_server_move_issue_link_type
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_link(**kwargs)
        if action == "jira_server_delete_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_issue_link(**kwargs)
        if action == "jira_server_get_issue_link_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_link_types(**kwargs)
        if action == "jira_server_create_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_issue_link_type(**kwargs)
        if action == "jira_server_get_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_link_type(**kwargs)
        if action == "jira_server_update_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_issue_link_type(**kwargs)
        if action == "jira_server_delete_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_issue_link_type(**kwargs)
        if action == "jira_server_move_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_move_issue_link_type(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_issue_link', 'jira_server_delete_issue_link', 'jira_server_get_issue_link_types', 'jira_server_create_issue_link_type', 'jira_server_get_issue_link_type', 'jira_server_update_issue_link_type', 'jira_server_delete_issue_link_type', 'jira_server_move_issue_link_type"
        )


def register_jira_server_issue_type_scheme_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-issue-type-scheme"})
    async def atlassian_jira_server_issue_type_scheme(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_all_issue_type_schemes', 'jira_server_create_issue_type_scheme', 'jira_server_get_issue_type_scheme', 'jira_server_update_issue_type_scheme', 'jira_server_delete_issue_type_scheme'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server issue type scheme operations.

        Actions:
          - 'jira_server_get_all_issue_type_schemes': Call jira_server_get_all_issue_type_schemes
          - 'jira_server_create_issue_type_scheme': Call jira_server_create_issue_type_scheme
          - 'jira_server_get_issue_type_scheme': Call jira_server_get_issue_type_scheme
          - 'jira_server_update_issue_type_scheme': Call jira_server_update_issue_type_scheme
          - 'jira_server_delete_issue_type_scheme': Call jira_server_delete_issue_type_scheme
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_all_issue_type_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_issue_type_schemes(**kwargs)
        if action == "jira_server_create_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_issue_type_scheme(**kwargs)
        if action == "jira_server_get_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_issue_type_scheme(**kwargs)
        if action == "jira_server_update_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_issue_type_scheme(**kwargs)
        if action == "jira_server_delete_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_issue_type_scheme(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_all_issue_type_schemes', 'jira_server_create_issue_type_scheme', 'jira_server_get_issue_type_scheme', 'jira_server_update_issue_type_scheme', 'jira_server_delete_issue_type_scheme"
        )


def register_jira_server_permission_scheme_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-permission-scheme"})
    async def atlassian_jira_server_permission_scheme(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_permission_schemes', 'jira_server_create_permission_scheme', 'jira_server_get_permission_scheme', 'jira_server_update_permission_scheme', 'jira_server_delete_permission_scheme', 'jira_server_get_permission_scheme_grants', 'jira_server_get_permission_scheme_grant', 'jira_server_delete_permission_scheme_entity', 'jira_server_get_assigned_permission_scheme', 'jira_server_assign_permission_scheme'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server permission scheme operations.

        Actions:
          - 'jira_server_get_permission_schemes': Call jira_server_get_permission_schemes
          - 'jira_server_create_permission_scheme': Call jira_server_create_permission_scheme
          - 'jira_server_get_permission_scheme': Call jira_server_get_permission_scheme
          - 'jira_server_update_permission_scheme': Call jira_server_update_permission_scheme
          - 'jira_server_delete_permission_scheme': Call jira_server_delete_permission_scheme
          - 'jira_server_get_permission_scheme_grants': Call jira_server_get_permission_scheme_grants
          - 'jira_server_get_permission_scheme_grant': Call jira_server_get_permission_scheme_grant
          - 'jira_server_delete_permission_scheme_entity': Call jira_server_delete_permission_scheme_entity
          - 'jira_server_get_assigned_permission_scheme': Call jira_server_get_assigned_permission_scheme
          - 'jira_server_assign_permission_scheme': Call jira_server_assign_permission_scheme
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_permission_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_permission_schemes(**kwargs)
        if action == "jira_server_create_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_permission_scheme(**kwargs)
        if action == "jira_server_get_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_permission_scheme(**kwargs)
        if action == "jira_server_update_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_permission_scheme(**kwargs)
        if action == "jira_server_delete_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_permission_scheme(**kwargs)
        if action == "jira_server_get_permission_scheme_grants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_permission_scheme_grants(**kwargs)
        if action == "jira_server_get_permission_scheme_grant":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_permission_scheme_grant(**kwargs)
        if action == "jira_server_delete_permission_scheme_entity":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_permission_scheme_entity(**kwargs)
        if action == "jira_server_get_assigned_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_assigned_permission_scheme(**kwargs)
        if action == "jira_server_assign_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_assign_permission_scheme(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_permission_schemes', 'jira_server_create_permission_scheme', 'jira_server_get_permission_scheme', 'jira_server_update_permission_scheme', 'jira_server_delete_permission_scheme', 'jira_server_get_permission_scheme_grants', 'jira_server_get_permission_scheme_grant', 'jira_server_delete_permission_scheme_entity', 'jira_server_get_assigned_permission_scheme', 'jira_server_assign_permission_scheme"
        )


def register_jira_server_priority_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-priority"})
    async def atlassian_jira_server_priority(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_priority'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server priority operations.

        Actions:
          - 'jira_server_get_priority': Call jira_server_get_priority
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_priority":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_priority(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_priority"
        )


def register_jira_server_priority_scheme_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-priority-scheme"})
    async def atlassian_jira_server_priority_scheme(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_priority_schemes', 'jira_server_create_priority_scheme', 'jira_server_get_priority_scheme', 'jira_server_update_priority_scheme', 'jira_server_delete_priority_scheme', 'jira_server_get_assigned_priority_scheme', 'jira_server_assign_priority_scheme', 'jira_server_unassign_priority_scheme'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server priority scheme operations.

        Actions:
          - 'jira_server_get_priority_schemes': Call jira_server_get_priority_schemes
          - 'jira_server_create_priority_scheme': Call jira_server_create_priority_scheme
          - 'jira_server_get_priority_scheme': Call jira_server_get_priority_scheme
          - 'jira_server_update_priority_scheme': Call jira_server_update_priority_scheme
          - 'jira_server_delete_priority_scheme': Call jira_server_delete_priority_scheme
          - 'jira_server_get_assigned_priority_scheme': Call jira_server_get_assigned_priority_scheme
          - 'jira_server_assign_priority_scheme': Call jira_server_assign_priority_scheme
          - 'jira_server_unassign_priority_scheme': Call jira_server_unassign_priority_scheme
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_priority_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_priority_schemes(**kwargs)
        if action == "jira_server_create_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_priority_scheme(**kwargs)
        if action == "jira_server_get_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_priority_scheme(**kwargs)
        if action == "jira_server_update_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_priority_scheme(**kwargs)
        if action == "jira_server_delete_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_priority_scheme(**kwargs)
        if action == "jira_server_get_assigned_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_assigned_priority_scheme(**kwargs)
        if action == "jira_server_assign_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_assign_priority_scheme(**kwargs)
        if action == "jira_server_unassign_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_unassign_priority_scheme(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_priority_schemes', 'jira_server_create_priority_scheme', 'jira_server_get_priority_scheme', 'jira_server_update_priority_scheme', 'jira_server_delete_priority_scheme', 'jira_server_get_assigned_priority_scheme', 'jira_server_assign_priority_scheme', 'jira_server_unassign_priority_scheme"
        )


def register_jira_server_project_avatar_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-project-avatar"})
    async def atlassian_jira_server_project_avatar(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_update_project_avatar'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server project avatar operations.

        Actions:
          - 'jira_server_update_project_avatar': Call jira_server_update_project_avatar
        """
        kwargs: dict[str, Any]
        if action == "jira_server_update_project_avatar":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_project_avatar(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_update_project_avatar"
        )


def register_jira_server_project_component_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-project-component"})
    async def atlassian_jira_server_project_component(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_project_components'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server project component operations.

        Actions:
          - 'jira_server_get_project_components': Call jira_server_get_project_components
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_project_components":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_components(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_project_components"
        )


def register_jira_server_project_role_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-project-role"})
    async def atlassian_jira_server_project_role(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_project_roles', 'jira_server_get_project_role', 'jira_server_get_project_roles_1', 'jira_server_create_project_role', 'jira_server_get_project_roles_by_id', 'jira_server_fully_update_project_role', 'jira_server_partial_update_project_role', 'jira_server_delete_project_role', 'jira_server_get_project_role_actors_for_role', 'jira_server_add_project_role_actors_to_role', 'jira_server_delete_project_role_actors_from_role'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server project role operations.

        Actions:
          - 'jira_server_get_project_roles': Call jira_server_get_project_roles
          - 'jira_server_get_project_role': Call jira_server_get_project_role
          - 'jira_server_get_project_roles_1': Call jira_server_get_project_roles_1
          - 'jira_server_create_project_role': Call jira_server_create_project_role
          - 'jira_server_get_project_roles_by_id': Call jira_server_get_project_roles_by_id
          - 'jira_server_fully_update_project_role': Call jira_server_fully_update_project_role
          - 'jira_server_partial_update_project_role': Call jira_server_partial_update_project_role
          - 'jira_server_delete_project_role': Call jira_server_delete_project_role
          - 'jira_server_get_project_role_actors_for_role': Call jira_server_get_project_role_actors_for_role
          - 'jira_server_add_project_role_actors_to_role': Call jira_server_add_project_role_actors_to_role
          - 'jira_server_delete_project_role_actors_from_role': Call jira_server_delete_project_role_actors_from_role
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_project_roles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_roles(**kwargs)
        if action == "jira_server_get_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_role(**kwargs)
        if action == "jira_server_get_project_roles_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_roles_1(**kwargs)
        if action == "jira_server_create_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_project_role(**kwargs)
        if action == "jira_server_get_project_roles_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_roles_by_id(**kwargs)
        if action == "jira_server_fully_update_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_fully_update_project_role(**kwargs)
        if action == "jira_server_partial_update_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_partial_update_project_role(**kwargs)
        if action == "jira_server_delete_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_project_role(**kwargs)
        if action == "jira_server_get_project_role_actors_for_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_role_actors_for_role(**kwargs)
        if action == "jira_server_add_project_role_actors_to_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_add_project_role_actors_to_role(**kwargs)
        if action == "jira_server_delete_project_role_actors_from_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_project_role_actors_from_role(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_project_roles', 'jira_server_get_project_role', 'jira_server_get_project_roles_1', 'jira_server_create_project_role', 'jira_server_get_project_roles_by_id', 'jira_server_fully_update_project_role', 'jira_server_partial_update_project_role', 'jira_server_delete_project_role', 'jira_server_get_project_role_actors_for_role', 'jira_server_add_project_role_actors_to_role', 'jira_server_delete_project_role_actors_from_role"
        )


def register_jira_server_project_category_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-project-category"})
    async def atlassian_jira_server_project_category(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_create_project_category', 'jira_server_get_project_category_by_id', 'jira_server_update_project_category', 'jira_server_remove_project_category'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server project category operations.

        Actions:
          - 'jira_server_create_project_category': Call jira_server_create_project_category
          - 'jira_server_get_project_category_by_id': Call jira_server_get_project_category_by_id
          - 'jira_server_update_project_category': Call jira_server_update_project_category
          - 'jira_server_remove_project_category': Call jira_server_remove_project_category
        """
        kwargs: dict[str, Any]
        if action == "jira_server_create_project_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_create_project_category(**kwargs)
        if action == "jira_server_get_project_category_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_project_category_by_id(**kwargs)
        if action == "jira_server_update_project_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_project_category(**kwargs)
        if action == "jira_server_remove_project_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_remove_project_category(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_create_project_category', 'jira_server_get_project_category_by_id', 'jira_server_update_project_category', 'jira_server_remove_project_category"
        )


def register_jira_server_resolution_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-resolution"})
    async def atlassian_jira_server_resolution(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_resolutions', 'jira_server_get_paginated_resolutions', 'jira_server_get_resolution'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server resolution operations.

        Actions:
          - 'jira_server_get_resolutions': Call jira_server_get_resolutions
          - 'jira_server_get_paginated_resolutions': Call jira_server_get_paginated_resolutions
          - 'jira_server_get_resolution': Call jira_server_get_resolution
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_resolutions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_resolutions(**kwargs)
        if action == "jira_server_get_paginated_resolutions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_paginated_resolutions(**kwargs)
        if action == "jira_server_get_resolution":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_resolution(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_resolutions', 'jira_server_get_paginated_resolutions', 'jira_server_get_resolution"
        )


def register_jira_server_search_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-search"})
    async def atlassian_jira_server_search(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_search_1', 'jira_server_search_using_search_request'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server search operations.

        Actions:
          - 'jira_server_search_1': Call jira_server_search_1
          - 'jira_server_search_using_search_request': Call jira_server_search_using_search_request
        """
        kwargs: dict[str, Any]
        if action == "jira_server_search_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_search_1(**kwargs)
        if action == "jira_server_search_using_search_request":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_search_using_search_request(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_search_1', 'jira_server_search_using_search_request"
        )


def register_jira_server_user_avatar_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-user-avatar"})
    async def atlassian_jira_server_user_avatar(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_update_user_avatar_1'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server user avatar operations.

        Actions:
          - 'jira_server_update_user_avatar_1': Call jira_server_update_user_avatar_1
        """
        kwargs: dict[str, Any]
        if action == "jira_server_update_user_avatar_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_user_avatar_1(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_update_user_avatar_1"
        )


def register_jira_server_workflow_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-server-workflow"})
    async def atlassian_jira_server_workflow(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_server_get_all_workflows', 'jira_server_get_draft_workflow', 'jira_server_update_draft_workflow_mapping', 'jira_server_delete_draft_workflow_mapping', 'jira_server_get_workflow', 'jira_server_update_workflow_mapping', 'jira_server_delete_workflow_mapping'"
        ),
        client=Depends(get_jira_server_client),
    ) -> dict:
        """Manage jira server workflow operations.

        Actions:
          - 'jira_server_get_all_workflows': Call jira_server_get_all_workflows
          - 'jira_server_get_draft_workflow': Call jira_server_get_draft_workflow
          - 'jira_server_update_draft_workflow_mapping': Call jira_server_update_draft_workflow_mapping
          - 'jira_server_delete_draft_workflow_mapping': Call jira_server_delete_draft_workflow_mapping
          - 'jira_server_get_workflow': Call jira_server_get_workflow
          - 'jira_server_update_workflow_mapping': Call jira_server_update_workflow_mapping
          - 'jira_server_delete_workflow_mapping': Call jira_server_delete_workflow_mapping
        """
        kwargs: dict[str, Any]
        if action == "jira_server_get_all_workflows":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_all_workflows(**kwargs)
        if action == "jira_server_get_draft_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_draft_workflow(**kwargs)
        if action == "jira_server_update_draft_workflow_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_draft_workflow_mapping(**kwargs)
        if action == "jira_server_delete_draft_workflow_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_draft_workflow_mapping(**kwargs)
        if action == "jira_server_get_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_get_workflow(**kwargs)
        if action == "jira_server_update_workflow_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_update_workflow_mapping(**kwargs)
        if action == "jira_server_delete_workflow_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_server_delete_workflow_mapping(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_server_get_all_workflows', 'jira_server_get_draft_workflow', 'jira_server_update_draft_workflow_mapping', 'jira_server_delete_draft_workflow_mapping', 'jira_server_get_workflow', 'jira_server_update_workflow_mapping', 'jira_server_delete_workflow_mapping"
        )


def register_jira_cloud_user_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-user"})
    async def atlassian_jira_cloud_user(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_all_application_roles', 'jira_cloud_get_application_role', 'jira_cloud_get_all_user_data_classification_levels', 'jira_cloud_get_share_permissions', 'jira_cloud_add_share_permission', 'jira_cloud_delete_share_permission', 'jira_cloud_get_share_permission', 'jira_cloud_remove_group', 'jira_cloud_get_group', 'jira_cloud_create_group', 'jira_cloud_get_users_from_group', 'jira_cloud_remove_user_from_group', 'jira_cloud_add_user_to_group', 'jira_cloud_find_groups', 'jira_cloud_find_users_and_groups', 'jira_cloud_get_my_permissions', 'jira_cloud_get_current_user', 'jira_cloud_get_all_permissions', 'jira_cloud_get_all_permission_schemes', 'jira_cloud_create_permission_scheme', 'jira_cloud_delete_permission_scheme', 'jira_cloud_get_permission_scheme', 'jira_cloud_update_permission_scheme', 'jira_cloud_get_permission_scheme_grants', 'jira_cloud_create_permission_grant', 'jira_cloud_delete_permission_scheme_entity', 'jira_cloud_get_permission_scheme_grant', 'jira_cloud_add_actor_users', 'jira_cloud_get_assigned_permission_scheme', 'jira_cloud_assign_permission_scheme', 'jira_cloud_remove_user', 'jira_cloud_get_user', 'jira_cloud_create_user', 'jira_cloud_find_assignable_users', 'jira_cloud_reset_user_columns', 'jira_cloud_get_user_default_columns', 'jira_cloud_set_user_columns', 'jira_cloud_get_user_email', 'jira_cloud_get_user_groups', 'jira_cloud_find_users_with_all_permissions', 'jira_cloud_find_users_for_picker', 'jira_cloud_get_user_property_keys', 'jira_cloud_delete_user_property', 'jira_cloud_get_user_property', 'jira_cloud_set_user_property', 'jira_cloud_find_users', 'jira_cloud_find_users_by_query', 'jira_cloud_find_user_keys_by_query', 'jira_cloud_find_users_with_browse_permission', 'jira_cloud_get_all_users_default', 'jira_cloud_get_all_users'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud user operations.

        Actions:
          - 'jira_cloud_get_all_application_roles': Call jira_cloud_get_all_application_roles
          - 'jira_cloud_get_application_role': Call jira_cloud_get_application_role
          - 'jira_cloud_get_all_user_data_classification_levels': Call jira_cloud_get_all_user_data_classification_levels
          - 'jira_cloud_get_share_permissions': Call jira_cloud_get_share_permissions
          - 'jira_cloud_add_share_permission': Call jira_cloud_add_share_permission
          - 'jira_cloud_delete_share_permission': Call jira_cloud_delete_share_permission
          - 'jira_cloud_get_share_permission': Call jira_cloud_get_share_permission
          - 'jira_cloud_remove_group': Call jira_cloud_remove_group
          - 'jira_cloud_get_group': Call jira_cloud_get_group
          - 'jira_cloud_create_group': Call jira_cloud_create_group
          - 'jira_cloud_get_users_from_group': Call jira_cloud_get_users_from_group
          - 'jira_cloud_remove_user_from_group': Call jira_cloud_remove_user_from_group
          - 'jira_cloud_add_user_to_group': Call jira_cloud_add_user_to_group
          - 'jira_cloud_find_groups': Call jira_cloud_find_groups
          - 'jira_cloud_find_users_and_groups': Call jira_cloud_find_users_and_groups
          - 'jira_cloud_get_my_permissions': Call jira_cloud_get_my_permissions
          - 'jira_cloud_get_current_user': Call jira_cloud_get_current_user
          - 'jira_cloud_get_all_permissions': Call jira_cloud_get_all_permissions
          - 'jira_cloud_get_all_permission_schemes': Call jira_cloud_get_all_permission_schemes
          - 'jira_cloud_create_permission_scheme': Call jira_cloud_create_permission_scheme
          - 'jira_cloud_delete_permission_scheme': Call jira_cloud_delete_permission_scheme
          - 'jira_cloud_get_permission_scheme': Call jira_cloud_get_permission_scheme
          - 'jira_cloud_update_permission_scheme': Call jira_cloud_update_permission_scheme
          - 'jira_cloud_get_permission_scheme_grants': Call jira_cloud_get_permission_scheme_grants
          - 'jira_cloud_create_permission_grant': Call jira_cloud_create_permission_grant
          - 'jira_cloud_delete_permission_scheme_entity': Call jira_cloud_delete_permission_scheme_entity
          - 'jira_cloud_get_permission_scheme_grant': Call jira_cloud_get_permission_scheme_grant
          - 'jira_cloud_add_actor_users': Call jira_cloud_add_actor_users
          - 'jira_cloud_get_assigned_permission_scheme': Call jira_cloud_get_assigned_permission_scheme
          - 'jira_cloud_assign_permission_scheme': Call jira_cloud_assign_permission_scheme
          - 'jira_cloud_remove_user': Call jira_cloud_remove_user
          - 'jira_cloud_get_user': Call jira_cloud_get_user
          - 'jira_cloud_create_user': Call jira_cloud_create_user
          - 'jira_cloud_find_assignable_users': Call jira_cloud_find_assignable_users
          - 'jira_cloud_reset_user_columns': Call jira_cloud_reset_user_columns
          - 'jira_cloud_get_user_default_columns': Call jira_cloud_get_user_default_columns
          - 'jira_cloud_set_user_columns': Call jira_cloud_set_user_columns
          - 'jira_cloud_get_user_email': Call jira_cloud_get_user_email
          - 'jira_cloud_get_user_groups': Call jira_cloud_get_user_groups
          - 'jira_cloud_find_users_with_all_permissions': Call jira_cloud_find_users_with_all_permissions
          - 'jira_cloud_find_users_for_picker': Call jira_cloud_find_users_for_picker
          - 'jira_cloud_get_user_property_keys': Call jira_cloud_get_user_property_keys
          - 'jira_cloud_delete_user_property': Call jira_cloud_delete_user_property
          - 'jira_cloud_get_user_property': Call jira_cloud_get_user_property
          - 'jira_cloud_set_user_property': Call jira_cloud_set_user_property
          - 'jira_cloud_find_users': Call jira_cloud_find_users
          - 'jira_cloud_find_users_by_query': Call jira_cloud_find_users_by_query
          - 'jira_cloud_find_user_keys_by_query': Call jira_cloud_find_user_keys_by_query
          - 'jira_cloud_find_users_with_browse_permission': Call jira_cloud_find_users_with_browse_permission
          - 'jira_cloud_get_all_users_default': Call jira_cloud_get_all_users_default
          - 'jira_cloud_get_all_users': Call jira_cloud_get_all_users
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_all_application_roles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_application_roles(**kwargs)
        if action == "jira_cloud_get_application_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_application_role(**kwargs)
        if action == "jira_cloud_get_all_user_data_classification_levels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_user_data_classification_levels(**kwargs)
        if action == "jira_cloud_get_share_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_share_permissions(**kwargs)
        if action == "jira_cloud_add_share_permission":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_share_permission(**kwargs)
        if action == "jira_cloud_delete_share_permission":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_share_permission(**kwargs)
        if action == "jira_cloud_get_share_permission":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_share_permission(**kwargs)
        if action == "jira_cloud_remove_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_group(**kwargs)
        if action == "jira_cloud_get_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_group(**kwargs)
        if action == "jira_cloud_create_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_group(**kwargs)
        if action == "jira_cloud_get_users_from_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_users_from_group(**kwargs)
        if action == "jira_cloud_remove_user_from_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_user_from_group(**kwargs)
        if action == "jira_cloud_add_user_to_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_user_to_group(**kwargs)
        if action == "jira_cloud_find_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_groups(**kwargs)
        if action == "jira_cloud_find_users_and_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_users_and_groups(**kwargs)
        if action == "jira_cloud_get_my_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_my_permissions(**kwargs)
        if action == "jira_cloud_get_current_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_current_user(**kwargs)
        if action == "jira_cloud_get_all_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_permissions(**kwargs)
        if action == "jira_cloud_get_all_permission_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_permission_schemes(**kwargs)
        if action == "jira_cloud_create_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_permission_scheme(**kwargs)
        if action == "jira_cloud_delete_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_permission_scheme(**kwargs)
        if action == "jira_cloud_get_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_permission_scheme(**kwargs)
        if action == "jira_cloud_update_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_permission_scheme(**kwargs)
        if action == "jira_cloud_get_permission_scheme_grants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_permission_scheme_grants(**kwargs)
        if action == "jira_cloud_create_permission_grant":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_permission_grant(**kwargs)
        if action == "jira_cloud_delete_permission_scheme_entity":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_permission_scheme_entity(**kwargs)
        if action == "jira_cloud_get_permission_scheme_grant":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_permission_scheme_grant(**kwargs)
        if action == "jira_cloud_add_actor_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_actor_users(**kwargs)
        if action == "jira_cloud_get_assigned_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_assigned_permission_scheme(**kwargs)
        if action == "jira_cloud_assign_permission_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_assign_permission_scheme(**kwargs)
        if action == "jira_cloud_remove_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_user(**kwargs)
        if action == "jira_cloud_get_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_user(**kwargs)
        if action == "jira_cloud_create_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_user(**kwargs)
        if action == "jira_cloud_find_assignable_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_assignable_users(**kwargs)
        if action == "jira_cloud_reset_user_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_reset_user_columns(**kwargs)
        if action == "jira_cloud_get_user_default_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_user_default_columns(**kwargs)
        if action == "jira_cloud_set_user_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_user_columns(**kwargs)
        if action == "jira_cloud_get_user_email":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_user_email(**kwargs)
        if action == "jira_cloud_get_user_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_user_groups(**kwargs)
        if action == "jira_cloud_find_users_with_all_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_users_with_all_permissions(**kwargs)
        if action == "jira_cloud_find_users_for_picker":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_users_for_picker(**kwargs)
        if action == "jira_cloud_get_user_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_user_property_keys(**kwargs)
        if action == "jira_cloud_delete_user_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_user_property(**kwargs)
        if action == "jira_cloud_get_user_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_user_property(**kwargs)
        if action == "jira_cloud_set_user_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_user_property(**kwargs)
        if action == "jira_cloud_find_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_users(**kwargs)
        if action == "jira_cloud_find_users_by_query":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_users_by_query(**kwargs)
        if action == "jira_cloud_find_user_keys_by_query":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_user_keys_by_query(**kwargs)
        if action == "jira_cloud_find_users_with_browse_permission":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_users_with_browse_permission(**kwargs)
        if action == "jira_cloud_get_all_users_default":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_users_default(**kwargs)
        if action == "jira_cloud_get_all_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_users(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_all_application_roles', 'jira_cloud_get_application_role', 'jira_cloud_get_all_user_data_classification_levels', 'jira_cloud_get_share_permissions', 'jira_cloud_add_share_permission', 'jira_cloud_delete_share_permission', 'jira_cloud_get_share_permission', 'jira_cloud_remove_group', 'jira_cloud_get_group', 'jira_cloud_create_group', 'jira_cloud_get_users_from_group', 'jira_cloud_remove_user_from_group', 'jira_cloud_add_user_to_group', 'jira_cloud_find_groups', 'jira_cloud_find_users_and_groups', 'jira_cloud_get_my_permissions', 'jira_cloud_get_current_user', 'jira_cloud_get_all_permissions', 'jira_cloud_get_all_permission_schemes', 'jira_cloud_create_permission_scheme', 'jira_cloud_delete_permission_scheme', 'jira_cloud_get_permission_scheme', 'jira_cloud_update_permission_scheme', 'jira_cloud_get_permission_scheme_grants', 'jira_cloud_create_permission_grant', 'jira_cloud_delete_permission_scheme_entity', 'jira_cloud_get_permission_scheme_grant', 'jira_cloud_add_actor_users', 'jira_cloud_get_assigned_permission_scheme', 'jira_cloud_assign_permission_scheme', 'jira_cloud_remove_user', 'jira_cloud_get_user', 'jira_cloud_create_user', 'jira_cloud_find_assignable_users', 'jira_cloud_reset_user_columns', 'jira_cloud_get_user_default_columns', 'jira_cloud_set_user_columns', 'jira_cloud_get_user_email', 'jira_cloud_get_user_groups', 'jira_cloud_find_users_with_all_permissions', 'jira_cloud_find_users_for_picker', 'jira_cloud_get_user_property_keys', 'jira_cloud_delete_user_property', 'jira_cloud_get_user_property', 'jira_cloud_set_user_property', 'jira_cloud_find_users', 'jira_cloud_find_users_by_query', 'jira_cloud_find_user_keys_by_query', 'jira_cloud_find_users_with_browse_permission', 'jira_cloud_get_all_users_default', 'jira_cloud_get_all_users"
        )


def register_jira_cloud_schema_field_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-field"})
    async def atlassian_jira_cloud_schema_field(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_custom_fields_configurations', 'jira_cloud_update_multiple_custom_field_values', 'jira_cloud_update_custom_field_value', 'jira_cloud_get_field_association_schemes', 'jira_cloud_create_field_association_scheme', 'jira_cloud_remove_fields_associated_with_schemes', 'jira_cloud_update_fields_associated_with_schemes', 'jira_cloud_delete_field_association_scheme', 'jira_cloud_get_field_association_scheme_by_id', 'jira_cloud_update_field_association_scheme', 'jira_cloud_clone_field_association_scheme', 'jira_cloud_search_field_association_scheme_fields', 'jira_cloud_get_field_association_scheme_item_parameters', 'jira_cloud_get_fields', 'jira_cloud_create_custom_field', 'jira_cloud_get_fields_paginated', 'jira_cloud_get_trashed_fields_paginated', 'jira_cloud_update_custom_field', 'jira_cloud_get_contexts_for_field', 'jira_cloud_get_contexts_for_field_deprecated', 'jira_cloud_delete_custom_field', 'jira_cloud_restore_custom_field', 'jira_cloud_trash_custom_field', 'jira_cloud_get_field_auto_complete_for_query_string'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema field operations.

        Actions:
          - 'jira_cloud_get_custom_fields_configurations': Call jira_cloud_get_custom_fields_configurations
          - 'jira_cloud_update_multiple_custom_field_values': Call jira_cloud_update_multiple_custom_field_values
          - 'jira_cloud_update_custom_field_value': Call jira_cloud_update_custom_field_value
          - 'jira_cloud_get_field_association_schemes': Call jira_cloud_get_field_association_schemes
          - 'jira_cloud_create_field_association_scheme': Call jira_cloud_create_field_association_scheme
          - 'jira_cloud_remove_fields_associated_with_schemes': Call jira_cloud_remove_fields_associated_with_schemes
          - 'jira_cloud_update_fields_associated_with_schemes': Call jira_cloud_update_fields_associated_with_schemes
          - 'jira_cloud_delete_field_association_scheme': Call jira_cloud_delete_field_association_scheme
          - 'jira_cloud_get_field_association_scheme_by_id': Call jira_cloud_get_field_association_scheme_by_id
          - 'jira_cloud_update_field_association_scheme': Call jira_cloud_update_field_association_scheme
          - 'jira_cloud_clone_field_association_scheme': Call jira_cloud_clone_field_association_scheme
          - 'jira_cloud_search_field_association_scheme_fields': Call jira_cloud_search_field_association_scheme_fields
          - 'jira_cloud_get_field_association_scheme_item_parameters': Call jira_cloud_get_field_association_scheme_item_parameters
          - 'jira_cloud_get_fields': Call jira_cloud_get_fields
          - 'jira_cloud_create_custom_field': Call jira_cloud_create_custom_field
          - 'jira_cloud_get_fields_paginated': Call jira_cloud_get_fields_paginated
          - 'jira_cloud_get_trashed_fields_paginated': Call jira_cloud_get_trashed_fields_paginated
          - 'jira_cloud_update_custom_field': Call jira_cloud_update_custom_field
          - 'jira_cloud_get_contexts_for_field': Call jira_cloud_get_contexts_for_field
          - 'jira_cloud_get_contexts_for_field_deprecated': Call jira_cloud_get_contexts_for_field_deprecated
          - 'jira_cloud_delete_custom_field': Call jira_cloud_delete_custom_field
          - 'jira_cloud_restore_custom_field': Call jira_cloud_restore_custom_field
          - 'jira_cloud_trash_custom_field': Call jira_cloud_trash_custom_field
          - 'jira_cloud_get_field_auto_complete_for_query_string': Call jira_cloud_get_field_auto_complete_for_query_string
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_custom_fields_configurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_custom_fields_configurations(**kwargs)
        if action == "jira_cloud_update_multiple_custom_field_values":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_multiple_custom_field_values(**kwargs)
        if action == "jira_cloud_update_custom_field_value":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_custom_field_value(**kwargs)
        if action == "jira_cloud_get_field_association_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_field_association_schemes(**kwargs)
        if action == "jira_cloud_create_field_association_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_field_association_scheme(**kwargs)
        if action == "jira_cloud_remove_fields_associated_with_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_fields_associated_with_schemes(**kwargs)
        if action == "jira_cloud_update_fields_associated_with_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_fields_associated_with_schemes(**kwargs)
        if action == "jira_cloud_delete_field_association_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_field_association_scheme(**kwargs)
        if action == "jira_cloud_get_field_association_scheme_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_field_association_scheme_by_id(**kwargs)
        if action == "jira_cloud_update_field_association_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_field_association_scheme(**kwargs)
        if action == "jira_cloud_clone_field_association_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_clone_field_association_scheme(**kwargs)
        if action == "jira_cloud_search_field_association_scheme_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_field_association_scheme_fields(**kwargs)
        if action == "jira_cloud_get_field_association_scheme_item_parameters":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_field_association_scheme_item_parameters(
                **kwargs
            )
        if action == "jira_cloud_get_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_fields(**kwargs)
        if action == "jira_cloud_create_custom_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_custom_field(**kwargs)
        if action == "jira_cloud_get_fields_paginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_fields_paginated(**kwargs)
        if action == "jira_cloud_get_trashed_fields_paginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_trashed_fields_paginated(**kwargs)
        if action == "jira_cloud_update_custom_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_custom_field(**kwargs)
        if action == "jira_cloud_get_contexts_for_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_contexts_for_field(**kwargs)
        if action == "jira_cloud_get_contexts_for_field_deprecated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_contexts_for_field_deprecated(**kwargs)
        if action == "jira_cloud_delete_custom_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_custom_field(**kwargs)
        if action == "jira_cloud_restore_custom_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_restore_custom_field(**kwargs)
        if action == "jira_cloud_trash_custom_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_trash_custom_field(**kwargs)
        if action == "jira_cloud_get_field_auto_complete_for_query_string":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_field_auto_complete_for_query_string(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_custom_fields_configurations', 'jira_cloud_update_multiple_custom_field_values', 'jira_cloud_update_custom_field_value', 'jira_cloud_get_field_association_schemes', 'jira_cloud_create_field_association_scheme', 'jira_cloud_remove_fields_associated_with_schemes', 'jira_cloud_update_fields_associated_with_schemes', 'jira_cloud_delete_field_association_scheme', 'jira_cloud_get_field_association_scheme_by_id', 'jira_cloud_update_field_association_scheme', 'jira_cloud_clone_field_association_scheme', 'jira_cloud_search_field_association_scheme_fields', 'jira_cloud_get_field_association_scheme_item_parameters', 'jira_cloud_get_fields', 'jira_cloud_create_custom_field', 'jira_cloud_get_fields_paginated', 'jira_cloud_get_trashed_fields_paginated', 'jira_cloud_update_custom_field', 'jira_cloud_get_contexts_for_field', 'jira_cloud_get_contexts_for_field_deprecated', 'jira_cloud_delete_custom_field', 'jira_cloud_restore_custom_field', 'jira_cloud_trash_custom_field', 'jira_cloud_get_field_auto_complete_for_query_string"
        )


def register_jira_cloud_schema_field_configuration_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-field-configuration"})
    async def atlassian_jira_cloud_schema_field_configuration(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_custom_field_configuration', 'jira_cloud_update_custom_field_configuration', 'jira_cloud_get_all_field_configurations', 'jira_cloud_create_field_configuration', 'jira_cloud_delete_field_configuration', 'jira_cloud_update_field_configuration', 'jira_cloud_get_field_configuration_items', 'jira_cloud_update_field_configuration_items'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema field configuration operations.

        Actions:
          - 'jira_cloud_get_custom_field_configuration': Call jira_cloud_get_custom_field_configuration
          - 'jira_cloud_update_custom_field_configuration': Call jira_cloud_update_custom_field_configuration
          - 'jira_cloud_get_all_field_configurations': Call jira_cloud_get_all_field_configurations
          - 'jira_cloud_create_field_configuration': Call jira_cloud_create_field_configuration
          - 'jira_cloud_delete_field_configuration': Call jira_cloud_delete_field_configuration
          - 'jira_cloud_update_field_configuration': Call jira_cloud_update_field_configuration
          - 'jira_cloud_get_field_configuration_items': Call jira_cloud_get_field_configuration_items
          - 'jira_cloud_update_field_configuration_items': Call jira_cloud_update_field_configuration_items
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_custom_field_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_custom_field_configuration(**kwargs)
        if action == "jira_cloud_update_custom_field_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_custom_field_configuration(**kwargs)
        if action == "jira_cloud_get_all_field_configurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_field_configurations(**kwargs)
        if action == "jira_cloud_create_field_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_field_configuration(**kwargs)
        if action == "jira_cloud_delete_field_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_field_configuration(**kwargs)
        if action == "jira_cloud_update_field_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_field_configuration(**kwargs)
        if action == "jira_cloud_get_field_configuration_items":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_field_configuration_items(**kwargs)
        if action == "jira_cloud_update_field_configuration_items":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_field_configuration_items(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_custom_field_configuration', 'jira_cloud_update_custom_field_configuration', 'jira_cloud_get_all_field_configurations', 'jira_cloud_create_field_configuration', 'jira_cloud_delete_field_configuration', 'jira_cloud_update_field_configuration', 'jira_cloud_get_field_configuration_items', 'jira_cloud_update_field_configuration_items"
        )


def register_jira_cloud_schema_field_option_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-field-option"})
    async def atlassian_jira_cloud_schema_field_option(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_custom_field_option', 'jira_cloud_create_custom_field_option', 'jira_cloud_update_custom_field_option', 'jira_cloud_reorder_custom_field_options', 'jira_cloud_delete_custom_field_option', 'jira_cloud_replace_custom_field_option'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema field option operations.

        Actions:
          - 'jira_cloud_get_custom_field_option': Call jira_cloud_get_custom_field_option
          - 'jira_cloud_create_custom_field_option': Call jira_cloud_create_custom_field_option
          - 'jira_cloud_update_custom_field_option': Call jira_cloud_update_custom_field_option
          - 'jira_cloud_reorder_custom_field_options': Call jira_cloud_reorder_custom_field_options
          - 'jira_cloud_delete_custom_field_option': Call jira_cloud_delete_custom_field_option
          - 'jira_cloud_replace_custom_field_option': Call jira_cloud_replace_custom_field_option
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_custom_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_custom_field_option(**kwargs)
        if action == "jira_cloud_create_custom_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_custom_field_option(**kwargs)
        if action == "jira_cloud_update_custom_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_custom_field_option(**kwargs)
        if action == "jira_cloud_reorder_custom_field_options":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_reorder_custom_field_options(**kwargs)
        if action == "jira_cloud_delete_custom_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_custom_field_option(**kwargs)
        if action == "jira_cloud_replace_custom_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_replace_custom_field_option(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_custom_field_option', 'jira_cloud_create_custom_field_option', 'jira_cloud_update_custom_field_option', 'jira_cloud_reorder_custom_field_options', 'jira_cloud_delete_custom_field_option', 'jira_cloud_replace_custom_field_option"
        )


def register_jira_cloud_schema_other_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-other"})
    async def atlassian_jira_cloud_schema_other(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_all_dashboards', 'jira_cloud_create_dashboard', 'jira_cloud_get_all_available_dashboard_gadgets', 'jira_cloud_get_dashboards_paginated', 'jira_cloud_get_dashboard_item_property_keys', 'jira_cloud_delete_dashboard_item_property', 'jira_cloud_get_dashboard_item_property', 'jira_cloud_set_dashboard_item_property', 'jira_cloud_delete_dashboard', 'jira_cloud_get_dashboard', 'jira_cloud_update_dashboard', 'jira_cloud_copy_dashboard', 'jira_cloud_search_security_schemes', 'jira_cloud_delete_security_scheme', 'jira_cloud_get_avatar_image_by_type', 'jira_cloud_update_schemes'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema other operations.

        Actions:
          - 'jira_cloud_get_all_dashboards': Call jira_cloud_get_all_dashboards
          - 'jira_cloud_create_dashboard': Call jira_cloud_create_dashboard
          - 'jira_cloud_get_all_available_dashboard_gadgets': Call jira_cloud_get_all_available_dashboard_gadgets
          - 'jira_cloud_get_dashboards_paginated': Call jira_cloud_get_dashboards_paginated
          - 'jira_cloud_get_dashboard_item_property_keys': Call jira_cloud_get_dashboard_item_property_keys
          - 'jira_cloud_delete_dashboard_item_property': Call jira_cloud_delete_dashboard_item_property
          - 'jira_cloud_get_dashboard_item_property': Call jira_cloud_get_dashboard_item_property
          - 'jira_cloud_set_dashboard_item_property': Call jira_cloud_set_dashboard_item_property
          - 'jira_cloud_delete_dashboard': Call jira_cloud_delete_dashboard
          - 'jira_cloud_get_dashboard': Call jira_cloud_get_dashboard
          - 'jira_cloud_update_dashboard': Call jira_cloud_update_dashboard
          - 'jira_cloud_copy_dashboard': Call jira_cloud_copy_dashboard
          - 'jira_cloud_search_security_schemes': Call jira_cloud_search_security_schemes
          - 'jira_cloud_delete_security_scheme': Call jira_cloud_delete_security_scheme
          - 'jira_cloud_get_avatar_image_by_type': Call jira_cloud_get_avatar_image_by_type
          - 'jira_cloud_update_schemes': Call jira_cloud_update_schemes
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_all_dashboards":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_dashboards(**kwargs)
        if action == "jira_cloud_create_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_dashboard(**kwargs)
        if action == "jira_cloud_get_all_available_dashboard_gadgets":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_available_dashboard_gadgets(**kwargs)
        if action == "jira_cloud_get_dashboards_paginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_dashboards_paginated(**kwargs)
        if action == "jira_cloud_get_dashboard_item_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_dashboard_item_property_keys(**kwargs)
        if action == "jira_cloud_delete_dashboard_item_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_dashboard_item_property(**kwargs)
        if action == "jira_cloud_get_dashboard_item_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_dashboard_item_property(**kwargs)
        if action == "jira_cloud_set_dashboard_item_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_dashboard_item_property(**kwargs)
        if action == "jira_cloud_delete_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_dashboard(**kwargs)
        if action == "jira_cloud_get_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_dashboard(**kwargs)
        if action == "jira_cloud_update_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_dashboard(**kwargs)
        if action == "jira_cloud_copy_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_copy_dashboard(**kwargs)
        if action == "jira_cloud_search_security_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_security_schemes(**kwargs)
        if action == "jira_cloud_delete_security_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_security_scheme(**kwargs)
        if action == "jira_cloud_get_avatar_image_by_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_avatar_image_by_type(**kwargs)
        if action == "jira_cloud_update_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_schemes(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_all_dashboards', 'jira_cloud_create_dashboard', 'jira_cloud_get_all_available_dashboard_gadgets', 'jira_cloud_get_dashboards_paginated', 'jira_cloud_get_dashboard_item_property_keys', 'jira_cloud_delete_dashboard_item_property', 'jira_cloud_get_dashboard_item_property', 'jira_cloud_set_dashboard_item_property', 'jira_cloud_delete_dashboard', 'jira_cloud_get_dashboard', 'jira_cloud_update_dashboard', 'jira_cloud_copy_dashboard', 'jira_cloud_search_security_schemes', 'jira_cloud_delete_security_scheme', 'jira_cloud_get_avatar_image_by_type', 'jira_cloud_update_schemes"
        )


def register_jira_cloud_schema_field_context_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-field-context"})
    async def atlassian_jira_cloud_schema_field_context(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_create_custom_field_context', 'jira_cloud_delete_custom_field_context', 'jira_cloud_update_custom_field_context'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema field context operations.

        Actions:
          - 'jira_cloud_create_custom_field_context': Call jira_cloud_create_custom_field_context
          - 'jira_cloud_delete_custom_field_context': Call jira_cloud_delete_custom_field_context
          - 'jira_cloud_update_custom_field_context': Call jira_cloud_update_custom_field_context
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_create_custom_field_context":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_custom_field_context(**kwargs)
        if action == "jira_cloud_delete_custom_field_context":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_custom_field_context(**kwargs)
        if action == "jira_cloud_update_custom_field_context":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_custom_field_context(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_create_custom_field_context', 'jira_cloud_delete_custom_field_context', 'jira_cloud_update_custom_field_context"
        )


def register_jira_cloud_schema_screen_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-screen"})
    async def atlassian_jira_cloud_schema_screen(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_screens_for_field', 'jira_cloud_get_screens', 'jira_cloud_create_screen', 'jira_cloud_add_field_to_default_screen', 'jira_cloud_delete_screen', 'jira_cloud_update_screen', 'jira_cloud_get_available_screen_fields'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema screen operations.

        Actions:
          - 'jira_cloud_get_screens_for_field': Call jira_cloud_get_screens_for_field
          - 'jira_cloud_get_screens': Call jira_cloud_get_screens
          - 'jira_cloud_create_screen': Call jira_cloud_create_screen
          - 'jira_cloud_add_field_to_default_screen': Call jira_cloud_add_field_to_default_screen
          - 'jira_cloud_delete_screen': Call jira_cloud_delete_screen
          - 'jira_cloud_update_screen': Call jira_cloud_update_screen
          - 'jira_cloud_get_available_screen_fields': Call jira_cloud_get_available_screen_fields
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_screens_for_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_screens_for_field(**kwargs)
        if action == "jira_cloud_get_screens":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_screens(**kwargs)
        if action == "jira_cloud_create_screen":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_screen(**kwargs)
        if action == "jira_cloud_add_field_to_default_screen":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_field_to_default_screen(**kwargs)
        if action == "jira_cloud_delete_screen":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_screen(**kwargs)
        if action == "jira_cloud_update_screen":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_screen(**kwargs)
        if action == "jira_cloud_get_available_screen_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_available_screen_fields(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_screens_for_field', 'jira_cloud_get_screens', 'jira_cloud_create_screen', 'jira_cloud_add_field_to_default_screen', 'jira_cloud_delete_screen', 'jira_cloud_update_screen', 'jira_cloud_get_available_screen_fields"
        )


def register_jira_cloud_schema_field_configuration_scheme_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-field-configuration-scheme"})
    async def atlassian_jira_cloud_schema_field_configuration_scheme(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_all_field_configuration_schemes', 'jira_cloud_create_field_configuration_scheme', 'jira_cloud_get_field_configuration_scheme_mappings', 'jira_cloud_delete_field_configuration_scheme', 'jira_cloud_update_field_configuration_scheme', 'jira_cloud_set_field_configuration_scheme_mapping'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema field configuration scheme operations.

        Actions:
          - 'jira_cloud_get_all_field_configuration_schemes': Call jira_cloud_get_all_field_configuration_schemes
          - 'jira_cloud_create_field_configuration_scheme': Call jira_cloud_create_field_configuration_scheme
          - 'jira_cloud_get_field_configuration_scheme_mappings': Call jira_cloud_get_field_configuration_scheme_mappings
          - 'jira_cloud_delete_field_configuration_scheme': Call jira_cloud_delete_field_configuration_scheme
          - 'jira_cloud_update_field_configuration_scheme': Call jira_cloud_update_field_configuration_scheme
          - 'jira_cloud_set_field_configuration_scheme_mapping': Call jira_cloud_set_field_configuration_scheme_mapping
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_all_field_configuration_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_field_configuration_schemes(**kwargs)
        if action == "jira_cloud_create_field_configuration_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_field_configuration_scheme(**kwargs)
        if action == "jira_cloud_get_field_configuration_scheme_mappings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_field_configuration_scheme_mappings(**kwargs)
        if action == "jira_cloud_delete_field_configuration_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_field_configuration_scheme(**kwargs)
        if action == "jira_cloud_update_field_configuration_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_field_configuration_scheme(**kwargs)
        if action == "jira_cloud_set_field_configuration_scheme_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_field_configuration_scheme_mapping(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_all_field_configuration_schemes', 'jira_cloud_create_field_configuration_scheme', 'jira_cloud_get_field_configuration_scheme_mappings', 'jira_cloud_delete_field_configuration_scheme', 'jira_cloud_update_field_configuration_scheme', 'jira_cloud_set_field_configuration_scheme_mapping"
        )


def register_jira_cloud_schema_screen_scheme_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-screen-scheme"})
    async def atlassian_jira_cloud_schema_screen_scheme(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_update_default_screen_scheme', 'jira_cloud_get_screen_schemes', 'jira_cloud_create_screen_scheme', 'jira_cloud_delete_screen_scheme', 'jira_cloud_update_screen_scheme'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema screen scheme operations.

        Actions:
          - 'jira_cloud_update_default_screen_scheme': Call jira_cloud_update_default_screen_scheme
          - 'jira_cloud_get_screen_schemes': Call jira_cloud_get_screen_schemes
          - 'jira_cloud_create_screen_scheme': Call jira_cloud_create_screen_scheme
          - 'jira_cloud_delete_screen_scheme': Call jira_cloud_delete_screen_scheme
          - 'jira_cloud_update_screen_scheme': Call jira_cloud_update_screen_scheme
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_update_default_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_default_screen_scheme(**kwargs)
        if action == "jira_cloud_get_screen_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_screen_schemes(**kwargs)
        if action == "jira_cloud_create_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_screen_scheme(**kwargs)
        if action == "jira_cloud_delete_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_screen_scheme(**kwargs)
        if action == "jira_cloud_update_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_screen_scheme(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_update_default_screen_scheme', 'jira_cloud_get_screen_schemes', 'jira_cloud_create_screen_scheme', 'jira_cloud_delete_screen_scheme', 'jira_cloud_update_screen_scheme"
        )


def register_jira_cloud_schema_notification_scheme_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-notification-scheme"})
    async def atlassian_jira_cloud_schema_notification_scheme(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_notification_schemes', 'jira_cloud_create_notification_scheme', 'jira_cloud_get_notification_scheme', 'jira_cloud_update_notification_scheme', 'jira_cloud_delete_notification_scheme', 'jira_cloud_remove_notification_from_notification_scheme'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema notification scheme operations.

        Actions:
          - 'jira_cloud_get_notification_schemes': Call jira_cloud_get_notification_schemes
          - 'jira_cloud_create_notification_scheme': Call jira_cloud_create_notification_scheme
          - 'jira_cloud_get_notification_scheme': Call jira_cloud_get_notification_scheme
          - 'jira_cloud_update_notification_scheme': Call jira_cloud_update_notification_scheme
          - 'jira_cloud_delete_notification_scheme': Call jira_cloud_delete_notification_scheme
          - 'jira_cloud_remove_notification_from_notification_scheme': Call jira_cloud_remove_notification_from_notification_scheme
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_notification_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_notification_schemes(**kwargs)
        if action == "jira_cloud_create_notification_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_notification_scheme(**kwargs)
        if action == "jira_cloud_get_notification_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_notification_scheme(**kwargs)
        if action == "jira_cloud_update_notification_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_notification_scheme(**kwargs)
        if action == "jira_cloud_delete_notification_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_notification_scheme(**kwargs)
        if action == "jira_cloud_remove_notification_from_notification_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_notification_from_notification_scheme(
                **kwargs
            )
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_notification_schemes', 'jira_cloud_create_notification_scheme', 'jira_cloud_get_notification_scheme', 'jira_cloud_update_notification_scheme', 'jira_cloud_delete_notification_scheme', 'jira_cloud_remove_notification_from_notification_scheme"
        )


def register_jira_cloud_schema_priority_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-priority"})
    async def atlassian_jira_cloud_schema_priority(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_create_priority', 'jira_cloud_set_default_priority', 'jira_cloud_delete_priority', 'jira_cloud_get_priority', 'jira_cloud_update_priority'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema priority operations.

        Actions:
          - 'jira_cloud_create_priority': Call jira_cloud_create_priority
          - 'jira_cloud_set_default_priority': Call jira_cloud_set_default_priority
          - 'jira_cloud_delete_priority': Call jira_cloud_delete_priority
          - 'jira_cloud_get_priority': Call jira_cloud_get_priority
          - 'jira_cloud_update_priority': Call jira_cloud_update_priority
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_create_priority":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_priority(**kwargs)
        if action == "jira_cloud_set_default_priority":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_default_priority(**kwargs)
        if action == "jira_cloud_delete_priority":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_priority(**kwargs)
        if action == "jira_cloud_get_priority":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_priority(**kwargs)
        if action == "jira_cloud_update_priority":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_priority(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_create_priority', 'jira_cloud_set_default_priority', 'jira_cloud_delete_priority', 'jira_cloud_get_priority', 'jira_cloud_update_priority"
        )


def register_jira_cloud_schema_priority_scheme_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-priority-scheme"})
    async def atlassian_jira_cloud_schema_priority_scheme(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_priority_schemes', 'jira_cloud_create_priority_scheme', 'jira_cloud_get_available_priorities_by_priority_scheme', 'jira_cloud_delete_priority_scheme', 'jira_cloud_update_priority_scheme', 'jira_cloud_get_priorities_by_priority_scheme'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema priority scheme operations.

        Actions:
          - 'jira_cloud_get_priority_schemes': Call jira_cloud_get_priority_schemes
          - 'jira_cloud_create_priority_scheme': Call jira_cloud_create_priority_scheme
          - 'jira_cloud_get_available_priorities_by_priority_scheme': Call jira_cloud_get_available_priorities_by_priority_scheme
          - 'jira_cloud_delete_priority_scheme': Call jira_cloud_delete_priority_scheme
          - 'jira_cloud_update_priority_scheme': Call jira_cloud_update_priority_scheme
          - 'jira_cloud_get_priorities_by_priority_scheme': Call jira_cloud_get_priorities_by_priority_scheme
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_priority_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_priority_schemes(**kwargs)
        if action == "jira_cloud_create_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_priority_scheme(**kwargs)
        if action == "jira_cloud_get_available_priorities_by_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_available_priorities_by_priority_scheme(
                **kwargs
            )
        if action == "jira_cloud_delete_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_priority_scheme(**kwargs)
        if action == "jira_cloud_update_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_priority_scheme(**kwargs)
        if action == "jira_cloud_get_priorities_by_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_priorities_by_priority_scheme(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_priority_schemes', 'jira_cloud_create_priority_scheme', 'jira_cloud_get_available_priorities_by_priority_scheme', 'jira_cloud_delete_priority_scheme', 'jira_cloud_update_priority_scheme', 'jira_cloud_get_priorities_by_priority_scheme"
        )


def register_jira_cloud_schema_status_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-status"})
    async def atlassian_jira_cloud_schema_status(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_all_statuses', 'jira_cloud_get_redaction_status', 'jira_cloud_get_statuses', 'jira_cloud_get_status', 'jira_cloud_get_status_categories', 'jira_cloud_get_status_category', 'jira_cloud_delete_statuses_by_id', 'jira_cloud_get_statuses_by_id', 'jira_cloud_create_statuses', 'jira_cloud_update_statuses', 'jira_cloud_get_statuses_by_name'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema status operations.

        Actions:
          - 'jira_cloud_get_all_statuses': Call jira_cloud_get_all_statuses
          - 'jira_cloud_get_redaction_status': Call jira_cloud_get_redaction_status
          - 'jira_cloud_get_statuses': Call jira_cloud_get_statuses
          - 'jira_cloud_get_status': Call jira_cloud_get_status
          - 'jira_cloud_get_status_categories': Call jira_cloud_get_status_categories
          - 'jira_cloud_get_status_category': Call jira_cloud_get_status_category
          - 'jira_cloud_delete_statuses_by_id': Call jira_cloud_delete_statuses_by_id
          - 'jira_cloud_get_statuses_by_id': Call jira_cloud_get_statuses_by_id
          - 'jira_cloud_create_statuses': Call jira_cloud_create_statuses
          - 'jira_cloud_update_statuses': Call jira_cloud_update_statuses
          - 'jira_cloud_get_statuses_by_name': Call jira_cloud_get_statuses_by_name
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_all_statuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_statuses(**kwargs)
        if action == "jira_cloud_get_redaction_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_redaction_status(**kwargs)
        if action == "jira_cloud_get_statuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_statuses(**kwargs)
        if action == "jira_cloud_get_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_status(**kwargs)
        if action == "jira_cloud_get_status_categories":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_status_categories(**kwargs)
        if action == "jira_cloud_get_status_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_status_category(**kwargs)
        if action == "jira_cloud_delete_statuses_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_statuses_by_id(**kwargs)
        if action == "jira_cloud_get_statuses_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_statuses_by_id(**kwargs)
        if action == "jira_cloud_create_statuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_statuses(**kwargs)
        if action == "jira_cloud_update_statuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_statuses(**kwargs)
        if action == "jira_cloud_get_statuses_by_name":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_statuses_by_name(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_all_statuses', 'jira_cloud_get_redaction_status', 'jira_cloud_get_statuses', 'jira_cloud_get_status', 'jira_cloud_get_status_categories', 'jira_cloud_get_status_category', 'jira_cloud_delete_statuses_by_id', 'jira_cloud_get_statuses_by_id', 'jira_cloud_create_statuses', 'jira_cloud_update_statuses', 'jira_cloud_get_statuses_by_name"
        )


def register_jira_cloud_schema_resolution_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-resolution"})
    async def atlassian_jira_cloud_schema_resolution(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_resolutions', 'jira_cloud_create_resolution', 'jira_cloud_set_default_resolution', 'jira_cloud_move_resolutions', 'jira_cloud_search_resolutions', 'jira_cloud_delete_resolution', 'jira_cloud_get_resolution', 'jira_cloud_update_resolution'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema resolution operations.

        Actions:
          - 'jira_cloud_get_resolutions': Call jira_cloud_get_resolutions
          - 'jira_cloud_create_resolution': Call jira_cloud_create_resolution
          - 'jira_cloud_set_default_resolution': Call jira_cloud_set_default_resolution
          - 'jira_cloud_move_resolutions': Call jira_cloud_move_resolutions
          - 'jira_cloud_search_resolutions': Call jira_cloud_search_resolutions
          - 'jira_cloud_delete_resolution': Call jira_cloud_delete_resolution
          - 'jira_cloud_get_resolution': Call jira_cloud_get_resolution
          - 'jira_cloud_update_resolution': Call jira_cloud_update_resolution
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_resolutions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_resolutions(**kwargs)
        if action == "jira_cloud_create_resolution":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_resolution(**kwargs)
        if action == "jira_cloud_set_default_resolution":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_default_resolution(**kwargs)
        if action == "jira_cloud_move_resolutions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_move_resolutions(**kwargs)
        if action == "jira_cloud_search_resolutions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_resolutions(**kwargs)
        if action == "jira_cloud_delete_resolution":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_resolution(**kwargs)
        if action == "jira_cloud_get_resolution":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_resolution(**kwargs)
        if action == "jira_cloud_update_resolution":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_resolution(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_resolutions', 'jira_cloud_create_resolution', 'jira_cloud_set_default_resolution', 'jira_cloud_move_resolutions', 'jira_cloud_search_resolutions', 'jira_cloud_delete_resolution', 'jira_cloud_get_resolution', 'jira_cloud_update_resolution"
        )


def register_jira_cloud_schema_screen_tab_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-screen-tab"})
    async def atlassian_jira_cloud_schema_screen_tab(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_all_screen_tabs', 'jira_cloud_add_screen_tab', 'jira_cloud_delete_screen_tab', 'jira_cloud_rename_screen_tab', 'jira_cloud_move_screen_tab'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema screen tab operations.

        Actions:
          - 'jira_cloud_get_all_screen_tabs': Call jira_cloud_get_all_screen_tabs
          - 'jira_cloud_add_screen_tab': Call jira_cloud_add_screen_tab
          - 'jira_cloud_delete_screen_tab': Call jira_cloud_delete_screen_tab
          - 'jira_cloud_rename_screen_tab': Call jira_cloud_rename_screen_tab
          - 'jira_cloud_move_screen_tab': Call jira_cloud_move_screen_tab
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_all_screen_tabs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_screen_tabs(**kwargs)
        if action == "jira_cloud_add_screen_tab":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_screen_tab(**kwargs)
        if action == "jira_cloud_delete_screen_tab":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_screen_tab(**kwargs)
        if action == "jira_cloud_rename_screen_tab":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_rename_screen_tab(**kwargs)
        if action == "jira_cloud_move_screen_tab":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_move_screen_tab(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_all_screen_tabs', 'jira_cloud_add_screen_tab', 'jira_cloud_delete_screen_tab', 'jira_cloud_rename_screen_tab', 'jira_cloud_move_screen_tab"
        )


def register_jira_cloud_schema_screen_tab_field_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-screen-tab-field"})
    async def atlassian_jira_cloud_schema_screen_tab_field(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_all_screen_tab_fields', 'jira_cloud_add_screen_tab_field', 'jira_cloud_remove_screen_tab_field', 'jira_cloud_move_screen_tab_field'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema screen tab field operations.

        Actions:
          - 'jira_cloud_get_all_screen_tab_fields': Call jira_cloud_get_all_screen_tab_fields
          - 'jira_cloud_add_screen_tab_field': Call jira_cloud_add_screen_tab_field
          - 'jira_cloud_remove_screen_tab_field': Call jira_cloud_remove_screen_tab_field
          - 'jira_cloud_move_screen_tab_field': Call jira_cloud_move_screen_tab_field
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_all_screen_tab_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_screen_tab_fields(**kwargs)
        if action == "jira_cloud_add_screen_tab_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_screen_tab_field(**kwargs)
        if action == "jira_cloud_remove_screen_tab_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_screen_tab_field(**kwargs)
        if action == "jira_cloud_move_screen_tab_field":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_move_screen_tab_field(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_all_screen_tab_fields', 'jira_cloud_add_screen_tab_field', 'jira_cloud_remove_screen_tab_field', 'jira_cloud_move_screen_tab_field"
        )


def register_jira_cloud_schema_workflow_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-workflow"})
    async def atlassian_jira_cloud_schema_workflow(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_workflow_usages_for_status', 'jira_cloud_get_all_workflows', 'jira_cloud_create_workflow', 'jira_cloud_read_workflow_from_history', 'jira_cloud_list_workflow_history', 'jira_cloud_get_workflows_paginated', 'jira_cloud_delete_inactive_workflow', 'jira_cloud_read_workflows', 'jira_cloud_workflow_capabilities', 'jira_cloud_create_workflows', 'jira_cloud_validate_create_workflows', 'jira_cloud_read_workflow_previews', 'jira_cloud_search_workflows', 'jira_cloud_update_workflows', 'jira_cloud_validate_update_workflows', 'jira_cloud_delete_default_workflow', 'jira_cloud_get_default_workflow', 'jira_cloud_update_default_workflow', 'jira_cloud_delete_draft_default_workflow', 'jira_cloud_get_draft_default_workflow', 'jira_cloud_update_draft_default_workflow', 'jira_cloud_delete_draft_workflow_mapping', 'jira_cloud_get_draft_workflow', 'jira_cloud_update_draft_workflow_mapping', 'jira_cloud_delete_workflow_mapping', 'jira_cloud_get_workflow', 'jira_cloud_update_workflow_mapping'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema workflow operations.

        Actions:
          - 'jira_cloud_get_workflow_usages_for_status': Call jira_cloud_get_workflow_usages_for_status
          - 'jira_cloud_get_all_workflows': Call jira_cloud_get_all_workflows
          - 'jira_cloud_create_workflow': Call jira_cloud_create_workflow
          - 'jira_cloud_read_workflow_from_history': Call jira_cloud_read_workflow_from_history
          - 'jira_cloud_list_workflow_history': Call jira_cloud_list_workflow_history
          - 'jira_cloud_get_workflows_paginated': Call jira_cloud_get_workflows_paginated
          - 'jira_cloud_delete_inactive_workflow': Call jira_cloud_delete_inactive_workflow
          - 'jira_cloud_read_workflows': Call jira_cloud_read_workflows
          - 'jira_cloud_workflow_capabilities': Call jira_cloud_workflow_capabilities
          - 'jira_cloud_create_workflows': Call jira_cloud_create_workflows
          - 'jira_cloud_validate_create_workflows': Call jira_cloud_validate_create_workflows
          - 'jira_cloud_read_workflow_previews': Call jira_cloud_read_workflow_previews
          - 'jira_cloud_search_workflows': Call jira_cloud_search_workflows
          - 'jira_cloud_update_workflows': Call jira_cloud_update_workflows
          - 'jira_cloud_validate_update_workflows': Call jira_cloud_validate_update_workflows
          - 'jira_cloud_delete_default_workflow': Call jira_cloud_delete_default_workflow
          - 'jira_cloud_get_default_workflow': Call jira_cloud_get_default_workflow
          - 'jira_cloud_update_default_workflow': Call jira_cloud_update_default_workflow
          - 'jira_cloud_delete_draft_default_workflow': Call jira_cloud_delete_draft_default_workflow
          - 'jira_cloud_get_draft_default_workflow': Call jira_cloud_get_draft_default_workflow
          - 'jira_cloud_update_draft_default_workflow': Call jira_cloud_update_draft_default_workflow
          - 'jira_cloud_delete_draft_workflow_mapping': Call jira_cloud_delete_draft_workflow_mapping
          - 'jira_cloud_get_draft_workflow': Call jira_cloud_get_draft_workflow
          - 'jira_cloud_update_draft_workflow_mapping': Call jira_cloud_update_draft_workflow_mapping
          - 'jira_cloud_delete_workflow_mapping': Call jira_cloud_delete_workflow_mapping
          - 'jira_cloud_get_workflow': Call jira_cloud_get_workflow
          - 'jira_cloud_update_workflow_mapping': Call jira_cloud_update_workflow_mapping
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_workflow_usages_for_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_usages_for_status(**kwargs)
        if action == "jira_cloud_get_all_workflows":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_workflows(**kwargs)
        if action == "jira_cloud_create_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_workflow(**kwargs)
        if action == "jira_cloud_read_workflow_from_history":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_read_workflow_from_history(**kwargs)
        if action == "jira_cloud_list_workflow_history":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_list_workflow_history(**kwargs)
        if action == "jira_cloud_get_workflows_paginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflows_paginated(**kwargs)
        if action == "jira_cloud_delete_inactive_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_inactive_workflow(**kwargs)
        if action == "jira_cloud_read_workflows":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_read_workflows(**kwargs)
        if action == "jira_cloud_workflow_capabilities":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_workflow_capabilities(**kwargs)
        if action == "jira_cloud_create_workflows":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_workflows(**kwargs)
        if action == "jira_cloud_validate_create_workflows":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_validate_create_workflows(**kwargs)
        if action == "jira_cloud_read_workflow_previews":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_read_workflow_previews(**kwargs)
        if action == "jira_cloud_search_workflows":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_workflows(**kwargs)
        if action == "jira_cloud_update_workflows":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_workflows(**kwargs)
        if action == "jira_cloud_validate_update_workflows":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_validate_update_workflows(**kwargs)
        if action == "jira_cloud_delete_default_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_default_workflow(**kwargs)
        if action == "jira_cloud_get_default_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_default_workflow(**kwargs)
        if action == "jira_cloud_update_default_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_default_workflow(**kwargs)
        if action == "jira_cloud_delete_draft_default_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_draft_default_workflow(**kwargs)
        if action == "jira_cloud_get_draft_default_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_draft_default_workflow(**kwargs)
        if action == "jira_cloud_update_draft_default_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_draft_default_workflow(**kwargs)
        if action == "jira_cloud_delete_draft_workflow_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_draft_workflow_mapping(**kwargs)
        if action == "jira_cloud_get_draft_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_draft_workflow(**kwargs)
        if action == "jira_cloud_update_draft_workflow_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_draft_workflow_mapping(**kwargs)
        if action == "jira_cloud_delete_workflow_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_workflow_mapping(**kwargs)
        if action == "jira_cloud_get_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow(**kwargs)
        if action == "jira_cloud_update_workflow_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_workflow_mapping(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_workflow_usages_for_status', 'jira_cloud_get_all_workflows', 'jira_cloud_create_workflow', 'jira_cloud_read_workflow_from_history', 'jira_cloud_list_workflow_history', 'jira_cloud_get_workflows_paginated', 'jira_cloud_delete_inactive_workflow', 'jira_cloud_read_workflows', 'jira_cloud_workflow_capabilities', 'jira_cloud_create_workflows', 'jira_cloud_validate_create_workflows', 'jira_cloud_read_workflow_previews', 'jira_cloud_search_workflows', 'jira_cloud_update_workflows', 'jira_cloud_validate_update_workflows', 'jira_cloud_delete_default_workflow', 'jira_cloud_get_default_workflow', 'jira_cloud_update_default_workflow', 'jira_cloud_delete_draft_default_workflow', 'jira_cloud_get_draft_default_workflow', 'jira_cloud_update_draft_default_workflow', 'jira_cloud_delete_draft_workflow_mapping', 'jira_cloud_get_draft_workflow', 'jira_cloud_update_draft_workflow_mapping', 'jira_cloud_delete_workflow_mapping', 'jira_cloud_get_workflow', 'jira_cloud_update_workflow_mapping"
        )


def register_jira_cloud_schema_workflow_scheme_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-workflow-scheme"})
    async def atlassian_jira_cloud_schema_workflow_scheme(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_workflow_scheme_usages_for_workflow', 'jira_cloud_get_all_workflow_schemes', 'jira_cloud_create_workflow_scheme', 'jira_cloud_read_workflow_schemes', 'jira_cloud_get_required_workflow_scheme_mappings', 'jira_cloud_delete_workflow_scheme', 'jira_cloud_get_workflow_scheme', 'jira_cloud_update_workflow_scheme', 'jira_cloud_create_workflow_scheme_draft_from_parent', 'jira_cloud_delete_workflow_scheme_draft', 'jira_cloud_get_workflow_scheme_draft', 'jira_cloud_update_workflow_scheme_draft', 'jira_cloud_publish_draft_workflow_scheme'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema workflow scheme operations.

        Actions:
          - 'jira_cloud_get_workflow_scheme_usages_for_workflow': Call jira_cloud_get_workflow_scheme_usages_for_workflow
          - 'jira_cloud_get_all_workflow_schemes': Call jira_cloud_get_all_workflow_schemes
          - 'jira_cloud_create_workflow_scheme': Call jira_cloud_create_workflow_scheme
          - 'jira_cloud_read_workflow_schemes': Call jira_cloud_read_workflow_schemes
          - 'jira_cloud_get_required_workflow_scheme_mappings': Call jira_cloud_get_required_workflow_scheme_mappings
          - 'jira_cloud_delete_workflow_scheme': Call jira_cloud_delete_workflow_scheme
          - 'jira_cloud_get_workflow_scheme': Call jira_cloud_get_workflow_scheme
          - 'jira_cloud_update_workflow_scheme': Call jira_cloud_update_workflow_scheme
          - 'jira_cloud_create_workflow_scheme_draft_from_parent': Call jira_cloud_create_workflow_scheme_draft_from_parent
          - 'jira_cloud_delete_workflow_scheme_draft': Call jira_cloud_delete_workflow_scheme_draft
          - 'jira_cloud_get_workflow_scheme_draft': Call jira_cloud_get_workflow_scheme_draft
          - 'jira_cloud_update_workflow_scheme_draft': Call jira_cloud_update_workflow_scheme_draft
          - 'jira_cloud_publish_draft_workflow_scheme': Call jira_cloud_publish_draft_workflow_scheme
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_workflow_scheme_usages_for_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_scheme_usages_for_workflow(**kwargs)
        if action == "jira_cloud_get_all_workflow_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_workflow_schemes(**kwargs)
        if action == "jira_cloud_create_workflow_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_workflow_scheme(**kwargs)
        if action == "jira_cloud_read_workflow_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_read_workflow_schemes(**kwargs)
        if action == "jira_cloud_get_required_workflow_scheme_mappings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_required_workflow_scheme_mappings(**kwargs)
        if action == "jira_cloud_delete_workflow_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_workflow_scheme(**kwargs)
        if action == "jira_cloud_get_workflow_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_scheme(**kwargs)
        if action == "jira_cloud_update_workflow_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_workflow_scheme(**kwargs)
        if action == "jira_cloud_create_workflow_scheme_draft_from_parent":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_workflow_scheme_draft_from_parent(**kwargs)
        if action == "jira_cloud_delete_workflow_scheme_draft":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_workflow_scheme_draft(**kwargs)
        if action == "jira_cloud_get_workflow_scheme_draft":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_scheme_draft(**kwargs)
        if action == "jira_cloud_update_workflow_scheme_draft":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_workflow_scheme_draft(**kwargs)
        if action == "jira_cloud_publish_draft_workflow_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_publish_draft_workflow_scheme(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_workflow_scheme_usages_for_workflow', 'jira_cloud_get_all_workflow_schemes', 'jira_cloud_create_workflow_scheme', 'jira_cloud_read_workflow_schemes', 'jira_cloud_get_required_workflow_scheme_mappings', 'jira_cloud_delete_workflow_scheme', 'jira_cloud_get_workflow_scheme', 'jira_cloud_update_workflow_scheme', 'jira_cloud_create_workflow_scheme_draft_from_parent', 'jira_cloud_delete_workflow_scheme_draft', 'jira_cloud_get_workflow_scheme_draft', 'jira_cloud_update_workflow_scheme_draft', 'jira_cloud_publish_draft_workflow_scheme"
        )


def register_jira_cloud_schema_workflow_rule_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-schema-workflow-rule"})
    async def atlassian_jira_cloud_schema_workflow_rule(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_migration_resource_workflow_rule_search_post'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud schema workflow rule operations.

        Actions:
          - 'jira_cloud_migration_resource_workflow_rule_search_post': Call jira_cloud_migration_resource_workflow_rule_search_post
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_migration_resource_workflow_rule_search_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_migration_resource_workflow_rule_search_post(
                **kwargs
            )
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_migration_resource_workflow_rule_search_post"
        )


def register_jira_cloud_core_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-core"})
    async def atlassian_jira_cloud_core(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_banner', 'jira_cloud_set_banner', 'jira_cloud_get_application_property', 'jira_cloud_get_advanced_settings', 'jira_cloud_set_application_property', 'jira_cloud_get_audit_records', 'jira_cloud_get_all_system_avatars', 'jira_cloud_get_configuration', 'jira_cloud_get_shared_time_tracking_configuration', 'jira_cloud_set_shared_time_tracking_configuration', 'jira_cloud_get_avatars', 'jira_cloud_store_avatar', 'jira_cloud_delete_avatar', 'jira_cloud_get_avatar_image_by_id', 'jira_cloud_get_avatar_image_by_owner', 'jira_cloud_get_forge_app_property_keys', 'jira_cloud_delete_forge_app_property', 'jira_cloud_get_forge_app_property', 'jira_cloud_put_forge_app_property'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud core operations.

        Actions:
          - 'jira_cloud_get_banner': Call jira_cloud_get_banner
          - 'jira_cloud_set_banner': Call jira_cloud_set_banner
          - 'jira_cloud_get_application_property': Call jira_cloud_get_application_property
          - 'jira_cloud_get_advanced_settings': Call jira_cloud_get_advanced_settings
          - 'jira_cloud_set_application_property': Call jira_cloud_set_application_property
          - 'jira_cloud_get_audit_records': Call jira_cloud_get_audit_records
          - 'jira_cloud_get_all_system_avatars': Call jira_cloud_get_all_system_avatars
          - 'jira_cloud_get_configuration': Call jira_cloud_get_configuration
          - 'jira_cloud_get_shared_time_tracking_configuration': Call jira_cloud_get_shared_time_tracking_configuration
          - 'jira_cloud_set_shared_time_tracking_configuration': Call jira_cloud_set_shared_time_tracking_configuration
          - 'jira_cloud_get_avatars': Call jira_cloud_get_avatars
          - 'jira_cloud_store_avatar': Call jira_cloud_store_avatar
          - 'jira_cloud_delete_avatar': Call jira_cloud_delete_avatar
          - 'jira_cloud_get_avatar_image_by_id': Call jira_cloud_get_avatar_image_by_id
          - 'jira_cloud_get_avatar_image_by_owner': Call jira_cloud_get_avatar_image_by_owner
          - 'jira_cloud_get_forge_app_property_keys': Call jira_cloud_get_forge_app_property_keys
          - 'jira_cloud_delete_forge_app_property': Call jira_cloud_delete_forge_app_property
          - 'jira_cloud_get_forge_app_property': Call jira_cloud_get_forge_app_property
          - 'jira_cloud_put_forge_app_property': Call jira_cloud_put_forge_app_property
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_banner":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_banner(**kwargs)
        if action == "jira_cloud_set_banner":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_banner(**kwargs)
        if action == "jira_cloud_get_application_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_application_property(**kwargs)
        if action == "jira_cloud_get_advanced_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_advanced_settings(**kwargs)
        if action == "jira_cloud_set_application_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_application_property(**kwargs)
        if action == "jira_cloud_get_audit_records":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_audit_records(**kwargs)
        if action == "jira_cloud_get_all_system_avatars":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_system_avatars(**kwargs)
        if action == "jira_cloud_get_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_configuration(**kwargs)
        if action == "jira_cloud_get_shared_time_tracking_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_shared_time_tracking_configuration(**kwargs)
        if action == "jira_cloud_set_shared_time_tracking_configuration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_shared_time_tracking_configuration(**kwargs)
        if action == "jira_cloud_get_avatars":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_avatars(**kwargs)
        if action == "jira_cloud_store_avatar":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_store_avatar(**kwargs)
        if action == "jira_cloud_delete_avatar":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_avatar(**kwargs)
        if action == "jira_cloud_get_avatar_image_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_avatar_image_by_id(**kwargs)
        if action == "jira_cloud_get_avatar_image_by_owner":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_avatar_image_by_owner(**kwargs)
        if action == "jira_cloud_get_forge_app_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_forge_app_property_keys(**kwargs)
        if action == "jira_cloud_delete_forge_app_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_forge_app_property(**kwargs)
        if action == "jira_cloud_get_forge_app_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_forge_app_property(**kwargs)
        if action == "jira_cloud_put_forge_app_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_put_forge_app_property(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_banner', 'jira_cloud_set_banner', 'jira_cloud_get_application_property', 'jira_cloud_get_advanced_settings', 'jira_cloud_set_application_property', 'jira_cloud_get_audit_records', 'jira_cloud_get_all_system_avatars', 'jira_cloud_get_configuration', 'jira_cloud_get_shared_time_tracking_configuration', 'jira_cloud_set_shared_time_tracking_configuration', 'jira_cloud_get_avatars', 'jira_cloud_store_avatar', 'jira_cloud_delete_avatar', 'jira_cloud_get_avatar_image_by_id', 'jira_cloud_get_avatar_image_by_owner', 'jira_cloud_get_forge_app_property_keys', 'jira_cloud_delete_forge_app_property', 'jira_cloud_get_forge_app_property', 'jira_cloud_put_forge_app_property"
        )


def register_jira_cloud_project_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-project"})
    async def atlassian_jira_cloud_project(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_find_components_for_projects', 'jira_cloud_create_component', 'jira_cloud_delete_component', 'jira_cloud_get_component', 'jira_cloud_update_component', 'jira_cloud_get_projects_with_field_schemes', 'jira_cloud_search_field_association_scheme_projects', 'jira_cloud_get_field_project_associations', 'jira_cloud_get_project_context_mapping', 'jira_cloud_assign_projects_to_custom_field_context', 'jira_cloud_remove_custom_field_context_from_projects', 'jira_cloud_assign_field_configuration_scheme_to_project', 'jira_cloud_search_projects_using_security_schemes', 'jira_cloud_associate_schemes_to_projects', 'jira_cloud_get_notification_scheme_to_project_mappings', 'jira_cloud_get_permitted_projects', 'jira_cloud_get_projects_by_priority_scheme', 'jira_cloud_get_all_projects', 'jira_cloud_create_project', 'jira_cloud_create_project_with_custom_template', 'jira_cloud_search_projects', 'jira_cloud_get_all_project_types', 'jira_cloud_get_all_accessible_project_types', 'jira_cloud_get_project_type_by_key', 'jira_cloud_get_accessible_project_type_by_key', 'jira_cloud_delete_project', 'jira_cloud_get_project', 'jira_cloud_update_project', 'jira_cloud_archive_project', 'jira_cloud_update_project_avatar', 'jira_cloud_delete_project_avatar', 'jira_cloud_create_project_avatar', 'jira_cloud_get_all_project_avatars', 'jira_cloud_get_project_classification_config', 'jira_cloud_remove_default_project_classification', 'jira_cloud_get_default_project_classification', 'jira_cloud_update_default_project_classification', 'jira_cloud_get_project_components_paginated', 'jira_cloud_get_project_components', 'jira_cloud_delete_project_asynchronously', 'jira_cloud_get_features_for_project', 'jira_cloud_toggle_feature_for_project', 'jira_cloud_get_project_property_keys', 'jira_cloud_delete_project_property', 'jira_cloud_get_project_property', 'jira_cloud_set_project_property', 'jira_cloud_get_project_roles', 'jira_cloud_get_project_role', 'jira_cloud_get_project_role_details', 'jira_cloud_get_project_versions_paginated', 'jira_cloud_get_project_versions', 'jira_cloud_get_project_email', 'jira_cloud_update_project_email', 'jira_cloud_get_notification_scheme_for_project', 'jira_cloud_get_security_levels_for_project', 'jira_cloud_get_all_project_categories', 'jira_cloud_create_project_category', 'jira_cloud_remove_project_category', 'jira_cloud_get_project_category_by_id', 'jira_cloud_update_project_category', 'jira_cloud_get_project_fields', 'jira_cloud_validate_project_key', 'jira_cloud_get_valid_project_key', 'jira_cloud_get_valid_project_name', 'jira_cloud_get_all_project_roles', 'jira_cloud_create_project_role', 'jira_cloud_delete_project_role', 'jira_cloud_get_project_role_by_id', 'jira_cloud_partial_update_project_role', 'jira_cloud_fully_update_project_role', 'jira_cloud_delete_project_role_actors_from_role', 'jira_cloud_get_project_role_actors_for_role', 'jira_cloud_add_project_role_actors_to_role', 'jira_cloud_get_project_usages_for_status', 'jira_cloud_create_version', 'jira_cloud_delete_version', 'jira_cloud_get_version', 'jira_cloud_update_version', 'jira_cloud_merge_versions', 'jira_cloud_move_version', 'jira_cloud_delete_and_replace_version', 'jira_cloud_get_project_usages_for_workflow', 'jira_cloud_get_workflow_scheme_project_associations', 'jira_cloud_assign_scheme_to_project', 'jira_cloud_switch_workflow_scheme_for_project', 'jira_cloud_get_project_usages_for_workflow_scheme'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud project operations.

        Actions:
          - 'jira_cloud_find_components_for_projects': Call jira_cloud_find_components_for_projects
          - 'jira_cloud_create_component': Call jira_cloud_create_component
          - 'jira_cloud_delete_component': Call jira_cloud_delete_component
          - 'jira_cloud_get_component': Call jira_cloud_get_component
          - 'jira_cloud_update_component': Call jira_cloud_update_component
          - 'jira_cloud_get_projects_with_field_schemes': Call jira_cloud_get_projects_with_field_schemes
          - 'jira_cloud_search_field_association_scheme_projects': Call jira_cloud_search_field_association_scheme_projects
          - 'jira_cloud_get_field_project_associations': Call jira_cloud_get_field_project_associations
          - 'jira_cloud_get_project_context_mapping': Call jira_cloud_get_project_context_mapping
          - 'jira_cloud_assign_projects_to_custom_field_context': Call jira_cloud_assign_projects_to_custom_field_context
          - 'jira_cloud_remove_custom_field_context_from_projects': Call jira_cloud_remove_custom_field_context_from_projects
          - 'jira_cloud_assign_field_configuration_scheme_to_project': Call jira_cloud_assign_field_configuration_scheme_to_project
          - 'jira_cloud_search_projects_using_security_schemes': Call jira_cloud_search_projects_using_security_schemes
          - 'jira_cloud_associate_schemes_to_projects': Call jira_cloud_associate_schemes_to_projects
          - 'jira_cloud_get_notification_scheme_to_project_mappings': Call jira_cloud_get_notification_scheme_to_project_mappings
          - 'jira_cloud_get_permitted_projects': Call jira_cloud_get_permitted_projects
          - 'jira_cloud_get_projects_by_priority_scheme': Call jira_cloud_get_projects_by_priority_scheme
          - 'jira_cloud_get_all_projects': Call jira_cloud_get_all_projects
          - 'jira_cloud_create_project': Call jira_cloud_create_project
          - 'jira_cloud_create_project_with_custom_template': Call jira_cloud_create_project_with_custom_template
          - 'jira_cloud_search_projects': Call jira_cloud_search_projects
          - 'jira_cloud_get_all_project_types': Call jira_cloud_get_all_project_types
          - 'jira_cloud_get_all_accessible_project_types': Call jira_cloud_get_all_accessible_project_types
          - 'jira_cloud_get_project_type_by_key': Call jira_cloud_get_project_type_by_key
          - 'jira_cloud_get_accessible_project_type_by_key': Call jira_cloud_get_accessible_project_type_by_key
          - 'jira_cloud_delete_project': Call jira_cloud_delete_project
          - 'jira_cloud_get_project': Call jira_cloud_get_project
          - 'jira_cloud_update_project': Call jira_cloud_update_project
          - 'jira_cloud_archive_project': Call jira_cloud_archive_project
          - 'jira_cloud_update_project_avatar': Call jira_cloud_update_project_avatar
          - 'jira_cloud_delete_project_avatar': Call jira_cloud_delete_project_avatar
          - 'jira_cloud_create_project_avatar': Call jira_cloud_create_project_avatar
          - 'jira_cloud_get_all_project_avatars': Call jira_cloud_get_all_project_avatars
          - 'jira_cloud_get_project_classification_config': Call jira_cloud_get_project_classification_config
          - 'jira_cloud_remove_default_project_classification': Call jira_cloud_remove_default_project_classification
          - 'jira_cloud_get_default_project_classification': Call jira_cloud_get_default_project_classification
          - 'jira_cloud_update_default_project_classification': Call jira_cloud_update_default_project_classification
          - 'jira_cloud_get_project_components_paginated': Call jira_cloud_get_project_components_paginated
          - 'jira_cloud_get_project_components': Call jira_cloud_get_project_components
          - 'jira_cloud_delete_project_asynchronously': Call jira_cloud_delete_project_asynchronously
          - 'jira_cloud_get_features_for_project': Call jira_cloud_get_features_for_project
          - 'jira_cloud_toggle_feature_for_project': Call jira_cloud_toggle_feature_for_project
          - 'jira_cloud_get_project_property_keys': Call jira_cloud_get_project_property_keys
          - 'jira_cloud_delete_project_property': Call jira_cloud_delete_project_property
          - 'jira_cloud_get_project_property': Call jira_cloud_get_project_property
          - 'jira_cloud_set_project_property': Call jira_cloud_set_project_property
          - 'jira_cloud_get_project_roles': Call jira_cloud_get_project_roles
          - 'jira_cloud_get_project_role': Call jira_cloud_get_project_role
          - 'jira_cloud_get_project_role_details': Call jira_cloud_get_project_role_details
          - 'jira_cloud_get_project_versions_paginated': Call jira_cloud_get_project_versions_paginated
          - 'jira_cloud_get_project_versions': Call jira_cloud_get_project_versions
          - 'jira_cloud_get_project_email': Call jira_cloud_get_project_email
          - 'jira_cloud_update_project_email': Call jira_cloud_update_project_email
          - 'jira_cloud_get_notification_scheme_for_project': Call jira_cloud_get_notification_scheme_for_project
          - 'jira_cloud_get_security_levels_for_project': Call jira_cloud_get_security_levels_for_project
          - 'jira_cloud_get_all_project_categories': Call jira_cloud_get_all_project_categories
          - 'jira_cloud_create_project_category': Call jira_cloud_create_project_category
          - 'jira_cloud_remove_project_category': Call jira_cloud_remove_project_category
          - 'jira_cloud_get_project_category_by_id': Call jira_cloud_get_project_category_by_id
          - 'jira_cloud_update_project_category': Call jira_cloud_update_project_category
          - 'jira_cloud_get_project_fields': Call jira_cloud_get_project_fields
          - 'jira_cloud_validate_project_key': Call jira_cloud_validate_project_key
          - 'jira_cloud_get_valid_project_key': Call jira_cloud_get_valid_project_key
          - 'jira_cloud_get_valid_project_name': Call jira_cloud_get_valid_project_name
          - 'jira_cloud_get_all_project_roles': Call jira_cloud_get_all_project_roles
          - 'jira_cloud_create_project_role': Call jira_cloud_create_project_role
          - 'jira_cloud_delete_project_role': Call jira_cloud_delete_project_role
          - 'jira_cloud_get_project_role_by_id': Call jira_cloud_get_project_role_by_id
          - 'jira_cloud_partial_update_project_role': Call jira_cloud_partial_update_project_role
          - 'jira_cloud_fully_update_project_role': Call jira_cloud_fully_update_project_role
          - 'jira_cloud_delete_project_role_actors_from_role': Call jira_cloud_delete_project_role_actors_from_role
          - 'jira_cloud_get_project_role_actors_for_role': Call jira_cloud_get_project_role_actors_for_role
          - 'jira_cloud_add_project_role_actors_to_role': Call jira_cloud_add_project_role_actors_to_role
          - 'jira_cloud_get_project_usages_for_status': Call jira_cloud_get_project_usages_for_status
          - 'jira_cloud_create_version': Call jira_cloud_create_version
          - 'jira_cloud_delete_version': Call jira_cloud_delete_version
          - 'jira_cloud_get_version': Call jira_cloud_get_version
          - 'jira_cloud_update_version': Call jira_cloud_update_version
          - 'jira_cloud_merge_versions': Call jira_cloud_merge_versions
          - 'jira_cloud_move_version': Call jira_cloud_move_version
          - 'jira_cloud_delete_and_replace_version': Call jira_cloud_delete_and_replace_version
          - 'jira_cloud_get_project_usages_for_workflow': Call jira_cloud_get_project_usages_for_workflow
          - 'jira_cloud_get_workflow_scheme_project_associations': Call jira_cloud_get_workflow_scheme_project_associations
          - 'jira_cloud_assign_scheme_to_project': Call jira_cloud_assign_scheme_to_project
          - 'jira_cloud_switch_workflow_scheme_for_project': Call jira_cloud_switch_workflow_scheme_for_project
          - 'jira_cloud_get_project_usages_for_workflow_scheme': Call jira_cloud_get_project_usages_for_workflow_scheme
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_find_components_for_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_components_for_projects(**kwargs)
        if action == "jira_cloud_create_component":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_component(**kwargs)
        if action == "jira_cloud_delete_component":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_component(**kwargs)
        if action == "jira_cloud_get_component":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_component(**kwargs)
        if action == "jira_cloud_update_component":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_component(**kwargs)
        if action == "jira_cloud_get_projects_with_field_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_projects_with_field_schemes(**kwargs)
        if action == "jira_cloud_search_field_association_scheme_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_field_association_scheme_projects(**kwargs)
        if action == "jira_cloud_get_field_project_associations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_field_project_associations(**kwargs)
        if action == "jira_cloud_get_project_context_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_context_mapping(**kwargs)
        if action == "jira_cloud_assign_projects_to_custom_field_context":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_assign_projects_to_custom_field_context(**kwargs)
        if action == "jira_cloud_remove_custom_field_context_from_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_custom_field_context_from_projects(**kwargs)
        if action == "jira_cloud_assign_field_configuration_scheme_to_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_assign_field_configuration_scheme_to_project(
                **kwargs
            )
        if action == "jira_cloud_search_projects_using_security_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_projects_using_security_schemes(**kwargs)
        if action == "jira_cloud_associate_schemes_to_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_associate_schemes_to_projects(**kwargs)
        if action == "jira_cloud_get_notification_scheme_to_project_mappings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_notification_scheme_to_project_mappings(
                **kwargs
            )
        if action == "jira_cloud_get_permitted_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_permitted_projects(**kwargs)
        if action == "jira_cloud_get_projects_by_priority_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_projects_by_priority_scheme(**kwargs)
        if action == "jira_cloud_get_all_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_projects(**kwargs)
        if action == "jira_cloud_create_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_project(**kwargs)
        if action == "jira_cloud_create_project_with_custom_template":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_project_with_custom_template(**kwargs)
        if action == "jira_cloud_search_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_projects(**kwargs)
        if action == "jira_cloud_get_all_project_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_project_types(**kwargs)
        if action == "jira_cloud_get_all_accessible_project_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_accessible_project_types(**kwargs)
        if action == "jira_cloud_get_project_type_by_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_type_by_key(**kwargs)
        if action == "jira_cloud_get_accessible_project_type_by_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_accessible_project_type_by_key(**kwargs)
        if action == "jira_cloud_delete_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_project(**kwargs)
        if action == "jira_cloud_get_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project(**kwargs)
        if action == "jira_cloud_update_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_project(**kwargs)
        if action == "jira_cloud_archive_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_archive_project(**kwargs)
        if action == "jira_cloud_update_project_avatar":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_project_avatar(**kwargs)
        if action == "jira_cloud_delete_project_avatar":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_project_avatar(**kwargs)
        if action == "jira_cloud_create_project_avatar":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_project_avatar(**kwargs)
        if action == "jira_cloud_get_all_project_avatars":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_project_avatars(**kwargs)
        if action == "jira_cloud_get_project_classification_config":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_classification_config(**kwargs)
        if action == "jira_cloud_remove_default_project_classification":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_default_project_classification(**kwargs)
        if action == "jira_cloud_get_default_project_classification":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_default_project_classification(**kwargs)
        if action == "jira_cloud_update_default_project_classification":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_default_project_classification(**kwargs)
        if action == "jira_cloud_get_project_components_paginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_components_paginated(**kwargs)
        if action == "jira_cloud_get_project_components":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_components(**kwargs)
        if action == "jira_cloud_delete_project_asynchronously":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_project_asynchronously(**kwargs)
        if action == "jira_cloud_get_features_for_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_features_for_project(**kwargs)
        if action == "jira_cloud_toggle_feature_for_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_toggle_feature_for_project(**kwargs)
        if action == "jira_cloud_get_project_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_property_keys(**kwargs)
        if action == "jira_cloud_delete_project_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_project_property(**kwargs)
        if action == "jira_cloud_get_project_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_property(**kwargs)
        if action == "jira_cloud_set_project_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_project_property(**kwargs)
        if action == "jira_cloud_get_project_roles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_roles(**kwargs)
        if action == "jira_cloud_get_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_role(**kwargs)
        if action == "jira_cloud_get_project_role_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_role_details(**kwargs)
        if action == "jira_cloud_get_project_versions_paginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_versions_paginated(**kwargs)
        if action == "jira_cloud_get_project_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_versions(**kwargs)
        if action == "jira_cloud_get_project_email":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_email(**kwargs)
        if action == "jira_cloud_update_project_email":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_project_email(**kwargs)
        if action == "jira_cloud_get_notification_scheme_for_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_notification_scheme_for_project(**kwargs)
        if action == "jira_cloud_get_security_levels_for_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_security_levels_for_project(**kwargs)
        if action == "jira_cloud_get_all_project_categories":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_project_categories(**kwargs)
        if action == "jira_cloud_create_project_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_project_category(**kwargs)
        if action == "jira_cloud_remove_project_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_project_category(**kwargs)
        if action == "jira_cloud_get_project_category_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_category_by_id(**kwargs)
        if action == "jira_cloud_update_project_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_project_category(**kwargs)
        if action == "jira_cloud_get_project_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_fields(**kwargs)
        if action == "jira_cloud_validate_project_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_validate_project_key(**kwargs)
        if action == "jira_cloud_get_valid_project_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_valid_project_key(**kwargs)
        if action == "jira_cloud_get_valid_project_name":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_valid_project_name(**kwargs)
        if action == "jira_cloud_get_all_project_roles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_project_roles(**kwargs)
        if action == "jira_cloud_create_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_project_role(**kwargs)
        if action == "jira_cloud_delete_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_project_role(**kwargs)
        if action == "jira_cloud_get_project_role_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_role_by_id(**kwargs)
        if action == "jira_cloud_partial_update_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_partial_update_project_role(**kwargs)
        if action == "jira_cloud_fully_update_project_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_fully_update_project_role(**kwargs)
        if action == "jira_cloud_delete_project_role_actors_from_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_project_role_actors_from_role(**kwargs)
        if action == "jira_cloud_get_project_role_actors_for_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_role_actors_for_role(**kwargs)
        if action == "jira_cloud_add_project_role_actors_to_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_project_role_actors_to_role(**kwargs)
        if action == "jira_cloud_get_project_usages_for_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_usages_for_status(**kwargs)
        if action == "jira_cloud_create_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_version(**kwargs)
        if action == "jira_cloud_delete_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_version(**kwargs)
        if action == "jira_cloud_get_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_version(**kwargs)
        if action == "jira_cloud_update_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_version(**kwargs)
        if action == "jira_cloud_merge_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_merge_versions(**kwargs)
        if action == "jira_cloud_move_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_move_version(**kwargs)
        if action == "jira_cloud_delete_and_replace_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_and_replace_version(**kwargs)
        if action == "jira_cloud_get_project_usages_for_workflow":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_usages_for_workflow(**kwargs)
        if action == "jira_cloud_get_workflow_scheme_project_associations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_scheme_project_associations(**kwargs)
        if action == "jira_cloud_assign_scheme_to_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_assign_scheme_to_project(**kwargs)
        if action == "jira_cloud_switch_workflow_scheme_for_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_switch_workflow_scheme_for_project(**kwargs)
        if action == "jira_cloud_get_project_usages_for_workflow_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_usages_for_workflow_scheme(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_find_components_for_projects', 'jira_cloud_create_component', 'jira_cloud_delete_component', 'jira_cloud_get_component', 'jira_cloud_update_component', 'jira_cloud_get_projects_with_field_schemes', 'jira_cloud_search_field_association_scheme_projects', 'jira_cloud_get_field_project_associations', 'jira_cloud_get_project_context_mapping', 'jira_cloud_assign_projects_to_custom_field_context', 'jira_cloud_remove_custom_field_context_from_projects', 'jira_cloud_assign_field_configuration_scheme_to_project', 'jira_cloud_search_projects_using_security_schemes', 'jira_cloud_associate_schemes_to_projects', 'jira_cloud_get_notification_scheme_to_project_mappings', 'jira_cloud_get_permitted_projects', 'jira_cloud_get_projects_by_priority_scheme', 'jira_cloud_get_all_projects', 'jira_cloud_create_project', 'jira_cloud_create_project_with_custom_template', 'jira_cloud_search_projects', 'jira_cloud_get_all_project_types', 'jira_cloud_get_all_accessible_project_types', 'jira_cloud_get_project_type_by_key', 'jira_cloud_get_accessible_project_type_by_key', 'jira_cloud_delete_project', 'jira_cloud_get_project', 'jira_cloud_update_project', 'jira_cloud_archive_project', 'jira_cloud_update_project_avatar', 'jira_cloud_delete_project_avatar', 'jira_cloud_create_project_avatar', 'jira_cloud_get_all_project_avatars', 'jira_cloud_get_project_classification_config', 'jira_cloud_remove_default_project_classification', 'jira_cloud_get_default_project_classification', 'jira_cloud_update_default_project_classification', 'jira_cloud_get_project_components_paginated', 'jira_cloud_get_project_components', 'jira_cloud_delete_project_asynchronously', 'jira_cloud_get_features_for_project', 'jira_cloud_toggle_feature_for_project', 'jira_cloud_get_project_property_keys', 'jira_cloud_delete_project_property', 'jira_cloud_get_project_property', 'jira_cloud_set_project_property', 'jira_cloud_get_project_roles', 'jira_cloud_get_project_role', 'jira_cloud_get_project_role_details', 'jira_cloud_get_project_versions_paginated', 'jira_cloud_get_project_versions', 'jira_cloud_get_project_email', 'jira_cloud_update_project_email', 'jira_cloud_get_notification_scheme_for_project', 'jira_cloud_get_security_levels_for_project', 'jira_cloud_get_all_project_categories', 'jira_cloud_create_project_category', 'jira_cloud_remove_project_category', 'jira_cloud_get_project_category_by_id', 'jira_cloud_update_project_category', 'jira_cloud_get_project_fields', 'jira_cloud_validate_project_key', 'jira_cloud_get_valid_project_key', 'jira_cloud_get_valid_project_name', 'jira_cloud_get_all_project_roles', 'jira_cloud_create_project_role', 'jira_cloud_delete_project_role', 'jira_cloud_get_project_role_by_id', 'jira_cloud_partial_update_project_role', 'jira_cloud_fully_update_project_role', 'jira_cloud_delete_project_role_actors_from_role', 'jira_cloud_get_project_role_actors_for_role', 'jira_cloud_add_project_role_actors_to_role', 'jira_cloud_get_project_usages_for_status', 'jira_cloud_create_version', 'jira_cloud_delete_version', 'jira_cloud_get_version', 'jira_cloud_update_version', 'jira_cloud_merge_versions', 'jira_cloud_move_version', 'jira_cloud_delete_and_replace_version', 'jira_cloud_get_project_usages_for_workflow', 'jira_cloud_get_workflow_scheme_project_associations', 'jira_cloud_assign_scheme_to_project', 'jira_cloud_switch_workflow_scheme_for_project', 'jira_cloud_get_project_usages_for_workflow_scheme"
        )


def register_jira_cloud_issue_attachment_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-issue-attachment"})
    async def atlassian_jira_cloud_issue_attachment(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_attachment_content', 'jira_cloud_get_attachment_meta', 'jira_cloud_get_attachment_thumbnail', 'jira_cloud_remove_attachment', 'jira_cloud_get_attachment', 'jira_cloud_expand_attachment_for_humans', 'jira_cloud_expand_attachment_for_machines', 'jira_cloud_add_attachment'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud issue attachment operations.

        Actions:
          - 'jira_cloud_get_attachment_content': Call jira_cloud_get_attachment_content
          - 'jira_cloud_get_attachment_meta': Call jira_cloud_get_attachment_meta
          - 'jira_cloud_get_attachment_thumbnail': Call jira_cloud_get_attachment_thumbnail
          - 'jira_cloud_remove_attachment': Call jira_cloud_remove_attachment
          - 'jira_cloud_get_attachment': Call jira_cloud_get_attachment
          - 'jira_cloud_expand_attachment_for_humans': Call jira_cloud_expand_attachment_for_humans
          - 'jira_cloud_expand_attachment_for_machines': Call jira_cloud_expand_attachment_for_machines
          - 'jira_cloud_add_attachment': Call jira_cloud_add_attachment
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_attachment_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_attachment_content(**kwargs)
        if action == "jira_cloud_get_attachment_meta":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_attachment_meta(**kwargs)
        if action == "jira_cloud_get_attachment_thumbnail":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_attachment_thumbnail(**kwargs)
        if action == "jira_cloud_remove_attachment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_attachment(**kwargs)
        if action == "jira_cloud_get_attachment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_attachment(**kwargs)
        if action == "jira_cloud_expand_attachment_for_humans":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_expand_attachment_for_humans(**kwargs)
        if action == "jira_cloud_expand_attachment_for_machines":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_expand_attachment_for_machines(**kwargs)
        if action == "jira_cloud_add_attachment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_attachment(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_attachment_content', 'jira_cloud_get_attachment_meta', 'jira_cloud_get_attachment_thumbnail', 'jira_cloud_remove_attachment', 'jira_cloud_get_attachment', 'jira_cloud_expand_attachment_for_humans', 'jira_cloud_expand_attachment_for_machines', 'jira_cloud_add_attachment"
        )


def register_jira_cloud_issue_bulk_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-issue-bulk"})
    async def atlassian_jira_cloud_issue_bulk(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_submit_bulk_delete', 'jira_cloud_get_bulk_editable_fields', 'jira_cloud_submit_bulk_edit', 'jira_cloud_submit_bulk_move', 'jira_cloud_submit_bulk_transition', 'jira_cloud_submit_bulk_unwatch', 'jira_cloud_submit_bulk_watch', 'jira_cloud_get_bulk_operation_progress', 'jira_cloud_get_bulk_changelogs', 'jira_cloud_bulk_edit_dashboards', 'jira_cloud_bulk_pin_unpin_projects_async', 'jira_cloud_bulk_get_groups', 'jira_cloud_bulk_fetch_issues', 'jira_cloud_bulk_set_issues_properties_list', 'jira_cloud_bulk_set_issue_properties_by_issue', 'jira_cloud_bulk_delete_issue_property', 'jira_cloud_bulk_set_issue_property', 'jira_cloud_get_is_watching_issue_bulk', 'jira_cloud_get_bulk_permissions', 'jira_cloud_get_bulk_screen_tabs', 'jira_cloud_find_bulk_assignable_users', 'jira_cloud_bulk_get_users', 'jira_cloud_bulk_get_users_migration', 'jira_cloud_get_user_email_bulk'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud issue bulk operations.

        Actions:
          - 'jira_cloud_submit_bulk_delete': Call jira_cloud_submit_bulk_delete
          - 'jira_cloud_get_bulk_editable_fields': Call jira_cloud_get_bulk_editable_fields
          - 'jira_cloud_submit_bulk_edit': Call jira_cloud_submit_bulk_edit
          - 'jira_cloud_submit_bulk_move': Call jira_cloud_submit_bulk_move
          - 'jira_cloud_submit_bulk_transition': Call jira_cloud_submit_bulk_transition
          - 'jira_cloud_submit_bulk_unwatch': Call jira_cloud_submit_bulk_unwatch
          - 'jira_cloud_submit_bulk_watch': Call jira_cloud_submit_bulk_watch
          - 'jira_cloud_get_bulk_operation_progress': Call jira_cloud_get_bulk_operation_progress
          - 'jira_cloud_get_bulk_changelogs': Call jira_cloud_get_bulk_changelogs
          - 'jira_cloud_bulk_edit_dashboards': Call jira_cloud_bulk_edit_dashboards
          - 'jira_cloud_bulk_pin_unpin_projects_async': Call jira_cloud_bulk_pin_unpin_projects_async
          - 'jira_cloud_bulk_get_groups': Call jira_cloud_bulk_get_groups
          - 'jira_cloud_bulk_fetch_issues': Call jira_cloud_bulk_fetch_issues
          - 'jira_cloud_bulk_set_issues_properties_list': Call jira_cloud_bulk_set_issues_properties_list
          - 'jira_cloud_bulk_set_issue_properties_by_issue': Call jira_cloud_bulk_set_issue_properties_by_issue
          - 'jira_cloud_bulk_delete_issue_property': Call jira_cloud_bulk_delete_issue_property
          - 'jira_cloud_bulk_set_issue_property': Call jira_cloud_bulk_set_issue_property
          - 'jira_cloud_get_is_watching_issue_bulk': Call jira_cloud_get_is_watching_issue_bulk
          - 'jira_cloud_get_bulk_permissions': Call jira_cloud_get_bulk_permissions
          - 'jira_cloud_get_bulk_screen_tabs': Call jira_cloud_get_bulk_screen_tabs
          - 'jira_cloud_find_bulk_assignable_users': Call jira_cloud_find_bulk_assignable_users
          - 'jira_cloud_bulk_get_users': Call jira_cloud_bulk_get_users
          - 'jira_cloud_bulk_get_users_migration': Call jira_cloud_bulk_get_users_migration
          - 'jira_cloud_get_user_email_bulk': Call jira_cloud_get_user_email_bulk
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_submit_bulk_delete":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_submit_bulk_delete(**kwargs)
        if action == "jira_cloud_get_bulk_editable_fields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_bulk_editable_fields(**kwargs)
        if action == "jira_cloud_submit_bulk_edit":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_submit_bulk_edit(**kwargs)
        if action == "jira_cloud_submit_bulk_move":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_submit_bulk_move(**kwargs)
        if action == "jira_cloud_submit_bulk_transition":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_submit_bulk_transition(**kwargs)
        if action == "jira_cloud_submit_bulk_unwatch":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_submit_bulk_unwatch(**kwargs)
        if action == "jira_cloud_submit_bulk_watch":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_submit_bulk_watch(**kwargs)
        if action == "jira_cloud_get_bulk_operation_progress":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_bulk_operation_progress(**kwargs)
        if action == "jira_cloud_get_bulk_changelogs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_bulk_changelogs(**kwargs)
        if action == "jira_cloud_bulk_edit_dashboards":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_edit_dashboards(**kwargs)
        if action == "jira_cloud_bulk_pin_unpin_projects_async":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_pin_unpin_projects_async(**kwargs)
        if action == "jira_cloud_bulk_get_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_get_groups(**kwargs)
        if action == "jira_cloud_bulk_fetch_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_fetch_issues(**kwargs)
        if action == "jira_cloud_bulk_set_issues_properties_list":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_set_issues_properties_list(**kwargs)
        if action == "jira_cloud_bulk_set_issue_properties_by_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_set_issue_properties_by_issue(**kwargs)
        if action == "jira_cloud_bulk_delete_issue_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_delete_issue_property(**kwargs)
        if action == "jira_cloud_bulk_set_issue_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_set_issue_property(**kwargs)
        if action == "jira_cloud_get_is_watching_issue_bulk":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_is_watching_issue_bulk(**kwargs)
        if action == "jira_cloud_get_bulk_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_bulk_permissions(**kwargs)
        if action == "jira_cloud_get_bulk_screen_tabs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_bulk_screen_tabs(**kwargs)
        if action == "jira_cloud_find_bulk_assignable_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_find_bulk_assignable_users(**kwargs)
        if action == "jira_cloud_bulk_get_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_get_users(**kwargs)
        if action == "jira_cloud_bulk_get_users_migration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_get_users_migration(**kwargs)
        if action == "jira_cloud_get_user_email_bulk":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_user_email_bulk(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_submit_bulk_delete', 'jira_cloud_get_bulk_editable_fields', 'jira_cloud_submit_bulk_edit', 'jira_cloud_submit_bulk_move', 'jira_cloud_submit_bulk_transition', 'jira_cloud_submit_bulk_unwatch', 'jira_cloud_submit_bulk_watch', 'jira_cloud_get_bulk_operation_progress', 'jira_cloud_get_bulk_changelogs', 'jira_cloud_bulk_edit_dashboards', 'jira_cloud_bulk_pin_unpin_projects_async', 'jira_cloud_bulk_get_groups', 'jira_cloud_bulk_fetch_issues', 'jira_cloud_bulk_set_issues_properties_list', 'jira_cloud_bulk_set_issue_properties_by_issue', 'jira_cloud_bulk_delete_issue_property', 'jira_cloud_bulk_set_issue_property', 'jira_cloud_get_is_watching_issue_bulk', 'jira_cloud_get_bulk_permissions', 'jira_cloud_get_bulk_screen_tabs', 'jira_cloud_find_bulk_assignable_users', 'jira_cloud_bulk_get_users', 'jira_cloud_bulk_get_users_migration', 'jira_cloud_get_user_email_bulk"
        )


def register_jira_cloud_issue_core_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-issue-core"})
    async def atlassian_jira_cloud_issue_core(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_available_transitions', 'jira_cloud_get_component_related_issues', 'jira_cloud_get_all_issue_field_options', 'jira_cloud_create_issue_field_option', 'jira_cloud_get_selectable_issue_field_options', 'jira_cloud_get_visible_issue_field_options', 'jira_cloud_delete_issue_field_option', 'jira_cloud_get_issue_field_option', 'jira_cloud_update_issue_field_option', 'jira_cloud_replace_issue_field_option', 'jira_cloud_create_filter', 'jira_cloud_get_favourite_filters', 'jira_cloud_get_my_filters', 'jira_cloud_get_filters_paginated', 'jira_cloud_delete_filter', 'jira_cloud_get_filter', 'jira_cloud_update_filter', 'jira_cloud_delete_favourite_for_filter', 'jira_cloud_set_favourite_for_filter', 'jira_cloud_change_filter_owner', 'jira_cloud_create_issue', 'jira_cloud_archive_issues_async', 'jira_cloud_archive_issues', 'jira_cloud_create_issues', 'jira_cloud_get_create_issue_meta', 'jira_cloud_get_issue_limit_report', 'jira_cloud_get_issue_picker_resource', 'jira_cloud_unarchive_issues', 'jira_cloud_delete_issue', 'jira_cloud_get_issue', 'jira_cloud_edit_issue', 'jira_cloud_assign_issue', 'jira_cloud_get_edit_issue_meta', 'jira_cloud_get_issue_property_keys', 'jira_cloud_delete_issue_property', 'jira_cloud_get_issue_property', 'jira_cloud_set_issue_property', 'jira_cloud_get_transitions', 'jira_cloud_do_transition', 'jira_cloud_remove_watcher', 'jira_cloud_add_watcher', 'jira_cloud_link_issues', 'jira_cloud_delete_issue_link', 'jira_cloud_get_issue_link', 'jira_cloud_get_issue_link_types', 'jira_cloud_create_issue_link_type', 'jira_cloud_delete_issue_link_type', 'jira_cloud_get_issue_link_type', 'jira_cloud_update_issue_link_type', 'jira_cloud_export_archived_issues', 'jira_cloud_get_issue_security_schemes', 'jira_cloud_create_issue_security_scheme', 'jira_cloud_get_issue_security_scheme', 'jira_cloud_update_issue_security_scheme', 'jira_cloud_get_issue_security_level_members', 'jira_cloud_get_issue_all_types', 'jira_cloud_match_issues', 'jira_cloud_parse_jql_queries', 'jira_cloud_sanitise_jql_queries', 'jira_cloud_get_project_issue_security_scheme', 'jira_cloud_search_for_issues_using_jql', 'jira_cloud_search_for_issues_using_jql_post', 'jira_cloud_count_issues', 'jira_cloud_search_and_reconsile_issues_using_jql', 'jira_cloud_search_and_reconsile_issues_using_jql_post', 'jira_cloud_get_issue_security_level', 'jira_cloud_get_issue_navigator_default_columns', 'jira_cloud_set_issue_navigator_default_columns', 'jira_cloud_get_version_related_issues', 'jira_cloud_get_version_unresolved_issues', 'jira_cloud_get_workflow_transition_rule_configurations', 'jira_cloud_delete_workflow_transition_property', 'jira_cloud_get_workflow_transition_properties', 'jira_cloud_create_workflow_transition_property', 'jira_cloud_update_workflow_transition_property'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud issue core operations.

        Actions:
          - 'jira_cloud_get_available_transitions': Call jira_cloud_get_available_transitions
          - 'jira_cloud_get_component_related_issues': Call jira_cloud_get_component_related_issues
          - 'jira_cloud_get_all_issue_field_options': Call jira_cloud_get_all_issue_field_options
          - 'jira_cloud_create_issue_field_option': Call jira_cloud_create_issue_field_option
          - 'jira_cloud_get_selectable_issue_field_options': Call jira_cloud_get_selectable_issue_field_options
          - 'jira_cloud_get_visible_issue_field_options': Call jira_cloud_get_visible_issue_field_options
          - 'jira_cloud_delete_issue_field_option': Call jira_cloud_delete_issue_field_option
          - 'jira_cloud_get_issue_field_option': Call jira_cloud_get_issue_field_option
          - 'jira_cloud_update_issue_field_option': Call jira_cloud_update_issue_field_option
          - 'jira_cloud_replace_issue_field_option': Call jira_cloud_replace_issue_field_option
          - 'jira_cloud_create_filter': Call jira_cloud_create_filter
          - 'jira_cloud_get_favourite_filters': Call jira_cloud_get_favourite_filters
          - 'jira_cloud_get_my_filters': Call jira_cloud_get_my_filters
          - 'jira_cloud_get_filters_paginated': Call jira_cloud_get_filters_paginated
          - 'jira_cloud_delete_filter': Call jira_cloud_delete_filter
          - 'jira_cloud_get_filter': Call jira_cloud_get_filter
          - 'jira_cloud_update_filter': Call jira_cloud_update_filter
          - 'jira_cloud_delete_favourite_for_filter': Call jira_cloud_delete_favourite_for_filter
          - 'jira_cloud_set_favourite_for_filter': Call jira_cloud_set_favourite_for_filter
          - 'jira_cloud_change_filter_owner': Call jira_cloud_change_filter_owner
          - 'jira_cloud_create_issue': Call jira_cloud_create_issue
          - 'jira_cloud_archive_issues_async': Call jira_cloud_archive_issues_async
          - 'jira_cloud_archive_issues': Call jira_cloud_archive_issues
          - 'jira_cloud_create_issues': Call jira_cloud_create_issues
          - 'jira_cloud_get_create_issue_meta': Call jira_cloud_get_create_issue_meta
          - 'jira_cloud_get_issue_limit_report': Call jira_cloud_get_issue_limit_report
          - 'jira_cloud_get_issue_picker_resource': Call jira_cloud_get_issue_picker_resource
          - 'jira_cloud_unarchive_issues': Call jira_cloud_unarchive_issues
          - 'jira_cloud_delete_issue': Call jira_cloud_delete_issue
          - 'jira_cloud_get_issue': Call jira_cloud_get_issue
          - 'jira_cloud_edit_issue': Call jira_cloud_edit_issue
          - 'jira_cloud_assign_issue': Call jira_cloud_assign_issue
          - 'jira_cloud_get_edit_issue_meta': Call jira_cloud_get_edit_issue_meta
          - 'jira_cloud_get_issue_property_keys': Call jira_cloud_get_issue_property_keys
          - 'jira_cloud_delete_issue_property': Call jira_cloud_delete_issue_property
          - 'jira_cloud_get_issue_property': Call jira_cloud_get_issue_property
          - 'jira_cloud_set_issue_property': Call jira_cloud_set_issue_property
          - 'jira_cloud_get_transitions': Call jira_cloud_get_transitions
          - 'jira_cloud_do_transition': Call jira_cloud_do_transition
          - 'jira_cloud_remove_watcher': Call jira_cloud_remove_watcher
          - 'jira_cloud_add_watcher': Call jira_cloud_add_watcher
          - 'jira_cloud_link_issues': Call jira_cloud_link_issues
          - 'jira_cloud_delete_issue_link': Call jira_cloud_delete_issue_link
          - 'jira_cloud_get_issue_link': Call jira_cloud_get_issue_link
          - 'jira_cloud_get_issue_link_types': Call jira_cloud_get_issue_link_types
          - 'jira_cloud_create_issue_link_type': Call jira_cloud_create_issue_link_type
          - 'jira_cloud_delete_issue_link_type': Call jira_cloud_delete_issue_link_type
          - 'jira_cloud_get_issue_link_type': Call jira_cloud_get_issue_link_type
          - 'jira_cloud_update_issue_link_type': Call jira_cloud_update_issue_link_type
          - 'jira_cloud_export_archived_issues': Call jira_cloud_export_archived_issues
          - 'jira_cloud_get_issue_security_schemes': Call jira_cloud_get_issue_security_schemes
          - 'jira_cloud_create_issue_security_scheme': Call jira_cloud_create_issue_security_scheme
          - 'jira_cloud_get_issue_security_scheme': Call jira_cloud_get_issue_security_scheme
          - 'jira_cloud_update_issue_security_scheme': Call jira_cloud_update_issue_security_scheme
          - 'jira_cloud_get_issue_security_level_members': Call jira_cloud_get_issue_security_level_members
          - 'jira_cloud_get_issue_all_types': Call jira_cloud_get_issue_all_types
          - 'jira_cloud_match_issues': Call jira_cloud_match_issues
          - 'jira_cloud_parse_jql_queries': Call jira_cloud_parse_jql_queries
          - 'jira_cloud_sanitise_jql_queries': Call jira_cloud_sanitise_jql_queries
          - 'jira_cloud_get_project_issue_security_scheme': Call jira_cloud_get_project_issue_security_scheme
          - 'jira_cloud_search_for_issues_using_jql': Call jira_cloud_search_for_issues_using_jql
          - 'jira_cloud_search_for_issues_using_jql_post': Call jira_cloud_search_for_issues_using_jql_post
          - 'jira_cloud_count_issues': Call jira_cloud_count_issues
          - 'jira_cloud_search_and_reconsile_issues_using_jql': Call jira_cloud_search_and_reconsile_issues_using_jql
          - 'jira_cloud_search_and_reconsile_issues_using_jql_post': Call jira_cloud_search_and_reconsile_issues_using_jql_post
          - 'jira_cloud_get_issue_security_level': Call jira_cloud_get_issue_security_level
          - 'jira_cloud_get_issue_navigator_default_columns': Call jira_cloud_get_issue_navigator_default_columns
          - 'jira_cloud_set_issue_navigator_default_columns': Call jira_cloud_set_issue_navigator_default_columns
          - 'jira_cloud_get_version_related_issues': Call jira_cloud_get_version_related_issues
          - 'jira_cloud_get_version_unresolved_issues': Call jira_cloud_get_version_unresolved_issues
          - 'jira_cloud_get_workflow_transition_rule_configurations': Call jira_cloud_get_workflow_transition_rule_configurations
          - 'jira_cloud_delete_workflow_transition_property': Call jira_cloud_delete_workflow_transition_property
          - 'jira_cloud_get_workflow_transition_properties': Call jira_cloud_get_workflow_transition_properties
          - 'jira_cloud_create_workflow_transition_property': Call jira_cloud_create_workflow_transition_property
          - 'jira_cloud_update_workflow_transition_property': Call jira_cloud_update_workflow_transition_property
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_available_transitions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_available_transitions(**kwargs)
        if action == "jira_cloud_get_component_related_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_component_related_issues(**kwargs)
        if action == "jira_cloud_get_all_issue_field_options":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_issue_field_options(**kwargs)
        if action == "jira_cloud_create_issue_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issue_field_option(**kwargs)
        if action == "jira_cloud_get_selectable_issue_field_options":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_selectable_issue_field_options(**kwargs)
        if action == "jira_cloud_get_visible_issue_field_options":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_visible_issue_field_options(**kwargs)
        if action == "jira_cloud_delete_issue_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue_field_option(**kwargs)
        if action == "jira_cloud_get_issue_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_field_option(**kwargs)
        if action == "jira_cloud_update_issue_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_issue_field_option(**kwargs)
        if action == "jira_cloud_replace_issue_field_option":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_replace_issue_field_option(**kwargs)
        if action == "jira_cloud_create_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_filter(**kwargs)
        if action == "jira_cloud_get_favourite_filters":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_favourite_filters(**kwargs)
        if action == "jira_cloud_get_my_filters":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_my_filters(**kwargs)
        if action == "jira_cloud_get_filters_paginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_filters_paginated(**kwargs)
        if action == "jira_cloud_delete_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_filter(**kwargs)
        if action == "jira_cloud_get_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_filter(**kwargs)
        if action == "jira_cloud_update_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_filter(**kwargs)
        if action == "jira_cloud_delete_favourite_for_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_favourite_for_filter(**kwargs)
        if action == "jira_cloud_set_favourite_for_filter":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_favourite_for_filter(**kwargs)
        if action == "jira_cloud_change_filter_owner":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_change_filter_owner(**kwargs)
        if action == "jira_cloud_create_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issue(**kwargs)
        if action == "jira_cloud_archive_issues_async":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_archive_issues_async(**kwargs)
        if action == "jira_cloud_archive_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_archive_issues(**kwargs)
        if action == "jira_cloud_create_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issues(**kwargs)
        if action == "jira_cloud_get_create_issue_meta":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_create_issue_meta(**kwargs)
        if action == "jira_cloud_get_issue_limit_report":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_limit_report(**kwargs)
        if action == "jira_cloud_get_issue_picker_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_picker_resource(**kwargs)
        if action == "jira_cloud_unarchive_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_unarchive_issues(**kwargs)
        if action == "jira_cloud_delete_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue(**kwargs)
        if action == "jira_cloud_get_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue(**kwargs)
        if action == "jira_cloud_edit_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_edit_issue(**kwargs)
        if action == "jira_cloud_assign_issue":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_assign_issue(**kwargs)
        if action == "jira_cloud_get_edit_issue_meta":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_edit_issue_meta(**kwargs)
        if action == "jira_cloud_get_issue_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_property_keys(**kwargs)
        if action == "jira_cloud_delete_issue_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue_property(**kwargs)
        if action == "jira_cloud_get_issue_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_property(**kwargs)
        if action == "jira_cloud_set_issue_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_issue_property(**kwargs)
        if action == "jira_cloud_get_transitions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_transitions(**kwargs)
        if action == "jira_cloud_do_transition":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_do_transition(**kwargs)
        if action == "jira_cloud_remove_watcher":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_watcher(**kwargs)
        if action == "jira_cloud_add_watcher":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_watcher(**kwargs)
        if action == "jira_cloud_link_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_link_issues(**kwargs)
        if action == "jira_cloud_delete_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue_link(**kwargs)
        if action == "jira_cloud_get_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_link(**kwargs)
        if action == "jira_cloud_get_issue_link_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_link_types(**kwargs)
        if action == "jira_cloud_create_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issue_link_type(**kwargs)
        if action == "jira_cloud_delete_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue_link_type(**kwargs)
        if action == "jira_cloud_get_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_link_type(**kwargs)
        if action == "jira_cloud_update_issue_link_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_issue_link_type(**kwargs)
        if action == "jira_cloud_export_archived_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_export_archived_issues(**kwargs)
        if action == "jira_cloud_get_issue_security_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_security_schemes(**kwargs)
        if action == "jira_cloud_create_issue_security_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issue_security_scheme(**kwargs)
        if action == "jira_cloud_get_issue_security_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_security_scheme(**kwargs)
        if action == "jira_cloud_update_issue_security_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_issue_security_scheme(**kwargs)
        if action == "jira_cloud_get_issue_security_level_members":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_security_level_members(**kwargs)
        if action == "jira_cloud_get_issue_all_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_all_types(**kwargs)
        if action == "jira_cloud_match_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_match_issues(**kwargs)
        if action == "jira_cloud_parse_jql_queries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_parse_jql_queries(**kwargs)
        if action == "jira_cloud_sanitise_jql_queries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_sanitise_jql_queries(**kwargs)
        if action == "jira_cloud_get_project_issue_security_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_issue_security_scheme(**kwargs)
        if action == "jira_cloud_search_for_issues_using_jql":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_for_issues_using_jql(**kwargs)
        if action == "jira_cloud_search_for_issues_using_jql_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_for_issues_using_jql_post(**kwargs)
        if action == "jira_cloud_count_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_count_issues(**kwargs)
        if action == "jira_cloud_search_and_reconsile_issues_using_jql":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_and_reconsile_issues_using_jql(**kwargs)
        if action == "jira_cloud_search_and_reconsile_issues_using_jql_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_and_reconsile_issues_using_jql_post(
                **kwargs
            )
        if action == "jira_cloud_get_issue_security_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_security_level(**kwargs)
        if action == "jira_cloud_get_issue_navigator_default_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_navigator_default_columns(**kwargs)
        if action == "jira_cloud_set_issue_navigator_default_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_issue_navigator_default_columns(**kwargs)
        if action == "jira_cloud_get_version_related_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_version_related_issues(**kwargs)
        if action == "jira_cloud_get_version_unresolved_issues":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_version_unresolved_issues(**kwargs)
        if action == "jira_cloud_get_workflow_transition_rule_configurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_transition_rule_configurations(
                **kwargs
            )
        if action == "jira_cloud_delete_workflow_transition_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_workflow_transition_property(**kwargs)
        if action == "jira_cloud_get_workflow_transition_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_transition_properties(**kwargs)
        if action == "jira_cloud_create_workflow_transition_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_workflow_transition_property(**kwargs)
        if action == "jira_cloud_update_workflow_transition_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_workflow_transition_property(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_available_transitions', 'jira_cloud_get_component_related_issues', 'jira_cloud_get_all_issue_field_options', 'jira_cloud_create_issue_field_option', 'jira_cloud_get_selectable_issue_field_options', 'jira_cloud_get_visible_issue_field_options', 'jira_cloud_delete_issue_field_option', 'jira_cloud_get_issue_field_option', 'jira_cloud_update_issue_field_option', 'jira_cloud_replace_issue_field_option', 'jira_cloud_create_filter', 'jira_cloud_get_favourite_filters', 'jira_cloud_get_my_filters', 'jira_cloud_get_filters_paginated', 'jira_cloud_delete_filter', 'jira_cloud_get_filter', 'jira_cloud_update_filter', 'jira_cloud_delete_favourite_for_filter', 'jira_cloud_set_favourite_for_filter', 'jira_cloud_change_filter_owner', 'jira_cloud_create_issue', 'jira_cloud_archive_issues_async', 'jira_cloud_archive_issues', 'jira_cloud_create_issues', 'jira_cloud_get_create_issue_meta', 'jira_cloud_get_issue_limit_report', 'jira_cloud_get_issue_picker_resource', 'jira_cloud_unarchive_issues', 'jira_cloud_delete_issue', 'jira_cloud_get_issue', 'jira_cloud_edit_issue', 'jira_cloud_assign_issue', 'jira_cloud_get_edit_issue_meta', 'jira_cloud_get_issue_property_keys', 'jira_cloud_delete_issue_property', 'jira_cloud_get_issue_property', 'jira_cloud_set_issue_property', 'jira_cloud_get_transitions', 'jira_cloud_do_transition', 'jira_cloud_remove_watcher', 'jira_cloud_add_watcher', 'jira_cloud_link_issues', 'jira_cloud_delete_issue_link', 'jira_cloud_get_issue_link', 'jira_cloud_get_issue_link_types', 'jira_cloud_create_issue_link_type', 'jira_cloud_delete_issue_link_type', 'jira_cloud_get_issue_link_type', 'jira_cloud_update_issue_link_type', 'jira_cloud_export_archived_issues', 'jira_cloud_get_issue_security_schemes', 'jira_cloud_create_issue_security_scheme', 'jira_cloud_get_issue_security_scheme', 'jira_cloud_update_issue_security_scheme', 'jira_cloud_get_issue_security_level_members', 'jira_cloud_get_issue_all_types', 'jira_cloud_match_issues', 'jira_cloud_parse_jql_queries', 'jira_cloud_sanitise_jql_queries', 'jira_cloud_get_project_issue_security_scheme', 'jira_cloud_search_for_issues_using_jql', 'jira_cloud_search_for_issues_using_jql_post', 'jira_cloud_count_issues', 'jira_cloud_search_and_reconsile_issues_using_jql', 'jira_cloud_search_and_reconsile_issues_using_jql_post', 'jira_cloud_get_issue_security_level', 'jira_cloud_get_issue_navigator_default_columns', 'jira_cloud_set_issue_navigator_default_columns', 'jira_cloud_get_version_related_issues', 'jira_cloud_get_version_unresolved_issues', 'jira_cloud_get_workflow_transition_rule_configurations', 'jira_cloud_delete_workflow_transition_property', 'jira_cloud_get_workflow_transition_properties', 'jira_cloud_create_workflow_transition_property', 'jira_cloud_update_workflow_transition_property"
        )


def register_jira_cloud_issue_comment_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-issue-comment"})
    async def atlassian_jira_cloud_issue_comment(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_comments_by_ids', 'jira_cloud_get_comment_property_keys', 'jira_cloud_delete_comment_property', 'jira_cloud_get_comment_property', 'jira_cloud_set_comment_property', 'jira_cloud_get_comments', 'jira_cloud_add_comment', 'jira_cloud_delete_comment', 'jira_cloud_get_comment', 'jira_cloud_update_comment'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud issue comment operations.

        Actions:
          - 'jira_cloud_get_comments_by_ids': Call jira_cloud_get_comments_by_ids
          - 'jira_cloud_get_comment_property_keys': Call jira_cloud_get_comment_property_keys
          - 'jira_cloud_delete_comment_property': Call jira_cloud_delete_comment_property
          - 'jira_cloud_get_comment_property': Call jira_cloud_get_comment_property
          - 'jira_cloud_set_comment_property': Call jira_cloud_set_comment_property
          - 'jira_cloud_get_comments': Call jira_cloud_get_comments
          - 'jira_cloud_add_comment': Call jira_cloud_add_comment
          - 'jira_cloud_delete_comment': Call jira_cloud_delete_comment
          - 'jira_cloud_get_comment': Call jira_cloud_get_comment
          - 'jira_cloud_update_comment': Call jira_cloud_update_comment
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_comments_by_ids":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_comments_by_ids(**kwargs)
        if action == "jira_cloud_get_comment_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_comment_property_keys(**kwargs)
        if action == "jira_cloud_delete_comment_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_comment_property(**kwargs)
        if action == "jira_cloud_get_comment_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_comment_property(**kwargs)
        if action == "jira_cloud_set_comment_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_comment_property(**kwargs)
        if action == "jira_cloud_get_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_comments(**kwargs)
        if action == "jira_cloud_add_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_comment(**kwargs)
        if action == "jira_cloud_delete_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_comment(**kwargs)
        if action == "jira_cloud_get_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_comment(**kwargs)
        if action == "jira_cloud_update_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_comment(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_comments_by_ids', 'jira_cloud_get_comment_property_keys', 'jira_cloud_delete_comment_property', 'jira_cloud_get_comment_property', 'jira_cloud_set_comment_property', 'jira_cloud_get_comments', 'jira_cloud_add_comment', 'jira_cloud_delete_comment', 'jira_cloud_get_comment', 'jira_cloud_update_comment"
        )


def register_jira_cloud_issue_type_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-issue-type"})
    async def atlassian_jira_cloud_issue_type(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_issue_type_mappings_for_contexts', 'jira_cloud_add_issue_types_to_context', 'jira_cloud_remove_issue_types_from_context', 'jira_cloud_get_create_issue_meta_issue_types', 'jira_cloud_get_create_issue_meta_issue_type_id', 'jira_cloud_create_issue_type', 'jira_cloud_get_issue_types_for_project', 'jira_cloud_delete_issue_type', 'jira_cloud_get_issue_type', 'jira_cloud_update_issue_type', 'jira_cloud_get_alternative_issue_types', 'jira_cloud_create_issue_type_avatar', 'jira_cloud_get_issue_type_property_keys', 'jira_cloud_delete_issue_type_property', 'jira_cloud_get_issue_type_property', 'jira_cloud_set_issue_type_property', 'jira_cloud_get_all_issue_type_schemes', 'jira_cloud_create_issue_type_scheme', 'jira_cloud_get_issue_type_schemes_mapping', 'jira_cloud_get_issue_type_scheme_for_projects', 'jira_cloud_assign_issue_type_scheme_to_project', 'jira_cloud_delete_issue_type_scheme', 'jira_cloud_update_issue_type_scheme', 'jira_cloud_add_issue_types_to_issue_type_scheme', 'jira_cloud_reorder_issue_types_in_issue_type_scheme', 'jira_cloud_remove_issue_type_from_issue_type_scheme', 'jira_cloud_get_issue_type_screen_schemes', 'jira_cloud_create_issue_type_screen_scheme', 'jira_cloud_get_issue_type_screen_scheme_mappings', 'jira_cloud_assign_issue_type_screen_scheme_to_project', 'jira_cloud_delete_issue_type_screen_scheme', 'jira_cloud_update_issue_type_screen_scheme', 'jira_cloud_append_mappings_for_issue_type_screen_scheme', 'jira_cloud_get_projects_for_issue_type_screen_scheme', 'jira_cloud_get_project_issue_type_usages_for_status', 'jira_cloud_get_workflow_project_issue_type_usages', 'jira_cloud_delete_workflow_scheme_draft_issue_type', 'jira_cloud_get_workflow_scheme_draft_issue_type', 'jira_cloud_set_workflow_scheme_draft_issue_type', 'jira_cloud_delete_workflow_scheme_issue_type', 'jira_cloud_get_workflow_scheme_issue_type', 'jira_cloud_set_workflow_scheme_issue_type'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud issue type operations.

        Actions:
          - 'jira_cloud_get_issue_type_mappings_for_contexts': Call jira_cloud_get_issue_type_mappings_for_contexts
          - 'jira_cloud_add_issue_types_to_context': Call jira_cloud_add_issue_types_to_context
          - 'jira_cloud_remove_issue_types_from_context': Call jira_cloud_remove_issue_types_from_context
          - 'jira_cloud_get_create_issue_meta_issue_types': Call jira_cloud_get_create_issue_meta_issue_types
          - 'jira_cloud_get_create_issue_meta_issue_type_id': Call jira_cloud_get_create_issue_meta_issue_type_id
          - 'jira_cloud_create_issue_type': Call jira_cloud_create_issue_type
          - 'jira_cloud_get_issue_types_for_project': Call jira_cloud_get_issue_types_for_project
          - 'jira_cloud_delete_issue_type': Call jira_cloud_delete_issue_type
          - 'jira_cloud_get_issue_type': Call jira_cloud_get_issue_type
          - 'jira_cloud_update_issue_type': Call jira_cloud_update_issue_type
          - 'jira_cloud_get_alternative_issue_types': Call jira_cloud_get_alternative_issue_types
          - 'jira_cloud_create_issue_type_avatar': Call jira_cloud_create_issue_type_avatar
          - 'jira_cloud_get_issue_type_property_keys': Call jira_cloud_get_issue_type_property_keys
          - 'jira_cloud_delete_issue_type_property': Call jira_cloud_delete_issue_type_property
          - 'jira_cloud_get_issue_type_property': Call jira_cloud_get_issue_type_property
          - 'jira_cloud_set_issue_type_property': Call jira_cloud_set_issue_type_property
          - 'jira_cloud_get_all_issue_type_schemes': Call jira_cloud_get_all_issue_type_schemes
          - 'jira_cloud_create_issue_type_scheme': Call jira_cloud_create_issue_type_scheme
          - 'jira_cloud_get_issue_type_schemes_mapping': Call jira_cloud_get_issue_type_schemes_mapping
          - 'jira_cloud_get_issue_type_scheme_for_projects': Call jira_cloud_get_issue_type_scheme_for_projects
          - 'jira_cloud_assign_issue_type_scheme_to_project': Call jira_cloud_assign_issue_type_scheme_to_project
          - 'jira_cloud_delete_issue_type_scheme': Call jira_cloud_delete_issue_type_scheme
          - 'jira_cloud_update_issue_type_scheme': Call jira_cloud_update_issue_type_scheme
          - 'jira_cloud_add_issue_types_to_issue_type_scheme': Call jira_cloud_add_issue_types_to_issue_type_scheme
          - 'jira_cloud_reorder_issue_types_in_issue_type_scheme': Call jira_cloud_reorder_issue_types_in_issue_type_scheme
          - 'jira_cloud_remove_issue_type_from_issue_type_scheme': Call jira_cloud_remove_issue_type_from_issue_type_scheme
          - 'jira_cloud_get_issue_type_screen_schemes': Call jira_cloud_get_issue_type_screen_schemes
          - 'jira_cloud_create_issue_type_screen_scheme': Call jira_cloud_create_issue_type_screen_scheme
          - 'jira_cloud_get_issue_type_screen_scheme_mappings': Call jira_cloud_get_issue_type_screen_scheme_mappings
          - 'jira_cloud_assign_issue_type_screen_scheme_to_project': Call jira_cloud_assign_issue_type_screen_scheme_to_project
          - 'jira_cloud_delete_issue_type_screen_scheme': Call jira_cloud_delete_issue_type_screen_scheme
          - 'jira_cloud_update_issue_type_screen_scheme': Call jira_cloud_update_issue_type_screen_scheme
          - 'jira_cloud_append_mappings_for_issue_type_screen_scheme': Call jira_cloud_append_mappings_for_issue_type_screen_scheme
          - 'jira_cloud_get_projects_for_issue_type_screen_scheme': Call jira_cloud_get_projects_for_issue_type_screen_scheme
          - 'jira_cloud_get_project_issue_type_usages_for_status': Call jira_cloud_get_project_issue_type_usages_for_status
          - 'jira_cloud_get_workflow_project_issue_type_usages': Call jira_cloud_get_workflow_project_issue_type_usages
          - 'jira_cloud_delete_workflow_scheme_draft_issue_type': Call jira_cloud_delete_workflow_scheme_draft_issue_type
          - 'jira_cloud_get_workflow_scheme_draft_issue_type': Call jira_cloud_get_workflow_scheme_draft_issue_type
          - 'jira_cloud_set_workflow_scheme_draft_issue_type': Call jira_cloud_set_workflow_scheme_draft_issue_type
          - 'jira_cloud_delete_workflow_scheme_issue_type': Call jira_cloud_delete_workflow_scheme_issue_type
          - 'jira_cloud_get_workflow_scheme_issue_type': Call jira_cloud_get_workflow_scheme_issue_type
          - 'jira_cloud_set_workflow_scheme_issue_type': Call jira_cloud_set_workflow_scheme_issue_type
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_issue_type_mappings_for_contexts":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type_mappings_for_contexts(**kwargs)
        if action == "jira_cloud_add_issue_types_to_context":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_issue_types_to_context(**kwargs)
        if action == "jira_cloud_remove_issue_types_from_context":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_issue_types_from_context(**kwargs)
        if action == "jira_cloud_get_create_issue_meta_issue_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_create_issue_meta_issue_types(**kwargs)
        if action == "jira_cloud_get_create_issue_meta_issue_type_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_create_issue_meta_issue_type_id(**kwargs)
        if action == "jira_cloud_create_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issue_type(**kwargs)
        if action == "jira_cloud_get_issue_types_for_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_types_for_project(**kwargs)
        if action == "jira_cloud_delete_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue_type(**kwargs)
        if action == "jira_cloud_get_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type(**kwargs)
        if action == "jira_cloud_update_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_issue_type(**kwargs)
        if action == "jira_cloud_get_alternative_issue_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_alternative_issue_types(**kwargs)
        if action == "jira_cloud_create_issue_type_avatar":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issue_type_avatar(**kwargs)
        if action == "jira_cloud_get_issue_type_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type_property_keys(**kwargs)
        if action == "jira_cloud_delete_issue_type_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue_type_property(**kwargs)
        if action == "jira_cloud_get_issue_type_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type_property(**kwargs)
        if action == "jira_cloud_set_issue_type_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_issue_type_property(**kwargs)
        if action == "jira_cloud_get_all_issue_type_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_issue_type_schemes(**kwargs)
        if action == "jira_cloud_create_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issue_type_scheme(**kwargs)
        if action == "jira_cloud_get_issue_type_schemes_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type_schemes_mapping(**kwargs)
        if action == "jira_cloud_get_issue_type_scheme_for_projects":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type_scheme_for_projects(**kwargs)
        if action == "jira_cloud_assign_issue_type_scheme_to_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_assign_issue_type_scheme_to_project(**kwargs)
        if action == "jira_cloud_delete_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue_type_scheme(**kwargs)
        if action == "jira_cloud_update_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_issue_type_scheme(**kwargs)
        if action == "jira_cloud_add_issue_types_to_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_issue_types_to_issue_type_scheme(**kwargs)
        if action == "jira_cloud_reorder_issue_types_in_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_reorder_issue_types_in_issue_type_scheme(**kwargs)
        if action == "jira_cloud_remove_issue_type_from_issue_type_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_issue_type_from_issue_type_scheme(**kwargs)
        if action == "jira_cloud_get_issue_type_screen_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type_screen_schemes(**kwargs)
        if action == "jira_cloud_create_issue_type_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_issue_type_screen_scheme(**kwargs)
        if action == "jira_cloud_get_issue_type_screen_scheme_mappings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type_screen_scheme_mappings(**kwargs)
        if action == "jira_cloud_assign_issue_type_screen_scheme_to_project":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_assign_issue_type_screen_scheme_to_project(
                **kwargs
            )
        if action == "jira_cloud_delete_issue_type_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_issue_type_screen_scheme(**kwargs)
        if action == "jira_cloud_update_issue_type_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_issue_type_screen_scheme(**kwargs)
        if action == "jira_cloud_append_mappings_for_issue_type_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_append_mappings_for_issue_type_screen_scheme(
                **kwargs
            )
        if action == "jira_cloud_get_projects_for_issue_type_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_projects_for_issue_type_screen_scheme(**kwargs)
        if action == "jira_cloud_get_project_issue_type_usages_for_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_project_issue_type_usages_for_status(**kwargs)
        if action == "jira_cloud_get_workflow_project_issue_type_usages":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_project_issue_type_usages(**kwargs)
        if action == "jira_cloud_delete_workflow_scheme_draft_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_workflow_scheme_draft_issue_type(**kwargs)
        if action == "jira_cloud_get_workflow_scheme_draft_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_scheme_draft_issue_type(**kwargs)
        if action == "jira_cloud_set_workflow_scheme_draft_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_workflow_scheme_draft_issue_type(**kwargs)
        if action == "jira_cloud_delete_workflow_scheme_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_workflow_scheme_issue_type(**kwargs)
        if action == "jira_cloud_get_workflow_scheme_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_workflow_scheme_issue_type(**kwargs)
        if action == "jira_cloud_set_workflow_scheme_issue_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_workflow_scheme_issue_type(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_issue_type_mappings_for_contexts', 'jira_cloud_add_issue_types_to_context', 'jira_cloud_remove_issue_types_from_context', 'jira_cloud_get_create_issue_meta_issue_types', 'jira_cloud_get_create_issue_meta_issue_type_id', 'jira_cloud_create_issue_type', 'jira_cloud_get_issue_types_for_project', 'jira_cloud_delete_issue_type', 'jira_cloud_get_issue_type', 'jira_cloud_update_issue_type', 'jira_cloud_get_alternative_issue_types', 'jira_cloud_create_issue_type_avatar', 'jira_cloud_get_issue_type_property_keys', 'jira_cloud_delete_issue_type_property', 'jira_cloud_get_issue_type_property', 'jira_cloud_set_issue_type_property', 'jira_cloud_get_all_issue_type_schemes', 'jira_cloud_create_issue_type_scheme', 'jira_cloud_get_issue_type_schemes_mapping', 'jira_cloud_get_issue_type_scheme_for_projects', 'jira_cloud_assign_issue_type_scheme_to_project', 'jira_cloud_delete_issue_type_scheme', 'jira_cloud_update_issue_type_scheme', 'jira_cloud_add_issue_types_to_issue_type_scheme', 'jira_cloud_reorder_issue_types_in_issue_type_scheme', 'jira_cloud_remove_issue_type_from_issue_type_scheme', 'jira_cloud_get_issue_type_screen_schemes', 'jira_cloud_create_issue_type_screen_scheme', 'jira_cloud_get_issue_type_screen_scheme_mappings', 'jira_cloud_assign_issue_type_screen_scheme_to_project', 'jira_cloud_delete_issue_type_screen_scheme', 'jira_cloud_update_issue_type_screen_scheme', 'jira_cloud_append_mappings_for_issue_type_screen_scheme', 'jira_cloud_get_projects_for_issue_type_screen_scheme', 'jira_cloud_get_project_issue_type_usages_for_status', 'jira_cloud_get_workflow_project_issue_type_usages', 'jira_cloud_delete_workflow_scheme_draft_issue_type', 'jira_cloud_get_workflow_scheme_draft_issue_type', 'jira_cloud_set_workflow_scheme_draft_issue_type', 'jira_cloud_delete_workflow_scheme_issue_type', 'jira_cloud_get_workflow_scheme_issue_type', 'jira_cloud_set_workflow_scheme_issue_type"
        )


def register_jira_cloud_issue_link_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-issue-link"})
    async def atlassian_jira_cloud_issue_link(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_delete_remote_issue_link_by_global_id', 'jira_cloud_get_remote_issue_links', 'jira_cloud_create_or_update_remote_issue_link', 'jira_cloud_delete_remote_issue_link_by_id', 'jira_cloud_get_remote_issue_link_by_id', 'jira_cloud_update_remote_issue_link'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud issue link operations.

        Actions:
          - 'jira_cloud_delete_remote_issue_link_by_global_id': Call jira_cloud_delete_remote_issue_link_by_global_id
          - 'jira_cloud_get_remote_issue_links': Call jira_cloud_get_remote_issue_links
          - 'jira_cloud_create_or_update_remote_issue_link': Call jira_cloud_create_or_update_remote_issue_link
          - 'jira_cloud_delete_remote_issue_link_by_id': Call jira_cloud_delete_remote_issue_link_by_id
          - 'jira_cloud_get_remote_issue_link_by_id': Call jira_cloud_get_remote_issue_link_by_id
          - 'jira_cloud_update_remote_issue_link': Call jira_cloud_update_remote_issue_link
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_delete_remote_issue_link_by_global_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_remote_issue_link_by_global_id(**kwargs)
        if action == "jira_cloud_get_remote_issue_links":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_remote_issue_links(**kwargs)
        if action == "jira_cloud_create_or_update_remote_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_or_update_remote_issue_link(**kwargs)
        if action == "jira_cloud_delete_remote_issue_link_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_remote_issue_link_by_id(**kwargs)
        if action == "jira_cloud_get_remote_issue_link_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_remote_issue_link_by_id(**kwargs)
        if action == "jira_cloud_update_remote_issue_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_remote_issue_link(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_delete_remote_issue_link_by_global_id', 'jira_cloud_get_remote_issue_links', 'jira_cloud_create_or_update_remote_issue_link', 'jira_cloud_delete_remote_issue_link_by_id', 'jira_cloud_get_remote_issue_link_by_id', 'jira_cloud_update_remote_issue_link"
        )


def register_jira_cloud_issue_watcher_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-issue-watcher"})
    async def atlassian_jira_cloud_issue_watcher(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_get_issue_watchers'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud issue watcher operations.

        Actions:
          - 'jira_cloud_get_issue_watchers': Call jira_cloud_get_issue_watchers
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_get_issue_watchers":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_watchers(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_get_issue_watchers"
        )


def register_jira_cloud_issue_worklog_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-issue-worklog"})
    async def atlassian_jira_cloud_issue_worklog(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_bulk_delete_worklogs', 'jira_cloud_get_issue_worklog', 'jira_cloud_add_worklog', 'jira_cloud_bulk_move_worklogs', 'jira_cloud_delete_worklog', 'jira_cloud_get_worklog', 'jira_cloud_update_worklog', 'jira_cloud_get_worklog_property_keys', 'jira_cloud_delete_worklog_property', 'jira_cloud_get_worklog_property', 'jira_cloud_set_worklog_property', 'jira_cloud_get_ids_of_worklogs_deleted_since', 'jira_cloud_get_worklogs_for_ids', 'jira_cloud_get_ids_of_worklogs_modified_since', 'jira_cloud_get_worklogs_by_issue_id_and_worklog_id'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud issue worklog operations.

        Actions:
          - 'jira_cloud_bulk_delete_worklogs': Call jira_cloud_bulk_delete_worklogs
          - 'jira_cloud_get_issue_worklog': Call jira_cloud_get_issue_worklog
          - 'jira_cloud_add_worklog': Call jira_cloud_add_worklog
          - 'jira_cloud_bulk_move_worklogs': Call jira_cloud_bulk_move_worklogs
          - 'jira_cloud_delete_worklog': Call jira_cloud_delete_worklog
          - 'jira_cloud_get_worklog': Call jira_cloud_get_worklog
          - 'jira_cloud_update_worklog': Call jira_cloud_update_worklog
          - 'jira_cloud_get_worklog_property_keys': Call jira_cloud_get_worklog_property_keys
          - 'jira_cloud_delete_worklog_property': Call jira_cloud_delete_worklog_property
          - 'jira_cloud_get_worklog_property': Call jira_cloud_get_worklog_property
          - 'jira_cloud_set_worklog_property': Call jira_cloud_set_worklog_property
          - 'jira_cloud_get_ids_of_worklogs_deleted_since': Call jira_cloud_get_ids_of_worklogs_deleted_since
          - 'jira_cloud_get_worklogs_for_ids': Call jira_cloud_get_worklogs_for_ids
          - 'jira_cloud_get_ids_of_worklogs_modified_since': Call jira_cloud_get_ids_of_worklogs_modified_since
          - 'jira_cloud_get_worklogs_by_issue_id_and_worklog_id': Call jira_cloud_get_worklogs_by_issue_id_and_worklog_id
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_bulk_delete_worklogs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_delete_worklogs(**kwargs)
        if action == "jira_cloud_get_issue_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_worklog(**kwargs)
        if action == "jira_cloud_add_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_worklog(**kwargs)
        if action == "jira_cloud_bulk_move_worklogs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_bulk_move_worklogs(**kwargs)
        if action == "jira_cloud_delete_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_worklog(**kwargs)
        if action == "jira_cloud_get_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_worklog(**kwargs)
        if action == "jira_cloud_update_worklog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_worklog(**kwargs)
        if action == "jira_cloud_get_worklog_property_keys":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_worklog_property_keys(**kwargs)
        if action == "jira_cloud_delete_worklog_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_worklog_property(**kwargs)
        if action == "jira_cloud_get_worklog_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_worklog_property(**kwargs)
        if action == "jira_cloud_set_worklog_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_worklog_property(**kwargs)
        if action == "jira_cloud_get_ids_of_worklogs_deleted_since":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_ids_of_worklogs_deleted_since(**kwargs)
        if action == "jira_cloud_get_worklogs_for_ids":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_worklogs_for_ids(**kwargs)
        if action == "jira_cloud_get_ids_of_worklogs_modified_since":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_ids_of_worklogs_modified_since(**kwargs)
        if action == "jira_cloud_get_worklogs_by_issue_id_and_worklog_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_worklogs_by_issue_id_and_worklog_id(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_bulk_delete_worklogs', 'jira_cloud_get_issue_worklog', 'jira_cloud_add_worklog', 'jira_cloud_bulk_move_worklogs', 'jira_cloud_delete_worklog', 'jira_cloud_get_worklog', 'jira_cloud_update_worklog', 'jira_cloud_get_worklog_property_keys', 'jira_cloud_delete_worklog_property', 'jira_cloud_get_worklog_property', 'jira_cloud_set_worklog_property', 'jira_cloud_get_ids_of_worklogs_deleted_since', 'jira_cloud_get_worklogs_for_ids', 'jira_cloud_get_ids_of_worklogs_modified_since', 'jira_cloud_get_worklogs_by_issue_id_and_worklog_id"
        )


def register_jira_cloud_other_tools(mcp: FastMCP):
    @mcp.tool(tags={"jira-cloud-other"})
    async def atlassian_jira_cloud_other(
        action: str = Field(
            description="Action to perform. Must be one of: 'jira_cloud_remove_field_association_scheme_item_parameters', 'jira_cloud_update_field_association_scheme_item_parameters', 'jira_cloud_associate_projects_to_field_association_schemes', 'jira_cloud_get_selected_time_tracking_implementation', 'jira_cloud_select_time_tracking_implementation', 'jira_cloud_get_available_time_tracking_implementations', 'jira_cloud_get_all_gadgets', 'jira_cloud_add_gadget', 'jira_cloud_remove_gadget', 'jira_cloud_update_gadget', 'jira_cloud_get_policy', 'jira_cloud_get_policies', 'jira_cloud_get_events', 'jira_cloud_analyse_expression', 'jira_cloud_evaluate_jira_expression', 'jira_cloud_evaluate_jsis_jira_expression', 'jira_cloud_remove_associations', 'jira_cloud_create_associations', 'jira_cloud_get_default_values', 'jira_cloud_set_default_values', 'jira_cloud_get_custom_field_contexts_for_projects_and_issue_types', 'jira_cloud_get_options_for_context', 'jira_cloud_get_field_configuration_scheme_project_mapping', 'jira_cloud_remove_issue_types_from_global_field_configuration_scheme', 'jira_cloud_get_default_share_scope', 'jira_cloud_set_default_share_scope', 'jira_cloud_reset_columns', 'jira_cloud_get_columns', 'jira_cloud_set_columns', 'jira_cloud_get_license', 'jira_cloud_get_change_logs', 'jira_cloud_get_change_logs_by_ids', 'jira_cloud_notify', 'jira_cloud_remove_vote', 'jira_cloud_get_votes', 'jira_cloud_add_vote', 'jira_cloud_get_security_levels', 'jira_cloud_set_default_levels', 'jira_cloud_get_security_level_members', 'jira_cloud_add_security_level', 'jira_cloud_remove_level', 'jira_cloud_update_security_level', 'jira_cloud_add_security_level_members', 'jira_cloud_remove_member_from_security_level', 'jira_cloud_get_issue_type_screen_scheme_project_associations', 'jira_cloud_remove_mappings_from_issue_type_screen_scheme', 'jira_cloud_get_auto_complete', 'jira_cloud_get_auto_complete_post', 'jira_cloud_get_precomputations', 'jira_cloud_update_precomputations', 'jira_cloud_get_precomputations_by_id', 'jira_cloud_migrate_queries', 'jira_cloud_get_all_labels', 'jira_cloud_get_approximate_license_count', 'jira_cloud_get_approximate_application_license_count', 'jira_cloud_remove_preference', 'jira_cloud_get_preference', 'jira_cloud_set_preference', 'jira_cloud_get_locale', 'jira_cloud_set_locale', 'jira_cloud_add_notifications', 'jira_cloud_get_plans', 'jira_cloud_create_plan', 'jira_cloud_get_plan', 'jira_cloud_update_plan', 'jira_cloud_archive_plan', 'jira_cloud_duplicate_plan', 'jira_cloud_get_teams', 'jira_cloud_add_atlassian_team', 'jira_cloud_remove_atlassian_team', 'jira_cloud_get_atlassian_team', 'jira_cloud_update_atlassian_team', 'jira_cloud_create_plan_only_team', 'jira_cloud_delete_plan_only_team', 'jira_cloud_get_plan_only_team', 'jira_cloud_update_plan_only_team', 'jira_cloud_trash_plan', 'jira_cloud_get_priorities', 'jira_cloud_move_priorities', 'jira_cloud_search_priorities', 'jira_cloud_suggested_priorities_for_mappings', 'jira_cloud_edit_template', 'jira_cloud_live_template', 'jira_cloud_remove_template', 'jira_cloud_save_template', 'jira_cloud_get_recent', 'jira_cloud_restore', 'jira_cloud_delete_actor', 'jira_cloud_set_actors', 'jira_cloud_get_hierarchy', 'jira_cloud_redact', 'jira_cloud_get_server_info', 'jira_cloud_search', 'jira_cloud_get_task', 'jira_cloud_cancel_task', 'jira_cloud_get_ui_modifications', 'jira_cloud_create_ui_modification', 'jira_cloud_delete_ui_modification', 'jira_cloud_update_ui_modification', 'jira_cloud_get_related_work', 'jira_cloud_create_related_work', 'jira_cloud_update_related_work', 'jira_cloud_delete_related_work', 'jira_cloud_delete_webhook_by_id', 'jira_cloud_get_dynamic_webhooks_for_app', 'jira_cloud_register_dynamic_webhooks', 'jira_cloud_get_failed_webhooks', 'jira_cloud_refresh_webhooks', 'jira_cloud_update_workflow_transition_rule_configurations', 'jira_cloud_delete_workflow_transition_rule_configurations', 'jira_cloud_get_default_editor', 'jira_cloud_addon_properties_resource_get_addon_properties_get', 'jira_cloud_addon_properties_resource_delete_addon_property_delete', 'jira_cloud_addon_properties_resource_get_addon_property_get', 'jira_cloud_addon_properties_resource_put_addon_property_put', 'jira_cloud_dynamic_modules_resource_remove_modules_delete', 'jira_cloud_dynamic_modules_resource_get_modules_get', 'jira_cloud_dynamic_modules_resource_register_modules_post', 'jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put', 'jira_cloud_migration_resource_update_entity_properties_value_put', 'jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get', 'jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post', 'jira_cloud_service_registry_resource_services_get'"
        ),
        client=Depends(get_jira_cloud_client),
    ) -> dict:
        """Manage jira cloud other operations.

        Actions:
          - 'jira_cloud_remove_field_association_scheme_item_parameters': Call jira_cloud_remove_field_association_scheme_item_parameters
          - 'jira_cloud_update_field_association_scheme_item_parameters': Call jira_cloud_update_field_association_scheme_item_parameters
          - 'jira_cloud_associate_projects_to_field_association_schemes': Call jira_cloud_associate_projects_to_field_association_schemes
          - 'jira_cloud_get_selected_time_tracking_implementation': Call jira_cloud_get_selected_time_tracking_implementation
          - 'jira_cloud_select_time_tracking_implementation': Call jira_cloud_select_time_tracking_implementation
          - 'jira_cloud_get_available_time_tracking_implementations': Call jira_cloud_get_available_time_tracking_implementations
          - 'jira_cloud_get_all_gadgets': Call jira_cloud_get_all_gadgets
          - 'jira_cloud_add_gadget': Call jira_cloud_add_gadget
          - 'jira_cloud_remove_gadget': Call jira_cloud_remove_gadget
          - 'jira_cloud_update_gadget': Call jira_cloud_update_gadget
          - 'jira_cloud_get_policy': Call jira_cloud_get_policy
          - 'jira_cloud_get_policies': Call jira_cloud_get_policies
          - 'jira_cloud_get_events': Call jira_cloud_get_events
          - 'jira_cloud_analyse_expression': Call jira_cloud_analyse_expression
          - 'jira_cloud_evaluate_jira_expression': Call jira_cloud_evaluate_jira_expression
          - 'jira_cloud_evaluate_jsis_jira_expression': Call jira_cloud_evaluate_jsis_jira_expression
          - 'jira_cloud_remove_associations': Call jira_cloud_remove_associations
          - 'jira_cloud_create_associations': Call jira_cloud_create_associations
          - 'jira_cloud_get_default_values': Call jira_cloud_get_default_values
          - 'jira_cloud_set_default_values': Call jira_cloud_set_default_values
          - 'jira_cloud_get_custom_field_contexts_for_projects_and_issue_types': Call jira_cloud_get_custom_field_contexts_for_projects_and_issue_types
          - 'jira_cloud_get_options_for_context': Call jira_cloud_get_options_for_context
          - 'jira_cloud_get_field_configuration_scheme_project_mapping': Call jira_cloud_get_field_configuration_scheme_project_mapping
          - 'jira_cloud_remove_issue_types_from_global_field_configuration_scheme': Call jira_cloud_remove_issue_types_from_global_field_configuration_scheme
          - 'jira_cloud_get_default_share_scope': Call jira_cloud_get_default_share_scope
          - 'jira_cloud_set_default_share_scope': Call jira_cloud_set_default_share_scope
          - 'jira_cloud_reset_columns': Call jira_cloud_reset_columns
          - 'jira_cloud_get_columns': Call jira_cloud_get_columns
          - 'jira_cloud_set_columns': Call jira_cloud_set_columns
          - 'jira_cloud_get_license': Call jira_cloud_get_license
          - 'jira_cloud_get_change_logs': Call jira_cloud_get_change_logs
          - 'jira_cloud_get_change_logs_by_ids': Call jira_cloud_get_change_logs_by_ids
          - 'jira_cloud_notify': Call jira_cloud_notify
          - 'jira_cloud_remove_vote': Call jira_cloud_remove_vote
          - 'jira_cloud_get_votes': Call jira_cloud_get_votes
          - 'jira_cloud_add_vote': Call jira_cloud_add_vote
          - 'jira_cloud_get_security_levels': Call jira_cloud_get_security_levels
          - 'jira_cloud_set_default_levels': Call jira_cloud_set_default_levels
          - 'jira_cloud_get_security_level_members': Call jira_cloud_get_security_level_members
          - 'jira_cloud_add_security_level': Call jira_cloud_add_security_level
          - 'jira_cloud_remove_level': Call jira_cloud_remove_level
          - 'jira_cloud_update_security_level': Call jira_cloud_update_security_level
          - 'jira_cloud_add_security_level_members': Call jira_cloud_add_security_level_members
          - 'jira_cloud_remove_member_from_security_level': Call jira_cloud_remove_member_from_security_level
          - 'jira_cloud_get_issue_type_screen_scheme_project_associations': Call jira_cloud_get_issue_type_screen_scheme_project_associations
          - 'jira_cloud_remove_mappings_from_issue_type_screen_scheme': Call jira_cloud_remove_mappings_from_issue_type_screen_scheme
          - 'jira_cloud_get_auto_complete': Call jira_cloud_get_auto_complete
          - 'jira_cloud_get_auto_complete_post': Call jira_cloud_get_auto_complete_post
          - 'jira_cloud_get_precomputations': Call jira_cloud_get_precomputations
          - 'jira_cloud_update_precomputations': Call jira_cloud_update_precomputations
          - 'jira_cloud_get_precomputations_by_id': Call jira_cloud_get_precomputations_by_id
          - 'jira_cloud_migrate_queries': Call jira_cloud_migrate_queries
          - 'jira_cloud_get_all_labels': Call jira_cloud_get_all_labels
          - 'jira_cloud_get_approximate_license_count': Call jira_cloud_get_approximate_license_count
          - 'jira_cloud_get_approximate_application_license_count': Call jira_cloud_get_approximate_application_license_count
          - 'jira_cloud_remove_preference': Call jira_cloud_remove_preference
          - 'jira_cloud_get_preference': Call jira_cloud_get_preference
          - 'jira_cloud_set_preference': Call jira_cloud_set_preference
          - 'jira_cloud_get_locale': Call jira_cloud_get_locale
          - 'jira_cloud_set_locale': Call jira_cloud_set_locale
          - 'jira_cloud_add_notifications': Call jira_cloud_add_notifications
          - 'jira_cloud_get_plans': Call jira_cloud_get_plans
          - 'jira_cloud_create_plan': Call jira_cloud_create_plan
          - 'jira_cloud_get_plan': Call jira_cloud_get_plan
          - 'jira_cloud_update_plan': Call jira_cloud_update_plan
          - 'jira_cloud_archive_plan': Call jira_cloud_archive_plan
          - 'jira_cloud_duplicate_plan': Call jira_cloud_duplicate_plan
          - 'jira_cloud_get_teams': Call jira_cloud_get_teams
          - 'jira_cloud_add_atlassian_team': Call jira_cloud_add_atlassian_team
          - 'jira_cloud_remove_atlassian_team': Call jira_cloud_remove_atlassian_team
          - 'jira_cloud_get_atlassian_team': Call jira_cloud_get_atlassian_team
          - 'jira_cloud_update_atlassian_team': Call jira_cloud_update_atlassian_team
          - 'jira_cloud_create_plan_only_team': Call jira_cloud_create_plan_only_team
          - 'jira_cloud_delete_plan_only_team': Call jira_cloud_delete_plan_only_team
          - 'jira_cloud_get_plan_only_team': Call jira_cloud_get_plan_only_team
          - 'jira_cloud_update_plan_only_team': Call jira_cloud_update_plan_only_team
          - 'jira_cloud_trash_plan': Call jira_cloud_trash_plan
          - 'jira_cloud_get_priorities': Call jira_cloud_get_priorities
          - 'jira_cloud_move_priorities': Call jira_cloud_move_priorities
          - 'jira_cloud_search_priorities': Call jira_cloud_search_priorities
          - 'jira_cloud_suggested_priorities_for_mappings': Call jira_cloud_suggested_priorities_for_mappings
          - 'jira_cloud_edit_template': Call jira_cloud_edit_template
          - 'jira_cloud_live_template': Call jira_cloud_live_template
          - 'jira_cloud_remove_template': Call jira_cloud_remove_template
          - 'jira_cloud_save_template': Call jira_cloud_save_template
          - 'jira_cloud_get_recent': Call jira_cloud_get_recent
          - 'jira_cloud_restore': Call jira_cloud_restore
          - 'jira_cloud_delete_actor': Call jira_cloud_delete_actor
          - 'jira_cloud_set_actors': Call jira_cloud_set_actors
          - 'jira_cloud_get_hierarchy': Call jira_cloud_get_hierarchy
          - 'jira_cloud_redact': Call jira_cloud_redact
          - 'jira_cloud_get_server_info': Call jira_cloud_get_server_info
          - 'jira_cloud_search': Call jira_cloud_search
          - 'jira_cloud_get_task': Call jira_cloud_get_task
          - 'jira_cloud_cancel_task': Call jira_cloud_cancel_task
          - 'jira_cloud_get_ui_modifications': Call jira_cloud_get_ui_modifications
          - 'jira_cloud_create_ui_modification': Call jira_cloud_create_ui_modification
          - 'jira_cloud_delete_ui_modification': Call jira_cloud_delete_ui_modification
          - 'jira_cloud_update_ui_modification': Call jira_cloud_update_ui_modification
          - 'jira_cloud_get_related_work': Call jira_cloud_get_related_work
          - 'jira_cloud_create_related_work': Call jira_cloud_create_related_work
          - 'jira_cloud_update_related_work': Call jira_cloud_update_related_work
          - 'jira_cloud_delete_related_work': Call jira_cloud_delete_related_work
          - 'jira_cloud_delete_webhook_by_id': Call jira_cloud_delete_webhook_by_id
          - 'jira_cloud_get_dynamic_webhooks_for_app': Call jira_cloud_get_dynamic_webhooks_for_app
          - 'jira_cloud_register_dynamic_webhooks': Call jira_cloud_register_dynamic_webhooks
          - 'jira_cloud_get_failed_webhooks': Call jira_cloud_get_failed_webhooks
          - 'jira_cloud_refresh_webhooks': Call jira_cloud_refresh_webhooks
          - 'jira_cloud_update_workflow_transition_rule_configurations': Call jira_cloud_update_workflow_transition_rule_configurations
          - 'jira_cloud_delete_workflow_transition_rule_configurations': Call jira_cloud_delete_workflow_transition_rule_configurations
          - 'jira_cloud_get_default_editor': Call jira_cloud_get_default_editor
          - 'jira_cloud_addon_properties_resource_get_addon_properties_get': Call jira_cloud_addon_properties_resource_get_addon_properties_get
          - 'jira_cloud_addon_properties_resource_delete_addon_property_delete': Call jira_cloud_addon_properties_resource_delete_addon_property_delete
          - 'jira_cloud_addon_properties_resource_get_addon_property_get': Call jira_cloud_addon_properties_resource_get_addon_property_get
          - 'jira_cloud_addon_properties_resource_put_addon_property_put': Call jira_cloud_addon_properties_resource_put_addon_property_put
          - 'jira_cloud_dynamic_modules_resource_remove_modules_delete': Call jira_cloud_dynamic_modules_resource_remove_modules_delete
          - 'jira_cloud_dynamic_modules_resource_get_modules_get': Call jira_cloud_dynamic_modules_resource_get_modules_get
          - 'jira_cloud_dynamic_modules_resource_register_modules_post': Call jira_cloud_dynamic_modules_resource_register_modules_post
          - 'jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put': Call jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put
          - 'jira_cloud_migration_resource_update_entity_properties_value_put': Call jira_cloud_migration_resource_update_entity_properties_value_put
          - 'jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get': Call jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get
          - 'jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post': Call jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post
          - 'jira_cloud_service_registry_resource_services_get': Call jira_cloud_service_registry_resource_services_get
        """
        kwargs: dict[str, Any]
        if action == "jira_cloud_remove_field_association_scheme_item_parameters":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_field_association_scheme_item_parameters(
                **kwargs
            )
        if action == "jira_cloud_update_field_association_scheme_item_parameters":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_field_association_scheme_item_parameters(
                **kwargs
            )
        if action == "jira_cloud_associate_projects_to_field_association_schemes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_associate_projects_to_field_association_schemes(
                **kwargs
            )
        if action == "jira_cloud_get_selected_time_tracking_implementation":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_selected_time_tracking_implementation(**kwargs)
        if action == "jira_cloud_select_time_tracking_implementation":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_select_time_tracking_implementation(**kwargs)
        if action == "jira_cloud_get_available_time_tracking_implementations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_available_time_tracking_implementations(
                **kwargs
            )
        if action == "jira_cloud_get_all_gadgets":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_gadgets(**kwargs)
        if action == "jira_cloud_add_gadget":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_gadget(**kwargs)
        if action == "jira_cloud_remove_gadget":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_gadget(**kwargs)
        if action == "jira_cloud_update_gadget":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_gadget(**kwargs)
        if action == "jira_cloud_get_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_policy(**kwargs)
        if action == "jira_cloud_get_policies":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_policies(**kwargs)
        if action == "jira_cloud_get_events":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_events(**kwargs)
        if action == "jira_cloud_analyse_expression":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_analyse_expression(**kwargs)
        if action == "jira_cloud_evaluate_jira_expression":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_evaluate_jira_expression(**kwargs)
        if action == "jira_cloud_evaluate_jsis_jira_expression":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_evaluate_jsis_jira_expression(**kwargs)
        if action == "jira_cloud_remove_associations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_associations(**kwargs)
        if action == "jira_cloud_create_associations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_associations(**kwargs)
        if action == "jira_cloud_get_default_values":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_default_values(**kwargs)
        if action == "jira_cloud_set_default_values":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_default_values(**kwargs)
        if (
            action
            == "jira_cloud_get_custom_field_contexts_for_projects_and_issue_types"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_custom_field_contexts_for_projects_and_issue_types(
                **kwargs
            )
        if action == "jira_cloud_get_options_for_context":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_options_for_context(**kwargs)
        if action == "jira_cloud_get_field_configuration_scheme_project_mapping":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_field_configuration_scheme_project_mapping(
                **kwargs
            )
        if (
            action
            == "jira_cloud_remove_issue_types_from_global_field_configuration_scheme"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_issue_types_from_global_field_configuration_scheme(
                **kwargs
            )
        if action == "jira_cloud_get_default_share_scope":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_default_share_scope(**kwargs)
        if action == "jira_cloud_set_default_share_scope":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_default_share_scope(**kwargs)
        if action == "jira_cloud_reset_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_reset_columns(**kwargs)
        if action == "jira_cloud_get_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_columns(**kwargs)
        if action == "jira_cloud_set_columns":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_columns(**kwargs)
        if action == "jira_cloud_get_license":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_license(**kwargs)
        if action == "jira_cloud_get_change_logs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_change_logs(**kwargs)
        if action == "jira_cloud_get_change_logs_by_ids":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_change_logs_by_ids(**kwargs)
        if action == "jira_cloud_notify":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_notify(**kwargs)
        if action == "jira_cloud_remove_vote":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_vote(**kwargs)
        if action == "jira_cloud_get_votes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_votes(**kwargs)
        if action == "jira_cloud_add_vote":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_vote(**kwargs)
        if action == "jira_cloud_get_security_levels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_security_levels(**kwargs)
        if action == "jira_cloud_set_default_levels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_default_levels(**kwargs)
        if action == "jira_cloud_get_security_level_members":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_security_level_members(**kwargs)
        if action == "jira_cloud_add_security_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_security_level(**kwargs)
        if action == "jira_cloud_remove_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_level(**kwargs)
        if action == "jira_cloud_update_security_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_security_level(**kwargs)
        if action == "jira_cloud_add_security_level_members":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_security_level_members(**kwargs)
        if action == "jira_cloud_remove_member_from_security_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_member_from_security_level(**kwargs)
        if action == "jira_cloud_get_issue_type_screen_scheme_project_associations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_issue_type_screen_scheme_project_associations(
                **kwargs
            )
        if action == "jira_cloud_remove_mappings_from_issue_type_screen_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_mappings_from_issue_type_screen_scheme(
                **kwargs
            )
        if action == "jira_cloud_get_auto_complete":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_auto_complete(**kwargs)
        if action == "jira_cloud_get_auto_complete_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_auto_complete_post(**kwargs)
        if action == "jira_cloud_get_precomputations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_precomputations(**kwargs)
        if action == "jira_cloud_update_precomputations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_precomputations(**kwargs)
        if action == "jira_cloud_get_precomputations_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_precomputations_by_id(**kwargs)
        if action == "jira_cloud_migrate_queries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_migrate_queries(**kwargs)
        if action == "jira_cloud_get_all_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_all_labels(**kwargs)
        if action == "jira_cloud_get_approximate_license_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_approximate_license_count(**kwargs)
        if action == "jira_cloud_get_approximate_application_license_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_approximate_application_license_count(**kwargs)
        if action == "jira_cloud_remove_preference":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_preference(**kwargs)
        if action == "jira_cloud_get_preference":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_preference(**kwargs)
        if action == "jira_cloud_set_preference":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_preference(**kwargs)
        if action == "jira_cloud_get_locale":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_locale(**kwargs)
        if action == "jira_cloud_set_locale":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_locale(**kwargs)
        if action == "jira_cloud_add_notifications":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_notifications(**kwargs)
        if action == "jira_cloud_get_plans":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_plans(**kwargs)
        if action == "jira_cloud_create_plan":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_plan(**kwargs)
        if action == "jira_cloud_get_plan":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_plan(**kwargs)
        if action == "jira_cloud_update_plan":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_plan(**kwargs)
        if action == "jira_cloud_archive_plan":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_archive_plan(**kwargs)
        if action == "jira_cloud_duplicate_plan":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_duplicate_plan(**kwargs)
        if action == "jira_cloud_get_teams":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_teams(**kwargs)
        if action == "jira_cloud_add_atlassian_team":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_add_atlassian_team(**kwargs)
        if action == "jira_cloud_remove_atlassian_team":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_atlassian_team(**kwargs)
        if action == "jira_cloud_get_atlassian_team":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_atlassian_team(**kwargs)
        if action == "jira_cloud_update_atlassian_team":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_atlassian_team(**kwargs)
        if action == "jira_cloud_create_plan_only_team":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_plan_only_team(**kwargs)
        if action == "jira_cloud_delete_plan_only_team":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_plan_only_team(**kwargs)
        if action == "jira_cloud_get_plan_only_team":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_plan_only_team(**kwargs)
        if action == "jira_cloud_update_plan_only_team":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_plan_only_team(**kwargs)
        if action == "jira_cloud_trash_plan":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_trash_plan(**kwargs)
        if action == "jira_cloud_get_priorities":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_priorities(**kwargs)
        if action == "jira_cloud_move_priorities":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_move_priorities(**kwargs)
        if action == "jira_cloud_search_priorities":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search_priorities(**kwargs)
        if action == "jira_cloud_suggested_priorities_for_mappings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_suggested_priorities_for_mappings(**kwargs)
        if action == "jira_cloud_edit_template":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_edit_template(**kwargs)
        if action == "jira_cloud_live_template":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_live_template(**kwargs)
        if action == "jira_cloud_remove_template":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_remove_template(**kwargs)
        if action == "jira_cloud_save_template":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_save_template(**kwargs)
        if action == "jira_cloud_get_recent":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_recent(**kwargs)
        if action == "jira_cloud_restore":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_restore(**kwargs)
        if action == "jira_cloud_delete_actor":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_actor(**kwargs)
        if action == "jira_cloud_set_actors":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_set_actors(**kwargs)
        if action == "jira_cloud_get_hierarchy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_hierarchy(**kwargs)
        if action == "jira_cloud_redact":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_redact(**kwargs)
        if action == "jira_cloud_get_server_info":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_server_info(**kwargs)
        if action == "jira_cloud_search":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_search(**kwargs)
        if action == "jira_cloud_get_task":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_task(**kwargs)
        if action == "jira_cloud_cancel_task":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_cancel_task(**kwargs)
        if action == "jira_cloud_get_ui_modifications":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_ui_modifications(**kwargs)
        if action == "jira_cloud_create_ui_modification":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_ui_modification(**kwargs)
        if action == "jira_cloud_delete_ui_modification":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_ui_modification(**kwargs)
        if action == "jira_cloud_update_ui_modification":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_ui_modification(**kwargs)
        if action == "jira_cloud_get_related_work":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_related_work(**kwargs)
        if action == "jira_cloud_create_related_work":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_create_related_work(**kwargs)
        if action == "jira_cloud_update_related_work":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_related_work(**kwargs)
        if action == "jira_cloud_delete_related_work":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_related_work(**kwargs)
        if action == "jira_cloud_delete_webhook_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_webhook_by_id(**kwargs)
        if action == "jira_cloud_get_dynamic_webhooks_for_app":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_dynamic_webhooks_for_app(**kwargs)
        if action == "jira_cloud_register_dynamic_webhooks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_register_dynamic_webhooks(**kwargs)
        if action == "jira_cloud_get_failed_webhooks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_failed_webhooks(**kwargs)
        if action == "jira_cloud_refresh_webhooks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_refresh_webhooks(**kwargs)
        if action == "jira_cloud_update_workflow_transition_rule_configurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_update_workflow_transition_rule_configurations(
                **kwargs
            )
        if action == "jira_cloud_delete_workflow_transition_rule_configurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_delete_workflow_transition_rule_configurations(
                **kwargs
            )
        if action == "jira_cloud_get_default_editor":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_get_default_editor(**kwargs)
        if action == "jira_cloud_addon_properties_resource_get_addon_properties_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_addon_properties_resource_get_addon_properties_get(
                **kwargs
            )
        if (
            action
            == "jira_cloud_addon_properties_resource_delete_addon_property_delete"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_addon_properties_resource_delete_addon_property_delete(
                **kwargs
            )
        if action == "jira_cloud_addon_properties_resource_get_addon_property_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_addon_properties_resource_get_addon_property_get(
                **kwargs
            )
        if action == "jira_cloud_addon_properties_resource_put_addon_property_put":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_addon_properties_resource_put_addon_property_put(
                **kwargs
            )
        if action == "jira_cloud_dynamic_modules_resource_remove_modules_delete":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_dynamic_modules_resource_remove_modules_delete(
                **kwargs
            )
        if action == "jira_cloud_dynamic_modules_resource_get_modules_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_dynamic_modules_resource_get_modules_get(**kwargs)
        if action == "jira_cloud_dynamic_modules_resource_register_modules_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_dynamic_modules_resource_register_modules_post(
                **kwargs
            )
        if (
            action
            == "jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put(
                **kwargs
            )
        if action == "jira_cloud_migration_resource_update_entity_properties_value_put":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return (
                client.jira_cloud_migration_resource_update_entity_properties_value_put(
                    **kwargs
                )
            )
        if (
            action
            == "jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get(
                **kwargs
            )
        if (
            action
            == "jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post(
                **kwargs
            )
        if action == "jira_cloud_service_registry_resource_services_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.jira_cloud_service_registry_resource_services_get(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: jira_cloud_remove_field_association_scheme_item_parameters', 'jira_cloud_update_field_association_scheme_item_parameters', 'jira_cloud_associate_projects_to_field_association_schemes', 'jira_cloud_get_selected_time_tracking_implementation', 'jira_cloud_select_time_tracking_implementation', 'jira_cloud_get_available_time_tracking_implementations', 'jira_cloud_get_all_gadgets', 'jira_cloud_add_gadget', 'jira_cloud_remove_gadget', 'jira_cloud_update_gadget', 'jira_cloud_get_policy', 'jira_cloud_get_policies', 'jira_cloud_get_events', 'jira_cloud_analyse_expression', 'jira_cloud_evaluate_jira_expression', 'jira_cloud_evaluate_jsis_jira_expression', 'jira_cloud_remove_associations', 'jira_cloud_create_associations', 'jira_cloud_get_default_values', 'jira_cloud_set_default_values', 'jira_cloud_get_custom_field_contexts_for_projects_and_issue_types', 'jira_cloud_get_options_for_context', 'jira_cloud_get_field_configuration_scheme_project_mapping', 'jira_cloud_remove_issue_types_from_global_field_configuration_scheme', 'jira_cloud_get_default_share_scope', 'jira_cloud_set_default_share_scope', 'jira_cloud_reset_columns', 'jira_cloud_get_columns', 'jira_cloud_set_columns', 'jira_cloud_get_license', 'jira_cloud_get_change_logs', 'jira_cloud_get_change_logs_by_ids', 'jira_cloud_notify', 'jira_cloud_remove_vote', 'jira_cloud_get_votes', 'jira_cloud_add_vote', 'jira_cloud_get_security_levels', 'jira_cloud_set_default_levels', 'jira_cloud_get_security_level_members', 'jira_cloud_add_security_level', 'jira_cloud_remove_level', 'jira_cloud_update_security_level', 'jira_cloud_add_security_level_members', 'jira_cloud_remove_member_from_security_level', 'jira_cloud_get_issue_type_screen_scheme_project_associations', 'jira_cloud_remove_mappings_from_issue_type_screen_scheme', 'jira_cloud_get_auto_complete', 'jira_cloud_get_auto_complete_post', 'jira_cloud_get_precomputations', 'jira_cloud_update_precomputations', 'jira_cloud_get_precomputations_by_id', 'jira_cloud_migrate_queries', 'jira_cloud_get_all_labels', 'jira_cloud_get_approximate_license_count', 'jira_cloud_get_approximate_application_license_count', 'jira_cloud_remove_preference', 'jira_cloud_get_preference', 'jira_cloud_set_preference', 'jira_cloud_get_locale', 'jira_cloud_set_locale', 'jira_cloud_add_notifications', 'jira_cloud_get_plans', 'jira_cloud_create_plan', 'jira_cloud_get_plan', 'jira_cloud_update_plan', 'jira_cloud_archive_plan', 'jira_cloud_duplicate_plan', 'jira_cloud_get_teams', 'jira_cloud_add_atlassian_team', 'jira_cloud_remove_atlassian_team', 'jira_cloud_get_atlassian_team', 'jira_cloud_update_atlassian_team', 'jira_cloud_create_plan_only_team', 'jira_cloud_delete_plan_only_team', 'jira_cloud_get_plan_only_team', 'jira_cloud_update_plan_only_team', 'jira_cloud_trash_plan', 'jira_cloud_get_priorities', 'jira_cloud_move_priorities', 'jira_cloud_search_priorities', 'jira_cloud_suggested_priorities_for_mappings', 'jira_cloud_edit_template', 'jira_cloud_live_template', 'jira_cloud_remove_template', 'jira_cloud_save_template', 'jira_cloud_get_recent', 'jira_cloud_restore', 'jira_cloud_delete_actor', 'jira_cloud_set_actors', 'jira_cloud_get_hierarchy', 'jira_cloud_redact', 'jira_cloud_get_server_info', 'jira_cloud_search', 'jira_cloud_get_task', 'jira_cloud_cancel_task', 'jira_cloud_get_ui_modifications', 'jira_cloud_create_ui_modification', 'jira_cloud_delete_ui_modification', 'jira_cloud_update_ui_modification', 'jira_cloud_get_related_work', 'jira_cloud_create_related_work', 'jira_cloud_update_related_work', 'jira_cloud_delete_related_work', 'jira_cloud_delete_webhook_by_id', 'jira_cloud_get_dynamic_webhooks_for_app', 'jira_cloud_register_dynamic_webhooks', 'jira_cloud_get_failed_webhooks', 'jira_cloud_refresh_webhooks', 'jira_cloud_update_workflow_transition_rule_configurations', 'jira_cloud_delete_workflow_transition_rule_configurations', 'jira_cloud_get_default_editor', 'jira_cloud_addon_properties_resource_get_addon_properties_get', 'jira_cloud_addon_properties_resource_delete_addon_property_delete', 'jira_cloud_addon_properties_resource_get_addon_property_get', 'jira_cloud_addon_properties_resource_put_addon_property_put', 'jira_cloud_dynamic_modules_resource_remove_modules_delete', 'jira_cloud_dynamic_modules_resource_get_modules_get', 'jira_cloud_dynamic_modules_resource_register_modules_post', 'jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put', 'jira_cloud_migration_resource_update_entity_properties_value_put', 'jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get', 'jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post', 'jira_cloud_service_registry_resource_services_get"
        )


def register_confluence_cloud_other_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-other"})
    async def atlassian_confluence_cloud_other(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_get_admin_key', 'confluence_cloud_enable_admin_key', 'confluence_cloud_disable_admin_key', 'confluence_cloud_get_blog_posts', 'confluence_cloud_create_blog_post', 'confluence_cloud_get_blog_post_by_id', 'confluence_cloud_update_blog_post', 'confluence_cloud_delete_blog_post', 'confluence_cloud_get_custom_content_by_type_in_blog_post', 'confluence_cloud_get_blog_post_like_count', 'confluence_cloud_get_blogpost_content_properties', 'confluence_cloud_create_blogpost_property', 'confluence_cloud_get_blogpost_content_properties_by_id', 'confluence_cloud_update_blogpost_property_by_id', 'confluence_cloud_delete_blogpost_property_by_id', 'confluence_cloud_get_blog_post_operations', 'confluence_cloud_get_blog_post_versions', 'confluence_cloud_get_blog_post_version_details', 'confluence_cloud_convert_content_ids_to_content_types', 'confluence_cloud_get_custom_content_by_type', 'confluence_cloud_create_custom_content', 'confluence_cloud_get_custom_content_by_id', 'confluence_cloud_update_custom_content', 'confluence_cloud_delete_custom_content', 'confluence_cloud_get_custom_content_comments', 'confluence_cloud_get_custom_content_operations', 'confluence_cloud_get_custom_content_content_properties', 'confluence_cloud_get_custom_content_content_properties_by_id', 'confluence_cloud_post_redact_blog', 'confluence_cloud_create_whiteboard', 'confluence_cloud_get_whiteboard_by_id', 'confluence_cloud_delete_whiteboard', 'confluence_cloud_get_whiteboard_content_properties', 'confluence_cloud_create_whiteboard_property', 'confluence_cloud_get_whiteboard_content_properties_by_id', 'confluence_cloud_update_whiteboard_property_by_id', 'confluence_cloud_delete_whiteboard_property_by_id', 'confluence_cloud_get_whiteboard_operations', 'confluence_cloud_get_whiteboard_direct_children', 'confluence_cloud_get_whiteboard_descendants', 'confluence_cloud_get_whiteboard_ancestors', 'confluence_cloud_create_database', 'confluence_cloud_get_database_by_id', 'confluence_cloud_delete_database', 'confluence_cloud_get_database_content_properties', 'confluence_cloud_create_database_property', 'confluence_cloud_get_database_content_properties_by_id', 'confluence_cloud_update_database_property_by_id', 'confluence_cloud_delete_database_property_by_id', 'confluence_cloud_get_database_operations', 'confluence_cloud_get_database_direct_children', 'confluence_cloud_get_database_descendants', 'confluence_cloud_get_database_ancestors', 'confluence_cloud_create_smart_link', 'confluence_cloud_get_smart_link_by_id', 'confluence_cloud_delete_smart_link', 'confluence_cloud_get_smart_link_content_properties', 'confluence_cloud_create_smart_link_property', 'confluence_cloud_get_smart_link_content_properties_by_id', 'confluence_cloud_update_smart_link_property_by_id', 'confluence_cloud_delete_smart_link_property_by_id', 'confluence_cloud_get_smart_link_operations', 'confluence_cloud_get_smart_link_direct_children', 'confluence_cloud_get_smart_link_descendants', 'confluence_cloud_get_smart_link_ancestors', 'confluence_cloud_create_folder', 'confluence_cloud_get_folder_by_id', 'confluence_cloud_delete_folder', 'confluence_cloud_get_folder_content_properties', 'confluence_cloud_create_folder_property', 'confluence_cloud_get_folder_content_properties_by_id', 'confluence_cloud_update_folder_property_by_id', 'confluence_cloud_delete_folder_property_by_id', 'confluence_cloud_get_folder_operations', 'confluence_cloud_get_folder_direct_children', 'confluence_cloud_get_folder_descendants', 'confluence_cloud_get_folder_ancestors', 'confluence_cloud_get_custom_content_versions', 'confluence_cloud_get_custom_content_version_details', 'confluence_cloud_get_blog_post_footer_comments', 'confluence_cloud_get_blog_post_inline_comments', 'confluence_cloud_get_footer_comments', 'confluence_cloud_create_footer_comment', 'confluence_cloud_get_footer_comment_by_id', 'confluence_cloud_update_footer_comment', 'confluence_cloud_delete_footer_comment', 'confluence_cloud_get_footer_comment_children', 'confluence_cloud_get_footer_like_count', 'confluence_cloud_get_footer_comment_operations', 'confluence_cloud_get_footer_comment_versions', 'confluence_cloud_get_footer_comment_version_details', 'confluence_cloud_get_inline_comments', 'confluence_cloud_create_inline_comment', 'confluence_cloud_get_inline_comment_by_id', 'confluence_cloud_update_inline_comment', 'confluence_cloud_delete_inline_comment', 'confluence_cloud_get_inline_comment_children', 'confluence_cloud_get_inline_like_count', 'confluence_cloud_get_inline_comment_operations', 'confluence_cloud_get_inline_comment_versions', 'confluence_cloud_get_inline_comment_version_details', 'confluence_cloud_get_comment_content_properties', 'confluence_cloud_create_comment_property', 'confluence_cloud_get_comment_content_properties_by_id', 'confluence_cloud_update_comment_property_by_id', 'confluence_cloud_delete_comment_property_by_id', 'confluence_cloud_get_tasks', 'confluence_cloud_get_task_by_id', 'confluence_cloud_update_task', 'confluence_cloud_get_child_custom_content', 'confluence_cloud_check_access_by_email', 'confluence_cloud_invite_by_email', 'confluence_cloud_get_data_policy_metadata', 'confluence_cloud_get_classification_levels', 'confluence_cloud_get_blog_post_classification_level', 'confluence_cloud_put_blog_post_classification_level', 'confluence_cloud_post_blog_post_classification_level', 'confluence_cloud_get_whiteboard_classification_level', 'confluence_cloud_put_whiteboard_classification_level', 'confluence_cloud_post_whiteboard_classification_level', 'confluence_cloud_get_database_classification_level', 'confluence_cloud_put_database_classification_level', 'confluence_cloud_post_database_classification_level', 'confluence_cloud_get_forge_app_properties', 'confluence_cloud_get_forge_app_property', 'confluence_cloud_put_forge_app_property', 'confluence_cloud_delete_forge_app_property'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud other operations.

        Actions:
          - 'confluence_cloud_get_admin_key': Call confluence_cloud_get_admin_key
          - 'confluence_cloud_enable_admin_key': Call confluence_cloud_enable_admin_key
          - 'confluence_cloud_disable_admin_key': Call confluence_cloud_disable_admin_key
          - 'confluence_cloud_get_blog_posts': Call confluence_cloud_get_blog_posts
          - 'confluence_cloud_create_blog_post': Call confluence_cloud_create_blog_post
          - 'confluence_cloud_get_blog_post_by_id': Call confluence_cloud_get_blog_post_by_id
          - 'confluence_cloud_update_blog_post': Call confluence_cloud_update_blog_post
          - 'confluence_cloud_delete_blog_post': Call confluence_cloud_delete_blog_post
          - 'confluence_cloud_get_custom_content_by_type_in_blog_post': Call confluence_cloud_get_custom_content_by_type_in_blog_post
          - 'confluence_cloud_get_blog_post_like_count': Call confluence_cloud_get_blog_post_like_count
          - 'confluence_cloud_get_blogpost_content_properties': Call confluence_cloud_get_blogpost_content_properties
          - 'confluence_cloud_create_blogpost_property': Call confluence_cloud_create_blogpost_property
          - 'confluence_cloud_get_blogpost_content_properties_by_id': Call confluence_cloud_get_blogpost_content_properties_by_id
          - 'confluence_cloud_update_blogpost_property_by_id': Call confluence_cloud_update_blogpost_property_by_id
          - 'confluence_cloud_delete_blogpost_property_by_id': Call confluence_cloud_delete_blogpost_property_by_id
          - 'confluence_cloud_get_blog_post_operations': Call confluence_cloud_get_blog_post_operations
          - 'confluence_cloud_get_blog_post_versions': Call confluence_cloud_get_blog_post_versions
          - 'confluence_cloud_get_blog_post_version_details': Call confluence_cloud_get_blog_post_version_details
          - 'confluence_cloud_convert_content_ids_to_content_types': Call confluence_cloud_convert_content_ids_to_content_types
          - 'confluence_cloud_get_custom_content_by_type': Call confluence_cloud_get_custom_content_by_type
          - 'confluence_cloud_create_custom_content': Call confluence_cloud_create_custom_content
          - 'confluence_cloud_get_custom_content_by_id': Call confluence_cloud_get_custom_content_by_id
          - 'confluence_cloud_update_custom_content': Call confluence_cloud_update_custom_content
          - 'confluence_cloud_delete_custom_content': Call confluence_cloud_delete_custom_content
          - 'confluence_cloud_get_custom_content_comments': Call confluence_cloud_get_custom_content_comments
          - 'confluence_cloud_get_custom_content_operations': Call confluence_cloud_get_custom_content_operations
          - 'confluence_cloud_get_custom_content_content_properties': Call confluence_cloud_get_custom_content_content_properties
          - 'confluence_cloud_get_custom_content_content_properties_by_id': Call confluence_cloud_get_custom_content_content_properties_by_id
          - 'confluence_cloud_post_redact_blog': Call confluence_cloud_post_redact_blog
          - 'confluence_cloud_create_whiteboard': Call confluence_cloud_create_whiteboard
          - 'confluence_cloud_get_whiteboard_by_id': Call confluence_cloud_get_whiteboard_by_id
          - 'confluence_cloud_delete_whiteboard': Call confluence_cloud_delete_whiteboard
          - 'confluence_cloud_get_whiteboard_content_properties': Call confluence_cloud_get_whiteboard_content_properties
          - 'confluence_cloud_create_whiteboard_property': Call confluence_cloud_create_whiteboard_property
          - 'confluence_cloud_get_whiteboard_content_properties_by_id': Call confluence_cloud_get_whiteboard_content_properties_by_id
          - 'confluence_cloud_update_whiteboard_property_by_id': Call confluence_cloud_update_whiteboard_property_by_id
          - 'confluence_cloud_delete_whiteboard_property_by_id': Call confluence_cloud_delete_whiteboard_property_by_id
          - 'confluence_cloud_get_whiteboard_operations': Call confluence_cloud_get_whiteboard_operations
          - 'confluence_cloud_get_whiteboard_direct_children': Call confluence_cloud_get_whiteboard_direct_children
          - 'confluence_cloud_get_whiteboard_descendants': Call confluence_cloud_get_whiteboard_descendants
          - 'confluence_cloud_get_whiteboard_ancestors': Call confluence_cloud_get_whiteboard_ancestors
          - 'confluence_cloud_create_database': Call confluence_cloud_create_database
          - 'confluence_cloud_get_database_by_id': Call confluence_cloud_get_database_by_id
          - 'confluence_cloud_delete_database': Call confluence_cloud_delete_database
          - 'confluence_cloud_get_database_content_properties': Call confluence_cloud_get_database_content_properties
          - 'confluence_cloud_create_database_property': Call confluence_cloud_create_database_property
          - 'confluence_cloud_get_database_content_properties_by_id': Call confluence_cloud_get_database_content_properties_by_id
          - 'confluence_cloud_update_database_property_by_id': Call confluence_cloud_update_database_property_by_id
          - 'confluence_cloud_delete_database_property_by_id': Call confluence_cloud_delete_database_property_by_id
          - 'confluence_cloud_get_database_operations': Call confluence_cloud_get_database_operations
          - 'confluence_cloud_get_database_direct_children': Call confluence_cloud_get_database_direct_children
          - 'confluence_cloud_get_database_descendants': Call confluence_cloud_get_database_descendants
          - 'confluence_cloud_get_database_ancestors': Call confluence_cloud_get_database_ancestors
          - 'confluence_cloud_create_smart_link': Call confluence_cloud_create_smart_link
          - 'confluence_cloud_get_smart_link_by_id': Call confluence_cloud_get_smart_link_by_id
          - 'confluence_cloud_delete_smart_link': Call confluence_cloud_delete_smart_link
          - 'confluence_cloud_get_smart_link_content_properties': Call confluence_cloud_get_smart_link_content_properties
          - 'confluence_cloud_create_smart_link_property': Call confluence_cloud_create_smart_link_property
          - 'confluence_cloud_get_smart_link_content_properties_by_id': Call confluence_cloud_get_smart_link_content_properties_by_id
          - 'confluence_cloud_update_smart_link_property_by_id': Call confluence_cloud_update_smart_link_property_by_id
          - 'confluence_cloud_delete_smart_link_property_by_id': Call confluence_cloud_delete_smart_link_property_by_id
          - 'confluence_cloud_get_smart_link_operations': Call confluence_cloud_get_smart_link_operations
          - 'confluence_cloud_get_smart_link_direct_children': Call confluence_cloud_get_smart_link_direct_children
          - 'confluence_cloud_get_smart_link_descendants': Call confluence_cloud_get_smart_link_descendants
          - 'confluence_cloud_get_smart_link_ancestors': Call confluence_cloud_get_smart_link_ancestors
          - 'confluence_cloud_create_folder': Call confluence_cloud_create_folder
          - 'confluence_cloud_get_folder_by_id': Call confluence_cloud_get_folder_by_id
          - 'confluence_cloud_delete_folder': Call confluence_cloud_delete_folder
          - 'confluence_cloud_get_folder_content_properties': Call confluence_cloud_get_folder_content_properties
          - 'confluence_cloud_create_folder_property': Call confluence_cloud_create_folder_property
          - 'confluence_cloud_get_folder_content_properties_by_id': Call confluence_cloud_get_folder_content_properties_by_id
          - 'confluence_cloud_update_folder_property_by_id': Call confluence_cloud_update_folder_property_by_id
          - 'confluence_cloud_delete_folder_property_by_id': Call confluence_cloud_delete_folder_property_by_id
          - 'confluence_cloud_get_folder_operations': Call confluence_cloud_get_folder_operations
          - 'confluence_cloud_get_folder_direct_children': Call confluence_cloud_get_folder_direct_children
          - 'confluence_cloud_get_folder_descendants': Call confluence_cloud_get_folder_descendants
          - 'confluence_cloud_get_folder_ancestors': Call confluence_cloud_get_folder_ancestors
          - 'confluence_cloud_get_custom_content_versions': Call confluence_cloud_get_custom_content_versions
          - 'confluence_cloud_get_custom_content_version_details': Call confluence_cloud_get_custom_content_version_details
          - 'confluence_cloud_get_blog_post_footer_comments': Call confluence_cloud_get_blog_post_footer_comments
          - 'confluence_cloud_get_blog_post_inline_comments': Call confluence_cloud_get_blog_post_inline_comments
          - 'confluence_cloud_get_footer_comments': Call confluence_cloud_get_footer_comments
          - 'confluence_cloud_create_footer_comment': Call confluence_cloud_create_footer_comment
          - 'confluence_cloud_get_footer_comment_by_id': Call confluence_cloud_get_footer_comment_by_id
          - 'confluence_cloud_update_footer_comment': Call confluence_cloud_update_footer_comment
          - 'confluence_cloud_delete_footer_comment': Call confluence_cloud_delete_footer_comment
          - 'confluence_cloud_get_footer_comment_children': Call confluence_cloud_get_footer_comment_children
          - 'confluence_cloud_get_footer_like_count': Call confluence_cloud_get_footer_like_count
          - 'confluence_cloud_get_footer_comment_operations': Call confluence_cloud_get_footer_comment_operations
          - 'confluence_cloud_get_footer_comment_versions': Call confluence_cloud_get_footer_comment_versions
          - 'confluence_cloud_get_footer_comment_version_details': Call confluence_cloud_get_footer_comment_version_details
          - 'confluence_cloud_get_inline_comments': Call confluence_cloud_get_inline_comments
          - 'confluence_cloud_create_inline_comment': Call confluence_cloud_create_inline_comment
          - 'confluence_cloud_get_inline_comment_by_id': Call confluence_cloud_get_inline_comment_by_id
          - 'confluence_cloud_update_inline_comment': Call confluence_cloud_update_inline_comment
          - 'confluence_cloud_delete_inline_comment': Call confluence_cloud_delete_inline_comment
          - 'confluence_cloud_get_inline_comment_children': Call confluence_cloud_get_inline_comment_children
          - 'confluence_cloud_get_inline_like_count': Call confluence_cloud_get_inline_like_count
          - 'confluence_cloud_get_inline_comment_operations': Call confluence_cloud_get_inline_comment_operations
          - 'confluence_cloud_get_inline_comment_versions': Call confluence_cloud_get_inline_comment_versions
          - 'confluence_cloud_get_inline_comment_version_details': Call confluence_cloud_get_inline_comment_version_details
          - 'confluence_cloud_get_comment_content_properties': Call confluence_cloud_get_comment_content_properties
          - 'confluence_cloud_create_comment_property': Call confluence_cloud_create_comment_property
          - 'confluence_cloud_get_comment_content_properties_by_id': Call confluence_cloud_get_comment_content_properties_by_id
          - 'confluence_cloud_update_comment_property_by_id': Call confluence_cloud_update_comment_property_by_id
          - 'confluence_cloud_delete_comment_property_by_id': Call confluence_cloud_delete_comment_property_by_id
          - 'confluence_cloud_get_tasks': Call confluence_cloud_get_tasks
          - 'confluence_cloud_get_task_by_id': Call confluence_cloud_get_task_by_id
          - 'confluence_cloud_update_task': Call confluence_cloud_update_task
          - 'confluence_cloud_get_child_custom_content': Call confluence_cloud_get_child_custom_content
          - 'confluence_cloud_check_access_by_email': Call confluence_cloud_check_access_by_email
          - 'confluence_cloud_invite_by_email': Call confluence_cloud_invite_by_email
          - 'confluence_cloud_get_data_policy_metadata': Call confluence_cloud_get_data_policy_metadata
          - 'confluence_cloud_get_classification_levels': Call confluence_cloud_get_classification_levels
          - 'confluence_cloud_get_blog_post_classification_level': Call confluence_cloud_get_blog_post_classification_level
          - 'confluence_cloud_put_blog_post_classification_level': Call confluence_cloud_put_blog_post_classification_level
          - 'confluence_cloud_post_blog_post_classification_level': Call confluence_cloud_post_blog_post_classification_level
          - 'confluence_cloud_get_whiteboard_classification_level': Call confluence_cloud_get_whiteboard_classification_level
          - 'confluence_cloud_put_whiteboard_classification_level': Call confluence_cloud_put_whiteboard_classification_level
          - 'confluence_cloud_post_whiteboard_classification_level': Call confluence_cloud_post_whiteboard_classification_level
          - 'confluence_cloud_get_database_classification_level': Call confluence_cloud_get_database_classification_level
          - 'confluence_cloud_put_database_classification_level': Call confluence_cloud_put_database_classification_level
          - 'confluence_cloud_post_database_classification_level': Call confluence_cloud_post_database_classification_level
          - 'confluence_cloud_get_forge_app_properties': Call confluence_cloud_get_forge_app_properties
          - 'confluence_cloud_get_forge_app_property': Call confluence_cloud_get_forge_app_property
          - 'confluence_cloud_put_forge_app_property': Call confluence_cloud_put_forge_app_property
          - 'confluence_cloud_delete_forge_app_property': Call confluence_cloud_delete_forge_app_property
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_get_admin_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_admin_key(**kwargs)
        if action == "confluence_cloud_enable_admin_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_enable_admin_key(**kwargs)
        if action == "confluence_cloud_disable_admin_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_disable_admin_key(**kwargs)
        if action == "confluence_cloud_get_blog_posts":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_posts(**kwargs)
        if action == "confluence_cloud_create_blog_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_blog_post(**kwargs)
        if action == "confluence_cloud_get_blog_post_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_by_id(**kwargs)
        if action == "confluence_cloud_update_blog_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_blog_post(**kwargs)
        if action == "confluence_cloud_delete_blog_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_blog_post(**kwargs)
        if action == "confluence_cloud_get_custom_content_by_type_in_blog_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_by_type_in_blog_post(
                **kwargs
            )
        if action == "confluence_cloud_get_blog_post_like_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_like_count(**kwargs)
        if action == "confluence_cloud_get_blogpost_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blogpost_content_properties(**kwargs)
        if action == "confluence_cloud_create_blogpost_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_blogpost_property(**kwargs)
        if action == "confluence_cloud_get_blogpost_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blogpost_content_properties_by_id(
                **kwargs
            )
        if action == "confluence_cloud_update_blogpost_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_blogpost_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_blogpost_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_blogpost_property_by_id(**kwargs)
        if action == "confluence_cloud_get_blog_post_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_operations(**kwargs)
        if action == "confluence_cloud_get_blog_post_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_versions(**kwargs)
        if action == "confluence_cloud_get_blog_post_version_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_version_details(**kwargs)
        if action == "confluence_cloud_convert_content_ids_to_content_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_convert_content_ids_to_content_types(
                **kwargs
            )
        if action == "confluence_cloud_get_custom_content_by_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_by_type(**kwargs)
        if action == "confluence_cloud_create_custom_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_custom_content(**kwargs)
        if action == "confluence_cloud_get_custom_content_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_by_id(**kwargs)
        if action == "confluence_cloud_update_custom_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_custom_content(**kwargs)
        if action == "confluence_cloud_delete_custom_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_custom_content(**kwargs)
        if action == "confluence_cloud_get_custom_content_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_comments(**kwargs)
        if action == "confluence_cloud_get_custom_content_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_operations(**kwargs)
        if action == "confluence_cloud_get_custom_content_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_content_properties(
                **kwargs
            )
        if action == "confluence_cloud_get_custom_content_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_content_properties_by_id(
                **kwargs
            )
        if action == "confluence_cloud_post_redact_blog":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_post_redact_blog(**kwargs)
        if action == "confluence_cloud_create_whiteboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_whiteboard(**kwargs)
        if action == "confluence_cloud_get_whiteboard_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_whiteboard_by_id(**kwargs)
        if action == "confluence_cloud_delete_whiteboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_whiteboard(**kwargs)
        if action == "confluence_cloud_get_whiteboard_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_whiteboard_content_properties(**kwargs)
        if action == "confluence_cloud_create_whiteboard_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_whiteboard_property(**kwargs)
        if action == "confluence_cloud_get_whiteboard_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_whiteboard_content_properties_by_id(
                **kwargs
            )
        if action == "confluence_cloud_update_whiteboard_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_whiteboard_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_whiteboard_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_whiteboard_property_by_id(**kwargs)
        if action == "confluence_cloud_get_whiteboard_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_whiteboard_operations(**kwargs)
        if action == "confluence_cloud_get_whiteboard_direct_children":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_whiteboard_direct_children(**kwargs)
        if action == "confluence_cloud_get_whiteboard_descendants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_whiteboard_descendants(**kwargs)
        if action == "confluence_cloud_get_whiteboard_ancestors":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_whiteboard_ancestors(**kwargs)
        if action == "confluence_cloud_create_database":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_database(**kwargs)
        if action == "confluence_cloud_get_database_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_database_by_id(**kwargs)
        if action == "confluence_cloud_delete_database":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_database(**kwargs)
        if action == "confluence_cloud_get_database_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_database_content_properties(**kwargs)
        if action == "confluence_cloud_create_database_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_database_property(**kwargs)
        if action == "confluence_cloud_get_database_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_database_content_properties_by_id(
                **kwargs
            )
        if action == "confluence_cloud_update_database_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_database_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_database_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_database_property_by_id(**kwargs)
        if action == "confluence_cloud_get_database_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_database_operations(**kwargs)
        if action == "confluence_cloud_get_database_direct_children":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_database_direct_children(**kwargs)
        if action == "confluence_cloud_get_database_descendants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_database_descendants(**kwargs)
        if action == "confluence_cloud_get_database_ancestors":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_database_ancestors(**kwargs)
        if action == "confluence_cloud_create_smart_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_smart_link(**kwargs)
        if action == "confluence_cloud_get_smart_link_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_smart_link_by_id(**kwargs)
        if action == "confluence_cloud_delete_smart_link":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_smart_link(**kwargs)
        if action == "confluence_cloud_get_smart_link_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_smart_link_content_properties(**kwargs)
        if action == "confluence_cloud_create_smart_link_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_smart_link_property(**kwargs)
        if action == "confluence_cloud_get_smart_link_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_smart_link_content_properties_by_id(
                **kwargs
            )
        if action == "confluence_cloud_update_smart_link_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_smart_link_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_smart_link_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_smart_link_property_by_id(**kwargs)
        if action == "confluence_cloud_get_smart_link_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_smart_link_operations(**kwargs)
        if action == "confluence_cloud_get_smart_link_direct_children":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_smart_link_direct_children(**kwargs)
        if action == "confluence_cloud_get_smart_link_descendants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_smart_link_descendants(**kwargs)
        if action == "confluence_cloud_get_smart_link_ancestors":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_smart_link_ancestors(**kwargs)
        if action == "confluence_cloud_create_folder":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_folder(**kwargs)
        if action == "confluence_cloud_get_folder_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_folder_by_id(**kwargs)
        if action == "confluence_cloud_delete_folder":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_folder(**kwargs)
        if action == "confluence_cloud_get_folder_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_folder_content_properties(**kwargs)
        if action == "confluence_cloud_create_folder_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_folder_property(**kwargs)
        if action == "confluence_cloud_get_folder_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_folder_content_properties_by_id(**kwargs)
        if action == "confluence_cloud_update_folder_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_folder_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_folder_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_folder_property_by_id(**kwargs)
        if action == "confluence_cloud_get_folder_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_folder_operations(**kwargs)
        if action == "confluence_cloud_get_folder_direct_children":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_folder_direct_children(**kwargs)
        if action == "confluence_cloud_get_folder_descendants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_folder_descendants(**kwargs)
        if action == "confluence_cloud_get_folder_ancestors":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_folder_ancestors(**kwargs)
        if action == "confluence_cloud_get_custom_content_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_versions(**kwargs)
        if action == "confluence_cloud_get_custom_content_version_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_version_details(**kwargs)
        if action == "confluence_cloud_get_blog_post_footer_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_footer_comments(**kwargs)
        if action == "confluence_cloud_get_blog_post_inline_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_inline_comments(**kwargs)
        if action == "confluence_cloud_get_footer_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_footer_comments(**kwargs)
        if action == "confluence_cloud_create_footer_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_footer_comment(**kwargs)
        if action == "confluence_cloud_get_footer_comment_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_footer_comment_by_id(**kwargs)
        if action == "confluence_cloud_update_footer_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_footer_comment(**kwargs)
        if action == "confluence_cloud_delete_footer_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_footer_comment(**kwargs)
        if action == "confluence_cloud_get_footer_comment_children":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_footer_comment_children(**kwargs)
        if action == "confluence_cloud_get_footer_like_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_footer_like_count(**kwargs)
        if action == "confluence_cloud_get_footer_comment_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_footer_comment_operations(**kwargs)
        if action == "confluence_cloud_get_footer_comment_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_footer_comment_versions(**kwargs)
        if action == "confluence_cloud_get_footer_comment_version_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_footer_comment_version_details(**kwargs)
        if action == "confluence_cloud_get_inline_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_inline_comments(**kwargs)
        if action == "confluence_cloud_create_inline_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_inline_comment(**kwargs)
        if action == "confluence_cloud_get_inline_comment_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_inline_comment_by_id(**kwargs)
        if action == "confluence_cloud_update_inline_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_inline_comment(**kwargs)
        if action == "confluence_cloud_delete_inline_comment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_inline_comment(**kwargs)
        if action == "confluence_cloud_get_inline_comment_children":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_inline_comment_children(**kwargs)
        if action == "confluence_cloud_get_inline_like_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_inline_like_count(**kwargs)
        if action == "confluence_cloud_get_inline_comment_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_inline_comment_operations(**kwargs)
        if action == "confluence_cloud_get_inline_comment_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_inline_comment_versions(**kwargs)
        if action == "confluence_cloud_get_inline_comment_version_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_inline_comment_version_details(**kwargs)
        if action == "confluence_cloud_get_comment_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_comment_content_properties(**kwargs)
        if action == "confluence_cloud_create_comment_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_comment_property(**kwargs)
        if action == "confluence_cloud_get_comment_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_comment_content_properties_by_id(
                **kwargs
            )
        if action == "confluence_cloud_update_comment_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_comment_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_comment_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_comment_property_by_id(**kwargs)
        if action == "confluence_cloud_get_tasks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_tasks(**kwargs)
        if action == "confluence_cloud_get_task_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_task_by_id(**kwargs)
        if action == "confluence_cloud_update_task":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_task(**kwargs)
        if action == "confluence_cloud_get_child_custom_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_child_custom_content(**kwargs)
        if action == "confluence_cloud_check_access_by_email":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_check_access_by_email(**kwargs)
        if action == "confluence_cloud_invite_by_email":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_invite_by_email(**kwargs)
        if action == "confluence_cloud_get_data_policy_metadata":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_data_policy_metadata(**kwargs)
        if action == "confluence_cloud_get_classification_levels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_classification_levels(**kwargs)
        if action == "confluence_cloud_get_blog_post_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_classification_level(**kwargs)
        if action == "confluence_cloud_put_blog_post_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_put_blog_post_classification_level(**kwargs)
        if action == "confluence_cloud_post_blog_post_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_post_blog_post_classification_level(**kwargs)
        if action == "confluence_cloud_get_whiteboard_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_whiteboard_classification_level(**kwargs)
        if action == "confluence_cloud_put_whiteboard_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_put_whiteboard_classification_level(**kwargs)
        if action == "confluence_cloud_post_whiteboard_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_post_whiteboard_classification_level(
                **kwargs
            )
        if action == "confluence_cloud_get_database_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_database_classification_level(**kwargs)
        if action == "confluence_cloud_put_database_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_put_database_classification_level(**kwargs)
        if action == "confluence_cloud_post_database_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_post_database_classification_level(**kwargs)
        if action == "confluence_cloud_get_forge_app_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_forge_app_properties(**kwargs)
        if action == "confluence_cloud_get_forge_app_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_forge_app_property(**kwargs)
        if action == "confluence_cloud_put_forge_app_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_put_forge_app_property(**kwargs)
        if action == "confluence_cloud_delete_forge_app_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_forge_app_property(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_get_admin_key', 'confluence_cloud_enable_admin_key', 'confluence_cloud_disable_admin_key', 'confluence_cloud_get_blog_posts', 'confluence_cloud_create_blog_post', 'confluence_cloud_get_blog_post_by_id', 'confluence_cloud_update_blog_post', 'confluence_cloud_delete_blog_post', 'confluence_cloud_get_custom_content_by_type_in_blog_post', 'confluence_cloud_get_blog_post_like_count', 'confluence_cloud_get_blogpost_content_properties', 'confluence_cloud_create_blogpost_property', 'confluence_cloud_get_blogpost_content_properties_by_id', 'confluence_cloud_update_blogpost_property_by_id', 'confluence_cloud_delete_blogpost_property_by_id', 'confluence_cloud_get_blog_post_operations', 'confluence_cloud_get_blog_post_versions', 'confluence_cloud_get_blog_post_version_details', 'confluence_cloud_convert_content_ids_to_content_types', 'confluence_cloud_get_custom_content_by_type', 'confluence_cloud_create_custom_content', 'confluence_cloud_get_custom_content_by_id', 'confluence_cloud_update_custom_content', 'confluence_cloud_delete_custom_content', 'confluence_cloud_get_custom_content_comments', 'confluence_cloud_get_custom_content_operations', 'confluence_cloud_get_custom_content_content_properties', 'confluence_cloud_get_custom_content_content_properties_by_id', 'confluence_cloud_post_redact_blog', 'confluence_cloud_create_whiteboard', 'confluence_cloud_get_whiteboard_by_id', 'confluence_cloud_delete_whiteboard', 'confluence_cloud_get_whiteboard_content_properties', 'confluence_cloud_create_whiteboard_property', 'confluence_cloud_get_whiteboard_content_properties_by_id', 'confluence_cloud_update_whiteboard_property_by_id', 'confluence_cloud_delete_whiteboard_property_by_id', 'confluence_cloud_get_whiteboard_operations', 'confluence_cloud_get_whiteboard_direct_children', 'confluence_cloud_get_whiteboard_descendants', 'confluence_cloud_get_whiteboard_ancestors', 'confluence_cloud_create_database', 'confluence_cloud_get_database_by_id', 'confluence_cloud_delete_database', 'confluence_cloud_get_database_content_properties', 'confluence_cloud_create_database_property', 'confluence_cloud_get_database_content_properties_by_id', 'confluence_cloud_update_database_property_by_id', 'confluence_cloud_delete_database_property_by_id', 'confluence_cloud_get_database_operations', 'confluence_cloud_get_database_direct_children', 'confluence_cloud_get_database_descendants', 'confluence_cloud_get_database_ancestors', 'confluence_cloud_create_smart_link', 'confluence_cloud_get_smart_link_by_id', 'confluence_cloud_delete_smart_link', 'confluence_cloud_get_smart_link_content_properties', 'confluence_cloud_create_smart_link_property', 'confluence_cloud_get_smart_link_content_properties_by_id', 'confluence_cloud_update_smart_link_property_by_id', 'confluence_cloud_delete_smart_link_property_by_id', 'confluence_cloud_get_smart_link_operations', 'confluence_cloud_get_smart_link_direct_children', 'confluence_cloud_get_smart_link_descendants', 'confluence_cloud_get_smart_link_ancestors', 'confluence_cloud_create_folder', 'confluence_cloud_get_folder_by_id', 'confluence_cloud_delete_folder', 'confluence_cloud_get_folder_content_properties', 'confluence_cloud_create_folder_property', 'confluence_cloud_get_folder_content_properties_by_id', 'confluence_cloud_update_folder_property_by_id', 'confluence_cloud_delete_folder_property_by_id', 'confluence_cloud_get_folder_operations', 'confluence_cloud_get_folder_direct_children', 'confluence_cloud_get_folder_descendants', 'confluence_cloud_get_folder_ancestors', 'confluence_cloud_get_custom_content_versions', 'confluence_cloud_get_custom_content_version_details', 'confluence_cloud_get_blog_post_footer_comments', 'confluence_cloud_get_blog_post_inline_comments', 'confluence_cloud_get_footer_comments', 'confluence_cloud_create_footer_comment', 'confluence_cloud_get_footer_comment_by_id', 'confluence_cloud_update_footer_comment', 'confluence_cloud_delete_footer_comment', 'confluence_cloud_get_footer_comment_children', 'confluence_cloud_get_footer_like_count', 'confluence_cloud_get_footer_comment_operations', 'confluence_cloud_get_footer_comment_versions', 'confluence_cloud_get_footer_comment_version_details', 'confluence_cloud_get_inline_comments', 'confluence_cloud_create_inline_comment', 'confluence_cloud_get_inline_comment_by_id', 'confluence_cloud_update_inline_comment', 'confluence_cloud_delete_inline_comment', 'confluence_cloud_get_inline_comment_children', 'confluence_cloud_get_inline_like_count', 'confluence_cloud_get_inline_comment_operations', 'confluence_cloud_get_inline_comment_versions', 'confluence_cloud_get_inline_comment_version_details', 'confluence_cloud_get_comment_content_properties', 'confluence_cloud_create_comment_property', 'confluence_cloud_get_comment_content_properties_by_id', 'confluence_cloud_update_comment_property_by_id', 'confluence_cloud_delete_comment_property_by_id', 'confluence_cloud_get_tasks', 'confluence_cloud_get_task_by_id', 'confluence_cloud_update_task', 'confluence_cloud_get_child_custom_content', 'confluence_cloud_check_access_by_email', 'confluence_cloud_invite_by_email', 'confluence_cloud_get_data_policy_metadata', 'confluence_cloud_get_classification_levels', 'confluence_cloud_get_blog_post_classification_level', 'confluence_cloud_put_blog_post_classification_level', 'confluence_cloud_post_blog_post_classification_level', 'confluence_cloud_get_whiteboard_classification_level', 'confluence_cloud_put_whiteboard_classification_level', 'confluence_cloud_post_whiteboard_classification_level', 'confluence_cloud_get_database_classification_level', 'confluence_cloud_put_database_classification_level', 'confluence_cloud_post_database_classification_level', 'confluence_cloud_get_forge_app_properties', 'confluence_cloud_get_forge_app_property', 'confluence_cloud_put_forge_app_property', 'confluence_cloud_delete_forge_app_property"
        )


def register_confluence_cloud_attachment_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-attachment"})
    async def atlassian_confluence_cloud_attachment(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_get_attachments', 'confluence_cloud_get_attachment_by_id', 'confluence_cloud_delete_attachment', 'confluence_cloud_get_attachment_labels', 'confluence_cloud_get_attachment_operations', 'confluence_cloud_get_attachment_content_properties', 'confluence_cloud_create_attachment_property', 'confluence_cloud_get_attachment_content_properties_by_id', 'confluence_cloud_update_attachment_property_by_id', 'confluence_cloud_delete_attachment_property_by_id', 'confluence_cloud_get_attachment_versions', 'confluence_cloud_get_attachment_version_details', 'confluence_cloud_get_attachment_comments', 'confluence_cloud_get_blogpost_attachments', 'confluence_cloud_get_custom_content_attachments', 'confluence_cloud_get_label_attachments'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud attachment operations.

        Actions:
          - 'confluence_cloud_get_attachments': Call confluence_cloud_get_attachments
          - 'confluence_cloud_get_attachment_by_id': Call confluence_cloud_get_attachment_by_id
          - 'confluence_cloud_delete_attachment': Call confluence_cloud_delete_attachment
          - 'confluence_cloud_get_attachment_labels': Call confluence_cloud_get_attachment_labels
          - 'confluence_cloud_get_attachment_operations': Call confluence_cloud_get_attachment_operations
          - 'confluence_cloud_get_attachment_content_properties': Call confluence_cloud_get_attachment_content_properties
          - 'confluence_cloud_create_attachment_property': Call confluence_cloud_create_attachment_property
          - 'confluence_cloud_get_attachment_content_properties_by_id': Call confluence_cloud_get_attachment_content_properties_by_id
          - 'confluence_cloud_update_attachment_property_by_id': Call confluence_cloud_update_attachment_property_by_id
          - 'confluence_cloud_delete_attachment_property_by_id': Call confluence_cloud_delete_attachment_property_by_id
          - 'confluence_cloud_get_attachment_versions': Call confluence_cloud_get_attachment_versions
          - 'confluence_cloud_get_attachment_version_details': Call confluence_cloud_get_attachment_version_details
          - 'confluence_cloud_get_attachment_comments': Call confluence_cloud_get_attachment_comments
          - 'confluence_cloud_get_blogpost_attachments': Call confluence_cloud_get_blogpost_attachments
          - 'confluence_cloud_get_custom_content_attachments': Call confluence_cloud_get_custom_content_attachments
          - 'confluence_cloud_get_label_attachments': Call confluence_cloud_get_label_attachments
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_get_attachments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachments(**kwargs)
        if action == "confluence_cloud_get_attachment_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachment_by_id(**kwargs)
        if action == "confluence_cloud_delete_attachment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_attachment(**kwargs)
        if action == "confluence_cloud_get_attachment_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachment_labels(**kwargs)
        if action == "confluence_cloud_get_attachment_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachment_operations(**kwargs)
        if action == "confluence_cloud_get_attachment_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachment_content_properties(**kwargs)
        if action == "confluence_cloud_create_attachment_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_attachment_property(**kwargs)
        if action == "confluence_cloud_get_attachment_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachment_content_properties_by_id(
                **kwargs
            )
        if action == "confluence_cloud_update_attachment_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_attachment_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_attachment_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_attachment_property_by_id(**kwargs)
        if action == "confluence_cloud_get_attachment_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachment_versions(**kwargs)
        if action == "confluence_cloud_get_attachment_version_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachment_version_details(**kwargs)
        if action == "confluence_cloud_get_attachment_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_attachment_comments(**kwargs)
        if action == "confluence_cloud_get_blogpost_attachments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blogpost_attachments(**kwargs)
        if action == "confluence_cloud_get_custom_content_attachments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_attachments(**kwargs)
        if action == "confluence_cloud_get_label_attachments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_label_attachments(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_get_attachments', 'confluence_cloud_get_attachment_by_id', 'confluence_cloud_delete_attachment', 'confluence_cloud_get_attachment_labels', 'confluence_cloud_get_attachment_operations', 'confluence_cloud_get_attachment_content_properties', 'confluence_cloud_create_attachment_property', 'confluence_cloud_get_attachment_content_properties_by_id', 'confluence_cloud_update_attachment_property_by_id', 'confluence_cloud_delete_attachment_property_by_id', 'confluence_cloud_get_attachment_versions', 'confluence_cloud_get_attachment_version_details', 'confluence_cloud_get_attachment_comments', 'confluence_cloud_get_blogpost_attachments', 'confluence_cloud_get_custom_content_attachments', 'confluence_cloud_get_label_attachments"
        )


def register_confluence_cloud_label_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-label"})
    async def atlassian_confluence_cloud_label(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_get_blog_post_labels', 'confluence_cloud_get_custom_content_labels', 'confluence_cloud_get_labels', 'confluence_cloud_get_label_blog_posts'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud label operations.

        Actions:
          - 'confluence_cloud_get_blog_post_labels': Call confluence_cloud_get_blog_post_labels
          - 'confluence_cloud_get_custom_content_labels': Call confluence_cloud_get_custom_content_labels
          - 'confluence_cloud_get_labels': Call confluence_cloud_get_labels
          - 'confluence_cloud_get_label_blog_posts': Call confluence_cloud_get_label_blog_posts
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_get_blog_post_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_labels(**kwargs)
        if action == "confluence_cloud_get_custom_content_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_labels(**kwargs)
        if action == "confluence_cloud_get_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_labels(**kwargs)
        if action == "confluence_cloud_get_label_blog_posts":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_label_blog_posts(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_get_blog_post_labels', 'confluence_cloud_get_custom_content_labels', 'confluence_cloud_get_labels', 'confluence_cloud_get_label_blog_posts"
        )


def register_confluence_cloud_user_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-user"})
    async def atlassian_confluence_cloud_user(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_get_blog_post_like_users', 'confluence_cloud_get_footer_like_users', 'confluence_cloud_get_inline_like_users', 'confluence_cloud_create_bulk_user_lookup'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud user operations.

        Actions:
          - 'confluence_cloud_get_blog_post_like_users': Call confluence_cloud_get_blog_post_like_users
          - 'confluence_cloud_get_footer_like_users': Call confluence_cloud_get_footer_like_users
          - 'confluence_cloud_get_inline_like_users': Call confluence_cloud_get_inline_like_users
          - 'confluence_cloud_create_bulk_user_lookup': Call confluence_cloud_create_bulk_user_lookup
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_get_blog_post_like_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_post_like_users(**kwargs)
        if action == "confluence_cloud_get_footer_like_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_footer_like_users(**kwargs)
        if action == "confluence_cloud_get_inline_like_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_inline_like_users(**kwargs)
        if action == "confluence_cloud_create_bulk_user_lookup":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_bulk_user_lookup(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_get_blog_post_like_users', 'confluence_cloud_get_footer_like_users', 'confluence_cloud_get_inline_like_users', 'confluence_cloud_create_bulk_user_lookup"
        )


def register_confluence_cloud_content_property_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-content-property"})
    async def atlassian_confluence_cloud_content_property(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_create_custom_content_property', 'confluence_cloud_update_custom_content_property_by_id', 'confluence_cloud_delete_custom_content_property_by_id'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud content property operations.

        Actions:
          - 'confluence_cloud_create_custom_content_property': Call confluence_cloud_create_custom_content_property
          - 'confluence_cloud_update_custom_content_property_by_id': Call confluence_cloud_update_custom_content_property_by_id
          - 'confluence_cloud_delete_custom_content_property_by_id': Call confluence_cloud_delete_custom_content_property_by_id
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_create_custom_content_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_custom_content_property(**kwargs)
        if action == "confluence_cloud_update_custom_content_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_custom_content_property_by_id(
                **kwargs
            )
        if action == "confluence_cloud_delete_custom_content_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_custom_content_property_by_id(
                **kwargs
            )
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_create_custom_content_property', 'confluence_cloud_update_custom_content_property_by_id', 'confluence_cloud_delete_custom_content_property_by_id"
        )


def register_confluence_cloud_page_core_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-page-core"})
    async def atlassian_confluence_cloud_page_core(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_get_label_pages', 'confluence_cloud_get_pages', 'confluence_cloud_create_page', 'confluence_cloud_get_page_by_id', 'confluence_cloud_update_page', 'confluence_cloud_delete_page', 'confluence_cloud_get_page_attachments', 'confluence_cloud_get_custom_content_by_type_in_page', 'confluence_cloud_get_page_labels', 'confluence_cloud_get_page_like_count', 'confluence_cloud_get_page_like_users', 'confluence_cloud_get_page_operations', 'confluence_cloud_create_page_property', 'confluence_cloud_update_page_property_by_id', 'confluence_cloud_delete_page_property_by_id', 'confluence_cloud_post_redact_page', 'confluence_cloud_update_page_title', 'confluence_cloud_get_page_versions', 'confluence_cloud_get_page_version_details', 'confluence_cloud_get_page_footer_comments', 'confluence_cloud_get_page_inline_comments', 'confluence_cloud_get_child_pages', 'confluence_cloud_get_page_direct_children', 'confluence_cloud_get_page_ancestors', 'confluence_cloud_get_page_descendants', 'confluence_cloud_get_page_classification_level', 'confluence_cloud_put_page_classification_level', 'confluence_cloud_post_page_classification_level'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud page core operations.

        Actions:
          - 'confluence_cloud_get_label_pages': Call confluence_cloud_get_label_pages
          - 'confluence_cloud_get_pages': Call confluence_cloud_get_pages
          - 'confluence_cloud_create_page': Call confluence_cloud_create_page
          - 'confluence_cloud_get_page_by_id': Call confluence_cloud_get_page_by_id
          - 'confluence_cloud_update_page': Call confluence_cloud_update_page
          - 'confluence_cloud_delete_page': Call confluence_cloud_delete_page
          - 'confluence_cloud_get_page_attachments': Call confluence_cloud_get_page_attachments
          - 'confluence_cloud_get_custom_content_by_type_in_page': Call confluence_cloud_get_custom_content_by_type_in_page
          - 'confluence_cloud_get_page_labels': Call confluence_cloud_get_page_labels
          - 'confluence_cloud_get_page_like_count': Call confluence_cloud_get_page_like_count
          - 'confluence_cloud_get_page_like_users': Call confluence_cloud_get_page_like_users
          - 'confluence_cloud_get_page_operations': Call confluence_cloud_get_page_operations
          - 'confluence_cloud_create_page_property': Call confluence_cloud_create_page_property
          - 'confluence_cloud_update_page_property_by_id': Call confluence_cloud_update_page_property_by_id
          - 'confluence_cloud_delete_page_property_by_id': Call confluence_cloud_delete_page_property_by_id
          - 'confluence_cloud_post_redact_page': Call confluence_cloud_post_redact_page
          - 'confluence_cloud_update_page_title': Call confluence_cloud_update_page_title
          - 'confluence_cloud_get_page_versions': Call confluence_cloud_get_page_versions
          - 'confluence_cloud_get_page_version_details': Call confluence_cloud_get_page_version_details
          - 'confluence_cloud_get_page_footer_comments': Call confluence_cloud_get_page_footer_comments
          - 'confluence_cloud_get_page_inline_comments': Call confluence_cloud_get_page_inline_comments
          - 'confluence_cloud_get_child_pages': Call confluence_cloud_get_child_pages
          - 'confluence_cloud_get_page_direct_children': Call confluence_cloud_get_page_direct_children
          - 'confluence_cloud_get_page_ancestors': Call confluence_cloud_get_page_ancestors
          - 'confluence_cloud_get_page_descendants': Call confluence_cloud_get_page_descendants
          - 'confluence_cloud_get_page_classification_level': Call confluence_cloud_get_page_classification_level
          - 'confluence_cloud_put_page_classification_level': Call confluence_cloud_put_page_classification_level
          - 'confluence_cloud_post_page_classification_level': Call confluence_cloud_post_page_classification_level
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_get_label_pages":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_label_pages(**kwargs)
        if action == "confluence_cloud_get_pages":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_pages(**kwargs)
        if action == "confluence_cloud_create_page":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_page(**kwargs)
        if action == "confluence_cloud_get_page_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_by_id(**kwargs)
        if action == "confluence_cloud_update_page":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_page(**kwargs)
        if action == "confluence_cloud_delete_page":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_page(**kwargs)
        if action == "confluence_cloud_get_page_attachments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_attachments(**kwargs)
        if action == "confluence_cloud_get_custom_content_by_type_in_page":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_by_type_in_page(**kwargs)
        if action == "confluence_cloud_get_page_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_labels(**kwargs)
        if action == "confluence_cloud_get_page_like_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_like_count(**kwargs)
        if action == "confluence_cloud_get_page_like_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_like_users(**kwargs)
        if action == "confluence_cloud_get_page_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_operations(**kwargs)
        if action == "confluence_cloud_create_page_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_page_property(**kwargs)
        if action == "confluence_cloud_update_page_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_page_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_page_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_page_property_by_id(**kwargs)
        if action == "confluence_cloud_post_redact_page":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_post_redact_page(**kwargs)
        if action == "confluence_cloud_update_page_title":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_page_title(**kwargs)
        if action == "confluence_cloud_get_page_versions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_versions(**kwargs)
        if action == "confluence_cloud_get_page_version_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_version_details(**kwargs)
        if action == "confluence_cloud_get_page_footer_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_footer_comments(**kwargs)
        if action == "confluence_cloud_get_page_inline_comments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_inline_comments(**kwargs)
        if action == "confluence_cloud_get_child_pages":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_child_pages(**kwargs)
        if action == "confluence_cloud_get_page_direct_children":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_direct_children(**kwargs)
        if action == "confluence_cloud_get_page_ancestors":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_ancestors(**kwargs)
        if action == "confluence_cloud_get_page_descendants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_descendants(**kwargs)
        if action == "confluence_cloud_get_page_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_classification_level(**kwargs)
        if action == "confluence_cloud_put_page_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_put_page_classification_level(**kwargs)
        if action == "confluence_cloud_post_page_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_post_page_classification_level(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_get_label_pages', 'confluence_cloud_get_pages', 'confluence_cloud_create_page', 'confluence_cloud_get_page_by_id', 'confluence_cloud_update_page', 'confluence_cloud_delete_page', 'confluence_cloud_get_page_attachments', 'confluence_cloud_get_custom_content_by_type_in_page', 'confluence_cloud_get_page_labels', 'confluence_cloud_get_page_like_count', 'confluence_cloud_get_page_like_users', 'confluence_cloud_get_page_operations', 'confluence_cloud_create_page_property', 'confluence_cloud_update_page_property_by_id', 'confluence_cloud_delete_page_property_by_id', 'confluence_cloud_post_redact_page', 'confluence_cloud_update_page_title', 'confluence_cloud_get_page_versions', 'confluence_cloud_get_page_version_details', 'confluence_cloud_get_page_footer_comments', 'confluence_cloud_get_page_inline_comments', 'confluence_cloud_get_child_pages', 'confluence_cloud_get_page_direct_children', 'confluence_cloud_get_page_ancestors', 'confluence_cloud_get_page_descendants', 'confluence_cloud_get_page_classification_level', 'confluence_cloud_put_page_classification_level', 'confluence_cloud_post_page_classification_level"
        )


def register_confluence_cloud_page_content_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-page-content"})
    async def atlassian_confluence_cloud_page_content(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_get_page_content_properties', 'confluence_cloud_get_page_content_properties_by_id'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud page content operations.

        Actions:
          - 'confluence_cloud_get_page_content_properties': Call confluence_cloud_get_page_content_properties
          - 'confluence_cloud_get_page_content_properties_by_id': Call confluence_cloud_get_page_content_properties_by_id
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_get_page_content_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_content_properties(**kwargs)
        if action == "confluence_cloud_get_page_content_properties_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_page_content_properties_by_id(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_get_page_content_properties', 'confluence_cloud_get_page_content_properties_by_id"
        )


def register_confluence_cloud_space_core_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-space-core"})
    async def atlassian_confluence_cloud_space_core(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_get_spaces', 'confluence_cloud_create_space', 'confluence_cloud_get_space_by_id', 'confluence_cloud_get_blog_posts_in_space', 'confluence_cloud_get_space_labels', 'confluence_cloud_get_space_content_labels', 'confluence_cloud_get_custom_content_by_type_in_space', 'confluence_cloud_get_space_operations', 'confluence_cloud_get_pages_in_space', 'confluence_cloud_get_space_properties', 'confluence_cloud_get_available_space_roles', 'confluence_cloud_create_space_role', 'confluence_cloud_get_space_roles_by_id', 'confluence_cloud_update_space_role', 'confluence_cloud_delete_space_role', 'confluence_cloud_get_space_role_mode', 'confluence_cloud_get_space_role_assignments', 'confluence_cloud_set_space_role_assignments', 'confluence_cloud_get_data_policy_spaces', 'confluence_cloud_get_space_default_classification_level', 'confluence_cloud_put_space_default_classification_level', 'confluence_cloud_delete_space_default_classification_level'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud space core operations.

        Actions:
          - 'confluence_cloud_get_spaces': Call confluence_cloud_get_spaces
          - 'confluence_cloud_create_space': Call confluence_cloud_create_space
          - 'confluence_cloud_get_space_by_id': Call confluence_cloud_get_space_by_id
          - 'confluence_cloud_get_blog_posts_in_space': Call confluence_cloud_get_blog_posts_in_space
          - 'confluence_cloud_get_space_labels': Call confluence_cloud_get_space_labels
          - 'confluence_cloud_get_space_content_labels': Call confluence_cloud_get_space_content_labels
          - 'confluence_cloud_get_custom_content_by_type_in_space': Call confluence_cloud_get_custom_content_by_type_in_space
          - 'confluence_cloud_get_space_operations': Call confluence_cloud_get_space_operations
          - 'confluence_cloud_get_pages_in_space': Call confluence_cloud_get_pages_in_space
          - 'confluence_cloud_get_space_properties': Call confluence_cloud_get_space_properties
          - 'confluence_cloud_get_available_space_roles': Call confluence_cloud_get_available_space_roles
          - 'confluence_cloud_create_space_role': Call confluence_cloud_create_space_role
          - 'confluence_cloud_get_space_roles_by_id': Call confluence_cloud_get_space_roles_by_id
          - 'confluence_cloud_update_space_role': Call confluence_cloud_update_space_role
          - 'confluence_cloud_delete_space_role': Call confluence_cloud_delete_space_role
          - 'confluence_cloud_get_space_role_mode': Call confluence_cloud_get_space_role_mode
          - 'confluence_cloud_get_space_role_assignments': Call confluence_cloud_get_space_role_assignments
          - 'confluence_cloud_set_space_role_assignments': Call confluence_cloud_set_space_role_assignments
          - 'confluence_cloud_get_data_policy_spaces': Call confluence_cloud_get_data_policy_spaces
          - 'confluence_cloud_get_space_default_classification_level': Call confluence_cloud_get_space_default_classification_level
          - 'confluence_cloud_put_space_default_classification_level': Call confluence_cloud_put_space_default_classification_level
          - 'confluence_cloud_delete_space_default_classification_level': Call confluence_cloud_delete_space_default_classification_level
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_get_spaces":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_spaces(**kwargs)
        if action == "confluence_cloud_create_space":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_space(**kwargs)
        if action == "confluence_cloud_get_space_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_by_id(**kwargs)
        if action == "confluence_cloud_get_blog_posts_in_space":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_blog_posts_in_space(**kwargs)
        if action == "confluence_cloud_get_space_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_labels(**kwargs)
        if action == "confluence_cloud_get_space_content_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_content_labels(**kwargs)
        if action == "confluence_cloud_get_custom_content_by_type_in_space":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_custom_content_by_type_in_space(**kwargs)
        if action == "confluence_cloud_get_space_operations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_operations(**kwargs)
        if action == "confluence_cloud_get_pages_in_space":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_pages_in_space(**kwargs)
        if action == "confluence_cloud_get_space_properties":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_properties(**kwargs)
        if action == "confluence_cloud_get_available_space_roles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_available_space_roles(**kwargs)
        if action == "confluence_cloud_create_space_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_space_role(**kwargs)
        if action == "confluence_cloud_get_space_roles_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_roles_by_id(**kwargs)
        if action == "confluence_cloud_update_space_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_space_role(**kwargs)
        if action == "confluence_cloud_delete_space_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_space_role(**kwargs)
        if action == "confluence_cloud_get_space_role_mode":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_role_mode(**kwargs)
        if action == "confluence_cloud_get_space_role_assignments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_role_assignments(**kwargs)
        if action == "confluence_cloud_set_space_role_assignments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_set_space_role_assignments(**kwargs)
        if action == "confluence_cloud_get_data_policy_spaces":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_data_policy_spaces(**kwargs)
        if action == "confluence_cloud_get_space_default_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_default_classification_level(
                **kwargs
            )
        if action == "confluence_cloud_put_space_default_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_put_space_default_classification_level(
                **kwargs
            )
        if action == "confluence_cloud_delete_space_default_classification_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_space_default_classification_level(
                **kwargs
            )
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_get_spaces', 'confluence_cloud_create_space', 'confluence_cloud_get_space_by_id', 'confluence_cloud_get_blog_posts_in_space', 'confluence_cloud_get_space_labels', 'confluence_cloud_get_space_content_labels', 'confluence_cloud_get_custom_content_by_type_in_space', 'confluence_cloud_get_space_operations', 'confluence_cloud_get_pages_in_space', 'confluence_cloud_get_space_properties', 'confluence_cloud_get_available_space_roles', 'confluence_cloud_create_space_role', 'confluence_cloud_get_space_roles_by_id', 'confluence_cloud_update_space_role', 'confluence_cloud_delete_space_role', 'confluence_cloud_get_space_role_mode', 'confluence_cloud_get_space_role_assignments', 'confluence_cloud_set_space_role_assignments', 'confluence_cloud_get_data_policy_spaces', 'confluence_cloud_get_space_default_classification_level', 'confluence_cloud_put_space_default_classification_level', 'confluence_cloud_delete_space_default_classification_level"
        )


def register_confluence_cloud_space_property_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-space-property"})
    async def atlassian_confluence_cloud_space_property(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_create_space_property', 'confluence_cloud_get_space_property_by_id', 'confluence_cloud_update_space_property_by_id', 'confluence_cloud_delete_space_property_by_id'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud space property operations.

        Actions:
          - 'confluence_cloud_create_space_property': Call confluence_cloud_create_space_property
          - 'confluence_cloud_get_space_property_by_id': Call confluence_cloud_get_space_property_by_id
          - 'confluence_cloud_update_space_property_by_id': Call confluence_cloud_update_space_property_by_id
          - 'confluence_cloud_delete_space_property_by_id': Call confluence_cloud_delete_space_property_by_id
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_create_space_property":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_create_space_property(**kwargs)
        if action == "confluence_cloud_get_space_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_property_by_id(**kwargs)
        if action == "confluence_cloud_update_space_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_update_space_property_by_id(**kwargs)
        if action == "confluence_cloud_delete_space_property_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_delete_space_property_by_id(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_create_space_property', 'confluence_cloud_get_space_property_by_id', 'confluence_cloud_update_space_property_by_id', 'confluence_cloud_delete_space_property_by_id"
        )


def register_confluence_cloud_space_permission_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-cloud-space-permission"})
    async def atlassian_confluence_cloud_space_permission(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_cloud_get_space_permissions_assignments', 'confluence_cloud_get_available_space_permissions'"
        ),
        client=Depends(get_confluence_cloud_client),
    ) -> dict:
        """Manage confluence cloud space permission operations.

        Actions:
          - 'confluence_cloud_get_space_permissions_assignments': Call confluence_cloud_get_space_permissions_assignments
          - 'confluence_cloud_get_available_space_permissions': Call confluence_cloud_get_available_space_permissions
        """
        kwargs: dict[str, Any]
        if action == "confluence_cloud_get_space_permissions_assignments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_space_permissions_assignments(**kwargs)
        if action == "confluence_cloud_get_available_space_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_cloud_get_available_space_permissions(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_cloud_get_space_permissions_assignments', 'confluence_cloud_get_available_space_permissions"
        )


def register_confluence_server_other_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-server-other"})
    async def atlassian_confluence_server_other(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_server_get_access_mode_status', 'confluence_server_create', 'confluence_server_delete', 'confluence_server_change_password', 'confluence_server_delete_1', 'confluence_server_disable', 'confluence_server_enable', 'confluence_server_get_attachments', 'confluence_server_create_attachments', 'confluence_server_get_attachment_extracted_text', 'confluence_server_move', 'confluence_server_update', 'confluence_server_remove_attachment', 'confluence_server_remove_attachment_version', 'confluence_server_update_data', 'confluence_server_get_audit_records', 'confluence_server_cancel_all_queued_jobs', 'confluence_server_cancel_job', 'confluence_server_create_site_backup_job', 'confluence_server_create_site_restore_job', 'confluence_server_create_site_restore_job_for_uploaded_backup_file', 'confluence_server_download_backup_file', 'confluence_server_find_jobs', 'confluence_server_get_files', 'confluence_server_get_job', 'confluence_server_remove_category', 'confluence_server_publish_shared_draft', 'confluence_server_publish_legacy_draft', 'confluence_server_convert', 'confluence_server_labels', 'confluence_server_add_labels', 'confluence_server_delete_label_with_query_param', 'confluence_server_delete_label', 'confluence_server_find_all', 'confluence_server_create_1', 'confluence_server_find_by_key', 'confluence_server_update_1', 'confluence_server_create_2', 'confluence_server_delete_2', 'confluence_server_delete_3', 'confluence_server_get_history', 'confluence_server_get_macro_body_by_hash', 'confluence_server_get_macro_body_by_macro_id', 'confluence_server_search', 'confluence_server_update_2', 'confluence_server_by_operation', 'confluence_server_for_operation', 'confluence_server_relevant_view_restrictions', 'confluence_server_update_restrictions', 'confluence_server_index', 'confluence_server_descendants', 'confluence_server_descendants_of_type', 'confluence_server_get_default_color_scheme', 'confluence_server_get_global_color_scheme', 'confluence_server_update_color_scheme', 'confluence_server_reset_global_color_scheme', 'confluence_server_get_all_global_permissions', 'confluence_server_find_webhooks', 'confluence_server_create_webhook', 'confluence_server_get_webhook', 'confluence_server_update_webhook', 'confluence_server_delete_webhook', 'confluence_server_get_latest_invocation', 'confluence_server_get_statistics', 'confluence_server_get_statistics_summary', 'confluence_server_test_webhook', 'confluence_server_get_members', 'confluence_server_index_1', 'confluence_server_get_related_labels', 'confluence_server_recent', 'confluence_server_get_task', 'confluence_server_get_tasks', 'confluence_server_search_1', 'confluence_server_index_2', 'confluence_server_get_color_scheme_type', 'confluence_server_update_color_scheme_type', 'confluence_server_index_3', 'confluence_server_popular', 'confluence_server_recent_1', 'confluence_server_related', 'confluence_server_set_permissions', 'confluence_server_get_1', 'confluence_server_create_3', 'confluence_server_get', 'confluence_server_update_3', 'confluence_server_create_4', 'confluence_server_delete_4', 'confluence_server_archive', 'confluence_server_update_4', 'confluence_server_delete_5', 'confluence_server_restore', 'confluence_server_trash', 'confluence_server_index_4', 'confluence_server_update_5', 'confluence_server_delete_6', 'confluence_server_change_password_1', 'confluence_server_get_anonymous', 'confluence_server_get_current'"
        ),
        client=Depends(get_confluence_server_client),
    ) -> dict:
        """Manage confluence server other operations.

        Actions:
          - 'confluence_server_get_access_mode_status': Call confluence_server_get_access_mode_status
          - 'confluence_server_create': Call confluence_server_create
          - 'confluence_server_delete': Call confluence_server_delete
          - 'confluence_server_change_password': Call confluence_server_change_password
          - 'confluence_server_delete_1': Call confluence_server_delete_1
          - 'confluence_server_disable': Call confluence_server_disable
          - 'confluence_server_enable': Call confluence_server_enable
          - 'confluence_server_get_attachments': Call confluence_server_get_attachments
          - 'confluence_server_create_attachments': Call confluence_server_create_attachments
          - 'confluence_server_get_attachment_extracted_text': Call confluence_server_get_attachment_extracted_text
          - 'confluence_server_move': Call confluence_server_move
          - 'confluence_server_update': Call confluence_server_update
          - 'confluence_server_remove_attachment': Call confluence_server_remove_attachment
          - 'confluence_server_remove_attachment_version': Call confluence_server_remove_attachment_version
          - 'confluence_server_update_data': Call confluence_server_update_data
          - 'confluence_server_get_audit_records': Call confluence_server_get_audit_records
          - 'confluence_server_cancel_all_queued_jobs': Call confluence_server_cancel_all_queued_jobs
          - 'confluence_server_cancel_job': Call confluence_server_cancel_job
          - 'confluence_server_create_site_backup_job': Call confluence_server_create_site_backup_job
          - 'confluence_server_create_site_restore_job': Call confluence_server_create_site_restore_job
          - 'confluence_server_create_site_restore_job_for_uploaded_backup_file': Call confluence_server_create_site_restore_job_for_uploaded_backup_file
          - 'confluence_server_download_backup_file': Call confluence_server_download_backup_file
          - 'confluence_server_find_jobs': Call confluence_server_find_jobs
          - 'confluence_server_get_files': Call confluence_server_get_files
          - 'confluence_server_get_job': Call confluence_server_get_job
          - 'confluence_server_remove_category': Call confluence_server_remove_category
          - 'confluence_server_publish_shared_draft': Call confluence_server_publish_shared_draft
          - 'confluence_server_publish_legacy_draft': Call confluence_server_publish_legacy_draft
          - 'confluence_server_convert': Call confluence_server_convert
          - 'confluence_server_labels': Call confluence_server_labels
          - 'confluence_server_add_labels': Call confluence_server_add_labels
          - 'confluence_server_delete_label_with_query_param': Call confluence_server_delete_label_with_query_param
          - 'confluence_server_delete_label': Call confluence_server_delete_label
          - 'confluence_server_find_all': Call confluence_server_find_all
          - 'confluence_server_create_1': Call confluence_server_create_1
          - 'confluence_server_find_by_key': Call confluence_server_find_by_key
          - 'confluence_server_update_1': Call confluence_server_update_1
          - 'confluence_server_create_2': Call confluence_server_create_2
          - 'confluence_server_delete_2': Call confluence_server_delete_2
          - 'confluence_server_delete_3': Call confluence_server_delete_3
          - 'confluence_server_get_history': Call confluence_server_get_history
          - 'confluence_server_get_macro_body_by_hash': Call confluence_server_get_macro_body_by_hash
          - 'confluence_server_get_macro_body_by_macro_id': Call confluence_server_get_macro_body_by_macro_id
          - 'confluence_server_search': Call confluence_server_search
          - 'confluence_server_update_2': Call confluence_server_update_2
          - 'confluence_server_by_operation': Call confluence_server_by_operation
          - 'confluence_server_for_operation': Call confluence_server_for_operation
          - 'confluence_server_relevant_view_restrictions': Call confluence_server_relevant_view_restrictions
          - 'confluence_server_update_restrictions': Call confluence_server_update_restrictions
          - 'confluence_server_index': Call confluence_server_index
          - 'confluence_server_descendants': Call confluence_server_descendants
          - 'confluence_server_descendants_of_type': Call confluence_server_descendants_of_type
          - 'confluence_server_get_default_color_scheme': Call confluence_server_get_default_color_scheme
          - 'confluence_server_get_global_color_scheme': Call confluence_server_get_global_color_scheme
          - 'confluence_server_update_color_scheme': Call confluence_server_update_color_scheme
          - 'confluence_server_reset_global_color_scheme': Call confluence_server_reset_global_color_scheme
          - 'confluence_server_get_all_global_permissions': Call confluence_server_get_all_global_permissions
          - 'confluence_server_find_webhooks': Call confluence_server_find_webhooks
          - 'confluence_server_create_webhook': Call confluence_server_create_webhook
          - 'confluence_server_get_webhook': Call confluence_server_get_webhook
          - 'confluence_server_update_webhook': Call confluence_server_update_webhook
          - 'confluence_server_delete_webhook': Call confluence_server_delete_webhook
          - 'confluence_server_get_latest_invocation': Call confluence_server_get_latest_invocation
          - 'confluence_server_get_statistics': Call confluence_server_get_statistics
          - 'confluence_server_get_statistics_summary': Call confluence_server_get_statistics_summary
          - 'confluence_server_test_webhook': Call confluence_server_test_webhook
          - 'confluence_server_get_members': Call confluence_server_get_members
          - 'confluence_server_index_1': Call confluence_server_index_1
          - 'confluence_server_get_related_labels': Call confluence_server_get_related_labels
          - 'confluence_server_recent': Call confluence_server_recent
          - 'confluence_server_get_task': Call confluence_server_get_task
          - 'confluence_server_get_tasks': Call confluence_server_get_tasks
          - 'confluence_server_search_1': Call confluence_server_search_1
          - 'confluence_server_index_2': Call confluence_server_index_2
          - 'confluence_server_get_color_scheme_type': Call confluence_server_get_color_scheme_type
          - 'confluence_server_update_color_scheme_type': Call confluence_server_update_color_scheme_type
          - 'confluence_server_index_3': Call confluence_server_index_3
          - 'confluence_server_popular': Call confluence_server_popular
          - 'confluence_server_recent_1': Call confluence_server_recent_1
          - 'confluence_server_related': Call confluence_server_related
          - 'confluence_server_set_permissions': Call confluence_server_set_permissions
          - 'confluence_server_get_1': Call confluence_server_get_1
          - 'confluence_server_create_3': Call confluence_server_create_3
          - 'confluence_server_get': Call confluence_server_get
          - 'confluence_server_update_3': Call confluence_server_update_3
          - 'confluence_server_create_4': Call confluence_server_create_4
          - 'confluence_server_delete_4': Call confluence_server_delete_4
          - 'confluence_server_archive': Call confluence_server_archive
          - 'confluence_server_update_4': Call confluence_server_update_4
          - 'confluence_server_delete_5': Call confluence_server_delete_5
          - 'confluence_server_restore': Call confluence_server_restore
          - 'confluence_server_trash': Call confluence_server_trash
          - 'confluence_server_index_4': Call confluence_server_index_4
          - 'confluence_server_update_5': Call confluence_server_update_5
          - 'confluence_server_delete_6': Call confluence_server_delete_6
          - 'confluence_server_change_password_1': Call confluence_server_change_password_1
          - 'confluence_server_get_anonymous': Call confluence_server_get_anonymous
          - 'confluence_server_get_current': Call confluence_server_get_current
        """
        kwargs: dict[str, Any]
        if action == "confluence_server_get_access_mode_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_access_mode_status(**kwargs)
        if action == "confluence_server_create":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create(**kwargs)
        if action == "confluence_server_delete":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete(**kwargs)
        if action == "confluence_server_change_password":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_change_password(**kwargs)
        if action == "confluence_server_delete_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_1(**kwargs)
        if action == "confluence_server_disable":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_disable(**kwargs)
        if action == "confluence_server_enable":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_enable(**kwargs)
        if action == "confluence_server_get_attachments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_attachments(**kwargs)
        if action == "confluence_server_create_attachments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_attachments(**kwargs)
        if action == "confluence_server_get_attachment_extracted_text":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_attachment_extracted_text(**kwargs)
        if action == "confluence_server_move":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_move(**kwargs)
        if action == "confluence_server_update":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update(**kwargs)
        if action == "confluence_server_remove_attachment":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_remove_attachment(**kwargs)
        if action == "confluence_server_remove_attachment_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_remove_attachment_version(**kwargs)
        if action == "confluence_server_update_data":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_data(**kwargs)
        if action == "confluence_server_get_audit_records":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_audit_records(**kwargs)
        if action == "confluence_server_cancel_all_queued_jobs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_cancel_all_queued_jobs(**kwargs)
        if action == "confluence_server_cancel_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_cancel_job(**kwargs)
        if action == "confluence_server_create_site_backup_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_site_backup_job(**kwargs)
        if action == "confluence_server_create_site_restore_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_site_restore_job(**kwargs)
        if (
            action
            == "confluence_server_create_site_restore_job_for_uploaded_backup_file"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_site_restore_job_for_uploaded_backup_file(
                **kwargs
            )
        if action == "confluence_server_download_backup_file":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_download_backup_file(**kwargs)
        if action == "confluence_server_find_jobs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_find_jobs(**kwargs)
        if action == "confluence_server_get_files":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_files(**kwargs)
        if action == "confluence_server_get_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_job(**kwargs)
        if action == "confluence_server_remove_category":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_remove_category(**kwargs)
        if action == "confluence_server_publish_shared_draft":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_publish_shared_draft(**kwargs)
        if action == "confluence_server_publish_legacy_draft":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_publish_legacy_draft(**kwargs)
        if action == "confluence_server_convert":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_convert(**kwargs)
        if action == "confluence_server_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_labels(**kwargs)
        if action == "confluence_server_add_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_add_labels(**kwargs)
        if action == "confluence_server_delete_label_with_query_param":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_label_with_query_param(**kwargs)
        if action == "confluence_server_delete_label":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_label(**kwargs)
        if action == "confluence_server_find_all":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_find_all(**kwargs)
        if action == "confluence_server_create_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_1(**kwargs)
        if action == "confluence_server_find_by_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_find_by_key(**kwargs)
        if action == "confluence_server_update_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_1(**kwargs)
        if action == "confluence_server_create_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_2(**kwargs)
        if action == "confluence_server_delete_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_2(**kwargs)
        if action == "confluence_server_delete_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_3(**kwargs)
        if action == "confluence_server_get_history":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_history(**kwargs)
        if action == "confluence_server_get_macro_body_by_hash":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_macro_body_by_hash(**kwargs)
        if action == "confluence_server_get_macro_body_by_macro_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_macro_body_by_macro_id(**kwargs)
        if action == "confluence_server_search":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_search(**kwargs)
        if action == "confluence_server_update_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_2(**kwargs)
        if action == "confluence_server_by_operation":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_by_operation(**kwargs)
        if action == "confluence_server_for_operation":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_for_operation(**kwargs)
        if action == "confluence_server_relevant_view_restrictions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_relevant_view_restrictions(**kwargs)
        if action == "confluence_server_update_restrictions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_restrictions(**kwargs)
        if action == "confluence_server_index":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_index(**kwargs)
        if action == "confluence_server_descendants":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_descendants(**kwargs)
        if action == "confluence_server_descendants_of_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_descendants_of_type(**kwargs)
        if action == "confluence_server_get_default_color_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_default_color_scheme(**kwargs)
        if action == "confluence_server_get_global_color_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_global_color_scheme(**kwargs)
        if action == "confluence_server_update_color_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_color_scheme(**kwargs)
        if action == "confluence_server_reset_global_color_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_reset_global_color_scheme(**kwargs)
        if action == "confluence_server_get_all_global_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_all_global_permissions(**kwargs)
        if action == "confluence_server_find_webhooks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_find_webhooks(**kwargs)
        if action == "confluence_server_create_webhook":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_webhook(**kwargs)
        if action == "confluence_server_get_webhook":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_webhook(**kwargs)
        if action == "confluence_server_update_webhook":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_webhook(**kwargs)
        if action == "confluence_server_delete_webhook":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_webhook(**kwargs)
        if action == "confluence_server_get_latest_invocation":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_latest_invocation(**kwargs)
        if action == "confluence_server_get_statistics":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_statistics(**kwargs)
        if action == "confluence_server_get_statistics_summary":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_statistics_summary(**kwargs)
        if action == "confluence_server_test_webhook":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_test_webhook(**kwargs)
        if action == "confluence_server_get_members":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_members(**kwargs)
        if action == "confluence_server_index_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_index_1(**kwargs)
        if action == "confluence_server_get_related_labels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_related_labels(**kwargs)
        if action == "confluence_server_recent":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_recent(**kwargs)
        if action == "confluence_server_get_task":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_task(**kwargs)
        if action == "confluence_server_get_tasks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_tasks(**kwargs)
        if action == "confluence_server_search_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_search_1(**kwargs)
        if action == "confluence_server_index_2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_index_2(**kwargs)
        if action == "confluence_server_get_color_scheme_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_color_scheme_type(**kwargs)
        if action == "confluence_server_update_color_scheme_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_color_scheme_type(**kwargs)
        if action == "confluence_server_index_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_index_3(**kwargs)
        if action == "confluence_server_popular":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_popular(**kwargs)
        if action == "confluence_server_recent_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_recent_1(**kwargs)
        if action == "confluence_server_related":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_related(**kwargs)
        if action == "confluence_server_set_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_set_permissions(**kwargs)
        if action == "confluence_server_get_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_1(**kwargs)
        if action == "confluence_server_create_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_3(**kwargs)
        if action == "confluence_server_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get(**kwargs)
        if action == "confluence_server_update_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_3(**kwargs)
        if action == "confluence_server_create_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_4(**kwargs)
        if action == "confluence_server_delete_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_4(**kwargs)
        if action == "confluence_server_archive":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_archive(**kwargs)
        if action == "confluence_server_update_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_4(**kwargs)
        if action == "confluence_server_delete_5":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_5(**kwargs)
        if action == "confluence_server_restore":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_restore(**kwargs)
        if action == "confluence_server_trash":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_trash(**kwargs)
        if action == "confluence_server_index_4":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_index_4(**kwargs)
        if action == "confluence_server_update_5":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_5(**kwargs)
        if action == "confluence_server_delete_6":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_6(**kwargs)
        if action == "confluence_server_change_password_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_change_password_1(**kwargs)
        if action == "confluence_server_get_anonymous":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_anonymous(**kwargs)
        if action == "confluence_server_get_current":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_current(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_server_get_access_mode_status', 'confluence_server_create', 'confluence_server_delete', 'confluence_server_change_password', 'confluence_server_delete_1', 'confluence_server_disable', 'confluence_server_enable', 'confluence_server_get_attachments', 'confluence_server_create_attachments', 'confluence_server_get_attachment_extracted_text', 'confluence_server_move', 'confluence_server_update', 'confluence_server_remove_attachment', 'confluence_server_remove_attachment_version', 'confluence_server_update_data', 'confluence_server_get_audit_records', 'confluence_server_cancel_all_queued_jobs', 'confluence_server_cancel_job', 'confluence_server_create_site_backup_job', 'confluence_server_create_site_restore_job', 'confluence_server_create_site_restore_job_for_uploaded_backup_file', 'confluence_server_download_backup_file', 'confluence_server_find_jobs', 'confluence_server_get_files', 'confluence_server_get_job', 'confluence_server_remove_category', 'confluence_server_publish_shared_draft', 'confluence_server_publish_legacy_draft', 'confluence_server_convert', 'confluence_server_labels', 'confluence_server_add_labels', 'confluence_server_delete_label_with_query_param', 'confluence_server_delete_label', 'confluence_server_find_all', 'confluence_server_create_1', 'confluence_server_find_by_key', 'confluence_server_update_1', 'confluence_server_create_2', 'confluence_server_delete_2', 'confluence_server_delete_3', 'confluence_server_get_history', 'confluence_server_get_macro_body_by_hash', 'confluence_server_get_macro_body_by_macro_id', 'confluence_server_search', 'confluence_server_update_2', 'confluence_server_by_operation', 'confluence_server_for_operation', 'confluence_server_relevant_view_restrictions', 'confluence_server_update_restrictions', 'confluence_server_index', 'confluence_server_descendants', 'confluence_server_descendants_of_type', 'confluence_server_get_default_color_scheme', 'confluence_server_get_global_color_scheme', 'confluence_server_update_color_scheme', 'confluence_server_reset_global_color_scheme', 'confluence_server_get_all_global_permissions', 'confluence_server_find_webhooks', 'confluence_server_create_webhook', 'confluence_server_get_webhook', 'confluence_server_update_webhook', 'confluence_server_delete_webhook', 'confluence_server_get_latest_invocation', 'confluence_server_get_statistics', 'confluence_server_get_statistics_summary', 'confluence_server_test_webhook', 'confluence_server_get_members', 'confluence_server_index_1', 'confluence_server_get_related_labels', 'confluence_server_recent', 'confluence_server_get_task', 'confluence_server_get_tasks', 'confluence_server_search_1', 'confluence_server_index_2', 'confluence_server_get_color_scheme_type', 'confluence_server_update_color_scheme_type', 'confluence_server_index_3', 'confluence_server_popular', 'confluence_server_recent_1', 'confluence_server_related', 'confluence_server_set_permissions', 'confluence_server_get_1', 'confluence_server_create_3', 'confluence_server_get', 'confluence_server_update_3', 'confluence_server_create_4', 'confluence_server_delete_4', 'confluence_server_archive', 'confluence_server_update_4', 'confluence_server_delete_5', 'confluence_server_restore', 'confluence_server_trash', 'confluence_server_index_4', 'confluence_server_update_5', 'confluence_server_delete_6', 'confluence_server_change_password_1', 'confluence_server_get_anonymous', 'confluence_server_get_current"
        )


def register_confluence_server_user_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-server-user"})
    async def atlassian_confluence_server_user(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_server_create_user', 'confluence_server_get_permissions_granted_to_anonymous_users', 'confluence_server_get_permissions_granted_to_unlicensed_users', 'confluence_server_get_permissions_granted_to_user', 'confluence_server_get_permissions_granted_to_anonymous_users_1', 'confluence_server_get_permissions_granted_to_user_1', 'confluence_server_grant_permissions_to_anonymous_users', 'confluence_server_grant_permissions_to_user', 'confluence_server_revoke_permissions_from_anonymous_user', 'confluence_server_revoke_permissions_from_user', 'confluence_server_get_user', 'confluence_server_get_users'"
        ),
        client=Depends(get_confluence_server_client),
    ) -> dict:
        """Manage confluence server user operations.

        Actions:
          - 'confluence_server_create_user': Call confluence_server_create_user
          - 'confluence_server_get_permissions_granted_to_anonymous_users': Call confluence_server_get_permissions_granted_to_anonymous_users
          - 'confluence_server_get_permissions_granted_to_unlicensed_users': Call confluence_server_get_permissions_granted_to_unlicensed_users
          - 'confluence_server_get_permissions_granted_to_user': Call confluence_server_get_permissions_granted_to_user
          - 'confluence_server_get_permissions_granted_to_anonymous_users_1': Call confluence_server_get_permissions_granted_to_anonymous_users_1
          - 'confluence_server_get_permissions_granted_to_user_1': Call confluence_server_get_permissions_granted_to_user_1
          - 'confluence_server_grant_permissions_to_anonymous_users': Call confluence_server_grant_permissions_to_anonymous_users
          - 'confluence_server_grant_permissions_to_user': Call confluence_server_grant_permissions_to_user
          - 'confluence_server_revoke_permissions_from_anonymous_user': Call confluence_server_revoke_permissions_from_anonymous_user
          - 'confluence_server_revoke_permissions_from_user': Call confluence_server_revoke_permissions_from_user
          - 'confluence_server_get_user': Call confluence_server_get_user
          - 'confluence_server_get_users': Call confluence_server_get_users
        """
        kwargs: dict[str, Any]
        if action == "confluence_server_create_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_user(**kwargs)
        if action == "confluence_server_get_permissions_granted_to_anonymous_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_permissions_granted_to_anonymous_users(
                **kwargs
            )
        if action == "confluence_server_get_permissions_granted_to_unlicensed_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_permissions_granted_to_unlicensed_users(
                **kwargs
            )
        if action == "confluence_server_get_permissions_granted_to_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_permissions_granted_to_user(**kwargs)
        if action == "confluence_server_get_permissions_granted_to_anonymous_users_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return (
                client.confluence_server_get_permissions_granted_to_anonymous_users_1(
                    **kwargs
                )
            )
        if action == "confluence_server_get_permissions_granted_to_user_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_permissions_granted_to_user_1(**kwargs)
        if action == "confluence_server_grant_permissions_to_anonymous_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_grant_permissions_to_anonymous_users(
                **kwargs
            )
        if action == "confluence_server_grant_permissions_to_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_grant_permissions_to_user(**kwargs)
        if action == "confluence_server_revoke_permissions_from_anonymous_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_revoke_permissions_from_anonymous_user(
                **kwargs
            )
        if action == "confluence_server_revoke_permissions_from_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_revoke_permissions_from_user(**kwargs)
        if action == "confluence_server_get_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_user(**kwargs)
        if action == "confluence_server_get_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_users(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_server_create_user', 'confluence_server_get_permissions_granted_to_anonymous_users', 'confluence_server_get_permissions_granted_to_unlicensed_users', 'confluence_server_get_permissions_granted_to_user', 'confluence_server_get_permissions_granted_to_anonymous_users_1', 'confluence_server_get_permissions_granted_to_user_1', 'confluence_server_grant_permissions_to_anonymous_users', 'confluence_server_grant_permissions_to_user', 'confluence_server_revoke_permissions_from_anonymous_user', 'confluence_server_revoke_permissions_from_user', 'confluence_server_get_user', 'confluence_server_get_users"
        )


def register_confluence_server_space_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-server-space"})
    async def atlassian_confluence_server_space(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_server_create_space_backup_job', 'confluence_server_create_space_restore_job', 'confluence_server_create_space_restore_job_for_uploaded_backup_file', 'confluence_server_get_space_color_scheme', 'confluence_server_update_space_color_scheme', 'confluence_server_reset_space_color_scheme', 'confluence_server_create_private_space', 'confluence_server_spaces', 'confluence_server_create_space', 'confluence_server_space', 'confluence_server_is_watching_space', 'confluence_server_add_space_watch', 'confluence_server_remove_space_watch'"
        ),
        client=Depends(get_confluence_server_client),
    ) -> dict:
        """Manage confluence server space operations.

        Actions:
          - 'confluence_server_create_space_backup_job': Call confluence_server_create_space_backup_job
          - 'confluence_server_create_space_restore_job': Call confluence_server_create_space_restore_job
          - 'confluence_server_create_space_restore_job_for_uploaded_backup_file': Call confluence_server_create_space_restore_job_for_uploaded_backup_file
          - 'confluence_server_get_space_color_scheme': Call confluence_server_get_space_color_scheme
          - 'confluence_server_update_space_color_scheme': Call confluence_server_update_space_color_scheme
          - 'confluence_server_reset_space_color_scheme': Call confluence_server_reset_space_color_scheme
          - 'confluence_server_create_private_space': Call confluence_server_create_private_space
          - 'confluence_server_spaces': Call confluence_server_spaces
          - 'confluence_server_create_space': Call confluence_server_create_space
          - 'confluence_server_space': Call confluence_server_space
          - 'confluence_server_is_watching_space': Call confluence_server_is_watching_space
          - 'confluence_server_add_space_watch': Call confluence_server_add_space_watch
          - 'confluence_server_remove_space_watch': Call confluence_server_remove_space_watch
        """
        kwargs: dict[str, Any]
        if action == "confluence_server_create_space_backup_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_space_backup_job(**kwargs)
        if action == "confluence_server_create_space_restore_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_space_restore_job(**kwargs)
        if (
            action
            == "confluence_server_create_space_restore_job_for_uploaded_backup_file"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_space_restore_job_for_uploaded_backup_file(
                **kwargs
            )
        if action == "confluence_server_get_space_color_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_space_color_scheme(**kwargs)
        if action == "confluence_server_update_space_color_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_update_space_color_scheme(**kwargs)
        if action == "confluence_server_reset_space_color_scheme":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_reset_space_color_scheme(**kwargs)
        if action == "confluence_server_create_private_space":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_private_space(**kwargs)
        if action == "confluence_server_spaces":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_spaces(**kwargs)
        if action == "confluence_server_create_space":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_space(**kwargs)
        if action == "confluence_server_space":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_space(**kwargs)
        if action == "confluence_server_is_watching_space":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_is_watching_space(**kwargs)
        if action == "confluence_server_add_space_watch":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_add_space_watch(**kwargs)
        if action == "confluence_server_remove_space_watch":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_remove_space_watch(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_server_create_space_backup_job', 'confluence_server_create_space_restore_job', 'confluence_server_create_space_restore_job_for_uploaded_backup_file', 'confluence_server_get_space_color_scheme', 'confluence_server_update_space_color_scheme', 'confluence_server_reset_space_color_scheme', 'confluence_server_create_private_space', 'confluence_server_spaces', 'confluence_server_create_space', 'confluence_server_space', 'confluence_server_is_watching_space', 'confluence_server_add_space_watch', 'confluence_server_remove_space_watch"
        )


def register_confluence_server_content_child_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-server-content-child"})
    async def atlassian_confluence_server_content_child(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_server_children', 'confluence_server_children_of_type'"
        ),
        client=Depends(get_confluence_server_client),
    ) -> dict:
        """Manage confluence server content child operations.

        Actions:
          - 'confluence_server_children': Call confluence_server_children
          - 'confluence_server_children_of_type': Call confluence_server_children_of_type
        """
        kwargs: dict[str, Any]
        if action == "confluence_server_children":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_children(**kwargs)
        if action == "confluence_server_children_of_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_children_of_type(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_server_children', 'confluence_server_children_of_type"
        )


def register_confluence_server_content_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-server-content"})
    async def atlassian_confluence_server_content(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_server_comments_of_content', 'confluence_server_get_content', 'confluence_server_create_content', 'confluence_server_get_content_by_id', 'confluence_server_scan_content', 'confluence_server_contents', 'confluence_server_contents_with_type', 'confluence_server_is_watching_content', 'confluence_server_add_content_watcher', 'confluence_server_remove_content_watcher'"
        ),
        client=Depends(get_confluence_server_client),
    ) -> dict:
        """Manage confluence server content operations.

        Actions:
          - 'confluence_server_comments_of_content': Call confluence_server_comments_of_content
          - 'confluence_server_get_content': Call confluence_server_get_content
          - 'confluence_server_create_content': Call confluence_server_create_content
          - 'confluence_server_get_content_by_id': Call confluence_server_get_content_by_id
          - 'confluence_server_scan_content': Call confluence_server_scan_content
          - 'confluence_server_contents': Call confluence_server_contents
          - 'confluence_server_contents_with_type': Call confluence_server_contents_with_type
          - 'confluence_server_is_watching_content': Call confluence_server_is_watching_content
          - 'confluence_server_add_content_watcher': Call confluence_server_add_content_watcher
          - 'confluence_server_remove_content_watcher': Call confluence_server_remove_content_watcher
        """
        kwargs: dict[str, Any]
        if action == "confluence_server_comments_of_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_comments_of_content(**kwargs)
        if action == "confluence_server_get_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_content(**kwargs)
        if action == "confluence_server_create_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_create_content(**kwargs)
        if action == "confluence_server_get_content_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_content_by_id(**kwargs)
        if action == "confluence_server_scan_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_scan_content(**kwargs)
        if action == "confluence_server_contents":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_contents(**kwargs)
        if action == "confluence_server_contents_with_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_contents_with_type(**kwargs)
        if action == "confluence_server_is_watching_content":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_is_watching_content(**kwargs)
        if action == "confluence_server_add_content_watcher":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_add_content_watcher(**kwargs)
        if action == "confluence_server_remove_content_watcher":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_remove_content_watcher(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_server_comments_of_content', 'confluence_server_get_content', 'confluence_server_create_content', 'confluence_server_get_content_by_id', 'confluence_server_scan_content', 'confluence_server_contents', 'confluence_server_contents_with_type', 'confluence_server_is_watching_content', 'confluence_server_add_content_watcher', 'confluence_server_remove_content_watcher"
        )


def register_confluence_server_content_history_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-server-content-history"})
    async def atlassian_confluence_server_content_history(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_server_delete_content_history'"
        ),
        client=Depends(get_confluence_server_client),
    ) -> dict:
        """Manage confluence server content history operations.

        Actions:
          - 'confluence_server_delete_content_history': Call confluence_server_delete_content_history
        """
        kwargs: dict[str, Any]
        if action == "confluence_server_delete_content_history":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_delete_content_history(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_server_delete_content_history"
        )


def register_confluence_server_group_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-server-group"})
    async def atlassian_confluence_server_group(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_server_get_permissions_granted_to_group', 'confluence_server_get_ancestor_groups', 'confluence_server_get_ancestor_groups_by_group_name', 'confluence_server_get_group', 'confluence_server_get_group_by_group_name', 'confluence_server_get_groups', 'confluence_server_get_members_by_group_name', 'confluence_server_get_nested_group_members', 'confluence_server_get_nested_group_members_by_group_name', 'confluence_server_get_parent_groups', 'confluence_server_get_parent_groups_by_group_name', 'confluence_server_get_permissions_granted_to_group_1', 'confluence_server_grant_permissions_to_group', 'confluence_server_revoke_permissions_from_group', 'confluence_server_get_groups_1'"
        ),
        client=Depends(get_confluence_server_client),
    ) -> dict:
        """Manage confluence server group operations.

        Actions:
          - 'confluence_server_get_permissions_granted_to_group': Call confluence_server_get_permissions_granted_to_group
          - 'confluence_server_get_ancestor_groups': Call confluence_server_get_ancestor_groups
          - 'confluence_server_get_ancestor_groups_by_group_name': Call confluence_server_get_ancestor_groups_by_group_name
          - 'confluence_server_get_group': Call confluence_server_get_group
          - 'confluence_server_get_group_by_group_name': Call confluence_server_get_group_by_group_name
          - 'confluence_server_get_groups': Call confluence_server_get_groups
          - 'confluence_server_get_members_by_group_name': Call confluence_server_get_members_by_group_name
          - 'confluence_server_get_nested_group_members': Call confluence_server_get_nested_group_members
          - 'confluence_server_get_nested_group_members_by_group_name': Call confluence_server_get_nested_group_members_by_group_name
          - 'confluence_server_get_parent_groups': Call confluence_server_get_parent_groups
          - 'confluence_server_get_parent_groups_by_group_name': Call confluence_server_get_parent_groups_by_group_name
          - 'confluence_server_get_permissions_granted_to_group_1': Call confluence_server_get_permissions_granted_to_group_1
          - 'confluence_server_grant_permissions_to_group': Call confluence_server_grant_permissions_to_group
          - 'confluence_server_revoke_permissions_from_group': Call confluence_server_revoke_permissions_from_group
          - 'confluence_server_get_groups_1': Call confluence_server_get_groups_1
        """
        kwargs: dict[str, Any]
        if action == "confluence_server_get_permissions_granted_to_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_permissions_granted_to_group(**kwargs)
        if action == "confluence_server_get_ancestor_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_ancestor_groups(**kwargs)
        if action == "confluence_server_get_ancestor_groups_by_group_name":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_ancestor_groups_by_group_name(**kwargs)
        if action == "confluence_server_get_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_group(**kwargs)
        if action == "confluence_server_get_group_by_group_name":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_group_by_group_name(**kwargs)
        if action == "confluence_server_get_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_groups(**kwargs)
        if action == "confluence_server_get_members_by_group_name":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_members_by_group_name(**kwargs)
        if action == "confluence_server_get_nested_group_members":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_nested_group_members(**kwargs)
        if action == "confluence_server_get_nested_group_members_by_group_name":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_nested_group_members_by_group_name(
                **kwargs
            )
        if action == "confluence_server_get_parent_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_parent_groups(**kwargs)
        if action == "confluence_server_get_parent_groups_by_group_name":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_parent_groups_by_group_name(**kwargs)
        if action == "confluence_server_get_permissions_granted_to_group_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_permissions_granted_to_group_1(**kwargs)
        if action == "confluence_server_grant_permissions_to_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_grant_permissions_to_group(**kwargs)
        if action == "confluence_server_revoke_permissions_from_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_revoke_permissions_from_group(**kwargs)
        if action == "confluence_server_get_groups_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_groups_1(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_server_get_permissions_granted_to_group', 'confluence_server_get_ancestor_groups', 'confluence_server_get_ancestor_groups_by_group_name', 'confluence_server_get_group', 'confluence_server_get_group_by_group_name', 'confluence_server_get_groups', 'confluence_server_get_members_by_group_name', 'confluence_server_get_nested_group_members', 'confluence_server_get_nested_group_members_by_group_name', 'confluence_server_get_parent_groups', 'confluence_server_get_parent_groups_by_group_name', 'confluence_server_get_permissions_granted_to_group_1', 'confluence_server_grant_permissions_to_group', 'confluence_server_revoke_permissions_from_group', 'confluence_server_get_groups_1"
        )


def register_confluence_server_space_permission_tools(mcp: FastMCP):
    @mcp.tool(tags={"confluence-server-space-permission"})
    async def atlassian_confluence_server_space_permission(
        action: str = Field(
            description="Action to perform. Must be one of: 'confluence_server_get_all_space_permissions'"
        ),
        client=Depends(get_confluence_server_client),
    ) -> dict:
        """Manage confluence server space permission operations.

        Actions:
          - 'confluence_server_get_all_space_permissions': Call confluence_server_get_all_space_permissions
        """
        kwargs: dict[str, Any]
        if action == "confluence_server_get_all_space_permissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.confluence_server_get_all_space_permissions(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: confluence_server_get_all_space_permissions"
        )


def register_atlassian_dlp_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-dlp"})
    async def atlassian_atlassian_dlp(
        action: str = Field(
            description="Action to perform. Must be one of: 'dlp_cloud_create_level', 'dlp_cloud_get_level_list', 'dlp_cloud_get_level', 'dlp_cloud_edit_level', 'dlp_cloud_publish_level', 'dlp_cloud_archive_level', 'dlp_cloud_restore_level', 'dlp_cloud_reorder'"
        ),
        client=Depends(get_dlp_cloud_client),
    ) -> dict:
        """Manage atlassian dlp operations.

        Actions:
          - 'dlp_cloud_create_level': Call dlp_cloud_create_level
          - 'dlp_cloud_get_level_list': Call dlp_cloud_get_level_list
          - 'dlp_cloud_get_level': Call dlp_cloud_get_level
          - 'dlp_cloud_edit_level': Call dlp_cloud_edit_level
          - 'dlp_cloud_publish_level': Call dlp_cloud_publish_level
          - 'dlp_cloud_archive_level': Call dlp_cloud_archive_level
          - 'dlp_cloud_restore_level': Call dlp_cloud_restore_level
          - 'dlp_cloud_reorder': Call dlp_cloud_reorder
        """
        kwargs: dict[str, Any]
        if action == "dlp_cloud_create_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.dlp_cloud_create_level(**kwargs)
        if action == "dlp_cloud_get_level_list":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.dlp_cloud_get_level_list(**kwargs)
        if action == "dlp_cloud_get_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.dlp_cloud_get_level(**kwargs)
        if action == "dlp_cloud_edit_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.dlp_cloud_edit_level(**kwargs)
        if action == "dlp_cloud_publish_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.dlp_cloud_publish_level(**kwargs)
        if action == "dlp_cloud_archive_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.dlp_cloud_archive_level(**kwargs)
        if action == "dlp_cloud_restore_level":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.dlp_cloud_restore_level(**kwargs)
        if action == "dlp_cloud_reorder":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.dlp_cloud_reorder(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: dlp_cloud_create_level', 'dlp_cloud_get_level_list', 'dlp_cloud_get_level', 'dlp_cloud_edit_level', 'dlp_cloud_publish_level', 'dlp_cloud_archive_level', 'dlp_cloud_restore_level', 'dlp_cloud_reorder"
        )


def register_atlassian_user_mgmt_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-user-mgmt"})
    async def atlassian_atlassian_user_mgmt(
        action: str = Field(
            description="Action to perform. Must be one of: 'user_mgmt_cloud_get_users_account_id_manage', 'user_mgmt_cloud_get_users_account_id_manage_profile', 'user_mgmt_cloud_patch_users_account_id_manage_profile', 'user_mgmt_cloud_put_users_account_id_manage_email', 'user_mgmt_cloud_get_users_account_id_manage_api_tokens', 'user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id', 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete'"
        ),
        client=Depends(get_user_mgmt_cloud_client),
    ) -> dict:
        """Manage atlassian user mgmt operations.

        Actions:
          - 'user_mgmt_cloud_get_users_account_id_manage': Call user_mgmt_cloud_get_users_account_id_manage
          - 'user_mgmt_cloud_get_users_account_id_manage_profile': Call user_mgmt_cloud_get_users_account_id_manage_profile
          - 'user_mgmt_cloud_patch_users_account_id_manage_profile': Call user_mgmt_cloud_patch_users_account_id_manage_profile
          - 'user_mgmt_cloud_put_users_account_id_manage_email': Call user_mgmt_cloud_put_users_account_id_manage_email
          - 'user_mgmt_cloud_get_users_account_id_manage_api_tokens': Call user_mgmt_cloud_get_users_account_id_manage_api_tokens
          - 'user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id': Call user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id
          - 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete': Call user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete
        """
        kwargs: dict[str, Any]
        if action == "user_mgmt_cloud_get_users_account_id_manage":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_get_users_account_id_manage(**kwargs)
        if action == "user_mgmt_cloud_get_users_account_id_manage_profile":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_get_users_account_id_manage_profile(**kwargs)
        if action == "user_mgmt_cloud_patch_users_account_id_manage_profile":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_patch_users_account_id_manage_profile(
                **kwargs
            )
        if action == "user_mgmt_cloud_put_users_account_id_manage_email":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_put_users_account_id_manage_email(**kwargs)
        if action == "user_mgmt_cloud_get_users_account_id_manage_api_tokens":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_get_users_account_id_manage_api_tokens(
                **kwargs
            )
        if (
            action
            == "user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id(
                **kwargs
            )
        if (
            action
            == "user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete(
                **kwargs
            )
        raise ValueError(
            f"Unknown action: {action}. Must be one of: user_mgmt_cloud_get_users_account_id_manage', 'user_mgmt_cloud_get_users_account_id_manage_profile', 'user_mgmt_cloud_patch_users_account_id_manage_profile', 'user_mgmt_cloud_put_users_account_id_manage_email', 'user_mgmt_cloud_get_users_account_id_manage_api_tokens', 'user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id', 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete"
        )


def register_atlassian_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian"})
    async def atlassian_atlassian(
        action: str = Field(
            description="Action to perform. Must be one of: 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable', 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable', 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete'"
        ),
        client=Depends(get_user_mgmt_cloud_client),
    ) -> dict:
        """Manage atlassian operations.

        Actions:
          - 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable': Call user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable
          - 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable': Call user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable
          - 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete': Call user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete
        """
        kwargs: dict[str, Any]
        if action == "user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return (
                client.user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable(
                    **kwargs
                )
            )
        if action == "user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable(
                **kwargs
            )
        if action == "user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete(
                **kwargs
            )
        raise ValueError(
            f"Unknown action: {action}. Must be one of: user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable', 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable', 'user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete"
        )


def register_atlassian_admin_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-admin"})
    async def atlassian_atlassian_admin(
        action: str = Field(
            description="Action to perform. Must be one of: 'admin_cloud_get_orgs', 'admin_cloud_get_org_by_id', 'admin_cloud_get_directory_users', 'admin_cloud_get_directory_user_details', 'admin_cloud_get_users', 'admin_cloud_post_v2_orgs_org_id_users_invite', 'admin_cloud_get_user_role_assignments', 'admin_cloud_assign_role', 'admin_cloud_revoke_role', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore', 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id', 'admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign', 'admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke', 'admin_cloud_get_directory_users_count', 'admin_cloud_get_user_stats', 'admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates', 'admin_cloud_search_users', 'admin_cloud_post_v1_orgs_org_id_users_invite', 'admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access', 'admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access', 'admin_cloud_delete_v1_orgs_org_id_directory_users_account_id', 'admin_cloud_get_groups', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups', 'admin_cloud_get_group_role_assignments', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships', 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id', 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id', 'admin_cloud_get_group', 'admin_cloud_get_groups_count', 'admin_cloud_get_groups_stats', 'admin_cloud_search_groups', 'admin_cloud_post_v1_orgs_org_id_directory_groups', 'admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id', 'admin_cloud_assign_role_to_group', 'admin_cloud_revoke_role_to_group', 'admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships', 'admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id', 'admin_cloud_get_directories_for_org', 'admin_cloud_get_domains', 'admin_cloud_get_domain_by_id', 'admin_cloud_get_events', 'admin_cloud_poll_events', 'admin_cloud_get_event_by_id', 'admin_cloud_get_event_actions', 'admin_cloud_get_policies', 'admin_cloud_create_policy', 'admin_cloud_get_policy_by_id', 'admin_cloud_update_policy', 'admin_cloud_delete_policy', 'admin_cloud_add_resource_to_policy', 'admin_cloud_update_policy_resource', 'admin_cloud_delete_policy_resource', 'admin_cloud_validate_policy', 'admin_cloud_query_workspaces_v2'"
        ),
        client=Depends(get_admin_cloud_client),
    ) -> dict:
        """Manage atlassian admin operations.

        Actions:
          - 'admin_cloud_get_orgs': Call admin_cloud_get_orgs
          - 'admin_cloud_get_org_by_id': Call admin_cloud_get_org_by_id
          - 'admin_cloud_get_directory_users': Call admin_cloud_get_directory_users
          - 'admin_cloud_get_directory_user_details': Call admin_cloud_get_directory_user_details
          - 'admin_cloud_get_users': Call admin_cloud_get_users
          - 'admin_cloud_post_v2_orgs_org_id_users_invite': Call admin_cloud_post_v2_orgs_org_id_users_invite
          - 'admin_cloud_get_user_role_assignments': Call admin_cloud_get_user_role_assignments
          - 'admin_cloud_assign_role': Call admin_cloud_assign_role
          - 'admin_cloud_revoke_role': Call admin_cloud_revoke_role
          - 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend': Call admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend
          - 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore': Call admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore
          - 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id': Call admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id
          - 'admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign': Call admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign
          - 'admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke': Call admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke
          - 'admin_cloud_get_directory_users_count': Call admin_cloud_get_directory_users_count
          - 'admin_cloud_get_user_stats': Call admin_cloud_get_user_stats
          - 'admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates': Call admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates
          - 'admin_cloud_search_users': Call admin_cloud_search_users
          - 'admin_cloud_post_v1_orgs_org_id_users_invite': Call admin_cloud_post_v1_orgs_org_id_users_invite
          - 'admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access': Call admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access
          - 'admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access': Call admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access
          - 'admin_cloud_delete_v1_orgs_org_id_directory_users_account_id': Call admin_cloud_delete_v1_orgs_org_id_directory_users_account_id
          - 'admin_cloud_get_groups': Call admin_cloud_get_groups
          - 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups': Call admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups
          - 'admin_cloud_get_group_role_assignments': Call admin_cloud_get_group_role_assignments
          - 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign': Call admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign
          - 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke': Call admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke
          - 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships': Call admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships
          - 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id': Call admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id
          - 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id': Call admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id
          - 'admin_cloud_get_group': Call admin_cloud_get_group
          - 'admin_cloud_get_groups_count': Call admin_cloud_get_groups_count
          - 'admin_cloud_get_groups_stats': Call admin_cloud_get_groups_stats
          - 'admin_cloud_search_groups': Call admin_cloud_search_groups
          - 'admin_cloud_post_v1_orgs_org_id_directory_groups': Call admin_cloud_post_v1_orgs_org_id_directory_groups
          - 'admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id': Call admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id
          - 'admin_cloud_assign_role_to_group': Call admin_cloud_assign_role_to_group
          - 'admin_cloud_revoke_role_to_group': Call admin_cloud_revoke_role_to_group
          - 'admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships': Call admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships
          - 'admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id': Call admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id
          - 'admin_cloud_get_directories_for_org': Call admin_cloud_get_directories_for_org
          - 'admin_cloud_get_domains': Call admin_cloud_get_domains
          - 'admin_cloud_get_domain_by_id': Call admin_cloud_get_domain_by_id
          - 'admin_cloud_get_events': Call admin_cloud_get_events
          - 'admin_cloud_poll_events': Call admin_cloud_poll_events
          - 'admin_cloud_get_event_by_id': Call admin_cloud_get_event_by_id
          - 'admin_cloud_get_event_actions': Call admin_cloud_get_event_actions
          - 'admin_cloud_get_policies': Call admin_cloud_get_policies
          - 'admin_cloud_create_policy': Call admin_cloud_create_policy
          - 'admin_cloud_get_policy_by_id': Call admin_cloud_get_policy_by_id
          - 'admin_cloud_update_policy': Call admin_cloud_update_policy
          - 'admin_cloud_delete_policy': Call admin_cloud_delete_policy
          - 'admin_cloud_add_resource_to_policy': Call admin_cloud_add_resource_to_policy
          - 'admin_cloud_update_policy_resource': Call admin_cloud_update_policy_resource
          - 'admin_cloud_delete_policy_resource': Call admin_cloud_delete_policy_resource
          - 'admin_cloud_validate_policy': Call admin_cloud_validate_policy
          - 'admin_cloud_query_workspaces_v2': Call admin_cloud_query_workspaces_v2
        """
        kwargs: dict[str, Any]
        if action == "admin_cloud_get_orgs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_orgs(**kwargs)
        if action == "admin_cloud_get_org_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_org_by_id(**kwargs)
        if action == "admin_cloud_get_directory_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_directory_users(**kwargs)
        if action == "admin_cloud_get_directory_user_details":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_directory_user_details(**kwargs)
        if action == "admin_cloud_get_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_users(**kwargs)
        if action == "admin_cloud_post_v2_orgs_org_id_users_invite":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v2_orgs_org_id_users_invite(**kwargs)
        if action == "admin_cloud_get_user_role_assignments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_user_role_assignments(**kwargs)
        if action == "admin_cloud_assign_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_assign_role(**kwargs)
        if action == "admin_cloud_revoke_role":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_revoke_role(**kwargs)
        if (
            action
            == "admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend(
                **kwargs
            )
        if (
            action
            == "admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore(
                **kwargs
            )
        if (
            action
            == "admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id(
                **kwargs
            )
        if (
            action
            == "admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign(
                **kwargs
            )
        if (
            action
            == "admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke(
                **kwargs
            )
        if action == "admin_cloud_get_directory_users_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_directory_users_count(**kwargs)
        if action == "admin_cloud_get_user_stats":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_user_stats(**kwargs)
        if (
            action
            == "admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates(
                **kwargs
            )
        if action == "admin_cloud_search_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_search_users(**kwargs)
        if action == "admin_cloud_post_v1_orgs_org_id_users_invite":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v1_orgs_org_id_users_invite(**kwargs)
        if (
            action
            == "admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access(
                **kwargs
            )
        if (
            action
            == "admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access(
                **kwargs
            )
        if action == "admin_cloud_delete_v1_orgs_org_id_directory_users_account_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_delete_v1_orgs_org_id_directory_users_account_id(
                **kwargs
            )
        if action == "admin_cloud_get_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_groups(**kwargs)
        if action == "admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return (
                client.admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups(
                    **kwargs
                )
            )
        if action == "admin_cloud_get_group_role_assignments":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_group_role_assignments(**kwargs)
        if (
            action
            == "admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign(
                **kwargs
            )
        if (
            action
            == "admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke(
                **kwargs
            )
        if (
            action
            == "admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships(
                **kwargs
            )
        if (
            action
            == "admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id(
                **kwargs
            )
        if (
            action
            == "admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id(
                **kwargs
            )
        if action == "admin_cloud_get_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_group(**kwargs)
        if action == "admin_cloud_get_groups_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_groups_count(**kwargs)
        if action == "admin_cloud_get_groups_stats":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_groups_stats(**kwargs)
        if action == "admin_cloud_search_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_search_groups(**kwargs)
        if action == "admin_cloud_post_v1_orgs_org_id_directory_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v1_orgs_org_id_directory_groups(**kwargs)
        if action == "admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id(
                **kwargs
            )
        if action == "admin_cloud_assign_role_to_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_assign_role_to_group(**kwargs)
        if action == "admin_cloud_revoke_role_to_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_revoke_role_to_group(**kwargs)
        if (
            action
            == "admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships(
                **kwargs
            )
        if (
            action
            == "admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id(
                **kwargs
            )
        if action == "admin_cloud_get_directories_for_org":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_directories_for_org(**kwargs)
        if action == "admin_cloud_get_domains":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_domains(**kwargs)
        if action == "admin_cloud_get_domain_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_domain_by_id(**kwargs)
        if action == "admin_cloud_get_events":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_events(**kwargs)
        if action == "admin_cloud_poll_events":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_poll_events(**kwargs)
        if action == "admin_cloud_get_event_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_event_by_id(**kwargs)
        if action == "admin_cloud_get_event_actions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_event_actions(**kwargs)
        if action == "admin_cloud_get_policies":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_policies(**kwargs)
        if action == "admin_cloud_create_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_create_policy(**kwargs)
        if action == "admin_cloud_get_policy_by_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_get_policy_by_id(**kwargs)
        if action == "admin_cloud_update_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_update_policy(**kwargs)
        if action == "admin_cloud_delete_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_delete_policy(**kwargs)
        if action == "admin_cloud_add_resource_to_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_add_resource_to_policy(**kwargs)
        if action == "admin_cloud_update_policy_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_update_policy_resource(**kwargs)
        if action == "admin_cloud_delete_policy_resource":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_delete_policy_resource(**kwargs)
        if action == "admin_cloud_validate_policy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_validate_policy(**kwargs)
        if action == "admin_cloud_query_workspaces_v2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admin_cloud_query_workspaces_v2(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: admin_cloud_get_orgs', 'admin_cloud_get_org_by_id', 'admin_cloud_get_directory_users', 'admin_cloud_get_directory_user_details', 'admin_cloud_get_users', 'admin_cloud_post_v2_orgs_org_id_users_invite', 'admin_cloud_get_user_role_assignments', 'admin_cloud_assign_role', 'admin_cloud_revoke_role', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore', 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id', 'admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign', 'admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke', 'admin_cloud_get_directory_users_count', 'admin_cloud_get_user_stats', 'admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates', 'admin_cloud_search_users', 'admin_cloud_post_v1_orgs_org_id_users_invite', 'admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access', 'admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access', 'admin_cloud_delete_v1_orgs_org_id_directory_users_account_id', 'admin_cloud_get_groups', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups', 'admin_cloud_get_group_role_assignments', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke', 'admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships', 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id', 'admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id', 'admin_cloud_get_group', 'admin_cloud_get_groups_count', 'admin_cloud_get_groups_stats', 'admin_cloud_search_groups', 'admin_cloud_post_v1_orgs_org_id_directory_groups', 'admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id', 'admin_cloud_assign_role_to_group', 'admin_cloud_revoke_role_to_group', 'admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships', 'admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id', 'admin_cloud_get_directories_for_org', 'admin_cloud_get_domains', 'admin_cloud_get_domain_by_id', 'admin_cloud_get_events', 'admin_cloud_poll_events', 'admin_cloud_get_event_by_id', 'admin_cloud_get_event_actions', 'admin_cloud_get_policies', 'admin_cloud_create_policy', 'admin_cloud_get_policy_by_id', 'admin_cloud_update_policy', 'admin_cloud_delete_policy', 'admin_cloud_add_resource_to_policy', 'admin_cloud_update_policy_resource', 'admin_cloud_delete_policy_resource', 'admin_cloud_validate_policy', 'admin_cloud_query_workspaces_v2"
        )


def register_atlassian_api_access_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-api-access"})
    async def atlassian_atlassian_api_access(
        action: str = Field(
            description="Action to perform. Must be one of: 'api_access_cloud_get_all_api_tokens_by_org_id', 'api_access_cloud_bulk_revoke_api_tokens', 'api_access_cloud_get_api_token_count_by_org_id', 'api_access_cloud_count_service_account_api_tokens', 'api_access_cloud_get_service_account_api_token', 'api_access_cloud_revoke_api_tokens', 'api_access_cloud_get_api_key_count_by_org_id', 'api_access_cloud_get_all_api_keys_by_org_id', 'api_access_cloud_revoke_api_key'"
        ),
        client=Depends(get_api_access_cloud_client),
    ) -> dict:
        """Manage atlassian api access operations.

        Actions:
          - 'api_access_cloud_get_all_api_tokens_by_org_id': Call api_access_cloud_get_all_api_tokens_by_org_id
          - 'api_access_cloud_bulk_revoke_api_tokens': Call api_access_cloud_bulk_revoke_api_tokens
          - 'api_access_cloud_get_api_token_count_by_org_id': Call api_access_cloud_get_api_token_count_by_org_id
          - 'api_access_cloud_count_service_account_api_tokens': Call api_access_cloud_count_service_account_api_tokens
          - 'api_access_cloud_get_service_account_api_token': Call api_access_cloud_get_service_account_api_token
          - 'api_access_cloud_revoke_api_tokens': Call api_access_cloud_revoke_api_tokens
          - 'api_access_cloud_get_api_key_count_by_org_id': Call api_access_cloud_get_api_key_count_by_org_id
          - 'api_access_cloud_get_all_api_keys_by_org_id': Call api_access_cloud_get_all_api_keys_by_org_id
          - 'api_access_cloud_revoke_api_key': Call api_access_cloud_revoke_api_key
        """
        kwargs: dict[str, Any]
        if action == "api_access_cloud_get_all_api_tokens_by_org_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_get_all_api_tokens_by_org_id(**kwargs)
        if action == "api_access_cloud_bulk_revoke_api_tokens":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_bulk_revoke_api_tokens(**kwargs)
        if action == "api_access_cloud_get_api_token_count_by_org_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_get_api_token_count_by_org_id(**kwargs)
        if action == "api_access_cloud_count_service_account_api_tokens":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_count_service_account_api_tokens(**kwargs)
        if action == "api_access_cloud_get_service_account_api_token":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_get_service_account_api_token(**kwargs)
        if action == "api_access_cloud_revoke_api_tokens":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_revoke_api_tokens(**kwargs)
        if action == "api_access_cloud_get_api_key_count_by_org_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_get_api_key_count_by_org_id(**kwargs)
        if action == "api_access_cloud_get_all_api_keys_by_org_id":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_get_all_api_keys_by_org_id(**kwargs)
        if action == "api_access_cloud_revoke_api_key":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.api_access_cloud_revoke_api_key(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: api_access_cloud_get_all_api_tokens_by_org_id', 'api_access_cloud_bulk_revoke_api_tokens', 'api_access_cloud_get_api_token_count_by_org_id', 'api_access_cloud_count_service_account_api_tokens', 'api_access_cloud_get_service_account_api_token', 'api_access_cloud_revoke_api_tokens', 'api_access_cloud_get_api_key_count_by_org_id', 'api_access_cloud_get_all_api_keys_by_org_id', 'api_access_cloud_revoke_api_key"
        )


def register_atlassian_user_provisioning_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-user-provisioning"})
    async def atlassian_atlassian_user_provisioning(
        action: str = Field(
            description="Action to perform. Must be one of: 'user_provisioning_cloud_get', 'user_provisioning_cloud_put', 'user_provisioning_cloud_delete_a_group', 'user_provisioning_cloud_patch', 'user_provisioning_cloud_get_all_groups_from_an_active_directory', 'user_provisioning_cloud_create_a_group_in_active_directory', 'user_provisioning_cloud_get_schemas', 'user_provisioning_cloud_get_resource_types', 'user_provisioning_cloud_get_user_resource_type', 'user_provisioning_cloud_get_group_resource_type', 'user_provisioning_cloud_get_user_schemas', 'user_provisioning_cloud_get_group_schemas', 'user_provisioning_cloud_get_extension_user_schemas', 'user_provisioning_cloud_get_config', 'user_provisioning_cloud_get_a_user_from_active_directory', 'user_provisioning_cloud_update_user_information_in_an_active_directory', 'user_provisioning_cloud_delete_a_user_from_an_active_directory', 'user_provisioning_cloud_patch_user_information_in_an_active_directory', 'user_provisioning_cloud_get_users_from_an_active_directory', 'user_provisioning_cloud_create_a_user_in_an_active_directory', 'user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db', 'user_provisioning_cloud_get_scim_links', 'user_provisioning_cloud_get_scim_links_by_email', 'user_provisioning_cloud_unlink_scim_user'"
        ),
        client=Depends(get_user_provisioning_cloud_client),
    ) -> dict:
        """Manage atlassian user provisioning operations.

        Actions:
          - 'user_provisioning_cloud_get': Call user_provisioning_cloud_get
          - 'user_provisioning_cloud_put': Call user_provisioning_cloud_put
          - 'user_provisioning_cloud_delete_a_group': Call user_provisioning_cloud_delete_a_group
          - 'user_provisioning_cloud_patch': Call user_provisioning_cloud_patch
          - 'user_provisioning_cloud_get_all_groups_from_an_active_directory': Call user_provisioning_cloud_get_all_groups_from_an_active_directory
          - 'user_provisioning_cloud_create_a_group_in_active_directory': Call user_provisioning_cloud_create_a_group_in_active_directory
          - 'user_provisioning_cloud_get_schemas': Call user_provisioning_cloud_get_schemas
          - 'user_provisioning_cloud_get_resource_types': Call user_provisioning_cloud_get_resource_types
          - 'user_provisioning_cloud_get_user_resource_type': Call user_provisioning_cloud_get_user_resource_type
          - 'user_provisioning_cloud_get_group_resource_type': Call user_provisioning_cloud_get_group_resource_type
          - 'user_provisioning_cloud_get_user_schemas': Call user_provisioning_cloud_get_user_schemas
          - 'user_provisioning_cloud_get_group_schemas': Call user_provisioning_cloud_get_group_schemas
          - 'user_provisioning_cloud_get_extension_user_schemas': Call user_provisioning_cloud_get_extension_user_schemas
          - 'user_provisioning_cloud_get_config': Call user_provisioning_cloud_get_config
          - 'user_provisioning_cloud_get_a_user_from_active_directory': Call user_provisioning_cloud_get_a_user_from_active_directory
          - 'user_provisioning_cloud_update_user_information_in_an_active_directory': Call user_provisioning_cloud_update_user_information_in_an_active_directory
          - 'user_provisioning_cloud_delete_a_user_from_an_active_directory': Call user_provisioning_cloud_delete_a_user_from_an_active_directory
          - 'user_provisioning_cloud_patch_user_information_in_an_active_directory': Call user_provisioning_cloud_patch_user_information_in_an_active_directory
          - 'user_provisioning_cloud_get_users_from_an_active_directory': Call user_provisioning_cloud_get_users_from_an_active_directory
          - 'user_provisioning_cloud_create_a_user_in_an_active_directory': Call user_provisioning_cloud_create_a_user_in_an_active_directory
          - 'user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db': Call user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db
          - 'user_provisioning_cloud_get_scim_links': Call user_provisioning_cloud_get_scim_links
          - 'user_provisioning_cloud_get_scim_links_by_email': Call user_provisioning_cloud_get_scim_links_by_email
          - 'user_provisioning_cloud_unlink_scim_user': Call user_provisioning_cloud_unlink_scim_user
        """
        kwargs: dict[str, Any]
        if action == "user_provisioning_cloud_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get(**kwargs)
        if action == "user_provisioning_cloud_put":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_put(**kwargs)
        if action == "user_provisioning_cloud_delete_a_group":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_delete_a_group(**kwargs)
        if action == "user_provisioning_cloud_patch":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_patch(**kwargs)
        if action == "user_provisioning_cloud_get_all_groups_from_an_active_directory":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return (
                client.user_provisioning_cloud_get_all_groups_from_an_active_directory(
                    **kwargs
                )
            )
        if action == "user_provisioning_cloud_create_a_group_in_active_directory":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_create_a_group_in_active_directory(
                **kwargs
            )
        if action == "user_provisioning_cloud_get_schemas":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_schemas(**kwargs)
        if action == "user_provisioning_cloud_get_resource_types":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_resource_types(**kwargs)
        if action == "user_provisioning_cloud_get_user_resource_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_user_resource_type(**kwargs)
        if action == "user_provisioning_cloud_get_group_resource_type":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_group_resource_type(**kwargs)
        if action == "user_provisioning_cloud_get_user_schemas":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_user_schemas(**kwargs)
        if action == "user_provisioning_cloud_get_group_schemas":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_group_schemas(**kwargs)
        if action == "user_provisioning_cloud_get_extension_user_schemas":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_extension_user_schemas(**kwargs)
        if action == "user_provisioning_cloud_get_config":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_config(**kwargs)
        if action == "user_provisioning_cloud_get_a_user_from_active_directory":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_a_user_from_active_directory(
                **kwargs
            )
        if (
            action
            == "user_provisioning_cloud_update_user_information_in_an_active_directory"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_update_user_information_in_an_active_directory(
                **kwargs
            )
        if action == "user_provisioning_cloud_delete_a_user_from_an_active_directory":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return (
                client.user_provisioning_cloud_delete_a_user_from_an_active_directory(
                    **kwargs
                )
            )
        if (
            action
            == "user_provisioning_cloud_patch_user_information_in_an_active_directory"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_patch_user_information_in_an_active_directory(
                **kwargs
            )
        if action == "user_provisioning_cloud_get_users_from_an_active_directory":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_users_from_an_active_directory(
                **kwargs
            )
        if action == "user_provisioning_cloud_create_a_user_in_an_active_directory":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_create_a_user_in_an_active_directory(
                **kwargs
            )
        if (
            action
            == "user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db"
        ):
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db(
                **kwargs
            )
        if action == "user_provisioning_cloud_get_scim_links":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_scim_links(**kwargs)
        if action == "user_provisioning_cloud_get_scim_links_by_email":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_get_scim_links_by_email(**kwargs)
        if action == "user_provisioning_cloud_unlink_scim_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.user_provisioning_cloud_unlink_scim_user(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: user_provisioning_cloud_get', 'user_provisioning_cloud_put', 'user_provisioning_cloud_delete_a_group', 'user_provisioning_cloud_patch', 'user_provisioning_cloud_get_all_groups_from_an_active_directory', 'user_provisioning_cloud_create_a_group_in_active_directory', 'user_provisioning_cloud_get_schemas', 'user_provisioning_cloud_get_resource_types', 'user_provisioning_cloud_get_user_resource_type', 'user_provisioning_cloud_get_group_resource_type', 'user_provisioning_cloud_get_user_schemas', 'user_provisioning_cloud_get_group_schemas', 'user_provisioning_cloud_get_extension_user_schemas', 'user_provisioning_cloud_get_config', 'user_provisioning_cloud_get_a_user_from_active_directory', 'user_provisioning_cloud_update_user_information_in_an_active_directory', 'user_provisioning_cloud_delete_a_user_from_an_active_directory', 'user_provisioning_cloud_patch_user_information_in_an_active_directory', 'user_provisioning_cloud_get_users_from_an_active_directory', 'user_provisioning_cloud_create_a_user_in_an_active_directory', 'user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db', 'user_provisioning_cloud_get_scim_links', 'user_provisioning_cloud_get_scim_links_by_email', 'user_provisioning_cloud_unlink_scim_user"
        )


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="atlassian-agent MCP",
        version=__version__,
        instructions="atlassian-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    DEFAULT_ATLASSIAN_CONTROLTOOL = to_boolean(
        os.getenv("ATLASSIAN_CONTROLTOOL", "True")
    )
    if DEFAULT_ATLASSIAN_CONTROLTOOL:
        register_atlassian_control_tools(mcp)
    DEFAULT_ATLASSIAN_ORGTOOL = to_boolean(os.getenv("ATLASSIAN_ORGTOOL", "True"))
    if DEFAULT_ATLASSIAN_ORGTOOL:
        register_atlassian_org_tools(mcp)
    DEFAULT_JIRA_SERVER_OTHERTOOL = to_boolean(
        os.getenv("JIRA_SERVER_OTHERTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_OTHERTOOL:
        register_jira_server_other_tools(mcp)
    DEFAULT_JIRA_SERVER_AGILE_BOARDTOOL = to_boolean(
        os.getenv("JIRA_SERVER_AGILE_BOARDTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_AGILE_BOARDTOOL:
        register_jira_server_agile_board_tools(mcp)
    DEFAULT_JIRA_SERVER_AGILE_EPICTOOL = to_boolean(
        os.getenv("JIRA_SERVER_AGILE_EPICTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_AGILE_EPICTOOL:
        register_jira_server_agile_epic_tools(mcp)
    DEFAULT_JIRA_SERVER_PROJECTTOOL = to_boolean(
        os.getenv("JIRA_SERVER_PROJECTTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PROJECTTOOL:
        register_jira_server_project_tools(mcp)
    DEFAULT_JIRA_SERVER_AGILE_SPRINTTOOL = to_boolean(
        os.getenv("JIRA_SERVER_AGILE_SPRINTTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_AGILE_SPRINTTOOL:
        register_jira_server_agile_sprint_tools(mcp)
    DEFAULT_JIRA_SERVER_SCREENTOOL = to_boolean(
        os.getenv("JIRA_SERVER_SCREENTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_SCREENTOOL:
        register_jira_server_screen_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_ATTACHMENTTOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_ATTACHMENTTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_ATTACHMENTTOOL:
        register_jira_server_issue_attachment_tools(mcp)
    DEFAULT_JIRA_SERVER_SYSTEMTOOL = to_boolean(
        os.getenv("JIRA_SERVER_SYSTEMTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_SYSTEMTOOL:
        register_jira_server_system_tools(mcp)
    DEFAULT_JIRA_SERVER_ADMIN_INDEXTOOL = to_boolean(
        os.getenv("JIRA_SERVER_ADMIN_INDEXTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ADMIN_INDEXTOOL:
        register_jira_server_admin_index_tools(mcp)
    DEFAULT_JIRA_SERVER_ADMIN_UPGRADETOOL = to_boolean(
        os.getenv("JIRA_SERVER_ADMIN_UPGRADETOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ADMIN_UPGRADETOOL:
        register_jira_server_admin_upgrade_tools(mcp)
    DEFAULT_JIRA_SERVER_FIELDTOOL = to_boolean(
        os.getenv("JIRA_SERVER_FIELDTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_FIELDTOOL:
        register_jira_server_field_tools(mcp)
    DEFAULT_JIRA_SERVER_FILTERTOOL = to_boolean(
        os.getenv("JIRA_SERVER_FILTERTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_FILTERTOOL:
        register_jira_server_filter_tools(mcp)
    DEFAULT_JIRA_SERVER_PERMISSIONTOOL = to_boolean(
        os.getenv("JIRA_SERVER_PERMISSIONTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PERMISSIONTOOL:
        register_jira_server_permission_tools(mcp)
    DEFAULT_JIRA_SERVER_GROUPTOOL = to_boolean(
        os.getenv("JIRA_SERVER_GROUPTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_GROUPTOOL:
        register_jira_server_group_tools(mcp)
    DEFAULT_JIRA_SERVER_USERTOOL = to_boolean(os.getenv("JIRA_SERVER_USERTOOL", "True"))
    if DEFAULT_JIRA_SERVER_USERTOOL:
        register_jira_server_user_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_TYPETOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_TYPETOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_TYPETOOL:
        register_jira_server_issue_type_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_LINKTOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_LINKTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_LINKTOOL:
        register_jira_server_issue_link_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_COMMENTTOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_COMMENTTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_COMMENTTOOL:
        register_jira_server_issue_comment_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_SUBTASKTOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_SUBTASKTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_SUBTASKTOOL:
        register_jira_server_issue_subtask_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_TRANSITIONTOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_TRANSITIONTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_TRANSITIONTOOL:
        register_jira_server_issue_transition_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_VOTETOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_VOTETOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_VOTETOOL:
        register_jira_server_issue_vote_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_WATCHERTOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_WATCHERTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_WATCHERTOOL:
        register_jira_server_issue_watcher_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_WORKLOGTOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_WORKLOGTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_WORKLOGTOOL:
        register_jira_server_issue_worklog_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_LINK_TYPETOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_LINK_TYPETOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_LINK_TYPETOOL:
        register_jira_server_issue_link_type_tools(mcp)
    DEFAULT_JIRA_SERVER_ISSUE_TYPE_SCHEMETOOL = to_boolean(
        os.getenv("JIRA_SERVER_ISSUE_TYPE_SCHEMETOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_ISSUE_TYPE_SCHEMETOOL:
        register_jira_server_issue_type_scheme_tools(mcp)
    DEFAULT_JIRA_SERVER_PERMISSION_SCHEMETOOL = to_boolean(
        os.getenv("JIRA_SERVER_PERMISSION_SCHEMETOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PERMISSION_SCHEMETOOL:
        register_jira_server_permission_scheme_tools(mcp)
    DEFAULT_JIRA_SERVER_PRIORITYTOOL = to_boolean(
        os.getenv("JIRA_SERVER_PRIORITYTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PRIORITYTOOL:
        register_jira_server_priority_tools(mcp)
    DEFAULT_JIRA_SERVER_PRIORITY_SCHEMETOOL = to_boolean(
        os.getenv("JIRA_SERVER_PRIORITY_SCHEMETOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PRIORITY_SCHEMETOOL:
        register_jira_server_priority_scheme_tools(mcp)
    DEFAULT_JIRA_SERVER_PROJECT_AVATARTOOL = to_boolean(
        os.getenv("JIRA_SERVER_PROJECT_AVATARTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PROJECT_AVATARTOOL:
        register_jira_server_project_avatar_tools(mcp)
    DEFAULT_JIRA_SERVER_PROJECT_COMPONENTTOOL = to_boolean(
        os.getenv("JIRA_SERVER_PROJECT_COMPONENTTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PROJECT_COMPONENTTOOL:
        register_jira_server_project_component_tools(mcp)
    DEFAULT_JIRA_SERVER_PROJECT_ROLETOOL = to_boolean(
        os.getenv("JIRA_SERVER_PROJECT_ROLETOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PROJECT_ROLETOOL:
        register_jira_server_project_role_tools(mcp)
    DEFAULT_JIRA_SERVER_PROJECT_CATEGORYTOOL = to_boolean(
        os.getenv("JIRA_SERVER_PROJECT_CATEGORYTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_PROJECT_CATEGORYTOOL:
        register_jira_server_project_category_tools(mcp)
    DEFAULT_JIRA_SERVER_RESOLUTIONTOOL = to_boolean(
        os.getenv("JIRA_SERVER_RESOLUTIONTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_RESOLUTIONTOOL:
        register_jira_server_resolution_tools(mcp)
    DEFAULT_JIRA_SERVER_SEARCHTOOL = to_boolean(
        os.getenv("JIRA_SERVER_SEARCHTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_SEARCHTOOL:
        register_jira_server_search_tools(mcp)
    DEFAULT_JIRA_SERVER_USER_AVATARTOOL = to_boolean(
        os.getenv("JIRA_SERVER_USER_AVATARTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_USER_AVATARTOOL:
        register_jira_server_user_avatar_tools(mcp)
    DEFAULT_JIRA_SERVER_WORKFLOWTOOL = to_boolean(
        os.getenv("JIRA_SERVER_WORKFLOWTOOL", "True")
    )
    if DEFAULT_JIRA_SERVER_WORKFLOWTOOL:
        register_jira_server_workflow_tools(mcp)
    DEFAULT_JIRA_CLOUD_USERTOOL = to_boolean(os.getenv("JIRA_CLOUD_USERTOOL", "True"))
    if DEFAULT_JIRA_CLOUD_USERTOOL:
        register_jira_cloud_user_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_FIELDTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_FIELDTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_FIELDTOOL:
        register_jira_cloud_schema_field_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_FIELD_CONFIGURATIONTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_FIELD_CONFIGURATIONTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_FIELD_CONFIGURATIONTOOL:
        register_jira_cloud_schema_field_configuration_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_FIELD_OPTIONTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_FIELD_OPTIONTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_FIELD_OPTIONTOOL:
        register_jira_cloud_schema_field_option_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_OTHERTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_OTHERTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_OTHERTOOL:
        register_jira_cloud_schema_other_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_FIELD_CONTEXTTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_FIELD_CONTEXTTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_FIELD_CONTEXTTOOL:
        register_jira_cloud_schema_field_context_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_SCREENTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_SCREENTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_SCREENTOOL:
        register_jira_cloud_schema_screen_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_FIELD_CONFIGURATION_SCHEMETOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_FIELD_CONFIGURATION_SCHEMETOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_FIELD_CONFIGURATION_SCHEMETOOL:
        register_jira_cloud_schema_field_configuration_scheme_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_SCREEN_SCHEMETOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_SCREEN_SCHEMETOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_SCREEN_SCHEMETOOL:
        register_jira_cloud_schema_screen_scheme_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_NOTIFICATION_SCHEMETOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_NOTIFICATION_SCHEMETOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_NOTIFICATION_SCHEMETOOL:
        register_jira_cloud_schema_notification_scheme_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_PRIORITYTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_PRIORITYTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_PRIORITYTOOL:
        register_jira_cloud_schema_priority_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_PRIORITY_SCHEMETOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_PRIORITY_SCHEMETOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_PRIORITY_SCHEMETOOL:
        register_jira_cloud_schema_priority_scheme_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_STATUSTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_STATUSTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_STATUSTOOL:
        register_jira_cloud_schema_status_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_RESOLUTIONTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_RESOLUTIONTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_RESOLUTIONTOOL:
        register_jira_cloud_schema_resolution_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_SCREEN_TABTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_SCREEN_TABTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_SCREEN_TABTOOL:
        register_jira_cloud_schema_screen_tab_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_SCREEN_TAB_FIELDTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_SCREEN_TAB_FIELDTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_SCREEN_TAB_FIELDTOOL:
        register_jira_cloud_schema_screen_tab_field_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_WORKFLOWTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_WORKFLOWTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_WORKFLOWTOOL:
        register_jira_cloud_schema_workflow_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_WORKFLOW_SCHEMETOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_WORKFLOW_SCHEMETOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_WORKFLOW_SCHEMETOOL:
        register_jira_cloud_schema_workflow_scheme_tools(mcp)
    DEFAULT_JIRA_CLOUD_SCHEMA_WORKFLOW_RULETOOL = to_boolean(
        os.getenv("JIRA_CLOUD_SCHEMA_WORKFLOW_RULETOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_SCHEMA_WORKFLOW_RULETOOL:
        register_jira_cloud_schema_workflow_rule_tools(mcp)
    DEFAULT_JIRA_CLOUD_CORETOOL = to_boolean(os.getenv("JIRA_CLOUD_CORETOOL", "True"))
    if DEFAULT_JIRA_CLOUD_CORETOOL:
        register_jira_cloud_core_tools(mcp)
    DEFAULT_JIRA_CLOUD_PROJECTTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_PROJECTTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_PROJECTTOOL:
        register_jira_cloud_project_tools(mcp)
    DEFAULT_JIRA_CLOUD_ISSUE_ATTACHMENTTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_ISSUE_ATTACHMENTTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_ISSUE_ATTACHMENTTOOL:
        register_jira_cloud_issue_attachment_tools(mcp)
    DEFAULT_JIRA_CLOUD_ISSUE_BULKTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_ISSUE_BULKTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_ISSUE_BULKTOOL:
        register_jira_cloud_issue_bulk_tools(mcp)
    DEFAULT_JIRA_CLOUD_ISSUE_CORETOOL = to_boolean(
        os.getenv("JIRA_CLOUD_ISSUE_CORETOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_ISSUE_CORETOOL:
        register_jira_cloud_issue_core_tools(mcp)
    DEFAULT_JIRA_CLOUD_ISSUE_COMMENTTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_ISSUE_COMMENTTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_ISSUE_COMMENTTOOL:
        register_jira_cloud_issue_comment_tools(mcp)
    DEFAULT_JIRA_CLOUD_ISSUE_TYPETOOL = to_boolean(
        os.getenv("JIRA_CLOUD_ISSUE_TYPETOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_ISSUE_TYPETOOL:
        register_jira_cloud_issue_type_tools(mcp)
    DEFAULT_JIRA_CLOUD_ISSUE_LINKTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_ISSUE_LINKTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_ISSUE_LINKTOOL:
        register_jira_cloud_issue_link_tools(mcp)
    DEFAULT_JIRA_CLOUD_ISSUE_WATCHERTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_ISSUE_WATCHERTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_ISSUE_WATCHERTOOL:
        register_jira_cloud_issue_watcher_tools(mcp)
    DEFAULT_JIRA_CLOUD_ISSUE_WORKLOGTOOL = to_boolean(
        os.getenv("JIRA_CLOUD_ISSUE_WORKLOGTOOL", "True")
    )
    if DEFAULT_JIRA_CLOUD_ISSUE_WORKLOGTOOL:
        register_jira_cloud_issue_worklog_tools(mcp)
    DEFAULT_JIRA_CLOUD_OTHERTOOL = to_boolean(os.getenv("JIRA_CLOUD_OTHERTOOL", "True"))
    if DEFAULT_JIRA_CLOUD_OTHERTOOL:
        register_jira_cloud_other_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_OTHERTOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_OTHERTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_OTHERTOOL:
        register_confluence_cloud_other_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_ATTACHMENTTOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_ATTACHMENTTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_ATTACHMENTTOOL:
        register_confluence_cloud_attachment_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_LABELTOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_LABELTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_LABELTOOL:
        register_confluence_cloud_label_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_USERTOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_USERTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_USERTOOL:
        register_confluence_cloud_user_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_CONTENT_PROPERTYTOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_CONTENT_PROPERTYTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_CONTENT_PROPERTYTOOL:
        register_confluence_cloud_content_property_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_PAGE_CORETOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_PAGE_CORETOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_PAGE_CORETOOL:
        register_confluence_cloud_page_core_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_PAGE_CONTENTTOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_PAGE_CONTENTTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_PAGE_CONTENTTOOL:
        register_confluence_cloud_page_content_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_SPACE_CORETOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_SPACE_CORETOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_SPACE_CORETOOL:
        register_confluence_cloud_space_core_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_SPACE_PROPERTYTOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_SPACE_PROPERTYTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_SPACE_PROPERTYTOOL:
        register_confluence_cloud_space_property_tools(mcp)
    DEFAULT_CONFLUENCE_CLOUD_SPACE_PERMISSIONTOOL = to_boolean(
        os.getenv("CONFLUENCE_CLOUD_SPACE_PERMISSIONTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_CLOUD_SPACE_PERMISSIONTOOL:
        register_confluence_cloud_space_permission_tools(mcp)
    DEFAULT_CONFLUENCE_SERVER_OTHERTOOL = to_boolean(
        os.getenv("CONFLUENCE_SERVER_OTHERTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_SERVER_OTHERTOOL:
        register_confluence_server_other_tools(mcp)
    DEFAULT_CONFLUENCE_SERVER_USERTOOL = to_boolean(
        os.getenv("CONFLUENCE_SERVER_USERTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_SERVER_USERTOOL:
        register_confluence_server_user_tools(mcp)
    DEFAULT_CONFLUENCE_SERVER_SPACETOOL = to_boolean(
        os.getenv("CONFLUENCE_SERVER_SPACETOOL", "True")
    )
    if DEFAULT_CONFLUENCE_SERVER_SPACETOOL:
        register_confluence_server_space_tools(mcp)
    DEFAULT_CONFLUENCE_SERVER_CONTENT_CHILDTOOL = to_boolean(
        os.getenv("CONFLUENCE_SERVER_CONTENT_CHILDTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_SERVER_CONTENT_CHILDTOOL:
        register_confluence_server_content_child_tools(mcp)
    DEFAULT_CONFLUENCE_SERVER_CONTENTTOOL = to_boolean(
        os.getenv("CONFLUENCE_SERVER_CONTENTTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_SERVER_CONTENTTOOL:
        register_confluence_server_content_tools(mcp)
    DEFAULT_CONFLUENCE_SERVER_CONTENT_HISTORYTOOL = to_boolean(
        os.getenv("CONFLUENCE_SERVER_CONTENT_HISTORYTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_SERVER_CONTENT_HISTORYTOOL:
        register_confluence_server_content_history_tools(mcp)
    DEFAULT_CONFLUENCE_SERVER_GROUPTOOL = to_boolean(
        os.getenv("CONFLUENCE_SERVER_GROUPTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_SERVER_GROUPTOOL:
        register_confluence_server_group_tools(mcp)
    DEFAULT_CONFLUENCE_SERVER_SPACE_PERMISSIONTOOL = to_boolean(
        os.getenv("CONFLUENCE_SERVER_SPACE_PERMISSIONTOOL", "True")
    )
    if DEFAULT_CONFLUENCE_SERVER_SPACE_PERMISSIONTOOL:
        register_confluence_server_space_permission_tools(mcp)
    DEFAULT_ATLASSIAN_DLPTOOL = to_boolean(os.getenv("ATLASSIAN_DLPTOOL", "True"))
    if DEFAULT_ATLASSIAN_DLPTOOL:
        register_atlassian_dlp_tools(mcp)
    DEFAULT_ATLASSIAN_USER_MGMTTOOL = to_boolean(
        os.getenv("ATLASSIAN_USER_MGMTTOOL", "True")
    )
    if DEFAULT_ATLASSIAN_USER_MGMTTOOL:
        register_atlassian_user_mgmt_tools(mcp)
    DEFAULT_ATLASSIANTOOL = to_boolean(os.getenv("ATLASSIANTOOL", "True"))
    if DEFAULT_ATLASSIANTOOL:
        register_atlassian_tools(mcp)
    DEFAULT_ATLASSIAN_ADMINTOOL = to_boolean(os.getenv("ATLASSIAN_ADMINTOOL", "True"))
    if DEFAULT_ATLASSIAN_ADMINTOOL:
        register_atlassian_admin_tools(mcp)
    DEFAULT_ATLASSIAN_API_ACCESSTOOL = to_boolean(
        os.getenv("ATLASSIAN_API_ACCESSTOOL", "True")
    )
    if DEFAULT_ATLASSIAN_API_ACCESSTOOL:
        register_atlassian_api_access_tools(mcp)
    DEFAULT_ATLASSIAN_USER_PROVISIONINGTOOL = to_boolean(
        os.getenv("ATLASSIAN_USER_PROVISIONINGTOOL", "True")
    )
    if DEFAULT_ATLASSIAN_USER_PROVISIONINGTOOL:
        register_atlassian_user_provisioning_tools(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    mcp, args, middlewares = get_mcp_instance()
    print(f"atlassian-agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
