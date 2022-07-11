#Will be used later

#Get number of minigames
from rockPaperScissors import rps
import random
import time

def gameCycle():
    minigameInstance = Minigames()
    while True:
        print("Starting next minigame...")
        time.sleep(1)
        minigameInstance.playGame()

class Minigames():
    def __init__(self):
        self.__playerScore = 0

    def getNumMinigames(self):
        return 1

    def playGame(self):
        game = self.selectMinigame()
        if game.getWinType() == "Boolean":
            if game.play() == True:
                self.__playerScore += 1

    def selectMinigame(self):
        number = random.randint(1, self.getNumMinigames())
        if number == 1:
            return RPSGame()

class RPSGame():
    def __init__(self):
        self.__winType = "Boolean"

    def play(self):
        return rps(True)

    def getWinType(self):
        return self.__winType

if __name__=="__main__":
    instance = Minigames()
    instance.playGame()