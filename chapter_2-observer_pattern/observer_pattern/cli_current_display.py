from weather_data import WeatherData
from open_weather_map import OpenWeatherMap


class CurrentDisplayCLI:
    def __init__(self, weather_data: WeatherData):
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0
        self.weather_station: WeatherData = weather_data
        self.weather_station.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        print(f'Temperature: {self._temperature}°F')
        print(f'Humidity: {self._humidity:.0f}%')
        print(f'Pressure: {self._pressure:.1f} hPa')
