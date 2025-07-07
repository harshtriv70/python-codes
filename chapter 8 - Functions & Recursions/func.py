def greet(name,end):
    # name = input("Enter you nm")
    print(f"Have a Goodday, {name}")
    print(end)
    return "Greeted Succesful....."

a = greet("Harsh","Thank you")
print(a)

#recurrsion using function finding factorial of any number!
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n=int(input("Enter a number : "))
print(f"The factorial of given number is {factorial(n)}")