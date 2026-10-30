from app.tools.reddit_search import search_reddit


def test_placeholder_has_no_evidence():
    result = search_reddit.invoke({"query": "headphones"})
    assert result["status"] == "not_implemented"
    assert result["comments"] == []

