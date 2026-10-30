from functools import lru_cache

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from app.core.config import get_settings
from app.tools.reddit_search import search_reddit

from app.agent.prompts import SYSTEM_PROMPT


@lru_cache
def get_agent():
    settings = get_settings()
    model = ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.llm_api_key.get_secret_value(),
        base_url=settings.llm_base_url,
        temperature=0,
        timeout=settings.request_timeout_seconds,
        max_retries=1,
    )
    return create_agent(model=model, tools=[search_reddit], system_prompt=SYSTEM_PROMPT)
