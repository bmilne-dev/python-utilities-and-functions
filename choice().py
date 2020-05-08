def choice():
    choice_options = ['y', 'yes', 'n', 'no']
    x = input("yes or no: ").lower()
    while x not in choice_options: 
        x = input("yes or no: ").lower()
    if x == 'yes' or x == 'y':
        return True
    else:
        return False
