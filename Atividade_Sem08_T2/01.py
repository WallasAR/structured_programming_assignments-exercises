# 01. Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja ímpar. Mostre na tela o resultado da operação.

# Creation of the function "analysis" for data processing
def analysis(var):
    # Conditional structure that checks whether the given number is even by the operation, if so it will return the variable "var" + 5, otherwise it will return "var" + 8
    if (var % 2 == 0):
        return var + 5
    else:
        return var + 8
    
# Creating the main function
def main():
    # The variable "var" receives an input, which is converted to the integer type
    var = int(input("Informe um número inteiro qualquer: "))
    # The variable "result" receives the call to the "analysis" function
    result = analysis(var)
    # Shows the value of the "result" variable on the screen
    print(f"O valor dado tem como resultado {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()