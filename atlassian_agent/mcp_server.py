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

from agent_utilities.core.config import load_config, setting
from agent_utilities.mcp.action_dispatch import (
    DISCOVERY_ACTIONS,
    dispatch,
    public_actions,
)
from agent_utilities.mcp.concurrency import run_blocking
from agent_utilities.mcp.server_factory import create_mcp_server
from agent_utilities.mcp.verbose_tools import register_tool_surface
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from atlassian_agent.api.base import BaseAtlassianClient
from atlassian_agent.auth import (
    get_admin_cloud_client,
    get_api_access_cloud_client,
    get_base_client,
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

__version__ = "1.1.0"

logger = get_logger(name="atlassian-agent")
logger.setLevel(logging.INFO)

_registered_tools: set[str] = set()


_STRIP_PREFIXES = (
    "control_cloud_",
    "org_cloud_",
    "dlp_cloud_",
    "user_mgmt_cloud_",
    "admin_cloud_",
    "api_access_cloud_",
    "user_provisioning_cloud_",
    "jira_cloud_",
    "jira_server_",
    "confluence_cloud_",
    "confluence_server_",
)


def execute_client_method(
    client,
    action: str,
    prefix_cloud: str,
    prefix_server: str,
    host_type: str,
    kwargs: dict,
) -> Any:
    """Dispatch ``action`` to a cloud or server client via the shared helper.

    Action discovery (``list_actions``/``help``/``actions``), plural->singular
    aliasing, and rich did-you-mean errors come from
    ``agent_utilities.mcp.action_dispatch.dispatch``. The client's methods are
    deployment-prefixed (e.g. ``jira_cloud_add_comment``); we build an alias map
    so callers may pass the unprefixed name (``add_comment``) too.
    """
    # Build an alias map so discovery stays bounded to the client's real actions
    # while preserving this repo's prefix conveniences:
    #  - unprefixed name -> real prefixed method (e.g. add_comment ->
    #    jira_cloud_add_comment), preferring the active deployment's prefix
    #  - a prefixed form -> a real unprefixed method (e.g. jira_cloud_foo -> foo)
    active_prefix = prefix_server if host_type == "server" else prefix_cloud
    names = public_actions(client)
    aliases: dict[str, str] = {}
    for name in names:
        for p in _STRIP_PREFIXES:
            if name.startswith(p):
                bare = name[len(p) :]
                if bare not in aliases or (active_prefix and p == active_prefix):
                    aliases[bare] = name
                break
        else:
            # Unprefixed real method: accept prefixed guesses pointing at it.
            for p in _STRIP_PREFIXES:
                aliases.setdefault(f"{p}{name}", name)

    def _coerce(res: Any) -> Any:
        if hasattr(res, "dict") and callable(res.dict):
            return res.dict()
        if hasattr(res, "model_dump") and callable(res.model_dump):
            return res.model_dump()
        return res

    return dispatch(
        client,
        action,
        kwargs,
        aliases=aliases,
        service=f"atlassian-agent ({host_type})",
        result_coercer=_coerce if action not in DISCOVERY_ACTIONS else None,
    )


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "control_cloud_",
                "",
                "cloud",
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = await run_blocking(
                execute_client_method, client, action, "org_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = await run_blocking(
                execute_client_method, client, action, "dlp_cloud_", "", "cloud", kwargs
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "user_mgmt_cloud_",
                "",
                "cloud",
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "admin_cloud_",
                "",
                "cloud",
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "api_access_cloud_",
                "",
                "cloud",
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "user_provisioning_cloud_",
                "",
                "cloud",
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "user_mgmt_cloud_",
                "",
                "cloud",
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
            default=setting("ATLASSIAN_JIRA_DEPLOYMENT", "cloud"),
            description="Specify 'cloud' or 'server' deployment type.",
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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud
        # Preserve the shared Jira preset across Cloud and Server/DC.  The
        # generated Server client calls its JQL endpoint ``search_1`` while the
        # Cloud client exposes the descriptive action name.  Older presets also
        # carry the historical "reconsile" spelling.
        if deployment == "server" and action in {
            "search_for_issues_using_jql",
            "search_and_reconsile_issues_using_jql",
        }:
            action = "jira_server_search_1"
        elif (
            deployment != "server" and action == "search_and_reconsile_issues_using_jql"
        ):
            action = "jira_cloud_search_for_issues_using_jql"

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
                client,
                action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                kwargs,
            )
            if hasattr(res, "dict") and callable(res.dict):
                return res.dict()
            elif hasattr(res, "model_dump") and callable(res.model_dump):
                return res.model_dump()
            return res
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
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
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
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
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
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
        except Exception:
            return {"error": "Operation failed"}


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        client = client_server if deployment == "server" else client_cloud

        try:
            res = await run_blocking(
                execute_client_method,
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
        except Exception:
            return {"error": "Operation failed"}


def register_kg_tools(mcp: FastMCP):
    """Native epistemic-graph ingestion tools (CONCEPT:AU-KG.ingest.enterprise-source-extractor).

    Adds Wire-First tools that list via the existing Jira/Confluence clients and push the
    records into the knowledge graph as typed nodes / documents. Gated by ``KGTOOL``.
    """
    if "kg" in _registered_tools and not type(mcp).__name__ == "Mock":
        return
    _registered_tools.add("kg")

    @mcp.tool(tags={"kg", "jira-issue"})
    async def atlassian_ingest_issues(
        jql: str = Field(
            default="ORDER BY updated DESC",
            description="JQL selecting the issues to ingest (e.g. 'project = PROJ').",
        ),
        max_results: int = Field(
            default=50, description="Maximum number of issues to fetch and ingest."
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
        """Natively ingest Jira issues into epistemic-graph as typed :Issue/:Epic/:Person nodes.

        Searches Jira with ``jql`` and pushes each issue (with its assignee/reporter
        :Person nodes and :inEpic / :assignedTo / :reportedBy links) into the knowledge
        graph via the fast engine client. Best-effort: ``{"ingested": None}`` when no
        engine is reachable. CONCEPT:AU-KG.ingest.enterprise-source-extractor.
        """
        if ctx:
            await ctx.info("Ingesting Jira issues into the knowledge graph...")
        from atlassian_agent.kg_ingest import ingest_issues

        client = client_server if deployment == "server" else client_cloud
        search_action = (
            "jira_server_search_1"
            if deployment == "server"
            else "jira_cloud_search_for_issues_using_jql"
        )
        try:
            resp = await run_blocking(
                execute_client_method,
                client,
                search_action,
                "jira_cloud_",
                "jira_server_",
                deployment,
                {"jql": jql, "max_results": max_results},
            )
        except Exception:
            return {"error": "Operation failed"}

        data = resp.get("data") if isinstance(resp, dict) else resp
        issues = data.get("issues", []) if isinstance(data, dict) else []
        result = ingest_issues(issues)
        return {"listed": len(issues), "ingested": result}

    @mcp.tool(tags={"kg", "confluence-page"})
    async def atlassian_ingest_confluence(
        space_id: str = Field(
            default="", description="Optional Confluence space id to scope the pages."
        ),
        limit: int = Field(
            default=25, description="Maximum number of pages to fetch and ingest."
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
        """Natively ingest Confluence pages into epistemic-graph as :Document nodes.

        Lists pages (body_format=storage) and pushes each as a :ConfluencePage :Document
        carrying the page body text + source_uri for semantic search. Best-effort:
        ``{"ingested": None}`` when no engine is reachable.
        CONCEPT:AU-KG.ingest.enterprise-source-extractor.
        """
        if ctx:
            await ctx.info("Ingesting Confluence pages into the knowledge graph...")
        from atlassian_agent.kg_ingest import ingest_confluence_pages

        client = client_server if deployment == "server" else client_cloud
        kwargs: dict[str, Any] = {"limit": limit, "body_format": "storage"}
        if space_id:
            kwargs["space_id"] = [space_id]
        try:
            resp = await run_blocking(
                execute_client_method,
                client,
                "get_pages",
                "confluence_cloud_",
                "confluence_server_",
                deployment,
                kwargs,
            )
        except Exception:
            return {"error": "Operation failed"}

        data = resp.get("data") if isinstance(resp, dict) else resp
        pages = data.get("results", []) if isinstance(data, dict) else []
        result = ingest_confluence_pages(pages)
        return {"listed": len(pages), "ingested": result}


def _condensed_action_providers() -> dict[str, type]:
    """Map each condensed action-routed tool to the client class it dispatches to.

    The condensed tools declare a free-form ``action: str`` and obtain their valid
    action names at runtime from ``public_actions(client)`` — so they carry no static
    JSON-schema ``enum`` and the verbose auto-wire (ECO-4.89) would otherwise skip
    them. Recording each tool's backing **client class** here lets the auto-wire
    enumerate that class's public methods credential-free (``dir()`` on the class)
    and emit one ``<tool>__<action>`` verbose tool per action — turning the 621 Jira
    and 214 Confluence operations into a directly-selectable 1:1 surface in
    ``MCP_TOOL_MODE=both``.

    All ``jira_*`` tools front the same ``JiraCloudAPI`` and all ``confluence_*``
    tools the same ``ConfluenceCloudAPI`` (the per-tool split is a UX grouping, not a
    client split). Exposing the full product action set on *every* sub-tool would
    multiply it (8 jira sub-tools × 621 = redundant copies of the same operations),
    so the full set is recorded on the single catch-all tool per product
    (``*_other``) — yielding exactly 621 Jira + 214 Confluence verbose tools, each
    operation reachable once. Each admin/governance suite tool fronts its own client
    and gets its own action set.

    CONCEPT:ECO-4.90 — verbose auto-wire enumerates dynamic (runtime) actions
    """
    from atlassian_agent.api.api_client_admin_cloud import AdminCloudAPI
    from atlassian_agent.api.api_client_api_access_cloud import APIAccessCloudAPI
    from atlassian_agent.api.api_client_confluence_cloud import ConfluenceCloudAPI
    from atlassian_agent.api.api_client_control_cloud import ControlCloudAPI
    from atlassian_agent.api.api_client_dlp_cloud import DLPCloudAPI
    from atlassian_agent.api.api_client_jira_cloud import JiraCloudAPI
    from atlassian_agent.api.api_client_org_cloud import OrgCloudAPI
    from atlassian_agent.api.api_client_user_mgmt_cloud import UserMgmtCloudAPI
    from atlassian_agent.api.api_client_user_provisioning_cloud import (
        UserProvisioningCloudAPI,
    )

    return {
        # Jira (621 actions) — recorded once on the catch-all jira tool.
        "atlassian_jira_other": JiraCloudAPI,
        # Confluence (214 actions) — recorded once on the catch-all confluence tool.
        "atlassian_confluence_other": ConfluenceCloudAPI,
        # Admin / org / governance suites — one client each.
        "atlassian_atlassian": UserMgmtCloudAPI,
        "atlassian_atlassian_admin": AdminCloudAPI,
        "atlassian_atlassian_org": OrgCloudAPI,
        "atlassian_atlassian_dlp": DLPCloudAPI,
        "atlassian_atlassian_control": ControlCloudAPI,
        "atlassian_atlassian_api_access": APIAccessCloudAPI,
        "atlassian_atlassian_user_provisioning": UserProvisioningCloudAPI,
    }


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="atlassian-agent MCP",
        version=__version__,
        instructions="atlassian-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    registered_tags = register_tool_surface(
        mcp,
        client_cls=BaseAtlassianClient,
        get_client=get_base_client,
        service="atlassian-agent",
        tools_module=sys.modules[__name__],
        action_providers=_condensed_action_providers(),
    )
    logger.debug("Registered condensed tool tags: %s", registered_tags)

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
