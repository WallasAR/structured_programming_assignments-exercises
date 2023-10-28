# 01. Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação: A condição de saída do laço será a leitura do valor 0 (flag).

# Creation of the function "sumNum" for data processing
def sumNum():
    # Variable "aux" is initialized
    aux = 0
    # Repetition structure that runs indefinitely
    while True:
        # Variable "num" receives input, then converted to integer type
        num = int(input("Digite um número qualquer (0 para sair): "))
        # Variable "aux" receives sum of itself with the variable "num"
        aux += num
        # Conditional structure used to interrupt the loop
        if (num == 0):
            return aux
# Creating the main function
def main():
    # The variable "valNum" receives the call to the "sumNum" function
    valNum = sumNum()
    # Show the value ​​of the variable "valNum" on the screen
    print(f"A soma de todos os números lidos é igual a {valNum}")
# Identify function main for execute
if __name__ == "__main__":
    main()