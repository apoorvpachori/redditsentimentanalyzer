from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_api_key: SecretStr
    llm_base_url: str = "https://api.openai.com/v1"
    llm_model: str
    request_timeout_seconds: float = Field(default=60, gt=0)
    agent_recursion_limit: int = Field(default=12, ge=2, le=100)


@lru_cache
def get_settings() -> Settings:
    return Settings()
