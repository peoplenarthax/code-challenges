#!/bin/python3

import math
import os
import random
import re
import sys

def slow_arrayManipulation(n, queries):
    intervals = [[1,n,0]]
    for query in queries:
        # low = query[0]
        # high = query[1]
        new_intervals = []
        for interval in intervals:
            # Cut out of the current interval
            if (query[0] < interval[0] and query[1] < interval[0]) or (query[0] > interval[1] and query[1] > interval[1]):
                new_intervals.append(interval)
                continue
            # Cut within an interval    
            if interval[0] <= query[0] and interval[1] >= query[1]:
                if (interval[0] == query[0]):
                    new_intervals.append([interval[0], query[1], interval[2] + query[2]])
                    new_intervals.append([query[1] + 1, interval[1], interval[2]])
                    continue
                if (interval[1] == query[1]):
                    new_intervals.append([interval[0], query[0], interval[2]])
                    new_intervals.append([query[0] +1 , interval[1], interval[2] + query[2]])
                    continue
                new_intervals.append([interval[0], query[0] - 1, interval[2]])
                new_intervals.append([query[0], query[1], interval[2] + query[2]])
                new_intervals.append([query[1] +1 , interval[1], interval[2] + query[2]])
                continue
            # Cut covers the interval    
            if interval[0] > query[0] and interval[1] < query[1]:
                new_intervals.append([interval[0], interval[1], interval[2] + query[2]])
                if (interval[1] == query[1]):
                    continue
            # Low limit in interval, high out        
            if interval[0] < query[0] <= interval[1] and query[1] > interval[1]:
                new_intervals.append([interval[0], query[0] - 1, interval[2]])
                new_intervals.append([query[0], interval[1], interval[2] + query[2]])
                continue

            # High limit inside interval    
            if interval[1] > query[1] > interval[0]:
                new_intervals.append([interval[0], query[1], interval[2] + query[2]])
                new_intervals.append([query[1] + 1, interval[1], interval[2]])
                continue
        intervals = new_intervals
        
    return max(intervals, key=lambda i: i[2])[2]

def arrayManipulation(n, queries):
    arr = [0]*n
    for query in queries:
        # Beginning of interval increments the number
        arr[query[0] - 1] += query[2]
        if query[1] != len(arr):
            # The end of the new interval substract the same it was increased
            arr[query[1]] -= query[2]   

    max_value = 0
    acc = 0
    # Calculate maximum accumulation 
    for value in arr:
        acc += value
        if acc > max_value:
            max_value = acc
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
