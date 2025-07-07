# write a program to calculate the factorial of a given num using for loop : 
# 5! = 1 x 2 x 3 x 4 x 5
n = int(input("Enter a number you want table of : "))

fac = 1
for i in range(1, n+1):
    fac = fac * i
    # i += 1

print(fac)