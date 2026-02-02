"""
Logging configuration module.
Sets up logging configuration and handlers for the application.
"""

import logging
import logging.handlers
import sys
from pathlib import Path
from typing import Optional


# Create logs directory if it doesn't exist
LOG_DIR = Path(__file__).parent.parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


class LogConfig:
    """Logging configuration class for the application."""

    # Log level
    LEVEL: str = logging.INFO

    # Log format
    FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    # Log files
    LOG_FILE: Path = LOG_DIR / "app.log"
    ERROR_LOG_FILE: Path = LOG_DIR / "error.log"


def setup_logging(
    log_level: Optional[str] = None,
    log_file: Optional[Path] = None,
) -> logging.Logger:
    """
    Configure logging for the application.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Defaults to INFO.
        log_file: Path to log file. Defaults to app.log.

    Returns:
        Logger instance configured for the application.
    """
    log_level = log_level or LogConfig.LEVEL
    log_file = log_file or LogConfig.LOG_FILE

    # Get root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Clear existing handlers
    logger.handlers.clear()

    # Create formatter
    formatter = logging.Formatter(
        fmt=LogConfig.FORMAT,
        datefmt=LogConfig.DATE_FORMAT,
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Error file handler
    error_handler = logging.handlers.RotatingFileHandler(
        LogConfig.ERROR_LOG_FILE,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the specified name.

    Args:
        name: Name of the logger (usually module name).

    Returns:
        Logger instance.
    """
    return logging.getLogger(name)
