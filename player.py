from items import items
from move import get_direction

def get_name():
    name = str(input("What is your name: "))
    if len(name) >= 20:
        print(f"Max name length is 20\nPlease Try Again")
        return get_name()
    else:
        print(f"Welcome to my game {name}")
        return name
    
def get_action():
    action = input("\nWhat do you want to do: ")
    if action == "":
        return get_action()
    clean_action = action.strip().lower()

    parts = clean_action.split(maxsplit=2)
    command = parts[0]
    arguments = []

    if len(parts) > 1:
        arguments.extend(parts[1:])

    if command == "quit":
        return (command, arguments)
    if command == "help":
        return (command, arguments)

    if command in ["go", "look"]:
        if len(arguments) < 1:
            arguments = get_arguments(command)
        return (command, arguments)
    
    if command == "inspect":
        return (command, arguments)

    if command == "use":
        if len(arguments) == 0:
            new_arguments = get_arguments(command)
            return (command, new_arguments)
        elif len(arguments) == 1:
            new_arguments = get_arguments(command, arguments[0])
            return (command, new_arguments)
        return (command, arguments)
    
    if command == "get":
        if len(arguments) < 1:
            arguments = get_arguments(command)
        return (command, arguments)
        
    print("Please enter a valid action")
    return get_action()


def inspect(items_list, target=None):
    if items_list == []:
        print("There is nothing of interest here")

    for item in items_list:
        if target is None:
            print(f"{item}")
            continue
        if item == target.lower():
            print(f"{items[item]["description"]}")
            print(f"{items[item]["type"]}")
            return True
        
    if target is None:
        return
    print(f"{target} not found")
    return False

def use_key(runtime_rooms, key, target, current_room):
    base_for_dictionary = runtime_rooms[current_room]["exits"][target]
    if items[key.lower()]["opens"] == base_for_dictionary["key"]:
        base_for_dictionary["locked"] = False
        print(f"{base_for_dictionary["room"]} has been unlocked")
        return True
    print(f"Incorrect key")
    return False


def use_item(runtime_rooms, item, target_object, current_room):
    if items[item.lower()]["type"] == "key":
        if use_key(runtime_rooms, item, target_object, current_room) is True:
            return True
    print(f"Could not use {item}")

def get_item(runtime_rooms, current_room, player_inventory, target_item):
    if inspect(runtime_rooms[current_room]["items"], target_item) is True:
        player_inventory.append(target_item)
        runtime_rooms[current_room]["items"].remove(target_item)


def get_arguments(command, single_argument=None):
    arguments = []
    if command in ["go", "look"]:
        arguments.append(input("Please enter a direction: "))
        if arguments == ['']:
            return get_arguments(command)
    elif command == "inspect":
        return None
    elif command == "get":
        arguments.append(input("What item do you want to get: "))
        if arguments == ['']:
            return get_arguments(command)
    elif command == "use":
        if single_argument:
            item = single_argument
            arguments.append(item)
        else:
            item = input("What item do you want to use:  ")
            if item == "":
                return get_arguments(command)
            arguments.append(item)
        arguments.append(input(f"What do you want to use {item} on: "))
        if arguments == [item, '']:
            return get_arguments(command, item)
    return arguments
