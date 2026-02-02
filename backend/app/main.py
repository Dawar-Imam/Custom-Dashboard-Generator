"""
FastAPI application entry point.
Initializes and configures the FastAPI application with all routes, middleware, and settings.
"""

from fastapi import FastAPI
from app.core.logging import setup_logging, get_logger
from app.api.router import api_router
import uvicorn
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


if __name__ == "__main__":
    
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000,
        reload=True,
    )