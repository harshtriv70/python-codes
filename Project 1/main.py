# making snake , water , gun game using python

'''
0 for water
1 for snake
2 for gun

'''
import random
computer = random.choice([0,1,2])
youstr = input("Enter your choice form S,W,G : ")
youdict = {
    "s" : 1,
    "w" : 0,
    "g" : 2
}
printdict = {
    0 : "Water",
    1 : "Snake",
    2 : "Gun"
}
you = youdict[youstr]
print(f"You chose {printdict[you]}\nComputer chose {printdict[computer]}")

if(you == computer):
    print("Its an Draw !")
else: 
    if(computer == 0 and you == 1):
        print("You won !")
    elif(computer == 0 and you == 2):
        print("You lose !")
    elif(computer == 1 and you == 0):
        print("You lose !")
    elif(computer == 1 and you == 2):
        print("You won !")
    elif(computer == 2 and you == 0):
        print("You won !")
    elif(computer == 2 and you == 1):
        print("You lose !")
    else:
        print("Ops Something wnet wrong ! ")