# 02. Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao caractere lido.

# Processing function
def numCode(char):
    # returns the input conversion method to a corresponding decimal number in the ASCII table
    return ord(char)

# Main function
def main():
    # The "varChar" variable receives input
    varChar = str(input("Informe um caractere qualquer: "))
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result
    result = numCode(varChar)
    # Prints the result of the "result" variable on the screen
    print(f"O codigo numérico correspondente a esse caracter de acordo com a tabela ASCII -> {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()