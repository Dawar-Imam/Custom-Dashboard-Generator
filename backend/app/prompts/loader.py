"""
Prompts loader module.
Loads prompt templates from .txt files with caching for efficient reuse.
"""

from functools import lru_cache
from pathlib import Path

BASE = Path(__file__).parent

@lru_cache
def load_prompt(name: str) -> str:
    """
    Load a prompt template from a .txt file.

    Prompts are cached for efficient reuse across multiple calls.

    Args:
        name: Path to the prompt file relative to prompts folder (e.g., "code_generation_prompt.txt").

    Returns:
        Content of the prompt file as a string.

    Raises:
        FileNotFoundError: If the prompt file doesn't exist.
    """
    prompt_path = BASE / name
    return prompt_path.read_text(encoding="utf-8")