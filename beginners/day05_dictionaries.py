# dictionary


# A dictionary is a data type which stores values in pairs. 
# For each element in the dictionary, there is a unique key that points to a value. 
# A dictionary is mutable. It can be changed.

# For example:
a_dict = {'one': 1} # Here 'one' is the key.  

# Note: The key of a dictionary is immutable. We cannot use a list as a key because a list is mutable. 
# But we can make a tuple of list and use as key.

a_dict['two'] = 2 # Adds key 'two' which points to 2
print(a_dict['one'])
# prints 1  
if 'three' in a_dict:
    # To check whether a certain string exist as a key in the dictionary  
    print(a_dict['three'])
else:  
    print("Three not there")
# prints Three not there
del a_dict['one']
# Deletes index 'one' and the value associated with it  
print(a_dict)
# prints {'two': 2}

# Note: A dictionary is unordered. So, only use the keys to navigate through the dictionary.


# -----------------------------------------
# Finding the percentage
# -----------------------------------------
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
