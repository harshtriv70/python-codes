# write class vector representing a vector of n dimensions. overload the + and  * operators
#  which will calculate the sum and (.) product of them.

# Define a class 'vector' to represent 3D vectors and perform vector operations
class vector:
    # Initialize vector with x, y, z coordinates
    def __init__(self, x ,y ,z):
        self.x = x
        self.y = y
        self.z = z

    # Overload + operator to add two vectors
    def __add__(self,other):
        result = (self.x + other.x,self.y + other.y,self.z + other.z)
        return result

    # Overload * operator to calculate dot product of two vectors
    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    # String representation of vector for printing
    # Returns vector coordinates as string
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"


# Create two vector objects
a = vector(2,4,5)
b = vector(1,2,3)

# Print vector addition result using overloaded + operator
print(a+b)
# Print dot product result using overloaded * operator
print(a*b)