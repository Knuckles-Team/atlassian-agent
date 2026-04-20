import os
from atlassian_agent.mcp_server import get_mcp_instance

# Mock environment
os.environ["ATLASSIAN_AGENT_URL"] = "https://dummy.atlassian.net"
os.environ["ATLASSIAN_AGENT_TOKEN"] = "dummy"
os.environ["ATLASSIAN_AGENT_USER"] = "dummy"
os.environ["ATLASSIAN_AGENT_IS_CLOUD"] = "True"

mcp, args, middlewares, registered_suites = get_mcp_instance()
print(f"Total tools registered: {len(mcp._tools)}")
for i, tool in enumerate(list(mcp._tools.values())[:10]):
    print(f"{i + 1}. {tool.name}")
