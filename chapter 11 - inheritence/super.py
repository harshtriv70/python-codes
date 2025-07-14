
class parent:
    def __init__(self):
        print("constructor of parent")
    a = 1

class child(parent):
    def __init__(self):
        super().__init__()              #<------ super()
        print("constructor of child")
    b = 2

class grandchild(child):
    def __init__(self):
        super().__init__()            #<------ super()      # we use super() to call parents constructor also 
        print("constructor of grand child")
    c = 3

o = parent()
print(o.a)

o = child()
print(o.a, o.b)

o = grandchild()
print(o.a, o.b , o.c)
