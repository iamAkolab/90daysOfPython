# Abstraction
# This is an essential feature of object-oriented programming. In essense, it's the separation between what a class does and how it's accomplished.

# One real world example of this concept is a snack machine, where you give the machine money, make a selection, and the machine dispenses the snack. 
# The only thing that matters is what the machine does (i.e.: dispenses the selected snack); 
# you can easily buy a snack from any number of snack machines without knowing how the machine's internals are designed (i.e.: the implementation details).

# Abstract Class
# This type of class can have abstract methods as well as defined methods, but it cannot be instantiated (meaning you cannot create a new instance of it). 
# To use an abstract class, you must create and instantiate a subclass that extends the abstract class.
# Any abstract methods declared in an abstract class must be implemented by its subclasses (unless the subclass is also abstract).

# Objective

# Today, we will extend what we learned yesterday about Inheritance to Abstract Classes. 
# Because this is a very specific object oriented concept, submissions are limited to the few languages that use this construct. 

# Task
# Given a Book class and a Solution class, write a MyBook class that does the following:

# Inherits from Book
# Has a parameterized constructor taking these  parameters:
# string title
# string author
# int price

# Implements the Book class' abstract display() method so it prints these  lines:
# Title, a space, and then the current instance's .
# Author, a space, and then the current instance's .
# Price, a space, and then the current instance's .

# Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.: public) when declaring MyBook or your code will not execute.

# Input Format

# You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook class constructor (passing it the necessary arguments). It then calls the display method on the Book object.

# Output Format

# The void display  method should print and label the respective , , and  of the MyBook object's instance (with each value on its own line) like so:

# Title: $title
# Author: $author
# Price: $price
# Note: The  is prepended to variable names to indicate they are placeholders for variables.

# Sample Input

# The following input from stdin is handled by the locked stub code in your editor:

# The Alchemist
# Paulo Coelho
# 248

# Sample Output

# The following output is printed by your display() method:

# Title: The Alchemist
# Author: Paulo Coelho
# Price: 248
