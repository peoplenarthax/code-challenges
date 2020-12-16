#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

# Get children from certain coordinate and add children to keep track
def get_children(grid, added_children, coord_row, coord_column):
    children = []
    # Get kids to the left, all of them, this is the difference between shortes amount of cells, and shortest amount of vertical or horizontal steps
    for column in range(coord_column - 1, -1, -1):
        coord = (coord_row, column)
		# Stop counting when X founded
        if grid[coord[0]][coord[1]] == 'X':
            break
		# Don't add if already in the queue	
        if coord not in added_children:
            children.append(coord)
            added_children[coord] = True    
    # Get children to the right        
    for column in range(coord_column + 1, len(grid[0])):
        coord = (coord_row, column)
        if grid[coord[0]][coord[1]] == 'X':
            break
        if coord not in added_children:
            children.append(coord)
            added_children[coord] = True    

    # Get kids to the top
    for row in range(coord_row -1, -1, -1):
        coord = (row, coord_column)
        if grid[coord[0]][coord[1]] == 'X':
            break
        if coord not in added_children:
            children.append(coord)
            added_children[coord] = True    

    # Get children to the bottom        
    for row in range(coord_row + 1, len(grid)):
        coord = (row, coord_column)
        if grid[coord[0]][coord[1]] == 'X':
            break
        if coord not in added_children:
            children.append(coord)
            added_children[coord] = True    

    return children        

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    done = False
	# BFS stacks and queues
    added_children = defaultdict(bool)
    visited_node = defaultdict(bool)
    parent = defaultdict(tuple)

    queue = deque([(startX, startY)])
    added_children[(startX, startY)] = True

    # BFS 
    while (not done and len(queue) > 0):
        current_node = queue.popleft()
        visited_node[current_node] = True
        
        children = get_children(grid, added_children, current_node[0], current_node[1])
        for child in children:
            parent[child] = current_node
            
            if child == (goalX, goalY):
                done = True
        queue.extend(children)

	# Count steps from goal to start
    end = (goalX, goalY)
    steps = 0
    while end != (startX, startY):
        steps += 1
        end = parent[end]
    return steps    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
