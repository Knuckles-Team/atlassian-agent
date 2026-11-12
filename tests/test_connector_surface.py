"""CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R001: the served tools, prompts and skills match the declared surface."""

from __future__ import annotations

import pytest
from scion_sdk.testing.surface_check import surface_check

pytestmark = pytest.mark.spec("CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R001")

PACKAGE = "atlassian_agent"


def test_declared_surface_has_no_gaps() -> None:
    """Contracts, links, locations, roles, prompts and skills cover every served tool."""
    assert surface_check(PACKAGE) == []


def test_every_contract_step_names_a_served_tool() -> None:
    from atlassian_agent.connector_contracts import CONTRACTS

    steps = [step.tool for contract in CONTRACTS for step in contract.steps]
    assert len(steps) == len(set(steps))
    assert all(step for step in steps)
