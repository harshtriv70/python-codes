##wrtie a program to find out wheather a student has passed or failed if it requires a totlal of 40% 
# and atleat 33% in each subject and take marks as input.

mark1 = int(input("Enter subject 1 mark : "))
mark2 = int(input("Enter subject 2 mark : "))
mark3 = int(input("Enter subject 3 mark : "))
mark4 = int(input("Enter subject 4 mark : "))

total_percentage = (100*(mark1+mark2+mark3+mark4))/400

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33 and mark4>=33):
    print(f"Congrats you passed with {total_percentage} %")
else : 
    print(f"Sorry you failed with {total_percentage}%")