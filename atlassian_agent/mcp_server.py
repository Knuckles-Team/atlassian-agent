#!/usr/bin/python
import warnings

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

# General urllib3/chardet mismatch warnings
warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from fastmcp.utilities.logging import get_logger
from starlette.requests import Request
from starlette.responses import JSONResponse

# Tool registration imports
try:
    from .tools.admin_cloud_tools import register_admin_cloud_tools
    from .tools.api_access_cloud_tools import register_api_access_cloud_tools
    from .tools.confluence_cloud_tools import register_confluence_cloud_tools
    from .tools.confluence_server_tools import register_confluence_server_tools
    from .tools.control_cloud_tools import register_control_cloud_tools
    from .tools.dlp_cloud_tools import register_dlp_cloud_tools
    from .tools.jira_cloud_tools import register_jira_cloud_tools
    from .tools.jira_server_tools import register_jira_server_tools
    from .tools.org_cloud_tools import register_org_cloud_tools
    from .tools.user_mgmt_cloud_tools import register_user_mgmt_cloud_tools
    from .tools.user_provisioning_cloud_tools import (
        register_user_provisioning_cloud_tools,
    )
except ImportError:
    # This might happen during initial setup or if tools aren't generated yet
    pass

__version__ = "0.1.8"

logger = get_logger(name="AtlassianMCP")


def get_mcp_instance() -> tuple[Any, Any, Any, Any]:
    """Initialize and return the MCP instance, args, and middlewares."""
    load_dotenv(find_dotenv())

    args, mcp, middlewares = create_mcp_server(
        name="Atlassian Universal Agent",
        version=__version__,
        instructions="Standardized Atlassian MCP server providing tools for Jira, Confluence, and Admin Cloud/Server.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    registered_suites = []

    # Mapping of env var to registration function
    suites = [
        ("ATLASSIAN_JIRA_CLOUD", register_jira_cloud_tools, "jira_cloud"),
        ("ATLASSIAN_JIRA_SERVER", register_jira_server_tools, "jira_server"),
        (
            "ATLASSIAN_CONFLUENCE_CLOUD",
            register_confluence_cloud_tools,
            "confluence_cloud",
        ),
        (
            "ATLASSIAN_CONFLUENCE_SERVER",
            register_confluence_server_tools,
            "confluence_server",
        ),
        ("ATLASSIAN_ADMIN_CLOUD", register_admin_cloud_tools, "admin_cloud"),
        ("ATLASSIAN_ORG_CLOUD", register_org_cloud_tools, "org_cloud"),
        (
            "ATLASSIAN_USER_MGMT_CLOUD",
            register_user_mgmt_cloud_tools,
            "user_mgmt_cloud",
        ),
        (
            "ATLASSIAN_USER_PROVISIONING_CLOUD",
            register_user_provisioning_cloud_tools,
            "user_provisioning_cloud",
        ),
        ("ATLASSIAN_CONTROL_CLOUD", register_control_cloud_tools, "control_cloud"),
        ("ATLASSIAN_DLP_CLOUD", register_dlp_cloud_tools, "dlp_cloud"),
        (
            "ATLASSIAN_API_ACCESS_CLOUD",
            register_api_access_cloud_tools,
            "api_access_cloud",
        ),
    ]

    for env_var, reg_func, name in suites:
        if to_boolean(os.getenv(env_var, "True")):
            try:
                reg_func(mcp)
                registered_suites.append(name)
            except Exception as e:
                logger.error(f"Failed to register suite {name}: {e}")

    for mw in middlewares:
        mcp.add_middleware(mw)

    return mcp, args, middlewares, registered_suites


def mcp_server() -> None:
    mcp, args, middlewares, registered_suites = get_mcp_instance()
    print(f"Atlassian Universal Agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)
    print(f"  Loaded Suites: {', '.join(registered_suites)}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error(f"Invalid transport: {args.transport}")
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
