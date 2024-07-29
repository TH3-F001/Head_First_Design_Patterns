from weather_data import WeatherData
from open_weather_map import OpenWeatherMap
from cli_current_display import CurrentDisplayCLI

if __name__ == '__main__':
    location = 'Portland, US'
    api = OpenWeatherMap(location)
    weather_data = WeatherData(api)
    display = CurrentDisplayCLI(weather_data)

    weather_data.retrieve_measurements()

