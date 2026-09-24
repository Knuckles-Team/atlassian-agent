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

    # Trigger availability flags. agent_server.py is retired (EH-480 policy
    # update), so _AGENT_AVAILABLE is always False now.
    assert atlassian_agent._MCP_AVAILABLE
    assert not atlassian_agent._AGENT_AVAILABLE

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
    class MockExposedClass:
        def __init__(self):
            self.value = 1

    def mock_exposed_func():
        return True

    dummy_module = MagicMock()
    dummy_module.MockExposedClass = MockExposedClass
    dummy_module.mock_exposed_func = mock_exposed_func
    dummy_module._private_item = lambda: None

    atlassian_agent._expose_members(dummy_module)
    assert hasattr(atlassian_agent, "MockExposedClass")
    assert hasattr(atlassian_agent, "mock_exposed_func")
    assert not hasattr(atlassian_agent, "_private_item")

    # Test _eager_import_modules helper function directly to cover eager core imports
    with patch("atlassian_agent._expose_members") as mock_expose:
        with patch("importlib.import_module") as mock_import:
            mock_mod = MagicMock()
            mock_import.return_value = mock_mod

            atlassian_agent._eager_import_modules(["atlassian_agent.api"])
            mock_import.assert_called_with("atlassian_agent.api")
            mock_expose.assert_called_with(mock_mod)


# 2. Tests for atlassian_agent/__main__.py (agent_server.py retired; the
# module entry point now launches mcp_server, EH-480 policy update)
def test_main_execution():
    with patch("atlassian_agent.mcp_server.mcp_server") as mock_server:
        with patch("sys.argv", ["atlassian-mcp"]):
            runpy.run_module("atlassian_agent.__main__", run_name="__main__")
            mock_server.assert_called_once()
