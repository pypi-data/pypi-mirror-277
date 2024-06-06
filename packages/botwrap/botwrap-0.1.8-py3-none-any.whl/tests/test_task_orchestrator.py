# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_task_orchestrator.py

# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_task_orchestrator.py

import logging
import pytest
from unittest.mock import AsyncMock, patch
from openaiwrapper.task_orchestrator import TaskOrchestrator
import asyncio

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture
def mock_make_api_call():
    return AsyncMock()

@pytest.fixture
def mock_config():
    with patch('openaiwrapper.task_orchestrator.get_config') as mock_get_config:
        mock_get_config.return_value = type('MockConfig', (), {
            'TEAM_MEMBERS': [
                {"id": "1", "name": "ParserAssistant", "role": "parser", "instructions": "Parse tasks", "model": "text-davinci-003"},
                {"id": "2", "name": "ExecutorAssistant", "role": "executor", "instructions": "Execute tasks", "model": "text-davinci-003"},
            ]
        })
        yield mock_get_config

@pytest.fixture
def task_orchestrator(mock_make_api_call, mock_config):
    return TaskOrchestrator(make_api_call=mock_make_api_call)

@pytest.fixture
def sample_task_description():
    return "This is a test task that requires parsing."

@pytest.fixture
def parsed_tasks_response():
    return {
        "tasks": [
            {
                "task_id": "test_thread-requester-1",
                "description": "First subtask",
                "dependencies": [],
                "assigned_by": "requester"
            },
            {
                "task_id": "test_thread-requester-2",
                "description": "Second subtask",
                "dependencies": ["test_thread-requester-1"],
                "assigned_by": "requester"
            }
        ]
    }

@pytest.fixture
def create_assistant_response():
    return {
        "id": "3",
        "name": "DynamicAssistant",
        "role": "dynamic",
        "instructions": "Dynamically created assistant",
        "model": "text-davinci-003"
    }

@pytest.mark.asyncio
async def test_parse_task_description(task_orchestrator, mock_make_api_call, sample_task_description, parsed_tasks_response):
    mock_make_api_call.return_value = parsed_tasks_response

    logger.info('Parsing task description...')
    try:
        tasks = await task_orchestrator.parse_task_description(sample_task_description)
        
        logger.debug(f'Parsed tasks: {tasks}')
        assert tasks is not None
        assert isinstance(tasks, list)
        assert len(tasks) > 0
    except Exception as e:
        logger.error("Error during task parsing", exc_info=True)
        raise

@pytest.mark.asyncio
async def test_orchestrate_tasks(task_orchestrator, mock_make_api_call, sample_task_description, parsed_tasks_response, create_assistant_response):
    completed_tasks = set()

    async def side_effect(endpoint, method="POST", data=None, **kwargs):
        logger.debug(f"API call to {endpoint} with data: {data}")
        if "assistants/create" in endpoint:
            return create_assistant_response
        elif "parse_task" in endpoint:
            return parsed_tasks_response
        elif "execute_task" in endpoint:
            task_id = data["task"]["task_id"]
            if task_id == "test_thread-requester-1":
                logger.info(f"Task {task_id} completed.")
                completed_tasks.add(task_id)
                return {"status": "completed"}
            elif task_id == "test_thread-requester-2":
                dependencies = data["task"]["dependencies"]
                if "test_thread-requester-1" in dependencies:
                    logger.info(f"Task {task_id} completed.")
                    completed_tasks.add(task_id)
                    return {"status": "completed"}
                else:
                    missing_deps = set(dependencies) - completed_tasks
                    logger.warning(f"Task {task_id} cannot be completed, missing dependencies: {missing_deps}")
                    return {"status": "pending"}

    mock_make_api_call.side_effect = side_effect

    thread_id = "test_thread"
    requesting_assistant_id = "requester"
    logger.info('Starting orchestration...')

    try:
        tasks = await asyncio.wait_for(
            task_orchestrator.orchestrate(sample_task_description, thread_id, requesting_assistant_id),
            timeout=10.0
        )
    except asyncio.TimeoutError:
        logger.error("Orchestration timed out")
        pytest.fail("Orchestration timed out")
    except Exception as e:
        logger.error("An unexpected error occurred during the orchestration process.", exc_info=True)
        raise

    logger.info(f"Completed tasks: {tasks['completed_tasks']}")
    assert len(tasks["completed_tasks"]) == 2, f"Only the following tasks were completed: {tasks['completed_tasks']}"

    for task_id, task_details in tasks["completed_tasks"].items():
        logger.debug(f"Task {task_id} details: {task_details}")
        assert task_details["status"] == "completed"
        assert "task_id" in task_details
        assert task_details["task_id"].startswith("test_thread-requester-")

    logger.info("Orchestration finished. Completed tasks:")
    for task_id, task_details in tasks["completed_tasks"].items():
        logger.info(f" - {task_id}: {task_details}")
