# 01. Considere que as variáveis “dia”, “mês” e “ano” contém os valores respectivos de uma certa data. Escreva um comando “print” que imprima essa data no formato usado, por exemplo, “15/4/2020” ou “2/12/2004”.

day = int(input("Digite o dia: "))
month = int(input("Digite o mês: "))
year = int(input("Digite o ano: "))

print(f"\n{day}/{month}/{year}")
