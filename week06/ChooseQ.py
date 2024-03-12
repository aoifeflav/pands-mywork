#chooseQ.py
#Author: Aoife Flavin

#keeps displaying the menu until the user picks q.

#old code
def display_menu():
    print("What would you like to do?")
    print("(a) Add new sudent")
    print("(v) View students")
    print("(q) Quit")
    choice = input("Type one letter(a/v/d): ")
    return choice

choice = display_menu()
print(f"you chose {choice}")

#new code
def do_add():
    #finish later
    print("in adding")

def do_view() :
    #finish later
    print("in viewing")

#main program
choice = display_menu()
while (choice != "q"):
    if choice == "a":
        do_add()
    elif choice == "v":
        do_view()
    elif choice != "q":
        print("\nplease select either a, v or q")
    choice = display_menu()

