# 02. Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.

def analysis(intNum):
    c = intNum // 100
    d = (intNum % 100) // 10
    u = intNum % 10
    
    count = 0
    if c % 2 == 0:
        count += 1
    if d % 2 == 0:
        count += 1
    if u % 2 == 0:
        count += 1

    if (count == 0):
        return "0"
    elif (count == 1):
        return "1"
    elif (count == 2):
        return "2"
    elif (count == 3):
        return "3"

def main():
    VarNum = int(input())

    result = analysis(VarNum)

    print(f"{result}")

if __name__ == "__main__":
    main()