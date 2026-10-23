# CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Architecture

`pyproject.toml` declares `atlassian-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `atlassian_agent` from it.
