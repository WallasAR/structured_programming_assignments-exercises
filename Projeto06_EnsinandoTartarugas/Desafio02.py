# Desafio: Desenhando planetas

from turtle import *

# Define a function to draw a planet with size and color
def drawPlanet(size, color):
    pendown()
    fillcolor(color)
    begin_fill()
    circle(size)
    end_fill()
    penup()

# Set the colors
bgcolor("Black")

# Use the function to draw a planet
drawPlanet(100, "Cyan")  # Specify size and color for the planet

hideturtle()
done()
