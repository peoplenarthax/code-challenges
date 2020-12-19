#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
	# Simple case
    if len(s) == 1:
        return "YES"
    count_letters = Counter(s)

    counts = list(count_letters.values())
    
    count_frequencies = Counter(counts)
    
	# More than 2 frequencies is a big no
    if (len(count_frequencies) > 2):
        return "NO"
	# Only one element is compliant	
    if (len(count_frequencies)) == 1:
        return "YES"
    
	# Counting that Counter return values from bigger to smaller,
    frequencies = sorted(list(count_frequencies.keys()), reverse=True)

	# we can check if one of the 2 values is 1 once. If so, we can delete it
    if frequencies[1] == 1 and count_frequencies[frequencies[1]] == 1:
        return "YES"
    
	# If we have this case where the difference is of one element with one more value, we can remove one ocassion
    if frequencies[0] - frequencies[1] == 1:
        if count_frequencies[frequencies[0]] == 1:
            return "YES"

    return "NO"      


def first_isValid(s):
	valid = True
	delta = 0

    valid = True
    min_value = counts[0]
    delta = 0
    for i in range(1, len(counts)):
        print("Max value", min_value)
        print(abs(counts[i] - min_value))
        if abs(counts[i] - min_value) != 0:
            delta += abs(counts[i] - min_value)
            max_value = min(counts[i], min_value) 

            if delta > 1:
                valid = False
                break

	return "YES" if valid else "NO"			
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
