# write a multiplication table of a given number using for loop:
num = int(input("Enter a number you want table of : "))
for i in range(10):
    print(f"{num}*{i+1}={(i+1)*num}")
    # i += 1

'''
Out put : 
Enter a number you want table of : 2
2*1=2
2*2=4
2*3=6
2*4=8
2*5=10
2*6=12
2*7=14
2*8=16
2*9=18
2*10=20
'''