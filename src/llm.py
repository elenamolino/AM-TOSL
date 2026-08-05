import logging
import os
from langchain_core.language_models import BaseChatModel

logger = logging.getLogger(__name__)


def build_model(
    model_name: str,
    *,
    temperature: float = 0,
    base_url: str | None = None,
    api_key: str | None = None,
) -> BaseChatModel:
    from langchain_openai import ChatOpenAI

    resolved_key = api_key or os.getenv("OPENAI_API_KEY")

    if not resolved_key:
        if base_url:
            # Most local servers don't validate the key
            resolved_key = "not-required"
        else:
            raise ValueError("OPENAI_API_KEY is not set. Add it to .env or pass --api-key.")

    kwargs: dict = {"model": model_name, "temperature": temperature, "api_key": resolved_key}
    if base_url:
        kwargs["base_url"] = base_url
        logger.info("LLM → %s | model: %s", base_url, model_name)
    else:
        logger.info("LLM → OpenAI | model: %s", model_name)

    return ChatOpenAI(**kwargs)
