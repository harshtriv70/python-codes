# write a program to check wheater a given num is prime or not 
num = int(input("Enter a number you want to check : "))
for i in range(2,num):
    if((num%i)== 0):
        print("This is not a prime")
        break
else:
    print("it is a prime num")
    