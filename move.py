from rooms import rooms

help = '''
Type 'go' then the direction you want to go
Type 'look' then the direction you want to go
Valid directions are: "North, South, East, West"
Type 'quit to exit the game
Type 'help' to see this message again
'''

def check_cancel():
    print(f"\nIf you want to cancel just press enter")
    direction = input(": ")
    return direction

def move(current_room, direction):
    lowered_direction = direction.lower()

    if lowered_direction not in rooms[current_room]["exits"]:
        print(f"\n{direction} is not a valid direction.\nPlease type North, South, East, or West")
        new_direction = check_cancel()
        if new_direction == "":
            return current_room
        return move(current_room, new_direction)
    
    path = rooms[current_room]["exits"][lowered_direction]
    if path is None:
        print(f"\nYou cannot go {lowered_direction}, the path is blocked")
        return current_room
    new_room = path

    return new_room

def check_room(current_room):
    print(rooms[current_room]["room_info"])
    if rooms[current_room]["game_over"] is True:
        return True
    return False

def check_direction(current_room, direction):
    lowered_direction = direction.lower()
    if lowered_direction not in rooms[current_room]["directional_info"]:
        print(f"\n{direction} is not a valid direction.\nPlease type North, South, East, or West")
        new_direction = check_cancel()
        if new_direction == "":
            return current_room
        return check_direction(current_room, new_direction)
    
    path = rooms[current_room]["directional_info"][lowered_direction]
    if path is None:
        print(f"\nNothing of note {direction} of you")
        return
    print(rooms[current_room]["directional_info"][lowered_direction])

def get_direction(action):
    if len(action) < 2:
        direction = input("\nWhat direction do you want to choose: ")
    else:
        direction = action[1].lower().strip()
    return direction

