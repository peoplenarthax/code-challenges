#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, prices):
    sorted_prices = sorted(prices, reverse=True)

    cost = 0

	# Best strategy is everyone buys the most expensive flowers and then the next cheapest and so on and so forth
    for i in range(len(sorted_prices)):
        cost += sorted_prices[i]*(1+ i // k)

    return cost    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
