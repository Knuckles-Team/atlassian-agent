from unittest.mock import MagicMock

import requests

from atlassian_agent.models import Response


def test_response_json_success():
    mock_resp = MagicMock(spec=requests.Response)
    mock_resp.status_code = 200
    mock_resp.ok = True
    mock_resp.json.return_value = {"key": "value"}

    res = Response.from_requests_response(mock_resp)
    assert res.status_code == 200
    assert res.data == {"key": "value"}
    assert res.message == "Success"


def test_response_json_failure():
    mock_resp = MagicMock(spec=requests.Response)
    mock_resp.status_code = 500
    mock_resp.ok = False
    mock_resp.reason = "Internal Server Error"
    mock_resp.json.side_effect = ValueError("Invalid JSON")
    mock_resp.text = "Error detail string"

    res = Response.from_requests_response(mock_resp)
    assert res.status_code == 500
    assert res.data == {"content": "Error detail string"}
    assert res.message == "Error: Internal Server Error"


def test_response_html_error_page_is_summarised():
    mock_resp = MagicMock(spec=requests.Response)
    mock_resp.status_code = 404
    mock_resp.ok = False
    mock_resp.reason = "Not Found"
    mock_resp.json.side_effect = ValueError("Invalid JSON")
    mock_resp.text = "<html><head><title>Page Unavailable</title></head><body><p>Site gone</p></body></html>"

    res = Response.from_requests_response(mock_resp)
    assert "<" not in res.data["content"]
    assert res.message == "Error: Not Found: Page Unavailable Site gone"


def test_response_json_error_message_is_surfaced():
    mock_resp = MagicMock(spec=requests.Response)
    mock_resp.status_code = 404
    mock_resp.ok = False
    mock_resp.reason = "Not Found"
    mock_resp.json.return_value = {"errorMessage": "Site temporarily unavailable"}

    res = Response.from_requests_response(mock_resp)
    assert res.message == "Error: Not Found: Site temporarily unavailable"
