"""MCP tools for atlassian operations.

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
    get_user_mgmt_cloud_client,
)


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
