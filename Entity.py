import math
from dice_roller import d20

class Entity:
    def __init__(self, name, level, constitution, strength, dexterity, intelligence, wisdom, charisma, weapon=None, advantage=False, disadvantage=False):
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
        self.advantage = advantage
        self.disadvantage = disadvantage

    def is_alive(self):
        return self.current_hp > 0
    
    def get_modifier(self, skill):
        return (skill - 10) // 2
    
    def take_damage(self, damage):
        self.current_hp -= damage
        print(f"{self.name} took {damage} damage!")
        if self.current_hp < 0:
            self.current_hp = 0
        return self.is_alive()
    
    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        print(f"{self.name} healed for {amount}: current hp is {self.current_hp}")
    
    # Armor and skill dependent
    def armor_class(self, armor_modifier=0):
        ac = 10 + self.get_modifier(self.dex) + armor_modifier + self.temp_ac_bonus
        self.temp_ac_bonus = 0
        return ac

    def unarmed_attack(self, enemy):
        damage = 1 + self.get_modifier(self.str)
        enemy.take_damage(damage)
    
    def unarmed_roll(self):
        attack_roll = d20(bonus=self.get_modifier(self.dex)).roll_dice
        return attack_roll
    
class Fighter(Entity):
    def __init__(self, name, level):
        super().__init__(
            name,
            level,
            14,
            16,
            12,
            8,
            10,
            10
        )

    def guard(self):
        self.temp_ac_bonus = self.get_modifier(self.str)

    def charge(self, enemy):
        enemy.take_damae(5)
        self.advantage = True


class Wizard(Entity):
    def __init__(self, name, level):
        super().__init__(
            name,
            level,
            10,
            8,
            12,
            16,
            12,
            10
        )

class Monk(Entity):
    def __init__(self, name, level):
        super().__init__(
            name,
            level,
            12,
            12,
            16,
            8,
            14,
            10
        )

    def unarmed_attack(self, roll, enemy):
        damage = roll + self.get_modifier(self.dex)
        enemy.take_damage(damage)

class Ranger(Entity):
    def __init__(self, name, level):
        super().__init__(
            name,
            level,
            12,
            10,
            16,
            10,
            13,
            9
        )

class Warlock(Entity):
    def __init__(self, name, level):
        super().__init__(
            name,
            level,
            12,
            8,
            12,
            10,
            10,
            16
        )