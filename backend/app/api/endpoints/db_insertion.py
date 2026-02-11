"""
Questions endpoints module.
Defines API routes related to question processing and LLM interactions.
"""

from fastapi import APIRouter
from fastapi import Response, status
from app.schemas.schema import WebpageGenerationWithoutTemplateResponse
from app.database.dashboard_generation import insert_template
from app.core.logging import get_logger

db_insertion_router = APIRouter()
logger = get_logger(__name__)

@db_insertion_router.post("/webpage_insertion")
async def generate_webpage(webpage_template: WebpageGenerationWithoutTemplateResponse):
    """
    Process a webpage generation request and generate a webpage response using LLM.

    Args:
        q: WebpageGenerationRequest object containing the request text.

    Returns:
        Dictionary containing the generated answer/webpage content.
    """
    logger.info(f"Inserting new webpage template for market '{webpage_template.market}' into DB.")
    insert_template(webpage_template.market, webpage_template.description)
    return Response(content="OK", status_code=status.HTTP_200_OK)
