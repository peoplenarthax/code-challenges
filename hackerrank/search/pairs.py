#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the pairs function below.
def pairs(k, arr):
    result = 0
    counter = Counter(arr)

    for i in counter:
        complement = i - k
        if complement in counter:
            result += counter[i] * counter[complement]
            
    return result        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
