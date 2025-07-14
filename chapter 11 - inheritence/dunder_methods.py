'''
Dunder Method	Triggered When You Use	               Example
__add__	                    +	                         a + b
__mul__	                    *	                         a * b
__sub__	                    -	                         a - b
__truediv__	                /	                         a / b

'''
class number:
    def __init__(self,value):
        self.value = value

    def __add__(self,num):
        return self.value + num.value
    
    def __sub__(self,num):
        return self.value - num.value
    
    def __mul__(self,num):
        return self.value * num.value

a = number(3)
b = number(4)
print(a*b)
print(a+b)
print(a-b)
