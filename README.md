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

*Version: 0.32.0*

> **Documentation** — Installation, deployment, and usage across the MCP, Python API,
> and CLI interfaces, along with guidance for connecting to Atlassian Cloud and
> Server instances, are maintained in the [official documentation](https://knuckles-team.github.io/atlassian-agent/).

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

The table below is auto-generated from the live server — do not edit by hand.

<!-- MCP-TOOLS-TABLE:START -->

#### Condensed action-routed tools (default — `MCP_TOOL_MODE=condensed`)

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `atlassian_atlassian` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian_admin` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_api_access` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_control` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_dlp` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_org` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_user_mgmt` | `ATLASSIAN_USER_MGMTTOOL` | Manage atlassian user mgmt operations. |
| `atlassian_atlassian_user_provisioning` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_confluence_other` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_page` | `CONFLUENCE_PAGETOOL` | Manage Confluence page operations. |
| `atlassian_confluence_space` | `CONFLUENCE_SPACETOOL` | Manage Confluence space operations. |
| `atlassian_confluence_user` | `CONFLUENCE_USERTOOL` | Manage Confluence user operations. |
| `atlassian_jira_comment` | `JIRA_COMMENTTOOL` | Manage Jira comment operations. |
| `atlassian_jira_field` | `JIRA_FIELDTOOL` | Manage Jira field operations. |
| `atlassian_jira_issue` | `JIRA_ISSUETOOL` | Manage Jira issue operations. |
| `atlassian_jira_other` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_project` | `JIRA_PROJECTTOOL` | Manage Jira project operations. |
| `atlassian_jira_screen` | `JIRA_SCREENTOOL` | Manage Jira screen operations. |
| `atlassian_jira_user` | `JIRA_USERTOOL` | Manage Jira user operations. |
| `atlassian_jira_workflow` | `JIRA_WORKFLOWTOOL` | Manage Jira workflow operations. |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>1 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `atlassian_request` | `BASE_ATLASSIAN_CLIENTTOOL` | Invoke the request operation. |

</details>

_20 action-routed tool(s) (default) · 1 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (`condensed` default · `verbose` 1:1 · `both`). Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

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

> **Install the slim `[mcp]` extra.** All examples below install
> `atlassian-agent[mcp]` — the MCP-server extra that pulls only the FastMCP /
> FastAPI tooling (`agent-utilities[mcp]`). It deliberately **excludes** the heavy
> agent runtime (the epistemic-graph engine, `pydantic-ai`, `dspy`, `llama-index`,
> `tree-sitter`), so `uvx`/container installs are dramatically smaller and faster.
> Use the full `[agent]` extra only when you need the integrated Pydantic AI agent
> (see [Installation](#installation)).

#### stdio Transport (Recommended for local IDEs e.g., Cursor, Claude Desktop)
Configure your IDE's `mcp.json` to launch the MCP server via `uvx`:

```json
{
  "mcpServers": {
    "atlassian-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "atlassian-agent[mcp]",
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
        "atlassian-agent[mcp]",
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
  knucklessg1/atlassian-agent:mcp
```

> The `:mcp` tag is the **slim MCP-server image** (built from
> `docker/Dockerfile --target mcp`, installing `atlassian-agent[mcp]`). The default
> `:latest` tag is the **full agent image** (`--target agent`, `atlassian-agent[agent]`)
> which also bundles the Pydantic AI agent and the epistemic-graph engine — use it
> when you run `atlassian-agent` (the agent), not just the MCP server. See
> [Container images](#container-images-mcp-vs-agent).

---

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`atlassian-agent` can also run as a **local container** (Docker / Podman / `uv`) or be
consumed from a **remote deployment**. The
[Deployment guide](https://knuckles-team.github.io/atlassian-agent/deployment/) has full, copy-paste
`mcp_config.json` for all four transports — **stdio**, **streamable-http**,
**local container / uv**, and **remote URL**:

- **Local container / uv** — launch the server from `mcp_config.json` via `uvx`,
  `docker run`, or `podman run`, or point at a local streamable-http container by `url`.
- **Remote URL** — connect to a server deployed behind Caddy at
  `http://atlassian-mcp.arpa/mcp` using the `"url"` key.
<!-- END GENERATED: additional-deployment-options -->

---

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` |  |
| `PORT` | `8000` |  |
| `TRANSPORT` | `stdio` | options: stdio, streamable-http, sse |
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | `pk-...` |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | `sk-...` |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `ATLASSIAN_AGENT_URL` | `http://localhost:8080` | (ATLASSIAN_{SUITE}_*) override is set. |
| `ATLASSIAN_AGENT_USER` | `your-email@example.com` |  |
| `ATLASSIAN_AGENT_TOKEN` | `your_token_here` |  |
| `ATLASSIAN_AGENT_VERIFY` | `True` |  |
| `ATLASSIAN_SSL_VERIFY` | `True` | takes precedence over ATLASSIAN_AGENT_VERIFY |
| `DEBUG` | `False` |  |
| `PYTHONUNBUFFERED` | `1` |  |
| `ENABLE_DELEGATION` | `True` | 1. OIDC delegation (RFC 8693) — flow the caller's IdP token to Atlassian |
| `OIDC_CONFIG_URL` | `https://idp.example.com/.well-known/openid-configuration` |  |
| `OIDC_CLIENT_ID` | `your_client_id` |  |
| `OIDC_CLIENT_SECRET` | `your_client_secret` |  |
| `AUDIENCE` | `https://your-instance.atlassian.net` |  |
| `DELEGATED_SCOPES` | `read:jira-work write:jira-work` |  |
| `ATLASSIAN_OAUTH_TOKEN` | `your_3lo_access_token` | 2. 3-Legged OAuth (3LO) bearer token |
| `ATLASSIAN_BEARER_TOKEN` | `your_personal_access_token` | 3. Bearer token / Personal Access Token (Server / Data Center) — global |
| `ATLASSIANTOOL` | `True` | MCP tools table (condensed action-routed surface). |
| `ATLASSIAN_ADMINTOOL` | `True` |  |
| `ATLASSIAN_API_ACCESSTOOL` | `True` |  |
| `ATLASSIAN_CONTROLTOOL` | `True` |  |
| `ATLASSIAN_DLPTOOL` | `True` |  |
| `ATLASSIAN_ORGTOOL` | `True` |  |
| `ATLASSIAN_USER_MGMTTOOL` | `True` |  |
| `ATLASSIAN_USER_PROVISIONINGTOOL` | `True` |  |
| `JIRA_PROJECTTOOL` | `True` |  |
| `JIRA_USERTOOL` | `True` |  |
| `JIRA_ISSUETOOL` | `True` |  |
| `JIRA_COMMENTTOOL` | `True` |  |
| `JIRA_FIELDTOOL` | `True` |  |
| `JIRA_SCREENTOOL` | `True` |  |
| `JIRA_WORKFLOWTOOL` | `True` |  |
| `JIRA_OTHERTOOL` | `True` |  |
| `CONFLUENCE_PAGETOOL` | `True` |  |
| `CONFLUENCE_SPACETOOL` | `True` |  |
| `CONFLUENCE_USERTOOL` | `True` |  |
| `CONFLUENCE_OTHERTOOL` | `True` |  |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `MCP_TOOL_MODE` | `condensed` | Tool surface: `condensed` | `verbose` | `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP auth (`oidc-client-credentials` for fleet calls) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_46 package + 10 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads. Suite-specific credential variables follow the pattern
`ATLASSIAN_{SUITE}_{URL|USER|TOKEN|VERIFY|BEARER_TOKEN}` and **fall back** to the shared
`ATLASSIAN_AGENT_*` values when unset — so you can run everything off one credential, or split
Jira vs Confluence (and Cloud vs Server/DC) by setting the prefixed variables.

### Connection & Credentials — shared fallback
| Variable | Description | Default |
|----------|-------------|---------|
| `ATLASSIAN_AGENT_URL` | Base Atlassian URL (shared fallback for all suites) | `http://localhost:8080` |
| `ATLASSIAN_AGENT_USER` | Account email / username (basic auth) | — |
| `ATLASSIAN_AGENT_TOKEN` | API token (basic auth) | — |
| `ATLASSIAN_AGENT_VERIFY` | TLS verification fallback | `True` |
| `ATLASSIAN_SSL_VERIFY` | TLS verification (takes precedence over `ATLASSIAN_AGENT_VERIFY`) | `True` |

### Connection & Credentials — Jira (per-suite overrides)
| Variable | Description |
|----------|-------------|
| `ATLASSIAN_JIRA_CLOUD_URL` / `_USER` / `_TOKEN` / `_VERIFY` | Jira **Cloud** connection + credentials |
| `ATLASSIAN_JIRA_CLOUD_BEARER_TOKEN` | Jira Cloud bearer token (OAuth/PAT) |
| `ATLASSIAN_JIRA_SERVER_URL` / `_USER` / `_TOKEN` / `_VERIFY` | Jira **Server / Data Center** connection + credentials |
| `ATLASSIAN_JIRA_SERVER_BEARER_TOKEN` | Jira Server/DC Personal Access Token (PAT) |

### Connection & Credentials — Confluence (per-suite overrides)
| Variable | Description |
|----------|-------------|
| `ATLASSIAN_CONFLUENCE_CLOUD_URL` / `_USER` / `_TOKEN` / `_VERIFY` | Confluence **Cloud** connection + credentials |
| `ATLASSIAN_CONFLUENCE_CLOUD_BEARER_TOKEN` | Confluence Cloud bearer token (OAuth/PAT) |
| `ATLASSIAN_CONFLUENCE_SERVER_URL` / `_USER` / `_TOKEN` / `_VERIFY` | Confluence **Server / Data Center** connection + credentials |
| `ATLASSIAN_CONFLUENCE_SERVER_BEARER_TOKEN` | Confluence Server/DC Personal Access Token (PAT) |

### Connection & Credentials — Admin suites (per-suite overrides)
Each admin suite accepts the same `_URL` / `_USER` / `_TOKEN` / `_VERIFY` / `_BEARER_TOKEN` set,
falling back to the shared `ATLASSIAN_AGENT_*` values:
`ATLASSIAN_ADMIN_CLOUD_*`, `ATLASSIAN_API_ACCESS_CLOUD_*`, `ATLASSIAN_CONTROL_CLOUD_*`,
`ATLASSIAN_DLP_CLOUD_*`, `ATLASSIAN_ORG_CLOUD_*`, `ATLASSIAN_USER_MGMT_CLOUD_*`,
`ATLASSIAN_USER_PROVISIONING_CLOUD_*`.

### Authentication mode
Resolved in priority order (first match wins). The bearer token is sent as
`Authorization: Bearer <token>`; basic auth uses email + API token.

| Variable | Auth mode | Notes |
|----------|-----------|-------|
| `ENABLE_DELEGATION` | **1. OIDC delegation** (RFC 8693 token exchange) | Set `true` to flow the caller's IdP token through to Atlassian |
| `OIDC_CONFIG_URL` / `OIDC_CLIENT_ID` / `OIDC_CLIENT_SECRET` | OIDC delegation IdP config | Required when delegation is enabled |
| `AUDIENCE` | OIDC delegation token audience | Defaults to the resolved URL |
| `DELEGATED_SCOPES` | OIDC delegation scopes | `read:jira-work write:jira-work` |
| `ATLASSIAN_OAUTH_TOKEN` | **2. 3-Legged OAuth (3LO)** bearer token | From the 3LO consent flow |
| `ATLASSIAN_BEARER_TOKEN` | **3. Bearer token / PAT** (global) | Server/DC Personal Access Token; per-suite `ATLASSIAN_{SUITE}_BEARER_TOKEN` overrides this |
| `ATLASSIAN_AGENT_TOKEN` (+ `_USER`) | **4. Basic auth** (fallback) | Email + API token |

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse` | `stdio` |
| `HOST` | Bind host (HTTP transports) | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports) | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both` | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list | — |
| `DEBUG` | Verbose logging | `False` |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers) | `1` |

### Tool toggles
Each action-routed tool can be disabled individually via its toggle env var (set to `false`).
The full list is in the [Available MCP Tools](#available-mcp-tools) table above
(e.g. `JIRA_ISSUETOOL`, `CONFLUENCE_PAGETOOL`, `ATLASSIAN_ADMINTOOL`).

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`) | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote` | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL | — |

### Agent CLI (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URL` | URL of the MCP server the agent connects to | `http://localhost:8000/mcp` |
| `PROVIDER` | LLM provider (e.g. `openai`) | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`) | `gpt-4o` |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface | `True` |

See [`.env.example`](.env.example) for a copy-paste starting point.

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
    image: knucklessg1/atlassian-agent:mcp
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

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `atlassian-agent[mcp]` | Slim MCP server only (`agent-utilities[mcp]` — FastMCP/FastAPI) | You only run the **MCP server** (smallest install / image) |
| `atlassian-agent[agent]` | Full agent runtime (`agent-utilities[agent,logfire]` — Pydantic AI + the epistemic-graph engine) | You run the **integrated agent** |
| `atlassian-agent[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# MCP server only (recommended for tool hosting — slim deps)
uv pip install "atlassian-agent[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine)
uv pip install "atlassian-agent[agent]"

# Everything (development)
uv pip install "atlassian-agent[all]"      # or: python -m pip install "atlassian-agent[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `knucklessg1/atlassian-agent:mcp` | `--target mcp` | `atlassian-agent[mcp]` — **slim**, no engine/`pydantic-ai`/`dspy`/`llama-index`/`tree-sitter` | `atlassian-mcp` |
| `knucklessg1/atlassian-agent:latest` | `--target agent` (default) | `atlassian-agent[agent]` — **full** agent runtime + epistemic-graph engine | `atlassian-agent` |

```bash
docker build --target mcp   -t knucklessg1/atlassian-agent:mcp    docker/   # slim MCP server
docker build --target agent -t knucklessg1/atlassian-agent:latest docker/   # full agent
```

`docker/mcp.compose.yml` runs the slim `:mcp` server; `docker/agent.compose.yml` runs the
agent (`:latest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

The **full agent** (`[agent]` / `:latest`) embeds the **epistemic-graph** engine (pulled in
transitively via `agent-utilities[agent]`). For production — or to share one knowledge graph
across multiple agents — run **epistemic-graph as its own database container** and point the
agent at it instead of embedding it. Deployment recipes (single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The slim `[mcp]` server does **not** require the database.

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/atlassian-agent/) and is
the recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/atlassian-agent/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/atlassian-agent/deployment/) | run the MCP server, the agent server, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/atlassian-agent/usage/) | the MCP tools, the Atlassian Python clients, the CLI |
| [Overview](https://knuckles-team.github.io/atlassian-agent/overview/) | architecture, enterprise readiness, MCP configuration |
| [Concepts](https://knuckles-team.github.io/atlassian-agent/concepts/) | concept registry (`CONCEPT:ATL-*`) |

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


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `atlassian-agent` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx atlassian-mcp` · or `uv tool install atlassian-agent` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/atlassian-agent:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
