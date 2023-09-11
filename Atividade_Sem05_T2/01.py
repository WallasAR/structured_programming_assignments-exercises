# 01. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma VOGAL ou o valor booleano False (falso) caso contrário.

# OBS.: Olá professor! tenho o costume de deixar minha documentação em inglês, espero que não tenha nenhum problema. Motivo: legibilidade para o maior número de pessoas na plataforma do GitHub.

# Processing function
def analysis(v):
    # The "isvogal" variable receives a boolean operation
    isvogal = bool((v == "a") or (v == "e") or (v == "i") or (v == "o") or (v == "u") or (v == "A") or (v == "E") or (v == "I") or (v == "O") or (v == "U"))
    return isvogal

# Main function
def main():
    # The "char" variable receives input and is converted to string type
    char = str(input("Qual o valor desejado? ")).strip()
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result immediately afterwards
    result = analysis(char)
    # Prints the result of the "result" variable on the screen
    print(f"A entrada dita é uma vogal?\nResposta: {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()