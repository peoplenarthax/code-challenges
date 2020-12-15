#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    too_chaotic = False
    num_bribes = 0
    
    for i in range(len(q)):
        # Only can bribe forward, so positions with a difference of 3 from original are not possible
        if (q[i]-1)-i >= 3:
            too_chaotic = True
            break
        # Brute force difference between index and distance 2    
        for j in range(max(0, q[i] - 2),i):
            print("J:" + str(j))
            if q[j] > q[i]:
                num_bribes+=1    

    print("Too chaotic" if too_chaotic else str(num_bribes))        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
