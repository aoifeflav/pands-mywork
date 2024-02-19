# randomfruit.py
# Prints out the name of a random fruit
# Author: Aoife Flavin

import random

fruits = ("Apple", "Orange", "Banana", "Pear")

#Find a random number between 0 and length -1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print(f"A random fruit:{fruit}")

#EXTRA QUESTIONS
# Should be:
message = ("I have eaten " + str(99) + " Burritos.")
print(message)

# 7. Variable names cannot start with numbers
# 8. int() str() float()