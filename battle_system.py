from Entity import *
import os
import random as r
from class_abilities_list import Fighter, Wizard, Monk, Ranger, Warlock

def battle(player, enemy):
    start = r.randrange(0, 2) # unused right now
    print("To choose an ability type the number associated with the ability")

    while player.is_alive() and enemy.is_alive():

        p_action = player_get_ability(player)
        p_attack_roll = p_action.attack_roll(modifier=0)
        roll_check(p_attack_roll, p_action, player, enemy)

        if enemy.is_alive():
            e_action = enemy_get_ability(enemy)
            e_attack_roll = e_action.attack_roll(modifier=0)
            roll_check(e_attack_roll, p_action, enemy, player)




        


def player_get_ability(entity):
    os.system('cls' if os.name == 'nt' else 'clear')
    available = [a for a in entity.abilities if a.check_cooldown()]

    for i, ability in enumerate(entity.abilities, 1):
        print(f"{i}. {ability.title()}")

    choice = input("\nChoose an ability: ")

    if not choice.isdigit() or not (1 <= int(choice) <= len(available)):
        return player_get_ability(entity)
    return available[int(choice) - 1]

def enemy_get_ability(entity):
    available = [a for a in entity.abilities if a.check_cooldown()]
    return r.choice(available)

def roll_check(attack_roll, action, a_entity, d_entity):
    nat, roll_val = attack_roll

    if nat and roll_val == 1:
            print(f"Critical miss!")

    elif roll_val >= d_entity.armor_class():
        damage = action.execute(attack_roll)
        d_entity.take_damage(damage)
        if nat and roll_val == 20:
            print(f"CRITICAL HIT! {d_entity.name} hit for {damage} damage!")
        else:
            print(f"{d_entity.name} hit for {damage} damage!")
    else:
        print(f"{a_entity.name} missed!")
    
if __name__ == "__main__":
    fighter = Fighter("Aragorn", 1)
    enemy = Monk("Goblin", 1)
    battle(fighter, enemy)