def choice():
    choice_options = ['y', 'Y','Yes', 'yes', 'n', 'N', 'No', 'no']
    x = input("yes or no: ")
    while x not in choice_options: 
        x = input("yes or no: ")
    if x == 'yes' or x == 'Yes' or x == 'y' or x == 'Y':
        return True
    else:
        return False
