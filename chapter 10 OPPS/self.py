class Employee :
    language = "Python"
    salary = "45k"

    def getinfo(self) :  # <-----self-----
        print(f"The language is {self.language}. The salary is {self.salary}")
 
    @staticmethod     # <---- maens does not need any object argument
    def greet():  # why to pass the full obj for this greet so marked as a static method
        print("Good morning")

Harsh = Employee()
Harsh.language = "JavaScript"
Harsh.getinfo()
Harsh.greet()
'''
here Harsh.getinfo() means Employee.getinfo(Harsh) 
so thatsway it is asking for argument.

Harsh.greet() means Employee.greet(Harsh) so why to pass the full obj for this greet as
 it doen not need any attribute form the class so marked as a static method
'''