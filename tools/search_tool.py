from crewai.tools import tool
from duckduckgo_search import DDGS

@tool("Search Tool")
def search_tool(query: str) -> str:
    """Search real-time information from the internet"""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        return "\n".join([r["body"] for r in results])
    except Exception as e:
        return f"Search error: {str(e)}"