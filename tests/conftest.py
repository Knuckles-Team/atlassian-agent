import sys
from unittest.mock import MagicMock

import pytest

if __name__ == "__main__":
    # Allows `python tests/conftest.py` to bootstrap a fresh worktree BEFORE
    # `uv sync`, without importing anything from this repo's own package or
    # its third-party deps — none of which exist yet in a pre-sync venv.
    raise SystemExit(0)


@pytest.fixture(autouse=True)
def _clean_argv(monkeypatch):
    """Fleet-wide test-harness defect: reset sys.argv to a single clean
    element before every test.

    Several tests in this suite exercise this package's own argparse-based
    CLI entrypoint — directly via `get_mcp_instance()`/`agent_server()`, or
    indirectly via `runpy.run_module(..., run_name="__main__")` — and that
    argparse call reads the LIVE `sys.argv`. Left alone, pytest's own
    invocation flags (`-p no:randomly`, `-n auto`, `--randomly-seed=...`, ...)
    end up in that argv and are rejected by the module's CLI parser:

        error: argument -p/--port: invalid int value: 'no:randomly'

    which makes `pytest tests/ -q -p no:randomly` disagree with a plain
    `pytest tests/ -q` run -- not a real regression, just this trap. A
    handful of call sites already pin their own argv locally (e.g. via
    `patch("sys.argv", [...])` around a `runpy.run_module` call); those
    still work unchanged, since that local patch simply overrides this
    fixture's baseline for the duration of its own `with` block, and
    monkeypatch restores this baseline afterward. This fixture is the
    fleet-wide backstop for every OTHER call site (most of them direct
    `get_mcp_instance()` calls with no local patch at all) that the
    per-call-site fix in WD4-FIX-01 could not enumerate exhaustively. See
    plans/complex/waves/wD4/WD4-FIX-01.md defect (a).
    """
    monkeypatch.setattr(sys, "argv", ["pytest"])


# 1. Mock fastmcp.Context methods to avoid RuntimeError in test environments
import fastmcp


async def dummy_async(*args, **kwargs):
    return None


fastmcp.Context.info = dummy_async  # type: ignore[method-assign]
fastmcp.Context.warning = dummy_async  # type: ignore[method-assign]
fastmcp.Context.error = dummy_async  # type: ignore[method-assign]
fastmcp.Context.debug = dummy_async  # type: ignore[method-assign]


# 2. Create a generic mock client that returns dummy data for any method call
class MockClient:
    def __getattr__(self, name):
        return lambda *args, **kwargs: {
            "id": "1",
            "key": "TEST",
            "values": [{"id": "1"}],
            "body": "test-body",
            "results": [{"id": "1"}],
        }


# 3. Patch all atlassian_agent.auth getters before other modules import them
import atlassian_agent.auth

for name in list(dir(atlassian_agent.auth)):
    if name.startswith("get_") and name.endswith("_client"):
        setattr(atlassian_agent.auth, name, MagicMock(return_value=MockClient()))
