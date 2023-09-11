# 03. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma CONSOANTE ou o valor booleano False (falso) caso contrário.

# Processing function
def analysis(c):
    # Variables "upperLetter, lowerLetter" receive strings of characters, respectively, of uppercase and lowercase letters.
    upperLetter = "BCDFGHJKLMNPQRSTVWXYZ"
    lowerLetter = "bcdfghjklmnpqrstvwxyz"
    # The variable "c" will be compared with the elements of the "upperLetter" and "lowerLetter" vectors, if any element matches the input the result will be True, otherwise it will be False.
    return c in upperLetter or c in lowerLetter

# Main function
def main():
    # The "char" variable receives input and is converted to string type
    char = str(input("Digite qualquer valor: ")).strip()
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result immediately afterwards
    result = analysis(char)
    # Prints the result of the "result" variable on the screen
    print(f"O valor informado é uma consoante?\nResposta: {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()