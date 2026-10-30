from langchain.tools import tool

from app.tools.schemas import SearchResults


@tool
def search_reddit(query: str, limit: int = 10) -> dict:
    """Search Reddit product comments using BM25. Use focused product queries; limit 1–50."""
    # TODO: Replace this body with your teammate's BM25/PySerini search.
    # Return SearchResults(status="ok", query=query, comments=[...]).model_dump().
    return SearchResults(
        status="not_implemented",
        query=query,
        message="BM25 retrieval is not connected. No Reddit evidence is available.",
    ).model_dump()

