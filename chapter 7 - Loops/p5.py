#write a program to find the sum of first n natural num using while loop 
num = int(input("Enter a number : "))
i = 0
t = 0
while(i<=num):
    t += i
    i += 1  #increase i by 1 in each iteration

print(t)