# create a class programmer for storing information of few programmers working at microsoft 
class programmer:
    company = "Microsoft"

    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age

h = programmer("Harsh",45000000,23)
print(h.name,h.age,h.company,h.salary)
r = programmer("rohan",41000000,24)
print(r.name,r.age,r.company,r.salary)
a = programmer("aman",5000000,26)
print(a.name,a.age,a.company,a.salary)