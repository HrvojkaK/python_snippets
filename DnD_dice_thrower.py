# random integer generator simulating many-sided dice

import random

class Dice:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def roll(self):
        for i in range(int(self.x)):
            print(random.randint(1,int(self.y)))



num_of_sides = input("How many sides does the die have (e.g. 4, 5,... 20-sided die? " )
num_of_dice = input("And how many dice are you throwing? " )
throw_dice = Dice(num_of_dice, num_of_sides)
throw_dice.roll()
