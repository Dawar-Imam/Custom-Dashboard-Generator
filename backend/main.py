"""
FastAPI application entry point.
Initializes and configures the FastAPI application with all routes, middleware, and settings.
"""

from fastapi import FastAPI
from app.core.logging import setup_logging, get_logger
from app.api.router import api_router
import uvicorn
from sqlalchemy import inspect
from app.core.connection import engine
from app.database.manage_db import create_tables

# Initialize logging
setup_logging()
logger = get_logger(__name__)

# Create FastAPI application
app = FastAPI(
    title="Custom Dashboard Generation API",
    description="API for generating custom dashboards with AI/LLM capabilities",
    version="1.0.0",
)

# Include routers
app.include_router(api_router)


@app.get("/")
async def root():
    """Root endpoint for API health check."""
    return {"message": "API is running", "status": "ok"}

def ensure_tables_exist():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if "webpage_templates" not in tables:
        logger.info("Table not found. Creating...")
        create_tables()
    else:
        logger.info("Table already exists. Skipping creation.")

if __name__ == "__main__":

    ensure_tables_exist()

    logger.info("Starting API server...")
    
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000,
        reload=False,
    )