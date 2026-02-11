"""
Main API router module.
Combines and registers all endpoint routers for the FastAPI application.
"""
from fastapi import APIRouter
from app.api.endpoints.dashboard_generation import generate_dashboard_router
from app.api.endpoints.db_insertion import db_insertion_router

api_router = APIRouter()

api_router.include_router(generate_dashboard_router, prefix="/api", tags=["dashboard_generation"])
api_router.include_router(db_insertion_router, prefix="/api", tags=["db_insertion"])