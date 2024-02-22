#topthree.py
# generates 10 random numbers, prints them out then prints out the top 3
#Author: Aoife Flavin

import random

#getting variables ready
how_many = 10
top_howmany = 3
range_from = 0
range_to = 100

#Create empty list
numbers = []

#This loop runs 'how_many' times (10)
#generates a random integer between the range and adds to numbers list
#Only adds one at a time
for i in range(0,how_many):
    numbers.append(random.randint(range_from,range_to))
    print (f"{how_many} random numbers\t {numbers}")

#creates a copy of the numbers list and assigns it the variable top_three
top_three = numbers.copy()

#Sorts the top 3 in descending order
top_three.sort(reverse = True)

#prints the top 3 using slicing
print(f"The top {top_howmany} are \t\t {top_three[0:top_howmany]}")
