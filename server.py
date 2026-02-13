# server.py
from mcp.server.fastmcp import FastMCP
import requests

# أبسط إصدار ممكن
mcp = FastMCP("test1")

@mcp.tool()
def test_port_15000() -> str:
    """Test if localhost:15000 is reachable"""
    try:
        response = requests.get("http://127.0.0.1:15000", timeout=3)
        return f"✅ Service is running! Status: {response.status_code}"
    except:
        return "❌ Service NOT found on port 15000"

@mcp.tool()
def fetch_url(url: str) -> str:
    """Fetch any URL"""
    try:
        response = requests.get(url, timeout=5)
        return f"Status: {response.status_code}\nPreview: {response.text[:200]}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Simple MCP Server starting...")
    mcp.run()
