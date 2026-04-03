from items import items
from parsing import normalize_argument

def get_name():
    name = str(input("What is your name: "))
    if len(name) >= 20:
        print(f"Max name length is 20\nPlease Try Again")
        return get_name()
    else:
        print(f"Welcome to my game {name}")
        return name


def inspect_room(room_item_list, target=None):
    cleaned_target = normalize_argument(target)
    if room_item_list == []:
        print("\nThere is nothing here")
        return None
    
    for item in room_item_list:
        cleaned_item = normalize_argument(item)
        if target is None:
            print(f"{item.title()}")
        elif cleaned_target == cleaned_item:
            return item
        
    if target:
        return None

def inspect_inventory(inventory, items_list=None, target=None):
    cleaned_target = normalize_argument(target)
    if inventory == []:
        print("Inventory is empty")
        return
    
    for item in inventory:
        cleaned_item = normalize_argument(item)
        if target is None:
            print(f"{item.title()}")
            continue


        if cleaned_item == cleaned_target:
            print(f"\nName: {item.title()}")
            print(f"Description: {items_list[cleaned_item]["description"]}")
            print(f"Item Type: {items_list[cleaned_item]["type"]}")
            return
        
    if target is None:
        return
    
    print(f"\n{target} not found")


def use_key(runtime_rooms, key, target, current_room):
    direction_to_unlock = runtime_rooms[current_room]["exits"][target]

    if items[key]["opens"] == direction_to_unlock["room"]:
        direction_to_unlock["locked"] = False
        print(f"\nThe path to the {target.title()} has been unlocked")
        return True
    
    print(f"\nIncorrect key")
    return False


def use_item(runtime_rooms, item, target_object, current_room):
    cleaned_item = normalize_argument(item)
    cleaned_target_object = normalize_argument(target_object)
    if items[cleaned_item]["type"] == "key":
        if use_key(runtime_rooms, cleaned_item, cleaned_target_object, current_room) is True:
            return True
        
    print(f"Could not use {cleaned_item.title()}")

def take_item(runtime_rooms, current_room, player_inventory, target_item):
    item_to_take = inspect_room(runtime_rooms[current_room]["items"], target_item)
    if item_to_take:
        player_inventory.append(item_to_take)
        runtime_rooms[current_room]["items"].remove(item_to_take)
        print(f"{item_to_take.title()} put in inventory")



