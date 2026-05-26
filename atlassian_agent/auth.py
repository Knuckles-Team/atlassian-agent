import os
import threading

import urllib3
from agent_utilities.base_utilities import get_logger, to_boolean

from .api.base import BaseAtlassianClient

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

local = threading.local()
logger = get_logger(__name__)

_base_client = None


def get_suite_client(suite_prefix: str | None = None) -> BaseAtlassianClient:
    """Get client using suite-specific env vars or fall back to shared.

    Authentication priority:
    1. **OIDC Delegation** — If ``ENABLE_DELEGATION`` is active, exchanges
       the IdP-issued user token for a downstream access token via
       RFC 8693 Token Exchange.  The resulting token is used as a Bearer
       token against the Atlassian API.
    2. **3-Legged OAuth (3LO)** — If ``ATLASSIAN_OAUTH_TOKEN`` is set,
       uses it as a Bearer token (obtained via the 3LO consent flow).
    3. **Environment Variables** — Falls back to ``ATLASSIAN_AGENT_TOKEN``
       with basic auth (email + API token).

    See ``docs/guides/oauth_sso.md`` in agent-utilities for full details.
    """
    from agent_utilities.mcp.delegated_auth import (
        get_delegated_token,
        get_user_identity,
        is_delegation_enabled,
    )

    if suite_prefix:
        url = os.getenv(f"ATLASSIAN_{suite_prefix}_URL")
        user = os.getenv(f"ATLASSIAN_{suite_prefix}_USER")
        token = os.getenv(f"ATLASSIAN_{suite_prefix}_TOKEN")
        verify_str = os.getenv(f"ATLASSIAN_{suite_prefix}_VERIFY")
    else:
        url = user = token = verify_str = None

    # fallback to shared
    url = url or os.getenv("ATLASSIAN_AGENT_URL")
    user = user or os.getenv("ATLASSIAN_AGENT_USER")
    token = token or os.getenv("ATLASSIAN_AGENT_TOKEN")

    verify = (
        verify_str.lower() in ("true", "1", "yes")
        if verify_str
        else to_boolean(
            os.getenv(
                "ATLASSIAN_SSL_VERIFY", os.getenv("ATLASSIAN_AGENT_VERIFY", "True")
            )
        )
    )

    # --- Path 1: OIDC Delegation (RFC 8693 Token Exchange) ---
    if is_delegation_enabled():
        try:
            delegated_token = get_delegated_token(
                audience=os.getenv("AUDIENCE", url),
                scopes=os.getenv("DELEGATED_SCOPES", "read:jira-work write:jira-work"),
                verify=verify,
            )
            identity = get_user_identity()
            logger.info(
                "Using OIDC delegated token for Atlassian API",
                extra={
                    "user_email": identity.get("email"),
                    "base_url": url,
                },
            )
            return BaseAtlassianClient(
                base_url=url or "https://dummy.atlassian.net",
                username=user or "",
                token="",
                verify=verify,
                bearer_token=delegated_token,
            )
        except Exception as e:
            logger.warning(f"OIDC delegation failed, falling back to credentials: {e}")

    # --- Path 2: 3-Legged OAuth (3LO) Bearer Token ---
    oauth_token = os.getenv("ATLASSIAN_OAUTH_TOKEN")
    if oauth_token:
        logger.info("Using 3LO OAuth Bearer token for Atlassian API")
        return BaseAtlassianClient(
            base_url=url or "https://dummy.atlassian.net",
            username=user or "",
            token="",
            verify=verify,
            bearer_token=oauth_token,
        )

    # --- Path 3: Basic Auth (email + API token) ---
    logger.info("Using basic auth credentials for Atlassian API")
    return BaseAtlassianClient(
        base_url=url or "https://dummy.atlassian.net",
        username=user or "",
        token=token or "",
        verify=verify,
    )


def get_base_client(
    url: str | None = None,
    user: str | None = None,
    token: str | None = None,
    verify: bool | None = None,
) -> BaseAtlassianClient:
    """Get or create a singleton base API client instance."""
    global _base_client
    if _base_client is None:
        _base_client = get_suite_client(None)
    return _base_client


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api.api_client_admin_cloud import AdminCloudAPI
    from .api.api_client_api_access_cloud import APIAccessCloudAPI
    from .api.api_client_confluence_cloud import ConfluenceCloudAPI
    from .api.api_client_confluence_server import ConfluenceServerAPI
    from .api.api_client_control_cloud import ControlCloudAPI
    from .api.api_client_dlp_cloud import DLPCloudAPI
    from .api.api_client_jira_cloud import JiraCloudAPI
    from .api.api_client_jira_server import JiraServerAPI
    from .api.api_client_org_cloud import OrgCloudAPI
    from .api.api_client_user_mgmt_cloud import UserMgmtCloudAPI
    from .api.api_client_user_provisioning_cloud import UserProvisioningCloudAPI


def get_admin_cloud_client() -> "AdminCloudAPI":
    from .api.api_client_admin_cloud import AdminCloudAPI

    return AdminCloudAPI(get_suite_client("ADMIN_CLOUD"))


def get_api_access_cloud_client() -> "APIAccessCloudAPI":
    from .api.api_client_api_access_cloud import APIAccessCloudAPI

    return APIAccessCloudAPI(get_suite_client("API_ACCESS_CLOUD"))


def get_confluence_cloud_client() -> "ConfluenceCloudAPI":
    from .api.api_client_confluence_cloud import ConfluenceCloudAPI

    return ConfluenceCloudAPI(get_suite_client("CONFLUENCE_CLOUD"))


def get_confluence_server_client() -> "ConfluenceServerAPI":
    from .api.api_client_confluence_server import ConfluenceServerAPI

    return ConfluenceServerAPI(get_suite_client("CONFLUENCE_SERVER"))


def get_control_cloud_client() -> "ControlCloudAPI":
    from .api.api_client_control_cloud import ControlCloudAPI

    return ControlCloudAPI(get_suite_client("CONTROL_CLOUD"))


def get_dlp_cloud_client() -> "DLPCloudAPI":
    from .api.api_client_dlp_cloud import DLPCloudAPI

    return DLPCloudAPI(get_suite_client("DLP_CLOUD"))


def get_jira_cloud_client() -> "JiraCloudAPI":
    from .api.api_client_jira_cloud import JiraCloudAPI

    return JiraCloudAPI(get_suite_client("JIRA_CLOUD"))


def get_jira_server_client() -> "JiraServerAPI":
    from .api.api_client_jira_server import JiraServerAPI

    return JiraServerAPI(get_suite_client("JIRA_SERVER"))


def get_org_cloud_client() -> "OrgCloudAPI":
    from .api.api_client_org_cloud import OrgCloudAPI

    return OrgCloudAPI(get_suite_client("ORG_CLOUD"))


def get_user_mgmt_cloud_client() -> "UserMgmtCloudAPI":
    from .api.api_client_user_mgmt_cloud import UserMgmtCloudAPI

    return UserMgmtCloudAPI(get_suite_client("USER_MGMT_CLOUD"))


def get_user_provisioning_cloud_client() -> "UserProvisioningCloudAPI":
    from .api.api_client_user_provisioning_cloud import UserProvisioningCloudAPI

    return UserProvisioningCloudAPI(get_suite_client("USER_PROVISIONING_CLOUD"))
