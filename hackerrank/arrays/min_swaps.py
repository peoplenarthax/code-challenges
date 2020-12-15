#!/bin/python3

import math
import os
import random
import re
import sys

# We will jump from index to the linked index until satisfy that our right value is self closed in this graph
def jumps_till_ordered(idx_target, value, acc, arr, travelled):
    if idx_target + 1 == value:
        return acc, travelled
    
    arr[idx_target], arr[value-1] = arr[value-1], arr[idx_target]
    return jumps_till_ordered(idx_target, arr[idx_target], acc +1, arr, travelled + [value]) 

def swapPositions(list, pos1, pos2):   
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list    

# Complete the minimumSwaps function below.
def slow_minimumSwaps(arr):
    swaps = 0
    travelled_nodes = []
    for idx, j in enumerate(arr):
        if j in travelled_nodes:
            continue
        while arr[idx] != idx + 1:
            arr = swapPositions(arr, idx, arr[idx]-1)
            travelled_nodes.append(j)
            swaps += 1
   
    return swaps   


def minimumSwaps(arr):
	# Initialize an array of same size
    visited_map = [0] * (len(arr) + 1)
	# Create array that reverse index - value
    for pos, val in enumerate(arr):
        visited_map[val] = pos

    swaps = 0
    for i in range(len(arr)):
		# The value is not in its place
        if arr[i] != i+1:
            swaps += 1
			# Swap value in arr
            arr[visited_map[i+1]] = arr[i]
			# Point in the visit map where did we swap the value (Keep track of the self closed)
            visited_map[arr[i]] = visited_map[i+1]
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
