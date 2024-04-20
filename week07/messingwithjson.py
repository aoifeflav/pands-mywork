# messingwithjson.py
#Author: Aoife Flavin

import json

FILENAME = "testdict.json"
sample = dict(name = 'fred', age = 31, grades = [1,34,55])

def write_dict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

#test
write_dict(sample)