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
import sys
from typing import Any

from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from fastmcp import Context, FastMCP
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

__version__ = "0.12.0"

logger = get_logger(name="atlassian-agent")
logger.setLevel(logging.INFO)


_registered_tools = set()


def execute_client_method(
    client,
    action: str,
    prefix_cloud: str,
    prefix_server: str,
    host_type: str,
    kwargs: dict,
) -> Any:
    """Helper to dynamically lookup and invoke methods on cloud or server clients."""
    prefix = prefix_server if host_type == "server" else prefix_cloud

    # Try direct name
    method = getattr(client, action, None)
    if method is not None:
        return method(**kwargs)

    # Try with prefix
    action_name = action if action.startswith(prefix) else f"{prefix}{action}"
    method = getattr(client, action_name, None)
    if method is not None:
        return method(**kwargs)

    # Try stripped action name
    stripped = action
    for p in (
        prefix_cloud,
        prefix_server,
        "jira_cloud_",
        "jira_server_",
        "confluence_cloud_",
        "confluence_server_",
    ):
        if stripped.startswith(p):
            stripped = stripped[len(p) :]
            break

    method = getattr(client, f"{prefix}{stripped}", None) or getattr(
        client, stripped, None
    )
    if method is not None:
        return method(**kwargs)

    raise ValueError(f"Unknown action: {action} on {host_type} deployment")


def register_atlassian_control_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-control"})
    async def atlassian_atlassian_control(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        client=Depends(get_control_cloud_client),
    ) -> Any:
        """Manage atlassian control operations."""
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
        raise ValueError(f"Unknown action: {action}")


def register_atlassian_org_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-org"})
    async def atlassian_atlassian_org(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        client=Depends(get_org_cloud_client),
    ) -> Any:
        """Manage atlassian org operations."""
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
        raise ValueError(f"Unknown action: {action}")


def register_atlassian_dlp_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-dlp"})
    async def atlassian_atlassian_dlp(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        client=Depends(get_dlp_cloud_client),
    ) -> Any:
        """Manage atlassian dlp operations."""
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
        raise ValueError(f"Unknown action: {action}")


def register_atlassian_user_mgmt_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-user-mgmt"})
    async def atlassian_atlassian_user_mgmt(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        client=Depends(get_user_mgmt_cloud_client),
    ) -> Any:
        """Manage atlassian user mgmt operations."""
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
        raise ValueError(f"Unknown action: {action}")


def register_atlassian_admin_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-admin"})
    async def atlassian_atlassian_admin(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        client=Depends(get_admin_cloud_client),
    ) -> Any:
        """Manage atlassian admin operations."""
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
        raise ValueError(f"Unknown action: {action}")


def register_atlassian_api_access_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-api-access"})
    async def atlassian_atlassian_api_access(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        client=Depends(get_api_access_cloud_client),
    ) -> Any:
        """Manage atlassian api access operations."""
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
        raise ValueError(f"Unknown action: {action}")


def register_atlassian_user_provisioning_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian-user-provisioning"})
    async def atlassian_atlassian_user_provisioning(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        client=Depends(get_user_provisioning_cloud_client),
    ) -> Any:
        """Manage atlassian user provisioning operations."""
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
        raise ValueError(f"Unknown action: {action}")


def register_atlassian_tools(mcp: FastMCP):
    @mcp.tool(tags={"atlassian"})
    async def atlassian_atlassian(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        client=Depends(get_user_mgmt_cloud_client),
    ) -> Any:
        """Manage atlassian operations."""
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
        raise ValueError(f"Unknown action: {action}")


def register_jira_project_tools(mcp: FastMCP):
    if "jira_project" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_project")

    @mcp.tool(tags={"jira-project"})
    async def atlassian_jira_project(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira project operations."""
        if ctx:
            await ctx.info("Executing jira_project operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_user_tools(mcp: FastMCP):
    if "jira_user" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_user")

    @mcp.tool(tags={"jira-user"})
    async def atlassian_jira_user(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira user operations."""
        if ctx:
            await ctx.info("Executing jira_user operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_issue_tools(mcp: FastMCP):
    if "jira_issue" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_issue")

    @mcp.tool(tags={"jira-issue"})
    async def atlassian_jira_issue(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira issue operations."""
        if ctx:
            await ctx.info("Executing jira_issue operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_comment_tools(mcp: FastMCP):
    if "jira_comment" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_comment")

    @mcp.tool(tags={"jira-comment"})
    async def atlassian_jira_comment(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira comment operations."""
        if ctx:
            await ctx.info("Executing jira_comment operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_field_tools(mcp: FastMCP):
    if "jira_field" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_field")

    @mcp.tool(tags={"jira-field"})
    async def atlassian_jira_field(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira field operations."""
        if ctx:
            await ctx.info("Executing jira_field operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_screen_tools(mcp: FastMCP):
    if "jira_screen" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_screen")

    @mcp.tool(tags={"jira-screen"})
    async def atlassian_jira_screen(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira screen operations."""
        if ctx:
            await ctx.info("Executing jira_screen operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_workflow_tools(mcp: FastMCP):
    if "jira_workflow" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_workflow")

    @mcp.tool(tags={"jira-workflow"})
    async def atlassian_jira_workflow(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira workflow operations."""
        if ctx:
            await ctx.info("Executing jira_workflow operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_other_tools(mcp: FastMCP):
    if "jira_other" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_other")

    @mcp.tool(tags={"jira-other"})
    async def atlassian_jira_other(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira other operations."""
        if ctx:
            await ctx.info("Executing jira_other operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_confluence_page_tools(mcp: FastMCP):
    if "confluence_page" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("confluence_page")

    @mcp.tool(tags={"confluence-page"})
    async def atlassian_confluence_page(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_confluence_cloud_client),
        client_server=Depends(get_confluence_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Confluence page operations."""
        if ctx:
            await ctx.info("Executing confluence_page operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client,
                action,
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_confluence_space_tools(mcp: FastMCP):
    if "confluence_space" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("confluence_space")

    @mcp.tool(tags={"confluence-space"})
    async def atlassian_confluence_space(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_confluence_cloud_client),
        client_server=Depends(get_confluence_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Confluence space operations."""
        if ctx:
            await ctx.info("Executing confluence_space operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client,
                action,
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_confluence_user_tools(mcp: FastMCP):
    if "confluence_user" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("confluence_user")

    @mcp.tool(tags={"confluence-user"})
    async def atlassian_confluence_user(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_confluence_cloud_client),
        client_server=Depends(get_confluence_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Confluence user operations."""
        if ctx:
            await ctx.info("Executing confluence_user operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client,
                action,
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_confluence_other_tools(mcp: FastMCP):
    if "confluence_other" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("confluence_other")

    @mcp.tool(tags={"confluence-other"})
    async def atlassian_confluence_other(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_confluence_cloud_client),
        client_server=Depends(get_confluence_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Confluence other operations."""
        if ctx:
            await ctx.info("Executing confluence_other operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client,
                action,
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


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

    # Register consolidated Atlassian tools
    register_atlassian_control_tools(mcp)
    register_atlassian_org_tools(mcp)

    # Register consolidated Jira tools
    register_jira_project_tools(mcp)
    register_jira_user_tools(mcp)
    register_jira_issue_tools(mcp)
    register_jira_comment_tools(mcp)
    register_jira_field_tools(mcp)
    register_jira_screen_tools(mcp)
    register_jira_workflow_tools(mcp)
    register_jira_other_tools(mcp)

    # Register consolidated Confluence tools
    register_confluence_page_tools(mcp)
    register_confluence_space_tools(mcp)
    register_confluence_user_tools(mcp)
    register_confluence_other_tools(mcp)

    # Register other Atlassian tools
    register_atlassian_dlp_tools(mcp)
    register_atlassian_user_mgmt_tools(mcp)
    register_atlassian_tools(mcp)
    register_atlassian_admin_tools(mcp)
    register_atlassian_api_access_tools(mcp)
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
