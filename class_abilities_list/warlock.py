from class_abilities_list.abilities import Ability
from dice_roller import *
from Entity import Entity

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

class Warlock(Entity):
    def __init__(self, name, level):
        a_abilities = [eldritch_blast, life_drain]
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