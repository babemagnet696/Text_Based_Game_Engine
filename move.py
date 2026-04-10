from parsing import normalize_argument, get_direction_arguments, valid_directions

help = '''
1. Type 'go' then the direction you want to go
2. Type 'look' then the direction you want to go
3. Type 'inspect' to inspect an item
4. Type 'use' to use an item in your inventory
5. Type 'take' to pick up and item
6. Valid directions are: "North, South, East, West"
7. Type 'quit to exit the game
8. Type 'help' to see this message again
'''


def end_check(runtime_rooms, current_room):
    if runtime_rooms[current_room]["game_over"] is True:
        return True
    return False

def move(runtime_rooms, current_room, direction=None):
    try:

        if direction not in runtime_rooms[current_room]["exits"]:
            print(f"\n{direction} is not a valid direction.\nPlease type North, South, East, or West")
            new_direction = get_direction_arguments()[0]
            return move(runtime_rooms, current_room, new_direction)
        
        path = runtime_rooms[current_room]["exits"][direction]
        if path["room"] is None:
            print(f"\nYou cannot go {direction.title()}, the path is blocked")
            return current_room
        if path["locked"] is True:
            print(f"The way to {path["room"]} is blocked by a locked door")
            return current_room
        
        new_room = path["room"]
        print(runtime_rooms[new_room]["room_info"])
        return new_room
    
    except ValueError(f"Room {path["room"]} does not exist")



def look_direction(runtime_rooms, current_room, direction):

    if direction not in runtime_rooms[current_room]["directional_info"]:
        print(f"\n{direction} is not a valid direction.\nPlease type North, South, East, or West")
        new_direction = get_direction_arguments()[0]
        return look_direction(runtime_rooms, current_room, new_direction)
    
    path = runtime_rooms[current_room]["directional_info"][direction]
    if path is None:
        print(f"\nNothing of note {direction.title()} of you")
        return
    print(path)


    

