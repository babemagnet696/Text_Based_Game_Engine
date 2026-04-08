from class_abilities_list.abilities import Ability
from status_effects_list.advantage import GainAdvantage, GainDisadvantage
from status_effects_list.change_ac import GainAC
from dice_roller import *
from Entity import Entity

charge = Ability(
    name="Charge",
    dice_class=None,
    num_of_dice=0,
    base_damage=5,
    cooldown=2,
    status_effect=True,
    self_effect=GainAdvantage()
)

strike = Ability(
    name="Strike",
    dice_class=d12,
    num_of_dice=1,
    base_damage=1,
    cooldown=0
)

heavy_strike = Ability(
    name="Heavy Strike",
    dice_class=d12,
    num_of_dice=1,
    base_damage=6,
    cooldown=2,
    roll_modifier=-3
)

battle_cry = Ability(
    name="Battle Cry",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=3,
    status_effect=True,
    target_effect=GainDisadvantage()
)

guard = Ability(
    name="Guard",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=5,
    status_effect=True,
    self_effect=GainAC()
)

class Fighter(Entity):
    def __init__(self, name, level):
        a_abilities = [strike, heavy_strike, charge, battle_cry, guard]
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

