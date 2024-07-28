# When using abstract classes as interfaces, the classes that implement that interface
# are dependent on that interface
from interfaces import QuackBehaviour


class Quack(QuackBehaviour):
    def quack(self):
        return "Quack!"


class Squeak(QuackBehaviour):
    def quack(self):
        return "Squeek!"


class Silence(QuackBehaviour):
    def quack(self):
        return "..."


# Used for testing Abstract Base Class type failure. Notice the warning in your IDE
class NonCompliantQuack(QuackBehaviour):
    def moo(self):
        print("moo!")
