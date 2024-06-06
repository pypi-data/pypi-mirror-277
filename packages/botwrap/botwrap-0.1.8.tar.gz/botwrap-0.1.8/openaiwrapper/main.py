# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\main.py

import logging
from typing import List
import asyncio
from openaiwrapper.api_client import initialize_client
from openaiwrapper.assistants import create_assistant, delete_assistant
from openaiwrapper.threads import create_thread, add_message_to_thread, list_thread_messages
from openaiwrapper.runs import create_and_poll_run
from openaiwrapper.profiles import (
    load_coreteam_profile_1,
    load_coreteam_profile_2,
    load_coreteam_profile_3,
    load_coreteam_profile_4,
    load_coreteam_profile_5,
    load_coreteam_profile_6,
    load_non_coreteam_profile
)
from openaiwrapper.error_logging import configure_logging, log_error

# Configure logging
configure_logging()

def run_math_tutor_interaction():
    """Main function to run the math tutor interaction."""
    try:
        client = initialize_client()

        profile = load_coreteam_profile_1()  # Example: using the first core team profile
        
        assistant = create_assistant(
            client,
            name=profile["name"],
            instructions=profile["instructions"],
            tools=profile["tools"],
            model=profile["model"],
        )
        
        thread = create_thread(client)
        
        add_message_to_thread(
            client,
            thread_id=thread.id,
            role="user",
            content="I need to solve the equation `3x + 11 = 14`. Can you help me?",
        )
        
        run = asyncio.run(create_and_poll_run(
            client,
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions="Please address the user as Jane Doe. The user has a premium account.",
        ))
        
        logging.info(f"Run completed with status: {run.status}")
        
        if run.status == "completed":
            messages = list_thread_messages(client, thread.id)
            logging.info("Messages:")
            for message in messages:
                assert message.content[0].type == "text"
                logging.info({"role": message.role, "message": message.content[0].text.value})
        
        delete_assistant(client, assistant.id)
    except Exception as e:
        log_error(e)
        raise

def send_msg_coreteam(profile_loader):
    """Main function to send a message to a core team assistant and capture the response."""
    try:
        client = initialize_client()

        profile = profile_loader()
        
        assistant = create_assistant(
            client,
            name=profile["name"],
            instructions=profile["instructions"],
            tools=profile["tools"],
            model=profile["model"],
        )
        
        thread = create_thread(client)
        
        add_message_to_thread(
            client,
            thread_id=thread.id,
            role="user",
            content="Hello, core team assistant! Can you help me with this task?",
        )
        
        run = asyncio.run(create_and_poll_run(
            client,
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions="Please address the user as Core Team. The user has a premium account.",
        ))
        
        logging.info(f"Run completed with status: {run.status}")
        
        messages = list_thread_messages(client, thread.id)
        logging.info("Messages:")
        for message in messages:
            assert message.content[0].type == "text"
            logging.info({"role": message.role, "message": message.content[0].text.value})
            print({"role": message.role, "message": message.content[0].text.value})
        
        # Leave the assistant and thread open for future interactions
        logging.info(f"Assistant ID: {assistant.id}, Thread ID: {thread.id}")
        print(f"Assistant ID: {assistant.id}, Thread ID: {thread.id}")
    except Exception as e:
        log_error(e)
        raise

def run_interaction_with_profile(profile_loader, user_message: str, assistant_instructions: str):
    """Run an interaction with a specific profile."""
    try:
        client = initialize_client()

        profile = profile_loader()
        
        assistant = create_assistant(
            client,
            name=profile["name"],
            instructions=profile["instructions"],
            tools=profile["tools"],
            model=profile["model"],
        )
        
        thread = create_thread(client)
        
        add_message_to_thread(
            client,
            thread_id=thread.id,
            role="user",
            content=user_message,
        )
        
        run = asyncio.run(create_and_poll_run(
            client,
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions=assistant_instructions,
        ))
        
        logging.info(f"Run completed with status: {run.status}")
        
        if run.status == "completed":
            messages = list_thread_messages(client, thread.id)
            logging.info("Messages:")
            for message in messages:
                assert message.content[0].type == "text"
                logging.info({"role": message.role, "message": message.content[0].text.value})
        
        delete_assistant(client, assistant.id)
    except Exception as e:
        log_error(e)
        raise

def send_message_and_wait_for_response(profile_loader, user_message: str, assistant_instructions: str):
    """Send a message to an assistant and wait for a response."""
    try:
        client = initialize_client()

        profile = profile_loader()
        
        assistant = create_assistant(
            client,
            name=profile["name"],
            instructions=profile["instructions"],
            tools=profile["tools"],
            model=profile["model"],
        )
        
        thread = create_thread(client)
        
        add_message_to_thread(
            client,
            thread_id=thread.id,
            role="user",
            content=user_message,
        )
        
        run = asyncio.run(create_and_poll_run(
            client,
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions=assistant_instructions,
        ))
        
        logging.info(f"Run completed with status: {run.status}")
        
        if run.status == "completed":
            messages = list_thread_messages(client, thread.id)
            logging.info("Messages:")
            for message in messages:
                assert message.content[0].type == "text"
                logging.info({"role": message.role, "message": message.content[0].text.value})
            return messages
        
        delete_assistant(client, assistant.id)
    except Exception as e:
        log_error(e)
        raise

def handle_multiple_threads(profile_loaders: List[callable], user_messages: List[str], assistant_instructions: List[str]):
    """Handle interactions with multiple threads."""
    try:
        client = initialize_client()

        assistants = []
        threads = []
        
        for profile_loader in profile_loaders:
            profile = profile_loader()
            assistant = create_assistant(
                client,
                name=profile["name"],
                instructions=profile["instructions"],
                tools=profile["tools"],
                model=profile["model"],
            )
            assistants.append(assistant)
        
        for assistant, user_message, instructions in zip(assistants, user_messages, assistant_instructions):
            thread = create_thread(client)
            add_message_to_thread(
                client,
                thread_id=thread.id,
                role="user",
                content=user_message,
            )
            
            run = asyncio.run(create_and_poll_run(
                client,
                thread_id=thread.id,
                assistant_id=assistant.id,
                instructions=instructions,
            ))
            
            logging.info(f"Run completed with status: {run.status}")
            
            if run.status == "completed":
                messages = list_thread_messages(client, thread.id)
                logging.info("Messages:")
                for message in messages:
                    assert message.content[0].type == "text"
                    logging.info({"role": message.role, "message": message.content[0].text.value})
            
            threads.append(thread)
        
        for assistant in assistants:
            delete_assistant(client, assistant.id)
        
        return threads
    except Exception as e:
        log_error(e)
        raise

def run_interaction_with_non_coreteam_profile(profile_id: str, user_message: str, assistant_instructions: str):
    """Run an interaction with a non-core team profile."""
    try:
        client = initialize_client()

        profile = load_non_coreteam_profile(profile_id)
        
        assistant = create_assistant(
            client,
            name=profile["name"],
            instructions=profile["instructions"],
            tools=profile["tools"],
            model=profile["model"],
        )
        
        thread = create_thread(client)
        
        add_message_to_thread(
            client,
            thread_id=thread.id,
            role="user",
            content=user_message,
        )
        
        run = asyncio.run(create_and_poll_run(
            client,
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions=assistant_instructions,
        ))
        
        logging.info(f"Run completed with status: {run.status}")
        
        if run.status == "completed":
            messages = list_thread_messages(client, thread.id)
            logging.info("Messages:")
            for message in messages:
                assert message.content[0].type == "text"
                logging.info({"role": message.role, "message": message.content[0].text.value})
        
        delete_assistant(client, assistant.id)
    except Exception as e:
        log_error(e)
        raise

# Example usage
if __name__ == "__main__":
    run_math_tutor_interaction()
    send_msg_coreteam(load_coreteam_profile_2)
    run_interaction_with_profile(load_coreteam_profile_3, "Can you help me with market analysis?", "Please address the user as Market Analyst.")
    run_interaction_with_non_coreteam_profile("non_core_1", "What is the status of the project?", "Please address the user as Project Manager.")
    handle_multiple_threads([load_coreteam_profile_4, load_coreteam_profile_5], ["Hello, I need your assistance.", "Can you provide an update?"], ["Address the user as Assistant 1.", "Address the user as Assistant 2."])
