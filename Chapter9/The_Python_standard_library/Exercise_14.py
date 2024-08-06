from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self, number_sided):
        """Simulate rolling a dice with a given number of sides and a given roll times."""
       
        count = 0
        while count < 10:
            self.sides = randint(1, number_sided)
            print("Rolling......: ", self.sides)
            count += 1
        
        print("\n")

        
my_dice = Die()
my_dice.roll_die(6)
my_dice.roll_die(10)
my_dice.roll_die(20)