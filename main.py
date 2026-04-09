import os
import time
import copy
from parsing import get_action
from player import get_class, inspect_room, inspect_inventory, use_item, take_item
from move import move, end_check, look_direction, help
from items import items
from rooms import rooms


max_inventory_size = 10

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    runtime_rooms = copy.deepcopy(rooms)
    game_over = False
    current_room = "cell"
    player = get_class()
    player_inventory = player.inventory
    time.sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Welcome to the dungeon {player.name} the {player.__class__.__name__}")
    print(f"You wake up in a dark room. It is cold and damp.")
    print(f"There is one way you can go: North out of your cell")
    print(f"\nType help if you are stuck")
    
    while True:
        command, args = get_action()
        if command == "quit":
            break
        elif command == "help":
            print(help)
            continue

        if "cancel" in args:
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
       
        
        if command in ["go", "move"]:
            direction = args[0]
            current_room = move(runtime_rooms, current_room, direction)
            game_over = end_check(runtime_rooms, current_room)
            

        elif command == "look":
            direction = args[0]
            look_direction(runtime_rooms, current_room, direction)

        elif command == "inspect":
            if args[0] == "room":
                inspect_room(runtime_rooms[current_room]["items"])
            elif args[0] == "inventory":
                if args[1] == "":
                    inspect_inventory(player_inventory)
                else:
                    inspect_inventory(player_inventory, items, args[1])
            else:
                inspect_inventory(player_inventory, items, " ".join(args))
        
        elif command == "use":
            item_to_use = args[0]
            direction = args[1]
            if args[0] in player_inventory:
                use_item(runtime_rooms, item_to_use, direction, current_room)
            else:
                print(f"{item_to_use} not found in inventory")
        
        elif command == "take":
            take_item(runtime_rooms, current_room, player_inventory, args[0])
            
        
        if game_over is True:
            break
        


if __name__ == "__main__":
    main()
        

            
