# Usage — MCP / Python API / CLI

`atlassian-agent` exposes the same Atlassian capability three ways: as **MCP tools** an
agent calls, as **Python clients** you import, and as a **CLI** that runs the MCP
server or the A2A agent. The tool domains and concept registry are in
[Overview](overview.md) and [Concepts](concepts.md).

## As an MCP server

Once [deployed](deployment.md), the server registers Atlassian tool groups, each
gated by a `*_TOOL` environment toggle. The groups span Jira, Confluence, and Cloud
organization administration:

| Domain | Tool groups |
|---|---|
| Jira | projects, issues, comments, fields, screens, workflows, users |
| Confluence | pages, spaces, users |
| Cloud administration | organization, admin, API access, DLP, user management, user provisioning, control |

Example agent prompts that map onto these tools:

- *"List the open issues in project `PROJ`"* → Jira issue tools
- *"Create a Confluence page titled 'Release Notes' in the `ENG` space"* → Confluence page tools
- *"Show the members of the Atlassian organization"* → organization / user management tools

## As a Python API

The clients wrap the Atlassian REST surface through a shared `BaseAtlassianClient`,
which carries the base URL, credentials, and TLS verification. Each call returns a
structured `Response` rather than raising, so the surface is safe to use without a
reachable instance.

```python
from atlassian_agent.api.base import BaseAtlassianClient
from atlassian_agent.api.api_client_jira_cloud import JiraCloudAPI
from atlassian_agent.api.api_client_confluence_cloud import ConfluenceCloudAPI

base = BaseAtlassianClient(
    base_url="https://your-company.atlassian.net",
    username="your-email@example.com",
    token="your_api_token",
    verify=True,
)

jira = JiraCloudAPI(base)
confluence = ConfluenceCloudAPI(base)

# Reads
projects = jira.jira_cloud_get_projects_with_field_schemes()   # structured Response
spaces = confluence.confluence_cloud_get_spaces()
pages = confluence.confluence_cloud_get_pages()

print(spaces.status_code, spaces.data)
```

Build a client straight from the environment — `get_suite_client()` reads the
`ATLASSIAN_*` variables (and supports OIDC delegation / 3LO OAuth before falling back
to basic auth):

```python
from atlassian_agent.auth import get_suite_client
base = get_suite_client()        # reads ATLASSIAN_* from the environment / .env
```

## As a CLI

`atlassian-agent` installs two console scripts.

Run the **MCP server**:

```bash
export ATLASSIAN_AGENT_URL=https://your-company.atlassian.net
export ATLASSIAN_AGENT_USER=your-email@example.com
export ATLASSIAN_AGENT_TOKEN=your_api_token

atlassian-mcp                                                   # stdio (default)
atlassian-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

Run the **A2A agent server** against a running MCP server:

```bash
export MCP_URL=http://localhost:8000/mcp
atlassian-agent --provider openai --model-id gpt-4o --api-key sk-...
```

Both scripts accept `--help` for the full flag set.
