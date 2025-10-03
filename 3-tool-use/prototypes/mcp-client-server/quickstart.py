from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

if __name__ == "__main__":
    mcp.run()

# Note: