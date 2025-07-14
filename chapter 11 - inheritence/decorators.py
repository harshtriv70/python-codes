# # class method
# class employee:
#     num = 1

#     @classmethod
#     def show(cls):
#         print(f"The class attribute of num is {cls.num}")

#     # e = employee()
#     # e.num = 45234
#     # e.show()

#     # property decorator
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"

#     @name.setter
#     def name (self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = employee()
# e.num = 45234
# e.show()

# e.name = "Harsh Trivedi"
# print(e.lname)



class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            print("Name is too short!")
        else:
            self._name = value

s = Student("Harsh")
s.name = "A"     # Prints: Name is too short!
s.name = "Arjun" # Updates the name
print(s.name)    # Prints: Arjun

