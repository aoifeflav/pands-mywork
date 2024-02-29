# queue.py
#  puts 10 random numbers into a queue
# program should then output all values in queue, 
#then take the numbers from the queue one at a time, 
#print it and the current numbers still in the queue.
# Author: Aoife Flavin

#import the random module
import random

# create empty lst
queue = []

# Set parameters
no_of_numbers = 10
range_to = 100

#Generate the random list
for n in range(0,no_of_numbers):
    queue.append(random.randint(0,range_to))

print(f"Queue is {queue}")

#Open the while loop
while len(queue) != 0:
    current_number = queue.pop(0) #removes the first figure
    print(f"Current number is {current_number} and the queue is {queue}")

#Close the while loop when list is empty
print ("The queue is now empty")