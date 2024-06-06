# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\vector_store_manager.py

import logging
from openai import OpenAI
from openaiwrapper.decorators import log_function_call

@log_function_call
def create_vector_store(client, name=None, file_ids=None, expires_after=None, chunking_strategy=None, metadata=None):
    """Create a vector store."""
    try:
        vector_store = client.beta.vector_stores.create(
            name=name,
            file_ids=file_ids,
            expires_after=expires_after,
            chunking_strategy=chunking_strategy,
            metadata=metadata,
        )
        logging.info(f"Vector store '{name}' created successfully with ID: {vector_store['id']}")
        return vector_store
    except Exception as e:
        logging.error(f"Failed to create vector store: {e}")
        raise

@log_function_call
def list_vector_stores(client, limit=20, order="desc", after=None, before=None):
    """List vector stores."""
    try:
        vector_stores = client.beta.vector_stores.list(
            limit=limit,
            order=order,
            after=after,
            before=before
        )
        logging.info(f"Listed {len(vector_stores['data'])} vector stores successfully.")
        return vector_stores
    except Exception as e:
        logging.error(f"Failed to list vector stores: {e}")
        raise

@log_function_call
def retrieve_vector_store(client, vector_store_id):
    """Retrieve a specific vector store."""
    try:
        vector_store = client.beta.vector_stores.retrieve(vector_store_id)
        logging.info(f"Retrieved vector store info for ID: {vector_store_id}")
        return vector_store
    except Exception as e:
        logging.error(f"Failed to retrieve vector store info for ID '{vector_store_id}': {e}")
        raise

@log_function_call
def update_vector_store(client, vector_store_id, name=None, expires_after=None, metadata=None):
    """Modify a vector store."""
    try:
        vector_store = client.beta.vector_stores.update(
            vector_store_id=vector_store_id,
            name=name,
            expires_after=expires_after,
            metadata=metadata,
        )
        logging.info(f"Updated vector store with ID: {vector_store_id}")
        return vector_store
    except Exception as e:
        logging.error(f"Failed to update vector store with ID '{vector_store_id}': {e}")
        raise

@log_function_call
def delete_vector_store(client, vector_store_id):
    """Delete a vector store."""
    try:
        deletion_status = client.beta.vector_stores.delete(vector_store_id)
        logging.info(f"Deleted vector store with ID: {vector_store_id}")
        return deletion_status
    except Exception as e:
        logging.error(f"Failed to delete vector store with ID '{vector_store_id}': {e}")
        raise

@log_function_call
def create_vector_store_file(client, vector_store_id, file_id, chunking_strategy=None):
    """Create a vector store file by attaching a File to a vector store."""
    try:
        vector_store_file = client.beta.vector_stores.files.create(
            vector_store_id=vector_store_id,
            file_id=file_id,
            chunking_strategy=chunking_strategy
        )
        logging.info(f"File '{file_id}' attached to vector store '{vector_store_id}' successfully.")
        return vector_store_file
    except Exception as e:
        logging.error(f"Failed to create vector store file: {e}")
        raise

@log_function_call
def list_vector_store_files(client, vector_store_id, limit=20, order="desc", after=None, before=None, filter=None):
    """List files in a vector store."""
    try:
        vector_store_files = client.beta.vector_stores.files.list(
            vector_store_id=vector_store_id,
            limit=limit,
            order=order,
            after=after,
            before=before,
            filter=filter
        )
        logging.info(f"Listed {len(vector_store_files['data'])} files in vector store '{vector_store_id}' successfully.")
        return vector_store_files
    except Exception as e:
        logging.error(f"Failed to list vector store files: {e}")
        raise

@log_function_call
def retrieve_vector_store_file(client, vector_store_id, file_id):
    """Retrieve a specific file in a vector store."""
    try:
        vector_store_file = client.beta.vector_stores.files.retrieve(
            vector_store_id=vector_store_id,
            file_id=file_id
        )
        logging.info(f"Retrieved file info for file ID '{file_id}' in vector store '{vector_store_id}'")
        return vector_store_file
    except Exception as e:
        logging.error(f"Failed to retrieve file info for file ID '{file_id}': {e}")
        raise

@log_function_call
def delete_vector_store_file(client, vector_store_id, file_id):
    """Delete a file from a vector store."""
    try:
        deletion_status = client.beta.vector_stores.files.delete(
            vector_store_id=vector_store_id,
            file_id=file_id
        )
        logging.info(f"Deleted file with ID '{file_id}' from vector store '{vector_store_id}'")
        return deletion_status
    except Exception as e:
        logging.error(f"Failed to delete file with ID '{file_id}': {e}")
        raise
