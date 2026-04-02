import os
import time
import copy
from parsing import get_action
from player import get_name, inspect_room, inspect_inventory, use_item, take_item
from move import move, end_check, look_direction, help, get_direction
from items import items
from rooms import rooms


max_inventory_size = 10

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    player_inventory = []
    runtime_rooms = copy.deepcopy(rooms)
    game_over = False
    #name = get_name()
    current_room = "cell"

    #time.sleep(2)    
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


       
        
        if command == "go":
            direction = args[0]
            current_room = move(runtime_rooms, current_room, direction)
            game_over = end_check(runtime_rooms, current_room)
            

        elif command == "look":
            direction = args[0]
            look_direction(runtime_rooms, current_room, direction)

        elif command == "inspect":
            if args[0] == "room":
                inspect_room(runtime_rooms[current_room]["items"])
            if args[0] == "inventory":
                if args[1] == "":
                    inspect_inventory(player_inventory)
                else:
                    inspect_inventory(player_inventory, items, args[1])
        
        elif command == "use":
            use_item(runtime_rooms, args[0], args[1], current_room)
        
        elif command == "take":
            take_item(runtime_rooms, current_room, player_inventory, args[0])
            
        
        if game_over is True:
            break
        


if __name__ == "__main__":
    main()
        

            
