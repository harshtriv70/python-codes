# write a program to check given username contain less than 10 charecter or not :
username = input("Enter your username : ")
count = len(username)
# print(count)
if(count < 10 ):
    print("Your username is less than 10 chars")
else:
    print("Your username is not less than 10 chars")