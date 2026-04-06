from abilities import Ability
from dice_roller import *

heavy_strike = Ability(
    name="Heavy Strike",
    dice_class=d12,
    num_of_dice=1,
    base_damage=6,
    cooldown=2,
    roll_modifier=-3
)