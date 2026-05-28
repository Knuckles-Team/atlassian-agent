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

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import logging
import sys
from typing import Any

from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from atlassian_agent.auth import (
    get_admin_cloud_client,
    get_api_access_cloud_client,
    get_confluence_cloud_client,
    get_confluence_server_client,
    get_control_cloud_client,
    get_dlp_cloud_client,
    get_jira_cloud_client,
    get_jira_server_client,
    get_org_cloud_client,
    get_user_mgmt_cloud_client,
    get_user_provisioning_cloud_client,
)

__version__ = "0.15.0"

logger = get_logger(name="atlassian-agent")
logger.setLevel(logging.INFO)

_registered_tools = set()


def execute_client_method(
    client,
    action: str,
    prefix_cloud: str,
    prefix_server: str,
    host_type: str,
    kwargs: dict,
) -> Any:
    """Helper to dynamically lookup and invoke methods on cloud or server clients."""
    prefix = prefix_server if host_type == "server" else prefix_cloud

    # Try direct name
    method = getattr(client, action, None)
    if method is not None:
        return method(**kwargs)

    # Try with prefix
    action_name = action if action.startswith(prefix) else f"{prefix}{action}"
    method = getattr(client, action_name, None)
    if method is not None:
        return method(**kwargs)

    # Try stripped action name
    stripped = action
    for p in (
        prefix_cloud,
        prefix_server,
        "jira_cloud_",
        "jira_server_",
        "confluence_cloud_",
        "confluence_server_",
    ):
        if stripped.startswith(p):
            stripped = stripped[len(p) :]
            break

    method = getattr(client, f"{prefix}{stripped}", None) or getattr(
        client, stripped, None
    )
    if method is not None:
        return method(**kwargs)

    raise ValueError(f"Unknown action: {action} on {host_type} deployment")


def register_atlassian_control_tools(mcp: FastMCP):
    if "atlassian_control" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("atlassian_control")

    @mcp.tool(tags={"atlassian-control"})
    async def atlassian_atlassian_control(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_control_cloud_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage atlassian control operations."""
        if ctx:
            await ctx.info("Executing atlassian_control operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = execute_client_method(
                client, action, "control_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_atlassian_org_tools(mcp: FastMCP):
    if "atlassian_org" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("atlassian_org")

    @mcp.tool(tags={"atlassian-org"})
    async def atlassian_atlassian_org(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_org_cloud_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage atlassian org operations."""
        if ctx:
            await ctx.info("Executing atlassian_org operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = execute_client_method(
                client, action, "org_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_atlassian_dlp_tools(mcp: FastMCP):
    if "atlassian_dlp" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("atlassian_dlp")

    @mcp.tool(tags={"atlassian-dlp"})
    async def atlassian_atlassian_dlp(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_dlp_cloud_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage atlassian dlp operations."""
        if ctx:
            await ctx.info("Executing atlassian_dlp operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = execute_client_method(
                client, action, "dlp_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_atlassian_user_mgmt_tools(mcp: FastMCP):
    if "atlassian_user_mgmt" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("atlassian_user_mgmt")

    @mcp.tool(tags={"atlassian-user-mgmt"})
    async def atlassian_atlassian_user_mgmt(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_user_mgmt_cloud_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage atlassian user mgmt operations."""
        if ctx:
            await ctx.info("Executing atlassian_user_mgmt operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = execute_client_method(
                client, action, "user_mgmt_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_atlassian_admin_tools(mcp: FastMCP):
    if "atlassian_admin" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("atlassian_admin")

    @mcp.tool(tags={"atlassian-admin"})
    async def atlassian_atlassian_admin(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_admin_cloud_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage atlassian admin operations."""
        if ctx:
            await ctx.info("Executing atlassian_admin operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = execute_client_method(
                client, action, "admin_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_atlassian_api_access_tools(mcp: FastMCP):
    if "atlassian_api_access" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("atlassian_api_access")

    @mcp.tool(tags={"atlassian-api-access"})
    async def atlassian_atlassian_api_access(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_api_access_cloud_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage atlassian api access operations."""
        if ctx:
            await ctx.info("Executing atlassian_api_access operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = execute_client_method(
                client, action, "api_access_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_atlassian_user_provisioning_tools(mcp: FastMCP):
    if (
        "atlassian_user_provisioning" in _registered_tools
        and not type(mcp).__name__ == "Mock"
    ):
        return
    _registered_tools.add("atlassian_user_provisioning")

    @mcp.tool(tags={"atlassian-user-provisioning"})
    async def atlassian_atlassian_user_provisioning(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_user_provisioning_cloud_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage atlassian user provisioning operations."""
        if ctx:
            await ctx.info("Executing atlassian_user_provisioning operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = execute_client_method(
                client, action, "user_provisioning_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_atlassian_tools(mcp: FastMCP):
    if "atlassian" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("atlassian")

    @mcp.tool(tags={"atlassian"})
    async def atlassian_atlassian(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_user_mgmt_cloud_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage atlassian operations."""
        if ctx:
            await ctx.info("Executing atlassian operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = execute_client_method(
                client, action, "user_mgmt_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_project_tools(mcp: FastMCP):
    if "jira_project" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_project")

    @mcp.tool(tags={"jira-project"})
    async def atlassian_jira_project(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira project operations."""
        if ctx:
            await ctx.info("Executing jira_project operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_user_tools(mcp: FastMCP):
    if "jira_user" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_user")

    @mcp.tool(tags={"jira-user"})
    async def atlassian_jira_user(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira user operations."""
        if ctx:
            await ctx.info("Executing jira_user operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_issue_tools(mcp: FastMCP):
    if "jira_issue" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_issue")

    @mcp.tool(tags={"jira-issue"})
    async def atlassian_jira_issue(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira issue operations."""
        if ctx:
            await ctx.info("Executing jira_issue operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_comment_tools(mcp: FastMCP):
    if "jira_comment" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_comment")

    @mcp.tool(tags={"jira-comment"})
    async def atlassian_jira_comment(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira comment operations."""
        if ctx:
            await ctx.info("Executing jira_comment operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_field_tools(mcp: FastMCP):
    if "jira_field" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_field")

    @mcp.tool(tags={"jira-field"})
    async def atlassian_jira_field(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira field operations."""
        if ctx:
            await ctx.info("Executing jira_field operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_screen_tools(mcp: FastMCP):
    if "jira_screen" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_screen")

    @mcp.tool(tags={"jira-screen"})
    async def atlassian_jira_screen(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira screen operations."""
        if ctx:
            await ctx.info("Executing jira_screen operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_workflow_tools(mcp: FastMCP):
    if "jira_workflow" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_workflow")

    @mcp.tool(tags={"jira-workflow"})
    async def atlassian_jira_workflow(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira workflow operations."""
        if ctx:
            await ctx.info("Executing jira_workflow operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_jira_other_tools(mcp: FastMCP):
    if "jira_other" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("jira_other")

    @mcp.tool(tags={"jira-other"})
    async def atlassian_jira_other(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_jira_cloud_client),
        client_server=Depends(get_jira_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Jira other operations."""
        if ctx:
            await ctx.info("Executing jira_other operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client, action, "jira_cloud_", "jira_server_", deployment, kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_confluence_page_tools(mcp: FastMCP):
    if "confluence_page" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("confluence_page")

    @mcp.tool(tags={"confluence-page"})
    async def atlassian_confluence_page(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_confluence_cloud_client),
        client_server=Depends(get_confluence_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Confluence page operations."""
        if ctx:
            await ctx.info("Executing confluence_page operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client,
                action,
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_confluence_space_tools(mcp: FastMCP):
    if "confluence_space" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("confluence_space")

    @mcp.tool(tags={"confluence-space"})
    async def atlassian_confluence_space(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_confluence_cloud_client),
        client_server=Depends(get_confluence_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Confluence space operations."""
        if ctx:
            await ctx.info("Executing confluence_space operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client,
                action,
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_confluence_user_tools(mcp: FastMCP):
    if "confluence_user" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("confluence_user")

    @mcp.tool(tags={"confluence-user"})
    async def atlassian_confluence_user(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_confluence_cloud_client),
        client_server=Depends(get_confluence_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Confluence user operations."""
        if ctx:
            await ctx.info("Executing confluence_user operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client,
                action,
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def register_confluence_other_tools(mcp: FastMCP):
    if "confluence_other" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("confluence_other")

    @mcp.tool(tags={"confluence-other"})
    async def atlassian_confluence_other(
        action: str = Field(
            description="The specific action or client method to execute."
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        deployment: str = Field(
            default="cloud", description="Specify 'cloud' or 'server' deployment type."
        ),
        client_cloud=Depends(get_confluence_cloud_client),
        client_server=Depends(get_confluence_server_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> Any:
        """Manage Confluence other operations."""
        if ctx:
            await ctx.info("Executing confluence_other operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = execute_client_method(
                client,
                action,
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception as e:
            return {"error": str(e)}


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="atlassian-agent MCP",
        version=__version__,
        instructions="atlassian-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    # Register consolidated Atlassian tools
    register_atlassian_control_tools(mcp)
    register_atlassian_org_tools(mcp)

    # Register consolidated Jira tools
    register_jira_project_tools(mcp)
    register_jira_user_tools(mcp)
    register_jira_issue_tools(mcp)
    register_jira_comment_tools(mcp)
    register_jira_field_tools(mcp)
    register_jira_screen_tools(mcp)
    register_jira_workflow_tools(mcp)
    register_jira_other_tools(mcp)

    # Register consolidated Confluence tools
    register_confluence_page_tools(mcp)
    register_confluence_space_tools(mcp)
    register_confluence_user_tools(mcp)
    register_confluence_other_tools(mcp)

    # Register other Atlassian tools
    register_atlassian_dlp_tools(mcp)
    register_atlassian_user_mgmt_tools(mcp)
    register_atlassian_tools(mcp)
    register_atlassian_admin_tools(mcp)
    register_atlassian_api_access_tools(mcp)
    register_atlassian_user_provisioning_tools(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    mcp, args, middlewares = get_mcp_instance()
    print(f"atlassian-agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
