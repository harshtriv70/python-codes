# make a game() where user plays a game and check the high score wheather it is high or not if high then update the file hi-score.tx
import random

def game():
    print('''
            you are playing a game,
           where you will be given an random number....''')
    
    score = random.randint(1,50)
    print(f"You score is {score}..")
        
    with open("hi-score.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else :
            highscore = 0
    if(highscore < score):
        with open("hi-score.txt", "w") as f:
            f.write(str(score))
        
game()