#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sherlockAndAagrams function below.
def get_substrings(string):
    l = len(string)
    dict = defaultdict(int)
    for i in range(l):
        for j in range(i+1,l+1):
            # Get normalised version of the substring
            sub = sorted(string[i:j])
            # Sorted transforms into list
            sub = "".join(sub)
            # Count occurrences of normalised substring 
            dict[sub]+=1
    return dict

def sherlockAndAnagrams(s):
    substrings = get_substrings(s)

    total_anagram = 0
    for substring_count in substrings.values():
        # n! / k! * (n-k)! Applying binomial coefficient for combinations, where k is equal to 2 because we count the pairs (2) of anagrams
        # Binomial coefficient gives the total amount of combinations of k size for a sequence of size n
        # In this case, we know how many times we found the normalised anagram, so we just want to know how many combinations can we have of them eg. 1 element has 0 possible combinations of 2 different elements, 2 elements only have 1 possible combination...
        total_anagram += int((substring_count*(substring_count - 1))/2)
    return total_anagram    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()