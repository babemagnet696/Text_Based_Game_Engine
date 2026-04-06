from abilities import Ability
from dice_roller import *

magic_missle = Ability(
    name="Magic Missle",
    dice_class=d4,
    num_of_dice=3,
    base_damage=0,
    cooldown=2,
    can_miss=False
)