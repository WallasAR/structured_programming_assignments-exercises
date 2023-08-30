# 03. Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da divisão inteira dos valores.

dividend = float(input("Digite o valor do dividendo: "))
divis = float(input("Digite o valor do divisor: "))

quoc = dividend // divis
rest = dividend % divis


print(f"Resultado: {quoc:.4f}\nResto {rest:.4f}.")
