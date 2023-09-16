# 01. Você sabia que os computadores amam contar coisas? Eles são como pequenos nerds! Vamos fazer um contador de letras. Peça ao usuário para digitar uma frase qualquer e, em seguida, imprima o número de caracteres nessa frase sem considerar espaços em branco no início ou final da frase digitada.

# Processing function
def charNum(char):
    # returns the counting method in the variable "char"
    return len(char)

# Main function
def main():
    # The "varChar" variable receives input
    varChar = str(input("Digite um nome: ")).strip()
    # The variable "result" receives the function call "charNum", sending the necessary parameter and receiving the result
    result = charNum(varChar)
    # Prints the result of the "result" variable on the screen
    print(f"A quantidade de caracteres (sem contar os espaços em branco do inÍcio ou final da frase) do nome são de {result} letras.")

# Identify function main for execute
if __name__ == "__main__":
    main()