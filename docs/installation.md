# Installation

`atlassian-agent` is a standard Python package and a prebuilt container image. Pick
the path that matches how you want to run it.

## Requirements

- **Python 3.11 – 3.14**.
- A reachable **Atlassian instance** — Jira and/or Confluence on Atlassian Cloud, or a
  self-managed Jira / Confluence Server (Data Center) deployment. See the
  [Backing Service](deployment.md#backing-service) note for connection guidance.

## From PyPI (recommended)

```bash
pip install atlassian-agent
```

### Optional extras

The base install is intentionally minimal. Install the extra for what you need:

| Extra | Install | Pulls in |
|---|---|---|
| `mcp` | `pip install "atlassian-agent[mcp]"` | FastMCP MCP-server runtime (`agent-utilities[mcp]`) |
| `agent` | `pip install "atlassian-agent[agent]"` | Pydantic-AI agent + Logfire tracing (`agent-utilities[agent,logfire]`) |
| `all` | `pip install "atlassian-agent[all]"` | MCP server **and** the A2A agent (everything above) |
| `test` | `pip install "atlassian-agent[test]"` | `pytest`, `pytest-asyncio`, `pytest-cov`, `pytest-xdist` |

```bash
# Typical: run the MCP server and the A2A agent
pip install "atlassian-agent[all]"
```

The base dependency set always includes `atlassian-python-api`, which backs the Jira
and Confluence clients.

## From source

```bash
git clone https://github.com/Knuckles-Team/atlassian-agent.git
cd atlassian-agent
pip install -e ".[all]"          # editable install with every extra
```

With [`uv`](https://docs.astral.sh/uv/):

```bash
uv pip install -e ".[all]"
uv run atlassian-mcp
```

## Prebuilt Docker image

A multi-stage, slim image is published on every release (entrypoint `atlassian-mcp`):

```bash
docker pull knucklessg1/atlassian-agent:latest

docker run --rm -i \
  -e ATLASSIAN_AGENT_URL=https://your-company.atlassian.net \
  -e ATLASSIAN_AGENT_USER=your-email@example.com \
  -e ATLASSIAN_AGENT_TOKEN=your_api_token \
  knucklessg1/atlassian-agent:latest        # stdio transport (default)
```

For an HTTP server with a published port and the agent server, see
[Deployment](deployment.md).

## Verify the install

```bash
atlassian-mcp --help
atlassian-agent --help
python -c "import atlassian_agent; print(atlassian_agent.__version__)"
```

## Next steps

- **[Deployment](deployment.md)** — run it as a long-lived MCP server and agent behind Caddy + DNS.
- **[Usage](usage.md)** — call the tools, the Python clients, and the CLI.
- **[Configuration](deployment.md#configuration-environment)** — every environment variable.
