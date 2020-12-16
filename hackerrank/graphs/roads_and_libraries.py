#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def create_adjacency_list(queries):
    cities = defaultdict(list)
    for query in queries:
        a, b = query
        cities[a].append(b)
        cities[b].append(a)

    return cities    

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, city_queries):
    # If libraries are cheaper than roads, the fast answer is to create a library in each city
    if c_lib <= c_road:
        return c_lib * n

    # Represent the graph in an adjacency list
    city_adjacency_list = create_adjacency_list(city_queries)

    # We know which cities exist by n, not all cities have queries
    cities = list(range(1, n + 1))
    
    # Init parameters for DFS
    visited = {}
    n_roads = 0
    n_libraries = 0

    # As long as we havent visited all the cities
    while len(visited.keys()) < n:
        root_city = None
        dfs_stack = []

        # Get a candidate for root in DFS (we pop elements from cities and check if they were visited)
        while len(cities) > 0:
            candidate = cities.pop()
            if candidate not in visited:
                root_city = candidate
                break

        # Each root needs a library since it represent a tree of connected nodes
        n_libraries += 1
        visited[root_city] = True
        dfs_stack.extend(city_adjacency_list[root_city])
        
        # Do DFS to visit all the nodes connected to the given root, in a non weighted graph is equal to Minimum Spanning Tree
        while dfs_stack and len(dfs_stack) > 0:
            next_visited = dfs_stack.pop()

            if next_visited not in visited:
                visited[next_visited] = True
                # Each visited node is a road, DFS will remove cyclical roads
                n_roads += 1
                for child in city_adjacency_list[next_visited]:
                    if child not in visited:
                        dfs_stack.append(child)
    
    return n_libraries * c_lib + n_roads * c_road                    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
