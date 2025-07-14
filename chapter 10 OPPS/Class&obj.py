
class Employee:   #this is an class (which act as an blueprint)

    age = 22               #this are attributes of class employee
    salary = 1200000       #this are attributes of class employee
    lang = "py"            #this are attributes of class employee


# giving a object an class as harsh is emp
Harsh = Employee()     
Harsh.name = "Harsh Trivedi"   # This is an Instance(object) attribute 
print(Harsh.name,Harsh.salary, Harsh.lang )

Rudra = Employee()
Rudra.name = "Rudra Roro"    # This is an Instance(object) attribute 
print(Rudra.name, Rudra.age,Rudra.lang)

# Here name is Instance(object) attribute and salary & languages are class attribute as they belong to the class employee class

rohan = Employee()
rohan.lang = "Java"   # here instance attribute get higher preference than class attributes 
print(rohan.lang)
print(Employee.lang)