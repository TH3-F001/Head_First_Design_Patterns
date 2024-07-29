from pyowm import OWM
from pyowm.utils.config import get_default_config
import os

"""Implements the WeatherAPI interface using the OpenWeatherMap API """


class OpenWeatherMap:
    def __init__(self, location):
        self.tmp_key_path = '/tmp/owm.temp'
        self.location = location
        api_key = self._get_api_key()

        weather_conf = get_default_config()
        weather_conf['language'] = 'en'
        sensor = OWM(api_key, weather_conf)
        self._station = sensor.weather_manager()

    def get_measurements(self) -> dict:
        observation = self._station.weather_at_place(self.location)
        weather = observation.weather
        temp = weather.temperature('fahrenheit')['temp']
        humi = weather.humidity
        pres = weather.pressure['press']
        return {
            'temperature': temp,
            'humidity': humi,
            'pressure': pres
        }

    def _get_api_key_from_file(self, path: str) -> str:
        """ Attempt to retrieve the API key from a file. """
        try:
            with open(path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return None  # File does not exist

    def _save_api_key_to_file(self, path: str, key: str):
        """ Save the API key to a file. """
        os.makedirs(os.path.dirname(path), exist_ok=True)  # Ensure directory exists
        with open(path, 'w') as file:
            file.write(key)

    def _get_api_key(self):
        api_key = self._get_api_key_from_file(self.tmp_key_path)
        if not api_key:
            print('Input your OpenWeatherMap API key:')
            api_key = input('> ')
            self._save_api_key_to_file(self.tmp_key_path, api_key)
        if not api_key:
            return None
        return api_key
