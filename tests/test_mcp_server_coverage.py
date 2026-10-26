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
from agent_connector_sdk.mcp import server as server_factory

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

import pytest

import atlassian_agent.mcp_server
from atlassian_agent.mcp_server import (
    get_mcp_instance,
    mcp_server,
)

# The factory patch only has to cover the import above. Left in place it would hide
# this package from the SDK's caller lookup for every later test in the session.
server_factory.create_mcp_server = original_create_mcp_server


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
    with (
        patch(
            "atlassian_agent.mcp_server.create_mcp_server",
            return_value=(None, mock_mcp, [mock_mw]),
        ),
        patch("atlassian_agent.mcp_server.register_tool_surface"),
    ):
        get_mcp_instance()
        mock_mcp.add_middleware.assert_called_with(mock_mw)


@pytest.mark.anyio
async def test_confluence_page_tool_direct():
    sys.modules["atlassian_agent.mcp_server"]._registered_tools.clear()

    mcp = get_mcp_instance()[0]
    tools = {t.name: t for t in await mcp.list_tools()}

    # One tool per operation; Jira and Confluence tools pick Cloud or Server
    # from configuration, so there is no deployment routing tool.
    assert "confluence_get_pages" in tools
    assert not any(name.startswith("confluence_server_") for name in tools)
    assert "atlassian_confluence_page" not in tools
    assert "action" not in tools["confluence_get_pages"].parameters.get(
        "properties", {}
    )
    assert tools["confluence_get_pages"].annotations.readOnlyHint is True


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
