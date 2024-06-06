import unittest
from unittest.mock import patch, MagicMock, AsyncMock

class TestMainFunctions(unittest.TestCase):

    @patch('openaiwrapper.main.initialize_client')
    @patch('openaiwrapper.main.create_assistant')
    @patch('openaiwrapper.main.create_thread')
    @patch('openaiwrapper.main.add_message_to_thread')
    @patch('openaiwrapper.main.create_and_poll_run', new_callable=AsyncMock)
    @patch('openaiwrapper.main.list_thread_messages')
    @patch('openaiwrapper.main.delete_assistant')
    def test_run_math_tutor_interaction(self, mock_delete_assistant, mock_list_thread_messages, mock_create_and_poll_run, mock_add_message_to_thread, mock_create_thread, mock_create_assistant, mock_initialize_client):
        from openaiwrapper.main import run_math_tutor_interaction

        # Set up mocks
        mock_client = MagicMock()
        mock_initialize_client.return_value = mock_client
        mock_assistant = MagicMock()
        mock_create_assistant.return_value = mock_assistant
        mock_thread = MagicMock()
        mock_create_thread.return_value = mock_thread
        mock_message = MagicMock()
        mock_add_message_to_thread.return_value = mock_message
        mock_run = MagicMock()
        mock_run.status = 'completed'
        mock_create_and_poll_run.return_value = mock_run
        mock_messages = [MagicMock()]
        mock_messages[0].content[0].type = 'text'
        mock_messages[0].content[0].text.value = "Test message"
        mock_list_thread_messages.return_value = mock_messages

        # Call the function
        run_math_tutor_interaction()

        # Assertions
        mock_initialize_client.assert_called_once()
        mock_create_assistant.assert_called_once()
        mock_create_thread.assert_called_once()
        mock_add_message_to_thread.assert_called_once()
        mock_create_and_poll_run.assert_called_once()
        mock_list_thread_messages.assert_called_once()
        mock_delete_assistant.assert_called_once()

    @patch('openaiwrapper.main.initialize_client')
    @patch('openaiwrapper.main.create_assistant')
    @patch('openaiwrapper.main.create_thread')
    @patch('openaiwrapper.main.add_message_to_thread')
    @patch('openaiwrapper.main.create_and_poll_run', new_callable=AsyncMock)
    @patch('openaiwrapper.main.list_thread_messages')
    def test_send_msg_coreteam(self, mock_list_thread_messages, mock_create_and_poll_run, mock_add_message_to_thread, mock_create_thread, mock_create_assistant, mock_initialize_client):
        from openaiwrapper.main import send_msg_coreteam, load_coreteam_profile_1

        # Set up mocks
        mock_client = MagicMock()
        mock_initialize_client.return_value = mock_client
        mock_assistant = MagicMock()
        mock_create_assistant.return_value = mock_assistant
        mock_thread = MagicMock()
        mock_create_thread.return_value = mock_thread
        mock_message = MagicMock()
        mock_add_message_to_thread.return_value = mock_message
        mock_run = MagicMock()
        mock_run.status = 'completed'
        mock_create_and_poll_run.return_value = mock_run
        mock_messages = [MagicMock()]
        mock_messages[0].content[0].type = 'text'
        mock_messages[0].content[0].text.value = "Test message"
        mock_list_thread_messages.return_value = mock_messages

        # Call the function
        send_msg_coreteam(load_coreteam_profile_1)

        # Assertions
        mock_initialize_client.assert_called_once()
        mock_create_assistant.assert_called_once()
        mock_create_thread.assert_called_once()
        mock_add_message_to_thread.assert_called_once()
        mock_create_and_poll_run.assert_called_once()
        mock_list_thread_messages.assert_called_once()

    @patch('openaiwrapper.main.initialize_client')
    @patch('openaiwrapper.main.create_assistant')
    @patch('openaiwrapper.main.create_thread')
    @patch('openaiwrapper.main.add_message_to_thread')
    @patch('openaiwrapper.main.create_and_poll_run', new_callable=AsyncMock)
    @patch('openaiwrapper.main.list_thread_messages')
    @patch('openaiwrapper.main.delete_assistant')
    def test_run_interaction_with_profile(self, mock_delete_assistant, mock_list_thread_messages, mock_create_and_poll_run, mock_add_message_to_thread, mock_create_thread, mock_create_assistant, mock_initialize_client):
        from openaiwrapper.main import run_interaction_with_profile, load_coreteam_profile_1

        # Set up mocks
        mock_client = MagicMock()
        mock_initialize_client.return_value = mock_client
        mock_assistant = MagicMock()
        mock_create_assistant.return_value = mock_assistant
        mock_thread = MagicMock()
        mock_create_thread.return_value = mock_thread
        mock_message = MagicMock()
        mock_add_message_to_thread.return_value = mock_message
        mock_run = MagicMock()
        mock_run.status = 'completed'
        mock_create_and_poll_run.return_value = mock_run
        mock_messages = [MagicMock()]
        mock_messages[0].content[0].type = 'text'
        mock_messages[0].content[0].text.value = "Test message"
        mock_list_thread_messages.return_value = mock_messages

        # Call the function
        run_interaction_with_profile(load_coreteam_profile_1, "Test user message", "Test assistant instructions")

        # Assertions
        mock_initialize_client.assert_called_once()
        mock_create_assistant.assert_called_once()
        mock_create_thread.assert_called_once()
        mock_add_message_to_thread.assert_called_once()
        mock_create_and_poll_run.assert_called_once()
        mock_list_thread_messages.assert_called_once()
        mock_delete_assistant.assert_called_once()

    @patch('openaiwrapper.main.initialize_client')
    @patch('openaiwrapper.main.create_assistant')
    @patch('openaiwrapper.main.create_thread')
    @patch('openaiwrapper.main.add_message_to_thread')
    @patch('openaiwrapper.main.create_and_poll_run', new_callable=AsyncMock)
    @patch('openaiwrapper.main.list_thread_messages')
    @patch('openaiwrapper.main.delete_assistant')
    def test_send_message_and_wait_for_response(self, mock_delete_assistant, mock_list_thread_messages, mock_create_and_poll_run, mock_add_message_to_thread, mock_create_thread, mock_create_assistant, mock_initialize_client):
        from openaiwrapper.main import send_message_and_wait_for_response, load_coreteam_profile_1

        # Set up mocks
        mock_client = MagicMock()
        mock_initialize_client.return_value = mock_client
        mock_assistant = MagicMock()
        mock_create_assistant.return_value = mock_assistant
        mock_thread = MagicMock()
        mock_create_thread.return_value = mock_thread
        mock_message = MagicMock()
        mock_add_message_to_thread.return_value = mock_message
        mock_run = MagicMock()
        mock_run.status = 'completed'
        mock_create_and_poll_run.return_value = mock_run
        mock_messages = [MagicMock()]
        mock_messages[0].content[0].type = 'text'
        mock_messages[0].content[0].text.value = "Test message"
        mock_list_thread_messages.return_value = mock_messages

        # Call the function
        messages = send_message_and_wait_for_response(load_coreteam_profile_1, "Test user message", "Test assistant instructions")

        # Assertions
        mock_initialize_client.assert_called_once()
        mock_create_assistant.assert_called_once()
        mock_create_thread.assert_called_once()
        mock_add_message_to_thread.assert_called_once()
        mock_create_and_poll_run.assert_called_once()
        mock_list_thread_messages.assert_called_once()
        mock_delete_assistant.assert_called_once()
        self.assertEqual(messages, mock_messages)

    @patch('openaiwrapper.main.initialize_client')
    @patch('openaiwrapper.main.create_assistant')
    @patch('openaiwrapper.main.create_thread')
    @patch('openaiwrapper.main.add_message_to_thread')
    @patch('openaiwrapper.main.create_and_poll_run', new_callable=AsyncMock)
    @patch('openaiwrapper.main.list_thread_messages')
    @patch('openaiwrapper.main.delete_assistant')
    @patch('openaiwrapper.main.load_non_coreteam_profile')
    def test_run_interaction_with_non_coreteam_profile(self, mock_load_non_coreteam_profile, mock_delete_assistant, mock_list_thread_messages, mock_create_and_poll_run, mock_add_message_to_thread, mock_create_thread, mock_create_assistant, mock_initialize_client):
        from openaiwrapper.main import run_interaction_with_non_coreteam_profile

        # Mock profile
        mock_profile = {
            "name": "Non-Core Assistant",
            "instructions": "You are a non-core assistant.",
            "tools": [{"type": "code_interpreter"}],
            "model": "gpt-4-1106-preview"
        }
        mock_load_non_coreteam_profile.return_value = mock_profile

        # Set up other mocks
        mock_client = MagicMock()
        mock_initialize_client.return_value = mock_client
        mock_assistant = MagicMock()
        mock_create_assistant.return_value = mock_assistant
        mock_thread = MagicMock()
        mock_create_thread.return_value = mock_thread
        mock_message = MagicMock()
        mock_add_message_to_thread.return_value = mock_message
        mock_run = MagicMock()
        mock_run.status = 'completed'
        mock_create_and_poll_run.return_value = mock_run
        mock_messages = [MagicMock()]
        mock_messages[0].content[0].type = 'text'
        mock_messages[0].content[0].text.value = "Test message"
        mock_list_thread_messages.return_value = mock_messages

        # Call the function
        run_interaction_with_non_coreteam_profile("non_core_1", "Test user message", "Test assistant instructions")

        # Assertions
        mock_initialize_client.assert_called_once()
        mock_create_assistant.assert_called_once()
        mock_create_thread.assert_called_once()
        mock_add_message_to_thread.assert_called_once()
        mock_create_and_poll_run.assert_called_once()
        mock_list_thread_messages.assert_called_once()
        mock_delete_assistant.assert_called_once()

    @patch('openaiwrapper.main.initialize_client')
    @patch('openaiwrapper.main.create_assistant')
    @patch('openaiwrapper.main.create_thread')
    @patch('openaiwrapper.main.add_message_to_thread')
    @patch('openaiwrapper.main.create_and_poll_run', new_callable=AsyncMock)
    @patch('openaiwrapper.main.list_thread_messages')
    @patch('openaiwrapper.main.delete_assistant')
    def test_handle_multiple_threads(self, mock_delete_assistant, mock_list_thread_messages, mock_create_and_poll_run, mock_add_message_to_thread, mock_create_thread, mock_create_assistant, mock_initialize_client):
        from openaiwrapper.main import handle_multiple_threads, load_coreteam_profile_1, load_coreteam_profile_2

        # Set up mocks
        mock_client = MagicMock()
        mock_initialize_client.return_value = mock_client
        mock_assistants = [MagicMock(), MagicMock()]
        mock_create_assistant.side_effect = mock_assistants
        mock_thread = MagicMock()
        mock_create_thread.return_value = mock_thread
        mock_message = MagicMock()
        mock_add_message_to_thread.return_value = mock_message
        mock_run = MagicMock()
        mock_run.status = 'completed'
        mock_create_and_poll_run.return_value = mock_run
        mock_messages = [MagicMock()]
        mock_messages[0].content[0].type = 'text'
        mock_messages[0].content[0].text.value = "Test message"
        mock_list_thread_messages.return_value = mock_messages

        # Call the function
        threads = handle_multiple_threads(
            [load_coreteam_profile_1, load_coreteam_profile_2],
            ["Test user message 1", "Test user message 2"],
            ["Test assistant instructions 1", "Test assistant instructions 2"]
        )

        # Assertions
        mock_initialize_client.assert_called_once()
        self.assertEqual(mock_create_assistant.call_count, 2)
        self.assertEqual(mock_create_thread.call_count, 2)
        self.assertEqual(mock_add_message_to_thread.call_count, 2)
        self.assertEqual(mock_create_and_poll_run.call_count, 2)
        self.assertEqual(mock_list_thread_messages.call_count, 2)
        self.assertEqual(mock_delete_assistant.call_count, 2)
        self.assertEqual(len(threads), 2)


if __name__ == '__main__':
    unittest.main()
