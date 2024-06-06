# Path: botwrap/openaiwrapper/assistants.py

import logging
from openaiwrapper.decorators import log_function_call

@log_function_call
def create_assistant(client, name, instructions, tools, model, description=None, tool_resources=None, metadata=None, temperature=1.0, top_p=1.0, response_format="auto"):
    """Create a new assistant with the given parameters."""
    try:
        assistant = client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=tools,
            model=model,
            description=description,
            tool_resources=tool_resources,
            metadata=metadata,
            temperature=temperature,
            top_p=top_p,
            response_format=response_format
        )
        logging.info(f"Assistant '{name}' created successfully.")
        return assistant
    except Exception as e:
        logging.error(f"Failed to create assistant: {e}")
        raise

@log_function_call
def delete_assistant(client, assistant_id):
    """Delete an existing assistant by ID."""
    try:
        client.beta.assistants.delete(assistant_id)
        logging.info(f"Assistant '{assistant_id}' deleted successfully.")
    except Exception as e:
        logging.error(f"Failed to delete assistant: {e}")
        raise

@log_function_call
def list_assistants(client, limit=20, order="desc", after=None, before=None):
    """List all assistants."""
    try:
        assistants = client.beta.assistants.list(
            limit=limit,
            order=order,
            after=after,
            before=before
        )
        logging.info(f"Listed {len(assistants['data'])} assistants successfully.")
        return assistants
    except Exception as e:
        logging.error(f"Failed to list assistants: {e}")
        raise

@log_function_call
def retrieve_assistant(client, assistant_id):
    """Retrieve a specific assistant by ID."""
    try:
        assistant = client.beta.assistants.retrieve(assistant_id)
        logging.info(f"Retrieved assistant with ID: {assistant_id}")
        return assistant
    except Exception as e:
        logging.error(f"Failed to retrieve assistant with ID '{assistant_id}': {e}")
        raise

@log_function_call
def modify_assistant(client, assistant_id, name=None, instructions=None, tools=None, model=None, description=None, tool_resources=None, metadata=None, temperature=None, top_p=None, response_format=None):
    """Modify an existing assistant."""
    try:
        assistant = client.beta.assistants.update(
            assistant_id=assistant_id,
            name=name,
            instructions=instructions,
            tools=tools,
            model=model,
            description=description,
            tool_resources=tool_resources,
            metadata=metadata,
            temperature=temperature,
            top_p=top_p,
            response_format=response_format
        )
        logging.info(f"Modified assistant with ID: {assistant_id}")
        return assistant
    except Exception as e:
        logging.error(f"Failed to modify assistant with ID '{assistant_id}': {e}")
        raise
