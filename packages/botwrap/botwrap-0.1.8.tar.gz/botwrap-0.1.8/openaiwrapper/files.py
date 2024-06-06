# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\files.py

import logging
import os
from openai import OpenAI
from openaiwrapper.decorators import log_function_call

@log_function_call
def upload_file(client, file_path, purpose):
    """Upload a file to OpenAI."""
    try:
        with open(file_path, "rb") as file:
            uploaded_file = client.files.create(file=file, purpose=purpose)
            logging.info(f"File '{file_path}' uploaded successfully with ID: {uploaded_file['id']}")
            return uploaded_file
    except Exception as e:
        logging.error(f"Failed to upload file '{file_path}': {e}")
        raise

@log_function_call
def list_files(client, purpose=None):
    """List files uploaded to OpenAI."""
    try:
        if purpose:
            files = client.files.list(purpose=purpose)
        else:
            files = client.files.list()
        logging.info(f"Listed {len(files['data'])} files successfully.")
        return files
    except Exception as e:
        logging.error(f"Failed to list files: {e}")
        raise

@log_function_call
def retrieve_file(client, file_id):
    """Retrieve information about a specific file."""
    try:
        file_info = client.files.retrieve(file_id)
        logging.info(f"Retrieved file info for file ID: {file_id}")
        return file_info
    except Exception as e:
        logging.error(f"Failed to retrieve file info for file ID '{file_id}': {e}")
        raise

@log_function_call
def delete_file(client, file_id):
    """Delete a file from OpenAI."""
    try:
        deletion_status = client.files.delete(file_id)
        logging.info(f"Deleted file with ID: {file_id}")
        return deletion_status
    except Exception as e:
        logging.error(f"Failed to delete file with ID '{file_id}': {e}")
        raise

@log_function_call
def get_file_content(client, file_id):
    """Retrieve the contents of the specified file."""
    try:
        content = client.files.content(file_id)
        logging.info(f"Retrieved content for file ID: {file_id}")
        return content
    except Exception as e:
        logging.error(f"Failed to retrieve content for file ID '{file_id}': {e}")
        raise
