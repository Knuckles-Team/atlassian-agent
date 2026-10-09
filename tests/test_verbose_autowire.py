"""The condensed action-routed surface is the only tool surface.

agent-connector-sdk retired the verbose 1:1 ``<tool>__<action>`` surface: its
``register_tool_surface`` registers only condensed, intent-gated tools and
ignores the old ``MCP_TOOL_MODE`` / action-provider inputs. These tests pin that
contract for atlassian-agent — even with ``MCP_TOOL_MODE=both`` set, no verbose
tool is registered — and prove every Jira (621) / Confluence (214) operation is
still reachable as an ``action`` on the condensed catch-all tools, which dispatch
it through the shared action dispatcher.
"""

from __future__ import annotations

import importlib
import sys
from unittest.mock import MagicMock

import pytest
from agent_connector_sdk.mcp.action_dispatch import public_actions
from agent_connector_sdk.mcp.tool_surface import registered_tools


def _fresh_mcp_server():
    """Import a clean ``atlassian_agent.mcp_server`` module.

    A sibling coverage test mutates ``sys.modules['atlassian_agent.mcp_server']``
    (pops + re-runs it as a script), which can leave a non-module object behind;
    drop and re-import so this test always sees the real module regardless of
    suite ordering.
    """
    sys.modules.pop("atlassian_agent.mcp_server", None)
    return importlib.import_module("atlassian_agent.mcp_server")


@pytest.fixture
def both_mode_mcp(monkeypatch):
    """Build the atlassian MCP surface with the retired ``MCP_TOOL_MODE=both`` set."""
    monkeypatch.setenv("MCP_TOOL_MODE", "both")

    import atlassian_agent.auth as auth_mod

    for name in list(dir(auth_mod)):
        if name.startswith("get_") and name.endswith("_client"):
            monkeypatch.setattr(auth_mod, name, MagicMock(return_value=MagicMock()))

    srv = _fresh_mcp_server()

    # The module guards against duplicate registration with a process-global set;
    # clear it so this test registers a fresh surface.
    monkeypatch.setattr(srv, "_registered_tools", set())
    mcp, _args, _mw = srv.get_mcp_instance()
    return srv, mcp


def test_no_verbose_tools_are_registered(both_mode_mcp):
    _srv, mcp = both_mode_mcp
    tools = registered_tools(mcp)
    assert "atlassian_jira_other" in tools
    assert "atlassian_confluence_other" in tools
    assert not [name for name in tools if "__" in name]


def test_every_product_operation_is_a_condensed_action():
    from atlassian_agent.api.api_client_confluence_cloud import ConfluenceCloudAPI
    from atlassian_agent.api.api_client_jira_cloud import JiraCloudAPI

    jira_actions = public_actions(JiraCloudAPI)
    conf_actions = public_actions(ConfluenceCloudAPI)
    assert len(jira_actions) == 621
    assert len(conf_actions) == 214
    assert "jira_cloud_add_comment" in jira_actions


@pytest.mark.asyncio
async def test_condensed_tool_dispatches_the_requested_action(
    both_mode_mcp, monkeypatch
):
    """Calling the condensed catch-all tool dispatches the requested ``action``."""
    srv, mcp = both_mode_mcp
    captured: dict[str, object] = {}

    def _capture(client, action, *args, **kwargs):
        captured["action"] = action
        return {"ok": True, "action": action}

    monkeypatch.setattr(srv, "execute_client_method", _capture)

    tool = registered_tools(mcp)["atlassian_jira_other"]
    result = await tool.fn(
        action="jira_cloud_add_comment",
        params_json="{}",
        deployment="cloud",
        client_cloud=MagicMock(),
        client_server=MagicMock(),
        ctx=None,
    )

    assert captured["action"] == "jira_cloud_add_comment"
    assert result == {"ok": True, "action": "jira_cloud_add_comment"}
