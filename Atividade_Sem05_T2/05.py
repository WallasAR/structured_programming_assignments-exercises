# 05. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um SÍMBOLO (o que não é letra ou número) ou o valor booleano False (falso) caso contrário.

# Processing function
def analysis(c):
    # The variable "simbol" receives a series of characters
    simbol = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~§ªº°"
    # The variable "c" will be compared with the elements in the vector "symbol", if any element corresponds to the entry the result will be True, otherwise it will be False.
    return c in simbol

# Main function
def main():
    # The "char" variable receives input and is converted to string type
    char = str(input("Digite o valor: ")).strip()
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result immediately afterwards
    result = analysis(char)
    # Prints the result of the "result" variable on the screen
    print(f"Esse valor é um simbolo?\nResposta: {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()