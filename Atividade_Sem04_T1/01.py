# 01. Escreva um programa que leia o valor de um raio, calcule e mostre na tela o comprimento da circunferência, a área do círculo, a área da esfera e o volume da esfera para o valor do raio lido. Mostre os valores com 6 casas decimais.

PI = 3.141592

raio = float(input("Digite o valor do raio: "))

circ = 2*PI*raio
area = PI*raio**2
areaEsf = 4*PI*raio**2
volEsf = 4/3*PI*raio**3

print(f"> Circunferência: {circ:.6f}\n> Area do circulo: {area:.6f}\n> Area da esfera: {areaEsf:.6f}\n> Volume da esfera: {volEsf:.6f}")