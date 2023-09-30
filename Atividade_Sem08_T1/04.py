# 04. Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a média. Considere duas casas decimais.

# Creation of the function "average" for data processing
def average(var1, var2, var3, var4, var5):
    # variable "aver" receives mathematical equation that calculates the average
    aver = (var1 + var2 + var3 + var4 + var5) / 5
    # Variable "" receives the variable "" converted to string + line break
    num = str(aver) + '\n'
    # Sequence of conditional structures that check whether the user input is greater than the previously calculated average, if so the variable is iterated the variable "num"
    if (var1 > aver):
        num += str(var1) + '\n'
    if (var2 > aver):
        num += str(var2) + '\n'
    if (var3 > aver):
        num += str(var3) + '\n'
    if (var4 > aver):
        num += str(var4) + '\n'
    if (var5 > aver):
        num += str(var5) + '\n'
    return num.strip()

# Creating the main function
def main():
    # Variables "num1, num2, num3, num4, num5" receive input and are converted to integer
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = int(input("Digite o terceiro número inteiro: "))
    num4 = int(input("Digite o quarto número inteiro: "))
    num5 = int(input("Digite o quinto número inteiro: "))
    # The variable "av" receives the call from the "average" function, receiving the value of the variable "num"
    av = average(num1, num2, num3, num4, num5)
    # Prints the value of the variable "av" on the screen.
    print(f"Valor da média junto aos números maiores que a mesma: {av}")

# Identify function main for execute
if __name__ == "__main__":
    main()