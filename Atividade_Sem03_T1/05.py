# 05. No próximo final de semana seu time de futebol entrará em campo. Escreva um programa que leia o seu nível de
# empolgação para a partida, um número inteiro entre 1 e 10, e mostre a empolgação do lado de fora do estádio
# representando por letras “O” ao gritar GOL. Por exemplo:
# Empolgação nível 1 >>> Gol!
# Empolgação nível 5 >>> Goooool!

empolg = int(input("Qual o seu nível de empolgação? "))

print("G" + "o"*empolg + "l!")