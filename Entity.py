import math
from class_abilities_list.abilities import Ability
import random as r

class Entity:
    def __init__(self, name, level, constitution, strength, 
                 dexterity, intelligence, wisdom, charisma, 
                 weapon=None, advantage=False, disadvantage=False, 
                 abilities=None):
        
        self.name = name
        self.level = level
        base_health = 20

        # all skills are on a scale of 1-20
        # Affects: Total health, resistance to poison, spell concentration
        self.con = constitution
        # Affects damage with physical melee attacks
        self.str = strength
        # Affects damage with ranged attacks and reflexes
        self.dex = dexterity
        # Affects intelligence based attacks and knowledge based checks
        self.int = intelligence
        # Affects perception and certain wisdom based attacks
        self.wis = wisdom
        # Affects charisma based attacks and social checks
        self.cha = charisma

        self.max_hp = base_health + (self.con * 3) + (self.level * 4)
        self.current_hp = self.max_hp
        self.temp_ac_bonus = 0
        self.temp_dmg_debuff = 0
        self.advantage = advantage
        self.disadvantage = disadvantage
        self.abilities = abilities or []
        self.armor_modifier = 0
        self.active_effects = []

    def is_alive(self):
        if self.current_hp > 0:
            return True
        return False
    
    def get_modifier(self, skill):
        return (skill - 10) // 2
    
    def take_damage(self, damage):
        new_damage = self.dmg_debuff_calc(damage)
        self.current_hp -= new_damage
        if self.is_alive() is False:
            self.current_hp = 0
    
    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        print(f"{self.name} healed for {amount}!")
    
    # Armor and skill dependent
    def armor_class(self):
        ac = 10 + self.get_modifier(self.dex) + self.armor_modifier + self.temp_ac_bonus
        self.temp_ac_bonus = 0
        return ac
    
    

    def dmg_debuff_calc(self, damage):
        if self.temp_dmg_debuff == 0:
            return damage
        extra_dmg_taken = r.randrange(1, self.temp_dmg_debuff+1)
        new_damage = damage + extra_dmg_taken
        print(f"{self.name} took an extra {extra_dmg_taken} damage!")
        return new_damage