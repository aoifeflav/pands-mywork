#read_dict.py
#read in a dict object from file.
#Author: Aoife Flavin

import json

FILENAME = "testdict.json"

def read_dict():
    with open(FILENAME)as f:
        return json.load(f)
    
#test
some_dict = read_dict()
print(some_dict)