#!/bin/python

import math
import os
import random
import re
import sys
from collections import defaultdict

def improved_makeAnagram(a, b):
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)

    equal_letters = 0
    for i in a:
        a_dict[i] += 1
    for i in b:
        b_dict[i] += 1

    for letter in (a_dict if len(a_dict) < len(b_dict) else b_dict).keys():
		# Count coincidences instead of differences and only through the smaller array
        equal_letters += min(a_dict[letter], b_dict[letter])

    return len(a) + len(b) - equal_letters*2



def makeAnagram(a, b):
    alphabet = "abcdefghijkmnlopqrstuvwxyz"
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)
    
    diff_letters = 0
    for i in a:
        a_dict[i] += 1
    for i in b:
        b_dict[i] += 1

    for letter in alphabet:
        diff_letters += abs(a_dict[letter] - b_dict[letter])
    return diff_letters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
