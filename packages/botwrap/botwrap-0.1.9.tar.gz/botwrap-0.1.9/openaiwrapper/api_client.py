# File: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\api_client.py

import os
import openai
from openaiwrapper.decorators import log_function_call

@log_function_call
def initialize_client():
    """Initialize the OpenAI client using the API key from environment variable."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    return openai.OpenAI(api_key=api_key)
