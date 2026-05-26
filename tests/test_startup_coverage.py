import os
import runpy
from unittest.mock import MagicMock, patch

import pytest


# 1. Tests for atlassian_agent/__init__.py
def test_init_coverage():
    import atlassian_agent

    # Trigger __dir__
    all_dir = dir(atlassian_agent)
    assert "CORE_MODULES" in all_dir

    # Trigger _import_module_safely exception branch
    res = atlassian_agent._import_module_safely("nonexistent_module_foo_bar")
    assert res is None

    # Trigger availability flags
    assert atlassian_agent._MCP_AVAILABLE
    assert atlassian_agent._AGENT_AVAILABLE

    # Test availability flags when optional modules are not in OPTIONAL_MODULES
    with patch.dict(atlassian_agent.OPTIONAL_MODULES, {}, clear=True):
        assert not atlassian_agent._MCP_AVAILABLE
        assert not atlassian_agent._AGENT_AVAILABLE

    # Trigger unknown attribute raising AttributeError
    with pytest.raises(AttributeError, match="has no attribute 'nonexistent_attr'"):
        _ = atlassian_agent.nonexistent_attr

    # Trigger optional module getattr for variables (which aren't exposed by _expose_members)
    # This covers line 69
    assert atlassian_agent.DEFAULT_AGENT_NAME is None

    # Test _expose_members with dummy classes and functions
    class DummyClass:
        pass

    def dummy_func():
        pass

    dummy_module = MagicMock()
    dummy_module.DummyClass = DummyClass
    dummy_module.dummy_func = dummy_func
    dummy_module._private_item = lambda: None

    atlassian_agent._expose_members(dummy_module)
    assert hasattr(atlassian_agent, "DummyClass")
    assert hasattr(atlassian_agent, "dummy_func")
    assert not hasattr(atlassian_agent, "_private_item")

    # Test _eager_import_modules helper function directly to cover eager core imports
    with patch("atlassian_agent._expose_members") as mock_expose:
        with patch("importlib.import_module") as mock_import:
            mock_mod = MagicMock()
            mock_import.return_value = mock_mod

            atlassian_agent._eager_import_modules(["atlassian_agent.api"])
            mock_import.assert_called_with("atlassian_agent.api")
            mock_expose.assert_called_with(mock_mod)


# 2. Tests for atlassian_agent/agent_server.py
@pytest.fixture
def mock_agent_utilities():
    with (
        patch("agent_utilities.initialize_workspace") as mock_init,
        patch("agent_utilities.load_identity") as mock_load,
        patch("agent_utilities.build_system_prompt_from_workspace") as mock_prompt,
        patch("agent_utilities.create_agent_parser") as mock_parser,
        patch("agent_utilities.create_agent_server") as mock_server,
    ):
        # Mock identity metadata
        mock_load.return_value = {
            "name": "Mocked Atlassian Agent",
            "description": "Mocked Description",
            "content": "Mocked system prompt",
        }

        # Mock argparse args
        mock_args = MagicMock()
        mock_args.mcp_url = "http://localhost:8000"
        mock_args.mcp_config = "mock_config.json"
        mock_args.host = "localhost"
        mock_args.port = 8000
        mock_args.provider = "openai"
        mock_args.model_id = "gpt-4o"
        mock_args.base_url = "http://api.openai.com"
        mock_args.api_key = "dummy-key"
        mock_args.custom_skills_directory = "skills"
        mock_args.web = True
        mock_args.otel = True
        mock_args.otel_endpoint = "otel-endpoint"
        mock_args.otel_headers = "otel-headers"
        mock_args.otel_public_key = "pub-key"
        mock_args.otel_secret_key = "sec-key"
        mock_args.otel_protocol = "grpc"
        mock_args.debug = True

        parser_instance = MagicMock()
        parser_instance.parse_args.return_value = mock_args
        mock_parser.return_value = parser_instance

        yield {
            "init": mock_init,
            "load": mock_load,
            "prompt": mock_prompt,
            "parser": mock_parser,
            "server": mock_server,
            "args": mock_args,
        }


def test_agent_server_debug_mode(mock_agent_utilities):
    from atlassian_agent.agent_server import agent_server

    with patch("sys.argv", ["atlassian-agent"]):
        agent_server()

    mock_agent_utilities["init"].assert_called_once()
    mock_agent_utilities["load"].assert_called_once()
    mock_agent_utilities["parser"].assert_called_once()
    mock_agent_utilities["server"].assert_called_once()


def test_agent_server_non_debug_and_fallback(mock_agent_utilities):
    from atlassian_agent.agent_server import agent_server

    # Adjust mock values to trigger alternative paths
    mock_agent_utilities["args"].debug = False
    mock_agent_utilities["load"].return_value = {
        "name": "Mocked Atlassian Agent",
        "description": "Mocked Description",
        "content": None,  # Trigger fallback system prompt builder
    }
    mock_agent_utilities["prompt"].return_value = "fallback system prompt"

    # Set environment variables to test env var prioritisation
    with patch.dict(
        os.environ,
        {
            "DEFAULT_AGENT_NAME": "Env Agent Name",
            "AGENT_DESCRIPTION": "Env Agent Description",
            "AGENT_SYSTEM_PROMPT": "Env Agent Prompt",
        },
    ):
        with patch("sys.argv", ["atlassian-agent"]):
            agent_server()


def test_agent_server_direct_script_execution(mock_agent_utilities):
    with patch("sys.argv", ["atlassian-agent"]):
        runpy.run_module("atlassian_agent.agent_server", run_name="__main__")


# 3. Tests for atlassian_agent/__main__.py
def test_main_execution():
    with patch("atlassian_agent.agent_server.agent_server") as mock_server:
        with patch("sys.argv", ["atlassian-agent"]):
            runpy.run_module("atlassian_agent.__main__", run_name="__main__")
            mock_server.assert_called_once()
