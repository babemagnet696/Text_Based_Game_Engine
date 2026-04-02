valid_directions = [
    "north",
    "south",
    "east",
    "west"
]


def get_action():
    action = input("\nWhat do you want to do: ")
    if action == "":
        return get_action()
    clean_action = action.strip().lower()

    parts = clean_action.split()
    command = parts[0]
    args = []

    if len(parts) > 1:
        args.extend(parts[1:])

    if command == "quit":
        return (command, args)
    if command == "help":
        return (command, args)

    if command in ["go", "look"]:
        if len(args) < 1:
            args = get_arguments(command)
        return (command, args)
    
    if command == "inspect":
        if len(args) == 0:
            new_args = get_arguments(command)
            return (command, new_args)
        elif len(args) == 1:
            new_args = get_arguments(command, args[0])
            return (command, new_args)
        return (command, args)

    if command == "use":
        if len(args) == 0:
            new_arguments = get_arguments(command)
            return (command, new_arguments)
        elif len(args) == 1:
            new_arguments = get_arguments(command, args[0])
            return (command, new_arguments)
        return (command, args)
    
    if command == "take":
        if len(args) < 1:
            args = get_arguments(command)
        return (command, args)
        
    print("Please enter a valid action")
    return get_action()

def get_arguments(command, arg=None):
    args = []

    if command in ["go", "look"]:
        args.append(input("Please enter a direction: "))
        if args == ['']:
            return get_arguments(command)
        
    elif command == "inspect":
        if arg:
            return get_inspect_arguments(arg)
        return get_inspect_arguments()
    
    elif command == "take":
        args.append(input("What item do you want to take: "))
        if args == ['']:
            return get_arguments(command)
        
    elif command == "use":
        if arg:
            item = arg
            args.append(item)
        else:
            item = input("What item do you want to use:  ")
            if item == "":
                return get_arguments(command)
            args.append(item)
        args.append(input(f"What do you want to use {item} on: "))
        if args == [item, '']:
            return get_arguments(command, item)
    
    return args

def get_inspect_arguments(arg=None):
    args = []
    clean_text = normalize_argument(arg)

    if not clean_text or clean_text not in ["room", "inventory"]:
        print("\nPress enter to cancel")
        list_to_inspect = input("Do you want to inpsect the room or your inventory: ")
        if list_to_inspect == "":
            return "cancel"
        return get_inspect_arguments(list_to_inspect.lower())
    
    if clean_text == "room":
        args.append(clean_text)
        return args
    
    if clean_text == "inventory":
        args.append(clean_text)

    item_to_inspect = input("Press enter to view inventory or type an item to inspect: ")
    args.append(item_to_inspect)
    
    return args


def normalize_argument(arg=None):
    if arg:
        return arg.lower().strip()
    return None


    
