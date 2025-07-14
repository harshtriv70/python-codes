# opening file using with statement which 
# is best for read or writing file as we do not have to close() a file every time 

with open("file.txt") as f:
    print(f.read())
