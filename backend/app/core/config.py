"""
Configuration module.
Manages application settings, environment variables, and configuration parameters.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


PG_HOST: str = os.getenv("PG_HOST")
PG_PORT: str = os.getenv("PG_PORT", "5432")
PG_USER: str = os.getenv("PG_USER_NAME")
PG_PASSWORD: str = os.getenv("PG_PASSWORD")
PG_DATABASE: str = os.getenv("PG_DATABASE")

DATABASE_URL = (
    f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
)

class Settings:
    """Application settings and configuration."""

    # Azure OpenAI Configuration
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION", "")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_DEPLOYMENT_NAME: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")

    # Application Settings
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    PROJECT_NAME: str = "Custom Dashboard Generation API"


settings = Settings()

