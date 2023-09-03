# 04. Você gostaria de saber quantos segundos se passaram desde a meia-noite? Escreva um programa que leia valores inteiros para hora, minuto e segundo. Em seguida, o programa deve calcular e imprimir quantos segundos se passaram no total desde a última meia-noite até a hora lida.

hour = int(input("Digite a(s) hora(s) desejada(s): "))
minu = int(input("Escreva o(s) minuto(s) desejado(s): "))
sec = int(input("Por fim, digite o(s) segundo(s): "))

totalsec = (hour*60)*60 + (minu * 60) + sec

print(f"Contando a partir da meia-noite, teremos um total de {totalsec} segundos")