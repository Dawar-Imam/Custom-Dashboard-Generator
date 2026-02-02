"""
API client module.
Handles all HTTP requests and communication with the FastAPI backend.
"""
import requests
from typing import Dict, Any

API_URL = "http://127.0.0.1:8000"


def ask_llm(question: str) -> Dict[str, Any]:
    """
    Send a question to the backend LLM and get the generated webpage.

    Args:
        question: User's description of the webpage to generate.

    Returns:
        Dictionary with the response from the backend API.

    Raises:
        requests.RequestException: If the API request fails.
    """
    try:
        response = requests.post(
            f"{API_URL}/api/dashboard_generation",
            json={"text": question},
            timeout=300,  # 5 minute timeout for LLM generation
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")