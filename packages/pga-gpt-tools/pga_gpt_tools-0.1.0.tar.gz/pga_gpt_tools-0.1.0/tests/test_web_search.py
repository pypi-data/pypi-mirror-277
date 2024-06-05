import unittest
from unittest.mock import patch, MagicMock
from pga_gpt_tools.web_search import WebSearch
import os
import json

class TestWebSearch(unittest.TestCase):
    def setUp(self):
        # Set up environment variables before each test
        os.environ['SERPAPI_API_KEY'] = 'test_serpapi_api_key'

    def tearDown(self):
        # Clean up environment variables after each test
        del os.environ['SERPAPI_API_KEY']

    @patch('pga_gpt_tools.web_search.GoogleSearch')
    def test_web_search_success(self, MockGoogleSearch):
        # Mock the GoogleSearch response
        mock_search_instance = MockGoogleSearch.return_value
        mock_search_instance.get_dict.return_value = {
            'organic_results': [{'title': 'Test Result', 'link': 'https://example.com'}]
        }

        # Create an instance of WebSearch with a query
        tool = WebSearch(query="PGA Tour")
        result = tool.run()

        # Expected result
        expected_result = json.dumps({
            'organic_results': [{'title': 'Test Result', 'link': 'https://example.com'}]
        })

        # Assertions
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_result)

    @patch('pga_gpt_tools.web_search.GoogleSearch')
    def test_web_search_failure(self, MockGoogleSearch):
        # Configure the mock to raise an exception
        mock_search_instance = MockGoogleSearch.return_value
        mock_search_instance.get_dict.side_effect = Exception("API error")

        # Create an instance of WebSearch with a query
        tool = WebSearch(query="PGA Tour")
        result = tool.run()

        # Assertions
        self.assertIsInstance(result, str)
        self.assertIn("API error", result)

if __name__ == '__main__':
    unittest.main()
