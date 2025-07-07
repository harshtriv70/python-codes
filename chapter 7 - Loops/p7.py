#write a program to print the star pattern :
'''
n = 3
  *
 ***
*****
'''
n = int(input("Enter a number : "))
for i in range(1,n+1):
    print(" " * (n-i), end="")
    print("*" * (i*2-1), end="")
    print("")