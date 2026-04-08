from dice_roller import *

class Ability:
    def __init__(self, name, dice_class, num_of_dice, base_damage, cooldown, can_miss=True, roll_modifier=0, status_effect=None, self_target=False):
        self.name = name
        self.dice_class = dice_class
        self.num_of_dice = num_of_dice
        self.base_damage = base_damage
        self.cooldown = cooldown
        self.can_miss = can_miss
        self.current_cd = 0
        self.roll_modifier = roll_modifier
        self.status_effect = status_effect
        self.self_target = self_target
        
    def execute(self, roll):

        if self.status_effect is not None:
            pass
        nat, val = roll
        dice = self.dice_class(1)
        damage = self.base_damage + dice.roll_dice()
        
        if nat and val == 20:
            # critical hit
            # roll and add dice again
            damage += dice.roll_dice()
        
        # self.current_cd = self.cooldown
        return damage
    
    def check_cooldown(self):
        return self.current_cd == 0
    
    def apply_status_effect(self, target):
        if not self.self_target:
            if self.status_effect.saving_throw(target):
                return
        self.status_effect.apply(target)
    
    def attack_roll(self, modifier, disadvantage=False, advantage=False, crit_modifier=0):
        die = d20(bonus=(self.roll_modifier + modifier), crit_chance_modifier=crit_modifier)

        # Returns a tuple (is_natural, roll_total)
        # If is_natural is True and a 20 a crit lands Calculated in battle_system
        # Attacks that can't miss can't crit since they don't roll
        if not self.can_miss:
            return (False, 9999)

        if advantage and not disadvantage:
            dice_roll = die.advantage()

        elif disadvantage and not advantage:
            dice_roll = die.disadvantage()

        else:
            # For when dis + adv cancel out True or are False
            dice_roll = die.roll_dice()

        return dice_roll
        