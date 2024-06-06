# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\task_orchestrator.py

import logging
from typing import Any, Dict, List, Optional
from .utils import generate_task_id
from .config import get_config

class TaskOrchestrator:
    def __init__(self, make_api_call, logger: Optional[logging.Logger] = None):
        self.make_api_call = make_api_call
        self.logger = logger or self._setup_logger()
        self.team = {}
        self.max_retries = 3
        self.config = get_config()
        self.configure_team(self.config.TEAM_MEMBERS)

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger(__name__)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levellevelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    async def parse_task_description(self, description: str) -> List[Dict[str, Any]]:
        self.logger.info(f"Parsing task description: {description}")
        parser_assistant = self.get_assistant_by_role("parser")
        if not parser_assistant:
            raise ValueError("Parser assistant not configured.")
        response = await self.make_api_call(
            endpoint=f"assistants/{parser_assistant['id']}/parse_task",
            method="POST",
            data={"description": description}
        )
        self.logger.debug(f"Parsed tasks: {response['tasks']}")
        return response["tasks"]

    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.info(f"Executing task: {task['task_id']}")
        response = await self.make_api_call(
            endpoint="assistants/execute_task",
            method="POST",
            data={"task": task}
        )
        task["status"] = "completed"
        self.logger.debug(f"Executed task: {task['task_id']} with response: {response}")
        return response

    def resolve_dependencies(self, task: Dict[str, Any], completed_tasks: Dict[str, Any]) -> bool:
        dependencies = task.get('dependencies', [])
        self.logger.info(f"Resolving dependencies for task {task['task_id']}: {dependencies}")
        for dep in dependencies:
            if dep not in completed_tasks:
                self.logger.info(f"Dependency {dep} not completed for task {task['task_id']}")
                return False
        return True

    async def handle_task_failure(self, task: Dict[str, Any], feedback: str) -> None:
        retries = task.get("retries", 0)
        if retries < self.max_retries:
            task["retries"] = retries + 1
            task["feedback"] = feedback
            self.logger.info(f"Retrying task {task['task_id']}, attempt {retries + 1}")
            await self.execute_task(task)
        else:
            self.logger.error(f"Task {task['task_id']} failed after {self.max_retries} attempts")
            task["status"] = "failed"
            parent_id = task.get("assigned_by")
            if parent_id:
                parent_task = completed_tasks.get(parent_id)
                if parent_task:
                    parent_task["status"] = "failed"
                    parent_task["feedback"] = feedback
                    await self.execute_task(parent_task)
                else:
                    self.logger.error(f"Parent task {parent_id} not found")

    def configure_team(self, team_config: List[Dict[str, Any]]) -> None:
        self.logger.info("Configuring team of personas")
        self.team = {member['id']: member for member in team_config}
        self.logger.info(f"Configured team: {self.team}")

    def get_assistant_by_role(self, role: str) -> Optional[Dict[str, Any]]:
        for assistant in self.team.values():
            if assistant['role'] == role:
                return assistant
        return None

    async def orchestrate(self, task_description: str, thread_id: str, requesting_assistant_id: str) -> Dict[str, Any]:
        self.logger.info(f"Orchestrating task: {task_description}")
        tasks = await self.parse_task_description(task_description)
        completed_tasks = {}

        while tasks:
            task = tasks.pop(0)
            task_id = generate_task_id(thread_id, requesting_assistant_id)
            task["task_id"] = task_id
            task["assigned_by"] = requesting_assistant_id
            if self.resolve_dependencies(task, completed_tasks):
                try:
                    response = await self.execute_task(task)
                    completed_tasks[task['task_id']] = task  # Add the task itself to completed tasks
                except Exception as e:
                    feedback = str(e)
                    await self.handle_task_failure(task, feedback)
            else:
                self.logger.info(f"Dependencies not resolved for task {task['task_id']}")
                tasks.append(task)  # Re-add task to end of the list if dependencies are not resolved

        self.logger.info(f"Final completed_tasks: {completed_tasks}")
        return {"completed_tasks": completed_tasks}
