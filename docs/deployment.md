# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`atlassian-agent` exposes its MCP server (console script `atlassian-mcp`) four ways. Pick the row that
matches where the server runs relative to your MCP client, then copy the matching
`mcp_config.json` below. Replace the `<your-…>` placeholders with the values from the **Configuration / Environment Variables** section.

| # | Option | Transport | Where it runs | `mcp_config.json` key |
|---|--------|-----------|---------------|------------------------|
| 1 | stdio | `stdio` | client launches a subprocess | `command` |
| 2 | Streamable-HTTP (local) | `streamable-http` | a local network port | `command` or `url` |
| 3 | Local container / uv | `stdio` or `streamable-http` | Docker / Podman / uv on this host | `command` or `url` |
| 4 | Remote URL | `streamable-http` | a remote host behind Caddy | `url` |

### 1. stdio (local subprocess)

The client launches the server over stdio via `uvx` — best for local IDEs
(Cursor, Claude Desktop, VS Code):

```json
{
  "mcpServers": {
    "atlassian-mcp": {
      "command": "uvx",
      "args": ["--from", "atlassian-agent", "atlassian-mcp"],
      "env": {
        "ATLASSIAN_AGENT_URL": "<your-atlassian_agent_url>",
        "ATLASSIAN_AGENT_TOKEN": "<your-atlassian_agent_token>",
        "ATLASSIAN_AGENT_USER": "<your-atlassian_agent_user>"
      }
    }
  }
}
```

### 2. Streamable-HTTP (local process)

Run the server as a long-lived HTTP process:

```bash
uvx --from atlassian-agent atlassian-mcp --transport streamable-http --host 0.0.0.0 --port 8000
curl -s http://localhost:8000/health        # {"status":"OK"}
```

Then either let the client launch it:

```json
{
  "mcpServers": {
    "atlassian-mcp": {
      "command": "uvx",
      "args": ["--from", "atlassian-agent", "atlassian-mcp", "--transport", "streamable-http", "--port", "8000"],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "ATLASSIAN_AGENT_URL": "<your-atlassian_agent_url>",
        "ATLASSIAN_AGENT_TOKEN": "<your-atlassian_agent_token>",
        "ATLASSIAN_AGENT_USER": "<your-atlassian_agent_user>"
      }
    }
  }
}
```

…or connect to the already-running process by URL:

```json
{
  "mcpServers": {
    "atlassian-mcp": { "url": "http://localhost:8000/mcp" }
  }
}
```

### 3. Local container / uv

**(a) Launch a container directly from `mcp_config.json`** (stdio over the container —
no ports to manage). Swap `docker` for `podman` for a daemonless runtime:

```json
{
  "mcpServers": {
    "atlassian-mcp": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "TRANSPORT=stdio",
        "-e", "ATLASSIAN_AGENT_URL=<your-atlassian_agent_url>",
        "-e", "ATLASSIAN_AGENT_TOKEN=<your-atlassian_agent_token>",
        "-e", "ATLASSIAN_AGENT_USER=<your-atlassian_agent_user>",
        "knucklessg1/atlassian-agent:latest"
      ]
    }
  }
}
```

**(b) Run a local streamable-http container, then connect by URL:**

```bash
docker run -d --name atlassian-mcp -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e ATLASSIAN_AGENT_URL="<your-atlassian_agent_url>" \
  -e ATLASSIAN_AGENT_TOKEN="<your-atlassian_agent_token>" \
  -e ATLASSIAN_AGENT_USER="<your-atlassian_agent_user>" \
  knucklessg1/atlassian-agent:latest
# or, from a clone of this repo:
docker compose -f docker/mcp.compose.yml up -d
```

```json
{
  "mcpServers": {
    "atlassian-mcp": { "url": "http://localhost:8000/mcp" }
  }
}
```

**(c) From a local checkout with `uv`:**

```bash
uv run atlassian-mcp --transport streamable-http --port 8000
```

### 4. Remote URL (deployed behind Caddy)

When the server is deployed remotely (e.g. as a Docker service) and published through
Caddy on the internal `*.arpa` zone, connect with the `"url"` key — no local process or
image required:

```json
{
  "mcpServers": {
    "atlassian-mcp": { "url": "http://atlassian-mcp.arpa/mcp" }
  }
}
```

Caddy reverse-proxies `http://atlassian-mcp.arpa` to the container's `:8000`
streamable-http listener; `http://atlassian-mcp.arpa/health` returns
`{"status":"OK"}` when the service is live.
<!-- END GENERATED: deployment-options -->

This page covers running `atlassian-agent` as a long-lived service: the transports, a
Docker Compose stack, the A2A agent server, putting it behind a Caddy reverse proxy,
and giving it a DNS name with Technitium.

> `atlassian-agent` ships **two** console scripts: an **MCP server** (`atlassian-mcp`)
> exposing a typed, deterministic Atlassian tool surface, and an **A2A agent server**
> (`atlassian-agent`) that drives those tools conversationally. Deploy the MCP server
> on its own, or deploy both together as a combined stack.

## Run the MCP server

The transport is selected with `--transport` (or the `TRANSPORT` env var):

=== "stdio (default)"

    ```bash
    atlassian-mcp
    ```
    For IDE / desktop MCP clients that launch the server as a subprocess.

=== "streamable-http"

    ```bash
    atlassian-mcp --transport streamable-http --host 0.0.0.0 --port 8000
    ```
    A network server with a `/health` endpoint and `/mcp` route.

=== "sse"

    ```bash
    atlassian-mcp --transport sse --host 0.0.0.0 --port 8000
    ```

Health check (HTTP transports):

```bash
curl -s http://localhost:8000/health        # {"status":"OK"}
```

## Configuration (environment)

`atlassian-agent` is configured entirely from the environment. The **required** set
for the shared (Cloud) connection:

| Var | Default | Meaning |
|---|---|---|
| `ATLASSIAN_AGENT_URL` | `http://localhost:8080` | Atlassian base URL (e.g. `https://your-company.atlassian.net`) |
| `ATLASSIAN_AGENT_USER` | — | Account email / username |
| `ATLASSIAN_AGENT_TOKEN` | — | API token (Cloud) or password / token (Server) |
| `ATLASSIAN_AGENT_VERIFY` | `True` | Verify TLS |
| `HOST` | `0.0.0.0` | Bind address (HTTP transports) |
| `PORT` | `8000` | Listen port (HTTP transports) |
| `TRANSPORT` | `stdio` | `stdio`, `streamable-http`, or `sse` |

Jira and Confluence **Server / Data Center** instances may be configured separately
with their own credentials (`ATLASSIAN_JIRA_SERVER_URL` / `_USER` / `_TOKEN` /
`_VERIFY`, and `ATLASSIAN_CONFLUENCE_SERVER_URL` / `_USER` / `_TOKEN` / `_VERIFY`).
Each tool group additionally has a `*_TOOL` toggle (for example `JIRA_ISSUE_TOOL`,
`CONFLUENCE_PAGE_TOOL`, `ATLASSIAN_ADMIN_TOOL`) to register only the surface you need.
The full set, grouped by product, is documented in
[`.env.example`](https://github.com/Knuckles-Team/atlassian-agent/blob/main/.env.example).
Copy it to `.env` and populate only what you use; tools whose credentials are absent
remain inactive.

### Backing Service

Atlassian Jira and Confluence are managed as **Atlassian Cloud** (a SaaS platform) or
as self-operated **Server / Data Center** products. `atlassian-agent` is a connector,
not a host for those systems, so there is no local backing-platform recipe — only
connection configuration is required. Provision an API token from your Atlassian
account and point `ATLASSIAN_AGENT_URL`, `ATLASSIAN_AGENT_USER`, and
`ATLASSIAN_AGENT_TOKEN` at the instance you intend to manage.

## Docker Compose

The repository ships [`docker/mcp.compose.yml`](https://github.com/Knuckles-Team/atlassian-agent/blob/main/docker/mcp.compose.yml).
It reads a sibling `.env` and publishes the HTTP server on `:8000`:

```yaml
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
```

```bash
cp .env.example .env          # then edit ATLASSIAN_AGENT_* values
docker compose -f docker/mcp.compose.yml up -d
docker compose -f docker/mcp.compose.yml logs -f
```

## Run the A2A agent server

The `atlassian-agent` console script starts a Pydantic-AI agent that consumes the MCP
tool surface and exposes an A2A endpoint (and an optional web UI). Point it at a
running MCP server with `MCP_URL` and select a model provider:

```bash
export MCP_URL=http://localhost:8000/mcp
atlassian-agent --provider openai --model-id gpt-4o --api-key sk-...
```

The repository ships [`docker/agent.compose.yml`](https://github.com/Knuckles-Team/atlassian-agent/blob/main/docker/agent.compose.yml),
which deploys the MCP server and the agent together. The agent publishes on `:9004`
and reaches the MCP server by container name:

```yaml
services:
  atlassian-agent-mcp:
    image: knucklessg1/atlassian-agent:latest
    hostname: atlassian-agent-mcp
    env_file: [../.env]
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports: ["8000:8000"]

  atlassian-agent-agent:
    image: knucklessg1/atlassian-agent:latest
    command: ["atlassian-agent"]
    depends_on: [atlassian-agent-mcp]
    env_file: [../.env]
    environment:
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://atlassian-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
    ports: ["9004:9004"]
```

```bash
docker compose -f docker/agent.compose.yml up -d
```

## Behind a Caddy reverse proxy

Expose the HTTP server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .arpa zone
atlassian-agent.arpa {
    tls internal
    reverse_proxy atlassian-agent-mcp:8000
}
```

```caddy
# Public — automatic Let's Encrypt
atlassian-agent.example.com {
    reverse_proxy atlassian-agent-mcp:8000
}
```

Reload Caddy:

```bash
docker compose -f services/caddy/compose.yml exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## DNS with Technitium

Point the hostname at the host running Caddy. Via the Technitium API:

```bash
curl -s "http://technitium.arpa:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=atlassian-agent.arpa" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=10.0.0.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `atlassian-agent.arpa → <caddy-host-ip>` in the Technitium web
console (`http://technitium.arpa:5380`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

Add to your client's `mcp_config.json`:

```json
{
  "mcpServers": {
    "atlassian-agent": {
      "command": "uv",
      "args": ["run", "atlassian-mcp"],
      "env": {
        "ATLASSIAN_AGENT_URL": "https://your-company.atlassian.net",
        "ATLASSIAN_AGENT_USER": "your-email@example.com",
        "ATLASSIAN_AGENT_TOKEN": "your_api_token"
      }
    }
  }
}
```

For a remote HTTP server, point the client at `http://atlassian-agent.arpa/mcp`
instead.
