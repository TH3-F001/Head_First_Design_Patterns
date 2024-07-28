# When using abstract classes as interfaces, the classes that implement that interface
# are dependent on that interface

class Quack:
    def quack(self):
        return "Quack!"


class Squeak:
    def quack(self):
        return "Squeek!"


class Silence:
    def quack(self):
        return "..."

class NonCompliantQuack:
    def moo(self):
        print("moo")