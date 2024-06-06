# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\runs.py

import logging
from openaiwrapper.decorators import log_function_call
from openaiwrapper.utils import make_api_call_with_retry
import asyncio

@log_function_call
def create_run(client, thread_id, assistant_id, model=None, instructions=None, additional_instructions=None, additional_messages=None, tools=None, metadata=None, temperature=1.0, top_p=1.0, stream=None, max_prompt_tokens=None, max_completion_tokens=None, truncation_strategy=None, tool_choice="auto", response_format="auto"):
    """Create a run for a thread."""
    try:
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
            model=model,
            instructions=instructions,
            additional_instructions=additional_instructions,
            additional_messages=additional_messages,
            tools=tools,
            metadata=metadata,
            temperature=temperature,
            top_p=top_p,
            stream=stream,
            max_prompt_tokens=max_prompt_tokens,
            max_completion_tokens=max_completion_tokens,
            truncation_strategy=truncation_strategy,
            tool_choice=tool_choice,
            response_format=response_format
        )
        logging.info(f"Run created successfully for thread '{thread_id}' with assistant '{assistant_id}'.")
        return run
    except Exception as e:
        logging.error(f"Failed to create run for thread '{thread_id}': {e}")
        raise

@log_function_call
async def create_and_poll_run(client, thread_id, assistant_id, model=None, instructions=None, additional_instructions=None, additional_messages=None, tools=None, metadata=None, temperature=1.0, top_p=1.0, stream=None, max_prompt_tokens=None, max_completion_tokens=None, truncation_strategy=None, tool_choice="auto", response_format="auto", timeout=300, sleep_interval=1):
    """Create a run and poll for its completion."""
    try:
        run = create_run(client, thread_id, assistant_id, model, instructions, additional_instructions, additional_messages, tools, metadata, temperature, top_p, stream, max_prompt_tokens, max_completion_tokens, truncation_strategy, tool_choice, response_format)
        
        end_time = asyncio.get_event_loop().time() + timeout
        while True:
            if asyncio.get_event_loop().time() > end_time:
                logging.error(f"Timeout while waiting for run completion in thread {thread_id}")
                raise asyncio.TimeoutError(f"Timeout while waiting for run completion in thread {thread_id}")
            run_status = retrieve_run(client, thread_id, run.id)
            if run_status.status == 'completed':
                logging.info(f"Run completed successfully for thread '{thread_id}' with assistant '{assistant_id}'.")
                return run_status
            await asyncio.sleep(sleep_interval)
    except Exception as e:
        logging.error(f"Failed to create and poll run for thread '{thread_id}' with assistant '{assistant_id}': {e}")
        raise

@log_function_call
def retrieve_run(client, thread_id, run_id):
    """Retrieve a specific run by ID."""
    try:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        logging.info(f"Retrieved run with ID '{run_id}' for thread '{thread_id}'.")
        return run
    except Exception as e:
        logging.error(f"Failed to retrieve run with ID '{run_id}' for thread '{thread_id}': {e}")
        raise

@log_function_call
def update_run(client, thread_id, run_id, metadata=None):
    """Modify an existing run by ID."""
    try:
        run = client.beta.threads.runs.update(
            thread_id=thread_id,
            run_id=run_id,
            metadata=metadata
        )
        logging.info(f"Updated run with ID '{run_id}' for thread '{thread_id}'.")
        return run
    except Exception as e:
        logging.error(f"Failed to update run with ID '{run_id}' for thread '{thread_id}': {e}")
        raise

@log_function_call
def cancel_run(client, thread_id, run_id):
    """Cancel a run that is in progress."""
    try:
        run = client.beta.threads.runs.cancel(
            thread_id=thread_id,
            run_id=run_id
        )
        logging.info(f"Cancelled run with ID '{run_id}' for thread '{thread_id}'.")
        return run
    except Exception as e:
        logging.error(f"Failed to cancel run with ID '{run_id}' for thread '{thread_id}': {e}")
        raise

@log_function_call
def submit_tool_outputs(client, thread_id, run_id, tool_outputs, stream=None):
    """Submit tool outputs to a run that requires action."""
    try:
        run = client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread_id,
            run_id=run_id,
            tool_outputs=tool_outputs,
            stream=stream
        )
        logging.info(f"Submitted tool outputs for run with ID '{run_id}' in thread '{thread_id}'.")
        return run
    except Exception as e:
        logging.error(f"Failed to submit tool outputs for run with ID '{run_id}' in thread '{thread_id}': {e}")
        raise

