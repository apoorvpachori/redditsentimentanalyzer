# Retrieval tools

`reddit_search.py` exposes `search_reddit(query, limit=10)` to the agent.
Its body is intentionally a placeholder returning `status="not_implemented"`,
an empty comments list, and an explanatory message.

`schemas.py` defines `SearchResults` and `RedditComment`. To connect BM25,
replace the placeholder body and return the same result shape with `status="ok"`.
Each comment must supply an ID, text, subreddit, and actual source URL;
retrieval score is optional. The integration should clamp limit to 1–50.
Dataset preprocessing and indexing belong to the retrieval component.
