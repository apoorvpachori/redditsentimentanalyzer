from pydantic import BaseModel, Field


class RedditComment(BaseModel):
    id: str
    text: str
    subreddit: str
    url: str
    score: float | None = None


class SearchResults(BaseModel):
    status: str
    query: str
    comments: list[RedditComment] = Field(default_factory=list)
    message: str = ""

