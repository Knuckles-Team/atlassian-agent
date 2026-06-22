"""Verbose auto-wire (ECO-4.90) is actually wired into atlassian-agent.

The verbose auto-wire mechanism lives in agent-utilities, but it only emits
verbose tools for a free-form ``action: str`` condensed tool when that tool's
runtime action surface is registered via an **action provider**. These tests
prove atlassian-agent passes that provider on the live registration path — the
Wire-First guarantee — so ``MCP_TOOL_MODE=both`` exposes one
``<tool>__<action>`` verbose tool per Jira/Confluence operation, each dispatching
to the condensed handler with ``action`` preset.

CONCEPT:ECO-4.90 — verbose auto-wire enumerates dynamic (runtime) actions
"""

from __future__ import annotations

import importlib
import sys
from unittest.mock import MagicMock

import pytest
from agent_utilities.mcp.action_dispatch import public_actions
from agent_utilities.mcp.verbose_tools import _provider_tools


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
    """Build the atlassian MCP surface in ``MCP_TOOL_MODE=both`` with mocked auth.

    The action providers introspect the client *classes* (credential-free), so no
    live credentials are needed; the auth getters are still mocked so condensed
    registration succeeds.
    """
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


def test_atlassian_action_providers_cover_every_condensed_tool():
    """Every condensed action-routed tool has a backing client class declared,
    so the auto-wire never silently skips one."""
    srv = _fresh_mcp_server()

    providers = srv._condensed_action_providers()
    # All provider values are client classes (credential-free introspection).
    assert all(isinstance(v, type) for v in providers.values())
    # The two products are present and resolve to the documented action counts.
    from atlassian_agent.api.api_client_confluence_cloud import ConfluenceCloudAPI
    from atlassian_agent.api.api_client_jira_cloud import JiraCloudAPI

    assert providers["atlassian_jira_other"] is JiraCloudAPI
    assert providers["atlassian_confluence_other"] is ConfluenceCloudAPI


def test_both_mode_emits_one_verbose_tool_per_action(both_mode_mcp):
    """The headline goal: in ``both`` mode the auto-wire derives one
    ``<tool>__<action>`` verbose tool per Jira (621) and Confluence (214) action."""
    from atlassian_agent.api.api_client_confluence_cloud import ConfluenceCloudAPI
    from atlassian_agent.api.api_client_jira_cloud import JiraCloudAPI

    _srv, mcp = both_mode_mcp
    tools = _provider_tools(mcp)
    jira_actions = public_actions(JiraCloudAPI)
    conf_actions = public_actions(ConfluenceCloudAPI)

    jira_verbose = sorted(n for n in tools if n.startswith("atlassian_jira_other__"))
    conf_verbose = sorted(
        n for n in tools if n.startswith("atlassian_confluence_other__")
    )

    assert jira_verbose == sorted(f"atlassian_jira_other__{a}" for a in jira_actions)
    assert conf_verbose == sorted(
        f"atlassian_confluence_other__{a}" for a in conf_actions
    )
    # Sanity: the documented counts (621 Jira + 214 Confluence).
    assert len(jira_verbose) == len(jira_actions) == 621
    assert len(conf_verbose) == len(conf_actions) == 214


def test_verbose_tool_presets_action_and_keeps_passthrough(both_mode_mcp):
    """A derived verbose tool hides the ``action`` arg (preset to its operation),
    keeps ``params_json`` as a passthrough, and inherits the source tags +
    ``verbose`` — i.e. it routes through the original condensed handler."""
    _srv, mcp = both_mode_mcp
    tools = _provider_tools(mcp)
    name = "atlassian_jira_other__jira_cloud_add_attachment"
    assert name in tools
    tool = tools[name]

    props = (tool.parameters or {}).get("properties", {})
    assert "action" not in props  # preset + hidden by ArgTransform
    assert "params_json" in props  # passthrough preserved
    assert "verbose" in tool.tags


@pytest.mark.asyncio
async def test_verbose_tool_dispatches_with_action_preset(both_mode_mcp, monkeypatch):
    """End-to-end: calling a verbose tool invokes the condensed handler with the
    action preset to its operation name (the dispatch contract).

    The verbose tool routes through the original condensed handler (FastMCP
    ``Tool.from_tool``), so it resolves the same ``Depends`` client and calls the
    same dispatcher — we intercept the dispatcher and call the tool through an
    in-memory client so the request context (needed by ``Depends``) is active.
    """
    from fastmcp import Client

    captured: dict[str, object] = {}

    srv, mcp = both_mode_mcp

    def _capture(client, action, *args, **kwargs):
        captured["action"] = action
        return {"ok": True, "action": action}

    # Intercept the shared dispatcher so we observe the preset action without a
    # live Atlassian call.
    monkeypatch.setattr(srv, "execute_client_method", _capture)

    async with Client(mcp) as client:
        await client.call_tool(
            "atlassian_jira_other__jira_cloud_add_comment",
            {"params_json": "{}"},
        )

    # The verbose tool dispatched through the condensed handler with action preset.
    assert captured["action"] == "jira_cloud_add_comment"
