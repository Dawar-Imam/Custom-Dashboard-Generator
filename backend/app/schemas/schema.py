"""
Question schema module.
Defines Pydantic models for Question data validation and database schema.
"""

from pydantic import BaseModel


class WebpageGenerationRequest(BaseModel):
    """Pydantic model for webpage generation request data validation."""
    text: str
