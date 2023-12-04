import sys
import random 
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    # different ways to access value on Enum class
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    userchoice = input('\nMake a choose:\n 1-for Rock\n 2-for Paper\n 3-for Scissors:\n\n')

    player = int(userchoice)

    if player < 1 | player > 3:
        sys.exit('You must enter 1,2 or 3')

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print('\nYou chose ' + str(RPS(player)).replace('RPS.','') + '.')
    print('Python chose ' + str(RPS(computer)).replace('RPS.','') + '.\n')
    

    if player == 1 and computer == 3 :
        print('🍾You win')
    elif player == 2 and computer == 3 :
        print('🍾You win')
    elif player == 3 and computer == 2 :
        print('🍾You win')
    elif player == computer :
        print('😲Tie game')
    else :
        print('🐍Phyton win')

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\nCelebrate")
        print("Thank you for playing")
        playagain = False

sys.exit("Bye")


