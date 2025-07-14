# override len() method in problem 5 to display dimension of the vector

class vector:
    # Initialize vector with x, y, z coordinates
    def __init__(self, l):
        self.l = l

    # def __add__(self,other):
    #     result = vector(self.x + other.x,self.y + other.y,self.z + other.z)#    <---- so here i added vector() class  
    #     return result

    # def __mul__(self,other):
    #     result = self.x * other.x + self.y * other.y + self.z * other.z
    #     return result

    # String representation of vector for printing
    # Returns vector coordinates as string
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __len__(self):
        return len(self.l)


# Create two vector objects
v1 = vector([2,4,5,5,4])

print(len(v1))
# print(v1 + v2)