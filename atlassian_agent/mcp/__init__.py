"""MCP tool registration modules for atlassian-agent.

Auto-generated during ecosystem standardization.
Each domain has its own module with a register_*_tools function.
"""

from atlassian_agent.mcp.mcp_atlassian import register_atlassian_tools
from atlassian_agent.mcp.mcp_atlassian_admin import register_atlassian_admin_tools
from atlassian_agent.mcp.mcp_atlassian_api_access import (
    register_atlassian_api_access_tools,
)
from atlassian_agent.mcp.mcp_atlassian_control import register_atlassian_control_tools
from atlassian_agent.mcp.mcp_atlassian_dlp import register_atlassian_dlp_tools
from atlassian_agent.mcp.mcp_atlassian_org import register_atlassian_org_tools
from atlassian_agent.mcp.mcp_atlassian_user_mgmt import (
    register_atlassian_user_mgmt_tools,
)
from atlassian_agent.mcp.mcp_atlassian_user_provisioning import (
    register_atlassian_user_provisioning_tools,
)
from atlassian_agent.mcp.mcp_confluence_other import register_confluence_other_tools
from atlassian_agent.mcp.mcp_confluence_page import register_confluence_page_tools
from atlassian_agent.mcp.mcp_confluence_space import register_confluence_space_tools
from atlassian_agent.mcp.mcp_confluence_user import register_confluence_user_tools
from atlassian_agent.mcp.mcp_jira_comment import register_jira_comment_tools
from atlassian_agent.mcp.mcp_jira_field import register_jira_field_tools
from atlassian_agent.mcp.mcp_jira_issue import register_jira_issue_tools
from atlassian_agent.mcp.mcp_jira_other import register_jira_other_tools
from atlassian_agent.mcp.mcp_jira_project import register_jira_project_tools
from atlassian_agent.mcp.mcp_jira_screen import register_jira_screen_tools
from atlassian_agent.mcp.mcp_jira_user import register_jira_user_tools
from atlassian_agent.mcp.mcp_jira_workflow import register_jira_workflow_tools

__all__ = [
    "register_atlassian_tools",
    "register_atlassian_admin_tools",
    "register_atlassian_api_access_tools",
    "register_atlassian_control_tools",
    "register_atlassian_dlp_tools",
    "register_atlassian_org_tools",
    "register_atlassian_user_mgmt_tools",
    "register_atlassian_user_provisioning_tools",
    "register_confluence_other_tools",
    "register_confluence_page_tools",
    "register_confluence_space_tools",
    "register_confluence_user_tools",
    "register_jira_comment_tools",
    "register_jira_field_tools",
    "register_jira_issue_tools",
    "register_jira_other_tools",
    "register_jira_project_tools",
    "register_jira_screen_tools",
    "register_jira_user_tools",
    "register_jira_workflow_tools",
]
