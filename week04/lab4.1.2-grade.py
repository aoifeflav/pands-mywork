# grade.py
# Reads in a student's mark and prints their grade
# Author

percent = float(input("Enter the percentage:"))

r_percent = round(percent)

if (r_percent < 40):
    print("Fail")
elif (r_percent < 50):
    print("Pass")
elif (r_percent < 60):
    print("Merit 2")
elif (r_percent < 70):
    print("Merit 1")
else:
    print("Distinction") 