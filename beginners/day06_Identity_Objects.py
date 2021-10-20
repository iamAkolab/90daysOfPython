"""
All the data in a Python code is represented by objects or by relations between objects. Every object has an identity, a type, and a value.

Identity
An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The is operator compares the identity of two objects; the id() function returns an integer representing its identity.
Type
An object’s type defines the possible values and operations (e.g. “does it have a length?”) that type supports. The type() function returns the type of an object. An object type is unchangeable like the identity.
Value
The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable.

ome objects contain references to other objects, these objects are called containers. Some examples of containers are a tuple, list, and dictionary. 
The value of an immutable container that contains a reference to a mutable object can be changed if that mutable object is changed. 
However, the container is still considered immutable because when we talk about the mutability of a container only the identities of the contained objects are implied.

Mutable and Immutable Data Types in Python
Some of the mutable data types in Python are list, dictionary, set and user-defined classes.
On the other hand, some of the immutable data types are int, float, decimal, bool, string, tuple, and range.

It’s time for some examples. Let’s start by comparing the tuple (immutable) and list (mutable) data types. We can define a list using square brackets [] like this: numbers = [1, 2, 3]. To define a tuple, we just need to replace the brackets with parentheses () like this: numbers = (1, 2, 3). From both data types, we can access elements by index and we can iterate over them. The main difference is that a tuple cannot be changed once it’s defined.


Indexing lists and tuples
list_values = [1, 2, 3]
set_values = (10, 20, 30)
print(list_values[0])
print(set_values[0])

Output:
1
10

Output:
1
10

[100, 2, 3]
--------------------------------------------------------------------
TypeError                         Traceback (most recent call last)
<ipython-input-2-286c46a29f5d> in <module>()
      3 list_values[0] = 100
      4 print(list_values)
----> 5 set_values[0] = 100

TypeError: 'tuple' object does not support item assignment
