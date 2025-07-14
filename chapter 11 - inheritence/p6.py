# write __str__() methods to print 3d vector as follows : 
#  7i + 8j + 10k with same p5.py 

class vector:
    # Initialize vector with x, y, z coordinates
    def __init__(self, x ,y ,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        result = vector(self.x + other.x,self.y + other.y,self.z + other.z)#    <---- so here i added vector() class  
        return result

    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    # String representation of vector for printing
    # Returns vector coordinates as string
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


# Create two vector objects
a = vector(2,4,5)
b = vector(1,2,3)

print(a+b)
print(a*b)