from items import items

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
    if action.strip().lower() == "quit":
        return
    if action.strip().lower() == "help":
        return action
    full_action = action.split(" ", 1)
    if full_action[0].lower() in ["go", "look", "inspect"]:
        return full_action
    print("Please enter a valid action")
    return get_action()

def inspect(object, list):
    for item in list:
        if item is object:
            print(f"{items[item]}")
    print(f"{item} not found")