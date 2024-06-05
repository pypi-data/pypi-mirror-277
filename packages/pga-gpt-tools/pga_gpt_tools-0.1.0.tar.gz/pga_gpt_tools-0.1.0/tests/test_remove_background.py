import unittest
from unittest.mock import patch, MagicMock
from pga_gpt_tools.remove_background import RemoveBackground
import os
import json

class TestRemoveBackground(unittest.TestCase):
    def setUp(self):
        # Set up environment variables before each test
        os.environ['FALAI_API_KEY'] = 'test_falai_api_key'

    def tearDown(self):
        # Clean up environment variables after each test
        del os.environ['FALAI_API_KEY']

    @patch('pga_gpt_tools.remove_background.fal_client.submit')
    def test_remove_background_success(self, mock_submit):
        # Mock the fal_client response
        mock_handler = MagicMock()
        mock_handler.get.return_value = {
            "image": "https://example.com/processed_image.png"
        }
        mock_submit.return_value = mock_handler

        # Create an instance of RemoveBackground with an image URL
        tool = RemoveBackground(image_url="https://example.com/original_image.jpg")
        result = tool.run()

        # Expected result
        expected_result = json.dumps("https://example.com/processed_image.png")

        # Assertions
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_result)

    @patch('pga_gpt_tools.remove_background.fal_client.submit', side_effect=Exception("API error"))
    def test_remove_background_failure(self, _):
        # Create an instance of RemoveBackground with an image URL
        tool = RemoveBackground(image_url="https://example.com/error_image.jpg")
        result = tool.run()

        # Assertions
        self.assertIsInstance(result, str)
        self.assertIn("API error", result)

if __name__ == '__main__':
    unittest.main()
