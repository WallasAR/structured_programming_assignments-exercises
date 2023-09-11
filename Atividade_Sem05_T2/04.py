# 04. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou um NÚMERO (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.

# Processing function
def analysis(c):
    # Variables "letter, number" receive strings of characters, respectively, of letters and numbers
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    # The variable “c” will be compared with the elements of the “letter and number” vectors, if any element matches the input the result will be True, otherwise it will be False.
    return c in letter or c in number

# Main function
def main():
    # The "char" variable receives input and is converted to string type
    char = str(input("Informe qualquer valor: ")).strip()
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result immediately afterwards
    result = analysis(char)
    # Prints the result of the "result" variable on the screen
    print(f"O valor digitado é uma letra(vogal ou consoante) ou um númeral(entre 0 e 9)?\nResposta: {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()