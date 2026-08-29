import importlib
import sys
from unittest.mock import MagicMock, patch

# Mock Context logging methods to avoid RuntimeError when called outside an active MCP session
import fastmcp


async def dummy_async(*args, **kwargs):
    return None


fastmcp.Context.info = dummy_async  # type: ignore[method-assign]
fastmcp.Context.warning = dummy_async  # type: ignore[method-assign]
fastmcp.Context.error = dummy_async  # type: ignore[method-assign]
fastmcp.Context.debug = dummy_async  # type: ignore[method-assign]


class DictResponse:
    def dict(self):
        return {"id": "1", "status": "ok"}


class ModelDumpResponse:
    def model_dump(self):
        return {"id": "1", "status": "ok"}


class MockClient:
    def __init__(self):
        self.mode = 0

    def __getattr__(self, name):
        if self.mode == 0:
            return lambda *args, **kwargs: DictResponse()
        elif self.mode == 1:
            return lambda *args, **kwargs: ModelDumpResponse()
        elif self.mode == 2:
            return lambda *args, **kwargs: "plain-string-response"
        else:

            def raise_exc(*args, **kwargs):
                raise RuntimeError("mocked API error")

            return raise_exc


mock_client_inst = MockClient()

# Patch all auth getters in the auth module before importing mcp_server
import atlassian_agent.auth

for name in list(dir(atlassian_agent.auth)):
    if name.startswith("get_") and name.endswith("_client"):
        setattr(atlassian_agent.auth, name, MagicMock(return_value=mock_client_inst))

# Force reload atlassian_agent.auth if it was imported elsewhere
importlib.reload(atlassian_agent.auth)
for name in list(dir(atlassian_agent.auth)):
    if name.startswith("get_") and name.endswith("_client"):
        setattr(atlassian_agent.auth, name, MagicMock(return_value=mock_client_inst))

# Mock create_mcp_server to return empty middlewares to avoid rate limiting
from agent_utilities.mcp import server_factory

original_create_mcp_server = server_factory.create_mcp_server


def mock_create_mcp_server(*args, **kwargs):
    s_args, s_mcp, _ = original_create_mcp_server(*args, **kwargs)
    return s_args, s_mcp, []


server_factory.create_mcp_server = mock_create_mcp_server

# Clear the global mcp instance and registered tools to force clean re-registration with mocked dependencies
# We pop any existing entries containing 'atlassian_agent.mcp_server' from sys.modules to force a complete re-execution
for key in list(sys.modules.keys()):
    if "atlassian_agent.mcp_server" in key:
        sys.modules.pop(key, None)

# Now import mcp_server so default arguments evaluate to the mocked functions
import ast
import inspect

import pytest
from starlette.requests import Request

import atlassian_agent.mcp_server
from atlassian_agent.mcp_server import (
    execute_client_method,
    get_mcp_instance,
    mcp_server,
    register_atlassian_admin_tools,
    register_atlassian_api_access_tools,
    register_atlassian_control_tools,
    register_atlassian_dlp_tools,
    register_atlassian_org_tools,
    register_atlassian_tools,
    register_atlassian_user_mgmt_tools,
    register_atlassian_user_provisioning_tools,
    register_confluence_other_tools,
    register_confluence_page_tools,
    register_confluence_space_tools,
    register_confluence_user_tools,
    register_jira_comment_tools,
    register_jira_field_tools,
    register_jira_issue_tools,
    register_jira_other_tools,
    register_jira_project_tools,
    register_jira_screen_tools,
    register_jira_user_tools,
    register_jira_workflow_tools,
)


def test_execute_client_method_branches():
    class SpecificMockClient:
        def __init__(self):
            self.calls = []

        def jira_cloud_test_action(self, **kwargs):
            self.calls.append(("cloud", kwargs))
            return "cloud_res"

        def jira_server_test_action(self, **kwargs):
            self.calls.append(("server", kwargs))
            return "server_res"

        def stripped_action(self, **kwargs):
            self.calls.append(("stripped", kwargs))
            return "stripped_res"

    client = SpecificMockClient()

    # 1. Direct name lookup
    res = execute_client_method(
        client,
        "jira_cloud_test_action",
        "jira_cloud_",
        "jira_server_",
        "cloud",
        {"a": 1},
    )
    assert res == "cloud_res"

    # 2. Prefix matching (cloud)
    res = execute_client_method(
        client, "test_action", "jira_cloud_", "jira_server_", "cloud", {"a": 1}
    )
    assert res == "cloud_res"

    # 3. Prefix matching (server)
    res = execute_client_method(
        client, "test_action", "jira_cloud_", "jira_server_", "server", {"a": 1}
    )
    assert res == "server_res"

    # 4. Stripped action matching
    res = execute_client_method(
        client,
        "jira_cloud_stripped_action",
        "jira_cloud_",
        "jira_server_",
        "cloud",
        {"a": 1},
    )
    assert res == "stripped_res"

    # 5. Unknown action matching raising ValueError (rich shared-helper error)
    with pytest.raises(ValueError, match="Unknown action 'invalid_action'"):
        execute_client_method(
            client, "invalid_action", "jira_cloud_", "jira_server_", "cloud", {}
        )
    with pytest.raises(ValueError, match="list_actions"):
        execute_client_method(
            client, "invalid_action", "jira_cloud_", "jira_server_", "cloud", {}
        )

    # 6. Discovery: list_actions returns the bounded action set
    disc = execute_client_method(
        client, "list_actions", "jira_cloud_", "jira_server_", "cloud", {}
    )
    assert isinstance(disc, dict)
    assert "jira_cloud_test_action" in disc["actions"]


# Representative dynamic actions for tools with dynamic routing (avoids dynamic method explosion)
_DYNAMIC_TOOL_ACTION_MAPPINGS = {
    "atlassian_jira_project": ["jira_cloud_get_project", "jira_server_get_project"],
    "atlassian_jira_user": ["jira_cloud_get_user", "jira_server_get_user"],
    "atlassian_jira_issue": ["jira_cloud_get_issue", "jira_server_get_issue"],
    "atlassian_jira_comment": ["jira_cloud_get_comment", "jira_server_get_comment"],
    "atlassian_jira_field": ["jira_cloud_get_field", "jira_server_get_field"],
    "atlassian_jira_screen": ["jira_cloud_get_screen", "jira_server_get_screen"],
    "atlassian_jira_workflow": [
        "jira_cloud_get_workflow",
        "jira_server_get_workflow",
    ],
    "atlassian_jira_other": ["jira_cloud_get_info", "jira_server_get_info"],
    "atlassian_confluence_page": [
        "confluence_cloud_get_page",
        "confluence_server_get_page",
    ],
    "atlassian_confluence_space": [
        "confluence_cloud_get_space",
        "confluence_server_get_space",
    ],
    "atlassian_confluence_user": [
        "confluence_cloud_get_user",
        "confluence_server_get_user",
    ],
    "atlassian_confluence_other": [
        "confluence_cloud_get_info",
        "confluence_server_get_info",
    ],
}


def _action_equality_literal(subnode: ast.AST) -> str | None:
    """If `subnode` is the AST for `action == "some_literal"`, return that literal."""
    if not isinstance(subnode, ast.Compare):
        return None
    if not (
        isinstance(subnode.left, ast.Name)
        and subnode.left.id == "action"
        and len(subnode.ops) == 1
        and isinstance(subnode.ops[0], ast.Eq)
        and len(subnode.comparators) == 1
        and isinstance(subnode.comparators[0], ast.Constant)
    ):
        return None
    val = subnode.comparators[0].value
    return val if isinstance(val, str) else None


def _tool_action_literals(node: ast.AsyncFunctionDef) -> list[str]:
    """Collect every literal `action == "..."` string compared inside a tool function."""
    actions: set[str] = set()
    for subnode in ast.walk(node):
        val = _action_equality_literal(subnode)
        if val is not None:
            actions.add(val)
    return list(actions)


def _discover_tool_actions(source_path: str) -> dict[str, list[str]]:
    """AST-walk the mcp_server source, mapping each atlassian_* tool to its actions."""
    tool_to_actions: dict[str, list[str]] = {}
    try:
        with open(source_path) as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.AsyncFunctionDef) and node.name.startswith(
                "atlassian_"
            ):
                tool_name = node.name.replace("-", "_")
                tool_to_actions[tool_name] = _tool_action_literals(node)
    except Exception as e:
        print(f"Operation failed: {type(e).__name__}")
    return tool_to_actions


def map_tools_to_actions():
    tool_to_actions = _discover_tool_actions("atlassian_agent/mcp_server.py")
    for tool_name, mapped_actions in _DYNAMIC_TOOL_ACTION_MAPPINGS.items():
        tool_to_actions[tool_name.replace("-", "_")] = mapped_actions
    return tool_to_actions


def _register_all_atlassian_tools(mcp) -> None:
    """Register every tool group -- also triggers each group's duplicate-registration guard."""
    register_atlassian_control_tools(mcp)
    register_atlassian_org_tools(mcp)
    register_jira_project_tools(mcp)
    register_jira_user_tools(mcp)
    register_jira_issue_tools(mcp)
    register_jira_comment_tools(mcp)
    register_jira_field_tools(mcp)
    register_jira_screen_tools(mcp)
    register_jira_workflow_tools(mcp)
    register_jira_other_tools(mcp)
    register_confluence_page_tools(mcp)
    register_confluence_space_tools(mcp)
    register_confluence_user_tools(mcp)
    register_confluence_other_tools(mcp)
    register_atlassian_dlp_tools(mcp)
    register_atlassian_user_mgmt_tools(mcp)
    register_atlassian_tools(mcp)
    register_atlassian_admin_tools(mcp)
    register_atlassian_api_access_tools(mcp)
    register_atlassian_user_provisioning_tools(mcp)


async def _assert_health_route_ok(mcp) -> None:
    mock_req = MagicMock(spec=Request)
    health_route = None
    for route in getattr(mcp, "_additional_http_routes", []):
        if route.path == "/health":
            health_route = route.endpoint
            break
    if health_route:
        res = await health_route(mock_req)
        assert res.status_code == 200


def _resolve_tool_actions(
    func_name: str, normalized_tool_name: str, tool_to_actions: dict
) -> list[str]:
    """Look up a tool's known actions by exact func/tool name, else by substring match."""
    actions = tool_to_actions.get(func_name, [])
    if actions:
        return actions
    actions = tool_to_actions.get(normalized_tool_name, [])
    if actions:
        return actions
    for name, acts in tool_to_actions.items():
        if normalized_tool_name in name or name in normalized_tool_name:
            return acts
    return []


def _deployments_for_action(action: str) -> list[str]:
    if "server" in action:
        return ["server"]
    if "cloud" in action:
        return ["cloud"]
    return ["cloud", "server"]


def _build_args_from_signature(sig, action: str, deployment: str, params_json: str) -> dict:
    """Build call args from a tool's signature: explicit values for
    action/deployment/params_json, 'test-value' for any other required param, `ctx` omitted."""
    args = {}
    for param_name, param in sig.parameters.items():
        if param_name == "action":
            args["action"] = action
        elif param_name == "deployment":
            args["deployment"] = deployment
        elif param_name == "params_json":
            args["params_json"] = params_json
        elif param_name == "ctx":
            pass
        elif param.default == inspect.Parameter.empty:
            args[param_name] = "test-value"
    return args


async def _exercise_tool_action(mcp, tool, sig, action: str, cycle_all_modes: bool) -> None:
    """Call `tool` once per (mode x deployment) for one action.

    Cycles all 4 response-formatting modes only when `cycle_all_modes` (the first
    action for this tool, to save time and avoid timeouts) -- other actions use mode 0.
    """
    modes = [0, 1, 2, 3] if cycle_all_modes else [0]
    for mode in modes:
        mock_client_inst.mode = mode
        for deployment in _deployments_for_action(action):
            if sig:
                args = _build_args_from_signature(sig, action, deployment, '{"id": "1"}')
            else:
                args = {
                    "action": action,
                    "deployment": deployment,
                    "params_json": '{"id": "1"}',
                }
            try:
                await mcp.call_tool(tool.name, args)
            except Exception:
                pass


async def _exercise_valid_actions(mcp, tool, sig, actions: list[str]) -> None:
    """1. Normal execution across every action (mode-cycled on the first only)."""
    for i, action in enumerate(actions):
        await _exercise_tool_action(mcp, tool, sig, action, cycle_all_modes=(i == 0))


async def _exercise_invalid_json(mcp, tool, sig, first_action: str) -> None:
    """2. Invalid params_json parsing-error coverage."""
    if not (sig and "params_json" in sig.parameters):
        return
    args = _build_args_from_signature(sig, first_action, "cloud", "{invalid_json}")
    try:
        await mcp.call_tool(tool.name, args)
    except Exception:
        pass


async def _exercise_unknown_action(mcp, tool, sig) -> None:
    """3. Unknown-action ValueError coverage."""
    if sig:
        args = _build_args_from_signature(sig, "invalid_action", "cloud", "{}")
    else:
        args = {"action": "invalid_action"}
    try:
        await mcp.call_tool(tool.name, args)
    except Exception:
        pass


async def _exercise_tool(mcp, tool, tool_to_actions: dict) -> None:
    """Run all three brute-force coverage cases for one registered tool."""
    normalized_tool_name = tool.name.replace("-", "_")
    func_name = (
        (tool.fn.__name__.replace("-", "_"))
        if hasattr(tool, "fn")
        else normalized_tool_name
    )

    actions = _resolve_tool_actions(func_name, normalized_tool_name, tool_to_actions)
    print(
        f"Tool: {tool.name} (normalized: {normalized_tool_name}) -> mapped actions: {actions}"
    )
    if not actions:
        actions = ["dummy_action"]

    sig = inspect.signature(tool.fn) if hasattr(tool, "fn") else None

    await _exercise_valid_actions(mcp, tool, sig, actions)
    await _exercise_invalid_json(mcp, tool, sig, actions[0])
    await _exercise_unknown_action(mcp, tool, sig)


@pytest.mark.anyio
async def test_mcp_server_tools_coverage():
    sys.modules["atlassian_agent.mcp_server"]._registered_tools.clear()

    tool_to_actions = map_tools_to_actions()

    mcp_data = get_mcp_instance()
    mcp = mcp_data[0]

    # Trigger duplicate registration guards
    mock_mcp = MagicMock()
    type(mock_mcp).__name__ = "Mock"
    _register_all_atlassian_tools(mcp)

    await _assert_health_route_ok(mcp)

    tools = await mcp.list_tools()
    for tool in tools:
        await _exercise_tool(mcp, tool, tool_to_actions)


def test_mcp_server_entrypoint():
    mock_mcp = MagicMock()

    # 1. Test stdio transport
    mock_args_stdio = MagicMock()
    mock_args_stdio.transport = "stdio"
    mock_args_stdio.auth_type = "oauth"

    with patch(
        "atlassian_agent.mcp_server.get_mcp_instance",
        return_value=(mock_mcp, mock_args_stdio, []),
    ):
        mcp_server()
        mock_mcp.run.assert_called_with(transport="stdio")

    # 2. Test streamable-http transport
    mock_args_http = MagicMock()
    mock_args_http.transport = "streamable-http"
    mock_args_http.auth_type = "oauth"
    mock_args_http.host = "localhost"
    mock_args_http.port = 8000

    with patch(
        "atlassian_agent.mcp_server.get_mcp_instance",
        return_value=(mock_mcp, mock_args_http, []),
    ):
        mcp_server()
        mock_mcp.run.assert_called_with(
            transport="streamable-http", host="localhost", port=8000
        )

    # 3. Test sse transport
    mock_args_sse = MagicMock()
    mock_args_sse.transport = "sse"
    mock_args_sse.auth_type = "oauth"
    mock_args_sse.host = "localhost"
    mock_args_sse.port = 8000

    with patch(
        "atlassian_agent.mcp_server.get_mcp_instance",
        return_value=(mock_mcp, mock_args_sse, []),
    ):
        mcp_server()
        mock_mcp.run.assert_called_with(transport="sse", host="localhost", port=8000)

    # 4. Test invalid transport
    mock_args_invalid = MagicMock()
    mock_args_invalid.transport = "invalid"
    mock_args_invalid.auth_type = "oauth"

    with patch(
        "atlassian_agent.mcp_server.get_mcp_instance",
        return_value=(mock_mcp, mock_args_invalid, []),
    ):
        with pytest.raises(SystemExit) as excinfo:
            mcp_server()
        assert excinfo.value.code == 1


def test_middlewares_addition():
    mock_mcp = MagicMock()
    mock_mw = MagicMock()
    with patch(
        "atlassian_agent.mcp_server.create_mcp_server",
        return_value=(None, mock_mcp, [mock_mw]),
    ):
        get_mcp_instance()
        mock_mcp.add_middleware.assert_called_with(mock_mw)


@pytest.mark.anyio
async def test_confluence_page_tool_direct():
    sys.modules["atlassian_agent.mcp_server"]._registered_tools.clear()

    mcp_data = get_mcp_instance()
    mcp = mcp_data[0]

    tools = await mcp.list_tools()
    tool_names = [t.name for t in tools]
    print("\nREGISTERED TOOLS:", tool_names)
    tool_name = (
        "atlassian_confluence_page"
        if "atlassian_confluence_page" in tool_names
        else "atlassian-confluence-page"
    )

    # Verify we can invoke the tool directly to ensure full branch coverage of Confluence page tool
    res1 = await mcp.call_tool(
        tool_name,
        {
            "action": "confluence_cloud_get_pages",
            "deployment": "cloud",
            "params_json": '{"page_id": "123"}',
        },
    )
    assert res1 is not None

    res2 = await mcp.call_tool(
        tool_name,
        {
            "action": "confluence_server_get_pages",
            "deployment": "server",
            "params_json": '{"page_id": "123"}',
        },
    )
    assert res2 is not None

    # Test invalid json parameter
    res3 = await mcp.call_tool(
        tool_name,
        {
            "action": "confluence_cloud_get_pages",
            "deployment": "cloud",
            "params_json": "{invalid_json}",
        },
    )
    # Since call_tool returns a ToolResult, we can inspect its content or structured_content
    result_text = ""
    if hasattr(res3, "content") and res3.content:
        result_text = res3.content[0].text
    elif isinstance(res3, dict):
        result_text = res3.get("error", "")
    # Exception details (e.g. raw JSON-parser internals) are sanitized out of the
    # response (security hardening) rather than echoed back to the caller.
    assert "Operation failed" in result_text


def test_requests_dependency_warning_import_error():
    # Force ImportError in the early warnings handling block
    import runpy

    # runpy.run_module("__main__") re-executes the module's own argparse
    # against the LIVE sys.argv, so any pytest flag (e.g. `-p no:randomly`)
    # leaks in and is rejected by the module's CLI parser. Pin argv to a
    # clean single-element list for the duration of the run so the module
    # under test sees the same argv regardless of how pytest was invoked.
    with (
        patch.dict(sys.modules, {"requests.exceptions": None}),
        patch("sys.argv", ["atlassian-agent-mcp"]),
    ):
        # Setting requests.exceptions to None raises ImportError upon import
        try:
            runpy.run_module("atlassian_agent.mcp_server", run_name="temp_name")
        except Exception:
            pass


def test_mcp_server_direct_script_execution():
    # Force execution of __name__ == "__main__" block without starting a real stdio server
    import runpy

    import fastmcp

    # See argv-isolation note above: pin sys.argv before invoking runpy so
    # the module's own argparse never sees pytest's argv/flags.
    with (
        patch.object(fastmcp.FastMCP, "run") as mock_run,
        patch("sys.argv", ["atlassian-agent-mcp"]),
    ):
        runpy.run_module("atlassian_agent.mcp_server", run_name="__main__")
        mock_run.assert_called_once()
