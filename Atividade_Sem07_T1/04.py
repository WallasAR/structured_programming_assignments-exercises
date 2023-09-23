# 04. Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”.

# Processing function
def analysis(char):
    # The variable "char" receives the method capable of changing the letter of a string to uppercase
    char = char.upper()
    # Conditional that checks whether it is a vowel
    if (char in "AEIOU"):
        return "vogal"
    # In this section, check if it is consonant
    elif ("A" <= char <= "Z") and char not in "AEIOU":
        return "consoante"
    # In the same way, check if it is a number
    elif ("0" <= char <= "9"):
        return "número"
    # If it is none of the above, it will return "symbol"
    else:
        return "símbolo"

# Main function
def main():
    # The variable "charNum" receives an input, which is converted to the string type
    charNum = str(input("Digite um caractere qualquer: "))
    # The variable "result" receives the function call "analysis"
    result = analysis(charNum)
    # Shows the values ​​of the variables "charNum" and "result" on the screen
    print(f"O caracter informado ({charNum}) é corresponde a um(a) {result}.")

# Identify function main for execute
if __name__ == "__main__":
    main()