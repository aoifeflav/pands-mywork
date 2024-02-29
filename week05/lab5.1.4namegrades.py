# namegrades.py
# stores and prins Mary's name and grades
#Author: Aoife Flavin

student = {
    "name" : "Mary",
    "modules" : [
        {"course_name" : "Programming", 
         "grade" : 45},
        {"course_name" : "History",
        "grade" : 99} ]}

print("Student: " + student["name"])
for module in student ["modules"] :
    print(module["course_name"] + " : " + str(module["grade"]))