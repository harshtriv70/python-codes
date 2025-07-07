## write a multiplication table of a given number using while loop:
num = int(input("Enter a number you want table of : "))
i = 1
while(i<11):
    print(f"{num} X {i} = {num*i}")
    i += 1