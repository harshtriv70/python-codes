from random import randint

class train:
    def __init__(self,traino):
        self.traino = traino

    def book(self,fro,to):
        print(f"ticket is booked for train number {self.traino} from {fro} to {to} ")
    
    def getstatus(self):
        print(f"ticket is booked for train number {self.traino} is running ")
    
    def getfare(sf,fro,to):
        print(f"ticket fare for train number {sf.traino} from {fro} to {to} is {randint(229,499)} ")


t = train(12312)
t.book("Kol","Ftp")
t.getstatus()
t.getfare("Kol","Ftp")
