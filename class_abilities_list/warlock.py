from abilities import Ability
from dice_roller import *

eldritch_blast = Ability(
    name="Eldritch Blast",
    dice_class=d10,
    num_of_dice=2,
    base_damage=4,
    cooldown=1,
)