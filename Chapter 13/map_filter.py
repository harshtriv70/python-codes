# map example : 
l = [1,2,3,4,5,6,7,8,9]

square = lambda x : x*x    # <------------function
 
sqlist = map(square,l)    # synatax :     map(function,list)
print(list(sqlist))   # converting into list

# filter example : 

def even(n):               # <------------function
    if ( n%2 == 0):
        return True
    return False

evenlist = filter(even,l)  # synatax :   filter(function,list)
print(list(evenlist)) # converting into list

# reduce example :
from functools import reduce
sum = lambda a,b:a+b
mul = lambda a,b : a*b

print(reduce(sum,l))  # Syntax :   reduce(function,list)
print(reduce(mul,l))

