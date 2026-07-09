"""Regression tests for the atlassian-my-priority-queue ranking helper.

Loads ``skills/atlassian-my-priority-queue/scripts/rank_items.py`` by path (it is a
standalone stdlib script, not an importable package module) and pins the combined
priority + staleness scoring, ordering, and STALE flags.
"""

import importlib.util
from datetime import datetime, timezone
from pathlib import Path

_SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "atlassian_agent"
    / "skills"
    / "atlassian-my-priority-queue"
    / "scripts"
    / "rank_items.py"
)

_spec = importlib.util.spec_from_file_location("jira_rank_items", _SCRIPT)
rank_items = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rank_items)

NOW = datetime(2026, 7, 9, tzinfo=timezone.utc)


def _issue(key, priority, updated):
    fields = {"summary": key, "updated": updated}
    fields["priority"] = {"name": priority} if priority else None
    return {"key": key, "fields": fields}


def test_ordering_and_scores():
    issues = [
        _issue("SKAN-3", "Highest", "2026-07-07T00:00:00.000+0000"),  # 2d fresh
        _issue("SKAN-1", "Medium", "2026-05-30T00:00:00.000+0000"),   # 40d stale
        _issue("SKAN-12", "Highest", "2026-06-25T00:00:00.000+0000"),  # 14d stale
        _issue("SKAN-9", "High", "2026-06-19T00:00:00.000+0000"),     # 20d stale
        _issue("SKAN-7", None, "2026-07-08T00:00:00.000+0000"),       # 1d, no priority
    ]
    ranked = rank_items.rank(issues, NOW)
    assert [r["key"] for r in ranked] == ["SKAN-12", "SKAN-3", "SKAN-9", "SKAN-1", "SKAN-7"]
    scores = {r["key"]: r["score"] for r in ranked}
    # priority_rank*100 + min(days,30) + (25 if days>7)
    assert scores["SKAN-12"] == 5 * 100 + 14 + 25   # 539
    assert scores["SKAN-3"] == 5 * 100 + 2           # 502
    assert scores["SKAN-9"] == 4 * 100 + 20 + 25     # 445
    assert scores["SKAN-1"] == 3 * 100 + 30 + 25     # 355 (staleness capped at 30)
    assert scores["SKAN-7"] == 3 * 100 + 1           # 301 (missing priority -> Medium)


def test_stale_flag_boundary():
    seven = rank_items.rank([_issue("A", "High", "2026-07-02T00:00:00.000+0000")], NOW)[0]
    eight = rank_items.rank([_issue("B", "High", "2026-07-01T00:00:00.000+0000")], NOW)[0]
    assert seven["days_stale"] == 7 and seven["stale"] is False
    assert eight["days_stale"] == 8 and eight["stale"] is True


def test_parse_dt_handles_offsets_and_z():
    a = rank_items.parse_dt("2026-07-01T00:00:00.000+0000")
    b = rank_items.parse_dt("2026-07-01T00:00:00Z")
    assert a == b == datetime(2026, 7, 1, tzinfo=timezone.utc)


def test_extract_from_envelope_and_list():
    env = {"issues": [_issue("A", "Low", "2026-07-08T00:00:00.000+0000")]}
    assert len(rank_items.extract_issues(env)) == 1
    assert len(rank_items.extract_issues([_issue("A", "Low", "2026-07-08T00:00:00.000+0000")])) == 1
