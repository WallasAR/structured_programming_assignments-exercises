#  05. Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco). A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:
# • Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
# • Se 1 (um), escreva se o valor lido é par ou ímpar;
# • Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
# • Se 3 (três), escreva a divisão inteira do valor lido por 10;
# • Se 4 (quatro), escreva o quadrado do valor lido;

# Creation of the function "choice" for data processing
def choice(numInt):
    # Variable "" receives mathematical operation
    calc = numInt % 5
    # Multiple choice structure that checks the corresponding operation according to the Boolean result of the variable "calc"
    if (calc == 0):
        return 9*numInt + 7
    
    elif (calc == 1):
        if numInt % 2 == 0:
            return "par"
        else:
            return "ímpar"
        
    elif(calc == 2):
        return 5*(numInt**2) - (3*numInt) + 42
    
    elif (calc == 3):
        return numInt // 10
    
    else:
        return numInt**2

# Creating the main function
def main():
    # Variable "num" receives an input and is then converted to the integer type
    num = int(input("Digite um número inteiro qualquer: "))
    # The variable "result" receives the call to the "choice" function
    result = choice(num)
    # Prints the value of the variable "result" on the screen
    print(f"A operação correspondente retornou o seguinte resultando: {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()