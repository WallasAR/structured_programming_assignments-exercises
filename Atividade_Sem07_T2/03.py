# 03. Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido. 
# • Nenhum dígito é ímpar. • Apenas um dígito é ímpar. • Os dois dígitos são ímpares.

def analysis(intNum):
    count = 0
    num = intNum // 10
    d = num % 2 == 1
    if d:
        count += 1
    u = intNum % 2 == 1
    if u:
        count += 1
    if (count == 0):
        return "Nenhum dígito é ímpar."
    elif (count == 1):
        return "Apenas um dígito é ímpar."
    elif (count == 2):
        return "Os dois dígitos são ímpares."

def main():
    VarNum = int(input())

    result = analysis(VarNum)

    print(f"{result}")

if __name__ == "__main__":
    main()