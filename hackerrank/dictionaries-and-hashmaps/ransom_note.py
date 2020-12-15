#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = {}
    possible = True
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1
    for word in note:
        if word not in magazine_dict:
            possible = False
            break
        else:
            newCount = magazine_dict[word] - 1

            if newCount < 0:
                possible = False
                break
            else:
                magazine_dict[word] = newCount
    print("No" if not possible else "Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
