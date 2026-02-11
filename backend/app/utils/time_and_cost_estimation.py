import tiktoken
from app.core.config import settings
from langchain_community.callbacks.openai_info import TokenType, get_openai_token_cost_for_model
from app.core.logging import get_logger
import time

logger = get_logger(__name__)
encoder = tiktoken.encoding_for_model(settings.AZURE_OPENAI_DEPLOYMENT_NAME)

def count_tokens(text: str) -> int:
    return len(encoder.encode(text))

def estimate_token_cost_per_call(input_text: str, output_text: str):
    input_tokens = count_tokens(input_text)
    output_tokens = count_tokens(output_text)

    in_cost = get_openai_token_cost_for_model(
        settings.AZURE_OPENAI_DEPLOYMENT_NAME,
        input_tokens,
        token_type=TokenType.PROMPT  # input tokens
    )

    out_cost = get_openai_token_cost_for_model(
        settings.AZURE_OPENAI_DEPLOYMENT_NAME,
        output_tokens,
        token_type=TokenType.COMPLETION  # output tokens
    )

    return in_cost + out_cost

def log_execution_time(start_time: float, name: str):
    end_time = time.time()
    elapsed_seconds = end_time - start_time
    minutes = int(elapsed_seconds // 60)
    seconds = elapsed_seconds % 60
    logger.info(f"{name} | Execution time: {minutes} min {seconds:.2f} seconds")