#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    ice_creams = {}

    chosen = []
    for i in range(len(cost)):
        complementary = money - cost[i]
        if complementary in ice_creams:
            chosen = [ice_creams[money-cost[i]], i + 1]
            break
        else:
            ice_creams[cost[i]] = i + 1

    print(*chosen)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
