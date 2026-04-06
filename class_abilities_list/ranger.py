from abilities import Ability
from dice_roller import *

quick_shot = Ability(
    name="Quick Shot",
    dice_class=d8,
    num_of_dice=1,
    base_damage=0,
    cooldown=0,
    roll_modifier=3
)