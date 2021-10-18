# Task
# Given a base- integer, , convert it to binary (base-). 
# Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. 
# When working with different bases, it is common to show the base as a subscript.

"""
while(n > 0):
    remainder = n%2;
    n = n/2;
    Insert remainder to front of a list or push onto a stack

Print list or stack
"""

# ========================
#         Solution
# ========================

#!/bin/python3


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    user_input = int(input().strip())

    array_remainder = []
    
    while user_input > 0:
        remainder = user_input % 2
        user_input = user_input//2
        array_remainder.append(remainder)
    
    count,result = 0,0
    
    for i in range(0,len(array_remainder)):
        if array_remainder[i] == 0:
            count = 0
        else:
            count +=1
            result = max(result,count)
    
    print(result)
