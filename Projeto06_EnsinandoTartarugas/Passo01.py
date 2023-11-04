# Etapa 01: Desenhando estrelas

from turtle import *

# Isso vai desenhar uma estrela cinza clara em um fundo azul escuro

color("WhiteSmoke")
bgcolor("MidnightBlue")

pendown()
begin_fill()

# Desenha a forma da estrela
for side in range(5):
    left(144)
    forward(50)

end_fill()
penup()

forward(100)
done()

