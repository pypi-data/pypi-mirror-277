import unittest
from unittest.mock import patch, MagicMock
from pga_gpt_tools.web_scrape import WebScrape
import os
import json

class TestWebScrape(unittest.TestCase):
    def setUp(self):
        # Set up environment variables before each test
        os.environ['FIRECRAWL_API_KEY'] = 'test_firecrawl_api_key'

    def tearDown(self):
        # Clean up environment variables after each test
        del os.environ['FIRECRAWL_API_KEY']

    @patch('pga_gpt_tools.web_scrape.FirecrawlApp')
    def test_web_scrape_success(self, MockFirecrawlApp):
        # Mock the FirecrawlApp response
        mock_app_instance = MockFirecrawlApp.return_value
        mock_app_instance.scrape_url.return_value = {'content': 'This is the main content of the page'}

        # Create an instance of WebScrape with a URL
        tool = WebScrape(url="https://example.com")
        result = tool.run()

        # Expected result
        expected_result = json.dumps({'content': 'This is the main content of the page'})

        # Assertions
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_result)

    @patch('pga_gpt_tools.web_scrape.FirecrawlApp')
    def test_web_scrape_failure(self, MockFirecrawlApp):
        # Configure the mock to raise an exception
        mock_app_instance = MockFirecrawlApp.return_value
        mock_app_instance.scrape_url.side_effect = Exception("API error")

        # Create an instance of WebScrape with a URL
        tool = WebScrape(url="https://example.com")
        result = tool.run()

        # Assertions
        self.assertIsInstance(result, str)
        self.assertIn("API error", result)

if __name__ == '__main__':
    unittest.main()
