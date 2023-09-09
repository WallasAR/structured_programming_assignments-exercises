# 01. Escreva um programa que ler três valores inteiros (a, b e c). Calcule o mostre o resultado da função:
# def calcular(a, b, c):
#     return 2 * a + 5 * b - c

# OBS.: Olá professor! tenho o costume de deixar minha documentação em inglês, espero que não tenha nenhum problema. Motivo: legibilidade para o maior número de pessoas na plataforma do GitHub.

# Processing
def calculate(n1, n2, n3):
     # returns the result of equation
    return (2 * n1) + (5 * n2) - n3

# Main function
def main():
    # Variables "val1, val2, val3" receives inputs and all are converted to int type
    val1 = int(input("Digite o primeiro valor inteiro: "))
    val2 = int(input("Digite o segundo valor inteiro: "))
    val3 = int(input("Digite o terceiro valor inteiro: "))
    # The "result" variable calls the "calculate" function, giving the necessary parameters and receiving the result immediately afterwards.
    result = calculate(val1, val2, val3)
    # Prints the result of the "result" variable on the screen
    print(f"O resultado da função é {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()