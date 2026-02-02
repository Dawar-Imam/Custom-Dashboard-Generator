"""
LLM service module.
Contains AI/LLM-related business logic for generating webpages and processing questions.
"""

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from app.prompts.loader import load_prompt
from app.utils.save_generated_snippet import save_html_code, execute_generated_html
from app.core.logging import get_logger
from app.core.config import settings

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

def generate_webpage(question: str) -> str:
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
