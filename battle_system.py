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

        player_turn(player, enemy)
            
        time.sleep(2)

        if enemy.is_alive():
            enemy_turn(player, enemy)

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

def roll_check(action, attacker, defender):
    
    for _ in range(action.num_of_dice):

        attack_roll = action.attack_roll(modifier=0, disadvantage=attacker.disadvantage, advantage=attacker.advantage)
        nat, roll_val = attack_roll

        if nat and roll_val == 1:
                print(f"Critical miss!")

        elif roll_val >= defender.armor_class():

            if action.status_effect:
                if action.target_effect is not None:
                    action.apply_status_effect(defender)

            damage = action.execute(attack_roll)
            action.on_hit(attacker, defender, damage)
            defender.take_damage(damage)

            if nat and roll_val == 20:
                print(f"CRITICAL HIT! {defender.name} hit for {damage} damage!")
            else:
                print(f"{defender.name} hit for {damage} damage!")

        else:
            print(f"Miss!")

        if action.status_effect:
            if action.self_effect is not None:
                action.apply_status_effect(attacker)

    if action.num_of_dice == 0:
        no_dice(action, attacker, defender)
    
def decrease_cooldowns(entity):
    for ability in entity.abilities:
        if ability.current_cd == 0:
            return
        ability.current_cd -= 1      

def process_effects(entity):
    for effect in entity.active_effects[:]:
        effect.on_turn(entity)
        effect.on_expire(entity)
        entity.surge_damage()

def no_dice(action, attacker, defender):

    if action.base_damage == 0:
        if action.target_effect is not None:
            action.apply_status_effect(defender)
            return
        action.apply_status_effect(attacker)
        return

    attack_roll = action.attack_roll(modifier=0)
    nat, roll_val = attack_roll

    if nat and roll_val == 1:
            print(f"Critical miss!")

    elif roll_val >= defender.armor_class():

        if action.status_effect:
            if action.target_effect is not None:
                action.apply_status_effect(defender)

        damage = action.base_damage

        if nat and roll_val == 20:
            damage += action.base_damage
            print(f"CRITICAL HIT! {defender.name} hit for {damage} damage!")
        else:
            print(f"{defender.name} hit for {damage} damage!")
        
        action.on_hit(attacker, defender, damage)
        defender.take_damage(damage)

    else:
        print(f"Miss!")
    
    if action.status_effect:
        if action.self_effect is not None:
            action.apply_status_effect(attacker)

def player_turn(player, enemy):
    decrease_cooldowns(player)
    p_action = player_get_ability(player)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{player.name} used {p_action.name}!")
    roll_check(p_action, player, enemy)

def enemy_turn(player, enemy):
    os.system('cls' if os.name == 'nt' else 'clear')
    decrease_cooldowns(enemy)
    e_action = enemy_get_ability(enemy)
    print(f"{enemy.name} used {e_action.name}!")
    roll_check(e_action, enemy, player)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    fighter = Warlock("Tyson", 1)
    enemy = Monk("Goblin", 1)
    battle(fighter, enemy)