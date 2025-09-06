import unittest
from unittest.mock import mock_open, patch
from main import *
from unittest.mock import patch, call
from freezegun import freeze_time


class TestMain(unittest.TestCase):


    @freeze_time("2013-04-09 09:05")
    @patch("main.get_input", side_effect=["", "Running this test", "GWT-001", ""])
    @patch("main.add_track")
    def test_track_expect_input_message_and_ticket_if_no_params(self, mock_add_track, mock_input):
        # Act
        track()

        # Assert
        mock_add_track.assert_has_calls([call('09/04/2013', '09:05', '09:05', 'GWT-001', 'Running this test')]
    )
        
    @freeze_time("2013-04-09 09:05")
    @patch("main.get_input")
    @patch("main.add_track")
    def test_track_expect_param_message_and_ticket(self, mock_add_track, mock_input):
        # Act
        track(message="Running this test", ticket="GWT-001")

        # Assert
        mock_add_track.assert_has_calls([call('09/04/2013', '09:05', '09:05', 'GWT-001', 'Running this test')])

    @freeze_time("2013-04-09 09:05")
    @patch("main.add_track")
    @patch("main.get_last_track", side_effect=["01/04/2014;08:00;08:30;GWT-000;Preparing this test"])
    def test_track_expect_start_is_last_end_using_past_true(self, mock_get_last_track, mock_add_track):
        # Act
        track(message="Running this test", ticket="GWT-001", past=True)
        
        # Assert
        mock_add_track.assert_has_calls([call('09/04/2013', '08:30', '09:05', 'GWT-001', 'Running this test')])



    @patch("builtins.open")
    @patch("yaml.safe_dump")
    @patch("main.config_data", {"output_directory": "C:\\previous\\output\\directory"})
    def test_config_expect_output_directory_set_to_new_directory(self, mock_dump, mock_open):
        # Act
        config(output="C:\\different\\output\\directory")

        # Assert
        mock_dump.assert_called_once_with({"output_directory": "C:\\different\\output\\directory"}, mock_open().__enter__())

    @patch("builtins.open")
    @patch("main.config_data", {"output_directory": "C:\\test\\output\\directory"})
    def test_show_opens_output_file(self, mock_open):
        # Act
        show()

        # Assert
        mock_open.assert_called_once_with("C:\\test\\output\\directory\\tracks.csv", "r")
        
    @patch("main.os.remove")
    @patch("main.config_data", {"output_directory": "C:\\test\\output\\directory"})
    def test_clear_removes_output_file(self, mock_remove):
        # Act
        clear()

        # Assert
        mock_remove.assert_called_once_with("C:\\test\\output\\directory\\tracks.csv")
    