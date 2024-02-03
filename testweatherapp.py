import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock
from weatherapp import WeatherApp
from requests.models import Response


class MyTestCase(TestCase):

    @patch('weatherapp.requests.get')
    def test_api_weather_call_success(self, mock_requests_get):
        # Mock the response for a successful API call
        mock_response = mock_requests_get.return_value
        mock_response.status_code = 200
        mock_response.json = lambda: {'your': 'mocked_data'}

        # Call the function
        weather_app = WeatherApp('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41')
        result = weather_app.api_weather_call()

        # Assertions
        self.assertEqual(result, {'your': 'mocked_data'})

        # Assert that requests.get was called with the correct URL
        expected_url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41'
        mock_requests_get.assert_called_once_with(expected_url)

    @patch('weatherapp.requests.post')
    def test_api_call_vans(self, mock_requests_post):
        mock_response = mock_requests_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'your': 'mocked_data'}

        weather_app = WeatherApp("http://localhost:8080/addvans")
        result = weather_app.api_call_vans()

        self.assertEqual(result, {'your': 'mocked_data'})


if __name__ == '__main__':
    unittest.main()
