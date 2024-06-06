# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_brie.py

import os
import asyncio
from openaiwrapper.openai_wrapper import OpenAIWrapper
from openaiwrapper.config import get_config, get_environment

async def main():
    # Get the API key from the environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    # Initialize the OpenAIWrapper with the API key
    environment = get_environment()
    config = get_config(environment)
    config.API_KEY = api_key

    async with OpenAIWrapper(api_key) as client:
        # Create an assistant
        assistant = await client.assistant_manager.create_assistant(
            name="Math Tutor",
            model="gpt-4-1106-preview",
            instructions="You are a personal math tutor. Write and run code to answer math questions.",
            tools=[{"type": "code_interpreter"}]
        )
        
        print(f"Assistant created: {assistant}")

        # Create a new thread
        thread_data = {
            'assistant_id': assistant['id'],
            'tool_resources': {},  # Include tool_resources as it is required
            'metadata': {
                'title': 'Math problem solving session'
            },
            'messages': [
                {
                    'role': 'user',
                    'content': 'I need to solve the equation `3x + 11 = 14`. Can you help me?'
                }
            ]
        }
        
        print(f"Thread data: {thread_data}")

        try:
            thread = await client.thread_manager.create_thread(
                assistant_id=thread_data['assistant_id'],
                tool_resources=thread_data['tool_resources'],
                metadata=thread_data['metadata'],
                messages=thread_data['messages']
            )
        except Exception as e:
            print(f"Error creating thread: {e}")
            return

        print(f"Thread created: {thread}")

        # Create and poll a run for the assistant
        run = await client.run_manager.create_and_poll(
            thread_id=thread['id'],
            assistant_id=assistant['id'],
            instructions="Please address the user as Jane Doe. The user has a premium account."
        )

        print("Run completed with status: " + run['status'])

        if run['status'] == "completed":
            # List messages in the thread
            messages = await client.message_manager.list_messages(thread_id=thread['id'])

            print("Messages: ")
            for message in messages['data']:
                if message['content'][0]['type'] == "text":
                    print({"role": message['role'], "message": message['content'][0]['text']['value']})

            # Delete the assistant
            await client.assistant_manager.delete_assistant(assistant['id'])

if __name__ == "__main__":
    asyncio.run(main())
