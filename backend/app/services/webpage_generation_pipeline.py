"""
LLM service module.
Contains AI/LLM-related business logic for generating webpages and processing questions.
"""

import re
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from app.schemas.schema import market_analyzer_parser, webpage_generation_parser
from app.prompts.loader import load_prompt
from app.utils.save_generated_snippet import save_html_code, execute_generated_html
from app.core.logging import get_logger
from app.core.config import settings
import json

logger = get_logger(__name__)

def get_llm() -> AzureChatOpenAI:
    """
    Initialize and return Azure Chat OpenAI LLM instance.

    Returns:
        Configured AzureChatOpenAI instance.
    """
    llm = AzureChatOpenAI(
        azure_deployment=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
        api_version=settings.AZURE_OPENAI_API_VERSION,
        api_key=settings.AZURE_OPENAI_API_KEY,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
        temperature=0,
    )
    return llm

def generate_basic_html_code(question: str) -> str:
    """
    Generate a webpage using LLM based on the user's question.

    Uses Azure OpenAI to generate HTML + JavaScript code based on requirements.
    Saves the generated webpage to the frontend folder and opens it in browser.

    Args:
        question: The user's requirement for the webpage.

    Returns:
        Success message indicating webpage generation and browser opening.

    Raises:
        Exception: If LLM request fails or file operations fail.
    """
    try:
        # Get LLM
        llm = get_llm()

        # Load prompt template from file
        prompt_text = load_prompt("code_generation_prompt.txt")
        prompt = PromptTemplate.from_template(prompt_text)

        logger.info(f"Generating webpage for user request...")

        # Create chain and invoke LLM
        chain = prompt | llm
        response = chain.invoke({"question": question})

        html_code = response.content
        output_path = save_html_code(html_code)

        logger.info(f"Webpage generated successfully at {output_path}")

        # Open in browserb
        execute_generated_html(output_path)

        return "Webpage generated and opened in browser!"

    except Exception as e:
        logger.error(f"Error generating webpage: {str(e)}")
        raise


def generate_webpage(user_request: str) -> str:
    """
    Generate a complete webpage using a two-step LLM pipeline based on the user's request.

    Step 1 analyzes the target market and industry standards.
    Step 2 generates structured HTML content for the webpage using those insights.

    The generated HTML is saved to the frontend directory and automatically opened in the browser.

    Args:
        user_request (str): User's description of the desired webpage.

    Returns:
        str: Success message confirming webpage generation and browser launch.

    Raises:
        Exception: If LLM processing, parsing, file saving, or browser execution fails.
    """
    try:
        # Get LLM
        llm = get_llm()
        logger.info(f"Processing user request. Understanding market and industry standards...")
        # Step 1: LLM1 → Market + Standards
        market_analyzer_prompt = load_prompt("market_analyzer_prompt.txt")
        market_analyzer_prompt = PromptTemplate.from_template(market_analyzer_prompt)
        msg = HumanMessage(content=market_analyzer_prompt.format(request=user_request))
        llm1_response = llm.generate([[msg]]) 
        llm1_data = market_analyzer_parser.parse(llm1_response.generations[0][0].text)
        market = llm1_data.market
        industry_standards = llm1_data.industry_standards

        logger.info(f"Generating webpage for user request...")
        # Step 2: LLM2 → Generate Webpage
        webpage_generation_prompt = load_prompt("webpage_generation_prompt.txt")
        webpage_generation_prompt = PromptTemplate.from_template(webpage_generation_prompt)
        msg2 = HumanMessage(content=webpage_generation_prompt.format(
            request=user_request,
            market=market,
            industry_standards=industry_standards
        ))
        llm2_response = llm.generate([[msg2]])  # double list
        llm2_data = webpage_generation_parser.parse(llm2_response.generations[0][0].text)
        html_code = llm2_data.generated_webpage

        output_path = save_html_code(html_code)

        logger.info(f"Webpage generated successfully at {output_path}")

        # Open in browserb
        execute_generated_html(output_path)

        return "Webpage generated and opened in browser!"

    except Exception as e:
        logger.error(f"Error generating webpage: {str(e)}")
        raise
