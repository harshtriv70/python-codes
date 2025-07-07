#create function to find greatest of three number : 
def greatest(num1,num2,num3):
    if(num1 > num2 and num1 > num3):
        print(f"{num1} is greatest ")
    
    elif(num2 > num1 and num2 > num3):
        print(f"{num2} is greatest ")

    else : 
        print(f"{num3} is greatest")

n1 = int(input("enter num : "))
n2 = int(input("enter num : "))
n3 = int(input("enter num : "))
greatest(n1,n2,n3)