# When we talk about storing multiple values in a container-like data structure, the first thing that comes to mind is a list.

# You can initialize a list as:

arr = list()
# or simply
arr = []

#Lists in Python are very versatile. You can add almost anything in a Python list.
# In Python, you can create a list of any objects: strings, integers, or even lists. 
# You can even add multiple types in a single list!

# Let's look at some of the methods you can use on list.

arr = [1,2,3]

# 1.) append(x) Adds a single element x to the end of a list.
arr.append(9)   
print arr 
# prints [1, 2, 3, 9]

# 2.) extend(L) Merges another list L to the end.
arr.extend([10,11])
print arr
# prints [1, 2, 3, 9, 10, 11]

# 3.) insert(i,x) Inserts element x at position i.
arr.insert(3,7)
print arr
# prints [1, 2, 3, 7, 9, 10, 11]

# 4.) remove(x) Removes the first occurrence of element x.
arr.remove(10)  
arr  
# prints [1, 2, 3, 7, 9, 11]

# 5.) pop() Removes the last element of a list. If an argument is passed, that index item is popped out.
temp = arr.pop()
print temp 
# prints 11

# 6.) index(x) Returns the first index of a value in the list. Throws an error if it's not found.
temp = arr.index(3)
print temp
# prints 2

# -------------------------------------------------
# PracticePythonBasic Data TypesLists
# --------------------------------------------------
if __name__ == '__main__':
    N = int(input())
    
    user_array = [];
    
    for i in range(0,N):
        user_input = input().split();
        
        # user types insert
        if user_input[0] == "insert":
            user_array.insert(int(user_input[1]), int(user_input[2]))
        
        # user types print
        elif user_input[0] == "print":
            print(user_array)
            
        # user types remove
        elif user_input[0] == "remove":
            user_array.remove(int(user_input[1]))
            
        # user types append
        elif user_input[0] == "append":
            user_array.append(int(user_input[1]))
            
        # user types sort
        elif user_input[0] == "sort":
            user_array.sort()
        
        # user types pop
        elif user_input[0] == "pop":
            user_array.pop()
        
        # user types reverse
        else :
            user_array.reverse()       
