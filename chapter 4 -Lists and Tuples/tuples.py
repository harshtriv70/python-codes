a = (1,2,3,True,False,"Harsh")
print(a)  
print(type(a))

# Tuples are immutable, so you cannot change their elements.
# a[0]=11 # ERROR
# print(a) # tuple value can't be changed so it will show error


# Tuple methods demonstration
b = (1, 2, 2, 2, 3, 4, 2)

# count() - returns the number of times a value appears
print("Count of 2 in b:", b.count(2))

# index() - returns the first index of a value
print("Index of 3 in b:", b.index(3))

# len() - returns the length of the tuple
print("Length of b:", len(b))

# sorted() - returns a sorted list from the tuple
print("Sorted b:", sorted(b))


mytuple = (1,2,3)
a, b, c = mytuple  # tuple unpacking
print("Unpacked values:", a, b, c)
print(c) #3