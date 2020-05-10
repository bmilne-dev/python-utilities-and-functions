#!/usr/bin/env python3

# import randint from the random module
# create class Die, with attribute sides.
# default sides=6. write a method
# roll_die() that prints a random number
# between 1 and the number of sides
# the die has. make a 6 sided die, roll it
# 10 times. then make a 10 and 20 sided die.

from random import randint

class Die():
    """virtual dice!!"""

    def __init__(self, sides=6):
        self.sides = sides

    def print_roll(self):
        print(f"Your roll (sides = {self.sides}):"
             f" {randint(1, self.sides)}")

    def roll(self):
        return randint(1, self.sides)

# die_1 = Die()
# die_1.roll_die()
# die_1.roll_die()
# die_1.roll_die()
# die_1.roll_die()
# die_1.roll_die()
# die_1.roll_die()

# ten_sides = Die(sides=10)
# twenty_sides = Die(sides=20)
# ten_sides.roll_die()
# twenty_sides.roll_die()
# die_test = Die(10)
# x = die_test.roll()
# print(x)
