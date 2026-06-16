"""Action-discovery behavior for the atlassian-agent action-routed tools.

Verifies the shared ``agent_utilities.mcp_utilities`` dispatch wiring:
``list_actions`` discovery, plural->singular aliasing, and a rich
did-you-mean error pointing back at ``list_actions``.
"""

from unittest.mock import MagicMock

import pytest

from atlassian_agent.mcp_server import execute_client_method


def _client():
    client = MagicMock()
    # Restrict the client's public surface to a couple of prefixed methods so
    # discovery is bounded and deterministic.
    client.mock_add_spec(["jira_cloud_get_issue", "jira_cloud_get_comment"])
    return client


def test_list_actions_returns_names():
    client = _client()
    res = execute_client_method(
        client, "list_actions", "jira_cloud_", "jira_server_", "cloud", {}
    )
    assert isinstance(res, dict)
    assert "jira_cloud_get_issue" in res["actions"]
    assert res["service"] == "atlassian-agent (cloud)"


def test_bogus_action_raises_with_list_actions_hint():
    client = _client()
    with pytest.raises(ValueError) as exc:
        execute_client_method(
            client,
            "definitely_not_a_real_action",
            "jira_cloud_",
            "jira_server_",
            "cloud",
            {},
        )
    assert "list_actions" in str(exc.value)


def test_unprefixed_alias_resolves():
    client = _client()
    execute_client_method(
        client, "get_issue", "jira_cloud_", "jira_server_", "cloud", {"id": 1}
    )
    client.jira_cloud_get_issue.assert_called_once_with(id=1)
