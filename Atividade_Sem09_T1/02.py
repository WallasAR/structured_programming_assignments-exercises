# 02. Escreva um programa que leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

# Creation of the function "calculator" for data processing
def calculator(n1, n2, choice):
    # Multiple choice structure that compares the value of the "choice" variable with the predetermined values ​​for each type of operation
    if (choice == 1):
        return n1 + n2
    elif (choice == 2):
        return n1 - n2
    elif (choice == 3):
        return n1 * n2
    elif (choice == 4):
        return n1 / n2
    else:
        return "Valor inválido"

# Creating the main function
def main():
    # The variables "num1, num2" receive input and are then transformed into float type
    num1 = float(input("Informe o primeiro valor: "))
    num2 = float(input("Informe o segundo valor: "))  
    # Variable "opChoice" receives an input and is then converted to the integer type
    opChoice = int(input("Digite a operação desejada(1 - Adição, 2 - Subtração, 3 - Multiplicação e 4 - Divisão): "))
    # The variable "operResult" receives the call to the "calculator" function, receiving the result with the desired operation
    operResult = calculator(num1, num2, opChoice)
    # Shows the result of the variable "operResult" on the screen
    print(f"O resultado da operação é {operResult}")

# Identify function main for execute
if __name__ == "__main__":
    main()