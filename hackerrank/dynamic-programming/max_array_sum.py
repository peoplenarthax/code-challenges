#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    # Max sum without counting current value
    exclusive = 0
    # Max sum with the current value
    # Max with 0 so that if we have negative numbers they do not polute the next inclusive calc (This only happens if negative number is on the first part)
    inclusive = max(0, arr[0])

    for i in range(1, len(arr)):
        temp = inclusive
        # Our new inclusive is the maximum between previous inclusive and the previous exclusive + current number. This is because the previous exclusive now can be considered inclusive
        inclusive = max(arr[i] + exclusive, inclusive)
        exclusive = temp
        
    return inclusive

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
