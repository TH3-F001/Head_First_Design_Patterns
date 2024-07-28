from Chapter1_StrategyPattern.abc_strategy_pattern.ducks import *
from Chapter1_StrategyPattern.abc_strategy_pattern.hunter import Hunter
from quacking import NonCompliantQuack

class DuckSim:
    def run(self):
        m = MallardDuck()
        r = RubberDuck()
        mo = ModelDuck()
        h = Hunter()
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

        # Equip the Model Duck with a Rocket Engine
        print("Equipping ModelDuck with Rocket Engine...")
        mo.set_fly_behaviour(rpfb)
        print(f"\tFly:", mo.do_fly())

        # Hunters can also quack
        print("A Wild Hunter Appears!")
        print("\tHunter:", h.duck_call.quack())

        # Demonstrate interface failure with protocols
        print("\nTesting Protocol Type Failure...")
        dummy_duck = DummyDuck()
        print("\tAssigning DummyDuck an non-compliant quack")
        ncq = NonCompliantQuack
        dummy_duck.set_quack_behaviour(ncq)  # <--[ Note that the IDE gives a warning here ]
        dummy_duck.do_quack()  # <--[ Notice that this isnt giving an error, nor does any other code in the chain. ]



if __name__ == "__main__":
    sim = DuckSim()
    sim.run()
