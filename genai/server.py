from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Awesome Server")

@mcp.tool("Adds two numbers")
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b


@mcp.tool("Say my name")
def greet(name: str) -> str:
    """Greets a person by their name."""
    return f"Hello, {name}!"