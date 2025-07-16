# divide a number and if the remainder is infinite then print infinite

try :
    a = int(input("enter a number : "))
    b = int(input("enter a number : "))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite")