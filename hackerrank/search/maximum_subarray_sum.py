#!/bin/python3

import math
import os
import random
import re
import sys

def maximumSum(a, m): 
    if len(a) == 0:
        return 0
    # prefix sum keeps: 
    # 0 - the sum of the current + previous term modularized by m
    # 1 - the index
    prefix_sum = [(a[0] % m, 0)]
    # current max sum
    max_sum = prefix_sum[0][0]
    for i, value in enumerate(a[1:], 1):
        previous_sum = (prefix_sum[-1][0] + value) % m
        prefix_sum.append((previous_sum, i))

        # Save maximum term
        if previous_sum > max_sum:
             max_sum = previous_sum
    
    # If one of the terms is already the maximum modular value, stop
    if (max_sum == m - 1):
        return max_sum
    
    # Sort by prefix_sum descendant order
    prefix_sum = sorted(prefix_sum, reverse=True)
    # Now what we are looking is for the maximum difference between 2 consecutive terms
    # where the smaller value is assigned to a bigger position 
    # When value at j is smaller than at i means that a multiple of the module m
    # has been added, and we are looking for those additions
    # https://www.quora.com/What-is-the-logic-used-in-the-HackerRank-Maximise-Sum-problem
    for i, value in enumerate(prefix_sum[:-1]):
        mod_sum_next, index_next = prefix_sum[i+1]
        if index_next > value[1]:
            candidate = (mod_sum_next - value[0]) % m
            if candidate > max_sum:
                max_sum = candidate
                # If one of the terms is already the maximum modular value, stop
                if (max_sum == m - 1):
                    break
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
