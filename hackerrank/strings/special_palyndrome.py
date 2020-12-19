#!/bin/python3

import math
import os
import random
import re
import sys

def substrCount(n, s):
    total = 0
    count_sequence = 0
    prev = ''
    for index, letter in enumerate(s):
        # first increase counter for all seperate characters
        count_sequence += 1
        if index and (prev != letter):
            # Looking for patterns of special palindromes as in all characters equals except the one in the middle of the array 
            subsequence_index = 1
            while ((index-subsequence_index) >= 0) and ((index+subsequence_index) < len(s)) and subsequence_index <= count_sequence:
                # Left - Right equality 
                if s[index-subsequence_index] == prev == s[index+subsequence_index]:
                    # Add one more special string
                    total += 1
                    subsequence_index += 1
                else:
                    break
            # Reset counter
            count_sequence = 1  
        total += count_sequence            
        prev = letter
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
