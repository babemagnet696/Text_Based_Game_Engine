help = '''
Type 'go' then the direction you want to go
Type 'look' then the direction you want to go
Type 'inspect' to inspect an item
Type 'use' to use an item in your inventory
Type 'get' to pick up and item
Valid directions are: "North, South, East, West"
Type 'quit to exit the game
Type 'help' to see this message again
'''


def check_cancel():
    print(f"\nIf you want to cancel just press enter")
    direction = input(": ")
    return direction


def end_check(runtime_rooms, current_room):
    print(runtime_rooms[current_room]["room_info"])
    if runtime_rooms[current_room]["game_over"] is True:
        return True
    return False

def move(runtime_rooms, current_room, direction=None):
    lowered_direction = direction.lower()

    if lowered_direction not in runtime_rooms[current_room]["exits"]:
        print(f"\n{direction} is not a valid direction.\nPlease type North, South, East, or West")
        new_direction = get_direction()
        if new_direction == True:
            return current_room
        return move(runtime_rooms, current_room, new_direction)
    
    path = runtime_rooms[current_room]["exits"][lowered_direction]
    if path["room"] is None:
        print(f"\nYou cannot go {lowered_direction}, the path is blocked")
        return current_room
    if path["locked"] is True:
        print(f"The way to {path["room"]} is blocked by a locked door")
        return current_room
    
    new_room = path["room"]
    return new_room



def look_direction(runtime_rooms, current_room, direction):
    lowered_direction = direction.lower()
    if lowered_direction not in runtime_rooms[current_room]["directional_info"]:
        print(f"\n{direction} is not a valid direction.\nPlease type North, South, East, or West")
        new_direction = get_direction()
        if new_direction == True:
            return current_room
        return look_direction(runtime_rooms, current_room, new_direction)
    
    path = runtime_rooms[current_room]["directional_info"][lowered_direction]
    if path is None:
        print(f"\nNothing of note {direction} of you")
        return
    print(path)

def get_direction():
    argument = input("If you want to cancel type cancel\nPlease enter a direction: ")
    if argument.lower() == "cancel":
        return True
    return argument
    

