import os
import random as r
from class_abilities_list import Fighter, Wizard, Monk, Ranger, Warlock
import time


def battle(player, enemy):
    os.system('cls' if os.name == 'nt' else 'clear')
    start = r.randrange(0, 2) # unused right now
    print("To choose an ability type the number associated with the ability")

    while player.is_alive() and enemy.is_alive():

        process_effects(player)
        process_effects(enemy)

        if not player.is_alive() or not enemy.is_alive():
            break

        print(f"{player.name} current health is: {player.current_hp}")
        print(f"{enemy.name} current health is: {enemy.current_hp}")

        
        decrease_cooldowns(player)
        p_action = player_get_ability(player)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{player.name} used {p_action.name}!")
        if p_action.self_target:
            p_action.apply_status_effect(player)
        else:
            roll_check(p_action, enemy)

        time.sleep(2)
        print("\n\n")

        if enemy.is_alive():
            os.system('cls' if os.name == 'nt' else 'clear')
            decrease_cooldowns(enemy)
            e_action = enemy_get_ability(enemy)
            print(f"{enemy.name} used {e_action.name}!")
            roll_check(e_action, player)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
    if player.is_alive():
        print(f"{enemy.name} has been defeated!")
        return True
    else:
        print(f"{player.name} has been defeated.\nYou are dead")
        return False

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

def roll_check(action, d_entity):
    for _ in range(action.num_of_dice):
        attack_roll = action.attack_roll(modifier=0)
        nat, roll_val = attack_roll


        if nat and roll_val == 1:
                print(f"Critical miss!")

        elif roll_val >= d_entity.armor_class():
            if action.status_effect is not None:
                action.apply_status_effect(d_entity)
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
            return
        ability.current_cd -= 1
        

def process_effects(entity):
    for effect in entity.active_effects[:]:
        effect.on_turn(entity)
        effect.on_expire(entity)

if __name__ == "__main__":
    fighter = Wizard("Tyson", 1)
    enemy = Ranger("Goblin", 1)
    battle(fighter, enemy)