# Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os valores lidos:
# • Todos os valores são diferentes;
# • Existem dois valores iguais e um diferente;
# • Todos os valores são iguais.

def message(n1, n2, n3):
    if (n1 != n2) and (n2 != n3) and (n1 != n3):
        return "Todos os valores são diferentes"
    elif (n1 == n2 == n3):
        return "Todos os valores são iguais"
    else:
        return "Existem dois valores iguais e um diferente"

def main():
    var01 = int(input())
    var02 = int(input())
    var03 = int(input())

    msg = message(var01, var02, var03)

    print(f"{msg}")
if __name__ == "__main__":
    main()