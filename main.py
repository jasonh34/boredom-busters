#TODO: Everything
#Tried putting minigames.py and rockPaperScissors.py into a folder, but I was having trouble, 
#so this project is currently directory systemless.

#import modules
import random
import time
import minigames

#start game
def start():
    print("Welcome to Boredom Busters! Presenting text-based Python minigames!")
    time.sleep(1)
    input("Press enter to start!")

    #Loading "animation"
    for i in range(3):
        print(".",end="")
        time.sleep(0.5)

    print("Game Start!")
    minigames.gameCycle()
    print("Game End!")

        

if __name__ == "__main__":
    start()