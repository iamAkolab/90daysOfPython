# Recursion

# This is an algorithmic concept that involves splitting a problem into two parts: a base case and a recursive case. 
# The problem is divided into smaller subproblems which are then solved recursively until such time as they are small enough and meet some base case; 
# once the base case is met, the solutions for each subproblem are combined and their result is the answer to the entire problem.

# If the base case is not met, the function's recursive case calls the function again with modified values. 
# The code must be structured in such a way that the base case is reachable after some number of iterations, 
# meaning that each subsequent modified value should bring you closer and closer to the base case; otherwise, you'll be stuck in the dreaded infinite loo


# ========================
#         Solution
# ========================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Base Case 
    if n == 1:
        return 1
    
    #Recursive case
    else:
       return n * factorial(n-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
