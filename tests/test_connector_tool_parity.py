"""Canonical SDK server parity for the Atlassian connector."""

from __future__ import annotations

import asyncio
import importlib
from pathlib import Path

import pytest
from agent_connector_sdk.connector import build_server

pytestmark = pytest.mark.spec("CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R001")

PACKAGE = "atlassian_agent"
ROOT = Path(importlib.import_module(PACKAGE).__path__[0])


def _tool_snapshot(server):
    async def collect():
        from fastmcp import Client

        async with Client(server) as client:
            return {
                tool.name: tool.model_dump(mode="json")
                for tool in await client.list_tools()
            }

    return asyncio.run(collect())


def test_canonical_server_preserves_legacy_tools_and_schemas(monkeypatch):
    """The SDK declaration exposes the same tools and typed schemas as legacy MCP."""
    monkeypatch.setenv("MCP_FLEET_REGISTRATION", "false")
    monkeypatch.setattr(
        "sys.argv", ["connector", "--transport", "stdio", "--auth-type", "none"]
    )
    legacy_module = importlib.import_module("atlassian_agent.mcp_server")

    legacy_module._registered_tools.clear()
    legacy = legacy_module.get_mcp_instance()[0]
    legacy_tools = _tool_snapshot(legacy)
    legacy_module._registered_tools.clear()
    _, canonical = build_server(PACKAGE, command_args=[])
    canonical_tools = _tool_snapshot(canonical)

    assert set(canonical_tools) == set(legacy_tools)
    for name in canonical_tools:
        assert canonical_tools[name] == legacy_tools[name]
    assert {
        "confluence_get_pages",
        "atlassian_ingest_confluence",
        "atlassian_ingest_issues",
    } <= set(canonical_tools)


def test_canonical_server_serves_every_packaged_content_payload(monkeypatch):
    """The declared server publishes all packaged ontology, shapes, and prompts."""
    monkeypatch.setenv("MCP_FLEET_REGISTRATION", "false")
    _, server = build_server(PACKAGE, command_args=[])

    async def collect():
        from fastmcp import Client

        async with Client(server) as client:
            resources = {str(item.uri) for item in await client.list_resources()}
            prompts = {item.name for item in await client.list_prompts()}
            payloads = {}
            for uri in resources:
                if uri.startswith(("ontology://", "shapes://")):
                    payloads[uri] = (await client.read_resource(uri))[0].text
            return resources, prompts, payloads

    resources, prompts, payloads = asyncio.run(collect())
    expected_resources = set()
    for path in sorted((ROOT / "ontology").glob("*.ttl")):
        expected_resources.add(f"ontology://atlassian-mcp/{path.name}")
    for path in sorted((ROOT / "ontology" / "shapes").glob("*.ttl")):
        expected_resources.add(f"shapes://atlassian-mcp/{path.name}")
    assert expected_resources <= resources
    for uri, text in payloads.items():
        directory = ROOT / "ontology"
        if uri.startswith("shapes://"):
            directory /= "shapes"
        assert text.encode() == (directory / uri.rsplit("/", 1)[-1]).read_bytes()

    expected_prompts = {
        path.stem
        for path in (ROOT / "prompts").glob("*.json")
        if not path.name.startswith("_")
    }
    assert expected_prompts <= prompts


@pytest.fixture(autouse=True)
def _no_outbound_network(monkeypatch):
    import socket

    def refuse(*_args, **_kwargs):
        raise AssertionError(
            "connector construction must not contact an external system"
        )

    monkeypatch.setenv("MCP_FLEET_REGISTRATION", "false")
    monkeypatch.setattr(socket.socket, "connect", refuse)
