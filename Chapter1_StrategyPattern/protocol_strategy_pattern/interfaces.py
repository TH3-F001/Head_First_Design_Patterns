from typing import Protocol


class FlyBehaviour(Protocol):
    def fly(self):
        ...


class QuackBehaviour(Protocol):
    def quack(self):
        ...



