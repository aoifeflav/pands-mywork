# convert.py
# Takes in a float amount of dollars and returns that absolute amount in cent
# Author: Aoife Flavin

# Enter original number
dollar_amount = float(input("Please enter an amount:"))

# Turn it ito an absolute
absolute_amount = abs(dollar_amount)

# Turn it into cent
converted_amount = int(absolute_amount * 100)

#print it out
print(f"That amount in cent is {converted_amount}")