# Task
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

#Example
#In the array shown above, the maximum hourglass sum is  for the hourglass in the top left corner.

#Input Format
""" There are  lines of input, where each line contains  space-separated integers that describe the 2D Array .
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Output Format
19

Print the maximum hourglass sum in A .
Explanation

A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4
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

    arr = []

    for _ in range(6):
        tmp = [int(x) for x in str(input()).split(" ")]
        arr.append(tmp)

    maximum = -9 * 7

    for i in range(6):
        for j in range(6):
            if j + 2 < 6 and i + 2 < 6:
                result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
                if result > maximum:
                    maximum = result

    print(maximum)
