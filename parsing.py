valid_directions = [
    "north",
    "south",
    "east",
    "west"
]

def clean_and_separate_action(action):
    clean_action = action.strip().lower()

    parts = clean_action.split()
    command = parts[0]
    args = []

    if len(parts) > 1:
        args.extend(parts[1:])

    return (command, args)


### This is just to get the initial command from the player
### Then wrapps all other functions into this
def get_action():
    action = input("\nWhat do you want to do: ")
    if action == "":
        return get_action()

    command, args = clean_and_separate_action(action)

    if command == "quit":
        return (command, args)
    
    if command == "help":
        return (command, args)

    if command in ["go", "look"]:
        return check_direction_command(command, args)
    
    if command == "inspect":
        return check_inspect_command(command, args)
    
    if command == "use":
        return check_use_command(command, args)
    
    if command == "take":
        return check_take_command(command, args)
        
    print("Please enter a valid action")
    return get_action()


### This is another wrapper but for the get_arguments functions
def get_arguments(command, arg=None):
    args = []

    if command in ["go", "look"]:
        return get_direction_arguments()
        
    elif command == "inspect":
        return get_inspect_arguments(arg)
    
    elif command == "take":
        return get_take_arguments()
        
    elif command == "use":
        return get_use_arguments(arg)
    
    return args



### quickly lowers and strips the strings
def normalize_argument(arg=None):
    if arg:
        return arg.lower().strip()
    return None


### Check functions
### These functions check how many arguments the action given have
### Different commands take different actions and this setup determines how many arguments to grab
def check_direction_command(command, args):
    if len(args) < 1:
        args = get_arguments(command)
    return (command, args)

def check_use_command(command, args):
        if len(args) == 0:
            new_args = get_arguments(command)
            return (command, new_args)
        elif len(args) == 1:
            new_args = get_arguments(command, args[0])
            return (command, new_args)
        elif len(args) > 2:
            if args[-1] in valid_directions:
                temp = " ".join(args)
                new_args = temp.rsplit(maxsplit=1)
                return (command, new_args)
        else:
            temp = " ".join(args)
            item_to_use = [temp]
            new_args = get_arguments(command, item_to_use[0])
            return (command, new_args)

        return (command, args)

def check_take_command(command, args):
    if len(args) < 1:
        args = get_arguments(command)
    if len(args) >= 2:
        temp = " ".join(args)
        new_args = [temp]
        return (command, new_args)
    return (command, args)

def check_inspect_command(command, args):
    if len(args) == 0:
        new_args = get_arguments(command)
        return (command, new_args)
    elif len(args) == 1:
        new_args = get_arguments(command, args[0])
        return (command, new_args)
    
    return (command, args)


### Get arguments functions
### If the check functions determine more arguments are needed these functions grab more
### Move and player functions require a certain amount of arguments so the game does not crash
def get_direction_arguments():
    args = []
    args.append(input("Please enter a direction: "))
    if args == ['']:
        return get_direction_arguments()
    return args

def get_use_arguments(arg=None):
    args = []
    if arg:
        item = arg
        args.append(item)
    else:
        item = input("What item do you want to use:  ")
        if item == "":
            return get_use_arguments()
        args.append(item)
    args.append(input(f"What do you want to use {item} on: "))
    if args == [item, '']:
        return get_use_arguments(item)
    return args

def get_take_arguments():
    args = []
    args.append(input("What item do you want to take: "))
    if args == ['']:
        return get_take_arguments()
    return args

def get_inspect_arguments(arg=None):
    args = []
    clean_text = normalize_argument(arg)

    if not clean_text or clean_text not in ["room", "inventory"]:
        print("\nType cancel to cancel the action")
        list_to_inspect = input("Do you want to inpsect the room or your inventory: ")
        if list_to_inspect == "cancel":
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

def check_cancel():
    print("Type cancel to cancel the action")
