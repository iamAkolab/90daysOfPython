# Task
"""
The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided for you in the editor below.

Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. 
The implementation for the divisorSum(n) method must return the sum of all divisors of n.

Example
n = 25
The divisors of 25 are 1, 5, 25. Their sum is 31.
n = 20
The divisors of 20 are 1 , 2, 4, 5, 10, 20 and their sum is 42.

Input Format
A single line with an integer, n.

Constraints
1 <= n <= 1000
Output Format
You are not responsible for printing anything to stdout. The locked template code in the editor below will call your code and print the necessary output.

Sample Input

6
Sample Output

I implemented: AdvancedArithmetic
12
Explanation

The integer 6 is evenly divisible by 1, 2, 3, and 6. Our divisorSum method should return the sum of these numbers, which is 1 + 2 + 3 + 6 = 12. 
The Solution class then prints I implemented: AdvancedArithmetic on the first line, followed by the sum returned by divisorSum (which is 12) on the second line

"""
# ========================== #
#         Solution           #
# ========================== #
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        factors = 0
        for i in range(1,n+1):
            if(n % i == 0):
                factors += i
        return factors


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
