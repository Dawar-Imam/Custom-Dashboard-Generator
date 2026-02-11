"""
Database configuration module.
Manages database connection, session creation, and ORM initialization.
"""
from sqlalchemy.orm import Session
from app.core.connection import get_db_session
from app.schemas.db_schema import WebpageTemplate
from typing import List, Dict
from app.core.logging import get_logger

# Logger
logger = get_logger(__name__)

# -----------------------------
# Fetch all markets from DB
# -----------------------------
def get_all_markets() -> list:
    """Fetch all unique markets from the DB."""
    try:
        db: Session = next(get_db_session())
        results = db.query(WebpageTemplate.market).distinct().all()
        markets = [row[0] for row in results]

        logger.info(f"Fetched {len(markets)} unique markets from DB: {markets}")
        return markets
    except Exception as e:
        logger.error(f"Error fetching markets: {e}")
        return []

# -----------------------------
# Fetch templates by market
# -----------------------------
def fetch_templates(market: str) -> List[Dict]:
    logger.info(f"fetch_templates called with market={market}")
    try:
        db: Session = next(get_db_session())
        results = db.query(WebpageTemplate).filter_by(market=market).all()

        templates = []
        for row in results:
            templates.append({
                "id": row.id,
                "market": row.market,
                "description": row.description,
            })

        logger.info(f"fetch_templates returning {len(templates)} templates for market={market}")
        return templates
    except Exception as e:
        logger.exception(f"Error fetching templates for market={market}: {e}")
        return []


# -----------------------------
# Insert new template (unique market)
# -----------------------------
def insert_template(market: str, description: str) -> int:
    logger.info(f"insert_template called with market={market}")
    try:
        db: Session = next(get_db_session())

        # Check if market already exists
        existing = db.query(WebpageTemplate).filter_by(market=market).first()
        if existing:
            logger.info(f"Market '{market}' already exists. Skipping insert.")
            return existing.id  # optionally return existing ID

        # Insert new entry
        new_entry = WebpageTemplate(
            market=market,
            description=description,
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        logger.info(f"Inserted new template id={new_entry.id} for market={market}")
        return new_entry.id

    except Exception as e:
        logger.exception(f"Error inserting template for market={market}: {e}")
        return -1


# -----------------------------
# Update template by market
# -----------------------------
def update_template_by_market(market: str, description: str = None) -> bool:
    logger.info(f"update_template_by_market called with market={market}")
    try:
        db: Session = next(get_db_session())

        # Check if market exists
        entry = db.query(WebpageTemplate).filter_by(market=market).first()
        if not entry:
            logger.info(f"Market '{market}' does not exist. Cannot update.")
            return False

        # Update fields if provided
        if description:
            entry.description = description

        db.commit()
        logger.info(f"Market '{market}' updated successfully.")
        return True

    except Exception as e:
        logger.exception(f"Error updating template for market={market}: {e}")
        return False



# -----------------------------
# Delete template by ID
# -----------------------------
def delete_template(template_id: int) -> bool:
    logger.info(f"delete_template called with template_id={template_id}")
    try:
        db: Session = next(get_db_session())
        entry = db.query(WebpageTemplate).filter_by(id=template_id).first()
        if not entry:
            logger.info(f"Template id={template_id} not found. Nothing to delete.")
            return False
        db.delete(entry)
        db.commit()
        logger.info(f"Deleted template id={template_id}")
        return True
    except Exception as e:
        logger.exception(f"Error deleting template id={template_id}: {e}")
        return False