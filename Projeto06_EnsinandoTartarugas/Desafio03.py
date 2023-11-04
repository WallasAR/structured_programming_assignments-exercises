# Desafio: Funções em toda parte

from turtle import *
import random

# Define a function to draw a cloud
def drawCloud(x, y):
    penup()
    goto(x, y)
    pendown()
    color("white")
    begin_fill()
    circle(30)
    end_fill()
    penup()

# Define a function to draw a bird
def drawBird(x, y):
    penup()
    color("Black")
    goto(x, y)
    pendown()
    right(135)
    forward(20)
    right(90)
    forward(20)
    penup()

# Set up the drawing environment
speed(11)
bgcolor("SkyBlue")

# Draw random clouds
for _ in range(10):
    x = random.randint(-400, 400)
    y = random.randint(100, 300)
    drawCloud(x, y)

# Draw random birds
for _ in range(5):
    x = random.randint(-400, 400)
    y = random.randint(-100, 200)
    drawBird(x, y)

# Hide the turtle and finish
hideturtle()
done()
