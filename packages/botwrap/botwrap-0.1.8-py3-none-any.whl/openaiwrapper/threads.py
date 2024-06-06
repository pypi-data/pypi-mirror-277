# File: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\threads.py

import logging
from openaiwrapper.decorators import log_function_call

@log_function_call
def create_thread(client, messages=None, tool_resources=None, metadata=None):
    """Create a new thread for conversation."""
    try:
        thread = client.beta.threads.create(
            messages=messages,
            tool_resources=tool_resources,
            metadata=metadata
        )
        logging.info("Thread created successfully.")
        return thread
    except Exception as e:
        logging.error(f"Failed to create thread: {e}")
        raise

@log_function_call
def retrieve_thread(client, thread_id):
    """Retrieve an existing thread by ID."""
    try:
        thread = client.beta.threads.retrieve(thread_id)
        logging.info(f"Retrieved thread with ID: {thread_id}")
        return thread
    except Exception as e:
        logging.error(f"Failed to retrieve thread with ID '{thread_id}': {e}")
        raise

@log_function_call
def update_thread(client, thread_id, tool_resources=None, metadata=None):
    """Modify an existing thread by ID."""
    try:
        thread = client.beta.threads.update(
            thread_id=thread_id,
            tool_resources=tool_resources,
            metadata=metadata
        )
        logging.info(f"Updated thread with ID: {thread_id}")
        return thread
    except Exception as e:
        logging.error(f"Failed to update thread with ID '{thread_id}': {e}")
        raise

@log_function_call
def delete_thread(client, thread_id):
    """Delete an existing thread by ID."""
    try:
        deletion_status = client.beta.threads.delete(thread_id)
        logging.info(f"Deleted thread with ID: {thread_id}")
        return deletion_status
    except Exception as e:
        logging.error(f"Failed to delete thread with ID '{thread_id}': {e}")
        raise

@log_function_call
def add_message_to_thread(client, thread_id, role, content):
    """Add a message to an existing thread."""
    try:
        message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role=role,
            content=content,
        )
        logging.info(f"Message added to thread '{thread_id}' successfully.")
        return message
    except Exception as e:
        logging.error(f"Failed to add message to thread: {e}")
        raise

@log_function_call
def list_thread_messages(client, thread_id):
    """List all messages in a thread."""
    try:
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        logging.info(f"Listed messages for thread '{thread_id}' successfully.")
        return messages
    except Exception as e:
        logging.error(f"Failed to list messages for thread: {e}")
        raise
