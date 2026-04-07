from abilities import Ability
from dice_roller import *
from Entity import Entity

class Wizard(Entity):
    def __init__(self, name, level):
        abilities = [magic_missle]
        super().__init__(
            name,
            level,
            10,
            8,
            12,
            16,
            12,
            10,
            abilities
        )

magic_missle = Ability(
    name="Magic Missle",
    dice_class=d4,
    num_of_dice=3,
    base_damage=0,
    cooldown=2,
    can_miss=False
)