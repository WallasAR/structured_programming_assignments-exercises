# 04. Escreva um programa que leia uma quantidade de minutos e mostre a quantidade de horas e minutos equivalente.

min = int(input("Digite a quantidade de minutos a serem convertidos: "))

h = min // 60
m = min % 60

print(f"{h} hora(s) e {m} minuto(s)")