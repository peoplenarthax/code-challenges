#!/bin/python3

import os
import sys
from collections import deque


def create_cumulative_queue(array):
    new_queue = []

    cumulative = 0
    for index in range(len(array) -1, -1, -1):
        cumulative += array[index]
        new_queue.append(cumulative)
    return new_queue    
	
def equalStacks(h1, h2, h3):
    h1 = create_cumulative_queue(h1)
    h2 = create_cumulative_queue(h2)
    h3 = create_cumulative_queue(h3)

    while len(h1) > 0 and len(h2) > 0 and len(h3) > 0 and not (h1[-1] == h2[-1] and h1[-1] == h3[-1]):
        if (h1[-1] >= h2[-1] and h1[-1] >= h3[-1]):
            h1.pop()
        elif (h2[-1] >= h1[-1] and h2[-1] >= h3[-1]):
            h2.pop()
        else:
            h3.pop()
            
    return h1[-1] if len(h1) > 0 and len(h2) > 0 and len(h3) > 0 else 0        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
