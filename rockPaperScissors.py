#Rock paper scissors
import time
import random

def rps(minigames = False):
    playerScore = 0
    computerScore = 0
    rounds = 0
    print("Lets play rock paper scissors!")
    for i in range(5):
        print("\nRound", rounds)

        computer = random.randint(1, 3)
        if computer == 1:
            computerChoose = "rock"
        elif computer == 2:
            computerChoose = "paper"
        elif computer == 3:
            computerChoose = "scissors"

        player, playerChoose = getRpsInput()
        
        print("Player chose", playerChoose)
        print("Computer chose", computerChoose)

        time.sleep(1)

        #1 == rock, 2 == paper, 3 == scissors
        #higher numbers are better as rock < paper < scissors
        #however at the endpoints (1 and 3), direct comparisons are needed.
        if player == computer:
            print("Its a tie!")
        elif player == 1 and computer == 3:
            print("Player wins!")
            playerScore += 1
        elif player == 3 and computer == 1:
            print("Computer wins!")
            computerScore += 1
        elif player > computer:
            print("Player wins!")
            playerScore += 1
        elif player < computer:
            print("Computer wins!")
            computerScore += 1
        rounds += 1
    
    print("\nEnd of rock paper scissors!")
    time.sleep(1)
    print("\nPlayer got", playerScore, "points!")
    print("Computer got", computerScore, "points!\n")
    time.sleep(1)
    if computerScore == playerScore:
        print("It's a tie!")
    elif computerScore > playerScore:
        print("Computer wins!")
    else:
        print("Player wins!")
    
    #Returns if player has won if part of minigames
    if minigames == True:
        return playerScore > computerScore

#Get input from player for Rock paper scissors,
#Returns valid input as an integer 
def getRpsInput():
    while True:
        player = input("\nChoose 'r'ock, 'p'aper, or 's'cissors! ").lower()
        if (player == "r"):
            return 1, "rock"
        elif (player == "p"):
            return 2, "paper"
        elif (player =="s"):
            return 3, "scissors"
        else:
            print("Input not valid! Try again.")

#Debug or standalone rock paper scissors game
if __name__=="__main__":
    print(rps())