"""CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R002: competency reads declare access contracts."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from scion_sdk.access_contract import parse_access_contracts
from scion_sdk.connector import build_server
from scion_sdk.testing.surface_check import served_surface

PACKAGE = "atlassian_agent"
ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = ROOT / PACKAGE / "ontology"
EXPECTED = {
    "issue": {
        "class": "Issue",
        "key": "key",
        "operation": "jira_search_for_issues_using_jql",
        "columns": {"status", "assignee", "blockedBy", "pullRequestUrl"},
    },
}


def _local(iri: str) -> str:
    return re.split(r"[#/]", iri)[-1]


def _declared_terms() -> set[str]:
    text = (ONTOLOGY / "atlassian.ttl").read_text(encoding="utf-8")
    return set(re.findall(r"^:(\w+)\s+a\s+owl:", text, flags=re.M))


def _findings(contracts, tools: set[str], terms: set[str], recordings: Path) -> list[str]:
    found: list[str] = []
    by_entity = {c.entity: c for c in contracts}
    for entity, want in EXPECTED.items():
        contract = by_entity.get(entity)
        if contract is None:
            found.append(f"{entity}: no contract")
            continue
        if contract.operation not in tools:
            found.append(f"{entity}: tool {contract.operation} is not served")
        if _local(contract.class_iri) not in terms:
            found.append(f"{entity}: class {contract.class_iri} not in ontology")
        if contract.key_field != want["key"] or contract.access_kind != "mcp_tool":
            found.append(f"{entity}: wrong key or access kind")
        for prop, field in contract.predicates:
            if _local(prop) != field or field not in terms:
                found.append(f"{entity}: column {field} is not an ontology property")
        columns = {field for _, field in contract.predicates}
        if columns != want["columns"]:
            found.append(f"{entity}: columns {sorted(columns)}")
        path = recordings / f"{entity}.json"
        if not path.is_file():
            found.append(f"{entity}: recording missing")
            continue
        records = json.loads(path.read_text(encoding="utf-8"))
        if not records:
            found.append(f"{entity}: recording is empty")
        for record in records:
            for field in {contract.key_field} | columns:
                if field not in record:
                    found.append(f"{entity}: recording lacks {field}")
    return found


@pytest.mark.spec("CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R002")
def test_competency_contracts_certified() -> None:
    contracts = parse_access_contracts(
        (ONTOLOGY / "access_contracts.ttl").read_text(encoding="utf-8")
    )
    tools = served_surface(build_server(PACKAGE, command_args=[])[1]).tools
    assert (
        _findings(contracts, tools, _declared_terms(), ROOT / "tests" / "recordings")
        == []
    )


@pytest.mark.spec("CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R002")
def test_missing_tool_or_column_fails_certification(tmp_path: Path) -> None:
    contracts = parse_access_contracts(
        (ONTOLOGY / "access_contracts.ttl").read_text(encoding="utf-8")
    )
    (tmp_path / "issue.json").write_text('[{"key": "A-1", "status": "Done"}]')
    found = _findings(contracts, set(), _declared_terms(), tmp_path)
    assert any("is not served" in f for f in found)
    assert any("recording lacks assignee" in f for f in found)
