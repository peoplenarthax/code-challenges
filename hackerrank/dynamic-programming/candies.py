#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candyRewards = [1] * len(arr)

    # Pass to the right, increasing candies by one as we encounter incremental cases
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            candyRewards[i] = candyRewards[i - 1] + 1
    
    # Pass tothe left, we only increase counter if the reward for the previous one is the same and the previous count is smaller
    for i in range(len(arr) - 2, -1, -1):
        if (arr[i] > arr[i+1]) and (candyRewards[i] <= candyRewards[i + 1]):
                candyRewards[i] = candyRewards[i + 1] + 1 
     
    return sum(candyRewards)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()