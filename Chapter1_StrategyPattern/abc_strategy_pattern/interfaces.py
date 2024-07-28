from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass


class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass



