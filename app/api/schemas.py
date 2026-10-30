from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000, pattern=r"\S")


class AnalyzeResponse(BaseModel):
    answer: str
    elapsed_seconds: float

