 #!/bin/python3

import math
import os
import random
import re
import sys

# Map for closing brackets
closing_map = {
    ")": "(",
    "}": "{",
    "]": "["
}

# Complete the isBalanced function below.
def isBalanced(s):
	# We will use a stack since we want to check that the last opened bracket is the first one to close (LIFO)
    stack = []
	# Assume balance
    balanced = True

    for bracket in  s:
        if bracket in closing_map:
			# If we have brackets in the stack and the last one is the same as the current closing
            if len(stack) > 0 and closing_map[bracket] == stack[-1]:
				# Remove it from the stack, we could make it faster without pop, but this is more readable
                stack.pop()
            else:
				# If the last opening bracket does not match, the string is not balanced
                balanced = False
                break
        else:
			# We add opening brackets
            stack.append(bracket)

	# At the end we need to check that the string is balanced and that all the opening brackets in the stack have been matched
    return 'YES' if balanced and len(stack) == 0 else 'NO'            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
