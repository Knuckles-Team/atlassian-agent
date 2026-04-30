import os

import urllib3

from .api.base import BaseAtlassianClient

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

_base_client = None


def get_suite_client(suite_prefix: str | None = None) -> BaseAtlassianClient:
    """Get client using suite-specific env vars or fall back to shared."""
    if suite_prefix:
        url = os.getenv(f"ATLASSIAN_{suite_prefix}_URL")
        user = os.getenv(f"ATLASSIAN_{suite_prefix}_USER")
        token = os.getenv(f"ATLASSIAN_{suite_prefix}_TOKEN")
        verify_str = os.getenv(f"ATLASSIAN_{suite_prefix}_VERIFY")
    else:
        url = user = token = verify_str = None

    # fallback to shared
    url = url or os.getenv("ATLASSIAN_AGENT_URL")
    user = user or os.getenv("ATLASSIAN_AGENT_USER")
    token = token or os.getenv("ATLASSIAN_AGENT_TOKEN")

    verify = (
        verify_str.lower() in ("true", "1", "yes")
        if verify_str
        else os.getenv("ATLASSIAN_AGENT_VERIFY", "True").lower() in ("true", "1", "yes")
    )

    return BaseAtlassianClient(
        base_url=url or "https://dummy.atlassian.net",
        username=user or "",
        token=token or "",
        verify=verify,
    )


def get_base_client(
    url: str | None = None,
    user: str | None = None,
    token: str | None = None,
    verify: bool | None = None,
) -> BaseAtlassianClient:
    """Get or create a singleton base API client instance."""
    global _base_client
    if _base_client is None:
        _base_client = get_suite_client(None)
    return _base_client
