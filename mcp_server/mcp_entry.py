from app import app  # FastMCP object in app.py

if __name__ == "__main__":
    # Compatible with Claude Desktop: MCP server running via stdio
    app.run(transport="stdio")
