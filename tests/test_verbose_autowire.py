"""One typed tool per Atlassian operation; Jira and Confluence pick Cloud or Server.

Jira and Confluence operations are served as ``jira_<operation>`` and
``confluence_<operation>``. The tool list is the configured deployment's
operations (``ATLASSIAN_JIRA_DEPLOYMENT`` / ``ATLASSIAN_CONFLUENCE_DEPLOYMENT``),
and each call reads the deployment again and calls that client. No action-routed
deployment tool remains.
"""

from __future__ import annotations

import importlib
import sys
from unittest.mock import MagicMock

import pytest
from scion_sdk.mcp.tool_surface import registered_tools

from atlassian_agent import deployment_tools


def _surface(monkeypatch, **env: str):
    for key in ("ATLASSIAN_JIRA_DEPLOYMENT", "ATLASSIAN_CONFLUENCE_DEPLOYMENT"):
        monkeypatch.delenv(key, raising=False)
    for key, value in env.items():
        monkeypatch.setenv(key, value)
    sys.modules.pop("atlassian_agent.mcp_server", None)
    srv = importlib.import_module("atlassian_agent.mcp_server")
    mcp, _args, _mw = srv.get_mcp_instance()
    return registered_tools(mcp)


def test_cloud_is_the_default_and_no_router_remains(monkeypatch):
    tools = _surface(monkeypatch)
    jira = [n for n in tools if n.startswith("jira_")]
    confluence = [n for n in tools if n.startswith("confluence_")]
    assert len(jira) == len(deployment_tools.operations("jira", "cloud")) == 621
    assert (
        len(confluence)
        == len(deployment_tools.operations("confluence", "cloud"))
        == 214
    )
    assert not [n for n in tools if n.startswith(("jira_cloud_", "jira_server_"))]
    assert not [n for n in tools if n.startswith(("atlassian_jira_", "atlassian_conf"))]
    assert not [n for n in tools if "__" in n]
    comment = tools["jira_add_comment"]
    assert "action" not in comment.parameters["properties"]
    assert comment.annotations.readOnlyHint is False
    assert tools["confluence_get_pages"].annotations.readOnlyHint is True


def test_server_configuration_serves_server_operations(monkeypatch):
    tools = _surface(
        monkeypatch,
        ATLASSIAN_JIRA_DEPLOYMENT="server",
        ATLASSIAN_CONFLUENCE_DEPLOYMENT="server",
    )
    assert sum(n.startswith("jira_") for n in tools) == 435
    assert sum(n.startswith("confluence_") for n in tools) == 154
    assert "jira_search_1" in tools


def test_call_uses_the_configured_deployment(monkeypatch):
    calls: list[tuple[str, dict]] = []
    cloud, server = MagicMock(), MagicMock()
    cloud.jira_cloud_add_comment.side_effect = lambda **kw: calls.append(("cloud", kw))
    server.jira_server_add_comment.side_effect = lambda **kw: calls.append(
        ("server", kw)
    )
    import atlassian_agent.auth as auth

    monkeypatch.setattr(auth, "get_jira_cloud_client", lambda: cloud)
    monkeypatch.setattr(auth, "get_jira_server_client", lambda: server)
    client = deployment_tools.facade_class("jira", "cloud")()

    monkeypatch.setenv("ATLASSIAN_JIRA_DEPLOYMENT", "cloud")
    client.add_comment(issue_id_or_key="P-1")
    monkeypatch.setenv("ATLASSIAN_JIRA_DEPLOYMENT", "server")
    client.add_comment(issue_id_or_key="P-1")
    assert calls == [
        ("cloud", {"issue_id_or_key": "P-1"}),
        ("server", {"issue_id_or_key": "P-1"}),
    ]


def test_operation_missing_on_the_configured_deployment_is_refused(monkeypatch):
    import atlassian_agent.auth as auth

    monkeypatch.setattr(auth, "get_jira_server_client", lambda: object())
    monkeypatch.setenv("ATLASSIAN_JIRA_DEPLOYMENT", "server")
    client = deployment_tools.facade_class("jira", "cloud")()
    with pytest.raises(deployment_tools.DeploymentUnavailableError):
        client.get_banner()


def test_bad_deployment_value_is_rejected(monkeypatch):
    monkeypatch.setenv("ATLASSIAN_JIRA_DEPLOYMENT", "datacenter")
    with pytest.raises(ValueError, match="cloud' or 'server"):
        deployment_tools.configured_deployment("jira")
