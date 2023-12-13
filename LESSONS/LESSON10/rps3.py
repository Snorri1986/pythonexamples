import sys
import random 
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

        # different ways to access value on Enum class
        # print(RPS(2))
        # print(RPS.ROCK)
        # print(RPS['ROCK'])
        # print(RPS.ROCK.value)
        # sys.exit()

    playerchoice = input (
        "\nEnter... \n1 for Rock,\n2 for Paper,or \n3 for Scissors:\n\n"
    )

    if playerchoice not in ["1","2","3"]:
        print('You must enter 1,2 or 3')
        return play_rps()

    userchoice = input('\nMake a choose:\n 1-for Rock\n 2-for Paper\n 3-for Scissors:\n\n')

    player = int(userchoice)

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

    print("\nPlay again?")
    while True:
       playagain = input("\nY for Yes or \nQ to Quit\n")
       if playagain.lower() not in ["y","q"]:
           continue
       else:
           break 

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\nCelebrate")
        print("Thank you for playing")
        sys.exit("Bye")

play_rps()


