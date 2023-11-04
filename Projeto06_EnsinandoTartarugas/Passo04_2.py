# Etapa 04: funções dentro de funções

from turtle import *
from random import *

def moveToRandomLocation():
    penup()
    setpos( randint(-400,400) , randint(-400,400) )
    pendown()


def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

def drawGalaxy (numberOfStars):
    starColours = ["#058396","#0275A6", "#827E01"]
    moveToRandomLocation()

    for star in range(numberOfStars):
        penup()
        left( randint(-180,180) )
        forward( randint(5,20) )
        pendown()
        drawStar( 2, choice(starColours) )

def drawconstellation(numberOfStars):
    moveToRandomLocation()
    for star in range(numberOfStars-1):
        drawStar( randint(7,15) , "white")
        pendown()
        left( randint(-90,90) )
        forward( randint(30,70) )
    drawStar( randint(7,15) , "White")
    
speed(11)

bgcolor("Black")

for star in range(30):
    moveToRandomLocation()
    drawStar( randint(5,25) , "White")

for galaxy in range(3):
    drawGalaxy (40)

for constellation in range(2):
    drawconstellation(randint(4,7))

hideturtle()
done()