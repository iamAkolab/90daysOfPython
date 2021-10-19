## Objective
## Today, we're delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video.

## Task
## You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
# Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:
"""
A Student class constructor, which has  parameters:
A string, firstName .
A string, lastName.
An integer, idNumber.
An integer array (or vector) of test scores, .
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

Input Format

The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. It also calls the calculate method which takes no arguments.

The first line contains firstName, lastName, and idNumber, separated by a space. The second line contains the number of test scores. The third line of space-separated integers describes .

Constraints

Output Format

Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O


Explanation

This student had 2 scores to average: 100 and 80 . The student's average grade is (100+80)/2 = 90. 
An average grade of 90 corresponds to the letter grade O, so the calculate() method should return the character 'O'.
"""

# ========================
#         Solution
# ========================
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    
    def __init__(self,firstName, lastName, idNum , scores):

        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores
    
    def printPerson(self):
        print("Name: " + lastName + ", " + firstName)
        print("ID:", idNum)
    
    def calculate(self):
        x = len(scores)
        n = 0
        for i in range(x):
            n+=scores[i]
        
        y = int(n)//int(x)

        if 90<= y <= 100:
            return 'O'
        elif 80<= y < 90:
            return 'E'
        elif 70<= y < 80:
            return 'A'
        elif 55<= y < 70:
            return 'P'
        elif 40<= y < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
