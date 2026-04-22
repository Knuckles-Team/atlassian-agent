import os

import urllib3

from .api.base import BaseAtlassianClient

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

_base_client = None


def get_base_client(
    url: str | None = None,
    user: str | None = None,
    token: str | None = None,
    verify: bool | None = None,
) -> BaseAtlassianClient:
    """Get or create a singleton base API client instance."""
    global _base_client

    # Use provided args or env vars
    url = url or os.getenv("ATLASSIAN_AGENT_URL") or "https://dummy.atlassian.net"
    user = user or os.getenv("ATLASSIAN_AGENT_USER") or ""
    token = token or os.getenv("ATLASSIAN_AGENT_TOKEN") or ""

    if verify is None:
        verify = os.getenv("ATLASSIAN_AGENT_VERIFY", "True").lower() in (
            "true",
            "1",
            "yes",
        )

    # For simplicity in this large suite, we'll use a singleton for the session-carrying base client
    if _base_client is None:
        _base_client = BaseAtlassianClient(
            base_url=url, username=user, token=token, verify=verify
        )
    return _base_client
