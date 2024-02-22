# Guess1.py
# Prompts the user to guess a number until they get it right
# Author: Aoife Flavin

correct_num = 30

guess = int(input("Please guess the number:"))

while guess != correct_num:
    print("Wrong")
    guess = int(input("Please guess again:"))

print(f"Well done the number was {correct_num}")
