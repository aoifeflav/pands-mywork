# normalise.py
# reads a string, strips any leading or trailing spaces
# Converts string to lower case
# outputs the length of the input and output strings
# Author: Aoife Flavin

raw_string = input("Please enter a string:")

# Remove leading or trailing spaces
normalised_string = raw_string.strip().lower()

#Find length of input and output
input_length = len(raw_string)
output_lenght = len(normalised_string)

#print
print(f"That string normalised is:{normalised_string}")
print(f"We reduced the input string from {input_length} to {output_lenght} characters")