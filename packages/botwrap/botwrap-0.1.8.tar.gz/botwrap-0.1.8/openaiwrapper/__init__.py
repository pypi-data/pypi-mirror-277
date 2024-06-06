# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\__init__.py

import logging
from .api_client import initialize_client
from .assistants import (
    create_assistant,
    delete_assistant,
    list_assistants,
    retrieve_assistant,
    modify_assistant
)
from .threads import (
    create_thread,
    retrieve_thread,
    update_thread,
    delete_thread,
    add_message_to_thread,
    list_thread_messages
)
from .runs import create_and_poll_run
from .profiles import (
    load_coreteam_profile_1,
    load_coreteam_profile_2,
    load_coreteam_profile_3,
    load_coreteam_profile_4,
    load_coreteam_profile_5,
    load_coreteam_profile_6,
    load_non_coreteam_profile
)
from .files import (
    upload_file,
    list_files,
    retrieve_file,
    delete_file,
    get_file_content
)
from .vector_store_manager import (
    create_vector_store,
    list_vector_stores,
    retrieve_vector_store,
    update_vector_store,
    delete_vector_store,
    create_vector_store_file,
    list_vector_store_files,
    retrieve_vector_store_file,
    delete_vector_store_file
)
from .error_logging import configure_logging, log_error

# Configure logging for the package
configure_logging()

# Define what is exposed when the package is imported
__all__ = [
    'initialize_client',
    'create_assistant',
    'delete_assistant',
    'list_assistants',
    'retrieve_assistant',
    'modify_assistant',
    'create_thread',
    'retrieve_thread',
    'update_thread',
    'delete_thread',
    'add_message_to_thread',
    'list_thread_messages',
    'create_and_poll_run',
    'load_coreteam_profile_1',
    'load_coreteam_profile_2',
    'load_coreteam_profile_3',
    'load_coreteam_profile_4',
    'load_coreteam_profile_5',
    'load_coreteam_profile_6',
    'load_non_coreteam_profile',
    'upload_file',
    'list_files',
    'retrieve_file',
    'delete_file',
    'get_file_content',
    'create_vector_store',
    'list_vector_stores',
    'retrieve_vector_store',
    'update_vector_store',
    'delete_vector_store',
    'create_vector_store_file',
    'list_vector_store_files',
    'retrieve_vector_store_file',
    'delete_vector_store_file',
    'configure_logging',
    'log_error'
]

# Initialize the package (if any initialization code is needed)
logging.info("OpenAI Wrapper package initialized.")
