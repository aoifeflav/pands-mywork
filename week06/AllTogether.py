#AllTogether.py
#Bringing all the previous steps together
#Author: Aoife Flavin

def display_menu():
    print("What would you like to do?")
    print("(a) Add new sudent")
    print("(v) View students")
    print("(q) Quit")
    choice = input("Type one letter(a/v/d): ")
    return choice

def do_add(students):
    current_student = {}
    current_student["name"]=input("enter name:")
    current_student["modules"]= read_modules()
    students.append(current_student)

def read_modules():
    modules = []
    module_name = input("\tEnter the first module name (blank to quit):")

    while module_name != "":
        module = {}
        module ["name"] = module_name
        module["grade"]=int(input("\tEnter grade:"))
        modules.append(module)
    #now read next module name
        module_name = input("\tEnter next module name(blank to quit)")

    return modules 

def display_modules(modules):
    print("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}")

def do_view(students) :
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])

#main program
students = []
choice = display_menu()
while (choice != "q"):
    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    elif choice != "q":
        print("\nplease select either a, v or q")
    choice = display_menu()
