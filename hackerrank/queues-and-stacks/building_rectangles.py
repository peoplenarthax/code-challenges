#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def largestRectangle(buildings):
	# We save the height of the building and the first index when it appeared
    building_buffer = [[buildings[0], 0]]
	# Biggest area by default is 1 * length of buildings
    maxArea = len(buildings)
	# To make sure we calculate all areas, we add a "closing building"
    buildings.append(0)

    for building_index in range(1, len(buildings)):
        first_index = building_index
		# If a building is smaller or equal to the last building
        while len(building_buffer) > 0 and buildings[building_index] <= building_buffer[-1][0]:
			# We remove the last case from the stack and use it to evaluate the area
            last_element = building_buffer.pop()
			# We save the index because, if a previous building A was higher or equal to the current one B
			# we know that we had the current height B since the last building that was higher or equal to B
            first_index = last_element[1]

			# Calculate the area for the current height and length (otherwise we need to calculate this outside the loop)
			# We add a +1 because we know we will keep the current height at least one more building
            maxArea = max(maxArea,
                buildings[building_index] * (building_index + 1 - last_element[1])
            )
			# Calculate the area for the previous height, we know that the length of that square is current index - index when the previous height was added
            maxArea = max(maxArea, 
                last_element[0] * (building_index - last_element[1])
            )
        # We add the current building to the stack, we may update the index with one of the previous cases if the height was smaller
        building_buffer.append([h[building_index], first_index])
    
    return maxArea

# It is a brute force version of the good solution.
def slow_largestRectangle(h):
	# We keep a cumulative sum
    maxBuffer = defaultdict(int)
    maxArea = 0

    for building_index in range(len(h)):
		# If the current building is shorter
        if building_index > 0 and h[building_index] < h[building_index - 1]:
			# For every height that we saved between the current and previous
			# We calculate the area and remove the height from our cumulative sum
            for j in range(h[building_index-1], h[building_index], -1):
                maxArea = max(maxArea, maxBuffer[j]*j)
                maxBuffer[j] = 0
		# we increase the count for all the levels as long as we are increasing or keeping the height		
        for i in range(h[building_index], 0, -1):
            maxBuffer[i] += 1
	# For all the existing heights, we calculate their area
    for size in maxBuffer:
        maxArea = max(maxArea, maxBuffer[size]*size)
    
    return maxArea


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
