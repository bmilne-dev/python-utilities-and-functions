#!/usr/bin/env python3

# an interactive dice rolling script.

from dice import Die

dice_1 = Die()
dice_10 = Die(10)
dice_20 = Die(20)

size_list = ['6', '10', '20', 'custom']

active = True
while active:
    print("Welcome to dice 2.0.")
    size = input("How many sides? (6/10/20/Custom): ").lower()
    while size not in size_list:
        size = input("How many sides? (6/10/20/Custom): ").lower()

    counter = 0
    if size == 'custom':
        sides = int(input("Custom sides (0-100): "))
        dice = Die(sides)
    elif size == '6':
        dice = dice_1
    elif size == '10':
        dice = dice_10
    else:
        dice = dice_20

    number = int(input("How many would you like to roll at once? (1-20): "))

    for _ in range(number):
        counter += dice.roll()

    print(f"Your roll is: {counter}")
    again = input("Roll again? (Y/N): ").lower()
    if again not in "ynYN":
        again = input("Roll again? (Y/N): ").lower()
    if again == 'y':
        continue
    elif again == 'n':
        active = False
