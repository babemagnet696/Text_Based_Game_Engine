import os
from player import get_name, get_action
from move import check_cancel, move, check_room, check_direction, help

good_directions = [
    "north",
    "south",
    "east",
    "west"
]



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    end_check = False
    name = get_name()
    current_room = "cell"
    print(f"You wake up in a dark room. It is cold and damp.")
    print(f"There is one way you can go:\n\nNorth out of your cell\n")
    print(help)
    
    while True:
        action = get_action()
        if action is None:
            break
        elif action == "help":
            print(help)

        if len(action) < 2:
            direction = input("\nWhat direction do you want to choose: ")
        else:
            direction = action[1].lower().strip()
        
        if action[0] == "go":
            current_room = move(current_room, direction)
            end_check = check_room(current_room)
            

        elif action[0] == "look":
            check_direction(current_room, direction)
        
        if end_check is True:
            break
        






if __name__ == "__main__":
    main()
        

            
