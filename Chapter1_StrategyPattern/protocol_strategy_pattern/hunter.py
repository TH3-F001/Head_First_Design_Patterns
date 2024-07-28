from enum import Enum
from quacking import Quack

class Seasons(Enum):
    WABBIT = 1
    DUCK = 2


class Hunter:
    season = Seasons.DUCK
    duck_call = Quack()
    shotgun_gauge: int

    def call_ducks(self):
        self.duck_call.quack()
