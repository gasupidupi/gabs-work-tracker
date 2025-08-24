import unittest
from unittest.mock import mock_open, patch
from main import *
from unittest.mock import patch, call
from freezegun import freeze_time


class TestMain(unittest.TestCase):


    @freeze_time("2013-04-09 09:05")
    @patch("builtins.open")
    @patch("main.get_input", side_effect=["", "Running this test", "GWT-001", ""])
    @patch("main.config_data", {"output_directory": "C:\\test\\output\\directory"})
    def test_track_expect_input_message_and_ticket_if_no_params(self, mock_input, mock_open):
        # Act
        track()

        # Assert
        mock_open.assert_has_calls([
            call("C:\\test\\output\\directory\\tracks.csv", "a"),
            call().__enter__(),
            call().__enter__().write("09/04/2013;09:05;09:05;GWT-001;Running this test\n"),
            call().__exit__(None, None, None),
            call().__enter__().close()
            ]
    )
        
    @freeze_time("2013-04-09 09:05")
    @patch("builtins.open")
    @patch("main.get_input", side_effect=[""])
    @patch("main.config_data", {"output_directory": "C:\\test\\output\\directory"})
    def test_track_expect_param_message_and_ticket(self, mock_input, mock_open):
        # Act
        track(message="Running this test", ticket="GWT-001")

        # Assert
        mock_open.assert_has_calls([
            call("C:\\test\\output\\directory\\tracks.csv", "a"),
            call().__enter__(),
            call().__enter__().write("09/04/2013;09:05;09:05;GWT-001;Running this test\n"),
            call().__exit__(None, None, None),
            call().__enter__().close()
            ])
        
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
    