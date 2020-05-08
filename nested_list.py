#!/usr/bin/env python3
# print a neatly formatted summary of your lists within lists!
#
# example list:
list_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# inspiration:
# for row in list_1:
#     while row == list_1[0]:
#         for entry in row:
#             print(entry, end=', ')
#         print('\n')
#         break
#     while row == list_1[1]:
#         for entry in row:
#             print(entry, end=', ')
#         print('\n')
#         break
#     while row == list_1[2]:
#         for entry in row:
#             print(entry, end=', ')
#         print('\n')
#         break
#     while row == list_1[3]:
#         for entry in row:
#             print(entry, end='')
#         print('\n')
#         break

n = 0
for row in list_1:
    if n == len(list_1) - 1:
        while row == list_1[n]:
            if row[0] == row[-1]:
                print(row[0], '\n')
                break
            elif row[1] == row[-1]:
                print(f"{row[0], row[1]}")
            else:
                for entry in row[0:-1]:
                    print(entry, end=', ')
                print(row[-1])
                print('\n')
                n += 1
                break
    elif n == len(list_1):
        break
    else:
        while row == list_1[n]:
            for entry in row:
                print(entry, end=', ')
            print('\n')
            break
        n += 1
