from class_abilities_list.abilities import Ability
from dice_roller import *
from Entity import Entity
from status_effects_list.burn import Burn
from status_effects_list.advantage import GainAdvantage
from status_effects_list.change_ac import LoseAC

firebolt = Ability(
    name="Firebolt",
    dice_class=d8,
    num_of_dice=1,
    base_damage=2,
    cooldown=0
)

fireball = Ability(
    name="Fireball",
    dice_class=d12,
    num_of_dice=1,
    base_damage=4,
    cooldown=3,
    roll_modifier=-3,
    status_effect=True,
    target_effect=Burn()
)

magic_missle = Ability(
    name="Magic Missle",
    dice_class=d4,
    num_of_dice=3,
    base_damage=0,
    cooldown=2,
    can_miss=False
)

focus = Ability(
    name="focus",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=2,
    status_effect=True,
    self_effect=GainAdvantage()
)

curse = Ability(
    name="curse",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=3,
    status_effect=True,
    target_effect=LoseAC()
)

class Wizard(Entity):
    def __init__(self, name, level):
        a_abilities = [firebolt, fireball, magic_missle, focus, curse]
        super().__init__(
            name,
            level,
            10,
            8,
            12,
            16,
            12,
            10,
            abilities=a_abilities
        )

