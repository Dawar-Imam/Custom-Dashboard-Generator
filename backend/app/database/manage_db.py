from app.core.connection import engine
from app.schemas.db_schema import Base
from app.core.logging import get_logger

logger = get_logger(__name__)

def create_tables():
    Base.metadata.create_all(bind=engine)
    logger.info("Table created successfully.")

def drop_tables():
    Base.metadata.drop_all(bind=engine)
    logger.info("Tables dropped.")