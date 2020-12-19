#!/bin/python3

import math
import os
import random
import re
import sys

#Fast online solution
def someone_minimumPasses(machines, workers, price, target):
    candy = 0
    invest = 0
    spend = sys.maxsize
    
    # As long as we do not hit the target
    while candy < target:
        # Calculate if enough candies to buy machines / workers (Otherwise price - candy becomes negative)
        # If not enough candies, we just add to the production with the current set up as many times as needed until can afford a new machine/worker
        passes = (price - candy) // (machines * workers)

		# if we can buy material, we do it (Greedy)
        if passes <= 0:
			# Number total of production power before acquiring machines or workers, we try have equal
			# knowing that max x * y = Z, maximum is x , y = Z/2
            production = (candy // price) + machines + workers
            half = math.ceil(production / 2)

			# We add to the group with less resources until have a number equal to the production
            if machines > workers:
                machines = max(machines, half)
                workers = production - machines
            else:
                workers = max(workers, half)
                machines = production - workers
			# We save the remaining money	
            candy %= price
			# In the next step, we will just add the new production for 1 pass when we buy
            passes = 1
        candy += passes * machines * workers

        invest += passes
		# Save the minimum between the current saving strategy (not buying new machine/worker) or using investment
        spend = min(spend, invest + math.ceil((target - candy) / (machines * workers)))

    return min(invest, spend)

# Complete the minimumPasses function below.
def minimumPasses(machines, workers, price, target):
    production = machines * workers
    saved_money = 0
    rounds = 1

    # print("machines ", machines)
    # print("workers ", workers)
    # print("We produce: ", production)

    if production >= target:
        return rounds

    while 2*production + saved_money < target:
        purchase, remain = divmod(production + saved_money, price) 
        saved_money = remain
        # print("We buy ", purchase)
        # print("We save ", saved_money)

        while purchase > 0:
            if machines == workers:
                equal_delta, extra = divmod(purchase, 2)
                machines += equal_delta + extra
                workers += equal_delta
                purchase = 0
            else:    
                diff = abs(machines - workers)
                delta = min(diff, purchase)
                if machines > workers:
                    workers += delta
                else: 
                    machines += delta    
                purchase -= delta    
        # print("machines ", machines)
        # print("workers ", workers)
        production = machines * workers
        # print("We produce: ", production)
       
        rounds += 1
        # print("Rounds ", rounds)
    
    return rounds + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
