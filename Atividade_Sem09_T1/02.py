# 02. Escreva um programa que leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

def calculator(n1, n2, choice):
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

def main():
    num1 = float(input())
    num2 = float(input())  
    opChoice = int(input())

    operResult = calculator(num1, num2, opChoice)

    print(f"{operResult}")
if __name__ == "__main__":
    main()