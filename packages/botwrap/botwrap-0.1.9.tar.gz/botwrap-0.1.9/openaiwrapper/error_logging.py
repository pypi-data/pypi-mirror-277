# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\error_logging.py

import logging

def configure_logging():
    """Configure logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

def log_error(e):
    """Log an error message."""
    logging.error(f"An error occurred: {e}")
