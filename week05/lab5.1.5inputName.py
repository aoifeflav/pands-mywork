# inputName.py
#Reads in names and grades until a blank is entered
# Author: Aoife Flavin

#Create empty dict
student = {}

#Read in students name
student_name = input("Please enter student name: ")
student["name"] = student_name

#Read in modules and grades
modules = []
while True:
    module_name = input("Enter module name (press ent to stop): ")
    if module_name == "":
        break
    grade = int(input(f"Enter grade for {module_name} module: "))
    #create a dict for module and grade and append it to modules
    modules.append({"course_name": module_name, "grade" : grade})

#Assign to module key
student["modules"] = modules

#print
print("Student: " + student["name"])
for module in student ["modules"] :
    print(module["course_name"] + " : " + str(module["grade"]))