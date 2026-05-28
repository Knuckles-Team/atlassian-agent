# Atlassian Agent
## CLI or API | MCP | Agent

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

*Version: 0.16.0*

---

## Overview

**Atlassian Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Comprehensive AI agent for Jira and Confluence management..

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Comprehensive AI agent for Jira and Confluence management. API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools
| Tool Module | Toggle Env Var | Enabled by Default | Description & Nested Methods |
|-------------|----------------|--------------------|------------------------------|
| **Atlassian Control** | `ATLASSIAN_CONTROL_TOOL` | `True` | Manage atlassian control operations. Action-routed methods: `control_cloud_ap_is_add_users_to_policy`, `control_cloud_ap_is_attach_detach_resources_v2`, `control_cloud_ap_is_bulk_fetch_auth_policy`, `control_cloud_ap_is_create_policy`, `control_cloud_ap_is_create_policy_v2`, `control_cloud_ap_is_create_resource`, `control_cloud_ap_is_delete_policy`, `control_cloud_ap_is_delete_resource`, `control_cloud_ap_is_delete_resources`, `control_cloud_ap_is_delete_resources_v2`, `control_cloud_ap_is_get_policies`, `control_cloud_ap_is_get_policies_v2`, `control_cloud_ap_is_get_policy`, `control_cloud_ap_is_get_policy_v2`, `control_cloud_ap_is_get_resources`, `control_cloud_ap_is_get_resources_v2`, `control_cloud_ap_is_get_task_status`, `control_cloud_ap_is_publish_draft_policies`, `control_cloud_ap_is_update_policy`, `control_cloud_ap_is_update_policy_v2`, `control_cloud_ap_is_update_resource`, `control_cloud_ap_is_validate_policy`. |
| **Atlassian Org** | `ATLASSIAN_ORG_TOOL` | `True` | Manage atlassian org operations. Action-routed methods: `org_cloud_add_resource_to_policy`, `org_cloud_assign_role`, `org_cloud_assign_role_to_group`, `org_cloud_create_policy`, `org_cloud_delete_policy`, `org_cloud_delete_policy_resource`, `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id`, `org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id`, `org_cloud_delete_v1_orgs_org_id_directory_users_account_id`, `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id`, `org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id`, `org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id`, `org_cloud_get_directories_for_org`, `org_cloud_get_directory_user_details`, `org_cloud_get_directory_users`, `org_cloud_get_directory_users_count`, `org_cloud_get_domain_by_id`, `org_cloud_get_domains`, `org_cloud_get_event_actions`, `org_cloud_get_event_by_id`, `org_cloud_get_events`, `org_cloud_get_group`, `org_cloud_get_group_role_assignments`, `org_cloud_get_groups`, `org_cloud_get_groups_count`, `org_cloud_get_groups_stats`, `org_cloud_get_org_by_id`, `org_cloud_get_orgs`, `org_cloud_get_policies`, `org_cloud_get_policy_by_id`, `org_cloud_get_user_role_assignments`, `org_cloud_get_user_stats`, `org_cloud_get_users`, `org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates`, `org_cloud_poll_events`, `org_cloud_post_v1_orgs_org_id_directory_groups`, `org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships`, `org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access`, `org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access`, `org_cloud_post_v1_orgs_org_id_users_invite`, `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign`, `org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke`, `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups`, `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships`, `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign`, `org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke`, `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore`, `org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend`, `org_cloud_post_v2_orgs_org_id_users_invite`, `org_cloud_query_workspaces_v2`, `org_cloud_revoke_role`, `org_cloud_revoke_role_to_group`, `org_cloud_search_groups`, `org_cloud_search_users`, `org_cloud_update_policy`, `org_cloud_update_policy_resource`, `org_cloud_validate_policy`. |
| **Atlassian Dlp** | `ATLASSIAN_DLP_TOOL` | `True` | Manage atlassian dlp operations. Action-routed methods: `dlp_cloud_archive_level`, `dlp_cloud_create_level`, `dlp_cloud_edit_level`, `dlp_cloud_get_level`, `dlp_cloud_get_level_list`, `dlp_cloud_publish_level`, `dlp_cloud_reorder`, `dlp_cloud_restore_level`. |
| **Atlassian User Mgmt** | `ATLASSIAN_USER_MGMT_TOOL` | `True` | Manage atlassian user mgmt operations. Action-routed methods: `user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id`, `user_mgmt_cloud_get_users_account_id_manage`, `user_mgmt_cloud_get_users_account_id_manage_api_tokens`, `user_mgmt_cloud_get_users_account_id_manage_profile`, `user_mgmt_cloud_patch_users_account_id_manage_profile`, `user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete`, `user_mgmt_cloud_put_users_account_id_manage_email`. |
| **Atlassian Admin** | `ATLASSIAN_ADMIN_TOOL` | `True` | Manage atlassian admin operations. Action-routed methods: `admin_cloud_add_resource_to_policy`, `admin_cloud_assign_role`, `admin_cloud_assign_role_to_group`, `admin_cloud_create_policy`, `admin_cloud_delete_policy`, `admin_cloud_delete_policy_resource`, `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id`, `admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id`, `admin_cloud_delete_v1_orgs_org_id_directory_users_account_id`, `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id`, `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id`, `admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id`, `admin_cloud_get_directories_for_org`, `admin_cloud_get_directory_user_details`, `admin_cloud_get_directory_users`, `admin_cloud_get_directory_users_count`, `admin_cloud_get_domain_by_id`, `admin_cloud_get_domains`, `admin_cloud_get_event_actions`, `admin_cloud_get_event_by_id`, `admin_cloud_get_events`, `admin_cloud_get_group`, `admin_cloud_get_group_role_assignments`, `admin_cloud_get_groups`, `admin_cloud_get_groups_count`, `admin_cloud_get_groups_stats`, `admin_cloud_get_org_by_id`, `admin_cloud_get_orgs`, `admin_cloud_get_policies`, `admin_cloud_get_policy_by_id`, `admin_cloud_get_user_role_assignments`, `admin_cloud_get_user_stats`, `admin_cloud_get_users`, `admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates`, `admin_cloud_poll_events`, `admin_cloud_post_v1_orgs_org_id_directory_groups`, `admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships`, `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access`, `admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access`, `admin_cloud_post_v1_orgs_org_id_users_invite`, `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign`, `admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke`, `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups`, `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships`, `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign`, `admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke`, `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore`, `admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend`, `admin_cloud_post_v2_orgs_org_id_users_invite`, `admin_cloud_query_workspaces_v2`, `admin_cloud_revoke_role`, `admin_cloud_revoke_role_to_group`, `admin_cloud_search_groups`, `admin_cloud_search_users`, `admin_cloud_update_policy`, `admin_cloud_update_policy_resource`, `admin_cloud_validate_policy`. |
| **Atlassian Api Access** | `ATLASSIAN_API_ACCESS_TOOL` | `True` | Manage atlassian api access operations. Action-routed methods: `api_access_cloud_bulk_revoke_api_tokens`, `api_access_cloud_count_service_account_api_tokens`, `api_access_cloud_get_all_api_keys_by_org_id`, `api_access_cloud_get_all_api_tokens_by_org_id`, `api_access_cloud_get_api_key_count_by_org_id`, `api_access_cloud_get_api_token_count_by_org_id`, `api_access_cloud_get_service_account_api_token`, `api_access_cloud_revoke_api_key`, `api_access_cloud_revoke_api_tokens`. |
| **Atlassian User Provisioning** | `ATLASSIAN_USER_PROVISIONING_TOOL` | `True` | Manage atlassian user provisioning operations. Action-routed methods: `user_provisioning_cloud_create_a_group_in_active_directory`, `user_provisioning_cloud_create_a_user_in_an_active_directory`, `user_provisioning_cloud_delete_a_group`, `user_provisioning_cloud_delete_a_user_from_an_active_directory`, `user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db`, `user_provisioning_cloud_get`, `user_provisioning_cloud_get_a_user_from_active_directory`, `user_provisioning_cloud_get_all_groups_from_an_active_directory`, `user_provisioning_cloud_get_config`, `user_provisioning_cloud_get_extension_user_schemas`, `user_provisioning_cloud_get_group_resource_type`, `user_provisioning_cloud_get_group_schemas`, `user_provisioning_cloud_get_resource_types`, `user_provisioning_cloud_get_schemas`, `user_provisioning_cloud_get_scim_links`, `user_provisioning_cloud_get_scim_links_by_email`, `user_provisioning_cloud_get_user_resource_type`, `user_provisioning_cloud_get_user_schemas`, `user_provisioning_cloud_get_users_from_an_active_directory`, `user_provisioning_cloud_patch`, `user_provisioning_cloud_patch_user_information_in_an_active_directory`, `user_provisioning_cloud_put`, `user_provisioning_cloud_unlink_scim_user`, `user_provisioning_cloud_update_user_information_in_an_active_directory`. |
| **Atlassian** | `ATLASSIAN_TOOL` | `True` | Manage atlassian operations. Action-routed methods: `user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete`, `user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable`, `user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable`. |
| **Jira Project** | `JIRA_PROJECT_TOOL` | `True` | Manage Jira project operations. |
| **Jira User** | `JIRA_USER_TOOL` | `True` | Manage Jira user operations. |
| **Jira Issue** | `JIRA_ISSUE_TOOL` | `True` | Manage Jira issue operations. |
| **Jira Comment** | `JIRA_COMMENT_TOOL` | `True` | Manage Jira comment operations. |
| **Jira Field** | `JIRA_FIELD_TOOL` | `True` | Manage Jira field operations. |
| **Jira Screen** | `JIRA_SCREEN_TOOL` | `True` | Manage Jira screen operations. |
| **Jira Workflow** | `JIRA_WORKFLOW_TOOL` | `True` | Manage Jira workflow operations. |
| **Jira Other** | `JIRA_OTHER_TOOL` | `True` | Manage Jira other operations. |
| **Confluence Page** | `CONFLUENCE_PAGE_TOOL` | `True` | Manage Confluence page operations. |
| **Confluence Space** | `CONFLUENCE_SPACE_TOOL` | `True` | Manage Confluence space operations. |
| **Confluence User** | `CONFLUENCE_USER_TOOL` | `True` | Manage Confluence user operations. |
| **Confluence Other** | `CONFLUENCE_OTHER_TOOL` | `True` | Manage Confluence other operations. |

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](docs/mcp.md).

### Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows you to restrict the set of exposed tools in order to prevent blowing up the LLM's context window.

You can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to your transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.

---

### MCP Configuration Examples

#### stdio Transport (Recommended for local IDEs e.g., Cursor, Claude Desktop)
Configure your IDE's `mcp.json` to launch the MCP server via `uvx`:

```json
{
  "mcpServers": {
    "atlassian-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "atlassian-agent",
        "atlassian-mcp"
      ],
      "env": {
        "ATLASSIAN_AGENT_URL": "your_atlassian_agent_url_here",
        "ATLASSIAN_AGENT_USER": "your_atlassian_agent_user_here",
        "ATLASSIAN_AGENT_TOKEN": "your_atlassian_agent_token_here",
        "ATLASSIAN_AGENT_VERIFY": "your_atlassian_agent_verify_here",
        "DEBUG": "your_debug_here",
        "PYTHONUNBUFFERED": "your_pythonunbuffered_here"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (Recommended for production deployments)
Configure your client's `mcp.json` to launch the Streamable-HTTP server via `uvx` with explicit host and port definition:

```json
{
  "mcpServers": {
    "atlassian-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "atlassian-agent",
        "atlassian-mcp"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "ATLASSIAN_AGENT_URL": "your_atlassian_agent_url_here",
        "ATLASSIAN_AGENT_USER": "your_atlassian_agent_user_here",
        "ATLASSIAN_AGENT_TOKEN": "your_atlassian_agent_token_here",
        "ATLASSIAN_AGENT_VERIFY": "your_atlassian_agent_verify_here",
        "DEBUG": "your_debug_here",
        "PYTHONUNBUFFERED": "your_pythonunbuffered_here"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed remote or local Streamable-HTTP instance:

```json
{
  "mcpServers": {
    "atlassian-agent": {
      "url": "http://localhost:8000/atlassian-agent/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name atlassian-agent-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e ATLASSIAN_AGENT_URL="your_value" \
  -e ATLASSIAN_AGENT_USER="your_value" \
  -e ATLASSIAN_AGENT_TOKEN="your_value" \
  -e ATLASSIAN_AGENT_VERIFY="your_value" \
  -e DEBUG="your_value" \
  -e PYTHONUNBUFFERED="your_value" \
  knucklessg1/atlassian-agent:latest
```

---

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export ATLASSIAN_AGENT_URL="your_value"
export ATLASSIAN_AGENT_USER="your_value"
export ATLASSIAN_AGENT_TOKEN="your_value"
export ATLASSIAN_AGENT_VERIFY="your_value"
export DEBUG="your_value"
export PYTHONUNBUFFERED="your_value"

# Run the agent server
atlassian-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

services:
  atlassian-agent-mcp:
    image: knucklessg1/atlassian-agent:latest
    container_name: atlassian-agent-mcp
    hostname: atlassian-agent-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  atlassian-agent-agent:
    image: knucklessg1/atlassian-agent:latest
    container_name: atlassian-agent-agent
    hostname: atlassian-agent-agent
    restart: always
    depends_on:
      - atlassian-agent-mcp
    env_file:
      - ../.env
    command: [ "atlassian-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://atlassian-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9004:9004"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9004/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](docs/agent.md).

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Install the Python package locally:

```bash
# Using uv (highly recommended)
uv pip install atlassian-agent[all]

# Using standard pip
python -m pip install atlassian-agent[all]
```

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`
