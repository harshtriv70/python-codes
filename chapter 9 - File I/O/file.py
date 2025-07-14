'''
file are of 2 types :
1) text file (ex : txt,.c,etc)
2) binary files (ex:.jpg, .dat, etc )

'''

#here we saw for to read a file in read mode "r" which is by default but for write we need to make it "w"
f = open("file.txt")
data = f.read()
print(data)
f.close()

#how to write in a file
st = "Hey Harsh you are really cool developer"

f = open("writefiledemo.txt", "w")

f.write(st)
for i in range(10):
    f.write("\nHow are you ")
    
f.close()

# f2 = open("file.txt", "w")  this will over write new string in existing file
# f2.write(st)

# f2 = open("file.txt", "a")  this will append new string in existing file
# f2.write(st)




##

# line = f.readline()
# while (line != ""):
#     print(line)
#     line = f.readline()

# f.close()
