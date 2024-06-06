# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\messages.py

import logging
import asyncio
from typing import Any, Dict, List, Optional
from .error_logging import log_error_decorator

class MessageManager:
    def __init__(self, make_api_call, logger: Optional[logging.Logger] = None):
        self.make_api_call = make_api_call
        self.logger = logger or logging.getLogger('openaiwrapper')
        self._setup_logging()

    def _setup_logging(self) -> logging.Logger:
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        return self.logger

    @log_error_decorator
    async def create_message(self, thread_id: str, role: str, content: str, attachments: Optional[List[Dict[str, Any]]] = None, metadata: Optional[Dict[str, Any]] = None) -> Dict:
        """Create a message in a thread."""
        data = {
            "role": role,
            "content": content,
            "attachments": attachments if attachments is not None else [],
            "metadata": metadata if metadata is not None else {}
        }
        return await self.make_api_call(f"threads/{thread_id}/messages", method="POST", json=data)

    @log_error_decorator
    async def retrieve_message(self, thread_id: str, message_id: str) -> Dict:
        """Retrieve a specific message by ID."""
        return await self.make_api_call(f"threads/{thread_id}/messages/{message_id}", method="GET")

    @log_error_decorator
    async def list_messages(self, thread_id: str, limit: int = 20, order: str = "desc", after: Optional[str] = None, before: Optional[str] = None, run_id: Optional[str] = None) -> Dict:
        """List all messages in a thread."""
        params = {
            "limit": limit,
            "order": order,
            "after": after,
            "before": before,
            "run_id": run_id
        }
        return await self.make_api_call(f"threads/{thread_id}/messages", method="GET", params=params)

    @log_error_decorator
    async def update_message(self, thread_id: str, message_id: str, metadata: Optional[Dict[str, Any]] = None) -> Dict:
        """Update an existing message by ID."""
        data = {
            "metadata": metadata if metadata is not None else {}
        }
        return await self.make_api_call(f"threads/{thread_id}/messages/{message_id}", method="POST", json=data)

    @log_error_decorator
    async def delete_message(self, thread_id: str, message_id: str) -> Dict:
        """Delete a message from a thread."""
        return await self.make_api_call(f"threads/{thread_id}/messages/{message_id}", method="DELETE")

    @log_error_decorator
    async def wait_for_assistant_response(self, thread_id: str, timeout: int = 300, sleep_interval: int = 1) -> Dict[str, Any]:
        """Wait for an assistant's response in a thread."""
        end_time = asyncio.get_event_loop().time() + timeout
        while True:
            if asyncio.get_event_loop().time() > end_time:
                self.logger.error(f"Timeout while waiting for response in thread {thread_id}")
                raise asyncio.TimeoutError(f"Timeout while waiting for response in thread {thread_id}")
            response = await self.list_messages(thread_id)
            if response and response["data"]:
                self.logger.info(f"Received response in thread {thread_id}")
                return response
            await asyncio.sleep(sleep_interval)
