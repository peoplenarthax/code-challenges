#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    sorted_array = sorted(arr)
    difference = sys.maxsize

    for i in range(1, len(arr)):
        if abs(sorted_array[i] - sorted_array[i-1]) < difference:
            difference = abs(sorted_array[i] - sorted_array[i-1])
    
    return difference        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
