#!/bin/python3

import math
import os
import random
import re
import sys



# Bottom up LCS implementation (passes in PyPy3)
def lcs(X , Y, length_X, length_Y): 
    # declaring the array for storing the dp values 
    L = [[None]*(length_Y+1) for i in range(length_X+1)] 
    
    # Bottom up recursive LCS
    for i in range(length_X+1): 
        for j in range(length_Y+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    return L[length_X][length_Y] 

# Complete the commonChild function below.
def commonChild(s1, s2):
    arr = {}
    def lcs(first, second, index_first, index_second):
        print(index_first, index_second)
        if (index_first, index_second) in arr:
            return arr[(index_first, index_second)]
        
        result = 0
        if index_first <= 0 or index_second <= 0:
            result = 0
        elif first[index_first - 1] == second[index_second - 1]:
            result = 1 + lcs(first, second, index_first - 1, index_second - 1)
        else:
            sub_search_1 = lcs(first, second, index_first - 1, index_second)
            sub_search_2 = lcs(first, second, index_first, index_second - 1)
            result = max(sub_search_1, sub_search_2)
        
        arr[(index_first, index_second)] = result
        return result
    
    longest_subsequence = lcs(s1, s2, len(s1), len(s2))
    
    return longest_subsequence

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
