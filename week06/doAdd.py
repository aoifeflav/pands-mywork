#doAdd.py
#working on the do add function of a larger program
#Author: Aoife Flavin

students = []
def readModules():
    modules = []
    module_name = input(f"\tEnter the first module name (blank to quit):")

    while module_name != "":
        module = {}
        module ["name"] = module_name

        module["grade"]=int(input("\tEnter grade:"))
        modules.append(module)
    #now read next module name
        module_name = input("\tEnter next module name(blank to quit)")

    return modules 

def do_add(students):
    current_student = {}
    current_student["name"]=input("enter name:")
    current_student["modules"]= readModules()

    students.append(current_student)

#test
do_add(students)
do_add(students)
print(students)