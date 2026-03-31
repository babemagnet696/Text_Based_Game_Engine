template = {
    "room_info": "",
    "game_over": False,
    "directional_info": {
        "north": "",
        "south": "",
        "east": "",
        "west": ""
    },
    "exits": {
        "north": None,
        "south": None,
        "east": None,
        "west": None
    }
}

rooms = {
    "cell": {
            "room_info": "A dark and cold room with a door that is slightly open",
            "game_over": False,
            "directional_info": {
                "north": "A brightly lit hallway",
                "south": "A cold, stone, moss covered wall, no way you're going that way",
                "east": "A cold, stone, moss covered wall, no way you're going that way",
                "west": "A cold, stone, moss covered wall, no way you're going that way"
            },
            "exits": {
                "north": "hallway",
                "south": None,
                "east": None,
                "west": None
            }
        },
        "hallway": {
            "room_info": "A brightly lit hallway filled with torches. The walls are made of stone",
            "game_over": False,
            "directional_info": {
                "north": "A stone wall blocks your path",
                "south": "A small cell, would you really want to go back in there?",
                "east": "A wooden door, there seems to be light behind it",
                "west": "A dark room covered in blood and in the middle is a single chair"
            },
            "exits": {
                "north": None,
                "south": "cell",
                "east": "wooden_door",
                "west": "bloodied_room"
            }
        },
        "bloodied_room": {
            "room_info": "The smell of iron and blood fills your nose. Bodies lay strewn across the walls and floor.\nIn the middle is a lone chair with chains to hold down the victim.\nYou feel something hit the back of your head\nYou don't wake back up",
            "game_over": True,
        },
        "wooden_door": {
            "room_info": "A average wooden door, unlocked",
            "game_over": False,
            "directional_info": {
                "north": "A stone wall",
                "south": "A stone wall",
                "east": "The wooden door blocks the path",
                "west": "A brightly lit hallway, you feel a sense of doom coming from that way"
            },
            "exits": {
                "north": None,
                "south": None,
                "east": "escape",
                "west": "hallway"
            }
        },
        "escape": {
            "room_info": "You open the door and it leads outside.\nNot sure where you are but anywhere is better than here\nYou start walking forward\nCongratulations! You Win!",
            "game_over": True,
        }
}