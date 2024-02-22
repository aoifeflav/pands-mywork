# Random_guess.py
#Generates a random number between 100 to be guessed
#Author: Aoife Flavin

import random

random_number = random.randint(0,100)

guess = int(input("Please guess the number:"))

while guess != random_number:
    if guess > random_number:
        print("Too High")
    else:
        print("Too Low")
    guess = int(input("Please guess again:"))
    
print(f"Well done the number was {random_number}")
