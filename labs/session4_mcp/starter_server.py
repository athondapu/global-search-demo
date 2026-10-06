"""Session 4 starter: an MCP server over the training handbook."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("handbook", host="127.0.0.1", port=8000)

HANDBOOK = {
    "schedule": "Six weekly sessions; capstone demo day closes the program.",
    "seats": "Reserve a lab seat with `lab seat` before sessions 3 and 4.",
}


@mcp.tool()
def lookup(topic: str) -> str:
    """Look up a handbook topic, e.g. 'schedule' or 'seats'."""
    return HANDBOOK.get(topic, f"No handbook entry for {topic!r}")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
