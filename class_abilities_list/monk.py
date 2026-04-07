from abilities import Ability
from dice_roller import *
from Entity import Entity

class Monk(Entity):
    def __init__(self, name, level):
        abilities = [flurry_of_blows]
        super().__init__(
            name,
            level,
            12,
            12,
            16,
            8,
            14,
            10,
            abilities
        )

flurry_of_blows = Ability(
    name="Flurry of Blows",
    dice_class=d4,
    num_of_dice=3,
    base_damage=4,
    cooldown=2,
)