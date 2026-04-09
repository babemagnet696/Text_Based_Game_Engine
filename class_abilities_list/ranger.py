from class_abilities_list.abilities import Ability
from dice_roller import *
from Entity import Entity
from status_effects_list.bleed import Bleed
from status_effects_list.dmg_debuff import Mark

quick_shot = Ability(
    name="Quick Shot",
    dice_class=d8,
    num_of_dice=1,
    base_damage=0,
    cooldown=0,
    roll_modifier=3
)

stab = Ability(
    name="Stab",
    dice_class=d6,
    num_of_dice=1,
    base_damage=1,
    cooldown=2,
    status_effect=True,
    target_effect=Bleed()
)

double_shot = Ability(
    name="Double Shot",
    dice_class=d8,
    num_of_dice=2,
    base_damage=2,
    cooldown=3
)

mark_target = Ability(
    name="Mark Target",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=2,
    status_effect=True,
    target_effect=Mark()
)

class Ranger(Entity):
    def __init__(self, name, level):
        a_abilities = [quick_shot, stab, double_shot, mark_target]
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


