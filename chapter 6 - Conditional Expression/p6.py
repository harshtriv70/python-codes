#give grades tpo student acc to marks 
m1 = int(input("Enter your marks 1 : "))
m2 = int(input("Enter your marks 2 : "))
m3 = int(input("Enter your marks 3 : "))

total = (m1+m2+m3)/3

if(total>=90 and total<=100):
    print("Ex")
elif(total>=80 and total<90):
    print("A")
elif(total>=70 and total<80):
    print("B")
elif(total>=60 and total<70):
    print("C")
elif(total>=50 and total<60):
    print("D")
else :
    print("F")