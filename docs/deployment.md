# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`atlassian-agent` supports local stdio, a loopback-only development listener, a
least-privilege stdio container, and a remote authenticated HTTPS boundary.
Provider endpoint, credential, selector, identity, and trust material are supplied
at runtime through `AgentConfig`; none is stored in this repository.

### Installed stdio process

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "atlassian-mcp",
      "args": [],
      "env": {"MCP_TOOL_MODE": "intent"}
    }
  }
}
```

### Loopback development listener

```bash
atlassian-mcp --transport streamable-http --host 127.0.0.1 --port 8000
```

Do not expose this listener beyond loopback. Network deployments require direct TLS
or an explicitly trusted TLS-terminating ingress, configured authentication, exact
`MCP_ALLOWED_HOSTS`, and an exact trusted-proxy CIDR policy.

### Least-privilege local container

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  registry.example.invalid/atlassian-agent@sha256:<digest> atlassian-mcp
```

The operator projects the selected AgentConfig profile into the process at runtime;
the image remains immutable and contains no environment connection profile.

### Remote authenticated HTTPS endpoint

```json
{
  "mcpServers": {
    "atlassian": {"url": "https://service.example.invalid/mcp"}
  }
}
```

Store the real remote URL, outbound identity reference, and TLS-profile reference in
`AgentConfig`, not in MCP client JSON or documentation.
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
| `ATLASSIAN_TLS_PROFILE` | _(unset)_ | Optional runtime TLS profile selector; verification is mandatory |
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
    image: example/atlassian-agent@sha256:<digest>
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
    image: example/atlassian-agent@sha256:<digest>
    hostname: atlassian-agent-mcp
    env_file: [../.env]
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports: ["8000:8000"]

  atlassian-agent-agent:
    image: example/atlassian-agent@sha256:<digest>
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
# Internal (self-signed) — homelab .example.invalid zone
atlassian-agent.example.invalid {
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
curl -s "http://technitium.example.invalid:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=atlassian-agent.example.invalid" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=192.0.2.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `atlassian-agent.example.invalid → <caddy-host-ip>` in the Technitium web
console (`http://technitium.example.invalid:5380`). The ecosystem
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

For a remote HTTP server, point the client at `http://atlassian-agent.example.invalid/mcp`
instead.
