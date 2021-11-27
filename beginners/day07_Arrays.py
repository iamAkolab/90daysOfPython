# Arrays
# A type of data structure that stores elements of the same type 
# You can think of an array, A , of size  N as a contiguous block of cells sequentially indexed from 0 to  1 
# which serve as containers for elements of the array's declared data type

# You can think of an array, , of size  as a contiguous block of cells sequentially indexed from  to  
# which serve as containers for elements of the array's declared data type

# Python program to demonstrate
# Creation of Array
 
# importing "array" for array creations
import array as arr
 
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
 
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
 
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
    
# -------------------------------------------------
# PracticePythonBasic Data TypesLists
# -------------------------------------------------- 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    #reverse the list 'arr' by using reversed function
    a= list(reversed(arr))
 
    #for loop for printing reverse of input
    for x in a:
       print(x, end=' ')
