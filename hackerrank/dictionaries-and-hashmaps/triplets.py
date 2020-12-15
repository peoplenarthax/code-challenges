#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def safe_get(number, dictionary):
    if number in dictionary:
        return dictionary[number]
    else:
        return 0 

# Works perfect with ascending order, fails if an unordered array is given
# O(n) best case O(2n) worst case
def naive_countTriplets(arr, r):
    dictionary = defaultdict(int)
    for number in arr:
		# Second condition probably wrong as 3, 6, 12 is a correct triplet of radius 2 but 3 is not divisible by 2
        if number == 1 or number % r == 0:
            dictionary[number] += 1
    
    total_triplets = 0
    if r == 1:
        for number_count in dictionary.values():
            # Shorthand form of binomial coefficient knowning that k is equal to 3
            total_triplets += int(((number_count**3)-(3*number_count**2)+(2*number_count))/6)
    else: 
        for number in dictionary:
			# Get all possible combinations for the existing progression
            first_member = safe_get(number, dictionary)
            second_member= safe_get(number*r, dictionary)
            third_member = safe_get(number*(r**2), dictionary)
            total_triplets +=  first_member * second_member * third_member
    return total_triplets

# Works always O(n)
def countTriplets(arr, r):
    second_members = defaultdict(int)
    third_members = defaultdict(int)
    total_triplets = 0

    for number in arr:
		# If there were 2nd degree members, 3rd degree members add to the total triplets by the amount of previous memebers
        if number in third_members:
            total_triplets += third_members[number]
		# If number is in second memebers means we can start looking for the 3rd degree members
        if number in second_members:
            third_members[number*r] += second_members[number]
		# All number is potentially a triplet	
        second_members[number*r] += 1
    return total_triplets            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
