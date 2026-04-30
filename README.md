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

*Version: 0.1.8*

## Overview

**Atlassian Agent MCP Server + A2A Agent**

Comprehensive AI agent for Jira and Confluence management.

This repository is actively maintained - Contributions are welcome!

## MCP

### Using as an MCP Server

The MCP Server can be run in two modes: `stdio` (for local testing) or `http` (for networked access).

#### Environment Variables

*   `ATLASSIAN_AGENT_URL`: The URL of the target service.
*   `ATLASSIAN_AGENT_TOKEN`: The API token or access token.

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
        "ATLASSIAN_AGENT_TOKEN": "your_token"
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
