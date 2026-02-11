"""
Question schema module.
Defines Pydantic models for Question data validation and database schema.
"""

from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from typing import List


class WebpageGenerationRequest(BaseModel):
    """Pydantic model for webpage generation request data validation."""
    text: str

class MarketResponse(BaseModel):
    market: str
    dashboard_requirements: str

class WebpageGenerationResponse(BaseModel):
    market: str
    generated_webpage: str

class WebpageGenerationWithoutTemplateResponse(BaseModel):
    market: str
    description: str
    generated_webpage: str

market_analyzer_parser = PydanticOutputParser(pydantic_object=MarketResponse)
webpage_generation_parser = PydanticOutputParser(pydantic_object=WebpageGenerationResponse)
webpage_generation_without_template_parser = PydanticOutputParser(pydantic_object=WebpageGenerationWithoutTemplateResponse)
