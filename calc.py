#!/usr/bin/env python3

# building a 'better' calc based on free code camp

def keep_going():
    ans_list = ['y', 'n']
    ans = input("Do another calculation? (Y/N): ").lower()
    while ans not in ans_list:
        ans = input("Do another calculation? (Y/N): ").lower()
    if ans == 'y':
        return True
    else:
        return False


active = True
while active == True:
    num_1 = float(input("First Number: "))
    operator = input("Operator: ")
    num_2 = float(input("Second Number: "))
    if operator == '+':
        print(num_1 + num_2)
        x = keep_going()
        if x == False:
            active = False
    elif operator == '-':
        print(num_1 - num_2)
        x = keep_going()
        if x == False:
            active = False
    elif operator == '*':
        print(num_1 * num_2)
        x = keep_going()
        if x == False: active = False
    elif operator == '/':
        print(num_1 / num_2)
        x = keep_going()
        if x == False:
            active = False
    else:
        print("Did not recognize that operator")
        x = keep_going()
        if x == False:
            active = False
