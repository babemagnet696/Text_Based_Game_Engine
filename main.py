import os
from player import get_name


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    name = get_name()
    current_room = "cell"
    print(f"You wake up in a dark room. It is cold and damp.")
    print(f"There is one way you can go:\nNorth out of your cell")
    print(f"Hint: Type 'go' then the direction you want to go")
    print(f"Hint: Type 'look' then the direction you want to go")
    
    while True:
        action = input("What do you want to do: ")
        if action.lower() not in ["go", "look"]:
            



if __name__ == "__main__":
    main()
        

            
