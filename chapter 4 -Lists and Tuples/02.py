# write a program to take marks of 5 student and display them in sorted manner 
marks= []
take = input("Enter marks of student 1: ")
marks.append(int(take))
take = input("Enter marks of student 2: ")
marks.append(int(take))
take = input("Enter marks of student 3: ")
marks.append(int(take))
take = input("Enter marks of student 4: ")
marks.append(int(take))
take = input("Enter marks of student 5: ")
marks.append(int(take))

print("Marks before sorting:", marks)
print("Marks after sorting :", sorted(marks))

#using for loop 
# marks = []
# for i in range(5):
#     take = input(f"Enter marks of student {i+1}: ")
#     marks.append(int(take))
# print("Marks before sorting:", marks)
# print("Marks after sorting :", sorted(marks))

