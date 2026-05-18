# Atlassian Agent - A2A | AG-UI | MCP

![PyPI - Version](https://img.shields.io/pypi/v/atlassian-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/atlassian-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/atlassian-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/atlassian-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/atlassian-agent)
![PyPI - License](https://img.shields.io/pypi/l/atlassian-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/atlassian-agent)

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/atlassian-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/atlassian-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/atlassian-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/atlassian-agent)

![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/atlassian-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/atlassian-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/atlassian-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/atlassian-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/atlassian-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/atlassian-agent)

*Version: 0.10.0*

## Overview

**Atlassian Agent MCP Server + A2A Agent**

Comprehensive AI agent for Jira and Confluence management.

This repository is actively maintained - Contributions are welcome!

## MCP

### Using as an MCP Server

The MCP Server can be run in two modes: `stdio` (for local testing) or `http` (for networked access).

#### Environment Variables

Shared Cloud Variables:
*   `ATLASSIAN_AGENT_URL`: The URL of the target service (e.g. https://your-company.atlassian.net).
*   `ATLASSIAN_AGENT_TOKEN`: The API token or access token for Cloud.

Jira Server Variables:
*   `ATLASSIAN_JIRA_SERVER_URL`: The URL of the Jira Server.
*   `ATLASSIAN_JIRA_SERVER_USER`: The username for Jira Server.
*   `ATLASSIAN_JIRA_SERVER_TOKEN`: The token/password for Jira Server.
*   `ATLASSIAN_JIRA_SERVER_VERIFY`: Boolean to verify SSL for Jira Server.

Confluence Server Variables:
*   `ATLASSIAN_CONFLUENCE_SERVER_URL`: The URL of the Confluence Server.
*   `ATLASSIAN_CONFLUENCE_SERVER_USER`: The username for Confluence Server.
*   `ATLASSIAN_CONFLUENCE_SERVER_TOKEN`: The token/password for Confluence Server.
*   `ATLASSIAN_CONFLUENCE_SERVER_VERIFY`: Boolean to verify SSL for Confluence Server.

#### Run in stdio mode (default):
```bash
export ATLASSIAN_AGENT_URL="http://localhost:8080"
export ATLASSIAN_AGENT_TOKEN="your_token"
atlassian-mcp --transport "stdio"
```

#### Run in HTTP mode:
```bash
export ATLASSIAN_AGENT_URL="http://localhost:8080"
export ATLASSIAN_AGENT_TOKEN="your_token"
atlassian-mcp --transport "http" --host "0.0.0.0" --port "8000"
```

## A2A Agent

### Run A2A Server
```bash
export ATLASSIAN_AGENT_URL="http://localhost:8080"
export ATLASSIAN_AGENT_TOKEN="your_token"
atlassian-agent --provider openai --model-id gpt-4o --api-key sk-...
```

## Docker

### Build

```bash
docker build -t atlassian-agent .
```

### Run MCP Server

```bash
docker run -d \
  --name atlassian-agent \
  -p 8000:8000 \
  -e TRANSPORT=http \
  -e ATLASSIAN_AGENT_URL="http://your-service:8080" \
  -e ATLASSIAN_AGENT_TOKEN="your_token" \
  knucklessg1/atlassian-agent:latest
```

### Deploy with Docker Compose

```yaml
services:
  atlassian-agent:
    image: knucklessg1/atlassian-agent:latest
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=http
      - ATLASSIAN_AGENT_URL=http://your-service:8080
      - ATLASSIAN_AGENT_TOKEN=your_token
    ports:
      - 8000:8000
```

#### Configure `mcp.json` for AI Integration (e.g. Claude Desktop)

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "atlassian-agent",
        "atlassian-mcp"
      ],
      "env": {
        "ATLASSIAN_AGENT_URL": "http://your-service:8080",
        "ATLASSIAN_AGENT_TOKEN": "your_token",
        "ATLASSIAN_JIRA_SERVER_URL": "http://your-jira-server",
        "ATLASSIAN_JIRA_SERVER_USER": "your-username",
        "ATLASSIAN_JIRA_SERVER_TOKEN": "your-jira-token",
        "ATLASSIAN_JIRA_SERVER_VERIFY": "true",
        "ATLASSIAN_CONFLUENCE_SERVER_URL": "http://your-confluence-server",
        "ATLASSIAN_CONFLUENCE_SERVER_USER": "your-username",
        "ATLASSIAN_CONFLUENCE_SERVER_TOKEN": "your-confluence-token",
        "ATLASSIAN_CONFLUENCE_SERVER_VERIFY": "true"
      }
    }
  }
}
```

## Install Python Package

```bash
python -m pip install atlassian-agent
```
```bash
uv pip install atlassian-agent
```

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)


## MCP Configuration Examples

### 1. Standard IO (stdio) Deployment

```json
{
  "mcpServers": {
    "atlassian-agent": {
      "command": "uv",
      "args": [
        "run",
        "atlassian-mcp"
      ],
      "env": {
        "AGENT_DESCRIPTION": "<YOUR_AGENT_DESCRIPTION>",
        "AGENT_SYSTEM_PROMPT": "<YOUR_AGENT_SYSTEM_PROMPT>",
        "ATLASSIAN_AGENT_TOKEN": "<YOUR_ATLASSIAN_AGENT_TOKEN>",
        "ATLASSIAN_AGENT_URL": "<YOUR_ATLASSIAN_AGENT_URL>",
        "ATLASSIAN_AGENT_USER": "<YOUR_ATLASSIAN_AGENT_USER>",
        "ATLASSIAN_AGENT_VERIFY": "<YOUR_ATLASSIAN_AGENT_VERIFY>",
        "DEFAULT_AGENT_NAME": "<YOUR_DEFAULT_AGENT_NAME>"
      }
    }
  }
}
```

### 2. Streamable HTTP (SSE) Deployment

```json
{
  "mcpServers": {
    "atlassian-agent": {
      "command": "uv",
      "args": [
        "run",
        "atlassian-mcp",
        "--transport",
        "http",
        "--host",
        "0.0.0.0",
        "--port",
        "8000"
      ],
      "env": {
        "AGENT_DESCRIPTION": "<YOUR_AGENT_DESCRIPTION>",
        "AGENT_SYSTEM_PROMPT": "<YOUR_AGENT_SYSTEM_PROMPT>",
        "ATLASSIAN_AGENT_TOKEN": "<YOUR_ATLASSIAN_AGENT_TOKEN>",
        "ATLASSIAN_AGENT_URL": "<YOUR_ATLASSIAN_AGENT_URL>",
        "ATLASSIAN_AGENT_USER": "<YOUR_ATLASSIAN_AGENT_USER>",
        "ATLASSIAN_AGENT_VERIFY": "<YOUR_ATLASSIAN_AGENT_VERIFY>",
        "DEFAULT_AGENT_NAME": "<YOUR_DEFAULT_AGENT_NAME>"
      }
    }
  }
}
```

## Available MCP Tools
This server implements an action-routed dynamic tool architecture, consolidating operations into categorized tools.
| Tool Name | Action | Description |
|-----------|--------|-------------|
| `control_cloud_atlassian_control` | `control_cloud_ap_is_get_policies` | Executes `control_cloud_ap_is_get_policies` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_create_policy` | Executes `control_cloud_ap_is_create_policy` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_get_policy` | Executes `control_cloud_ap_is_get_policy` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_update_policy` | Executes `control_cloud_ap_is_update_policy` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_delete_policy` | Executes `control_cloud_ap_is_delete_policy` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_get_policies_v2` | Executes `control_cloud_ap_is_get_policies_v2` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_create_policy_v2` | Executes `control_cloud_ap_is_create_policy_v2` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_get_policy_v2` | Executes `control_cloud_ap_is_get_policy_v2` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_update_policy_v2` | Executes `control_cloud_ap_is_update_policy_v2` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_publish_draft_policies` | Executes `control_cloud_ap_is_publish_draft_policies` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_get_resources` | Executes `control_cloud_ap_is_get_resources` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_create_resource` | Executes `control_cloud_ap_is_create_resource` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_delete_resources` | Executes `control_cloud_ap_is_delete_resources` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_update_resource` | Executes `control_cloud_ap_is_update_resource` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_delete_resource` | Executes `control_cloud_ap_is_delete_resource` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_get_resources_v2` | Executes `control_cloud_ap_is_get_resources_v2` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_attach_detach_resources_v2` | Executes `control_cloud_ap_is_attach_detach_resources_v2` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_delete_resources_v2` | Executes `control_cloud_ap_is_delete_resources_v2` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_validate_policy` | Executes `control_cloud_ap_is_validate_policy` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_add_users_to_policy` | Executes `control_cloud_ap_is_add_users_to_policy` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_get_task_status` | Executes `control_cloud_ap_is_get_task_status` within the `atlassian-control` category. |
| `control_cloud_atlassian_control` | `control_cloud_ap_is_bulk_fetch_auth_policy` | Executes `control_cloud_ap_is_bulk_fetch_auth_policy` within the `atlassian-control` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_orgs` | Executes `org_cloud_get_orgs` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_org_by_id` | Executes `org_cloud_get_org_by_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_directory_users` | Executes `org_cloud_get_directory_users` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_directory_user_details` | Executes `org_cloud_get_directory_user_details` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_users` | Executes `org_cloud_get_users` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v2_orgs_org_id_users_invite` | Executes `org_cloud_post_v2_orgs_org_id_users_invite` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_user_role_assignments` | Executes `org_cloud_get_user_role_assignments` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_assign_role` | Executes `org_cloud_assign_role` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_revoke_role` | Executes `org_cloud_revoke_role` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` | Executes `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` | Executes `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` | Executes `org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` | Executes `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` | Executes `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_directory_users_count` | Executes `org_cloud_get_directory_users_count` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_user_stats` | Executes `org_cloud_get_user_stats` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` | Executes `org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_search_users` | Executes `org_cloud_search_users` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v1_orgs_org_id_users_invite` | Executes `org_cloud_post_v1_orgs_org_id_users_invite` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` | Executes `org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` | Executes `org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_delete_v1_orgs_org_id_directory_users_account_id` | Executes `org_cloud_delete_v1_orgs_org_id_directory_users_account_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_groups` | Executes `org_cloud_get_groups` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups` | Executes `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_group_role_assignments` | Executes `org_cloud_get_group_role_assignments` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` | Executes `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` | Executes `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` | Executes `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` | Executes `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` | Executes `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_group` | Executes `org_cloud_get_group` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_groups_count` | Executes `org_cloud_get_groups_count` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_groups_stats` | Executes `org_cloud_get_groups_stats` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_search_groups` | Executes `org_cloud_search_groups` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v1_orgs_org_id_directory_groups` | Executes `org_cloud_post_v1_orgs_org_id_directory_groups` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id` | Executes `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_assign_role_to_group` | Executes `org_cloud_assign_role_to_group` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_revoke_role_to_group` | Executes `org_cloud_revoke_role_to_group` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` | Executes `org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` | Executes `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_directories_for_org` | Executes `org_cloud_get_directories_for_org` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_domains` | Executes `org_cloud_get_domains` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_domain_by_id` | Executes `org_cloud_get_domain_by_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_events` | Executes `org_cloud_get_events` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_poll_events` | Executes `org_cloud_poll_events` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_event_by_id` | Executes `org_cloud_get_event_by_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_event_actions` | Executes `org_cloud_get_event_actions` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_policies` | Executes `org_cloud_get_policies` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_create_policy` | Executes `org_cloud_create_policy` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_get_policy_by_id` | Executes `org_cloud_get_policy_by_id` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_update_policy` | Executes `org_cloud_update_policy` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_delete_policy` | Executes `org_cloud_delete_policy` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_add_resource_to_policy` | Executes `org_cloud_add_resource_to_policy` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_update_policy_resource` | Executes `org_cloud_update_policy_resource` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_delete_policy_resource` | Executes `org_cloud_delete_policy_resource` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_validate_policy` | Executes `org_cloud_validate_policy` within the `atlassian-org` category. |
| `org_cloud_atlassian_org` | `org_cloud_query_workspaces_v2` | Executes `org_cloud_query_workspaces_v2` within the `atlassian-org` category. |
| `jira_server_jira_server_other` | `jira_server_move_issues_to_backlog` | Executes `jira_server_move_issues_to_backlog` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issues_for_backlog` | Executes `jira_server_get_issues_for_backlog` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_configuration` | Executes `jira_server_get_configuration` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_properties_keys` | Executes `jira_server_get_properties_keys` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_property` | Executes `jira_server_get_property` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_property` | Executes `jira_server_set_property` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_property` | Executes `jira_server_delete_property` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_refined_velocity` | Executes `jira_server_get_refined_velocity` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_refined_velocity` | Executes `jira_server_set_refined_velocity` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_all_versions` | Executes `jira_server_get_all_versions` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_rank_issues` | Executes `jira_server_rank_issues` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue` | Executes `jira_server_get_issue` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_properties_keys_1` | Executes `jira_server_get_properties_keys_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_property_1` | Executes `jira_server_get_property_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_property_1` | Executes `jira_server_set_property_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_property_1` | Executes `jira_server_delete_property_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_application_property` | Executes `jira_server_get_application_property` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_advanced_settings` | Executes `jira_server_get_advanced_settings` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_all` | Executes `jira_server_get_all` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_put_bulk` | Executes `jira_server_put_bulk` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_4` | Executes `jira_server_get_4` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_put_2` | Executes `jira_server_put_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_expand_for_humans` | Executes `jira_server_expand_for_humans` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_expand_for_machines` | Executes `jira_server_expand_for_machines` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_node` | Executes `jira_server_delete_node` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_change_node_state_to_offline` | Executes `jira_server_change_node_state_to_offline` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_all_nodes` | Executes `jira_server_get_all_nodes` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_acknowledge_errors` | Executes `jira_server_acknowledge_errors` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_state` | Executes `jira_server_get_state` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_properties_keys_1_2` | Executes `jira_server_get_properties_keys_1_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_comment_property` | Executes `jira_server_get_comment_property` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_property_1_2` | Executes `jira_server_set_property_1_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_property_2` | Executes `jira_server_delete_property_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_component` | Executes `jira_server_create_component` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_paginated_components` | Executes `jira_server_get_paginated_components` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_component` | Executes `jira_server_get_component` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_update_component` | Executes `jira_server_update_component` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete` | Executes `jira_server_delete` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_component_related_issues` | Executes `jira_server_get_component_related_issues` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_configuration_1` | Executes `jira_server_get_configuration_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_list` | Executes `jira_server_list` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_dashboard_item_properties_keys` | Executes `jira_server_get_dashboard_item_properties_keys` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_property_1_2` | Executes `jira_server_get_property_1_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_dashboard_item_property` | Executes `jira_server_set_dashboard_item_property` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_property_1_2` | Executes `jira_server_delete_property_1_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_download_email_templates` | Executes `jira_server_download_email_templates` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_upload_email_templates` | Executes `jira_server_upload_email_templates` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_apply_email_templates` | Executes `jira_server_apply_email_templates` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_revert_email_templates_to_default` | Executes `jira_server_revert_email_templates_to_default` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_email_types` | Executes `jira_server_get_email_types` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_default_share_scope` | Executes `jira_server_get_default_share_scope` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_default_share_scope` | Executes `jira_server_set_default_share_scope` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_default_columns_1` | Executes `jira_server_default_columns_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_columns_1` | Executes `jira_server_set_columns_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_reset_columns_1` | Executes `jira_server_reset_columns_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_issue` | Executes `jira_server_create_issue` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_archive_issues` | Executes `jira_server_archive_issues` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_issues` | Executes `jira_server_create_issues` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue_picker_resource` | Executes `jira_server_get_issue_picker_resource` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue_2` | Executes `jira_server_get_issue_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_edit_issue` | Executes `jira_server_edit_issue` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_issue` | Executes `jira_server_delete_issue` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_archive_issue` | Executes `jira_server_archive_issue` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_assign` | Executes `jira_server_assign` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_edit_issue_meta` | Executes `jira_server_get_edit_issue_meta` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_notify` | Executes `jira_server_notify` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue_properties_keys` | Executes `jira_server_get_issue_properties_keys` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_property_3` | Executes `jira_server_get_property_3` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_issue_property` | Executes `jira_server_set_issue_property` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_property_3` | Executes `jira_server_delete_property_3` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_restore_issue` | Executes `jira_server_restore_issue` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_link_issues` | Executes `jira_server_link_issues` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_reset_order` | Executes `jira_server_reset_order` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue_security_schemes` | Executes `jira_server_get_issue_security_schemes` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue_security_scheme` | Executes `jira_server_get_issue_security_scheme` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue_all_types` | Executes `jira_server_get_issue_all_types` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_avatar_from_temporary` | Executes `jira_server_create_avatar_from_temporary` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_store_temporary_avatar_using_multi_part` | Executes `jira_server_store_temporary_avatar_using_multi_part` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_property_keys` | Executes `jira_server_get_property_keys` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_property_4` | Executes `jira_server_get_property_4` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_property_3` | Executes `jira_server_set_property_3` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_property_4` | Executes `jira_server_delete_property_4` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_auto_complete` | Executes `jira_server_get_auto_complete` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_validate` | Executes `jira_server_validate` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_is_app_monitoring_enabled` | Executes `jira_server_is_app_monitoring_enabled` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_app_monitoring_enabled` | Executes `jira_server_set_app_monitoring_enabled` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_is_ipd_monitoring_enabled` | Executes `jira_server_is_ipd_monitoring_enabled` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_app_monitoring_enabled_1` | Executes `jira_server_set_app_monitoring_enabled_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_are_metrics_exposed` | Executes `jira_server_are_metrics_exposed` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_available_metrics` | Executes `jira_server_get_available_metrics` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_start` | Executes `jira_server_start` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_stop` | Executes `jira_server_stop` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_preference` | Executes `jira_server_get_preference` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_preference` | Executes `jira_server_set_preference` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_remove_preference` | Executes `jira_server_remove_preference` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_change_my_password` | Executes `jira_server_change_my_password` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_notification_schemes` | Executes `jira_server_get_notification_schemes` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_notification_scheme` | Executes `jira_server_get_notification_scheme` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_password_policy` | Executes `jira_server_get_password_policy` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_scheme_attribute` | Executes `jira_server_get_scheme_attribute` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_scheme_attribute` | Executes `jira_server_set_scheme_attribute` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_priorities` | Executes `jira_server_get_priorities` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_priorities_1` | Executes `jira_server_get_priorities_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_avatar_from_temporary_1` | Executes `jira_server_create_avatar_from_temporary_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_store_temporary_avatar_using_multi_part_1` | Executes `jira_server_store_temporary_avatar_using_multi_part_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_avatar` | Executes `jira_server_delete_avatar` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_all_avatars` | Executes `jira_server_get_all_avatars` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_properties_keys_3` | Executes `jira_server_get_properties_keys_3` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_property_5` | Executes `jira_server_get_property_5` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_property_4` | Executes `jira_server_set_property_4` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_property_5` | Executes `jira_server_delete_property_5` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_actors` | Executes `jira_server_set_actors` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_actor` | Executes `jira_server_delete_actor` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_all_statuses` | Executes `jira_server_get_all_statuses` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue_security_scheme_1` | Executes `jira_server_get_issue_security_scheme_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_notification_scheme_1` | Executes `jira_server_get_notification_scheme_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_process_requests` | Executes `jira_server_process_requests` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_progress_bulk` | Executes `jira_server_get_progress_bulk` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_progress` | Executes `jira_server_get_progress` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_update_show_when_empty_indicator` | Executes `jira_server_update_show_when_empty_indicator` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_error` | Executes `jira_server_get_error` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_max_aggregation_buckets` | Executes `jira_server_get_max_aggregation_buckets` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_max_result_window` | Executes `jira_server_get_max_result_window` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issuesecuritylevel` | Executes `jira_server_get_issuesecuritylevel` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_base_url` | Executes `jira_server_set_base_url` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_issue_navigator_default_columns` | Executes `jira_server_get_issue_navigator_default_columns` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_issue_navigator_default_columns_form` | Executes `jira_server_set_issue_navigator_default_columns_form` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_statuses` | Executes `jira_server_get_statuses` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_paginated_statuses` | Executes `jira_server_get_paginated_statuses` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_status` | Executes `jira_server_get_status` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_status_categories` | Executes `jira_server_get_status_categories` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_status_category` | Executes `jira_server_get_status_category` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_all_terminology_entries` | Executes `jira_server_get_all_terminology_entries` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_terminology_entries` | Executes `jira_server_set_terminology_entries` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_terminology_entry` | Executes `jira_server_get_terminology_entry` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_avatars` | Executes `jira_server_get_avatars` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_avatar_from_temporary_2` | Executes `jira_server_create_avatar_from_temporary_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_avatar_1` | Executes `jira_server_delete_avatar_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_store_temporary_avatar_using_multi_part_2` | Executes `jira_server_store_temporary_avatar_using_multi_part_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_a11y_personal_settings` | Executes `jira_server_get_a11y_personal_settings` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_progress_1` | Executes `jira_server_get_progress_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_unlock_anonymization` | Executes `jira_server_unlock_anonymization` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_avatar_from_temporary_3` | Executes `jira_server_create_avatar_from_temporary_3` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_store_temporary_avatar_using_multi_part_3` | Executes `jira_server_store_temporary_avatar_using_multi_part_3` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_avatar_2` | Executes `jira_server_delete_avatar_2` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_all_avatars_1` | Executes `jira_server_get_all_avatars_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_default_columns` | Executes `jira_server_default_columns` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_columns_url_encoded` | Executes `jira_server_set_columns_url_encoded` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_reset_columns` | Executes `jira_server_reset_columns` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_properties_keys_4` | Executes `jira_server_get_properties_keys_4` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_property_6` | Executes `jira_server_get_property_6` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_set_property_5` | Executes `jira_server_set_property_5` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_property_6` | Executes `jira_server_delete_property_6` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_session` | Executes `jira_server_delete_session` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_paginated_versions` | Executes `jira_server_get_paginated_versions` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_version` | Executes `jira_server_create_version` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_remote_version_links` | Executes `jira_server_get_remote_version_links` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_version` | Executes `jira_server_get_version` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_update_version` | Executes `jira_server_update_version` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_merge` | Executes `jira_server_merge` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_move_version` | Executes `jira_server_move_version` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_version_related_issues` | Executes `jira_server_get_version_related_issues` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_1` | Executes `jira_server_delete_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_version_unresolved_issues` | Executes `jira_server_get_version_unresolved_issues` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_remote_version_links_by_version_id` | Executes `jira_server_get_remote_version_links_by_version_id` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_or_update_remote_version_link` | Executes `jira_server_create_or_update_remote_version_link` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_remote_version_links_by_version_id` | Executes `jira_server_delete_remote_version_links_by_version_id` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_remote_version_link` | Executes `jira_server_get_remote_version_link` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_or_update_remote_version_link_1` | Executes `jira_server_create_or_update_remote_version_link_1` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_remote_version_link` | Executes `jira_server_delete_remote_version_link` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_scheme` | Executes `jira_server_create_scheme` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_by_id` | Executes `jira_server_get_by_id` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_update` | Executes `jira_server_update` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_scheme` | Executes `jira_server_delete_scheme` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_create_draft_for_parent` | Executes `jira_server_create_draft_for_parent` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_default` | Executes `jira_server_get_default` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_update_default` | Executes `jira_server_update_default` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_default` | Executes `jira_server_delete_default` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_draft_by_id` | Executes `jira_server_get_draft_by_id` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_update_draft` | Executes `jira_server_update_draft` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_draft_by_id` | Executes `jira_server_delete_draft_by_id` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_get_draft_default` | Executes `jira_server_get_draft_default` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_update_draft_default` | Executes `jira_server_update_draft_default` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_delete_draft_default` | Executes `jira_server_delete_draft_default` within the `jira-server-other` category. |
| `jira_server_jira_server_other` | `jira_server_release` | Executes `jira_server_release` within the `jira-server-other` category. |
| `jira_server_jira_server_agile_board` | `jira_server_get_all_boards` | Executes `jira_server_get_all_boards` within the `jira-server-agile-board` category. |
| `jira_server_jira_server_agile_board` | `jira_server_create_board` | Executes `jira_server_create_board` within the `jira-server-agile-board` category. |
| `jira_server_jira_server_agile_board` | `jira_server_get_board` | Executes `jira_server_get_board` within the `jira-server-agile-board` category. |
| `jira_server_jira_server_agile_board` | `jira_server_delete_board` | Executes `jira_server_delete_board` within the `jira-server-agile-board` category. |
| `jira_server_jira_server_agile_board` | `jira_server_get_issues_for_board` | Executes `jira_server_get_issues_for_board` within the `jira-server-agile-board` category. |
| `jira_server_jira_server_agile_board` | `jira_server_get_issue_estimation_for_board` | Executes `jira_server_get_issue_estimation_for_board` within the `jira-server-agile-board` category. |
| `jira_server_jira_server_agile_board` | `jira_server_estimate_issue_for_board` | Executes `jira_server_estimate_issue_for_board` within the `jira-server-agile-board` category. |
| `jira_server_jira_server_agile_board` | `jira_server_get_dashboard` | Executes `jira_server_get_dashboard` within the `jira-server-agile-board` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_get_epics` | Executes `jira_server_get_epics` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_get_issues_without_epic` | Executes `jira_server_get_issues_without_epic` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_get_issues_for_epic` | Executes `jira_server_get_issues_for_epic` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_get_issues_without_epic_1` | Executes `jira_server_get_issues_without_epic_1` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_remove_issues_from_epic` | Executes `jira_server_remove_issues_from_epic` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_get_epic` | Executes `jira_server_get_epic` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_partially_update_epic` | Executes `jira_server_partially_update_epic` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_get_issues_for_epic_1` | Executes `jira_server_get_issues_for_epic_1` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_move_issues_to_epic` | Executes `jira_server_move_issues_to_epic` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_agile_epic` | `jira_server_rank_epics` | Executes `jira_server_rank_epics` within the `jira-server-agile-epic` category. |
| `jira_server_jira_server_project` | `jira_server_get_projects` | Executes `jira_server_get_projects` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_associated_projects` | Executes `jira_server_get_associated_projects` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_set_project_associations_for_scheme` | Executes `jira_server_set_project_associations_for_scheme` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_add_project_associations_to_scheme` | Executes `jira_server_add_project_associations_to_scheme` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_remove_all_project_associations` | Executes `jira_server_remove_all_project_associations` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_remove_project_association` | Executes `jira_server_remove_project_association` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_all_projects` | Executes `jira_server_get_all_projects` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_create_project` | Executes `jira_server_create_project` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_all_project_types` | Executes `jira_server_get_all_project_types` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_project_type_by_key` | Executes `jira_server_get_project_type_by_key` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_accessible_project_type_by_key` | Executes `jira_server_get_accessible_project_type_by_key` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_project` | Executes `jira_server_get_project` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_update_project` | Executes `jira_server_update_project` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_delete_project` | Executes `jira_server_delete_project` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_archive_project` | Executes `jira_server_archive_project` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_restore_project` | Executes `jira_server_restore_project` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_update_project_type` | Executes `jira_server_update_project_type` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_project_versions_paginated` | Executes `jira_server_get_project_versions_paginated` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_project_versions` | Executes `jira_server_get_project_versions` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_security_levels_for_project` | Executes `jira_server_get_security_levels_for_project` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_workflow_scheme_for_project` | Executes `jira_server_get_workflow_scheme_for_project` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_all_project_categories` | Executes `jira_server_get_all_project_categories` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_search_for_projects` | Executes `jira_server_search_for_projects` within the `jira-server-project` category. |
| `jira_server_jira_server_project` | `jira_server_get_project_1` | Executes `jira_server_get_project_1` within the `jira-server-project` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_get_all_sprints` | Executes `jira_server_get_all_sprints` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_get_issues_for_sprint` | Executes `jira_server_get_issues_for_sprint` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_create_sprint` | Executes `jira_server_create_sprint` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_unmap_sprints` | Executes `jira_server_unmap_sprints` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_unmap_all_sprints` | Executes `jira_server_unmap_all_sprints` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_get_sprint` | Executes `jira_server_get_sprint` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_update_sprint` | Executes `jira_server_update_sprint` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_partially_update_sprint` | Executes `jira_server_partially_update_sprint` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_delete_sprint` | Executes `jira_server_delete_sprint` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_get_issues_for_sprint_1` | Executes `jira_server_get_issues_for_sprint_1` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_move_issues_to_sprint` | Executes `jira_server_move_issues_to_sprint` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_agile_sprint` | `jira_server_swap_sprint` | Executes `jira_server_swap_sprint` within the `jira-server-agile-sprint` category. |
| `jira_server_jira_server_screen` | `jira_server_set_property_via_restful_table` | Executes `jira_server_set_property_via_restful_table` within the `jira-server-screen` category. |
| `jira_server_jira_server_screen` | `jira_server_get_all_screens` | Executes `jira_server_get_all_screens` within the `jira-server-screen` category. |
| `jira_server_jira_server_screen` | `jira_server_add_field_to_default_screen` | Executes `jira_server_add_field_to_default_screen` within the `jira-server-screen` category. |
| `jira_server_jira_server_screen` | `jira_server_get_all_tabs` | Executes `jira_server_get_all_tabs` within the `jira-server-screen` category. |
| `jira_server_jira_server_screen` | `jira_server_add_tab` | Executes `jira_server_add_tab` within the `jira-server-screen` category. |
| `jira_server_jira_server_screen` | `jira_server_rename_tab` | Executes `jira_server_rename_tab` within the `jira-server-screen` category. |
| `jira_server_jira_server_screen` | `jira_server_delete_tab` | Executes `jira_server_delete_tab` within the `jira-server-screen` category. |
| `jira_server_jira_server_screen` | `jira_server_move_tab` | Executes `jira_server_move_tab` within the `jira-server-screen` category. |
| `jira_server_jira_server_issue_attachment` | `jira_server_get_attachment_meta` | Executes `jira_server_get_attachment_meta` within the `jira-server-issue-attachment` category. |
| `jira_server_jira_server_issue_attachment` | `jira_server_get_attachment` | Executes `jira_server_get_attachment` within the `jira-server-issue-attachment` category. |
| `jira_server_jira_server_issue_attachment` | `jira_server_remove_attachment` | Executes `jira_server_remove_attachment` within the `jira-server-issue-attachment` category. |
| `jira_server_jira_server_issue_attachment` | `jira_server_add_attachment` | Executes `jira_server_add_attachment` within the `jira-server-issue-attachment` category. |
| `jira_server_jira_server_system` | `jira_server_get_all_system_avatars` | Executes `jira_server_get_all_system_avatars` within the `jira-server-system` category. |
| `jira_server_jira_server_system` | `jira_server_get_server_info` | Executes `jira_server_get_server_info` within the `jira-server-system` category. |
| `jira_server_jira_server_system` | `jira_server_login` | Executes `jira_server_login` within the `jira-server-system` category. |
| `jira_server_jira_server_system` | `jira_server_logout` | Executes `jira_server_logout` within the `jira-server-system` category. |
| `jira_server_jira_server_admin_index` | `jira_server_request_current_index_from_node` | Executes `jira_server_request_current_index_from_node` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_index` | `jira_server_list_index_snapshot` | Executes `jira_server_list_index_snapshot` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_index` | `jira_server_create_index_snapshot` | Executes `jira_server_create_index_snapshot` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_index` | `jira_server_is_index_snapshot_running` | Executes `jira_server_is_index_snapshot_running` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_index` | `jira_server_get_index_summary` | Executes `jira_server_get_index_summary` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_index` | `jira_server_get_reindex_info` | Executes `jira_server_get_reindex_info` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_index` | `jira_server_reindex` | Executes `jira_server_reindex` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_index` | `jira_server_reindex_issues` | Executes `jira_server_reindex_issues` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_index` | `jira_server_get_reindex_progress` | Executes `jira_server_get_reindex_progress` within the `jira-server-admin-index` category. |
| `jira_server_jira_server_admin_upgrade` | `jira_server_approve_upgrade` | Executes `jira_server_approve_upgrade` within the `jira-server-admin-upgrade` category. |
| `jira_server_jira_server_admin_upgrade` | `jira_server_cancel_upgrade` | Executes `jira_server_cancel_upgrade` within the `jira-server-admin-upgrade` category. |
| `jira_server_jira_server_admin_upgrade` | `jira_server_set_ready_to_upgrade` | Executes `jira_server_set_ready_to_upgrade` within the `jira-server-admin-upgrade` category. |
| `jira_server_jira_server_admin_upgrade` | `jira_server_get_upgrade_result` | Executes `jira_server_get_upgrade_result` within the `jira-server-admin-upgrade` category. |
| `jira_server_jira_server_admin_upgrade` | `jira_server_run_upgrades_now` | Executes `jira_server_run_upgrades_now` within the `jira-server-admin-upgrade` category. |
| `jira_server_jira_server_field` | `jira_server_get_custom_field_option` | Executes `jira_server_get_custom_field_option` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_get_custom_fields` | Executes `jira_server_get_custom_fields` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_bulk_delete_custom_fields` | Executes `jira_server_bulk_delete_custom_fields` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_get_custom_field_options` | Executes `jira_server_get_custom_field_options` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_get_fields` | Executes `jira_server_get_fields` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_create_custom_field` | Executes `jira_server_create_custom_field` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_get_create_issue_meta_fields` | Executes `jira_server_get_create_issue_meta_fields` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_get_field_auto_complete_for_query_string` | Executes `jira_server_get_field_auto_complete_for_query_string` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_get_fields_to_add` | Executes `jira_server_get_fields_to_add` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_get_all_fields` | Executes `jira_server_get_all_fields` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_add_field` | Executes `jira_server_add_field` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_remove_field` | Executes `jira_server_remove_field` within the `jira-server-field` category. |
| `jira_server_jira_server_field` | `jira_server_move_field` | Executes `jira_server_move_field` within the `jira-server-field` category. |
| `jira_server_jira_server_filter` | `jira_server_create_filter` | Executes `jira_server_create_filter` within the `jira-server-filter` category. |
| `jira_server_jira_server_filter` | `jira_server_get_favourite_filters` | Executes `jira_server_get_favourite_filters` within the `jira-server-filter` category. |
| `jira_server_jira_server_filter` | `jira_server_get_filter` | Executes `jira_server_get_filter` within the `jira-server-filter` category. |
| `jira_server_jira_server_filter` | `jira_server_edit_filter` | Executes `jira_server_edit_filter` within the `jira-server-filter` category. |
| `jira_server_jira_server_filter` | `jira_server_delete_filter` | Executes `jira_server_delete_filter` within the `jira-server-filter` category. |
| `jira_server_jira_server_permission` | `jira_server_get_share_permissions` | Executes `jira_server_get_share_permissions` within the `jira-server-permission` category. |
| `jira_server_jira_server_permission` | `jira_server_add_share_permission` | Executes `jira_server_add_share_permission` within the `jira-server-permission` category. |
| `jira_server_jira_server_permission` | `jira_server_delete_share_permission` | Executes `jira_server_delete_share_permission` within the `jira-server-permission` category. |
| `jira_server_jira_server_permission` | `jira_server_get_share_permission` | Executes `jira_server_get_share_permission` within the `jira-server-permission` category. |
| `jira_server_jira_server_permission` | `jira_server_get_permissions` | Executes `jira_server_get_permissions` within the `jira-server-permission` category. |
| `jira_server_jira_server_permission` | `jira_server_get_all_permissions` | Executes `jira_server_get_all_permissions` within the `jira-server-permission` category. |
| `jira_server_jira_server_permission` | `jira_server_create_permission_grant` | Executes `jira_server_create_permission_grant` within the `jira-server-permission` category. |
| `jira_server_jira_server_group` | `jira_server_create_group` | Executes `jira_server_create_group` within the `jira-server-group` category. |
| `jira_server_jira_server_group` | `jira_server_remove_group` | Executes `jira_server_remove_group` within the `jira-server-group` category. |
| `jira_server_jira_server_group` | `jira_server_find_groups` | Executes `jira_server_find_groups` within the `jira-server-group` category. |
| `jira_server_jira_server_user` | `jira_server_get_users_from_group` | Executes `jira_server_get_users_from_group` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_add_user_to_group` | Executes `jira_server_add_user_to_group` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_remove_user_from_group` | Executes `jira_server_remove_user_from_group` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_find_users_and_groups` | Executes `jira_server_find_users_and_groups` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_get_user` | Executes `jira_server_get_user` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_update_user` | Executes `jira_server_update_user` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_policy_check_create_user` | Executes `jira_server_policy_check_create_user` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_policy_check_update_user` | Executes `jira_server_policy_check_update_user` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_add_actor_users` | Executes `jira_server_add_actor_users` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_get_user_1` | Executes `jira_server_get_user_1` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_update_user_1` | Executes `jira_server_update_user_1` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_create_user` | Executes `jira_server_create_user` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_remove_user` | Executes `jira_server_remove_user` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_validate_user_anonymization` | Executes `jira_server_validate_user_anonymization` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_schedule_user_anonymization` | Executes `jira_server_schedule_user_anonymization` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_validate_user_anonymization_rerun` | Executes `jira_server_validate_user_anonymization_rerun` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_schedule_user_anonymization_rerun` | Executes `jira_server_schedule_user_anonymization_rerun` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_add_user_to_application_1` | Executes `jira_server_add_user_to_application_1` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_remove_user_from_application_1` | Executes `jira_server_remove_user_from_application_1` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_find_bulk_assignable_users` | Executes `jira_server_find_bulk_assignable_users` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_find_assignable_users_1` | Executes `jira_server_find_assignable_users_1` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_get_duplicated_users_count` | Executes `jira_server_get_duplicated_users_count` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_get_duplicated_users_mapping` | Executes `jira_server_get_duplicated_users_mapping` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_get_user_list` | Executes `jira_server_get_user_list` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_change_user_password` | Executes `jira_server_change_user_password` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_find_users_with_all_permissions` | Executes `jira_server_find_users_with_all_permissions` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_find_users_for_picker` | Executes `jira_server_find_users_for_picker` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_find_users` | Executes `jira_server_find_users` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_find_users_with_browse_permission` | Executes `jira_server_find_users_with_browse_permission` within the `jira-server-user` category. |
| `jira_server_jira_server_user` | `jira_server_current_user` | Executes `jira_server_current_user` within the `jira-server-user` category. |
| `jira_server_jira_server_issue_type` | `jira_server_get_create_issue_meta_project_issue_types` | Executes `jira_server_get_create_issue_meta_project_issue_types` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_create_issue_type` | Executes `jira_server_create_issue_type` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_get_paginated_issue_types` | Executes `jira_server_get_paginated_issue_types` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_get_issue_type_1` | Executes `jira_server_get_issue_type_1` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_update_issue_type` | Executes `jira_server_update_issue_type` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_delete_issue_type_1` | Executes `jira_server_delete_issue_type_1` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_get_alternative_issue_types` | Executes `jira_server_get_alternative_issue_types` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_get_draft_issue_type` | Executes `jira_server_get_draft_issue_type` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_set_draft_issue_type` | Executes `jira_server_set_draft_issue_type` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_delete_draft_issue_type` | Executes `jira_server_delete_draft_issue_type` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_get_issue_type` | Executes `jira_server_get_issue_type` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_set_issue_type` | Executes `jira_server_set_issue_type` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_type` | `jira_server_delete_issue_type` | Executes `jira_server_delete_issue_type` within the `jira-server-issue-type` category. |
| `jira_server_jira_server_issue_link` | `jira_server_create_reciprocal_remote_issue_link` | Executes `jira_server_create_reciprocal_remote_issue_link` within the `jira-server-issue-link` category. |
| `jira_server_jira_server_issue_link` | `jira_server_get_remote_issue_links` | Executes `jira_server_get_remote_issue_links` within the `jira-server-issue-link` category. |
| `jira_server_jira_server_issue_link` | `jira_server_create_or_update_remote_issue_link` | Executes `jira_server_create_or_update_remote_issue_link` within the `jira-server-issue-link` category. |
| `jira_server_jira_server_issue_link` | `jira_server_delete_remote_issue_link_by_global_id` | Executes `jira_server_delete_remote_issue_link_by_global_id` within the `jira-server-issue-link` category. |
| `jira_server_jira_server_issue_link` | `jira_server_get_remote_issue_link_by_id` | Executes `jira_server_get_remote_issue_link_by_id` within the `jira-server-issue-link` category. |
| `jira_server_jira_server_issue_link` | `jira_server_update_remote_issue_link` | Executes `jira_server_update_remote_issue_link` within the `jira-server-issue-link` category. |
| `jira_server_jira_server_issue_link` | `jira_server_delete_remote_issue_link_by_id` | Executes `jira_server_delete_remote_issue_link_by_id` within the `jira-server-issue-link` category. |
| `jira_server_jira_server_issue_comment` | `jira_server_get_comments` | Executes `jira_server_get_comments` within the `jira-server-issue-comment` category. |
| `jira_server_jira_server_issue_comment` | `jira_server_add_comment` | Executes `jira_server_add_comment` within the `jira-server-issue-comment` category. |
| `jira_server_jira_server_issue_comment` | `jira_server_get_comment` | Executes `jira_server_get_comment` within the `jira-server-issue-comment` category. |
| `jira_server_jira_server_issue_comment` | `jira_server_update_comment` | Executes `jira_server_update_comment` within the `jira-server-issue-comment` category. |
| `jira_server_jira_server_issue_comment` | `jira_server_delete_comment` | Executes `jira_server_delete_comment` within the `jira-server-issue-comment` category. |
| `jira_server_jira_server_issue_comment` | `jira_server_set_pin_comment` | Executes `jira_server_set_pin_comment` within the `jira-server-issue-comment` category. |
| `jira_server_jira_server_issue_comment` | `jira_server_get_pinned_comments` | Executes `jira_server_get_pinned_comments` within the `jira-server-issue-comment` category. |
| `jira_server_jira_server_issue_subtask` | `jira_server_get_sub_tasks` | Executes `jira_server_get_sub_tasks` within the `jira-server-issue-subtask` category. |
| `jira_server_jira_server_issue_subtask` | `jira_server_can_move_sub_task` | Executes `jira_server_can_move_sub_task` within the `jira-server-issue-subtask` category. |
| `jira_server_jira_server_issue_subtask` | `jira_server_move_sub_tasks` | Executes `jira_server_move_sub_tasks` within the `jira-server-issue-subtask` category. |
| `jira_server_jira_server_issue_transition` | `jira_server_get_transitions` | Executes `jira_server_get_transitions` within the `jira-server-issue-transition` category. |
| `jira_server_jira_server_issue_transition` | `jira_server_do_transition` | Executes `jira_server_do_transition` within the `jira-server-issue-transition` category. |
| `jira_server_jira_server_issue_vote` | `jira_server_get_votes` | Executes `jira_server_get_votes` within the `jira-server-issue-vote` category. |
| `jira_server_jira_server_issue_vote` | `jira_server_add_vote` | Executes `jira_server_add_vote` within the `jira-server-issue-vote` category. |
| `jira_server_jira_server_issue_vote` | `jira_server_remove_vote` | Executes `jira_server_remove_vote` within the `jira-server-issue-vote` category. |
| `jira_server_jira_server_issue_watcher` | `jira_server_get_issue_watchers` | Executes `jira_server_get_issue_watchers` within the `jira-server-issue-watcher` category. |
| `jira_server_jira_server_issue_watcher` | `jira_server_add_watcher_1` | Executes `jira_server_add_watcher_1` within the `jira-server-issue-watcher` category. |
| `jira_server_jira_server_issue_watcher` | `jira_server_remove_watcher_1` | Executes `jira_server_remove_watcher_1` within the `jira-server-issue-watcher` category. |
| `jira_server_jira_server_issue_worklog` | `jira_server_get_issue_worklog` | Executes `jira_server_get_issue_worklog` within the `jira-server-issue-worklog` category. |
| `jira_server_jira_server_issue_worklog` | `jira_server_add_worklog` | Executes `jira_server_add_worklog` within the `jira-server-issue-worklog` category. |
| `jira_server_jira_server_issue_worklog` | `jira_server_get_worklog` | Executes `jira_server_get_worklog` within the `jira-server-issue-worklog` category. |
| `jira_server_jira_server_issue_worklog` | `jira_server_update_worklog` | Executes `jira_server_update_worklog` within the `jira-server-issue-worklog` category. |
| `jira_server_jira_server_issue_worklog` | `jira_server_delete_worklog` | Executes `jira_server_delete_worklog` within the `jira-server-issue-worklog` category. |
| `jira_server_jira_server_issue_worklog` | `jira_server_get_ids_of_worklogs_deleted_since` | Executes `jira_server_get_ids_of_worklogs_deleted_since` within the `jira-server-issue-worklog` category. |
| `jira_server_jira_server_issue_worklog` | `jira_server_get_worklogs_for_ids` | Executes `jira_server_get_worklogs_for_ids` within the `jira-server-issue-worklog` category. |
| `jira_server_jira_server_issue_worklog` | `jira_server_get_ids_of_worklogs_modified_since` | Executes `jira_server_get_ids_of_worklogs_modified_since` within the `jira-server-issue-worklog` category. |
| `jira_server_jira_server_issue_link_type` | `jira_server_get_issue_link` | Executes `jira_server_get_issue_link` within the `jira-server-issue-link-type` category. |
| `jira_server_jira_server_issue_link_type` | `jira_server_delete_issue_link` | Executes `jira_server_delete_issue_link` within the `jira-server-issue-link-type` category. |
| `jira_server_jira_server_issue_link_type` | `jira_server_get_issue_link_types` | Executes `jira_server_get_issue_link_types` within the `jira-server-issue-link-type` category. |
| `jira_server_jira_server_issue_link_type` | `jira_server_create_issue_link_type` | Executes `jira_server_create_issue_link_type` within the `jira-server-issue-link-type` category. |
| `jira_server_jira_server_issue_link_type` | `jira_server_get_issue_link_type` | Executes `jira_server_get_issue_link_type` within the `jira-server-issue-link-type` category. |
| `jira_server_jira_server_issue_link_type` | `jira_server_update_issue_link_type` | Executes `jira_server_update_issue_link_type` within the `jira-server-issue-link-type` category. |
| `jira_server_jira_server_issue_link_type` | `jira_server_delete_issue_link_type` | Executes `jira_server_delete_issue_link_type` within the `jira-server-issue-link-type` category. |
| `jira_server_jira_server_issue_link_type` | `jira_server_move_issue_link_type` | Executes `jira_server_move_issue_link_type` within the `jira-server-issue-link-type` category. |
| `jira_server_jira_server_issue_type_scheme` | `jira_server_get_all_issue_type_schemes` | Executes `jira_server_get_all_issue_type_schemes` within the `jira-server-issue-type-scheme` category. |
| `jira_server_jira_server_issue_type_scheme` | `jira_server_create_issue_type_scheme` | Executes `jira_server_create_issue_type_scheme` within the `jira-server-issue-type-scheme` category. |
| `jira_server_jira_server_issue_type_scheme` | `jira_server_get_issue_type_scheme` | Executes `jira_server_get_issue_type_scheme` within the `jira-server-issue-type-scheme` category. |
| `jira_server_jira_server_issue_type_scheme` | `jira_server_update_issue_type_scheme` | Executes `jira_server_update_issue_type_scheme` within the `jira-server-issue-type-scheme` category. |
| `jira_server_jira_server_issue_type_scheme` | `jira_server_delete_issue_type_scheme` | Executes `jira_server_delete_issue_type_scheme` within the `jira-server-issue-type-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_get_permission_schemes` | Executes `jira_server_get_permission_schemes` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_create_permission_scheme` | Executes `jira_server_create_permission_scheme` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_get_permission_scheme` | Executes `jira_server_get_permission_scheme` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_update_permission_scheme` | Executes `jira_server_update_permission_scheme` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_delete_permission_scheme` | Executes `jira_server_delete_permission_scheme` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_get_permission_scheme_grants` | Executes `jira_server_get_permission_scheme_grants` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_get_permission_scheme_grant` | Executes `jira_server_get_permission_scheme_grant` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_delete_permission_scheme_entity` | Executes `jira_server_delete_permission_scheme_entity` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_get_assigned_permission_scheme` | Executes `jira_server_get_assigned_permission_scheme` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_permission_scheme` | `jira_server_assign_permission_scheme` | Executes `jira_server_assign_permission_scheme` within the `jira-server-permission-scheme` category. |
| `jira_server_jira_server_priority` | `jira_server_get_priority` | Executes `jira_server_get_priority` within the `jira-server-priority` category. |
| `jira_server_jira_server_priority_scheme` | `jira_server_get_priority_schemes` | Executes `jira_server_get_priority_schemes` within the `jira-server-priority-scheme` category. |
| `jira_server_jira_server_priority_scheme` | `jira_server_create_priority_scheme` | Executes `jira_server_create_priority_scheme` within the `jira-server-priority-scheme` category. |
| `jira_server_jira_server_priority_scheme` | `jira_server_get_priority_scheme` | Executes `jira_server_get_priority_scheme` within the `jira-server-priority-scheme` category. |
| `jira_server_jira_server_priority_scheme` | `jira_server_update_priority_scheme` | Executes `jira_server_update_priority_scheme` within the `jira-server-priority-scheme` category. |
| `jira_server_jira_server_priority_scheme` | `jira_server_delete_priority_scheme` | Executes `jira_server_delete_priority_scheme` within the `jira-server-priority-scheme` category. |
| `jira_server_jira_server_priority_scheme` | `jira_server_get_assigned_priority_scheme` | Executes `jira_server_get_assigned_priority_scheme` within the `jira-server-priority-scheme` category. |
| `jira_server_jira_server_priority_scheme` | `jira_server_assign_priority_scheme` | Executes `jira_server_assign_priority_scheme` within the `jira-server-priority-scheme` category. |
| `jira_server_jira_server_priority_scheme` | `jira_server_unassign_priority_scheme` | Executes `jira_server_unassign_priority_scheme` within the `jira-server-priority-scheme` category. |
| `jira_server_jira_server_project_avatar` | `jira_server_update_project_avatar` | Executes `jira_server_update_project_avatar` within the `jira-server-project-avatar` category. |
| `jira_server_jira_server_project_component` | `jira_server_get_project_components` | Executes `jira_server_get_project_components` within the `jira-server-project-component` category. |
| `jira_server_jira_server_project_role` | `jira_server_get_project_roles` | Executes `jira_server_get_project_roles` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_get_project_role` | Executes `jira_server_get_project_role` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_get_project_roles_1` | Executes `jira_server_get_project_roles_1` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_create_project_role` | Executes `jira_server_create_project_role` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_get_project_roles_by_id` | Executes `jira_server_get_project_roles_by_id` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_fully_update_project_role` | Executes `jira_server_fully_update_project_role` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_partial_update_project_role` | Executes `jira_server_partial_update_project_role` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_delete_project_role` | Executes `jira_server_delete_project_role` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_get_project_role_actors_for_role` | Executes `jira_server_get_project_role_actors_for_role` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_add_project_role_actors_to_role` | Executes `jira_server_add_project_role_actors_to_role` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_role` | `jira_server_delete_project_role_actors_from_role` | Executes `jira_server_delete_project_role_actors_from_role` within the `jira-server-project-role` category. |
| `jira_server_jira_server_project_category` | `jira_server_create_project_category` | Executes `jira_server_create_project_category` within the `jira-server-project-category` category. |
| `jira_server_jira_server_project_category` | `jira_server_get_project_category_by_id` | Executes `jira_server_get_project_category_by_id` within the `jira-server-project-category` category. |
| `jira_server_jira_server_project_category` | `jira_server_update_project_category` | Executes `jira_server_update_project_category` within the `jira-server-project-category` category. |
| `jira_server_jira_server_project_category` | `jira_server_remove_project_category` | Executes `jira_server_remove_project_category` within the `jira-server-project-category` category. |
| `jira_server_jira_server_resolution` | `jira_server_get_resolutions` | Executes `jira_server_get_resolutions` within the `jira-server-resolution` category. |
| `jira_server_jira_server_resolution` | `jira_server_get_paginated_resolutions` | Executes `jira_server_get_paginated_resolutions` within the `jira-server-resolution` category. |
| `jira_server_jira_server_resolution` | `jira_server_get_resolution` | Executes `jira_server_get_resolution` within the `jira-server-resolution` category. |
| `jira_server_jira_server_search` | `jira_server_search_1` | Executes `jira_server_search_1` within the `jira-server-search` category. |
| `jira_server_jira_server_search` | `jira_server_search_using_search_request` | Executes `jira_server_search_using_search_request` within the `jira-server-search` category. |
| `jira_server_jira_server_user_avatar` | `jira_server_update_user_avatar_1` | Executes `jira_server_update_user_avatar_1` within the `jira-server-user-avatar` category. |
| `jira_server_jira_server_workflow` | `jira_server_get_all_workflows` | Executes `jira_server_get_all_workflows` within the `jira-server-workflow` category. |
| `jira_server_jira_server_workflow` | `jira_server_get_draft_workflow` | Executes `jira_server_get_draft_workflow` within the `jira-server-workflow` category. |
| `jira_server_jira_server_workflow` | `jira_server_update_draft_workflow_mapping` | Executes `jira_server_update_draft_workflow_mapping` within the `jira-server-workflow` category. |
| `jira_server_jira_server_workflow` | `jira_server_delete_draft_workflow_mapping` | Executes `jira_server_delete_draft_workflow_mapping` within the `jira-server-workflow` category. |
| `jira_server_jira_server_workflow` | `jira_server_get_workflow` | Executes `jira_server_get_workflow` within the `jira-server-workflow` category. |
| `jira_server_jira_server_workflow` | `jira_server_update_workflow_mapping` | Executes `jira_server_update_workflow_mapping` within the `jira-server-workflow` category. |
| `jira_server_jira_server_workflow` | `jira_server_delete_workflow_mapping` | Executes `jira_server_delete_workflow_mapping` within the `jira-server-workflow` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_all_application_roles` | Executes `jira_cloud_get_all_application_roles` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_application_role` | Executes `jira_cloud_get_application_role` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_all_user_data_classification_levels` | Executes `jira_cloud_get_all_user_data_classification_levels` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_share_permissions` | Executes `jira_cloud_get_share_permissions` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_add_share_permission` | Executes `jira_cloud_add_share_permission` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_delete_share_permission` | Executes `jira_cloud_delete_share_permission` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_share_permission` | Executes `jira_cloud_get_share_permission` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_remove_group` | Executes `jira_cloud_remove_group` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_group` | Executes `jira_cloud_get_group` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_create_group` | Executes `jira_cloud_create_group` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_users_from_group` | Executes `jira_cloud_get_users_from_group` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_remove_user_from_group` | Executes `jira_cloud_remove_user_from_group` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_add_user_to_group` | Executes `jira_cloud_add_user_to_group` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_groups` | Executes `jira_cloud_find_groups` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_users_and_groups` | Executes `jira_cloud_find_users_and_groups` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_my_permissions` | Executes `jira_cloud_get_my_permissions` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_current_user` | Executes `jira_cloud_get_current_user` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_all_permissions` | Executes `jira_cloud_get_all_permissions` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_all_permission_schemes` | Executes `jira_cloud_get_all_permission_schemes` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_create_permission_scheme` | Executes `jira_cloud_create_permission_scheme` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_delete_permission_scheme` | Executes `jira_cloud_delete_permission_scheme` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_permission_scheme` | Executes `jira_cloud_get_permission_scheme` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_update_permission_scheme` | Executes `jira_cloud_update_permission_scheme` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_permission_scheme_grants` | Executes `jira_cloud_get_permission_scheme_grants` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_create_permission_grant` | Executes `jira_cloud_create_permission_grant` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_delete_permission_scheme_entity` | Executes `jira_cloud_delete_permission_scheme_entity` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_permission_scheme_grant` | Executes `jira_cloud_get_permission_scheme_grant` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_add_actor_users` | Executes `jira_cloud_add_actor_users` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_assigned_permission_scheme` | Executes `jira_cloud_get_assigned_permission_scheme` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_assign_permission_scheme` | Executes `jira_cloud_assign_permission_scheme` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_remove_user` | Executes `jira_cloud_remove_user` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_user` | Executes `jira_cloud_get_user` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_create_user` | Executes `jira_cloud_create_user` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_assignable_users` | Executes `jira_cloud_find_assignable_users` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_reset_user_columns` | Executes `jira_cloud_reset_user_columns` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_user_default_columns` | Executes `jira_cloud_get_user_default_columns` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_set_user_columns` | Executes `jira_cloud_set_user_columns` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_user_email` | Executes `jira_cloud_get_user_email` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_user_groups` | Executes `jira_cloud_get_user_groups` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_users_with_all_permissions` | Executes `jira_cloud_find_users_with_all_permissions` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_users_for_picker` | Executes `jira_cloud_find_users_for_picker` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_user_property_keys` | Executes `jira_cloud_get_user_property_keys` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_delete_user_property` | Executes `jira_cloud_delete_user_property` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_user_property` | Executes `jira_cloud_get_user_property` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_set_user_property` | Executes `jira_cloud_set_user_property` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_users` | Executes `jira_cloud_find_users` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_users_by_query` | Executes `jira_cloud_find_users_by_query` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_user_keys_by_query` | Executes `jira_cloud_find_user_keys_by_query` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_find_users_with_browse_permission` | Executes `jira_cloud_find_users_with_browse_permission` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_all_users_default` | Executes `jira_cloud_get_all_users_default` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_user` | `jira_cloud_get_all_users` | Executes `jira_cloud_get_all_users` within the `jira-cloud-user` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_custom_fields_configurations` | Executes `jira_cloud_get_custom_fields_configurations` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_update_multiple_custom_field_values` | Executes `jira_cloud_update_multiple_custom_field_values` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_update_custom_field_value` | Executes `jira_cloud_update_custom_field_value` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_field_association_schemes` | Executes `jira_cloud_get_field_association_schemes` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_create_field_association_scheme` | Executes `jira_cloud_create_field_association_scheme` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_remove_fields_associated_with_schemes` | Executes `jira_cloud_remove_fields_associated_with_schemes` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_update_fields_associated_with_schemes` | Executes `jira_cloud_update_fields_associated_with_schemes` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_delete_field_association_scheme` | Executes `jira_cloud_delete_field_association_scheme` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_field_association_scheme_by_id` | Executes `jira_cloud_get_field_association_scheme_by_id` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_update_field_association_scheme` | Executes `jira_cloud_update_field_association_scheme` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_clone_field_association_scheme` | Executes `jira_cloud_clone_field_association_scheme` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_search_field_association_scheme_fields` | Executes `jira_cloud_search_field_association_scheme_fields` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_field_association_scheme_item_parameters` | Executes `jira_cloud_get_field_association_scheme_item_parameters` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_fields` | Executes `jira_cloud_get_fields` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_create_custom_field` | Executes `jira_cloud_create_custom_field` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_fields_paginated` | Executes `jira_cloud_get_fields_paginated` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_trashed_fields_paginated` | Executes `jira_cloud_get_trashed_fields_paginated` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_update_custom_field` | Executes `jira_cloud_update_custom_field` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_contexts_for_field` | Executes `jira_cloud_get_contexts_for_field` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_contexts_for_field_deprecated` | Executes `jira_cloud_get_contexts_for_field_deprecated` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_delete_custom_field` | Executes `jira_cloud_delete_custom_field` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_restore_custom_field` | Executes `jira_cloud_restore_custom_field` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_trash_custom_field` | Executes `jira_cloud_trash_custom_field` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field` | `jira_cloud_get_field_auto_complete_for_query_string` | Executes `jira_cloud_get_field_auto_complete_for_query_string` within the `jira-cloud-schema-field` category. |
| `jira_cloud_jira_cloud_schema_field_configuration` | `jira_cloud_get_custom_field_configuration` | Executes `jira_cloud_get_custom_field_configuration` within the `jira-cloud-schema-field-configuration` category. |
| `jira_cloud_jira_cloud_schema_field_configuration` | `jira_cloud_update_custom_field_configuration` | Executes `jira_cloud_update_custom_field_configuration` within the `jira-cloud-schema-field-configuration` category. |
| `jira_cloud_jira_cloud_schema_field_configuration` | `jira_cloud_get_all_field_configurations` | Executes `jira_cloud_get_all_field_configurations` within the `jira-cloud-schema-field-configuration` category. |
| `jira_cloud_jira_cloud_schema_field_configuration` | `jira_cloud_create_field_configuration` | Executes `jira_cloud_create_field_configuration` within the `jira-cloud-schema-field-configuration` category. |
| `jira_cloud_jira_cloud_schema_field_configuration` | `jira_cloud_delete_field_configuration` | Executes `jira_cloud_delete_field_configuration` within the `jira-cloud-schema-field-configuration` category. |
| `jira_cloud_jira_cloud_schema_field_configuration` | `jira_cloud_update_field_configuration` | Executes `jira_cloud_update_field_configuration` within the `jira-cloud-schema-field-configuration` category. |
| `jira_cloud_jira_cloud_schema_field_configuration` | `jira_cloud_get_field_configuration_items` | Executes `jira_cloud_get_field_configuration_items` within the `jira-cloud-schema-field-configuration` category. |
| `jira_cloud_jira_cloud_schema_field_configuration` | `jira_cloud_update_field_configuration_items` | Executes `jira_cloud_update_field_configuration_items` within the `jira-cloud-schema-field-configuration` category. |
| `jira_cloud_jira_cloud_schema_field_option` | `jira_cloud_get_custom_field_option` | Executes `jira_cloud_get_custom_field_option` within the `jira-cloud-schema-field-option` category. |
| `jira_cloud_jira_cloud_schema_field_option` | `jira_cloud_create_custom_field_option` | Executes `jira_cloud_create_custom_field_option` within the `jira-cloud-schema-field-option` category. |
| `jira_cloud_jira_cloud_schema_field_option` | `jira_cloud_update_custom_field_option` | Executes `jira_cloud_update_custom_field_option` within the `jira-cloud-schema-field-option` category. |
| `jira_cloud_jira_cloud_schema_field_option` | `jira_cloud_reorder_custom_field_options` | Executes `jira_cloud_reorder_custom_field_options` within the `jira-cloud-schema-field-option` category. |
| `jira_cloud_jira_cloud_schema_field_option` | `jira_cloud_delete_custom_field_option` | Executes `jira_cloud_delete_custom_field_option` within the `jira-cloud-schema-field-option` category. |
| `jira_cloud_jira_cloud_schema_field_option` | `jira_cloud_replace_custom_field_option` | Executes `jira_cloud_replace_custom_field_option` within the `jira-cloud-schema-field-option` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_get_all_dashboards` | Executes `jira_cloud_get_all_dashboards` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_create_dashboard` | Executes `jira_cloud_create_dashboard` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_get_all_available_dashboard_gadgets` | Executes `jira_cloud_get_all_available_dashboard_gadgets` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_get_dashboards_paginated` | Executes `jira_cloud_get_dashboards_paginated` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_get_dashboard_item_property_keys` | Executes `jira_cloud_get_dashboard_item_property_keys` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_delete_dashboard_item_property` | Executes `jira_cloud_delete_dashboard_item_property` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_get_dashboard_item_property` | Executes `jira_cloud_get_dashboard_item_property` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_set_dashboard_item_property` | Executes `jira_cloud_set_dashboard_item_property` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_delete_dashboard` | Executes `jira_cloud_delete_dashboard` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_get_dashboard` | Executes `jira_cloud_get_dashboard` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_update_dashboard` | Executes `jira_cloud_update_dashboard` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_copy_dashboard` | Executes `jira_cloud_copy_dashboard` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_search_security_schemes` | Executes `jira_cloud_search_security_schemes` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_delete_security_scheme` | Executes `jira_cloud_delete_security_scheme` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_get_avatar_image_by_type` | Executes `jira_cloud_get_avatar_image_by_type` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_other` | `jira_cloud_update_schemes` | Executes `jira_cloud_update_schemes` within the `jira-cloud-schema-other` category. |
| `jira_cloud_jira_cloud_schema_field_context` | `jira_cloud_create_custom_field_context` | Executes `jira_cloud_create_custom_field_context` within the `jira-cloud-schema-field-context` category. |
| `jira_cloud_jira_cloud_schema_field_context` | `jira_cloud_delete_custom_field_context` | Executes `jira_cloud_delete_custom_field_context` within the `jira-cloud-schema-field-context` category. |
| `jira_cloud_jira_cloud_schema_field_context` | `jira_cloud_update_custom_field_context` | Executes `jira_cloud_update_custom_field_context` within the `jira-cloud-schema-field-context` category. |
| `jira_cloud_jira_cloud_schema_screen` | `jira_cloud_get_screens_for_field` | Executes `jira_cloud_get_screens_for_field` within the `jira-cloud-schema-screen` category. |
| `jira_cloud_jira_cloud_schema_screen` | `jira_cloud_get_screens` | Executes `jira_cloud_get_screens` within the `jira-cloud-schema-screen` category. |
| `jira_cloud_jira_cloud_schema_screen` | `jira_cloud_create_screen` | Executes `jira_cloud_create_screen` within the `jira-cloud-schema-screen` category. |
| `jira_cloud_jira_cloud_schema_screen` | `jira_cloud_add_field_to_default_screen` | Executes `jira_cloud_add_field_to_default_screen` within the `jira-cloud-schema-screen` category. |
| `jira_cloud_jira_cloud_schema_screen` | `jira_cloud_delete_screen` | Executes `jira_cloud_delete_screen` within the `jira-cloud-schema-screen` category. |
| `jira_cloud_jira_cloud_schema_screen` | `jira_cloud_update_screen` | Executes `jira_cloud_update_screen` within the `jira-cloud-schema-screen` category. |
| `jira_cloud_jira_cloud_schema_screen` | `jira_cloud_get_available_screen_fields` | Executes `jira_cloud_get_available_screen_fields` within the `jira-cloud-schema-screen` category. |
| `jira_cloud_jira_cloud_schema_field_configuration_scheme` | `jira_cloud_get_all_field_configuration_schemes` | Executes `jira_cloud_get_all_field_configuration_schemes` within the `jira-cloud-schema-field-configuration-scheme` category. |
| `jira_cloud_jira_cloud_schema_field_configuration_scheme` | `jira_cloud_create_field_configuration_scheme` | Executes `jira_cloud_create_field_configuration_scheme` within the `jira-cloud-schema-field-configuration-scheme` category. |
| `jira_cloud_jira_cloud_schema_field_configuration_scheme` | `jira_cloud_get_field_configuration_scheme_mappings` | Executes `jira_cloud_get_field_configuration_scheme_mappings` within the `jira-cloud-schema-field-configuration-scheme` category. |
| `jira_cloud_jira_cloud_schema_field_configuration_scheme` | `jira_cloud_delete_field_configuration_scheme` | Executes `jira_cloud_delete_field_configuration_scheme` within the `jira-cloud-schema-field-configuration-scheme` category. |
| `jira_cloud_jira_cloud_schema_field_configuration_scheme` | `jira_cloud_update_field_configuration_scheme` | Executes `jira_cloud_update_field_configuration_scheme` within the `jira-cloud-schema-field-configuration-scheme` category. |
| `jira_cloud_jira_cloud_schema_field_configuration_scheme` | `jira_cloud_set_field_configuration_scheme_mapping` | Executes `jira_cloud_set_field_configuration_scheme_mapping` within the `jira-cloud-schema-field-configuration-scheme` category. |
| `jira_cloud_jira_cloud_schema_screen_scheme` | `jira_cloud_update_default_screen_scheme` | Executes `jira_cloud_update_default_screen_scheme` within the `jira-cloud-schema-screen-scheme` category. |
| `jira_cloud_jira_cloud_schema_screen_scheme` | `jira_cloud_get_screen_schemes` | Executes `jira_cloud_get_screen_schemes` within the `jira-cloud-schema-screen-scheme` category. |
| `jira_cloud_jira_cloud_schema_screen_scheme` | `jira_cloud_create_screen_scheme` | Executes `jira_cloud_create_screen_scheme` within the `jira-cloud-schema-screen-scheme` category. |
| `jira_cloud_jira_cloud_schema_screen_scheme` | `jira_cloud_delete_screen_scheme` | Executes `jira_cloud_delete_screen_scheme` within the `jira-cloud-schema-screen-scheme` category. |
| `jira_cloud_jira_cloud_schema_screen_scheme` | `jira_cloud_update_screen_scheme` | Executes `jira_cloud_update_screen_scheme` within the `jira-cloud-schema-screen-scheme` category. |
| `jira_cloud_jira_cloud_schema_notification_scheme` | `jira_cloud_get_notification_schemes` | Executes `jira_cloud_get_notification_schemes` within the `jira-cloud-schema-notification-scheme` category. |
| `jira_cloud_jira_cloud_schema_notification_scheme` | `jira_cloud_create_notification_scheme` | Executes `jira_cloud_create_notification_scheme` within the `jira-cloud-schema-notification-scheme` category. |
| `jira_cloud_jira_cloud_schema_notification_scheme` | `jira_cloud_get_notification_scheme` | Executes `jira_cloud_get_notification_scheme` within the `jira-cloud-schema-notification-scheme` category. |
| `jira_cloud_jira_cloud_schema_notification_scheme` | `jira_cloud_update_notification_scheme` | Executes `jira_cloud_update_notification_scheme` within the `jira-cloud-schema-notification-scheme` category. |
| `jira_cloud_jira_cloud_schema_notification_scheme` | `jira_cloud_delete_notification_scheme` | Executes `jira_cloud_delete_notification_scheme` within the `jira-cloud-schema-notification-scheme` category. |
| `jira_cloud_jira_cloud_schema_notification_scheme` | `jira_cloud_remove_notification_from_notification_scheme` | Executes `jira_cloud_remove_notification_from_notification_scheme` within the `jira-cloud-schema-notification-scheme` category. |
| `jira_cloud_jira_cloud_schema_priority` | `jira_cloud_create_priority` | Executes `jira_cloud_create_priority` within the `jira-cloud-schema-priority` category. |
| `jira_cloud_jira_cloud_schema_priority` | `jira_cloud_set_default_priority` | Executes `jira_cloud_set_default_priority` within the `jira-cloud-schema-priority` category. |
| `jira_cloud_jira_cloud_schema_priority` | `jira_cloud_delete_priority` | Executes `jira_cloud_delete_priority` within the `jira-cloud-schema-priority` category. |
| `jira_cloud_jira_cloud_schema_priority` | `jira_cloud_get_priority` | Executes `jira_cloud_get_priority` within the `jira-cloud-schema-priority` category. |
| `jira_cloud_jira_cloud_schema_priority` | `jira_cloud_update_priority` | Executes `jira_cloud_update_priority` within the `jira-cloud-schema-priority` category. |
| `jira_cloud_jira_cloud_schema_priority_scheme` | `jira_cloud_get_priority_schemes` | Executes `jira_cloud_get_priority_schemes` within the `jira-cloud-schema-priority-scheme` category. |
| `jira_cloud_jira_cloud_schema_priority_scheme` | `jira_cloud_create_priority_scheme` | Executes `jira_cloud_create_priority_scheme` within the `jira-cloud-schema-priority-scheme` category. |
| `jira_cloud_jira_cloud_schema_priority_scheme` | `jira_cloud_get_available_priorities_by_priority_scheme` | Executes `jira_cloud_get_available_priorities_by_priority_scheme` within the `jira-cloud-schema-priority-scheme` category. |
| `jira_cloud_jira_cloud_schema_priority_scheme` | `jira_cloud_delete_priority_scheme` | Executes `jira_cloud_delete_priority_scheme` within the `jira-cloud-schema-priority-scheme` category. |
| `jira_cloud_jira_cloud_schema_priority_scheme` | `jira_cloud_update_priority_scheme` | Executes `jira_cloud_update_priority_scheme` within the `jira-cloud-schema-priority-scheme` category. |
| `jira_cloud_jira_cloud_schema_priority_scheme` | `jira_cloud_get_priorities_by_priority_scheme` | Executes `jira_cloud_get_priorities_by_priority_scheme` within the `jira-cloud-schema-priority-scheme` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_get_all_statuses` | Executes `jira_cloud_get_all_statuses` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_get_redaction_status` | Executes `jira_cloud_get_redaction_status` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_get_statuses` | Executes `jira_cloud_get_statuses` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_get_status` | Executes `jira_cloud_get_status` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_get_status_categories` | Executes `jira_cloud_get_status_categories` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_get_status_category` | Executes `jira_cloud_get_status_category` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_delete_statuses_by_id` | Executes `jira_cloud_delete_statuses_by_id` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_get_statuses_by_id` | Executes `jira_cloud_get_statuses_by_id` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_create_statuses` | Executes `jira_cloud_create_statuses` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_update_statuses` | Executes `jira_cloud_update_statuses` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_status` | `jira_cloud_get_statuses_by_name` | Executes `jira_cloud_get_statuses_by_name` within the `jira-cloud-schema-status` category. |
| `jira_cloud_jira_cloud_schema_resolution` | `jira_cloud_get_resolutions` | Executes `jira_cloud_get_resolutions` within the `jira-cloud-schema-resolution` category. |
| `jira_cloud_jira_cloud_schema_resolution` | `jira_cloud_create_resolution` | Executes `jira_cloud_create_resolution` within the `jira-cloud-schema-resolution` category. |
| `jira_cloud_jira_cloud_schema_resolution` | `jira_cloud_set_default_resolution` | Executes `jira_cloud_set_default_resolution` within the `jira-cloud-schema-resolution` category. |
| `jira_cloud_jira_cloud_schema_resolution` | `jira_cloud_move_resolutions` | Executes `jira_cloud_move_resolutions` within the `jira-cloud-schema-resolution` category. |
| `jira_cloud_jira_cloud_schema_resolution` | `jira_cloud_search_resolutions` | Executes `jira_cloud_search_resolutions` within the `jira-cloud-schema-resolution` category. |
| `jira_cloud_jira_cloud_schema_resolution` | `jira_cloud_delete_resolution` | Executes `jira_cloud_delete_resolution` within the `jira-cloud-schema-resolution` category. |
| `jira_cloud_jira_cloud_schema_resolution` | `jira_cloud_get_resolution` | Executes `jira_cloud_get_resolution` within the `jira-cloud-schema-resolution` category. |
| `jira_cloud_jira_cloud_schema_resolution` | `jira_cloud_update_resolution` | Executes `jira_cloud_update_resolution` within the `jira-cloud-schema-resolution` category. |
| `jira_cloud_jira_cloud_schema_screen_tab` | `jira_cloud_get_all_screen_tabs` | Executes `jira_cloud_get_all_screen_tabs` within the `jira-cloud-schema-screen-tab` category. |
| `jira_cloud_jira_cloud_schema_screen_tab` | `jira_cloud_add_screen_tab` | Executes `jira_cloud_add_screen_tab` within the `jira-cloud-schema-screen-tab` category. |
| `jira_cloud_jira_cloud_schema_screen_tab` | `jira_cloud_delete_screen_tab` | Executes `jira_cloud_delete_screen_tab` within the `jira-cloud-schema-screen-tab` category. |
| `jira_cloud_jira_cloud_schema_screen_tab` | `jira_cloud_rename_screen_tab` | Executes `jira_cloud_rename_screen_tab` within the `jira-cloud-schema-screen-tab` category. |
| `jira_cloud_jira_cloud_schema_screen_tab` | `jira_cloud_move_screen_tab` | Executes `jira_cloud_move_screen_tab` within the `jira-cloud-schema-screen-tab` category. |
| `jira_cloud_jira_cloud_schema_screen_tab_field` | `jira_cloud_get_all_screen_tab_fields` | Executes `jira_cloud_get_all_screen_tab_fields` within the `jira-cloud-schema-screen-tab-field` category. |
| `jira_cloud_jira_cloud_schema_screen_tab_field` | `jira_cloud_add_screen_tab_field` | Executes `jira_cloud_add_screen_tab_field` within the `jira-cloud-schema-screen-tab-field` category. |
| `jira_cloud_jira_cloud_schema_screen_tab_field` | `jira_cloud_remove_screen_tab_field` | Executes `jira_cloud_remove_screen_tab_field` within the `jira-cloud-schema-screen-tab-field` category. |
| `jira_cloud_jira_cloud_schema_screen_tab_field` | `jira_cloud_move_screen_tab_field` | Executes `jira_cloud_move_screen_tab_field` within the `jira-cloud-schema-screen-tab-field` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_get_workflow_usages_for_status` | Executes `jira_cloud_get_workflow_usages_for_status` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_get_all_workflows` | Executes `jira_cloud_get_all_workflows` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_create_workflow` | Executes `jira_cloud_create_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_read_workflow_from_history` | Executes `jira_cloud_read_workflow_from_history` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_list_workflow_history` | Executes `jira_cloud_list_workflow_history` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_get_workflows_paginated` | Executes `jira_cloud_get_workflows_paginated` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_delete_inactive_workflow` | Executes `jira_cloud_delete_inactive_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_read_workflows` | Executes `jira_cloud_read_workflows` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_workflow_capabilities` | Executes `jira_cloud_workflow_capabilities` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_create_workflows` | Executes `jira_cloud_create_workflows` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_validate_create_workflows` | Executes `jira_cloud_validate_create_workflows` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_read_workflow_previews` | Executes `jira_cloud_read_workflow_previews` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_search_workflows` | Executes `jira_cloud_search_workflows` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_update_workflows` | Executes `jira_cloud_update_workflows` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_validate_update_workflows` | Executes `jira_cloud_validate_update_workflows` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_delete_default_workflow` | Executes `jira_cloud_delete_default_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_get_default_workflow` | Executes `jira_cloud_get_default_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_update_default_workflow` | Executes `jira_cloud_update_default_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_delete_draft_default_workflow` | Executes `jira_cloud_delete_draft_default_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_get_draft_default_workflow` | Executes `jira_cloud_get_draft_default_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_update_draft_default_workflow` | Executes `jira_cloud_update_draft_default_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_delete_draft_workflow_mapping` | Executes `jira_cloud_delete_draft_workflow_mapping` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_get_draft_workflow` | Executes `jira_cloud_get_draft_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_update_draft_workflow_mapping` | Executes `jira_cloud_update_draft_workflow_mapping` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_delete_workflow_mapping` | Executes `jira_cloud_delete_workflow_mapping` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_get_workflow` | Executes `jira_cloud_get_workflow` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow` | `jira_cloud_update_workflow_mapping` | Executes `jira_cloud_update_workflow_mapping` within the `jira-cloud-schema-workflow` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_get_workflow_scheme_usages_for_workflow` | Executes `jira_cloud_get_workflow_scheme_usages_for_workflow` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_get_all_workflow_schemes` | Executes `jira_cloud_get_all_workflow_schemes` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_create_workflow_scheme` | Executes `jira_cloud_create_workflow_scheme` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_read_workflow_schemes` | Executes `jira_cloud_read_workflow_schemes` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_get_required_workflow_scheme_mappings` | Executes `jira_cloud_get_required_workflow_scheme_mappings` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_delete_workflow_scheme` | Executes `jira_cloud_delete_workflow_scheme` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_get_workflow_scheme` | Executes `jira_cloud_get_workflow_scheme` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_update_workflow_scheme` | Executes `jira_cloud_update_workflow_scheme` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_create_workflow_scheme_draft_from_parent` | Executes `jira_cloud_create_workflow_scheme_draft_from_parent` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_delete_workflow_scheme_draft` | Executes `jira_cloud_delete_workflow_scheme_draft` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_get_workflow_scheme_draft` | Executes `jira_cloud_get_workflow_scheme_draft` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_update_workflow_scheme_draft` | Executes `jira_cloud_update_workflow_scheme_draft` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_scheme` | `jira_cloud_publish_draft_workflow_scheme` | Executes `jira_cloud_publish_draft_workflow_scheme` within the `jira-cloud-schema-workflow-scheme` category. |
| `jira_cloud_jira_cloud_schema_workflow_rule` | `jira_cloud_migration_resource_workflow_rule_search_post` | Executes `jira_cloud_migration_resource_workflow_rule_search_post` within the `jira-cloud-schema-workflow-rule` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_banner` | Executes `jira_cloud_get_banner` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_set_banner` | Executes `jira_cloud_set_banner` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_application_property` | Executes `jira_cloud_get_application_property` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_advanced_settings` | Executes `jira_cloud_get_advanced_settings` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_set_application_property` | Executes `jira_cloud_set_application_property` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_audit_records` | Executes `jira_cloud_get_audit_records` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_all_system_avatars` | Executes `jira_cloud_get_all_system_avatars` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_configuration` | Executes `jira_cloud_get_configuration` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_shared_time_tracking_configuration` | Executes `jira_cloud_get_shared_time_tracking_configuration` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_set_shared_time_tracking_configuration` | Executes `jira_cloud_set_shared_time_tracking_configuration` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_avatars` | Executes `jira_cloud_get_avatars` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_store_avatar` | Executes `jira_cloud_store_avatar` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_delete_avatar` | Executes `jira_cloud_delete_avatar` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_avatar_image_by_id` | Executes `jira_cloud_get_avatar_image_by_id` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_avatar_image_by_owner` | Executes `jira_cloud_get_avatar_image_by_owner` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_forge_app_property_keys` | Executes `jira_cloud_get_forge_app_property_keys` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_delete_forge_app_property` | Executes `jira_cloud_delete_forge_app_property` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_get_forge_app_property` | Executes `jira_cloud_get_forge_app_property` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_core` | `jira_cloud_put_forge_app_property` | Executes `jira_cloud_put_forge_app_property` within the `jira-cloud-core` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_find_components_for_projects` | Executes `jira_cloud_find_components_for_projects` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_create_component` | Executes `jira_cloud_create_component` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_component` | Executes `jira_cloud_delete_component` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_component` | Executes `jira_cloud_get_component` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_update_component` | Executes `jira_cloud_update_component` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_projects_with_field_schemes` | Executes `jira_cloud_get_projects_with_field_schemes` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_search_field_association_scheme_projects` | Executes `jira_cloud_search_field_association_scheme_projects` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_field_project_associations` | Executes `jira_cloud_get_field_project_associations` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_context_mapping` | Executes `jira_cloud_get_project_context_mapping` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_assign_projects_to_custom_field_context` | Executes `jira_cloud_assign_projects_to_custom_field_context` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_remove_custom_field_context_from_projects` | Executes `jira_cloud_remove_custom_field_context_from_projects` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_assign_field_configuration_scheme_to_project` | Executes `jira_cloud_assign_field_configuration_scheme_to_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_search_projects_using_security_schemes` | Executes `jira_cloud_search_projects_using_security_schemes` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_associate_schemes_to_projects` | Executes `jira_cloud_associate_schemes_to_projects` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_notification_scheme_to_project_mappings` | Executes `jira_cloud_get_notification_scheme_to_project_mappings` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_permitted_projects` | Executes `jira_cloud_get_permitted_projects` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_projects_by_priority_scheme` | Executes `jira_cloud_get_projects_by_priority_scheme` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_all_projects` | Executes `jira_cloud_get_all_projects` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_create_project` | Executes `jira_cloud_create_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_create_project_with_custom_template` | Executes `jira_cloud_create_project_with_custom_template` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_search_projects` | Executes `jira_cloud_search_projects` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_all_project_types` | Executes `jira_cloud_get_all_project_types` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_all_accessible_project_types` | Executes `jira_cloud_get_all_accessible_project_types` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_type_by_key` | Executes `jira_cloud_get_project_type_by_key` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_accessible_project_type_by_key` | Executes `jira_cloud_get_accessible_project_type_by_key` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_project` | Executes `jira_cloud_delete_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project` | Executes `jira_cloud_get_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_update_project` | Executes `jira_cloud_update_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_archive_project` | Executes `jira_cloud_archive_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_update_project_avatar` | Executes `jira_cloud_update_project_avatar` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_project_avatar` | Executes `jira_cloud_delete_project_avatar` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_create_project_avatar` | Executes `jira_cloud_create_project_avatar` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_all_project_avatars` | Executes `jira_cloud_get_all_project_avatars` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_classification_config` | Executes `jira_cloud_get_project_classification_config` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_remove_default_project_classification` | Executes `jira_cloud_remove_default_project_classification` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_default_project_classification` | Executes `jira_cloud_get_default_project_classification` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_update_default_project_classification` | Executes `jira_cloud_update_default_project_classification` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_components_paginated` | Executes `jira_cloud_get_project_components_paginated` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_components` | Executes `jira_cloud_get_project_components` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_project_asynchronously` | Executes `jira_cloud_delete_project_asynchronously` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_features_for_project` | Executes `jira_cloud_get_features_for_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_toggle_feature_for_project` | Executes `jira_cloud_toggle_feature_for_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_property_keys` | Executes `jira_cloud_get_project_property_keys` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_project_property` | Executes `jira_cloud_delete_project_property` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_property` | Executes `jira_cloud_get_project_property` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_set_project_property` | Executes `jira_cloud_set_project_property` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_roles` | Executes `jira_cloud_get_project_roles` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_role` | Executes `jira_cloud_get_project_role` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_role_details` | Executes `jira_cloud_get_project_role_details` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_versions_paginated` | Executes `jira_cloud_get_project_versions_paginated` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_versions` | Executes `jira_cloud_get_project_versions` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_email` | Executes `jira_cloud_get_project_email` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_update_project_email` | Executes `jira_cloud_update_project_email` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_notification_scheme_for_project` | Executes `jira_cloud_get_notification_scheme_for_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_security_levels_for_project` | Executes `jira_cloud_get_security_levels_for_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_all_project_categories` | Executes `jira_cloud_get_all_project_categories` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_create_project_category` | Executes `jira_cloud_create_project_category` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_remove_project_category` | Executes `jira_cloud_remove_project_category` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_category_by_id` | Executes `jira_cloud_get_project_category_by_id` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_update_project_category` | Executes `jira_cloud_update_project_category` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_fields` | Executes `jira_cloud_get_project_fields` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_validate_project_key` | Executes `jira_cloud_validate_project_key` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_valid_project_key` | Executes `jira_cloud_get_valid_project_key` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_valid_project_name` | Executes `jira_cloud_get_valid_project_name` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_all_project_roles` | Executes `jira_cloud_get_all_project_roles` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_create_project_role` | Executes `jira_cloud_create_project_role` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_project_role` | Executes `jira_cloud_delete_project_role` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_role_by_id` | Executes `jira_cloud_get_project_role_by_id` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_partial_update_project_role` | Executes `jira_cloud_partial_update_project_role` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_fully_update_project_role` | Executes `jira_cloud_fully_update_project_role` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_project_role_actors_from_role` | Executes `jira_cloud_delete_project_role_actors_from_role` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_role_actors_for_role` | Executes `jira_cloud_get_project_role_actors_for_role` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_add_project_role_actors_to_role` | Executes `jira_cloud_add_project_role_actors_to_role` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_usages_for_status` | Executes `jira_cloud_get_project_usages_for_status` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_create_version` | Executes `jira_cloud_create_version` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_version` | Executes `jira_cloud_delete_version` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_version` | Executes `jira_cloud_get_version` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_update_version` | Executes `jira_cloud_update_version` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_merge_versions` | Executes `jira_cloud_merge_versions` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_move_version` | Executes `jira_cloud_move_version` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_delete_and_replace_version` | Executes `jira_cloud_delete_and_replace_version` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_usages_for_workflow` | Executes `jira_cloud_get_project_usages_for_workflow` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_workflow_scheme_project_associations` | Executes `jira_cloud_get_workflow_scheme_project_associations` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_assign_scheme_to_project` | Executes `jira_cloud_assign_scheme_to_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_switch_workflow_scheme_for_project` | Executes `jira_cloud_switch_workflow_scheme_for_project` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_project` | `jira_cloud_get_project_usages_for_workflow_scheme` | Executes `jira_cloud_get_project_usages_for_workflow_scheme` within the `jira-cloud-project` category. |
| `jira_cloud_jira_cloud_issue_attachment` | `jira_cloud_get_attachment_content` | Executes `jira_cloud_get_attachment_content` within the `jira-cloud-issue-attachment` category. |
| `jira_cloud_jira_cloud_issue_attachment` | `jira_cloud_get_attachment_meta` | Executes `jira_cloud_get_attachment_meta` within the `jira-cloud-issue-attachment` category. |
| `jira_cloud_jira_cloud_issue_attachment` | `jira_cloud_get_attachment_thumbnail` | Executes `jira_cloud_get_attachment_thumbnail` within the `jira-cloud-issue-attachment` category. |
| `jira_cloud_jira_cloud_issue_attachment` | `jira_cloud_remove_attachment` | Executes `jira_cloud_remove_attachment` within the `jira-cloud-issue-attachment` category. |
| `jira_cloud_jira_cloud_issue_attachment` | `jira_cloud_get_attachment` | Executes `jira_cloud_get_attachment` within the `jira-cloud-issue-attachment` category. |
| `jira_cloud_jira_cloud_issue_attachment` | `jira_cloud_expand_attachment_for_humans` | Executes `jira_cloud_expand_attachment_for_humans` within the `jira-cloud-issue-attachment` category. |
| `jira_cloud_jira_cloud_issue_attachment` | `jira_cloud_expand_attachment_for_machines` | Executes `jira_cloud_expand_attachment_for_machines` within the `jira-cloud-issue-attachment` category. |
| `jira_cloud_jira_cloud_issue_attachment` | `jira_cloud_add_attachment` | Executes `jira_cloud_add_attachment` within the `jira-cloud-issue-attachment` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_submit_bulk_delete` | Executes `jira_cloud_submit_bulk_delete` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_get_bulk_editable_fields` | Executes `jira_cloud_get_bulk_editable_fields` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_submit_bulk_edit` | Executes `jira_cloud_submit_bulk_edit` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_submit_bulk_move` | Executes `jira_cloud_submit_bulk_move` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_submit_bulk_transition` | Executes `jira_cloud_submit_bulk_transition` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_submit_bulk_unwatch` | Executes `jira_cloud_submit_bulk_unwatch` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_submit_bulk_watch` | Executes `jira_cloud_submit_bulk_watch` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_get_bulk_operation_progress` | Executes `jira_cloud_get_bulk_operation_progress` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_get_bulk_changelogs` | Executes `jira_cloud_get_bulk_changelogs` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_edit_dashboards` | Executes `jira_cloud_bulk_edit_dashboards` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_pin_unpin_projects_async` | Executes `jira_cloud_bulk_pin_unpin_projects_async` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_get_groups` | Executes `jira_cloud_bulk_get_groups` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_fetch_issues` | Executes `jira_cloud_bulk_fetch_issues` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_set_issues_properties_list` | Executes `jira_cloud_bulk_set_issues_properties_list` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_set_issue_properties_by_issue` | Executes `jira_cloud_bulk_set_issue_properties_by_issue` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_delete_issue_property` | Executes `jira_cloud_bulk_delete_issue_property` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_set_issue_property` | Executes `jira_cloud_bulk_set_issue_property` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_get_is_watching_issue_bulk` | Executes `jira_cloud_get_is_watching_issue_bulk` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_get_bulk_permissions` | Executes `jira_cloud_get_bulk_permissions` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_get_bulk_screen_tabs` | Executes `jira_cloud_get_bulk_screen_tabs` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_find_bulk_assignable_users` | Executes `jira_cloud_find_bulk_assignable_users` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_get_users` | Executes `jira_cloud_bulk_get_users` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_bulk_get_users_migration` | Executes `jira_cloud_bulk_get_users_migration` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_bulk` | `jira_cloud_get_user_email_bulk` | Executes `jira_cloud_get_user_email_bulk` within the `jira-cloud-issue-bulk` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_available_transitions` | Executes `jira_cloud_get_available_transitions` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_component_related_issues` | Executes `jira_cloud_get_component_related_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_all_issue_field_options` | Executes `jira_cloud_get_all_issue_field_options` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_create_issue_field_option` | Executes `jira_cloud_create_issue_field_option` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_selectable_issue_field_options` | Executes `jira_cloud_get_selectable_issue_field_options` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_visible_issue_field_options` | Executes `jira_cloud_get_visible_issue_field_options` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_delete_issue_field_option` | Executes `jira_cloud_delete_issue_field_option` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_field_option` | Executes `jira_cloud_get_issue_field_option` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_update_issue_field_option` | Executes `jira_cloud_update_issue_field_option` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_replace_issue_field_option` | Executes `jira_cloud_replace_issue_field_option` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_create_filter` | Executes `jira_cloud_create_filter` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_favourite_filters` | Executes `jira_cloud_get_favourite_filters` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_my_filters` | Executes `jira_cloud_get_my_filters` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_filters_paginated` | Executes `jira_cloud_get_filters_paginated` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_delete_filter` | Executes `jira_cloud_delete_filter` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_filter` | Executes `jira_cloud_get_filter` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_update_filter` | Executes `jira_cloud_update_filter` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_delete_favourite_for_filter` | Executes `jira_cloud_delete_favourite_for_filter` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_set_favourite_for_filter` | Executes `jira_cloud_set_favourite_for_filter` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_change_filter_owner` | Executes `jira_cloud_change_filter_owner` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_create_issue` | Executes `jira_cloud_create_issue` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_archive_issues_async` | Executes `jira_cloud_archive_issues_async` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_archive_issues` | Executes `jira_cloud_archive_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_create_issues` | Executes `jira_cloud_create_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_create_issue_meta` | Executes `jira_cloud_get_create_issue_meta` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_limit_report` | Executes `jira_cloud_get_issue_limit_report` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_picker_resource` | Executes `jira_cloud_get_issue_picker_resource` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_unarchive_issues` | Executes `jira_cloud_unarchive_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_delete_issue` | Executes `jira_cloud_delete_issue` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue` | Executes `jira_cloud_get_issue` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_edit_issue` | Executes `jira_cloud_edit_issue` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_assign_issue` | Executes `jira_cloud_assign_issue` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_edit_issue_meta` | Executes `jira_cloud_get_edit_issue_meta` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_property_keys` | Executes `jira_cloud_get_issue_property_keys` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_delete_issue_property` | Executes `jira_cloud_delete_issue_property` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_property` | Executes `jira_cloud_get_issue_property` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_set_issue_property` | Executes `jira_cloud_set_issue_property` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_transitions` | Executes `jira_cloud_get_transitions` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_do_transition` | Executes `jira_cloud_do_transition` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_remove_watcher` | Executes `jira_cloud_remove_watcher` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_add_watcher` | Executes `jira_cloud_add_watcher` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_link_issues` | Executes `jira_cloud_link_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_delete_issue_link` | Executes `jira_cloud_delete_issue_link` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_link` | Executes `jira_cloud_get_issue_link` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_link_types` | Executes `jira_cloud_get_issue_link_types` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_create_issue_link_type` | Executes `jira_cloud_create_issue_link_type` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_delete_issue_link_type` | Executes `jira_cloud_delete_issue_link_type` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_link_type` | Executes `jira_cloud_get_issue_link_type` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_update_issue_link_type` | Executes `jira_cloud_update_issue_link_type` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_export_archived_issues` | Executes `jira_cloud_export_archived_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_security_schemes` | Executes `jira_cloud_get_issue_security_schemes` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_create_issue_security_scheme` | Executes `jira_cloud_create_issue_security_scheme` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_security_scheme` | Executes `jira_cloud_get_issue_security_scheme` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_update_issue_security_scheme` | Executes `jira_cloud_update_issue_security_scheme` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_security_level_members` | Executes `jira_cloud_get_issue_security_level_members` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_all_types` | Executes `jira_cloud_get_issue_all_types` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_match_issues` | Executes `jira_cloud_match_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_parse_jql_queries` | Executes `jira_cloud_parse_jql_queries` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_sanitise_jql_queries` | Executes `jira_cloud_sanitise_jql_queries` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_project_issue_security_scheme` | Executes `jira_cloud_get_project_issue_security_scheme` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_search_for_issues_using_jql` | Executes `jira_cloud_search_for_issues_using_jql` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_search_for_issues_using_jql_post` | Executes `jira_cloud_search_for_issues_using_jql_post` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_count_issues` | Executes `jira_cloud_count_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_search_and_reconsile_issues_using_jql` | Executes `jira_cloud_search_and_reconsile_issues_using_jql` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_search_and_reconsile_issues_using_jql_post` | Executes `jira_cloud_search_and_reconsile_issues_using_jql_post` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_security_level` | Executes `jira_cloud_get_issue_security_level` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_issue_navigator_default_columns` | Executes `jira_cloud_get_issue_navigator_default_columns` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_set_issue_navigator_default_columns` | Executes `jira_cloud_set_issue_navigator_default_columns` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_version_related_issues` | Executes `jira_cloud_get_version_related_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_version_unresolved_issues` | Executes `jira_cloud_get_version_unresolved_issues` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_workflow_transition_rule_configurations` | Executes `jira_cloud_get_workflow_transition_rule_configurations` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_delete_workflow_transition_property` | Executes `jira_cloud_delete_workflow_transition_property` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_get_workflow_transition_properties` | Executes `jira_cloud_get_workflow_transition_properties` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_create_workflow_transition_property` | Executes `jira_cloud_create_workflow_transition_property` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_core` | `jira_cloud_update_workflow_transition_property` | Executes `jira_cloud_update_workflow_transition_property` within the `jira-cloud-issue-core` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_get_comments_by_ids` | Executes `jira_cloud_get_comments_by_ids` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_get_comment_property_keys` | Executes `jira_cloud_get_comment_property_keys` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_delete_comment_property` | Executes `jira_cloud_delete_comment_property` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_get_comment_property` | Executes `jira_cloud_get_comment_property` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_set_comment_property` | Executes `jira_cloud_set_comment_property` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_get_comments` | Executes `jira_cloud_get_comments` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_add_comment` | Executes `jira_cloud_add_comment` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_delete_comment` | Executes `jira_cloud_delete_comment` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_get_comment` | Executes `jira_cloud_get_comment` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_comment` | `jira_cloud_update_comment` | Executes `jira_cloud_update_comment` within the `jira-cloud-issue-comment` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_type_mappings_for_contexts` | Executes `jira_cloud_get_issue_type_mappings_for_contexts` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_add_issue_types_to_context` | Executes `jira_cloud_add_issue_types_to_context` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_remove_issue_types_from_context` | Executes `jira_cloud_remove_issue_types_from_context` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_create_issue_meta_issue_types` | Executes `jira_cloud_get_create_issue_meta_issue_types` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_create_issue_meta_issue_type_id` | Executes `jira_cloud_get_create_issue_meta_issue_type_id` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_create_issue_type` | Executes `jira_cloud_create_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_types_for_project` | Executes `jira_cloud_get_issue_types_for_project` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_delete_issue_type` | Executes `jira_cloud_delete_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_type` | Executes `jira_cloud_get_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_update_issue_type` | Executes `jira_cloud_update_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_alternative_issue_types` | Executes `jira_cloud_get_alternative_issue_types` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_create_issue_type_avatar` | Executes `jira_cloud_create_issue_type_avatar` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_type_property_keys` | Executes `jira_cloud_get_issue_type_property_keys` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_delete_issue_type_property` | Executes `jira_cloud_delete_issue_type_property` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_type_property` | Executes `jira_cloud_get_issue_type_property` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_set_issue_type_property` | Executes `jira_cloud_set_issue_type_property` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_all_issue_type_schemes` | Executes `jira_cloud_get_all_issue_type_schemes` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_create_issue_type_scheme` | Executes `jira_cloud_create_issue_type_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_type_schemes_mapping` | Executes `jira_cloud_get_issue_type_schemes_mapping` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_type_scheme_for_projects` | Executes `jira_cloud_get_issue_type_scheme_for_projects` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_assign_issue_type_scheme_to_project` | Executes `jira_cloud_assign_issue_type_scheme_to_project` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_delete_issue_type_scheme` | Executes `jira_cloud_delete_issue_type_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_update_issue_type_scheme` | Executes `jira_cloud_update_issue_type_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_add_issue_types_to_issue_type_scheme` | Executes `jira_cloud_add_issue_types_to_issue_type_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_reorder_issue_types_in_issue_type_scheme` | Executes `jira_cloud_reorder_issue_types_in_issue_type_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_remove_issue_type_from_issue_type_scheme` | Executes `jira_cloud_remove_issue_type_from_issue_type_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_type_screen_schemes` | Executes `jira_cloud_get_issue_type_screen_schemes` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_create_issue_type_screen_scheme` | Executes `jira_cloud_create_issue_type_screen_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_issue_type_screen_scheme_mappings` | Executes `jira_cloud_get_issue_type_screen_scheme_mappings` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_assign_issue_type_screen_scheme_to_project` | Executes `jira_cloud_assign_issue_type_screen_scheme_to_project` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_delete_issue_type_screen_scheme` | Executes `jira_cloud_delete_issue_type_screen_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_update_issue_type_screen_scheme` | Executes `jira_cloud_update_issue_type_screen_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_append_mappings_for_issue_type_screen_scheme` | Executes `jira_cloud_append_mappings_for_issue_type_screen_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_projects_for_issue_type_screen_scheme` | Executes `jira_cloud_get_projects_for_issue_type_screen_scheme` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_project_issue_type_usages_for_status` | Executes `jira_cloud_get_project_issue_type_usages_for_status` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_workflow_project_issue_type_usages` | Executes `jira_cloud_get_workflow_project_issue_type_usages` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_delete_workflow_scheme_draft_issue_type` | Executes `jira_cloud_delete_workflow_scheme_draft_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_workflow_scheme_draft_issue_type` | Executes `jira_cloud_get_workflow_scheme_draft_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_set_workflow_scheme_draft_issue_type` | Executes `jira_cloud_set_workflow_scheme_draft_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_delete_workflow_scheme_issue_type` | Executes `jira_cloud_delete_workflow_scheme_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_get_workflow_scheme_issue_type` | Executes `jira_cloud_get_workflow_scheme_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_type` | `jira_cloud_set_workflow_scheme_issue_type` | Executes `jira_cloud_set_workflow_scheme_issue_type` within the `jira-cloud-issue-type` category. |
| `jira_cloud_jira_cloud_issue_link` | `jira_cloud_delete_remote_issue_link_by_global_id` | Executes `jira_cloud_delete_remote_issue_link_by_global_id` within the `jira-cloud-issue-link` category. |
| `jira_cloud_jira_cloud_issue_link` | `jira_cloud_get_remote_issue_links` | Executes `jira_cloud_get_remote_issue_links` within the `jira-cloud-issue-link` category. |
| `jira_cloud_jira_cloud_issue_link` | `jira_cloud_create_or_update_remote_issue_link` | Executes `jira_cloud_create_or_update_remote_issue_link` within the `jira-cloud-issue-link` category. |
| `jira_cloud_jira_cloud_issue_link` | `jira_cloud_delete_remote_issue_link_by_id` | Executes `jira_cloud_delete_remote_issue_link_by_id` within the `jira-cloud-issue-link` category. |
| `jira_cloud_jira_cloud_issue_link` | `jira_cloud_get_remote_issue_link_by_id` | Executes `jira_cloud_get_remote_issue_link_by_id` within the `jira-cloud-issue-link` category. |
| `jira_cloud_jira_cloud_issue_link` | `jira_cloud_update_remote_issue_link` | Executes `jira_cloud_update_remote_issue_link` within the `jira-cloud-issue-link` category. |
| `jira_cloud_jira_cloud_issue_watcher` | `jira_cloud_get_issue_watchers` | Executes `jira_cloud_get_issue_watchers` within the `jira-cloud-issue-watcher` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_bulk_delete_worklogs` | Executes `jira_cloud_bulk_delete_worklogs` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_get_issue_worklog` | Executes `jira_cloud_get_issue_worklog` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_add_worklog` | Executes `jira_cloud_add_worklog` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_bulk_move_worklogs` | Executes `jira_cloud_bulk_move_worklogs` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_delete_worklog` | Executes `jira_cloud_delete_worklog` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_get_worklog` | Executes `jira_cloud_get_worklog` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_update_worklog` | Executes `jira_cloud_update_worklog` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_get_worklog_property_keys` | Executes `jira_cloud_get_worklog_property_keys` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_delete_worklog_property` | Executes `jira_cloud_delete_worklog_property` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_get_worklog_property` | Executes `jira_cloud_get_worklog_property` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_set_worklog_property` | Executes `jira_cloud_set_worklog_property` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_get_ids_of_worklogs_deleted_since` | Executes `jira_cloud_get_ids_of_worklogs_deleted_since` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_get_worklogs_for_ids` | Executes `jira_cloud_get_worklogs_for_ids` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_get_ids_of_worklogs_modified_since` | Executes `jira_cloud_get_ids_of_worklogs_modified_since` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_issue_worklog` | `jira_cloud_get_worklogs_by_issue_id_and_worklog_id` | Executes `jira_cloud_get_worklogs_by_issue_id_and_worklog_id` within the `jira-cloud-issue-worklog` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_field_association_scheme_item_parameters` | Executes `jira_cloud_remove_field_association_scheme_item_parameters` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_field_association_scheme_item_parameters` | Executes `jira_cloud_update_field_association_scheme_item_parameters` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_associate_projects_to_field_association_schemes` | Executes `jira_cloud_associate_projects_to_field_association_schemes` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_selected_time_tracking_implementation` | Executes `jira_cloud_get_selected_time_tracking_implementation` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_select_time_tracking_implementation` | Executes `jira_cloud_select_time_tracking_implementation` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_available_time_tracking_implementations` | Executes `jira_cloud_get_available_time_tracking_implementations` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_all_gadgets` | Executes `jira_cloud_get_all_gadgets` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_add_gadget` | Executes `jira_cloud_add_gadget` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_gadget` | Executes `jira_cloud_remove_gadget` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_gadget` | Executes `jira_cloud_update_gadget` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_policy` | Executes `jira_cloud_get_policy` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_policies` | Executes `jira_cloud_get_policies` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_events` | Executes `jira_cloud_get_events` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_analyse_expression` | Executes `jira_cloud_analyse_expression` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_evaluate_jira_expression` | Executes `jira_cloud_evaluate_jira_expression` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_evaluate_jsis_jira_expression` | Executes `jira_cloud_evaluate_jsis_jira_expression` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_associations` | Executes `jira_cloud_remove_associations` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_create_associations` | Executes `jira_cloud_create_associations` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_default_values` | Executes `jira_cloud_get_default_values` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_set_default_values` | Executes `jira_cloud_set_default_values` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_custom_field_contexts_for_projects_and_issue_types` | Executes `jira_cloud_get_custom_field_contexts_for_projects_and_issue_types` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_options_for_context` | Executes `jira_cloud_get_options_for_context` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_field_configuration_scheme_project_mapping` | Executes `jira_cloud_get_field_configuration_scheme_project_mapping` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_issue_types_from_global_field_configuration_scheme` | Executes `jira_cloud_remove_issue_types_from_global_field_configuration_scheme` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_default_share_scope` | Executes `jira_cloud_get_default_share_scope` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_set_default_share_scope` | Executes `jira_cloud_set_default_share_scope` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_reset_columns` | Executes `jira_cloud_reset_columns` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_columns` | Executes `jira_cloud_get_columns` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_set_columns` | Executes `jira_cloud_set_columns` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_license` | Executes `jira_cloud_get_license` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_change_logs` | Executes `jira_cloud_get_change_logs` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_change_logs_by_ids` | Executes `jira_cloud_get_change_logs_by_ids` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_notify` | Executes `jira_cloud_notify` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_vote` | Executes `jira_cloud_remove_vote` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_votes` | Executes `jira_cloud_get_votes` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_add_vote` | Executes `jira_cloud_add_vote` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_security_levels` | Executes `jira_cloud_get_security_levels` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_set_default_levels` | Executes `jira_cloud_set_default_levels` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_security_level_members` | Executes `jira_cloud_get_security_level_members` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_add_security_level` | Executes `jira_cloud_add_security_level` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_level` | Executes `jira_cloud_remove_level` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_security_level` | Executes `jira_cloud_update_security_level` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_add_security_level_members` | Executes `jira_cloud_add_security_level_members` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_member_from_security_level` | Executes `jira_cloud_remove_member_from_security_level` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_issue_type_screen_scheme_project_associations` | Executes `jira_cloud_get_issue_type_screen_scheme_project_associations` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_mappings_from_issue_type_screen_scheme` | Executes `jira_cloud_remove_mappings_from_issue_type_screen_scheme` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_auto_complete` | Executes `jira_cloud_get_auto_complete` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_auto_complete_post` | Executes `jira_cloud_get_auto_complete_post` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_precomputations` | Executes `jira_cloud_get_precomputations` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_precomputations` | Executes `jira_cloud_update_precomputations` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_precomputations_by_id` | Executes `jira_cloud_get_precomputations_by_id` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_migrate_queries` | Executes `jira_cloud_migrate_queries` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_all_labels` | Executes `jira_cloud_get_all_labels` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_approximate_license_count` | Executes `jira_cloud_get_approximate_license_count` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_approximate_application_license_count` | Executes `jira_cloud_get_approximate_application_license_count` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_preference` | Executes `jira_cloud_remove_preference` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_preference` | Executes `jira_cloud_get_preference` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_set_preference` | Executes `jira_cloud_set_preference` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_locale` | Executes `jira_cloud_get_locale` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_set_locale` | Executes `jira_cloud_set_locale` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_add_notifications` | Executes `jira_cloud_add_notifications` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_plans` | Executes `jira_cloud_get_plans` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_create_plan` | Executes `jira_cloud_create_plan` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_plan` | Executes `jira_cloud_get_plan` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_plan` | Executes `jira_cloud_update_plan` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_archive_plan` | Executes `jira_cloud_archive_plan` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_duplicate_plan` | Executes `jira_cloud_duplicate_plan` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_teams` | Executes `jira_cloud_get_teams` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_add_atlassian_team` | Executes `jira_cloud_add_atlassian_team` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_atlassian_team` | Executes `jira_cloud_remove_atlassian_team` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_atlassian_team` | Executes `jira_cloud_get_atlassian_team` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_atlassian_team` | Executes `jira_cloud_update_atlassian_team` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_create_plan_only_team` | Executes `jira_cloud_create_plan_only_team` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_delete_plan_only_team` | Executes `jira_cloud_delete_plan_only_team` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_plan_only_team` | Executes `jira_cloud_get_plan_only_team` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_plan_only_team` | Executes `jira_cloud_update_plan_only_team` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_trash_plan` | Executes `jira_cloud_trash_plan` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_priorities` | Executes `jira_cloud_get_priorities` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_move_priorities` | Executes `jira_cloud_move_priorities` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_search_priorities` | Executes `jira_cloud_search_priorities` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_suggested_priorities_for_mappings` | Executes `jira_cloud_suggested_priorities_for_mappings` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_edit_template` | Executes `jira_cloud_edit_template` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_live_template` | Executes `jira_cloud_live_template` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_remove_template` | Executes `jira_cloud_remove_template` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_save_template` | Executes `jira_cloud_save_template` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_recent` | Executes `jira_cloud_get_recent` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_restore` | Executes `jira_cloud_restore` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_delete_actor` | Executes `jira_cloud_delete_actor` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_set_actors` | Executes `jira_cloud_set_actors` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_hierarchy` | Executes `jira_cloud_get_hierarchy` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_redact` | Executes `jira_cloud_redact` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_server_info` | Executes `jira_cloud_get_server_info` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_search` | Executes `jira_cloud_search` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_task` | Executes `jira_cloud_get_task` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_cancel_task` | Executes `jira_cloud_cancel_task` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_ui_modifications` | Executes `jira_cloud_get_ui_modifications` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_create_ui_modification` | Executes `jira_cloud_create_ui_modification` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_delete_ui_modification` | Executes `jira_cloud_delete_ui_modification` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_ui_modification` | Executes `jira_cloud_update_ui_modification` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_related_work` | Executes `jira_cloud_get_related_work` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_create_related_work` | Executes `jira_cloud_create_related_work` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_related_work` | Executes `jira_cloud_update_related_work` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_delete_related_work` | Executes `jira_cloud_delete_related_work` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_delete_webhook_by_id` | Executes `jira_cloud_delete_webhook_by_id` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_dynamic_webhooks_for_app` | Executes `jira_cloud_get_dynamic_webhooks_for_app` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_register_dynamic_webhooks` | Executes `jira_cloud_register_dynamic_webhooks` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_failed_webhooks` | Executes `jira_cloud_get_failed_webhooks` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_refresh_webhooks` | Executes `jira_cloud_refresh_webhooks` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_update_workflow_transition_rule_configurations` | Executes `jira_cloud_update_workflow_transition_rule_configurations` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_delete_workflow_transition_rule_configurations` | Executes `jira_cloud_delete_workflow_transition_rule_configurations` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_get_default_editor` | Executes `jira_cloud_get_default_editor` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_addon_properties_resource_get_addon_properties_get` | Executes `jira_cloud_addon_properties_resource_get_addon_properties_get` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_addon_properties_resource_delete_addon_property_delete` | Executes `jira_cloud_addon_properties_resource_delete_addon_property_delete` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_addon_properties_resource_get_addon_property_get` | Executes `jira_cloud_addon_properties_resource_get_addon_property_get` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_addon_properties_resource_put_addon_property_put` | Executes `jira_cloud_addon_properties_resource_put_addon_property_put` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_dynamic_modules_resource_remove_modules_delete` | Executes `jira_cloud_dynamic_modules_resource_remove_modules_delete` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_dynamic_modules_resource_get_modules_get` | Executes `jira_cloud_dynamic_modules_resource_get_modules_get` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_dynamic_modules_resource_register_modules_post` | Executes `jira_cloud_dynamic_modules_resource_register_modules_post` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put` | Executes `jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_migration_resource_update_entity_properties_value_put` | Executes `jira_cloud_migration_resource_update_entity_properties_value_put` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get` | Executes `jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post` | Executes `jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post` within the `jira-cloud-other` category. |
| `jira_cloud_jira_cloud_other` | `jira_cloud_service_registry_resource_services_get` | Executes `jira_cloud_service_registry_resource_services_get` within the `jira-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_admin_key` | Executes `confluence_cloud_get_admin_key` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_enable_admin_key` | Executes `confluence_cloud_enable_admin_key` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_disable_admin_key` | Executes `confluence_cloud_disable_admin_key` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_posts` | Executes `confluence_cloud_get_blog_posts` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_blog_post` | Executes `confluence_cloud_create_blog_post` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_post_by_id` | Executes `confluence_cloud_get_blog_post_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_blog_post` | Executes `confluence_cloud_update_blog_post` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_blog_post` | Executes `confluence_cloud_delete_blog_post` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_by_type_in_blog_post` | Executes `confluence_cloud_get_custom_content_by_type_in_blog_post` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_post_like_count` | Executes `confluence_cloud_get_blog_post_like_count` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blogpost_content_properties` | Executes `confluence_cloud_get_blogpost_content_properties` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_blogpost_property` | Executes `confluence_cloud_create_blogpost_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blogpost_content_properties_by_id` | Executes `confluence_cloud_get_blogpost_content_properties_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_blogpost_property_by_id` | Executes `confluence_cloud_update_blogpost_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_blogpost_property_by_id` | Executes `confluence_cloud_delete_blogpost_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_post_operations` | Executes `confluence_cloud_get_blog_post_operations` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_post_versions` | Executes `confluence_cloud_get_blog_post_versions` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_post_version_details` | Executes `confluence_cloud_get_blog_post_version_details` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_convert_content_ids_to_content_types` | Executes `confluence_cloud_convert_content_ids_to_content_types` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_by_type` | Executes `confluence_cloud_get_custom_content_by_type` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_custom_content` | Executes `confluence_cloud_create_custom_content` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_by_id` | Executes `confluence_cloud_get_custom_content_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_custom_content` | Executes `confluence_cloud_update_custom_content` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_custom_content` | Executes `confluence_cloud_delete_custom_content` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_comments` | Executes `confluence_cloud_get_custom_content_comments` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_operations` | Executes `confluence_cloud_get_custom_content_operations` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_content_properties` | Executes `confluence_cloud_get_custom_content_content_properties` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_content_properties_by_id` | Executes `confluence_cloud_get_custom_content_content_properties_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_post_redact_blog` | Executes `confluence_cloud_post_redact_blog` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_whiteboard` | Executes `confluence_cloud_create_whiteboard` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_whiteboard_by_id` | Executes `confluence_cloud_get_whiteboard_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_whiteboard` | Executes `confluence_cloud_delete_whiteboard` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_whiteboard_content_properties` | Executes `confluence_cloud_get_whiteboard_content_properties` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_whiteboard_property` | Executes `confluence_cloud_create_whiteboard_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_whiteboard_content_properties_by_id` | Executes `confluence_cloud_get_whiteboard_content_properties_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_whiteboard_property_by_id` | Executes `confluence_cloud_update_whiteboard_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_whiteboard_property_by_id` | Executes `confluence_cloud_delete_whiteboard_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_whiteboard_operations` | Executes `confluence_cloud_get_whiteboard_operations` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_whiteboard_direct_children` | Executes `confluence_cloud_get_whiteboard_direct_children` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_whiteboard_descendants` | Executes `confluence_cloud_get_whiteboard_descendants` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_whiteboard_ancestors` | Executes `confluence_cloud_get_whiteboard_ancestors` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_database` | Executes `confluence_cloud_create_database` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_database_by_id` | Executes `confluence_cloud_get_database_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_database` | Executes `confluence_cloud_delete_database` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_database_content_properties` | Executes `confluence_cloud_get_database_content_properties` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_database_property` | Executes `confluence_cloud_create_database_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_database_content_properties_by_id` | Executes `confluence_cloud_get_database_content_properties_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_database_property_by_id` | Executes `confluence_cloud_update_database_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_database_property_by_id` | Executes `confluence_cloud_delete_database_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_database_operations` | Executes `confluence_cloud_get_database_operations` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_database_direct_children` | Executes `confluence_cloud_get_database_direct_children` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_database_descendants` | Executes `confluence_cloud_get_database_descendants` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_database_ancestors` | Executes `confluence_cloud_get_database_ancestors` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_smart_link` | Executes `confluence_cloud_create_smart_link` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_smart_link_by_id` | Executes `confluence_cloud_get_smart_link_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_smart_link` | Executes `confluence_cloud_delete_smart_link` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_smart_link_content_properties` | Executes `confluence_cloud_get_smart_link_content_properties` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_smart_link_property` | Executes `confluence_cloud_create_smart_link_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_smart_link_content_properties_by_id` | Executes `confluence_cloud_get_smart_link_content_properties_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_smart_link_property_by_id` | Executes `confluence_cloud_update_smart_link_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_smart_link_property_by_id` | Executes `confluence_cloud_delete_smart_link_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_smart_link_operations` | Executes `confluence_cloud_get_smart_link_operations` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_smart_link_direct_children` | Executes `confluence_cloud_get_smart_link_direct_children` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_smart_link_descendants` | Executes `confluence_cloud_get_smart_link_descendants` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_smart_link_ancestors` | Executes `confluence_cloud_get_smart_link_ancestors` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_folder` | Executes `confluence_cloud_create_folder` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_folder_by_id` | Executes `confluence_cloud_get_folder_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_folder` | Executes `confluence_cloud_delete_folder` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_folder_content_properties` | Executes `confluence_cloud_get_folder_content_properties` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_folder_property` | Executes `confluence_cloud_create_folder_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_folder_content_properties_by_id` | Executes `confluence_cloud_get_folder_content_properties_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_folder_property_by_id` | Executes `confluence_cloud_update_folder_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_folder_property_by_id` | Executes `confluence_cloud_delete_folder_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_folder_operations` | Executes `confluence_cloud_get_folder_operations` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_folder_direct_children` | Executes `confluence_cloud_get_folder_direct_children` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_folder_descendants` | Executes `confluence_cloud_get_folder_descendants` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_folder_ancestors` | Executes `confluence_cloud_get_folder_ancestors` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_versions` | Executes `confluence_cloud_get_custom_content_versions` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_custom_content_version_details` | Executes `confluence_cloud_get_custom_content_version_details` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_post_footer_comments` | Executes `confluence_cloud_get_blog_post_footer_comments` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_post_inline_comments` | Executes `confluence_cloud_get_blog_post_inline_comments` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_footer_comments` | Executes `confluence_cloud_get_footer_comments` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_footer_comment` | Executes `confluence_cloud_create_footer_comment` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_footer_comment_by_id` | Executes `confluence_cloud_get_footer_comment_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_footer_comment` | Executes `confluence_cloud_update_footer_comment` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_footer_comment` | Executes `confluence_cloud_delete_footer_comment` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_footer_comment_children` | Executes `confluence_cloud_get_footer_comment_children` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_footer_like_count` | Executes `confluence_cloud_get_footer_like_count` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_footer_comment_operations` | Executes `confluence_cloud_get_footer_comment_operations` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_footer_comment_versions` | Executes `confluence_cloud_get_footer_comment_versions` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_footer_comment_version_details` | Executes `confluence_cloud_get_footer_comment_version_details` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_inline_comments` | Executes `confluence_cloud_get_inline_comments` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_inline_comment` | Executes `confluence_cloud_create_inline_comment` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_inline_comment_by_id` | Executes `confluence_cloud_get_inline_comment_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_inline_comment` | Executes `confluence_cloud_update_inline_comment` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_inline_comment` | Executes `confluence_cloud_delete_inline_comment` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_inline_comment_children` | Executes `confluence_cloud_get_inline_comment_children` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_inline_like_count` | Executes `confluence_cloud_get_inline_like_count` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_inline_comment_operations` | Executes `confluence_cloud_get_inline_comment_operations` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_inline_comment_versions` | Executes `confluence_cloud_get_inline_comment_versions` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_inline_comment_version_details` | Executes `confluence_cloud_get_inline_comment_version_details` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_comment_content_properties` | Executes `confluence_cloud_get_comment_content_properties` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_create_comment_property` | Executes `confluence_cloud_create_comment_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_comment_content_properties_by_id` | Executes `confluence_cloud_get_comment_content_properties_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_comment_property_by_id` | Executes `confluence_cloud_update_comment_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_comment_property_by_id` | Executes `confluence_cloud_delete_comment_property_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_tasks` | Executes `confluence_cloud_get_tasks` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_task_by_id` | Executes `confluence_cloud_get_task_by_id` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_update_task` | Executes `confluence_cloud_update_task` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_child_custom_content` | Executes `confluence_cloud_get_child_custom_content` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_check_access_by_email` | Executes `confluence_cloud_check_access_by_email` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_invite_by_email` | Executes `confluence_cloud_invite_by_email` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_data_policy_metadata` | Executes `confluence_cloud_get_data_policy_metadata` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_classification_levels` | Executes `confluence_cloud_get_classification_levels` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_blog_post_classification_level` | Executes `confluence_cloud_get_blog_post_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_put_blog_post_classification_level` | Executes `confluence_cloud_put_blog_post_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_post_blog_post_classification_level` | Executes `confluence_cloud_post_blog_post_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_whiteboard_classification_level` | Executes `confluence_cloud_get_whiteboard_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_put_whiteboard_classification_level` | Executes `confluence_cloud_put_whiteboard_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_post_whiteboard_classification_level` | Executes `confluence_cloud_post_whiteboard_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_database_classification_level` | Executes `confluence_cloud_get_database_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_put_database_classification_level` | Executes `confluence_cloud_put_database_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_post_database_classification_level` | Executes `confluence_cloud_post_database_classification_level` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_forge_app_properties` | Executes `confluence_cloud_get_forge_app_properties` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_get_forge_app_property` | Executes `confluence_cloud_get_forge_app_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_put_forge_app_property` | Executes `confluence_cloud_put_forge_app_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_other` | `confluence_cloud_delete_forge_app_property` | Executes `confluence_cloud_delete_forge_app_property` within the `confluence-cloud-other` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachments` | Executes `confluence_cloud_get_attachments` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachment_by_id` | Executes `confluence_cloud_get_attachment_by_id` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_delete_attachment` | Executes `confluence_cloud_delete_attachment` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachment_labels` | Executes `confluence_cloud_get_attachment_labels` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachment_operations` | Executes `confluence_cloud_get_attachment_operations` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachment_content_properties` | Executes `confluence_cloud_get_attachment_content_properties` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_create_attachment_property` | Executes `confluence_cloud_create_attachment_property` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachment_content_properties_by_id` | Executes `confluence_cloud_get_attachment_content_properties_by_id` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_update_attachment_property_by_id` | Executes `confluence_cloud_update_attachment_property_by_id` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_delete_attachment_property_by_id` | Executes `confluence_cloud_delete_attachment_property_by_id` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachment_versions` | Executes `confluence_cloud_get_attachment_versions` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachment_version_details` | Executes `confluence_cloud_get_attachment_version_details` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_attachment_comments` | Executes `confluence_cloud_get_attachment_comments` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_blogpost_attachments` | Executes `confluence_cloud_get_blogpost_attachments` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_custom_content_attachments` | Executes `confluence_cloud_get_custom_content_attachments` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_attachment` | `confluence_cloud_get_label_attachments` | Executes `confluence_cloud_get_label_attachments` within the `confluence-cloud-attachment` category. |
| `confluence_cloud_confluence_cloud_label` | `confluence_cloud_get_blog_post_labels` | Executes `confluence_cloud_get_blog_post_labels` within the `confluence-cloud-label` category. |
| `confluence_cloud_confluence_cloud_label` | `confluence_cloud_get_custom_content_labels` | Executes `confluence_cloud_get_custom_content_labels` within the `confluence-cloud-label` category. |
| `confluence_cloud_confluence_cloud_label` | `confluence_cloud_get_labels` | Executes `confluence_cloud_get_labels` within the `confluence-cloud-label` category. |
| `confluence_cloud_confluence_cloud_label` | `confluence_cloud_get_label_blog_posts` | Executes `confluence_cloud_get_label_blog_posts` within the `confluence-cloud-label` category. |
| `confluence_cloud_confluence_cloud_user` | `confluence_cloud_get_blog_post_like_users` | Executes `confluence_cloud_get_blog_post_like_users` within the `confluence-cloud-user` category. |
| `confluence_cloud_confluence_cloud_user` | `confluence_cloud_get_footer_like_users` | Executes `confluence_cloud_get_footer_like_users` within the `confluence-cloud-user` category. |
| `confluence_cloud_confluence_cloud_user` | `confluence_cloud_get_inline_like_users` | Executes `confluence_cloud_get_inline_like_users` within the `confluence-cloud-user` category. |
| `confluence_cloud_confluence_cloud_user` | `confluence_cloud_create_bulk_user_lookup` | Executes `confluence_cloud_create_bulk_user_lookup` within the `confluence-cloud-user` category. |
| `confluence_cloud_confluence_cloud_content_property` | `confluence_cloud_create_custom_content_property` | Executes `confluence_cloud_create_custom_content_property` within the `confluence-cloud-content-property` category. |
| `confluence_cloud_confluence_cloud_content_property` | `confluence_cloud_update_custom_content_property_by_id` | Executes `confluence_cloud_update_custom_content_property_by_id` within the `confluence-cloud-content-property` category. |
| `confluence_cloud_confluence_cloud_content_property` | `confluence_cloud_delete_custom_content_property_by_id` | Executes `confluence_cloud_delete_custom_content_property_by_id` within the `confluence-cloud-content-property` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_label_pages` | Executes `confluence_cloud_get_label_pages` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_pages` | Executes `confluence_cloud_get_pages` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_create_page` | Executes `confluence_cloud_create_page` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_by_id` | Executes `confluence_cloud_get_page_by_id` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_update_page` | Executes `confluence_cloud_update_page` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_delete_page` | Executes `confluence_cloud_delete_page` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_attachments` | Executes `confluence_cloud_get_page_attachments` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_custom_content_by_type_in_page` | Executes `confluence_cloud_get_custom_content_by_type_in_page` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_labels` | Executes `confluence_cloud_get_page_labels` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_like_count` | Executes `confluence_cloud_get_page_like_count` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_like_users` | Executes `confluence_cloud_get_page_like_users` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_operations` | Executes `confluence_cloud_get_page_operations` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_create_page_property` | Executes `confluence_cloud_create_page_property` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_update_page_property_by_id` | Executes `confluence_cloud_update_page_property_by_id` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_delete_page_property_by_id` | Executes `confluence_cloud_delete_page_property_by_id` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_post_redact_page` | Executes `confluence_cloud_post_redact_page` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_update_page_title` | Executes `confluence_cloud_update_page_title` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_versions` | Executes `confluence_cloud_get_page_versions` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_version_details` | Executes `confluence_cloud_get_page_version_details` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_footer_comments` | Executes `confluence_cloud_get_page_footer_comments` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_inline_comments` | Executes `confluence_cloud_get_page_inline_comments` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_child_pages` | Executes `confluence_cloud_get_child_pages` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_direct_children` | Executes `confluence_cloud_get_page_direct_children` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_ancestors` | Executes `confluence_cloud_get_page_ancestors` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_descendants` | Executes `confluence_cloud_get_page_descendants` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_get_page_classification_level` | Executes `confluence_cloud_get_page_classification_level` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_put_page_classification_level` | Executes `confluence_cloud_put_page_classification_level` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_core` | `confluence_cloud_post_page_classification_level` | Executes `confluence_cloud_post_page_classification_level` within the `confluence-cloud-page-core` category. |
| `confluence_cloud_confluence_cloud_page_content` | `confluence_cloud_get_page_content_properties` | Executes `confluence_cloud_get_page_content_properties` within the `confluence-cloud-page-content` category. |
| `confluence_cloud_confluence_cloud_page_content` | `confluence_cloud_get_page_content_properties_by_id` | Executes `confluence_cloud_get_page_content_properties_by_id` within the `confluence-cloud-page-content` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_spaces` | Executes `confluence_cloud_get_spaces` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_create_space` | Executes `confluence_cloud_create_space` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_by_id` | Executes `confluence_cloud_get_space_by_id` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_blog_posts_in_space` | Executes `confluence_cloud_get_blog_posts_in_space` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_labels` | Executes `confluence_cloud_get_space_labels` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_content_labels` | Executes `confluence_cloud_get_space_content_labels` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_custom_content_by_type_in_space` | Executes `confluence_cloud_get_custom_content_by_type_in_space` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_operations` | Executes `confluence_cloud_get_space_operations` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_pages_in_space` | Executes `confluence_cloud_get_pages_in_space` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_properties` | Executes `confluence_cloud_get_space_properties` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_available_space_roles` | Executes `confluence_cloud_get_available_space_roles` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_create_space_role` | Executes `confluence_cloud_create_space_role` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_roles_by_id` | Executes `confluence_cloud_get_space_roles_by_id` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_update_space_role` | Executes `confluence_cloud_update_space_role` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_delete_space_role` | Executes `confluence_cloud_delete_space_role` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_role_mode` | Executes `confluence_cloud_get_space_role_mode` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_role_assignments` | Executes `confluence_cloud_get_space_role_assignments` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_set_space_role_assignments` | Executes `confluence_cloud_set_space_role_assignments` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_data_policy_spaces` | Executes `confluence_cloud_get_data_policy_spaces` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_get_space_default_classification_level` | Executes `confluence_cloud_get_space_default_classification_level` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_put_space_default_classification_level` | Executes `confluence_cloud_put_space_default_classification_level` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_core` | `confluence_cloud_delete_space_default_classification_level` | Executes `confluence_cloud_delete_space_default_classification_level` within the `confluence-cloud-space-core` category. |
| `confluence_cloud_confluence_cloud_space_property` | `confluence_cloud_create_space_property` | Executes `confluence_cloud_create_space_property` within the `confluence-cloud-space-property` category. |
| `confluence_cloud_confluence_cloud_space_property` | `confluence_cloud_get_space_property_by_id` | Executes `confluence_cloud_get_space_property_by_id` within the `confluence-cloud-space-property` category. |
| `confluence_cloud_confluence_cloud_space_property` | `confluence_cloud_update_space_property_by_id` | Executes `confluence_cloud_update_space_property_by_id` within the `confluence-cloud-space-property` category. |
| `confluence_cloud_confluence_cloud_space_property` | `confluence_cloud_delete_space_property_by_id` | Executes `confluence_cloud_delete_space_property_by_id` within the `confluence-cloud-space-property` category. |
| `confluence_cloud_confluence_cloud_space_permission` | `confluence_cloud_get_space_permissions_assignments` | Executes `confluence_cloud_get_space_permissions_assignments` within the `confluence-cloud-space-permission` category. |
| `confluence_cloud_confluence_cloud_space_permission` | `confluence_cloud_get_available_space_permissions` | Executes `confluence_cloud_get_available_space_permissions` within the `confluence-cloud-space-permission` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_access_mode_status` | Executes `confluence_server_get_access_mode_status` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create` | Executes `confluence_server_create` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete` | Executes `confluence_server_delete` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_change_password` | Executes `confluence_server_change_password` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_1` | Executes `confluence_server_delete_1` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_disable` | Executes `confluence_server_disable` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_enable` | Executes `confluence_server_enable` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_attachments` | Executes `confluence_server_get_attachments` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_attachments` | Executes `confluence_server_create_attachments` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_attachment_extracted_text` | Executes `confluence_server_get_attachment_extracted_text` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_move` | Executes `confluence_server_move` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update` | Executes `confluence_server_update` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_remove_attachment` | Executes `confluence_server_remove_attachment` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_remove_attachment_version` | Executes `confluence_server_remove_attachment_version` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_data` | Executes `confluence_server_update_data` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_audit_records` | Executes `confluence_server_get_audit_records` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_cancel_all_queued_jobs` | Executes `confluence_server_cancel_all_queued_jobs` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_cancel_job` | Executes `confluence_server_cancel_job` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_site_backup_job` | Executes `confluence_server_create_site_backup_job` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_site_restore_job` | Executes `confluence_server_create_site_restore_job` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_site_restore_job_for_uploaded_backup_file` | Executes `confluence_server_create_site_restore_job_for_uploaded_backup_file` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_download_backup_file` | Executes `confluence_server_download_backup_file` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_find_jobs` | Executes `confluence_server_find_jobs` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_files` | Executes `confluence_server_get_files` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_job` | Executes `confluence_server_get_job` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_remove_category` | Executes `confluence_server_remove_category` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_publish_shared_draft` | Executes `confluence_server_publish_shared_draft` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_publish_legacy_draft` | Executes `confluence_server_publish_legacy_draft` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_convert` | Executes `confluence_server_convert` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_labels` | Executes `confluence_server_labels` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_add_labels` | Executes `confluence_server_add_labels` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_label_with_query_param` | Executes `confluence_server_delete_label_with_query_param` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_label` | Executes `confluence_server_delete_label` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_find_all` | Executes `confluence_server_find_all` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_1` | Executes `confluence_server_create_1` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_find_by_key` | Executes `confluence_server_find_by_key` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_1` | Executes `confluence_server_update_1` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_2` | Executes `confluence_server_create_2` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_2` | Executes `confluence_server_delete_2` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_3` | Executes `confluence_server_delete_3` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_history` | Executes `confluence_server_get_history` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_macro_body_by_hash` | Executes `confluence_server_get_macro_body_by_hash` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_macro_body_by_macro_id` | Executes `confluence_server_get_macro_body_by_macro_id` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_search` | Executes `confluence_server_search` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_2` | Executes `confluence_server_update_2` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_by_operation` | Executes `confluence_server_by_operation` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_for_operation` | Executes `confluence_server_for_operation` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_relevant_view_restrictions` | Executes `confluence_server_relevant_view_restrictions` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_restrictions` | Executes `confluence_server_update_restrictions` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_index` | Executes `confluence_server_index` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_descendants` | Executes `confluence_server_descendants` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_descendants_of_type` | Executes `confluence_server_descendants_of_type` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_default_color_scheme` | Executes `confluence_server_get_default_color_scheme` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_global_color_scheme` | Executes `confluence_server_get_global_color_scheme` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_color_scheme` | Executes `confluence_server_update_color_scheme` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_reset_global_color_scheme` | Executes `confluence_server_reset_global_color_scheme` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_all_global_permissions` | Executes `confluence_server_get_all_global_permissions` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_find_webhooks` | Executes `confluence_server_find_webhooks` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_webhook` | Executes `confluence_server_create_webhook` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_webhook` | Executes `confluence_server_get_webhook` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_webhook` | Executes `confluence_server_update_webhook` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_webhook` | Executes `confluence_server_delete_webhook` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_latest_invocation` | Executes `confluence_server_get_latest_invocation` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_statistics` | Executes `confluence_server_get_statistics` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_statistics_summary` | Executes `confluence_server_get_statistics_summary` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_test_webhook` | Executes `confluence_server_test_webhook` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_members` | Executes `confluence_server_get_members` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_index_1` | Executes `confluence_server_index_1` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_related_labels` | Executes `confluence_server_get_related_labels` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_recent` | Executes `confluence_server_recent` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_task` | Executes `confluence_server_get_task` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_tasks` | Executes `confluence_server_get_tasks` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_search_1` | Executes `confluence_server_search_1` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_index_2` | Executes `confluence_server_index_2` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_color_scheme_type` | Executes `confluence_server_get_color_scheme_type` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_color_scheme_type` | Executes `confluence_server_update_color_scheme_type` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_index_3` | Executes `confluence_server_index_3` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_popular` | Executes `confluence_server_popular` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_recent_1` | Executes `confluence_server_recent_1` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_related` | Executes `confluence_server_related` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_set_permissions` | Executes `confluence_server_set_permissions` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_1` | Executes `confluence_server_get_1` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_3` | Executes `confluence_server_create_3` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get` | Executes `confluence_server_get` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_3` | Executes `confluence_server_update_3` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_create_4` | Executes `confluence_server_create_4` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_4` | Executes `confluence_server_delete_4` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_archive` | Executes `confluence_server_archive` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_4` | Executes `confluence_server_update_4` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_5` | Executes `confluence_server_delete_5` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_restore` | Executes `confluence_server_restore` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_trash` | Executes `confluence_server_trash` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_index_4` | Executes `confluence_server_index_4` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_update_5` | Executes `confluence_server_update_5` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_delete_6` | Executes `confluence_server_delete_6` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_change_password_1` | Executes `confluence_server_change_password_1` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_anonymous` | Executes `confluence_server_get_anonymous` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_other` | `confluence_server_get_current` | Executes `confluence_server_get_current` within the `confluence-server-other` category. |
| `confluence_server_confluence_server_user` | `confluence_server_create_user` | Executes `confluence_server_create_user` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_get_permissions_granted_to_anonymous_users` | Executes `confluence_server_get_permissions_granted_to_anonymous_users` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_get_permissions_granted_to_unlicensed_users` | Executes `confluence_server_get_permissions_granted_to_unlicensed_users` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_get_permissions_granted_to_user` | Executes `confluence_server_get_permissions_granted_to_user` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_get_permissions_granted_to_anonymous_users_1` | Executes `confluence_server_get_permissions_granted_to_anonymous_users_1` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_get_permissions_granted_to_user_1` | Executes `confluence_server_get_permissions_granted_to_user_1` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_grant_permissions_to_anonymous_users` | Executes `confluence_server_grant_permissions_to_anonymous_users` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_grant_permissions_to_user` | Executes `confluence_server_grant_permissions_to_user` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_revoke_permissions_from_anonymous_user` | Executes `confluence_server_revoke_permissions_from_anonymous_user` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_revoke_permissions_from_user` | Executes `confluence_server_revoke_permissions_from_user` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_get_user` | Executes `confluence_server_get_user` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_user` | `confluence_server_get_users` | Executes `confluence_server_get_users` within the `confluence-server-user` category. |
| `confluence_server_confluence_server_space` | `confluence_server_create_space_backup_job` | Executes `confluence_server_create_space_backup_job` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_create_space_restore_job` | Executes `confluence_server_create_space_restore_job` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_create_space_restore_job_for_uploaded_backup_file` | Executes `confluence_server_create_space_restore_job_for_uploaded_backup_file` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_get_space_color_scheme` | Executes `confluence_server_get_space_color_scheme` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_update_space_color_scheme` | Executes `confluence_server_update_space_color_scheme` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_reset_space_color_scheme` | Executes `confluence_server_reset_space_color_scheme` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_create_private_space` | Executes `confluence_server_create_private_space` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_spaces` | Executes `confluence_server_spaces` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_create_space` | Executes `confluence_server_create_space` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_space` | Executes `confluence_server_space` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_is_watching_space` | Executes `confluence_server_is_watching_space` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_add_space_watch` | Executes `confluence_server_add_space_watch` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_space` | `confluence_server_remove_space_watch` | Executes `confluence_server_remove_space_watch` within the `confluence-server-space` category. |
| `confluence_server_confluence_server_content_child` | `confluence_server_children` | Executes `confluence_server_children` within the `confluence-server-content-child` category. |
| `confluence_server_confluence_server_content_child` | `confluence_server_children_of_type` | Executes `confluence_server_children_of_type` within the `confluence-server-content-child` category. |
| `confluence_server_confluence_server_content` | `confluence_server_comments_of_content` | Executes `confluence_server_comments_of_content` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_get_content` | Executes `confluence_server_get_content` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_create_content` | Executes `confluence_server_create_content` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_get_content_by_id` | Executes `confluence_server_get_content_by_id` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_scan_content` | Executes `confluence_server_scan_content` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_contents` | Executes `confluence_server_contents` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_contents_with_type` | Executes `confluence_server_contents_with_type` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_is_watching_content` | Executes `confluence_server_is_watching_content` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_add_content_watcher` | Executes `confluence_server_add_content_watcher` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content` | `confluence_server_remove_content_watcher` | Executes `confluence_server_remove_content_watcher` within the `confluence-server-content` category. |
| `confluence_server_confluence_server_content_history` | `confluence_server_delete_content_history` | Executes `confluence_server_delete_content_history` within the `confluence-server-content-history` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_permissions_granted_to_group` | Executes `confluence_server_get_permissions_granted_to_group` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_ancestor_groups` | Executes `confluence_server_get_ancestor_groups` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_ancestor_groups_by_group_name` | Executes `confluence_server_get_ancestor_groups_by_group_name` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_group` | Executes `confluence_server_get_group` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_group_by_group_name` | Executes `confluence_server_get_group_by_group_name` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_groups` | Executes `confluence_server_get_groups` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_members_by_group_name` | Executes `confluence_server_get_members_by_group_name` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_nested_group_members` | Executes `confluence_server_get_nested_group_members` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_nested_group_members_by_group_name` | Executes `confluence_server_get_nested_group_members_by_group_name` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_parent_groups` | Executes `confluence_server_get_parent_groups` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_parent_groups_by_group_name` | Executes `confluence_server_get_parent_groups_by_group_name` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_permissions_granted_to_group_1` | Executes `confluence_server_get_permissions_granted_to_group_1` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_grant_permissions_to_group` | Executes `confluence_server_grant_permissions_to_group` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_revoke_permissions_from_group` | Executes `confluence_server_revoke_permissions_from_group` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_group` | `confluence_server_get_groups_1` | Executes `confluence_server_get_groups_1` within the `confluence-server-group` category. |
| `confluence_server_confluence_server_space_permission` | `confluence_server_get_all_space_permissions` | Executes `confluence_server_get_all_space_permissions` within the `confluence-server-space-permission` category. |
| `dlp_cloud_atlassian_dlp` | `dlp_cloud_create_level` | Executes `dlp_cloud_create_level` within the `atlassian-dlp` category. |
| `dlp_cloud_atlassian_dlp` | `dlp_cloud_get_level_list` | Executes `dlp_cloud_get_level_list` within the `atlassian-dlp` category. |
| `dlp_cloud_atlassian_dlp` | `dlp_cloud_get_level` | Executes `dlp_cloud_get_level` within the `atlassian-dlp` category. |
| `dlp_cloud_atlassian_dlp` | `dlp_cloud_edit_level` | Executes `dlp_cloud_edit_level` within the `atlassian-dlp` category. |
| `dlp_cloud_atlassian_dlp` | `dlp_cloud_publish_level` | Executes `dlp_cloud_publish_level` within the `atlassian-dlp` category. |
| `dlp_cloud_atlassian_dlp` | `dlp_cloud_archive_level` | Executes `dlp_cloud_archive_level` within the `atlassian-dlp` category. |
| `dlp_cloud_atlassian_dlp` | `dlp_cloud_restore_level` | Executes `dlp_cloud_restore_level` within the `atlassian-dlp` category. |
| `dlp_cloud_atlassian_dlp` | `dlp_cloud_reorder` | Executes `dlp_cloud_reorder` within the `atlassian-dlp` category. |
| `user_mgmt_cloud_atlassian_user_mgmt` | `user_mgmt_cloud_get_users_account_id_manage` | Executes `user_mgmt_cloud_get_users_account_id_manage` within the `atlassian-user-mgmt` category. |
| `user_mgmt_cloud_atlassian_user_mgmt` | `user_mgmt_cloud_get_users_account_id_manage_profile` | Executes `user_mgmt_cloud_get_users_account_id_manage_profile` within the `atlassian-user-mgmt` category. |
| `user_mgmt_cloud_atlassian_user_mgmt` | `user_mgmt_cloud_patch_users_account_id_manage_profile` | Executes `user_mgmt_cloud_patch_users_account_id_manage_profile` within the `atlassian-user-mgmt` category. |
| `user_mgmt_cloud_atlassian_user_mgmt` | `user_mgmt_cloud_put_users_account_id_manage_email` | Executes `user_mgmt_cloud_put_users_account_id_manage_email` within the `atlassian-user-mgmt` category. |
| `user_mgmt_cloud_atlassian_user_mgmt` | `user_mgmt_cloud_get_users_account_id_manage_api_tokens` | Executes `user_mgmt_cloud_get_users_account_id_manage_api_tokens` within the `atlassian-user-mgmt` category. |
| `user_mgmt_cloud_atlassian_user_mgmt` | `user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id` | Executes `user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id` within the `atlassian-user-mgmt` category. |
| `user_mgmt_cloud_atlassian_user_mgmt` | `user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete` | Executes `user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete` within the `atlassian-user-mgmt` category. |
| `user_mgmt_cloud_atlassian` | `user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable` | Executes `user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable` within the `atlassian` category. |
| `user_mgmt_cloud_atlassian` | `user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable` | Executes `user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable` within the `atlassian` category. |
| `user_mgmt_cloud_atlassian` | `user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete` | Executes `user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete` within the `atlassian` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_orgs` | Executes `admin_cloud_get_orgs` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_org_by_id` | Executes `admin_cloud_get_org_by_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_directory_users` | Executes `admin_cloud_get_directory_users` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_directory_user_details` | Executes `admin_cloud_get_directory_user_details` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_users` | Executes `admin_cloud_get_users` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v2_orgs_org_id_users_invite` | Executes `admin_cloud_post_v2_orgs_org_id_users_invite` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_user_role_assignments` | Executes `admin_cloud_get_user_role_assignments` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_assign_role` | Executes `admin_cloud_assign_role` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_revoke_role` | Executes `admin_cloud_revoke_role` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` | Executes `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` | Executes `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` | Executes `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` | Executes `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` | Executes `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_directory_users_count` | Executes `admin_cloud_get_directory_users_count` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_user_stats` | Executes `admin_cloud_get_user_stats` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` | Executes `admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_search_users` | Executes `admin_cloud_search_users` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v1_orgs_org_id_users_invite` | Executes `admin_cloud_post_v1_orgs_org_id_users_invite` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` | Executes `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` | Executes `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_delete_v1_orgs_org_id_directory_users_account_id` | Executes `admin_cloud_delete_v1_orgs_org_id_directory_users_account_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_groups` | Executes `admin_cloud_get_groups` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups` | Executes `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_group_role_assignments` | Executes `admin_cloud_get_group_role_assignments` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` | Executes `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` | Executes `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` | Executes `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` | Executes `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` | Executes `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_group` | Executes `admin_cloud_get_group` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_groups_count` | Executes `admin_cloud_get_groups_count` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_groups_stats` | Executes `admin_cloud_get_groups_stats` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_search_groups` | Executes `admin_cloud_search_groups` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v1_orgs_org_id_directory_groups` | Executes `admin_cloud_post_v1_orgs_org_id_directory_groups` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id` | Executes `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_assign_role_to_group` | Executes `admin_cloud_assign_role_to_group` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_revoke_role_to_group` | Executes `admin_cloud_revoke_role_to_group` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` | Executes `admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` | Executes `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_directories_for_org` | Executes `admin_cloud_get_directories_for_org` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_domains` | Executes `admin_cloud_get_domains` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_domain_by_id` | Executes `admin_cloud_get_domain_by_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_events` | Executes `admin_cloud_get_events` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_poll_events` | Executes `admin_cloud_poll_events` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_event_by_id` | Executes `admin_cloud_get_event_by_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_event_actions` | Executes `admin_cloud_get_event_actions` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_policies` | Executes `admin_cloud_get_policies` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_create_policy` | Executes `admin_cloud_create_policy` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_get_policy_by_id` | Executes `admin_cloud_get_policy_by_id` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_update_policy` | Executes `admin_cloud_update_policy` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_delete_policy` | Executes `admin_cloud_delete_policy` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_add_resource_to_policy` | Executes `admin_cloud_add_resource_to_policy` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_update_policy_resource` | Executes `admin_cloud_update_policy_resource` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_delete_policy_resource` | Executes `admin_cloud_delete_policy_resource` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_validate_policy` | Executes `admin_cloud_validate_policy` within the `atlassian-admin` category. |
| `admin_cloud_atlassian_admin` | `admin_cloud_query_workspaces_v2` | Executes `admin_cloud_query_workspaces_v2` within the `atlassian-admin` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_get_all_api_tokens_by_org_id` | Executes `api_access_cloud_get_all_api_tokens_by_org_id` within the `atlassian-api-access` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_bulk_revoke_api_tokens` | Executes `api_access_cloud_bulk_revoke_api_tokens` within the `atlassian-api-access` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_get_api_token_count_by_org_id` | Executes `api_access_cloud_get_api_token_count_by_org_id` within the `atlassian-api-access` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_count_service_account_api_tokens` | Executes `api_access_cloud_count_service_account_api_tokens` within the `atlassian-api-access` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_get_service_account_api_token` | Executes `api_access_cloud_get_service_account_api_token` within the `atlassian-api-access` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_revoke_api_tokens` | Executes `api_access_cloud_revoke_api_tokens` within the `atlassian-api-access` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_get_api_key_count_by_org_id` | Executes `api_access_cloud_get_api_key_count_by_org_id` within the `atlassian-api-access` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_get_all_api_keys_by_org_id` | Executes `api_access_cloud_get_all_api_keys_by_org_id` within the `atlassian-api-access` category. |
| `api_access_cloud_atlassian_api_access` | `api_access_cloud_revoke_api_key` | Executes `api_access_cloud_revoke_api_key` within the `atlassian-api-access` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get` | Executes `user_provisioning_cloud_get` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_put` | Executes `user_provisioning_cloud_put` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_delete_a_group` | Executes `user_provisioning_cloud_delete_a_group` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_patch` | Executes `user_provisioning_cloud_patch` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_all_groups_from_an_active_directory` | Executes `user_provisioning_cloud_get_all_groups_from_an_active_directory` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_create_a_group_in_active_directory` | Executes `user_provisioning_cloud_create_a_group_in_active_directory` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_schemas` | Executes `user_provisioning_cloud_get_schemas` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_resource_types` | Executes `user_provisioning_cloud_get_resource_types` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_user_resource_type` | Executes `user_provisioning_cloud_get_user_resource_type` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_group_resource_type` | Executes `user_provisioning_cloud_get_group_resource_type` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_user_schemas` | Executes `user_provisioning_cloud_get_user_schemas` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_group_schemas` | Executes `user_provisioning_cloud_get_group_schemas` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_extension_user_schemas` | Executes `user_provisioning_cloud_get_extension_user_schemas` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_config` | Executes `user_provisioning_cloud_get_config` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_a_user_from_active_directory` | Executes `user_provisioning_cloud_get_a_user_from_active_directory` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_update_user_information_in_an_active_directory` | Executes `user_provisioning_cloud_update_user_information_in_an_active_directory` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_delete_a_user_from_an_active_directory` | Executes `user_provisioning_cloud_delete_a_user_from_an_active_directory` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_patch_user_information_in_an_active_directory` | Executes `user_provisioning_cloud_patch_user_information_in_an_active_directory` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_users_from_an_active_directory` | Executes `user_provisioning_cloud_get_users_from_an_active_directory` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_create_a_user_in_an_active_directory` | Executes `user_provisioning_cloud_create_a_user_in_an_active_directory` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db` | Executes `user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_scim_links` | Executes `user_provisioning_cloud_get_scim_links` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_get_scim_links_by_email` | Executes `user_provisioning_cloud_get_scim_links_by_email` within the `atlassian-user-provisioning` category. |
| `user_provisioning_cloud_atlassian_user_provisioning` | `user_provisioning_cloud_unlink_scim_user` | Executes `user_provisioning_cloud_unlink_scim_user` within the `atlassian-user-provisioning` category. |
