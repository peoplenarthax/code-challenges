#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque, defaultdict

def create_adjacency_list(number_nodes, queries):
    nodes = defaultdict(list)
    for query in queries:
        a, b = query
        nodes[a].append(b)
        nodes[b].append(a)

    return nodes    
        
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
	# Represent the graph in an adjacency list (using a defaultdict we won't need to add the isolated nodes)
    adjacency_list = create_adjacency_list(graph_nodes, zip(graph_from, graph_to))

	# Create queue for BFS
    queue = deque()
    visited = {}

	# We will start BFS from all the nodes for the given colour
    for i, id in enumerate(ids):
        if id is val:
            index_node = i + 1
			# We save the origin and the distance
            visited[index_node] = (index_node, 0)
            queue.append(index_node)
    
    # BFS 
    while queue:
        current = queue.popleft()
        origin, distance = visited[current]

        for n in adjacency_list[current]:
            if n not in visited:
				# If it hasn't been visited means that we did not find a conection to the other nodes of same color, we increase distance by one
                visited[n] = (origin, distance + 1)
                queue.append(n)
            else:
				# Closed circle
                if visited[n][0] == origin:
                    continue
				# Found the adjacent nodes, total is distance from the current node to the initiator (BFS guarantees MST in non directional), + distance to the connected path	
                return distance + visited[n][1] + 1
    # No path? return -1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
