#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    num_swaps = 0
    is_sorted = True

	# This check avoids O(n^2) computation in case array already sorted 
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            is_sorted = False
     
    if not is_sorted:        
		# Classical bubble sort
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if(a[j] > a[j+1]):
                    a[j], a[j+1] = a[j+1], a[j]
                    num_swaps += 1
                    
    print("Array is sorted in " + str(num_swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
