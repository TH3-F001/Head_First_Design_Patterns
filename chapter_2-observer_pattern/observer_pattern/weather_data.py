from interfaces import Observer, WeatherAPI

class WeatherData:
    def __init__(self, weather_api: WeatherAPI):
        self._observers: list[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

        self.api: WeatherAPI = weather_api


    def register_observer(self, obs: Observer):
        self._observers.append(obs)

    def remove_observer(self, obs: Observer):
        self._observers.remove(obs)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

    def retrieve_measurements(self):
        measurements = self.api.get_measurements()
        temp = measurements['temperature']
        humi = measurements['humidity']
        pres = measurements['pressure']
        self.set_measurements(temp, humi, pres)

