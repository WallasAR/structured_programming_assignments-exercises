# 01. Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.

# OBS.: Olá professor! tenho o costume de deixar minha documentação em inglês, espero que não tenha nenhum problema. Motivo: legibilidade para o maior número de pessoas na plataforma do GitHub.

# Processing function
def charNum(char):
    # returns the counting method in the variable "char"
    return len(char)

# Main function
def main():
    # The "varChar" variable receives input
    varChar = str(input("Digite um nome: "))
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result
    result = charNum(varChar)
    # Prints the result of the "result" variable on the screen
    print(f"A quantidade de caracteres do nome são de {result} letras")

# Identify function main for execute
if __name__ == "__main__":
    main()