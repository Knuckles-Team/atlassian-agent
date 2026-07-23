#!/usr/bin/env python3
"""Rank Jira issues by a combined priority + staleness score.

Reads the JSON returned by the ``atlassian_jira_issue`` search action (either the
raw ``{"issues": [...]}`` envelope or a bare list of issue objects) from a file
argument or stdin, and prints a single list sorted highest-first by::

    score = priority_rank * 100 + min(days_stale, 30) + (25 if days_stale > 7 else 0)

Priority dominates; staleness breaks ties and boosts anything untouched for more
than 7 days (flagged ``STALE``). Stdlib only — no third-party dependencies.

Usage::

    atlassian_jira_issue search ... > results.json
    python rank_items.py results.json            # human table
    python rank_items.py --json results.json     # ranked JSON list
    cat results.json | python rank_items.py      # stdin
    python rank_items.py --now 2026-07-09T00:00:00Z results.json   # deterministic
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone

# Jira priority name -> rank. Higher rank floats to the top.
PRIORITY_RANK = {
    "highest": 5,
    "high": 4,
    "medium": 3,
    "low": 2,
    "lowest": 1,
}
DEFAULT_PRIORITY_RANK = 3  # unset/unknown priority -> treated as Medium
STALE_DAYS = 7
STALE_BONUS = 25
STALE_CAP = 30


def parse_dt(value: str) -> datetime:
    """Parse Jira timestamps into an aware UTC datetime.

    Handles ``2026-07-08T10:15:30.000+0000`` (offset without a colon),
    trailing ``Z``, and plain ISO-8601. Falls back to ``epoch`` if it cannot
    be parsed.
    """
    if not value:
        return datetime.fromtimestamp(0, tz=timezone.utc)
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    # Insert a colon into a "+0000" / "-0700" style offset for fromisoformat.
    if len(text) >= 5 and text[-5] in "+-" and text[-3] != ":":
        text = text[:-2] + ":" + text[-2:]
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z"):
            try:
                dt = datetime.strptime(value.strip(), fmt)
                break
            except ValueError:
                continue
        else:
            return datetime.fromtimestamp(0, tz=timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def extract_issues(payload) -> list:
    """Accept a list, or an envelope keyed by 'issues'/'results'."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("issues", "results", "work_items"):
            if isinstance(payload.get(key), list):
                return payload[key]
    return []


def rank(issues: list, now: datetime) -> list:
    ranked = []
    for issue in issues:
        fields = issue.get("fields", issue) or {}
        priority_obj = fields.get("priority") or {}
        priority = (
            priority_obj.get("name") if isinstance(priority_obj, dict) else priority_obj
        ) or ""
        rank_val = PRIORITY_RANK.get(priority.lower(), DEFAULT_PRIORITY_RANK)
        updated = fields.get("updated") or fields.get("updated_at") or ""
        days_stale = max(0, (now - parse_dt(updated)).days) if updated else 0
        score = rank_val * 100 + min(days_stale, STALE_CAP)
        if days_stale > STALE_DAYS:
            score += STALE_BONUS
        status = fields.get("status") or {}
        ranked.append(
            {
                "key": issue.get("key") or issue.get("id") or "?",
                "summary": fields.get("summary") or fields.get("name") or "",
                "priority": priority or "(none)",
                "status": status.get("name")
                if isinstance(status, dict)
                else (status or ""),
                "days_stale": days_stale,
                "stale": days_stale > STALE_DAYS,
                "score": score,
            }
        )
    ranked.sort(key=lambda r: (r["score"], r["days_stale"]), reverse=True)
    return ranked


def render_table(rows: list) -> str:
    if not rows:
        return "(no issues assigned)"
    header = f"{'KEY':<14} {'PRIORITY':<9} {'STALE':<7} {'SCORE':<6} SUMMARY"
    lines = [header, "-" * len(header)]
    for r in rows:
        flag = "⚠STALE" if r["stale"] else ""
        lines.append(
            f"{r['key']:<14} {r['priority']:<9} {str(r['days_stale']) + 'd':<7} "
            f"{r['score']:<6} {flag + ' ' if flag else ''}{r['summary'][:70]}"
        )
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="JSON file (default: stdin)")
    parser.add_argument("--json", action="store_true", help="emit ranked JSON list")
    parser.add_argument("--now", help="override 'now' as ISO-8601 (for tests)")
    args = parser.parse_args(argv)

    raw = open(args.path, encoding="utf-8").read() if args.path else sys.stdin.read()
    now = parse_dt(args.now) if args.now else datetime.now(timezone.utc)
    rows = rank(extract_issues(json.loads(raw)), now)

    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        print(render_table(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
