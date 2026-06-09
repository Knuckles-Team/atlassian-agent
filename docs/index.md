# atlassian-agent

Comprehensive **MCP server + A2A agent** for Jira and Confluence management across
Atlassian Cloud and Server.

!!! info "Official documentation"
    This site is the canonical reference for `atlassian-agent`, maintained alongside
    every release.

[![PyPI](https://img.shields.io/pypi/v/atlassian-agent)](https://pypi.org/project/atlassian-agent/)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
[![License](https://img.shields.io/pypi/l/atlassian-agent)](https://github.com/Knuckles-Team/atlassian-agent/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/source-GitHub-181717?logo=github)](https://github.com/Knuckles-Team/atlassian-agent)

## Overview

`atlassian-agent` wraps the Atlassian REST surface — Jira and Confluence, for both
Cloud and Server / Data Center — with typed, deterministic MCP tools, and ships a
Pydantic-AI A2A agent that drives those tools conversationally. It provides:

- **A broad Atlassian tool surface** — Jira projects, issues, comments, fields,
  screens, workflows, and users, alongside Confluence pages, spaces, and users, plus
  Cloud organization administration (org, admin, API access, DLP, user management,
  user provisioning, control).
- **Two console scripts** — `atlassian-mcp` (the MCP server) and `atlassian-agent`
  (the A2A agent server with an optional web UI).
- **Tolerant REST clients** — every call returns a structured `Response` rather than
  raising, so the surface remains usable without a reachable instance and **remains
  inactive when credentials are absent**.

## Explore the documentation

<div class="grid cards" markdown>

- :material-rocket-launch: **[Installation](installation.md)** — pip, source, extras, and the prebuilt Docker image.
- :material-server-network: **[Deployment](deployment.md)** — run the MCP server, the agent server, Docker Compose, Caddy + Technitium.
- :material-console: **[Usage](usage.md)** — the MCP tools, the Atlassian Python clients, and the CLI.
- :material-sitemap: **[Architecture](overview.md)** — the layered tool / API / agent design.
- :material-tag-multiple: **[Concepts](concepts.md)** — the `CONCEPT:ATL-*` registry.

</div>

## Quick start

```bash
pip install "atlassian-agent[mcp]"
atlassian-mcp                       # stdio MCP server (default transport)
```

Connect it to an Atlassian instance:

```bash
export ATLASSIAN_AGENT_URL=https://your-company.atlassian.net
export ATLASSIAN_AGENT_USER=your-email@example.com
export ATLASSIAN_AGENT_TOKEN=your_api_token
atlassian-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

See **[Installation](installation.md)** and **[Deployment](deployment.md)** for the
full matrix (PyPI extras, Docker image, all transports, the agent server, reverse
proxy, DNS).
