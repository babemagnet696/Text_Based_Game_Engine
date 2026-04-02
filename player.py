from items import items

def get_name():
    name = str(input("What is your name: "))
    if len(name) >= 20:
        print(f"Max name length is 20\nPlease Try Again")
        return get_name()
    else:
        print(f"Welcome to my game {name}")
        return name


def inspect_room(room_item_list, target=None):
    if room_item_list == []:
        print("There is nothing here")
        return
    for item in room_item_list:
        print(f"{item}")

def inspect_inventory(inventory, items_list=None, target=None):
    if inventory == []:
        print("Inventory is empty")
        return
    
    for item in inventory:
        if target is None:
            print(f"{item}")
            continue


        if item == target.lower():
            print(f"{items_list[target]["description"]}")
            print(f"{items_list[target]["type"]}")
            return
        
    if target is None:
        return
    
    print(f"{target} not found")


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
    if inspect_room(runtime_rooms[current_room]["items"], target_item) is True:
        player_inventory.append(target_item)
        runtime_rooms[current_room]["items"].remove(target_item)



