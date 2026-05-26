"""MCP tools for atlassian dlp operations.

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
    get_dlp_cloud_client,
)


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
