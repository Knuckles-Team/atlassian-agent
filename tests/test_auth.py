import importlib
import os
from unittest.mock import MagicMock, patch

import pytest

import atlassian_agent.auth as auth_mod


@pytest.fixture(autouse=True, scope="module")
def restore_real_auth():
    # Save the mocked functions created by conftest.py
    original_mocks = {}
    for name in list(dir(auth_mod)):
        if name.startswith("get_") and name.endswith("_client"):
            original_mocks[name] = getattr(auth_mod, name)

    # Reload auth_mod to get the real implementations
    importlib.reload(auth_mod)

    yield

    # Restore the mocked functions so subsequent test files are not affected
    for name, mock_func in original_mocks.items():
        setattr(auth_mod, name, mock_func)


def test_get_suite_client_basic_auth():
    # Test path 3: Basic Auth with shared environment variables
    env_mock = {
        "ATLASSIAN_AGENT_URL": "https://test.atlassian.net",
        "ATLASSIAN_AGENT_USER": "test-user@domain.com",
        "ATLASSIAN_AGENT_TOKEN": "test-token",
        "ATLASSIAN_AGENT_VERIFY": "True",
    }
    with (
        patch.dict(os.environ, env_mock, clear=True),
        patch(
            "agent_utilities.mcp.delegated_auth.is_delegation_enabled",
            return_value=False,
        ),
    ):
        client = auth_mod.get_suite_client(None)
        assert client.base_url == "https://test.atlassian.net"
        assert client.username == "test-user@domain.com"
        assert client.token == "test-token"
        assert client.verify is True
        assert client.bearer_token is None


def test_get_suite_client_suite_prefix():
    # Test with a specific suite prefix
    env_mock = {
        "ATLASSIAN_JIRA_URL": "https://jira.domain.net",
        "ATLASSIAN_JIRA_USER": "jira-user",
        "ATLASSIAN_JIRA_TOKEN": "jira-token",
        "ATLASSIAN_JIRA_VERIFY": "false",
    }
    with (
        patch.dict(os.environ, env_mock, clear=True),
        patch(
            "agent_utilities.mcp.delegated_auth.is_delegation_enabled",
            return_value=False,
        ),
    ):
        client = auth_mod.get_suite_client("JIRA")
        assert client.base_url == "https://jira.domain.net"
        assert client.username == "jira-user"
        assert client.token == "jira-token"
        assert client.verify is False


def test_get_suite_client_oidc_delegation_success():
    # Test path 1: OIDC Delegation successful
    env_mock = {
        "ATLASSIAN_AGENT_URL": "https://test.atlassian.net",
        "AUDIENCE": "test-audience",
        "DELEGATED_SCOPES": "read:jira write:jira",
    }
    with (
        patch.dict(os.environ, env_mock, clear=True),
        patch(
            "agent_utilities.mcp.delegated_auth.is_delegation_enabled",
            return_value=True,
        ),
        patch(
            "agent_utilities.mcp.delegated_auth.get_delegated_token",
            return_value="delegated-token-xyz",
        ) as mock_get_token,
        patch(
            "agent_utilities.mcp.delegated_auth.get_user_identity",
            return_value={"email": "user@example.com"},
        ),
    ):
        client = auth_mod.get_suite_client(None)
        assert client.bearer_token == "delegated-token-xyz"
        assert client.base_url == "https://test.atlassian.net"
        mock_get_token.assert_called_once_with(
            audience="test-audience", scopes="read:jira write:jira", verify=True
        )


def test_get_suite_client_oidc_delegation_failure_fallback():
    # Test path 1: OIDC Delegation raising exception, falling back to credentials
    env_mock = {
        "ATLASSIAN_AGENT_URL": "https://test.atlassian.net",
        "ATLASSIAN_AGENT_USER": "test-user@domain.com",
        "ATLASSIAN_AGENT_TOKEN": "test-token",
    }
    with (
        patch.dict(os.environ, env_mock, clear=True),
        patch(
            "agent_utilities.mcp.delegated_auth.is_delegation_enabled",
            return_value=True,
        ),
        patch(
            "agent_utilities.mcp.delegated_auth.get_delegated_token",
            side_effect=RuntimeError("OIDC Error"),
        ),
    ):
        client = auth_mod.get_suite_client(None)
        assert client.bearer_token is None
        assert client.username == "test-user@domain.com"
        assert client.token == "test-token"


def test_get_suite_client_oauth_3lo():
    # Test path 2: 3-Legged OAuth (3LO) Bearer Token
    env_mock = {
        "ATLASSIAN_AGENT_URL": "https://test.atlassian.net",
        "ATLASSIAN_OAUTH_TOKEN": "oauth-3lo-token",
    }
    with (
        patch.dict(os.environ, env_mock, clear=True),
        patch(
            "agent_utilities.mcp.delegated_auth.is_delegation_enabled",
            return_value=False,
        ),
    ):
        client = auth_mod.get_suite_client(None)
        assert client.bearer_token == "oauth-3lo-token"
        assert client.base_url == "https://test.atlassian.net"


def test_get_suite_client_bearer_token_global():
    # Test path 3: global bearer token / PAT
    env_mock = {
        "ATLASSIAN_AGENT_URL": "https://dc.example.com",
        "ATLASSIAN_BEARER_TOKEN": "pat-global-123",
    }
    with (
        patch.dict(os.environ, env_mock, clear=True),
        patch(
            "agent_utilities.mcp.delegated_auth.is_delegation_enabled",
            return_value=False,
        ),
    ):
        client = auth_mod.get_suite_client(None)
        assert client.bearer_token == "pat-global-123"
        assert client.token == ""
        assert client.session.headers["Authorization"] == "Bearer pat-global-123"


def test_get_suite_client_bearer_token_suite_overrides_global():
    # Test path 3: per-suite bearer token takes precedence over the global one
    env_mock = {
        "ATLASSIAN_AGENT_URL": "https://dc.example.com",
        "ATLASSIAN_BEARER_TOKEN": "pat-global-123",
        "ATLASSIAN_JIRA_SERVER_BEARER_TOKEN": "pat-jira-server-456",
    }
    with (
        patch.dict(os.environ, env_mock, clear=True),
        patch(
            "agent_utilities.mcp.delegated_auth.is_delegation_enabled",
            return_value=False,
        ),
    ):
        client = auth_mod.get_suite_client("JIRA_SERVER")
        assert client.bearer_token == "pat-jira-server-456"
        assert client.session.headers["Authorization"] == "Bearer pat-jira-server-456"


def test_get_base_client():
    # Test singleton client retrieval
    auth_mod._base_client = None
    with patch("atlassian_agent.auth.get_suite_client") as mock_get_suite:
        mock_client = MagicMock()
        mock_get_suite.return_value = mock_client

        c1 = auth_mod.get_base_client()
        assert c1 == mock_client
        mock_get_suite.assert_called_once_with(None)

        # Calling again returns same cached instance without invoking get_suite_client again
        c2 = auth_mod.get_base_client()
        assert c2 == mock_client
        assert mock_get_suite.call_count == 1


def test_all_client_getters():
    from typing import Any

    # Test all specific sub-client factory functions
    mock_client = MagicMock()
    with patch(
        "atlassian_agent.auth.get_suite_client", return_value=mock_client
    ) as mock_get_suite:
        c: Any = auth_mod.get_admin_cloud_client()
        mock_get_suite.assert_called_with("ADMIN_CLOUD")
        assert c is not None

        c = auth_mod.get_api_access_cloud_client()
        mock_get_suite.assert_called_with("API_ACCESS_CLOUD")
        assert c is not None

        c = auth_mod.get_confluence_cloud_client()
        mock_get_suite.assert_called_with("CONFLUENCE_CLOUD")
        assert c is not None

        c = auth_mod.get_confluence_server_client()
        mock_get_suite.assert_called_with("CONFLUENCE_SERVER")
        assert c is not None

        c = auth_mod.get_control_cloud_client()
        mock_get_suite.assert_called_with("CONTROL_CLOUD")
        assert c is not None

        c = auth_mod.get_dlp_cloud_client()
        mock_get_suite.assert_called_with("DLP_CLOUD")
        assert c is not None

        c = auth_mod.get_jira_cloud_client()
        mock_get_suite.assert_called_with("JIRA_CLOUD")
        assert c is not None

        c = auth_mod.get_jira_server_client()
        mock_get_suite.assert_called_with("JIRA_SERVER")
        assert c is not None

        c = auth_mod.get_org_cloud_client()
        mock_get_suite.assert_called_with("ORG_CLOUD")
        assert c is not None

        c = auth_mod.get_user_mgmt_cloud_client()
        mock_get_suite.assert_called_with("USER_MGMT_CLOUD")
        assert c is not None

        c = auth_mod.get_user_provisioning_cloud_client()
        mock_get_suite.assert_called_with("USER_PROVISIONING_CLOUD")
        assert c is not None
