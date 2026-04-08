from Entity import *
import os
import random as r
from class_abilities_list import Fighter, Wizard, Monk, Ranger, Warlock
import time

def battle(player, enemy):
    os.system('cls' if os.name == 'nt' else 'clear')
    start = r.randrange(0, 2) # unused right now
    print("To choose an ability type the number associated with the ability")

    while player.is_alive() and enemy.is_alive():

        print(f"\n{player.name} current health is: {player.current_hp}")
        print(f"{enemy.name} current health is: {enemy.current_hp}")

        decrease_cooldowns(player)
        p_action = player_get_ability(player)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{player.name} used {p_action.name}!")
        roll_check(p_action, player, enemy)

        time.sleep(2)
        print("\n\n")

        if enemy.is_alive():
            decrease_cooldowns(enemy)
            e_action = enemy_get_ability(enemy)
            print(f"{enemy.name} used {e_action.name}!")
            roll_check(e_action, enemy, player)


def player_get_ability(entity):
    
    available = [a for a in entity.abilities if a.check_cooldown()]

    for i, ability in enumerate(entity.abilities, 1):
        print(f"{i}. {ability.name.title()}")

    choice = input("\nChoose an ability: ")

    if not choice.isdigit() or not (1 <= int(choice) <= len(available)):
        return player_get_ability(entity)
    
    return available[int(choice) - 1]

def enemy_get_ability(entity):
    available = [a for a in entity.abilities if a.check_cooldown()]
    return r.choice(available)

def roll_check(action, a_entity, d_entity):
    for _ in range(action.num_of_dice):
        attack_roll = action.attack_roll(modifier=0)
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
            print(f"Miss!")
    
def decrease_cooldowns(entity):
    for ability in entity.abilities:
        if ability.current_cd == 0:
            continue
        ability.current_cd -= 1

if __name__ == "__main__":
    fighter = Wizard("Tyson", 1)
    enemy = Ranger("Goblin", 1)
    battle(fighter, enemy)