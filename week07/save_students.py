#save_students.py
#Using last week's rogram bu saving the students
#Author: Aoife Flavin

import json

students = []
FILENAME = "students.json"

def write_dict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

def read_dict():
    with open(FILENAME)as f:
        return json.load(f)

def display_menu():
    print("What woud you like to do?")
    print("\t(a) Add new sudent")
    print("\t(v) View students")
    print("\t(l) load students")
    print("\t(s) save students")
    print("\t(q) Quit")
    choice = input("Type one letter(a/v/l/s/q): ").strip()

    return choice

def do_add():
    current_student = {}
    current_student["name"]=input("enter name:")
    current_student["modules"]= read_modules()
    students.append(current_student)
    
def read_modules():
    modules = []
    module_name = input("\Enter the first module name (blank to quit): ").strip()

    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
#next module name
        module_name = input("\tEnter next module name (blank to quit) :").strip()
    
    return modules

def display_modules(modules):
    print("\tName \t Grade")
    for module in modules:
        print(f"\t{module['name']} \t {module['grade']}")

def do_view():
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])

def do_save():
    write_dict(students)
    print("students saved")
   
def do_load():
    global students
    students = read_dict()
    print("students loaded")

#main program
choice = display_menu()
while(choice != 'q'):
    if choice == 'a':
        do_add()
    elif choice =='v':
        do_view()
    elif choice == 'l':
        do_load()
    elif choice == 's':
        do_save()
    elif choice != 'q':
        print("\n\nPlease select either a,v,s or q")
    choice = display_menu() 

    
    