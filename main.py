import os
import time
import copy
from player import get_name, get_action
from move import move, check_room, check_direction, help, get_direction
from rooms import rooms


max_inventory_size = 10

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    inventory = []
    runtime_rooms = copy.deepcopy(rooms)
    end_check = False
    name = get_name()
    current_room = "cell"

    time.sleep(2)    
    print(f"You wake up in a dark room. It is cold and damp.")
    print(f"There is one way you can go:\n\nNorth out of your cell")
    print(f"Type help if you are stuck")
    
    while True:
        action = get_action()
        if action is None:
            break
        elif action == "help":
            print(help)

       
        
        if action[0] == "go":
            direction = get_direction(action)
            current_room = move(current_room, direction)
            end_check = check_room(current_room)
            

        elif action[0] == "look":
            direction = get_direction(action)
            check_direction(current_room, direction)

        elif action[0] == "inspect":
            if len(action) < 2:
                item = input("What do you want to inspect: ")
            
        
        if end_check is True:
            break
        


if __name__ == "__main__":
    main()
        

            
