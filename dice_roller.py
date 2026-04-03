import random

class DiceRoller:
    def __init__(self, num_of_sides, num_of_dice):
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
    
class d20(DiceRoller):
    def __init__(self, num_of_dice, bonus=0, critical_chance_modifier=0):
        super().__init__(20, num_of_dice)
        self.modifier = critical_chance_modifier
        self.bonus = bonus

    def roll_dice(self):
        total = super().roll_dice()
        

        if total in range((20-self.modifier), 21):
            print("Critical Success!")
            total += self.bonus
            return total
        
        elif total == 1:
            print("Critical Fail!")
            total += self.bonus
            return total
        
        total += self.bonus
        return total
    
    def advantage(self):
        roll1 = random.randint(1, self.num_of_sides)
        roll2 = random.randint(1, self.num_of_sides)
        num_chosen = max(roll1, roll2)
        

        if num_chosen in range((20-self.modifier), 21):
            print(f"Advantage: {roll1} vs {roll2} → Critical Success!")
            return num_chosen
        
        elif num_chosen == 1:
            print(f"Advantage: {roll1} vs {roll2} → Critical Fail!")
            return num_chosen
        
        num_chosen += self.bonus
        print(f"Advantage: {roll1} vs {roll2} → {max(roll1, roll2)} + {self.bonus}")
        print(f"Total: {num_chosen}")
        return num_chosen
    
    def disadvantage(self):
        roll1 = random.randint(1, self.num_of_sides)
        roll2 = random.randint(1, self.num_of_sides)
        num_chosen = min(roll1, roll2)
        

        if num_chosen in range((20-self.modifier), 21):
            print(f"Disadvantage: {roll1} vs {roll2} → Critical Success!")
            return num_chosen
        
        elif num_chosen == 1:
            print(f"Disadvantage: {roll1} vs {roll2} → Critical Fail!")
            return num_chosen
        
        num_chosen += self.bonus
        print(f"Disadvantage: {roll1} vs {roll2} → {min(roll1, roll2)} + {self.bonus}" )
        print(f"Total: {num_chosen}")
        return num_chosen

class d12(DiceRoller):
    def __init__(self, num_of_dice, bonus=0):
        super().__init__(12, num_of_dice)
        self.bonus = bonus
    
    def roll_dice(self):
        return super().roll_dice() + self.bonus

class d10(DiceRoller):
    def __init__(self, num_of_dice, bonus=0):
        super().__init__(10, num_of_dice)
        self.bonus = bonus

    def roll_dice(self):
        return super().roll_dice() + self.bonus
    
class d8(DiceRoller):
    def __init__(self, num_of_dice, bonus=0):
        super().__init__(8, num_of_dice)
        self.bonus = bonus
        
    def roll_dice(self):
        return super().roll_dice() + self.bonus
    
class d6(DiceRoller):
    def __init__(self, num_of_dice, bonus=0):
        super().__init__(6, num_of_dice)
        self.bonus = bonus
        
    def roll_dice(self):
        return super().roll_dice() + self.bonus
    
class d4(DiceRoller):
    def __init__(self, num_of_dice, bonus=0):
        super().__init__(4, num_of_dice)
        self.bonus = bonus
        
    def roll_dice(self):
        return super().roll_dice() + self.bonus
    
def interactive_die():
    
    cases = {
        '20': d20,
        '12': d12,
        '10': d10,
        '8': d8,
        '6': d6,
        '4': d4
    }

    while True:
        try:
            dice_being_rolled = input("Enter the number of sides on the die (4, 6, 8, 10, 12, or 20): ").strip()
            if dice_being_rolled in cases:
                break  # Exit the loop if input is valid
            else:
                print("Enter a valid die type (4, 6, 8, 10, 12, or 20).")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    match dice_being_rolled:

        case '20':
            is_advantage = input("Roll with advantage? (y/n): ").strip().lower() == 'y'
            is_disadvantage = input("Roll with disadvantage? (y/n): ").strip().lower() == 'y'
            if is_advantage and is_disadvantage:
                die = d20(1)
                roll = die.roll_dice()
                print("Both advantage and disadvantage selected. Rolling normally.")
                print(f"Rolling 1d20: {roll}")
                return roll
            elif is_advantage:
                die = d20(2)
                roll = die.advantage()
                print(roll)
                return(roll)
            elif is_disadvantage:
                die = d20(2)
                roll = die.disadvantage()
                print(roll)
                return(roll)
            
            else:
                die = d20(1)
                roll = die.roll_dice()
                print(f"Rolling 1d20: {roll}")
                return roll
        
        case '12' | '10' | '8' | '6' | '4':
            num_of_dice = int(input("Enter the number of dice to roll: "))
            bonus = int(input("Enter any bonus to add (default 0): ") or 0)
            die = cases[dice_being_rolled](num_of_dice, bonus)
            roll = die.roll_dice()
            print(f"Rolling {num_of_dice}d{dice_being_rolled} + {bonus}: {roll}")
            return roll
        



if __name__ == "__main__":
    interactive_die()