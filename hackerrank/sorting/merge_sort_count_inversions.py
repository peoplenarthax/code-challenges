#!/bin/python3

import math
import os
import random
import re
import sys

def merge(a, b):
    num_of_swaps = 0
    c = []

    while len(a) > 0 and len(b) > 0:
        if (a[0] > b[0]):
			## Inversion only happens when a > b, and we add len(a) because this means that elements to the right of the current a element, will need to swap
            num_of_swaps += len(a)
            swap_element = b.pop(0)
            c.append(swap_element)
        else:
            correct_element = a.pop(0)
            c.append(correct_element)
            
    if len(a) > 0:
        c.extend(a)
    else:
        c.extend(b)
    
    print(num_of_swaps)
    return c, num_of_swaps

# Using an incremental index instead of popping elements reduce O(n) complexity per each pop, instead we do a O(1) operation
def slightly_faster_merge(a, b):
    num_of_swaps = 0
    c = []
    idx_a = 0
    idx_b = 0

    while idx_a < len(a) and idx_b < len(b):
        if (a[idx_a] > b[idx_b]):
            num_of_swaps += len(a) - idx_a
            c.append(b[idx_b])
            idx_b += 1
        else:
            c.append(a[idx_a])
            idx_a += 1
            
    if idx_a < len(a):
        c.extend(a[idx_a:])
    else:
        c.extend(b[idx_b:])
    
    return c, num_of_swaps
## Classical merge sort with counter
def mergesort(arr):
    if (len(arr) == 1):
        return arr, 0
    middle_idx = len(arr) // 2
    first_half = arr[:middle_idx]
    second_half = arr[middle_idx:]
    
    first_half, num_swaps_1 = mergesort(first_half)
    second_half, num_swaps_2 = mergesort(second_half)
    
    merged, num_swaps = merge(first_half, second_half)
    return merged, num_swaps + num_swaps_1 + num_swaps_2

# Complete the countInversions function below.
def countInversions(arr):
    already_sorted = True

    for i in range(len(arr)-1):
        if (arr[i] > arr[i+1]):
            already_sorted = False
            break
    if already_sorted:
        return 0

    sort, num_of_swaps = mergesort(arr)
    print(sort)    
    return num_of_swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
