# calculator class that can find square and cube square root of a num
class cal:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The Square is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")
    
    def squareRoot(self):
        print(f"The SquareRoot is {self.n ** 0.5}")   # ** means ----> 2 ** 3 returns 8 (since 2³ = 8)

    # problem 4 adding static method to greet hello 
    @staticmethod
    def greet():
        print("howdy there myself Harsh")

n = cal(55)
n.greet(),
n.square()
n.cube()
n.squareRoot()
