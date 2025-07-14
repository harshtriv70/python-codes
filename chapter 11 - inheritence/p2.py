# create a class "pet" from class "animal" and further 
# create a class "dog " from pets , Add a method bark to clas dog

class animal:
    pass

class pets(animal):
    pass

class dog(pets):

    @staticmethod
    def bark():
        print("Bow Bow!")

dog = dog()
dog.bark()