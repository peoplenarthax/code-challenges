#!/bin/python3

import math
import os
import random
import re
import sys

def checkAbbr(string_a, string_b, memory):
    # if A smaller than B, we cannot replicate B
    if len(string_a) < len(string_b):
        return False
    # if B is empty, it is only true if A is lowercase or empty
    if len(string_b) == 0:
        if len(string_a) == 0 or string_a.islower():
            return True
        else:
            return False
    
    # Check memory
    if (string_a, string_b) in memory:
        return memory[(string_a, string_b)]
    
    # if the last letter is equal, we check for the next substring without it
    if string_a[-1] == string_b[-1]:
        memory[(string_a, string_b)] = checkAbbr(string_a[:-1], string_b[:-1], memory)
        return memory[(string_a, string_b)]
    
    # if A has an uppercase letter that B doesn't, it is false
    if string_a[-1].isupper():
        return False    
    else:
        # We check removing the last letter
        if string_a[-1].upper() != string_b[-1]:
            memory[(string_a, string_b)] = checkAbbr(string_a[:-1], string_b, memory)
        else:
            # We check with both uppercase and lowercase last letter
            memory[(string_a, string_b)] = checkAbbr(string_a[:-1]+string_a[-1].upper(), string_b, memory) or checkAbbr(string_a[:-1], string_b, memory)

    return  memory[(string_a, string_b)]

def abbreviation(a, b):
    memory = {}
    return 'YES' if checkAbbr(a, b, memory) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
