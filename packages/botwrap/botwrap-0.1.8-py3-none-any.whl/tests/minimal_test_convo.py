import asyncio
import sys
import logging
from orchestrator.task_orchestrator import TaskOrchestrator

# Setup logging
log_path = 'api_calls.log'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler for logging
file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.DEBUG)

# Console handler for logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Formatter for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
if logger.hasHandlers():
    logger.handlers.clear()
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info(f"Logging to file: {log_path}")

async def main(api_key, profile_paths):
    orchestrator = TaskOrchestrator(api_key, profile_paths)
    await orchestrator.load_profiles()
    await orchestrator.create_assistants()

    # Example tasks
    await orchestrator.create_task("Math Assistant", "I need to solve the equation `3x + 11 = 14`. Can you help me?")
    await orchestrator.create_task("Science Assistant", "Explain the theory of relativity.")
    
    await orchestrator.process_tasks()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python minimal_test_convo.py <api_key> <profile_path_1> [<profile_path_2> ...]")
    else:
        api_key = sys.argv[1]
        profile_paths = sys.argv[2:]
        asyncio.run(main(api_key, profile_paths))
