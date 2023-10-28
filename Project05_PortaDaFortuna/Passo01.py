# Passo 01: O que está atrás da porta

from random import *

#print the 3 doors and the game instructions
print('''
Porta da fortuna!
=========

Há um prêmio atrás de uma das 3 portas!
Adivinhe a porta correta para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')

for count in range(3):
    print("\nChoose a door (1, 2 or 3):")
    
    #get the chosen door and store it as an integer (whole number)
    chosenDoor = int(input())

    #randomly choose the winning door number (between 1 and 3)
    winningDoor = randint(1,3)

    #show the player the winning and chosen door numbers
    print("A porta escolhida foi ", chosenDoor)
    print("A porta certa é a ", winningDoor)

    #player wins if the chosen door and winning door number are the same
    if chosenDoor == winningDoor:
        print("Well done!")
    else:
        print("Unlucky!")
