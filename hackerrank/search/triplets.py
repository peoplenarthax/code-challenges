#!/bin/python3

import math
import os
import random
import re
import sys

def triplets(a, b, c):
	# We create a set because we want to count unique triplets, sorte ascendent order
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
	# Indexes are declared outside, given that we are going in ascendent order, we know that numbers that fulfil the condition for b0, will also be valid for b1
	# This is the main mechanism to save loops
    a_index = 0
    c_index = 0
    
    total = 0
    
	# For each value of b
    for i in range(len(b)):
		# If we find a value of a that is lower or equal to b, we add it to the count, otherwise proceed to count triplets
        while a_index < len(a) and a[a_index] <= b[i]:
            a_index += 1
        
        while c_index < len(c) and c[c_index] <= b[i]:
            c_index += 1
        
		# We want to count all posible combinations of c numbers with a numbers with only 1 b number per cycle
        total += a_index * c_index
    
    return total  

def slow_triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))

    total_count = 0
    for i in range(len(b)):
        val = b[i]
    
        count_a = 0
        for i in range(len(a)):
            if val < a[i]:
                break
            count_a += 1
        count_c = 0    
        for i in range(len(c)):
            if val < c[i]:
                break
            count_c += 1
        
        total_count += count_a*count_c
    
    return total_count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
