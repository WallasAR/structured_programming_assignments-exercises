# 05. A Bate Ponto LTDA bonifica seus funcionários de acordo o tempo de serviço na empresa. Escreva um programa que leia o tempo de serviço de um funcionário e o valor do bônus por ano trabalhado. Mostre na tela quanto será abonificação do funcionário.

timeserv = float(input("Tempo de serviço do funcionário: "))
bonus = float(input("Bônus anual R$ "))

totalbonus = timeserv * bonus

print(f"Bônus R$ {totalbonus:.2f}")