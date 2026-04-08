from abilities import Ability
from dice_roller import *
from Entity import Entity

quick_shot = Ability(
    name="Quick Shot",
    dice_class=d8,
    num_of_dice=1,
    base_damage=0,
    cooldown=0,
    roll_modifier=3
)

class Ranger(Entity):
    def __init__(self, name, level):
        a_abilities = [quick_shot]
        super().__init__(
            name,
            level,
            12,
            10,
            16,
            10,
            13,
            9,
            abilities=a_abilities
        )


