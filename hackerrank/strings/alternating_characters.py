#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    last_character = s[0]
    deleted_characters = 0
    for i in range(1, len(s)):
        if s[i] == last_character:
            deleted_characters += 1
        else:
            last_character = s[i]
            
    return deleted_characters        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
