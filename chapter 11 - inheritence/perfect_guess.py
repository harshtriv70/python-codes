# This is an perfect guess game where you need to guess correct number in less attempts
import random
n = random.randint(1,100)
a = -1
g = 1
while(a != n ):
    a = int(input("Guess the number : "))
    if(a > n):
        print("Lower number please ...")
        g += 1
    elif(a < n ):
        print("Higher number please ...")
        g += 1

print(f"You guess of {n} number was correct in {g}attemps ")