# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\decorators.py

import logging
from functools import wraps

def log_function_call(func):
    """Decorator to log function calls, inputs, and outputs."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Function '{func.__name__}' returned: {result}")
            return result
        except Exception as e:
            logging.error(f"Function '{func.__name__}' raised an error: {e}")
            raise
    return wrapper
