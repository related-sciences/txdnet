import logging
from pathlib import Path
from typing import Any
from typing import Callable
from typing import TypeVar

import openai
from tenacity import retry_if_not_exception_type
from tenacity import Retrying
from tenacity import stop_after_attempt
from tenacity import wait_exponential

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "gpt-4"

T = TypeVar("T")


def retry(
    fn: Callable[..., T], max_attempts: int = 5, max_wait_seconds: int = 180
) -> Callable[..., T]:
    return Retrying(  # type: ignore[no-any-return]
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(min=1, max=max_wait_seconds),
        retry=retry_if_not_exception_type(openai.InvalidRequestError),
        reraise=True,
    ).wraps(fn)


def chat_completion_from_template(
    prompt_template: Path | str,
    model: str = DEFAULT_MODEL,
    temperature: float | None = None,
    **template_args: Any,
) -> str:
    with Path(prompt_template).open("r", encoding="utf-8") as f:
        prompt = f.read().strip().format(**template_args)
    return chat_completion(prompt, model=model, temperature=temperature)


def chat_completion(
    prompt: str,
    model: str = DEFAULT_MODEL,
    temperature: float | None = None,
    **api_args: Any,
) -> str:
    logger.info(f"Prompt (temperature={temperature}, model={model}):\n{prompt}")
    if temperature is not None:
        api_args["temperature"] = temperature
    chat_completion = openai.ChatCompletion.create(
        model=model, messages=[{"role": "user", "content": prompt}], **api_args
    )
    response = str(chat_completion.choices[0].message.content)
    logger.info(f"Response:\n{response}")
    return response


def text_embedding(text: str, model: str = "text-embedding-ada-002") -> list[float]:
    text = text.replace(
        "\n", " "
    )  # see https://platform.openai.com/docs/guides/embeddings/use-cases
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]  # type: ignore[no-any-return]
