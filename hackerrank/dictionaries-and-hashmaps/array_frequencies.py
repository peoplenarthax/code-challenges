#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    # Key: Frequency, Value: number of numbers with that frequency
    frequencies = defaultdict(int)
    # Key: Numbers, Value: Frequency
    numbers = defaultdict(int)
    answers = []

    for (operation, number) in queries:
        # Adding a number
        if operation == 1:
            numbers[number] += 1
            # The new frequency increments by 1, the old one decreases
            frequencies[numbers[number]] += 1
            frequencies[numbers[number] - 1] -= 1
        # Removing a number    
        elif operation == 2:
            frequency = numbers[number]
            # Avoiding negative frequencies
            if frequency > 0:
                # The current frequency reduces by 1, the one below increases by one
                frequencies[numbers[number]] -= 1
                frequencies[numbers[number]-1] += 1
                
                numbers[number] -= 1
        elif operation == 3:
            # O(1) operation to look up if a frequency exist
            answers.append(1 if frequencies[number] > 0 else 0)

    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
