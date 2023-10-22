# Desafio: Desenhando padrões

from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("Red")

for count in range(36):
    forward(100)
    right(100)
penup()

backward(200)

pendown()
color("Blue")
for count in range(18):
    forward(100)
    right(200)
penup()

left(100)
forward(200)

pendown()
color("Green")
for count in range(32):
    forward(100)
    right(50)
    forward(50)
done()
