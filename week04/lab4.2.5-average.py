# average.py
# Keeps reading numbers until user enters 0
# Prints out each number and their average (list)

# Makes an empty list
numbers = []

#prompts yu to enter number
number = int(input("Enter a number (0 to quit):"))

# when number isn't 0 it is added to the empty list
while number != 0:
    numbers.append(number)

#reads the number and check if 0
    number = int(input("Enter another number (0 to quit):"))

#For loop iterates over each value in the numbers list, and prints the value
for value in numbers:
    print(value)

#makes the averages a float
average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}")


