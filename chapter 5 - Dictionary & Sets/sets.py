## Sets :
# empty_set = set()
# print(type(empty_set))


# sets methods : 
s = {11,2,3,5,5}
# s.add(4)
# s.clear()
# print(len(s))
# s.remove(1)
# s.pop()
# print(s)
s = {"banana", "apple", "cherry", "grape"}
print(s)  # This proves it's unordered, because this order is neither sorted nor inserted.

##SOME MATHEMATICAL OPERATIONS :
s1 = {1,4,5,6,7}
s2 = {1,11,2,3,5,8,9}
print(s1.union(s2))  #this removes common in both sets and prints 
print(s1.intersection(s2))  #takes the common in both set and prints 
print({1,2}.issubset(s1))
print({1,2}.issubset(s2))



