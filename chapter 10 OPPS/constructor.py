class Employee :
    language = "Python"
    salary = "45k"

    def __init__(self, name , salary , language):   # <-----------this are called DUNDER methods in python as ther start and end with underscore

        print("i am creating an object")   # This will be called authomaticaly when an object will be created 
        
        self.name = name
        self.salary = salary
        self.language = language   #  here we can also pass parameters or name like this



Harsh = Employee("harsh", "90k", "java")
# Harsh.language = "JavaScript"
print(Harsh.language,Harsh.name, Harsh.salary )
