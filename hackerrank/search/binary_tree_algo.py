#!/bin/python3

import os
import sys

# Cheating a bit with the stack size, otherwise reimplement in iterative way should be easy
sys.setrecursionlimit(1500)

# We mutate indexes so we save the time of making a copy of the indexes array
def swap(indexes, swap_at_depth):
    def swap_recursion(current, depth,):
        if current == -1:
            return
        
        # The actual swap
        if depth % swap_at_depth == 0:
            values = indexes[current - 1]
            indexes[current - 1] = [values[1], values[0]]
        
        swap_recursion(indexes[current - 1][0], depth + 1)
        swap_recursion(indexes[current - 1][1], depth + 1)
        
    swap_recursion(1, 1)    

# We can do traversion in this way because of the nodes being ordered and being a binary treee
# That means that we can calculate the index where the left and the right nodes are
def travers(current, depth, indexes):
    return_value = []
    
    # Base case, nodes with -1 mean that the branch ends there
    if current == -1:
        return return_value
    
    # Get left side node traverse
    left = travers(indexes[current - 1][0], depth + 1, indexes)
    # Get right side node traverse 
    right = travers(indexes[current - 1][1], depth + 1, indexes)
    
    # In-Order traverse -> Left, root, right, we destruct left and right
    return [*left, current, *right]

# Complete the swapNodes function below.
def swapNodes(indexes, queries):
    result = []

    for query in queries:
        swap(indexes, query)
        # Pass info of the root node
        result.append(travers(1, 1, indexes))

    return result;
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
