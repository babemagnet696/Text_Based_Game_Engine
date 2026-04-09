from .abilities import Ability
from .entity import Entity
from effects import Hex
from effects import DarkSurge
from dice_roller import *

class LifeDrainAbility(Ability):
    def on_hit(self, attacker, defender, damage):
        attacker.heal(damage)

eldritch_blast = Ability(
    name="Eldritch Blast",
    dice_class=d6,
    num_of_dice=2,
    base_damage=2,
    cooldown=1,
)

life_drain = LifeDrainAbility(
    name="Life Drain",
    dice_class=d6,
    num_of_dice=1,
    base_damage=2,
    cooldown=4
)

hex = Ability(
    name="Hex",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=2,
    status_effect=True,
    target_effect=Hex()
)

dark_surge = Ability(
    name="Dark Surge",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=3,
    status_effect=True,
    self_effect=DarkSurge()
)

class Warlock(Entity):
    def __init__(self, name, level):
        a_abilities = [eldritch_blast, life_drain, hex, dark_surge]
        super().__init__(
            name,
            level,
            12,
            8,
            12,
            10,
            10,
            16,
            abilities=a_abilities
        )

    def on_hit(self, attacker, defender, damage):
        attacker.heal(damage)