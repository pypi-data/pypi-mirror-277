import unittest
from unittest.mock import patch, MagicMock
from pga_gpt_tools.generate_image import GenerateImage
import os
import json

class TestGenerateImage(unittest.TestCase):
    def setUp(self):
        # Set up environment variables before each test
        os.environ['OPENAI_API_KEY'] = 'test_openai_api_key'

    def tearDown(self):
        # Clean up environment variables after each test
        del os.environ['OPENAI_API_KEY']

    @patch('pga_gpt_tools.generate_image.OpenAI')
    def test_generate_image_success(self, MockOpenAI):
        # Mock the OpenAI response
        mock_response = MagicMock()
        mock_image_data = MagicMock()
        mock_image_data.url = "https://example.com/generated_image.png"
        mock_image_data.revised_prompt = "A scenic view of mountains during sunset"
        mock_response.data = [mock_image_data]

        # Configure the mock to return a response with an image URL and revised prompt
        MockOpenAI.return_value.images.generate.return_value = mock_response

        # Configure the mock to return a response with an image URL and revised prompt
        MockOpenAI.return_value.images.generate.return_value = mock_response

        # Create an instance of GenerateImage with a prompt
        tool = GenerateImage(prompt="A scenic view of mountains during sunset")
        result = tool.run()

        # Expected result
        expected_result = json.dumps({
            "image_url": "https://example.com/generated_image.png",
            "prompt": "A scenic view of mountains during sunset"
        })

        # Assertions
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_result)

    @patch('pga_gpt_tools.generate_image.OpenAI')
    def test_generate_image_failure(self, MockOpenAI):
        # Configure the mock to raise an exception
        MockOpenAI.return_value.images.generate.side_effect = Exception("API error")

        # Create an instance of GenerateImage with a prompt
        tool = GenerateImage(prompt="An error-prone prompt")
        result = tool.run()

        # Assertions
        self.assertIsInstance(result, str)
        self.assertIn("API error", result)

if __name__ == '__main__':
    unittest.main()
