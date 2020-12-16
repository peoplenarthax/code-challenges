#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def riddle(arr):
    stack = []
    arr.append(0) # Add 0 at the end of the numbers
    map_of_minimums=defaultdict(int)
    # Identify the largest window a number is minimum to
    for index,current_value in enumerate(arr):           
        new_index=index

        while stack and stack[-1][0]>=current_value:
            val,old_index = stack.pop()
            map_of_minimums[current_value]=max(map_of_minimums[current_value],index-old_index+1)
            map_of_minimums[val]=max(map_of_minimums[val],index-old_index)
            new_index=old_index
        stack.append([current_value,new_index])
    del map_of_minimums[0] # Removed artificial entry

    e=defaultdict(int)
    # Inverting the saved values to compare the biggest in each window size
    for i in map_of_minimums:                           
        e[map_of_minimums[i]]=max(e[map_of_minimums[i]],i)

    ans=[e[len(arr)-1]] # First add the global minimum
    for i in range(len(arr)-2,0,-1):        
        # If window does not exist or is smaller than the previous window element, we use the previous
        if e[i]<ans[-1]:
            ans.append(ans[-1])
        else:
            ans.append(e[i])
    return reversed(ans) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
