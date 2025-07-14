# create a clas employee and add salary and increment properties to it :
class Employee:
    salary = 234
    increment = 20


    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment = (((salary / self.salary) - 1) * 100)
    
    ''' formula :  new salary = old salary *  (1+ increment/100)
        formula for finding increment vice versa :
                    new salary/old salary - 1 * 100 = increment
    '''

e = Employee()
print(e.salaryafterincrement)
# e.salaryafterincrement = 280
print(e.increment)  