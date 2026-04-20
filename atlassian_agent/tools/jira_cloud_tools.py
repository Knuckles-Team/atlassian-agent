# Generated MCP Tools for JiraCloud (Modular Coordinator)
from fastmcp import FastMCP
from .jira_issue_tools import register_jira_issue_tools
from .jira_project_tools import register_jira_project_tools
from .jira_user_tools import register_jira_user_tools
from .jira_schema_tools import register_jira_schema_tools
from .jira_core_tools import register_jira_core_tools
from .jira_other_tools import register_jira_other_tools


def register_jira_cloud_tools(mcp: FastMCP):
    """Register all modularized Jira Cloud tools"""
    register_jira_issue_tools(mcp)
    register_jira_project_tools(mcp)
    register_jira_user_tools(mcp)
    register_jira_schema_tools(mcp)
    register_jira_core_tools(mcp)
    register_jira_other_tools(mcp)
