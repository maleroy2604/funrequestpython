import requests
from van import Van
import json


class WeatherApp:

    def __init__(self, endpoint):
        self._endpoint = endpoint

    def api_weather_call(self):
        response = requests.get(self._endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data. Status code:", response.status_code)
            print("Response content:", response.text)

    def api_call_vans(self):
        van = Van(0, "great van", "150", "great van to road with", "/banner-van.png", "luxury")
        van_data = {
            'id': van.get_id(),
            'name': van.get_name(),
            'price': van.get_price(),
            'description': van.get_description(),
            'image_url': van.get_image_url(),
            'type': van.get_type()
        }
        json_data = json.dumps(van_data)

        response = requests.post(self._endpoint, data=json_data,  headers={'Content-Type': 'application/json'})
        if response.status_code == 200 :
            return response.json()
        else:
            return f"error status code :{response.status_code}"

