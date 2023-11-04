# Desafio: Mais funções

from turtle import *

# Define a function to draw a square
def drawSquare(sideLength):
    pendown()
    begin_fill()
    for _ in range(4):
        forward(sideLength)
        left(90)
    end_fill()
    penup()

# Define a function to draw a triangle
def drawTriangle(sideLength):
    pendown()
    begin_fill()
    for _ in range(3):
        forward(sideLength)
        left(120)
    end_fill()
    penup()

# Set the colors
color("WhiteSmoke")
bgcolor("Gray")

# Use the functions to draw a square and a triangle
drawSquare(100)
forward(200)
drawTriangle(100)

hideturtle()
done()
