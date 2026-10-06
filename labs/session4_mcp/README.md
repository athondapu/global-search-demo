# Session 4: MCP connectors

Build a small MCP server that exposes the training handbook as tools, then connect an agent to
it.

## Setup

Install from the lockfile so you get the MCP SDK version this lab was written for:

```bash
cd labs/session4_mcp
uv sync
uv run python starter_server.py
```

Do **not** `pip install mcp` directly: a newer SDK release may not match the starter code.
