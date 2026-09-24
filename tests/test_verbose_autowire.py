"""Verbose auto-wire (ECO-4.89) is actually wired into atlassian-agent.

Every Jira/Confluence action-routed tool (``atlassian_jira_*``,
``atlassian_confluence_*``) now declares a real, closed ``Literal`` action
enum (``_JIRA_ISSUE_ACTIONS``/``_CONFLUENCE_PAGE_ACTIONS`` -- the true union
across the cloud and server clients, since every one of these tools
dispatches through the identical ``execute_client_method``/``_run_dispatch``
pair against the identical clients; see ``action_literals.py``'s module
docstring). That closed static enum is what the fleet-wide verbose auto-wire
(``agent_utilities.mcp.verbose_tools.autowire_verbose_from_condensed``) reads
directly (:func:`_action_enum`) -- no per-connector "action provider"
registration is needed for these tools any more (the previous
dynamic-provider path, ECO-4.90, is now only exercised by connectors whose
action set genuinely cannot be a static enum).

These tests prove ``MCP_TOOL_MODE=both`` exposes one ``<tool>__<action>``
verbose tool per Jira/Confluence operation, for every one of the 12 tools,
each dispatching to the condensed handler with ``action`` preset.

CONCEPT:ECO-4.89 — fleet-wide verbose auto-wire from condensed action enums
"""

from __future__ import annotations

import importlib
import sys

import pytest
from agent_connector_sdk.mcp.tool_mode import registered_tools as _provider_tools

from atlassian_agent.action_literals import (
    _CONFLUENCE_PAGE_ACTIONS,
    _JIRA_ISSUE_ACTIONS,
)

#: The 8 Jira / 4 Confluence tools that all dispatch through the same
#: cloud+server client pair and therefore all share the same closed enum.
_JIRA_TOOL_NAMES = (
    "atlassian_jira_project",
    "atlassian_jira_user",
    "atlassian_jira_issue",
    "atlassian_jira_comment",
    "atlassian_jira_field",
    "atlassian_jira_screen",
    "atlassian_jira_workflow",
    "atlassian_jira_other",
)
_CONFLUENCE_TOOL_NAMES = (
    "atlassian_confluence_page",
    "atlassian_confluence_space",
    "atlassian_confluence_user",
    "atlassian_confluence_other",
)


def _literal_values(literal: object) -> tuple[str, ...]:
    import typing

    return typing.get_args(literal)


def _fresh_mcp_server():
    """Import a clean ``atlassian_agent.mcp_server`` module.

    A sibling coverage test mutates ``sys.modules['atlassian_agent.mcp_server']``
    (pops + re-runs it as a script), which can leave a non-module object behind;
    drop and re-import so this test always sees the real module regardless of
    suite ordering.
    """
    sys.modules.pop("atlassian_agent.mcp_server", None)
    return importlib.import_module("atlassian_agent.mcp_server")


@pytest.fixture(scope="module")
def both_mode_mcp():
    """Build the atlassian MCP surface in ``MCP_TOOL_MODE=both`` with mocked auth.

    Module-scoped: registering ~19k verbose tools across the 12 Jira/Confluence
    tools is real work (the whole point of this file), done once for every
    test here rather than per test. Auth getters are still mocked (matching
    the previous per-test fixture) so condensed registration succeeds without
    live credentials.
    """
    import os
    from unittest.mock import MagicMock, patch

    import atlassian_agent.auth as auth_mod

    getter_names = [
        name
        for name in dir(auth_mod)
        if name.startswith("get_") and name.endswith("_client")
    ]
    old_mode = os.environ.get("MCP_TOOL_MODE")
    os.environ["MCP_TOOL_MODE"] = "both"
    try:
        with patch.multiple(
            auth_mod,
            **{name: MagicMock(return_value=MagicMock()) for name in getter_names},
        ):
            srv = _fresh_mcp_server()
            # `_registered_tools` is a module-level global mutated in place by
            # every `register_*_tools` call; save/restore it explicitly (a
            # plain `.clear()` with no restore, unlike `monkeypatch.setattr`,
            # would permanently leak this module's real tool names into it
            # and starve a later test file's own fresh-registration checks).
            original_registered = set(srv._registered_tools)
            srv._registered_tools.clear()
            mcp, _args, _mw = srv.get_mcp_instance()
    finally:
        if old_mode is None:
            os.environ.pop("MCP_TOOL_MODE", None)
        else:
            os.environ["MCP_TOOL_MODE"] = old_mode
        srv._registered_tools.clear()
        srv._registered_tools.update(original_registered)
    return srv, mcp


def test_no_action_routed_tool_left_as_free_form_str():
    """Every Jira/Confluence/admin action-routed tool declares a real closed
    enum -- none of the 20 dispatchers is left as an unbounded ``action: str``
    (EH-215/EH-217)."""
    srv = _fresh_mcp_server()
    import inspect

    for name in _JIRA_TOOL_NAMES + _CONFLUENCE_TOOL_NAMES:
        register_fn = getattr(srv, f"register_{name.removeprefix('atlassian_')}_tools")
        source = inspect.getsource(register_fn)
        assert "action: str" not in source, f"{name} still declares action: str"


@pytest.mark.parametrize("tool_name", _JIRA_TOOL_NAMES)
def test_jira_tool_action_enum_matches_closed_union(both_mode_mcp, tool_name):
    """Every Jira tool's declared ``action`` enum is exactly the real closed
    union (1933 actions) -- not a narrower or invented set."""
    _srv, mcp = both_mode_mcp
    tools = _provider_tools(mcp)
    tool = tools[tool_name]
    props = (tool.parameters or {}).get("properties", {})
    assert set(props["action"]["enum"]) == set(_literal_values(_JIRA_ISSUE_ACTIONS))


@pytest.mark.parametrize("tool_name", _CONFLUENCE_TOOL_NAMES)
def test_confluence_tool_action_enum_matches_closed_union(both_mode_mcp, tool_name):
    """Every Confluence tool's declared ``action`` enum is exactly the real
    closed union (731 actions)."""
    _srv, mcp = both_mode_mcp
    tools = _provider_tools(mcp)
    tool = tools[tool_name]
    props = (tool.parameters or {}).get("properties", {})
    assert set(props["action"]["enum"]) == set(
        _literal_values(_CONFLUENCE_PAGE_ACTIONS)
    )


@pytest.mark.parametrize("tool_name", _JIRA_TOOL_NAMES)
def test_both_mode_emits_one_verbose_jira_tool_per_action(both_mode_mcp, tool_name):
    """In ``both`` mode the auto-wire derives one ``<tool>__<action>`` verbose
    tool per Jira action, for every one of the 8 Jira tools (1933 each)."""
    _srv, mcp = both_mode_mcp
    tools = _provider_tools(mcp)
    jira_actions = _literal_values(_JIRA_ISSUE_ACTIONS)

    verbose = sorted(n for n in tools if n.startswith(f"{tool_name}__"))
    assert verbose == sorted(f"{tool_name}__{a}" for a in jira_actions)
    assert len(verbose) == len(jira_actions) == 1933


@pytest.mark.parametrize("tool_name", _CONFLUENCE_TOOL_NAMES)
def test_both_mode_emits_one_verbose_confluence_tool_per_action(
    both_mode_mcp, tool_name
):
    """In ``both`` mode the auto-wire derives one ``<tool>__<action>`` verbose
    tool per Confluence action, for every one of the 4 Confluence tools
    (731 each)."""
    _srv, mcp = both_mode_mcp
    tools = _provider_tools(mcp)
    conf_actions = _literal_values(_CONFLUENCE_PAGE_ACTIONS)

    verbose = sorted(n for n in tools if n.startswith(f"{tool_name}__"))
    assert verbose == sorted(f"{tool_name}__{a}" for a in conf_actions)
    assert len(verbose) == len(conf_actions) == 731


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
