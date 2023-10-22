# Desafio: Variáveis e loops

from turtle import *

# Variables
sides = 150
ang = 360/sides

speed(11)
shape("turtle")
pensize(6)
color("Red")

for count in range(36):
    forward(100)
    right(sides)
penup()

backward(200)

pendown()
color("Blue")
for count in range(18):
    forward(100)
    right(sides)
penup()

left(100)
forward(200)

pendown()
color("Green")
for count in range(32):
    forward(100)
    right(sides)
    forward(50)
done()