import sys
sys.path.append('./')
import unittest
from unittest.mock import patch, MagicMock
from pga_gpt_tools.get_okta_user import GetOktaUser
import os
import json

class TestGetOktaUser(unittest.TestCase):
    def setUp(self):
        os.environ['OKTA_USER_GROUP_READ_API_TOKEN'] = 'test_okta_api_token'

    def tearDown(self):
        del os.environ['OKTA_USER_GROUP_READ_API_TOKEN']

    @patch('pga_gpt_tools.get_okta_user.requests.get')
    def test_get_okta_user_success(self, mock_get):
        profile_data = {'city': 'Springfield', 'costCenter': '123', 'department': 'Sales', 'displayName': 'John Doe', 'email': 'jdoe@example.com', 'firstName': 'John', 'lastName': 'Doe', 'manager': 'Jane Smith', 'mobilePhone': '123-456-7890', 'organization': 'PGA', 'profileUrl': 'https://example.com/profile', 'secondEmail': 'jdoe2@example.com', 'state': 'IL', 'streetAddress': '123 Elm St', 'title': 'Sales Manager', 'userType': 'Employee', 'zipCode': '62704'}
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = [{'profile': profile_data}]
        mock_get.return_value = mock_response
        tool = GetOktaUser(email="jdoe@example.com")
        result = tool.run()
        expected_result = json.dumps(profile_data)

        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_result)

    @patch('pga_gpt_tools.get_okta_user.requests.get')
    def test_get_okta_user_filter_correctly(self, mock_get):
        profile_data = {'city': 'Springfield', 'costCenter': '123', 'department': 'Sales', 'displayName': 'John Doe', 'email': 'jdoe@example.com', 'firstName': 'John', 'lastName': 'Doe', 'manager': 'Jane Smith', 'mobilePhone': '123-456-7890', 'organization': 'PGA', 'profileUrl': 'https://example.com/profile', 'secondEmail': 'jdoe2@example.com', 'state': 'IL', 'streetAddress': '123 Elm St', 'title': 'Sales Manager', 'userType': 'Employee', 'zipCode': '62704'}
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = [{'profile': profile_data, 'ExtraneousField': 'blah blah blah'}]
        mock_get.return_value = mock_response
        tool = GetOktaUser(email="jdoe@example.com")
        result = tool.run()
        expected_result = json.dumps(profile_data)

        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_result)

    @patch('pga_gpt_tools.get_okta_user.requests.get')
    def test_get_okta_user_failure(self, mock_get):
        mock_get.side_effect = Exception("API error")
        tool = GetOktaUser(email="jdoe@example.com")
        result = tool.run()

        self.assertIsInstance(result, str)
        self.assertIn("API error", result)

if __name__ == '__main__':
    unittest.main()
