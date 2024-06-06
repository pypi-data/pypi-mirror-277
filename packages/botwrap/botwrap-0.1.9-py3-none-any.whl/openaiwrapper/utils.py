# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\utils.py

import aiohttp
import logging
import asyncio
import hashlib
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

async def make_api_call(session, url, method='POST', headers=None, json=None):
    try:
        async with session.request(method=method, url=url, headers=headers, json=json) as response:
            logger.info(f"Response status: {response.status}")
            response_text = await response.text()
            logger.debug(f"Response text: {response_text}")

            response.raise_for_status()

            return await response.json()
    except aiohttp.ClientResponseError as e:
        logger.error(f"HTTP error occurred: {e.status}, {e.message}")
        logger.error(f"Failed request data: {json}")
        try:
            error_details = await e.response.text()
            logger.error(f"Error details: {error_details}")
        except Exception:
            logger.error("Failed to retrieve error details.")
        raise
    except aiohttp.ClientError as e:
        logger.error("Client error during the API request.", exc_info=True)
        raise
    except Exception as e:
        logger.error("Unexpected error", exc_info=True)
        raise

async def make_api_call_with_retry(session: aiohttp.ClientSession, url: str, method: str = 'POST', headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, str]] = None, retries: int = 3) -> Dict[str, Any]:
    for attempt in range(retries):
        try:
            return await make_api_call(session, url, method, headers, json)
        except aiohttp.ClientResponseError as e:
            if attempt < retries - 1:
                logger.warning(f"Retrying API call. Attempt {attempt + 1} of {retries}.")
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
            else:
                logger.error("Max retries reached. Failing.")
                raise

def generate_task_id(thread_id: str, requesting_assistant_id: str) -> str:
    unique_string = f"{thread_id}-{requesting_assistant_id}"
    return hashlib.sha256(unique_string.encode()).hexdigest()
