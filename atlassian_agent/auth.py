import threading

from agent_connector_sdk.config import setting
from agent_connector_sdk.tls.resolve import resolve_tls_profile
from agent_connector_sdk.utilities import get_logger

from .api.base import BaseAtlassianClient

local = threading.local()
logger = get_logger(__name__)

_base_client = None


def _entitled(namespace: str, names) -> list[str]:
    """Filter ``names`` to the subset the calling identity's Okta/Keycloak groups
    entitle (CONCEPT:AU-OS.identity.identity-scoped-resource-autoload). Degrades
    to the full list if agent-utilities predates the resolver, or if the current
    context has no verified, tenant-bound actor to resolve against (e.g. an
    unauthenticated/local SYSTEM_ACTOR context) — sees all, unchanged from today.
    """
    try:
        from agent_utilities.security.entitlements import identity_scoped_resources

        return list(identity_scoped_resources(namespace, names))
    except Exception:
        return list(names)


def _resolve_suite_settings(
    suite_prefix: str | None,
) -> tuple[str | None, str | None, str | None, str | None]:
    """Resolve url/user/token/tls_profile_name for one suite, falling back to shared env vars."""
    if suite_prefix:
        url = setting(f"ATLASSIAN_{suite_prefix}_URL")
        user = setting(f"ATLASSIAN_{suite_prefix}_USER")
        token = setting(f"ATLASSIAN_{suite_prefix}_TOKEN")
        tls_profile_name = setting(f"ATLASSIAN_{suite_prefix}_TLS_PROFILE")
    else:
        url = user = token = tls_profile_name = None

    # fallback to shared
    url = url or setting("ATLASSIAN_AGENT_URL")
    user = user or setting("ATLASSIAN_AGENT_USER")
    token = token or setting("ATLASSIAN_AGENT_TOKEN")
    return url, user, token, tls_profile_name


def _delegated_client(url, user, tls_profile) -> BaseAtlassianClient | None:
    """Path 1: OIDC Delegation (RFC 8693 Token Exchange). None if disabled or it fails."""
    from agent_utilities.mcp.delegated_auth import (
        get_delegated_token,
        is_delegation_enabled,
    )

    if not is_delegation_enabled():
        return None
    try:
        delegated_token = get_delegated_token(
            audience=setting("AUDIENCE", url),
            scopes=setting("DELEGATED_SCOPES", "read:jira-work write:jira-work"),
        )
        logger.info("Using OIDC delegated token for Atlassian API")
        return BaseAtlassianClient(
            base_url=url or "https://dummy.atlassian.net",
            username=user or "",
            token="",
            tls_profile=tls_profile,
            bearer_token=delegated_token,
        )
    except Exception as e:
        logger.warning("Operation failed: error_type=%s", type(e).__name__)
        return None


def _oauth_3lo_client(url, user, tls_profile) -> BaseAtlassianClient | None:
    """Path 2: 3-Legged OAuth (3LO) Bearer Token. None if not configured."""
    oauth_token = setting("ATLASSIAN_OAUTH_TOKEN")
    if not oauth_token:
        return None
    logger.info("Using 3LO OAuth Bearer token for Atlassian API")
    return BaseAtlassianClient(
        base_url=url or "https://dummy.atlassian.net",
        username=user or "",
        token="",
        tls_profile=tls_profile,
        bearer_token=oauth_token,
    )


def _pat_bearer_client(
    suite_prefix, url, user, tls_profile
) -> BaseAtlassianClient | None:
    """Path 3: Bearer Token / PAT (Server / Data Center). None if not configured."""
    bearer_token = (
        setting(f"ATLASSIAN_{suite_prefix}_BEARER_TOKEN") if suite_prefix else None
    ) or setting("ATLASSIAN_BEARER_TOKEN")
    if not bearer_token:
        return None
    logger.info("Using bearer token (PAT) for Atlassian API")
    return BaseAtlassianClient(
        base_url=url or "https://dummy.atlassian.net",
        username=user or "",
        token="",
        tls_profile=tls_profile,
        bearer_token=bearer_token,
    )


def _basic_auth_client(url, user, token, tls_profile) -> BaseAtlassianClient:
    """Path 4: Basic Auth (email + API token) -- the unconditional fallback."""
    logger.info("Using basic auth credentials for Atlassian API")
    return BaseAtlassianClient(
        base_url=url or "https://dummy.atlassian.net",
        username=user or "",
        token=token or "",
        tls_profile=tls_profile,
    )


def get_suite_client(suite_prefix: str | None = None) -> BaseAtlassianClient:
    """Get client using suite-specific env vars or fall back to shared.

    Authentication priority:
    1. **OIDC Delegation** — If ``ENABLE_DELEGATION`` is active, exchanges
       the IdP-issued user token for a downstream access token via
       RFC 8693 Token Exchange.  The resulting token is used as a Bearer
       token against the Atlassian API.
    2. **3-Legged OAuth (3LO)** — If ``ATLASSIAN_OAUTH_TOKEN`` is set,
       uses it as a Bearer token (obtained via the 3LO consent flow).
    3. **Bearer Token / PAT** — If ``ATLASSIAN_{SUITE}_BEARER_TOKEN`` or the
       shared ``ATLASSIAN_BEARER_TOKEN`` is set, uses it directly as a Bearer
       token.  Intended for Atlassian Server / Data Center Personal Access
       Tokens (sent as ``Authorization: Bearer <PAT>``).
    4. **Environment Variables** — Falls back to ``ATLASSIAN_AGENT_TOKEN``
       with basic auth (email + API token).

    A named ``suite_prefix`` the caller's identity is not entitled to is
    denied before any credential resolution happens.

    See ``docs/guides/oauth_sso.md`` in agent-utilities for full details.
    """
    if suite_prefix and suite_prefix not in _entitled("atlassian", [suite_prefix]):
        raise PermissionError(
            f"Your identity is not entitled to the Atlassian suite '{suite_prefix}'."
        )

    url, user, token, tls_profile_name = _resolve_suite_settings(suite_prefix)

    tls_profile = resolve_tls_profile(
        "ATLASSIAN",
        profile_name=tls_profile_name or setting("ATLASSIAN_TLS_PROFILE"),
    )

    client = _delegated_client(url, user, tls_profile)
    if client is not None:
        return client

    client = _oauth_3lo_client(url, user, tls_profile)
    if client is not None:
        return client

    client = _pat_bearer_client(suite_prefix, url, user, tls_profile)
    if client is not None:
        return client

    return _basic_auth_client(url, user, token, tls_profile)


def get_base_client() -> BaseAtlassianClient:
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
