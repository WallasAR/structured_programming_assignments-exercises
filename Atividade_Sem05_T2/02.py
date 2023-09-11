# 02. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou o valor booleano False (falso) caso contrário.

# Processing function
def analysis(l):
    # Variables "upperLetter, lowerLetter" receive strings of characters, respectively, of uppercase and lowercase letters.
    upperLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerLetter = "abcdefghijklmnopqrstuvwxyz"
    # The variable "l" will be compared with the elements of the "upperLetter" and "lowerLetter" vectors, if any element matches the input the result will be True, otherwise it will be False.
    return l in upperLetter or l in lowerLetter

# Main function
def main():# The "char" variable receives input and is converted to string type
    
    char = str(input("Informe algum valor: ")).strip()
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result immediately afterwards
    result = analysis(char)
    # Prints the result of the "result" variable on the screen
    print(f"A entrada informada é uma letra(vogal ou consoante)?\nResposta: {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()