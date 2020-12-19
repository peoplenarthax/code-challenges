#!/bin/python3

import math
import os
import random
import re
import sys

def get_number_of_production(machines, days):
    total = 0

    for machine in machines:
        total += days // machine

    return total    

def minTime(machines, goal):
    machines.sort()

    fastest_machine = machines[0]
    slowest_machine = machines[-1]
    
	# How many days it will take with the fastest machine pace in all machines
    min_days = goal // (len(machines) / fastest_machine)
	# How many days it will take with the slowest machine pace in all machines
    max_days = (goal //  (len(machines) / slowest_machine)) + 1

	# Binary search between both boundaries
    while min_days < max_days:
        middle_days = (max_days + min_days) // 2
		# Get how much can they produce in the given days
        total = get_number_of_production(machines, middle_days)

		# If we produce more than the goal, we adjust upper boundary
        if total >= goal:
            max_days = middle_days
		# Otherwise we adjust lower
        elif total < goal:
            min_days = middle_days + 1

    return int(min_days)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
