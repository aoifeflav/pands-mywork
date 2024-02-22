# Guess2.py
# Prompts the user to guess a number until they get it right
# Thhis time with hints
# Author: Aoife Flavin

correct_num = 30

guess = int(input("Please guess the number:"))

while guess != correct_num:
    if guess > correct_num:
        print("Too High")
    else:
        print("Too Low")
    guess = int(input("Please guess again:"))
    
print(f"Well done the number was {correct_num}")
