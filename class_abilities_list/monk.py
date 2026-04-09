from class_abilities_list.abilities import Ability
from dice_roller import *
from Entity import Entity
from status_effects_list.change_ac import GainAC
from status_effects_list.advantage import GainAdvantage, GainDisadvantage

flurry_of_blows = Ability(
    name="Flurry of Blows",
    dice_class=d4,
    num_of_dice=3,
    base_damage=0,
    cooldown=2,
)

agile_strike = Ability(
    name="Agile Strike",
    dice_class=d4,
    num_of_dice=1,
    base_damage=1,
    cooldown=2,
    status_effect=True,
    self_effect=GainAC()
)

focus = Ability(
    name="Focus",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=3,
    status_effect=True,
    self_effect=GainAdvantage()
)

palm_strike = Ability(
    name="Palm Strike",
    dice_class=d8,
    num_of_dice=1,
    base_damage=3,
    cooldown=2,
    status_effect=True,
    target_effect=GainDisadvantage()
)

class Monk(Entity):
    def __init__(self, name, level):
        a_abilities = [flurry_of_blows, agile_strike, palm_strike, focus]
        super().__init__(
            name,
            level,
            12,
            12,
            16,
            8,
            14,
            10,
            abilities=a_abilities
        )

