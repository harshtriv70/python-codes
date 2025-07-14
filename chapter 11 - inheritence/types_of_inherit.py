'''
single inheritance
    BASE CLASS
        |
        V
    DERIVED CLASS
'''
class employee:                    #so this is parent class means base class
    pass

class programmer(employee):       # and this is child class which inherits the methods and properties of base class
    pass

'''
Multiple inheritance
 PARENT 1   PARENT 2
         |
         V
    CHILD CLASS
'''

class employee:
    pass

class coder:
    pass

class programmer(employee,coder):
    pass

'''
Multi level inheritance
      PARENT
         |
         V
      CHILD 1
         |
         v
      CHILD 2
'''

class parent:
    a = 1

class child(parent):
    b = 2

class grandchild(child):
    c = 3

o = parent()
print(o.a)

o = child()
print(o.a, o.b)

o = grandchild()
print(o.a, o.b , o.c)
