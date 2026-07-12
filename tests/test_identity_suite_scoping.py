"""Identity-scoped Atlassian suite auto-load (CONCEPT:AU-OS.identity.identity-scoped-resource-autoload).

A ``suite_prefix`` the caller's identity is not entitled to is denied before
any credential resolution happens; an entitled or omitted suite_prefix behaves
exactly as before. Tests the enforcement logic with the entitlement source
mocked (the resolver itself is tested in agent-utilities).
"""

import importlib
import os
from unittest.mock import patch

import pytest

import atlassian_agent.auth as auth_mod


@pytest.fixture(autouse=True, scope="module")
def restore_real_auth():
    """conftest.py replaces every ``get_*_client`` with a MagicMock at import
    time; reload the module so these tests exercise the real ``get_suite_client``
    entitlement gate (mirrors ``tests/test_auth.py``)."""
    original_mocks = {}
    for name in list(dir(auth_mod)):
        if name.startswith("get_") and name.endswith("_client"):
            original_mocks[name] = getattr(auth_mod, name)

    importlib.reload(auth_mod)

    yield

    for name, mock_func in original_mocks.items():
        setattr(auth_mod, name, mock_func)


def _entitle(monkeypatch, entitled):
    monkeypatch.setattr(
        auth_mod,
        "_entitled",
        lambda namespace, names: [n for n in names if n in entitled],
    )


def test_named_suite_not_entitled_is_denied(monkeypatch):
    _entitle(monkeypatch, set())
    with pytest.raises(PermissionError):
        auth_mod.get_suite_client("JIRA_CLOUD")


def test_named_entitled_suite_allowed(monkeypatch):
    _entitle(monkeypatch, {"JIRA_CLOUD"})
    env_mock = {
        "ATLASSIAN_JIRA_CLOUD_URL": "https://jira.domain.net",
        "ATLASSIAN_JIRA_CLOUD_USER": "jira-user",
        "ATLASSIAN_JIRA_CLOUD_TOKEN": "jira-token",
    }
    with (
        patch.dict(os.environ, env_mock, clear=True),
        patch(
            "agent_utilities.mcp.delegated_auth.is_delegation_enabled",
            return_value=False,
        ),
    ):
        client = auth_mod.get_suite_client("JIRA_CLOUD")
        assert client.base_url == "https://jira.domain.net"


def test_no_suite_prefix_skips_entitlement_check(monkeypatch):
    """The shared fallback (suite_prefix=None) is never gated — no resource to deny."""
    _entitle(monkeypatch, set())
    env_mock = {
        "ATLASSIAN_AGENT_URL": "https://test.atlassian.net",
        "ATLASSIAN_AGENT_USER": "test-user@domain.com",
        "ATLASSIAN_AGENT_TOKEN": "test-token",
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


def test_missing_resolver_degrades_to_allow(monkeypatch):
    """A broken/absent import of the shared resolver fails open (back-compat)."""
    import builtins

    real_import = builtins.__import__

    def _blocked_import(name, *args, **kwargs):
        if name == "agent_utilities.security.entitlements":
            raise ImportError("simulated: resolver not available")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", _blocked_import)
    assert auth_mod._entitled("atlassian", ["JIRA_CLOUD"]) == ["JIRA_CLOUD"]
