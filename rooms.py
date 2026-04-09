from entities import Fighter, Wizard, Monk, Ranger, Warlock

template = {
            "room_info": "",
            "game_over": False,
            "directional_info": {
                "north": "",
                "south": "",
                "east": "",
                "west": ""
            },
            "items": [],
            "enemies": None,
            "exits": {
                "north": {
                    "room": None,
                    "locked": False,
                    "key": None
                },
                "south": {
                    "room": None,
                    "locked": False,
                    "key": None
                },
                "east": {
                    "room": None,
                    "locked": False,
                    "key": None
                },
                "west": {
                    "room": None,
                    "locked": False,
                    "key": None
                }
            },
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
            "items":["test key"],
            "enemies": None,
            "exits": {
                "north": {
                    "room": "hallway",
                    "locked": False,
                    "key": None
                },
                "south": {
                    "room": None,
                    "locked": False,
                    "key": None
                },
                "east": {
                    "room": None,
                    "locked": False,
                    "key": None
                },
                "west": {
                    "room": None,
                    "locked": False,
                    "key": None
                }
            }
        },


        "hallway": {
            "room_info": "A brightly lit hallway filled with torches. The walls are made of stone",
            "game_over": False,
            "directional_info": {
                "north": "A stone wall blocks your path",
                "south": "A small cell, would you really want to go back in there?",
                "east": "A locked wooden door, there seems to be light behind it",
                "west": "A dark room covered in blood and in the middle is a single chair"
            },
            "items": [],
            "enemies": None,
            "exits": {
                "north": {
                    "room": None,
                    "locked": False,
                    "key": None
                },
                "south": {
                    "room": "cell",
                    "locked": False,
                    "key": None
                },
                "east": {
                    "room": "escape",
                    "locked": True,
                    "key": "test key"
                },
                "west": {
                    "room": "bloodied_room",
                    "locked": False,
                    "key": None
                }
            }
        },


        "bloodied_room": {
            "room_info": "The smell of iron and blood fills your nose. Bodies lay strewn across the walls and floor.\nIn the middle is a lone chair with chains to hold down the victim.\nYou are not alone...\nPrepare for battle!",
            "directional_info": {
                "north": "Nothing but a bloody wall",
                "south": "Nothing but a bloody wall",
                "east": "The brightly lit hallway",
                "west": "There is a way down, I don't want to go that way\nThere is screaming"
                },
            },
            "items": [],
            "enemies": Fighter("Skeleton", 1),
            "exits": {
                "north": {
                    "room": None,
                    "locked": False,
                    "key": None
                },
                "south": {
                    "room": None,
                    "locked": False,
                    "key": None
                },
                "east": {
                    "room": "Hallway",
                    "locked": False,
                    "key": None
                },
                "west": {
                    "room": None,
                    "locked": False,
                    "key": None
                }
            },


        "escape": {
            "room_info": "You open the door and it leads outside.\nNot sure where you are but anywhere is better than here\nYou start walking forward\nCongratulations! You Win!",
            "game_over": True,
        }
}

