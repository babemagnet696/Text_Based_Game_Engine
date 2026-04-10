# Text based Game Engine

# About

This was my first personal project. It origially started put as a text based game only, but quickly became an engine. It is nowhere near complete but it is close enough to build a basic concept of a game with. I plan to add more features in the future. It took me two weeks to get where it is now.

### Tools

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="100px" />

### Challenges

The hardest part was keeping track of where everything was in the beginning. If I made a few changes one might break a few things. To combat this I made smaller and smaller functions and a lot of safeguards to prevent crashes. This worked for awhile until I made the battle system. Classes had abilities, and abilites had status effects, and both abilities and status effects affected an Entity.

An unexpected difficulty I had was keeping the folder clean and neat. As well as naming things. That was defenitly a constant battle.

### What I Learned

Start simple and build up. Don't get any big ideas right away. That was my mistake and once I saw each function as it's own goal it became easier to write. Of course I had an overall idea but I had to break it into pieces. I couldn't start with a whole battle system and movement system in one swoop. Many more bugs would have been introduced that way.

Keeping the scope of work small allowed me to get a better understanding of each file and what it contained. When a bug happened I could quickly narrow down where it was without a stack trace.

I also learned that even simple programs take a lot of code and a lot of hours. It ended up being way bigger than I first imagined.

The part that helped me the most was refactoring. If I saw a function start to become long I looked for ways to make it smaller. It cleaned up the code and made it much more readable. There is still  plenty of refactoring to do.

Parsing was the most exciting file to refactor. It became super clean and clear what everything did.

```py
def normalize_argument(arg=None):
```

```py
def check_take_command(command, args):
```

```py
def get_use_arguments(arg=None):
```

# Features

### User input parsing, normalization, and validation

When not in batte, the player can move, take, look, and inspect (room, inventory) giving them a full imersive view of their enviroment. Bad inputs lead to asking again. There is also an option to cancel inputs as well by typing cancel.

```py
def get_action():
    action = input("\nWhat do you want to do: ")
    if action == "":
        return get_action()

    command, args = clean_and_separate_action(action)

    if command == "quit":
        return (command, args)
    
    if command == "help":
        return (command, args)

    if command in ["go", "look", "move"]:
        return check_direction_command(command, args)
    
    if command == "inspect":
        return check_inspect_command(command, args)
    
    if command == "use":
        return check_use_command(command, args)
    
    if command == "take":
        return check_take_command(command, args)
        
    print("Please enter a valid action")
    return get_action()
```

```py
def get_arguments(command, arg=None):
    args = []

    print("\nType 'cancel' at any time to cancel the action\n")

    if command in ["go", "look", "move"]:
        return(get_direction_arguments())
        
    elif command == "inspect":
        return(get_inspect_arguments(arg))
    
    elif command == "take":
        return(get_take_arguments())
        
    elif command == "use":
        return(get_use_arguments(arg))

    
    return args
```

### Classes

I was inspired by DnD. There are 5 classes to choose from. Fighter, Wizard, Ranger, Monk, Warlock. Each has unique abilities to deal damage, give an advantage, or inflict status effects, or inflict disadvantage. Currently the stats are fixed with plans to add a leveling system.

```py
class Warlock(Entity):
    def __init__(self, name, level):
        a_abilities = [eldritch_blast, life_drain, hex, dark_surge]
        super().__init__(
            name,
            level,
            12,
            8,
            12,
            10,
            10,
            16,
            abilities=a_abilities
        )
```

### Dice rolling

Also DnD inspired I added a dice rolling system with most dice we all know and love. D20, D12, D10, D8, D6, D4. These dice are available on another repo on my profile.

```py
class DiceRoller:
    def __init__(self, num_of_sides, num_of_dice=1):
        self.num_of_sides = int(num_of_sides)
        self.num_of_dice = int(num_of_dice)
        self.rolls = []
        self.total = 0

    def roll_dice(self):
        self.rolls = [random.randint(1, self.num_of_sides) for _ in range(self.num_of_dice)]
        self.total = sum(self.rolls)
        if self.num_of_dice > 1:
            print(f"Individual rolls: {', '.join(map(str, self.rolls))}")
        return self.total
```

### Hit chance and saving throws

This one was fun to make. Every class has AC based on their dex and eventually armor (maybe feats later on who knows). d20 checks agains their ac using an attack roll. Certain attacks that have status effects roll again for a saving throw with the effects own difficulty class. There is also advantage and disadvantage that takes the higher or lower of two dice rolls. Some attacks can't miss such as magic missle. To do that I added a can_miss=bool for the ability.

```py
 def saving_throw(self, entity):
    if self.dc is not None:
        stat = getattr(entity, self.save_stat)
        modifier = entity.get_modifier(stat)
        die = d20(bonus=modifier)
        _, roll = die.roll_dice()
        return roll >= self.dc
    return False
```

```py
def attack_roll(self, modifier, disadvantage=False, advantage=False, crit_modifier=0):
    die = d20(bonus=(self.roll_modifier + modifier), crit_chance_modifier=crit_modifier)

    # Returns a tuple (is_natural, roll_total)
    # If is_natural is True and a 20 a crit lands Calculated in battle_system
    # Attacks that can't miss can't crit since they don't roll
    if not self.can_miss:
        return (False, 9999)

    if advantage and not disadvantage:
        dice_roll = die.advantage()

    elif disadvantage and not advantage:
        dice_roll = die.disadvantage()

    else:
        # For when dis + adv cancel out True or are False
        dice_roll = die.roll_dice()

    return dice_roll
```

### Abilities and Status Effects

Every class has at least 4 abilities and some with status effects. Some deal damage to the enemy, some only apply a status effect to the enemy, some just apply a status affect to the caster.

```py
hex = Ability(
    name="Hex",
    dice_class=None,
    num_of_dice=0,
    base_damage=0,
    cooldown=2,
    status_effect=True,
    target_effect=Hex()
)
```
```py
charge = Ability(
    name="Charge",
    dice_class=None,
    num_of_dice=0,
    base_damage=5,
    cooldown=2,
    status_effect=True,
    self_effect=GainAdvantage()
)
```

```py
quick_shot = Ability(
    name="Quick Shot",
    dice_class=d8,
    num_of_dice=1,
    base_damage=0,
    cooldown=0,
    roll_modifier=3
)
```

# Getting Started

### Prerequisits

The latest version of python3 must be installed to run:

-   Python 3.12.3 or higher

### Setup

1. Clone the repository to your local machine

```
git clone https://github.com/babemagnet696/my_first_game.git
```

2. Change into the project directory

```
cd Text_Based_Game_Engine
```

3. Run main.py for basic game

```
python3 main.py
```

4. You can use the rooms templete and move, player functions to make your own game!



