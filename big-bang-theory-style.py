
import random

userScore , systemScore = 0 , 0
gameList = ["rock","paper","scissors","lizard","spock"]

while True:
    userInput = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()

    if userInput == 'q':
        break

    if userInput not in gameList:
        print(userInput)
        continue

    # rock -> 0, paper ->1, scissors->2, lizard ->3 ,spock->4
    rand = random.randint(0,4)
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
        
    elif userInput == "rock" and computerMove == "lizard":
        print("You won!")
        userScore+=1
    elif userInput == "spock" and computerMove == "scissors":
        print("You won!")
        userScore+=1
    elif userInput == "scissors" and computerMove == "lizard":
        print("You won!")
        userScore+=1
    elif userInput == "lizard" and computerMove == "paper":
        print("You won!")
        userScore+=1
    elif userInput == "paper" and computerMove == "spock":
        print("You won!")
        userScore+=1
    elif userInput == "spock" and computerMove == "rock":
        print("You won!")
        userScore+=1
    else: 
        print("Computer wins! you lost")
        systemScore+=1

print("you won",userScore,"times !")      
print("computer won",systemScore,"times !")  

print("End of the game! goodbye")
