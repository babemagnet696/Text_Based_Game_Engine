def get_name():
    name = str(input("What is your name: "))
    if len(name) >= 20:
        print(f"Max name length is 20\nPlease Try Again")
        return get_name()
    else:
        print(f"Welcome to my game {name}")
        return name
    
def get_action():
    action = input("What do you want to do: ")
    if action.lower() not in ["go", "look"]:
        print("Please enter a valid action")
        return get_action()
    return action