# Etapa 02: Passando dados para funções

from turtle import *

def drawStar(starSize):
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drawStar(59)

forward(109)

drawStar(30)

left(120)

forward(159)

drawStar(70)

hideturtle()
done()
