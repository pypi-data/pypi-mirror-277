# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\logging_config.py

import logging
from typing import Optional

def configure_logging(log_file: str = 'application.log', level: int = logging.INFO) -> logging.Logger:
    """Setup logging configuration for the application."""
    logger = logging.getLogger('openaiwrapper')
    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(console_handler)
        logger.setLevel(level)
    return logger

def get_default_logger() -> logging.Logger:
    return configure_logging()
