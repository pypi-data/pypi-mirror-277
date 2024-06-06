
import asyncio
import logging
from openaiwrapper.openai_wrapper import OpenAIWrapper

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    api_key = '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'
    profile_path = r'C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\profiles\coreteam_brie.json'

    async with OpenAIWrapper(api_key=api_key) as wrapper:
        try:
            # Load the profile from the given path
            assistant = await wrapper.create_assistant_from_profile(profile_path)
            assistant_id = assistant['id']
            initial_message = "Hello, can you help me with a task?"

            response = await wrapper.create_thread_for_existing_assistant(assistant_id, initial_message)
            print(f"Assistant response: {response}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")

# Running the async main function
if __name__ == '__main__':
    asyncio.run(main())
