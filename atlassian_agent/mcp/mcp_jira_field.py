"""MCP tools for jira field operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from atlassian_agent.mcp_server import (
    _registered_tools,
    execute_client_method,
)
from atlassian_agent.auth import (
    get_jira_cloud_client,
    get_jira_server_client,
)


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
