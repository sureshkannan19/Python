import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("terminal")

# FIXED: Workspace is always relative to server.py file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WORKSPACE = os.path.join(BASE_DIR, "workspace")

# Auto-create the workspace so Windows stops crying
os.makedirs(DEFAULT_WORKSPACE, exist_ok=True)

@mcp.tool(description ="List the files in current directory")
async def list_files() -> str:
    return ", ".join(os.listdir(DEFAULT_WORKSPACE))

@mcp.tool(description ="Execute commands")
async def run_server_command(command: str) -> str:
    try:
        result = subprocess.run(
            command,
            cwd=DEFAULT_WORKSPACE,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)

@mcp.tool(description ="List of movies that i like")
async def movies_i_like(command: str) -> str:
    print("movies that i like", str)
    return str(["Batman"])

if __name__ == "__main__":
    mcp.run(transport="stdio")
