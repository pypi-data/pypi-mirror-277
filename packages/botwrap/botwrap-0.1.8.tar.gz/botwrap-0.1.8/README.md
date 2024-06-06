from openaiwrapper import (
    initialize_client,
    create_assistant,
    delete_assistant,
    create_thread,
    add_message_to_thread,
    list_thread_messages,
    create_and_poll_run,
    load_coreteam_profile_1,
    load_coreteam_profile_2,
    load_coreteam_profile_3,
    load_coreteam_profile_4,
    load_coreteam_profile_5,
    load_coreteam_profile_6,
    load_non_coreteam_profile
)

# Example usage
client = initialize_client()
profile = load_coreteam_profile_1()
assistant = create_assistant(client, profile["name"], profile["instructions"], profile["tools"], profile["model"])
thread = create_thread(client)
add_message_to_thread(client, thread.id, "user", "Hello, can you help me with this task?")
run = create_and_poll_run(client, thread.id, assistant.id, "Please assist with the task.")
messages = list_thread_messages(client, thread.id)
for message in messages:
    print(f"{message.role}: {message.content[0].text.value}")

