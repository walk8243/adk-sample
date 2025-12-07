from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Calculator", port=8001, stateless_http=True, json_response=True)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Run with streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
