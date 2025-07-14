try : 
    a = int(input("Enter a number : "))
    print(a)
except Exception as e :
    print(e)

print("Thank you ")
# this ensures that if there is any error the code should not crash or stop 
# the code will be executed till the end even if there is any error


# we can also raise the error to crash the program in critical mistakes 
# like python does not divide any number with 0
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

if(b == 0):
    raise ZeroDivisionError("abye laure program me 0 se divide nahi hota tik kar")
else:
    print(f"The division a/b is {a/b}")