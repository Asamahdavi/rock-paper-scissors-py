
import random

userScore , systemScore = 0 , 0
gameList = ["rock","paper","scissors"]

while True:
    userInput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if userInput == 'q':
        break

    if userInput not in gameList:
        print(userInput)
        continue

    # rock -> 0, paper ->2, scissors->2
    rand = random.randint(0,2)
    computerMove = gameList[rand]
    print("Computer move", computerMove +".")

    if userInput == "rock" and computerMove == "scissors":
        print("You won!")
        userScore+=1
        
    elif userInput == "paper" and computerMove == "rock":
        print("You won!")
        userScore+=1
        
    elif userInput == "scissors" and computerMove == "paper":
        print("You won!")
        userScore+=1
        
    elif userInput == "rock" and computerMove == "scissors":
        print("You won!")
        userScore+=1
    else: 
        print("Computer wins! you lost")
        systemScore+=1

print("you won",userScore,"times !")      
print("computer won",systemScore,"times !")  

print("End of the game! goodbye")
