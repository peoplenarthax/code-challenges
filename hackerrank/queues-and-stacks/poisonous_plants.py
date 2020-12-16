#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Create descending stacks from the given poison list
def create_first_stacks(plant_list):
    stacks = []
	# Deque because pop left is O(1)
    plant_buffer = deque([plant_list[0]])
    for i in range(1, len(plant_list)):
        if plant_list[i] > plant_buffer[-1]:
            stacks.append(plant_buffer)

            plant_buffer = deque([plant_list[i]])
        else:
            plant_buffer.append(plant_list[i])
    
    if len(plant_buffer) > 0:
        stacks.append(plant_buffer)

    return stacks    
# Complete the poisonousPlants function below.
def poisonousPlants(plant_list):
    stacks = create_first_stacks(plant_list)

    days = 0
	# Once we have a single descending stack, no more plants will die
    while len(stacks) > 1:
        days += 1

        # remove left most of all the stacks except the first one (because it does not have a bigger number on the left)
        for i in range(1, len(stacks)):
            stacks[i].popleft()
        
        new_stacks = [stacks[0]]
		# we merge stacks that after the pop become descending order of the element on the left
        for i in range(1, len(stacks)):
            
            if len(stacks[i]) == 0 or new_stacks[-1][-1] >= stacks[i][0]:
                new_stacks[-1].extend(stacks[i])
            else:
                new_stacks.append(stacks[i])    
        stacks = new_stacks
    return days     
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
