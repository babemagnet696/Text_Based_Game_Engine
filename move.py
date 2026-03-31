from rooms import rooms

def move(current_room, direction):
    lowered_direction = direction.lower()

    if lowered_direction not in rooms[current_room]["exits"]:
        print(f"{lowered_direction} is not a valid direction.\nPlease type North, South, East, or West")
        return current_room
    
    path = rooms[current_room]["exits"][lowered_direction]
    if path is None:
        print(f"You cannot go {lowered_direction}, the path is blocked")
        return current_room
    new_room = path

    return new_room

def check_room(current_room):
    print(rooms[current_room]["room_info"])
    if rooms[current_room]["game_over"] is True:
        return False
    return True

def check_direction(current_room, direction):
    lowered_direction = direction.lower()
    if lowered_direction not in rooms[current_room]["directional_info"]:
        print(f"{lowered_direction} is not a valid direction.\nPlease type North, South, East, or West")
        return
    
    path = rooms[current_room]["directional_info"][lowered_direction]
    if path is None:
        print(f"Nothing of note {direction} of you")
        return
    print(rooms[current_room]["directional_info"][lowered_direction])