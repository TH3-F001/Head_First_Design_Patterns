# When using protocols as interfaces, the classes that implement that interface
# dont explicitly depend on the interface
from interfaces import FlyBehaviour


class FlyWithWings(FlyBehaviour):
    def fly(self):
        return 'Flying with wings'


class FlyCantFly(FlyBehaviour):
    def fly(self):
        return '... -_-"'


class FlyWithRocket(FlyBehaviour):
    def fly(self):
        return 'PSSSSSHHHHWWWWRRRRAAAAAAAARRRRRR! Look at me now momma!'
