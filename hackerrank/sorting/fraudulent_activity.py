#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

def get_median(count, size):
    count_sort_acc = count[0]

    median_idx = 1
    while count_sort_acc <= size:
		# Update the possible index for the median
        median_high = median_idx
        if count_sort_acc < size:
			# We update the lower boundary with the previous value in the count sort
            median_low = median_idx

        count_sort_acc += count[median_idx]
        median_idx += 1

	# If odd, middle idx, otherwise value in between
    if size % 2:
        return median_high
    else:
        return (median_high + median_low) / 2    


def activityNotifications(expenditure, d):
    median_idx = d // 2
    max_value = max(expenditure)
    total_alerts = 0
	# Count occurrences of numbers within the window queue
    count = [0] * (max_value+1) 
	# Window of days to keep track of the array to sort for the median
    window = deque([])

    for expendidure_idx in range(len(expenditure)):
        if expendidure_idx >= d:   
			# Using Counting Sort, it is easier to keep track of the count on each element so complexity is smaller than resorting the trailing array
            median = get_median(count, median_idx)

            if expenditure[expendidure_idx] >= 2 * median:
                total_alerts += 1

            count[window.popleft()] -= 1
                 
        count[expenditure[expendidure_idx]] += 1
        window.append(expenditure[expendidure_idx])  

    return total_alerts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
