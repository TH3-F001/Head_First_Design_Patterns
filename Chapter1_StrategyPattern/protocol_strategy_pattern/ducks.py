from flying import FlyWithWings, FlyCantFly, FlyWithRocket
from quacking import Quack, Squeak, Silence, NonCompliantQuack

from interfaces import FlyBehaviour, QuackBehaviour


class Duck:
    fly_behaviour: FlyBehaviour
    quack_behaviour: QuackBehaviour

    def set_fly_behaviour(self, b: FlyBehaviour):
        self.fly_behaviour = b

    def set_quack_behaviour(self, b: QuackBehaviour):
        self.quack_behaviour = b

    def display(self):
        ...

    def do_fly(self):
        return self.fly_behaviour.fly()

    def do_quack(self):
        return self.quack_behaviour.quack()

    def swim(self):
        return "We all float down here Georgy!"


class MallardDuck(Duck):
    fly_behaviour = FlyWithWings()
    quack_behaviour = Quack()

    def display(self):
        return "Look at my damn wings yo!"


class RubberDuck(Duck):
    fly_behaviour = FlyCantFly()
    quack_behaviour = Squeak()

    def display(self):
        return "Rubber Ducky, you're the one!"


class ModelDuck(Duck):
    fly_behaviour = FlyCantFly()
    quack_behaviour = Quack()

    def display(self):
        return "I sure wish I could fly..."


# Used to test Protocol type failure (Note that there are no errors for NonCompliant
# quack at they time it is assigned to the DummyDuck class
class DummyDuck(Duck):
    fly_behaviour = FlyWithWings
    quack_behaviour = NonCompliantQuack

    def display(self):
        return "I'm just a protocol dummy"

