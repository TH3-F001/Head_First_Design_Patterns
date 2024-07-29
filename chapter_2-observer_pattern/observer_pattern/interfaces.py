from abc import abstractmethod
from typing import Protocol


class Observer(Protocol):
    @abstractmethod
    def update(self, temp:float, humidity: float, pressure: float):
        pass


class Display(Protocol):
    @abstractmethod
    def display(self):
        pass


class Subject(Protocol):
    @abstractmethod
    def register_observer(self, obs: Observer):
        ...

    @abstractmethod
    def remove_observer(self, obs: Observer):
        ...

    @abstractmethod
    def notify_observers(self):
        ...


# Extra dash of strategy pattern for our weather api

class WeatherAPI(Protocol):
    @abstractmethod
    def __init__(self, location: str):
        ...

    @abstractmethod
    def get_measurements(self) -> dict:
        ...

