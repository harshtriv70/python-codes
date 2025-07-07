# check that tuplr type cannot be changed in py 
a = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(type(a))
a[2] = 12 # This will raise a TypeError because tuples are immutable
print(a)