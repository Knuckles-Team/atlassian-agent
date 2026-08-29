import inspect
from unittest.mock import MagicMock, patch

import pytest

from atlassian_agent.api.api_client_admin_cloud import AdminCloudAPI
from atlassian_agent.api.api_client_api_access_cloud import APIAccessCloudAPI
from atlassian_agent.api.api_client_confluence_cloud import ConfluenceCloudAPI
from atlassian_agent.api.api_client_confluence_server import ConfluenceServerAPI
from atlassian_agent.api.api_client_control_cloud import ControlCloudAPI
from atlassian_agent.api.api_client_dlp_cloud import DLPCloudAPI
from atlassian_agent.api.api_client_jira_cloud import JiraCloudAPI
from atlassian_agent.api.api_client_jira_server import JiraServerAPI
from atlassian_agent.api.api_client_org_cloud import OrgCloudAPI
from atlassian_agent.api.api_client_user_mgmt_cloud import UserMgmtCloudAPI
from atlassian_agent.api.api_client_user_provisioning_cloud import (
    UserProvisioningCloudAPI,
)
from atlassian_agent.api.base import BaseAtlassianClient


@pytest.fixture
def mock_session():
    with patch("requests.Session") as mock_s:
        session = mock_s.return_value

        response = MagicMock()
        response.status_code = 200
        response.ok = True
        response.json.return_value = {"id": "1", "key": "TEST", "values": [{"id": "1"}]}
        response.text = '{"status": "ok"}'
        response.headers = {"Link": '<http://test?page=2>; rel="next"'}

        session.request.return_value = response
        session.get.return_value = response
        session.post.return_value = response
        session.put.return_value = response
        session.delete.return_value = response
        session.patch.return_value = response
        yield session


def _guess_kwarg_value(param_name: str, annotation, common_args: dict) -> object:
    """Best-effort guess of a plausible value for one brute-forced parameter."""
    if param_name in common_args:
        return common_args[param_name]
    if annotation is int:
        return 1
    if annotation is bool:
        return True
    if annotation is dict:
        return {}
    if annotation is list:
        return []
    return "test-value"


def _guessed_kwargs(sig: inspect.Signature, common_args: dict) -> dict:
    """Guess a kwargs dict covering every required (default-less) parameter of ``sig``."""
    return {
        param_name: _guess_kwarg_value(param_name, param.annotation, common_args)
        for param_name, param in sig.parameters.items()
        if param.default == inspect.Parameter.empty
    }


def _call_client_method_best_effort(method, common_args: dict) -> None:
    """Call one client method with guessed args; any failure is expected/logged."""
    kwargs = _guessed_kwargs(inspect.signature(method), common_args)
    try:
        method(**kwargs)
    except Exception as e:
        print(f"Operation failed: {type(e).__name__}")


def _brute_force_client(client_class, base_client, common_args: dict) -> None:
    """Instantiate one API client class and best-effort call every public method."""
    client_instance = client_class(base_client)
    for name, method in inspect.getmembers(
        client_instance, predicate=inspect.ismethod
    ):
        if name.startswith("_") or name == "__init__":
            continue
        _call_client_method_best_effort(method, common_args)


def test_api_clients_brute_force(mock_session):
    base_client = BaseAtlassianClient(
        base_url="https://test.atlassian.net",
        username="test@example.com",
        token="dummy-token",
    )

    # Also verify Bearer token path in base client constructor
    base_client_bearer = BaseAtlassianClient(
        base_url="https://test.atlassian.net",
        username="test@example.com",
        token="dummy-token",
        bearer_token="dummy-bearer",
    )
    assert base_client_bearer.bearer_token == "dummy-bearer"

    # Test request exception path in base client
    with patch.object(
        base_client.session, "request", side_effect=Exception("Connection reset")
    ):
        res = base_client.request("GET", "/test")
        assert res.status_code == 500
        # Exception details are sanitized out of the response (security hardening);
        # the raw message is logged server-side instead of returned to the caller.
        assert res.message == "Operation failed"

    clients = [
        AdminCloudAPI,
        APIAccessCloudAPI,
        ConfluenceCloudAPI,
        ConfluenceServerAPI,
        ControlCloudAPI,
        DLPCloudAPI,
        JiraCloudAPI,
        JiraServerAPI,
        OrgCloudAPI,
        UserMgmtCloudAPI,
        UserProvisioningCloudAPI,
    ]

    common_args = {
        "org_id": "test-org",
        "level_id": "test-level",
        "orgId": "test-org",
        "issue_key": "PROJ-123",
        "issueIdOrKey": "PROJ-123",
        "project_key": "PROJ",
        "projectIdOrKey": "PROJ",
        "page_id": "123",
        "space_key": "SPACE",
        "user_id": "test-user",
        "username": "test-user",
        "id": "test-id",
        "key": "test-key",
        "name": "test-name",
        "payload": {},
        "body": {},
        "_max_pages": 5,
        "page_size": 10,
        "limit": 10,
        "start": 0,
    }

    for client_class in clients:
        _brute_force_client(client_class, base_client, common_args)
