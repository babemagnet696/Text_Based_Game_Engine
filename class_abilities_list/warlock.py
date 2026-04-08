from abilities import Ability
from dice_roller import *
from Entity import Entity

eldritch_blast = Ability(
    name="Eldritch Blast",
    dice_class=d10,
    num_of_dice=2,
    base_damage=4,
    cooldown=1,
)

class Warlock(Entity):
    def __init__(self, name, level):
        a_abilities = [eldritch_blast]
        super().__init__(
            name,
            level,
            12,
            8,
            12,
            10,
            10,
            16,
            abilities=a_abilities
        )

