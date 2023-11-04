# Etapa 03: Estrelas aleatórias

from turtle import *
from random import *

def moveToRandomLocation():
    penup()
    setpos( randint(-400, 400), randint(-400, 400))
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

bgcolor("Black")

for star in range(30):
    moveToRandomLocation()
    drawStar( randint(5,25) , "White")

hideturtle()
done()
