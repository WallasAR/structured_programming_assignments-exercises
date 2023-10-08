# Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os valores lidos:
# • Todos os valores são diferentes;
# • Existem dois valores iguais e um diferente;
# • Todos os valores são iguais.

# Creation of the function "message" for data processing
def message(n1, n2, n3):
    # Multiple choice structure that checks and compares the three input numbers in order to say whether they are all the same, all different or just two equal and one different
    if (n1 != n2) and (n2 != n3) and (n1 != n3):
        return "Todos os valores são diferentes"
    elif (n1 == n2 == n3):
        return "Todos os valores são iguais"
    else:
        return "Existem dois valores iguais e um diferente"

# Creating the main function
def main():
    # Variables "var01, var02, var03" receive inputs and are all converted to integers
    var01 = int(input("Digite o primeiro número inteiro: "))
    var02 = int(input("Digite o segundo número inteiro: "))
    var03 = int(input("Digite o terceiro número inteiro: "))
    # The variable "msg" receives the call to the "message" function, receiving the appropriate description
    msg = message(var01, var02, var03)
    # Shows the result of the variable "msg" on the screen
    print(f"Entre os três números dados, conclui-se que: {msg}")

# Identify function main for execute
if __name__ == "__main__":
    main()