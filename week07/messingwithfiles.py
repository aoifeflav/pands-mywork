# messingwithfiles.py
# reads in a number from a file that already exists
# Author: Aoife Flavin

FILENAME = "count.txt"
def read_number():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        #this file will be created when we write back
        #no file assumes first time running
        return 0
    

def over_write(number):
    with open(FILENAME, "wt") as f:
        #write takes a string so we need to convert
        f.write(str(number))

#main
num = read_number()
num += 1
print(f"we have run this program {num} times")
over_write(num)

import os.path
FILENAME = "count.txt"
if not os.path.isfile(FILENAME):
    print("File does not exist")

    #initialise file here
    over_write(0)