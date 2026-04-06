from abilities import Ability
from dice_roller import *

flurry_of_blows = Ability(
    name="Flurry of Blows",
    dice_class=d4,
    num_of_dice=3,
    base_damage=4,
    cooldown=2,
)