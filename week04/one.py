# one.py
# Keeps prompting a user to enter a number until they enter-1

while True:
    initial = float(input("Please guess a number:"))

    if initial > -1:
        print("Try Again (lower):")
    elif initial < -1:
        print("Try Again (higher):")
    else:
        print("You got it")
        break