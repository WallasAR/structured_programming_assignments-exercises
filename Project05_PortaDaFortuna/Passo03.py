# Passo 03: Quanta sorte você tem?

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

score = 0
attempts = 0

while score < 3:

    attempts += 1
    print(f"Attempts: {attempts}\nEscolha uma porta (1, 2 or 3):")
    
    #get the chosen door and store it as an integer (whole number)
    chosenDoor = int(input())

    #randomly choose the winning door number (between 1 and 3)
    winningDoor = randint(1,3)

    #show the player the winning and chosen door numbers
    print("A porta escolhida foi ", chosenDoor)
    print("A porta certa é a ", winningDoor)

    #player wins if the chosen door and winning door number are the same
    if chosenDoor == winningDoor:
        score += 1
        print(f"Parabéns")
    else:
        print("Que pena!")

print(f"You did it! finished the game in {attempts} attempts")
