#  Bubble Sort.
"""


"""

# ========================== #
#         Solution           #
# ========================== #
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    
    j = 1
    i = 0
    swap = []
    for i in range(n):
        currentSwaps = 0
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap.append(a[i])
                currentSwaps += 1
        if currentSwaps == 0:
            break
          
    print("Array is sorted in",len(swap),"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
    
 """"

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    totalSwaps = 0
    
    for i in range(0, n-1):
        for i in range (0, n - 1):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                totalSwaps +=1
    
    print("Array is sorted in {} swaps.".format(totalSwaps))
    print("First Element:",a[0])
    print("Last Element:",a[2])
    
   """
