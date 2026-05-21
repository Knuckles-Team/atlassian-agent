from unittest.mock import Mock

import pytest

from atlassian_agent.mcp_server import register_confluence_page_tools


@pytest.fixture
def mock_mcp():
    mcp = Mock()
    mcp.tool = Mock(return_value=lambda f: f)
    return mcp


def test_register_confluence_page_tools(mock_mcp):
    register_confluence_page_tools(mock_mcp)
    mock_mcp.tool.assert_called()
