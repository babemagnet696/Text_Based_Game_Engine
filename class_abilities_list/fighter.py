from class_abilities_list.abilities import Ability
from dice_roller import *
from Entity import Entity

heavy_strike = Ability(
    name="Heavy Strike",
    dice_class=d12,
    num_of_dice=1,
    base_damage=6,
    cooldown=2,
    roll_modifier=-3
)

class Fighter(Entity):
    def __init__(self, name, level):
        a_abilities = [heavy_strike]
        super().__init__(
            name,
            level,
            14,
            16,
            12,
            8,
            10,
            10,
            abilities=a_abilities
        )

