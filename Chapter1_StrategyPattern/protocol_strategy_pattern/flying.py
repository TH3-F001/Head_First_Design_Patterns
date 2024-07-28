# When using protocols as interfaces, the classes that implement that interface
# dont explicitly depend on the interface


class FlyWithWings:
    def fly(self):
        return 'Flying with wings'


class FlyCantFly:
    def fly(self):
        return '... -_-"'


class FlyWithRocket:
    def fly(self):
        return 'PSSSSSHHHHWWWWRRRRAAAAAAAARRRRRR! Look at me now momma!'
