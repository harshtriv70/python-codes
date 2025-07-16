
# write a program to find the max of the number in a lsit using the reduce function
import functools as fun

def findgreater(a,b):
    if(a>b):
        return a
    return b

l = [12,345,123,34,45,23,56,77,3,2,44,2]

reduce = fun.reduce(findgreater,l)
print(reduce)
