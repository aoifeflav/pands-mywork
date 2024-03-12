# Student Added
# Author: Aoife Flavin

# Prints out a menu of commands we can perform, ie add, 
# view and quit. Return what the user chose.
def display_menu ():
    print("What would you like to do?")
    print("(a) Add new sudent")
    print("(v) View students")
    print("(q) Quit")
    choice = input("Type one letter(a/v/d): ")
    return choice

choice = display_menu ()
print(f"you chose {choice}")

