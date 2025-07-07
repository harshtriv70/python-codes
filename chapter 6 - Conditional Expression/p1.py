#wrtie a program to find the gratest of 4 number entered by the user :
num1 = int(input("Enter four Number : "))
num2 = int(input("Enter four Number : "))
num3 = int(input("Enter four Number : "))
num4 = int(input("Enter four Number : "))

if(num1>num2 and num1>num3 and num1>num4):
    print("num 1 is the greatest among all")

elif(num2>num1 and num2>num3 and num2>num4):
    print("num 2 is the greatest among all")

elif(num3>num1 and num3>num2 and num3>num4):
    print("num 3 is the greatest among all")

else :
    print("num 4 is the greatest among all")

