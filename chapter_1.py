from typing import Protocol
from abc import abstractmethod


#region FlyBehaviours
class FlyBehaviour(Protocol):
    @abstractmethod
    def fly(self):
        ...


class FlyWithWings(FlyBehaviour):
    def fly(self):
        return 'Flying with wings'

class FlyCantFly(FlyBehaviour):
    def fly(self):
        return '... -_-"'


class FlyWithRocket(FlyBehaviour):
    def fly(self):
        return 'PSSSSSHHHHRRRRAAAAAAAARRRRRR! Look at me now momma!'
#endregion


#region QuackBehaviours
class QuackBehaviour(Protocol):
    @abstractmethod
    def quack(self):
        ...


class Quack(QuackBehaviour):
    def quack(self):
        return "Quack!"


class Squeek(QuackBehaviour):
    def quack(self):
        return "Squeek!"


class Silence(QuackBehaviour):
    def quack(self):
        return "..."
#endregion


#region Duck Classes
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
    quack_behaviour = Squeek()

    def display(self):
        return "Rubber Ducky, you're the one!"


class ModelDuck(Duck):
    fly_behaviour = FlyCantFly()
    quack_behaviour = Quack()

    def display(self):
        return "I sure wish I could fly..."

class DuckSim:
    def run(self):
        m = MallardDuck()
        r = RubberDuck()
        mo = ModelDuck()
        print("Mallard:")
        print(f"\tSwim:", m.swim())
        print(f"\tDisplay:", m.display())
        print(f"\tFly:", m.do_fly())
        print(f"\tQuack:", m.do_quack())

        print("\nRubber:")
        print(f"\tSwim:", r.swim())
        print(f"\tDisplay:", r.display())
        print(f"\tFly:", r.do_fly())
        print(f"\tQuack:", r.do_quack())

        print("\nModel:")
        print(f"\tSwim:", mo.swim())
        print(f"\tDisplay:", mo.display())
        print(f"\tFly:", mo.do_fly())
        print(f"\tQuack:", mo.do_quack())
        rpfb = FlyWithRocket()
        print("Equipping ModelDuck with Rocket Engine...")
        mo.set_fly_behaviour(rpfb)
        print(f"\tFly:", mo.do_fly())


if __name__ == "__main__":
    sim = DuckSim()
    sim.run()
