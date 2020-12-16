#!/bin/python3

import math
import os
import random
import re
import sys

def luckBalance(k, contests):
    # Descending sort
    sorted_contests = sorted(contests, key= lambda x: (x[1], x[0]), reverse=True)
    luck = 0

    for contest in sorted_contests:
        # In case is not an important tournament just add
        if contest[1] == 0:
            luck += contest[0]
        # If they are important we only lost the ones that maximixe the luck (aka more important) 
        elif k > 0:
            luck += contest[0]
            k -= 1
        # Remove the luck from the ones that we are enquired to win
        else:
            luck -= contest[0]

    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
