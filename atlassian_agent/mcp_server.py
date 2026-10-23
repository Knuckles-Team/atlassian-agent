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

from agent_connector_sdk.config import load_config
from agent_connector_sdk.mcp.concurrency import run_blocking
from agent_connector_sdk.mcp.server import create_mcp_server
from agent_connector_sdk.mcp.tool_surface import register_tool_surface
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from atlassian_agent.deployment_tools import client_factory, configured_deployment

__version__ = "2.4.1"

logger = get_logger(name="atlassian-agent")
logger.setLevel(logging.INFO)

_registered_tools: set[str] = set()


def _plain(res: Any) -> Any:
    """A client Response as a plain dict."""
    if hasattr(res, "model_dump") and callable(res.model_dump):
        return res.model_dump()
    return res


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
        client=Depends(client_factory("jira")),
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

        # Cloud and Server name their JQL search differently; the deployment comes
        # from ATLASSIAN_JIRA_DEPLOYMENT, like every jira_<operation> tool.
        search = (
            "search_1"
            if configured_deployment("jira") == "server"
            else "search_for_issues_using_jql"
        )
        try:
            resp = _plain(
                await run_blocking(
                    client._call, search, {"jql": jql, "max_results": max_results}
                )
            )
        except Exception:
            return {"error": "Operation failed"}

        data = resp.get("data") if isinstance(resp, dict) else resp
        issues = data.get("issues", []) if isinstance(data, dict) else []
        result = await ingest_issues(issues)
        return {"listed": len(issues), "ingested": result}

    @mcp.tool(tags={"kg", "confluence-page"})
    async def atlassian_ingest_confluence(
        space_id: str = Field(
            default="", description="Optional Confluence space id to scope the pages."
        ),
        limit: int = Field(
            default=25, description="Maximum number of pages to fetch and ingest."
        ),
        client=Depends(client_factory("confluence")),
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

        kwargs: dict[str, Any] = {"limit": limit, "body_format": "storage"}
        if space_id:
            kwargs["space_id"] = [space_id]
        try:
            resp = _plain(await run_blocking(client._call, "get_pages", kwargs))
        except Exception:
            return {"error": "Operation failed"}

        data = resp.get("data") if isinstance(resp, dict) else resp
        pages = data.get("results", []) if isinstance(data, dict) else []
        result = await ingest_confluence_pages(pages)
        return {"listed": len(pages), "ingested": result}


_OPERATION_CLIENTS = (
    (
        "admin_cloud",
        "api_client_admin_cloud",
        "AdminCloudAPI",
        "get_admin_cloud_client",
    ),
    (
        "api_access_cloud",
        "api_client_api_access_cloud",
        "APIAccessCloudAPI",
        "get_api_access_cloud_client",
    ),
    (
        "control_cloud",
        "api_client_control_cloud",
        "ControlCloudAPI",
        "get_control_cloud_client",
    ),
    ("dlp_cloud", "api_client_dlp_cloud", "DLPCloudAPI", "get_dlp_cloud_client"),
    ("org_cloud", "api_client_org_cloud", "OrgCloudAPI", "get_org_cloud_client"),
    (
        "user_mgmt_cloud",
        "api_client_user_mgmt_cloud",
        "UserMgmtCloudAPI",
        "get_user_mgmt_cloud_client",
    ),
    (
        "user_provisioning_cloud",
        "api_client_user_provisioning_cloud",
        "UserProvisioningCloudAPI",
        "get_user_provisioning_cloud_client",
    ),
)


def _operation_targets() -> list[dict[str, Any]]:
    """One operation-tool target per Atlassian API client, named ``<suite>_<operation>``."""
    import importlib

    from atlassian_agent import auth
    from atlassian_agent.deployment_tools import PRODUCTS, client_factory, facade_class

    # Jira and Confluence: one jira_<operation> / confluence_<operation> tool per
    # operation; each picks Cloud or Server from configuration when it is called.
    targets: list[dict[str, Any]] = [
        {
            "client_cls": facade_class(product),
            "get_client": client_factory(product),
            "prefix": product,
        }
        for product in PRODUCTS
    ]
    for prefix, module, cls, factory in _OPERATION_CLIENTS:
        client_cls = getattr(
            importlib.import_module(f"atlassian_agent.api.{module}"), cls
        )
        targets.append(
            {
                "client_cls": client_cls,
                "get_client": getattr(auth, factory),
                "prefix": prefix,
            }
        )
    return targets


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="atlassian-agent MCP",
        version=__version__,
        instructions=(
            "atlassian-agent MCP Server: one typed tool per Atlassian API operation. "
            "Jira and Confluence tools use the Cloud or Server/Data Center client "
            "set by ATLASSIAN_JIRA_DEPLOYMENT / ATLASSIAN_CONFLUENCE_DEPLOYMENT."
        ),
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    registered_tags = register_tool_surface(
        mcp,
        service="atlassian-agent",
        tools_module=sys.modules[__name__],
        verbose_targets=_operation_targets(),
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
