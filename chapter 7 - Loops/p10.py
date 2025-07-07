# print table in reversed order 
num = int(input("Enter a number you want table of : "))

for i in range(1,11):
    print(f"{num} X {11-i} = {num*(11-i)}")
    
    #beacuse here sum of all num are 11 so just used simple logic to reverse
    # 1 10 = 11
    # 2 9 = 11
    # 3 8 = 11
    # 4 7 = 11
    # 5 6 = 11