mylist = [1,22,44,23,44]

'''
index = 0
for item in mylist:
    print(f"The items of index {index} is  {item}")
    index += 1
'''
# in simple i can use enumarate func

for index,item in enumerate(mylist):
      print(f"The items of index {index} is  {item}")