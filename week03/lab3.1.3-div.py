# div.py
# Divides two numbers and gives the result with a remainder
# Author: Aoife Flavin

number1 = int(input("Enter first number:"))
number2 = int(input("Enter the number you want to divide by:"))

result = (number1//number2)
remainder = (number1%number2)

print(f"{number1} divided by {number2} is {result} with remainder {remainder}")