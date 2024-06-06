# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\openai_wrapper.py

import asyncio
import logging
from typing import Dict, List, Any, Optional
from .api_client import OpenAIAPIClient
from .threads import ThreadManager
from .messages import MessageManager
from .runs import RunManager
from .tools import ToolsManager
from .vector_store_manager import VectorStoreManager
from .assistants import AssistantManager
from orchestrator.task_orchestrator import TaskOrchestrator
from .error_logging import log_error_decorator

class OpenAIWrapper:
    def __init__(self, api_key: str, logger: Optional[logging.Logger] = None):
        self.api_client = OpenAIAPIClient(api_key=api_key, logger=logger)
        self.logger = logger or logging.getLogger('openaiwrapper')
        self._setup_logging()
        self.setup_managers()

    def _setup_logging(self):
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levellevel)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    async def __aenter__(self):
        await self.api_client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.api_client.__aexit__(exc_type, exc_val, exc_tb)

    def setup_managers(self):
        make_api_call = self.api_client.make_api_call
        self.thread_manager = ThreadManager(make_api_call, self.logger)
        self.message_manager = MessageManager(make_api_call, self.logger)
        self.run_manager = RunManager(make_api_call, self.logger)
        self.tools_manager = ToolsManager(make_api_call, self.logger)
        self.vector_store_manager = VectorStoreManager(make_api_call, self.logger)
        self.assistant_manager = AssistantManager(make_api_call, self.logger)
        self.task_orchestrator = TaskOrchestrator(make_api_call, self.logger)

    async def _create_thread(self, assistant_id: str, messages: List[Dict[str, Any]]) -> str:
        thread_response = await self.thread_manager.create_thread(assistant_id=assistant_id, messages=messages)
        return thread_response['id']

    async def _create_run(self, thread_id: str, assistant_id: str) -> str:
        run_response = await self.run_manager.create_run(thread_id=thread_id, assistant_id=assistant_id)
        return run_response['id']

    @log_error_decorator(logger=None)
    async def run_assistant_workflow(self, assistant_id: str, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        try:
            thread_id = await self._create_thread(assistant_id, messages)
            run_id = await self._create_run(thread_id, assistant_id)
            run_result = await self.run_manager.wait_for_run_completion(thread_id, run_id)
            return run_result
        except Exception as e:
            self.logger.error(f"Error in assistant workflow: {e}")
            raise

    async def create_assistant(self, profile_name: str) -> str:
        assistant = await self.assistant_manager.create_assistant_from_profile(profile_name)
        return assistant['id']

    async def send_message_to_assistant(self, thread_id: str, message: Dict[str, Any]) -> Dict:
        message_response = await self.message_manager.create_message(thread_id, **message)
        return message_response

    async def reply_to_existing_thread(self, thread_id: str, assistant_id: str, message: Dict[str, Any]) -> Dict:
        await self.send_message_to_assistant(thread_id, message)
        run_response = await self._create_run(thread_id, assistant_id)
        return run_response

    async def validate_and_upload_file(self, file_path: str, purpose: str = "assistants") -> Dict:
        is_valid = await self.file_manager.validate_file_for_upload(file_path)
        if is_valid:
            return await self.file_manager.upload_file(file_path, purpose)
        else:
            self.logger.error(f"File validation failed: {file_path}")
            raise ValueError("File validation failed.")

    async def create_and_poll_assistant(self, profile_name: str, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        assistant_id = await self.create_assistant(profile_name)
        return await self.run_assistant_workflow(assistant_id, messages)
