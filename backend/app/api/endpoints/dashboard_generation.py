"""
Questions endpoints module.
Defines API routes related to question processing and LLM interactions.
"""

from fastapi import APIRouter
from app.schemas.schema import WebpageGenerationRequest
from app.services.webpage_generation_pipeline import generate_webpage

generate_dashboard_router = APIRouter()

@generate_dashboard_router.post("/dashboard_generation")
async def generate_dashboard(q: WebpageGenerationRequest):
    """
    Process a webpage generation request and generate a webpage response using LLM.

    Args:
        q: WebpageGenerationRequest object containing the request text.

    Returns:
        Dictionary containing the generated answer/webpage content.
    """
    message = generate_webpage(q.text)
    return {"answer": message}
