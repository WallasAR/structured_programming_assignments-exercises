# 04. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou um NÚMERO (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.

def analysis(c):
    isconsonant = bool(c >= "a" and c <= "z" )
    isNumber = bool(c >= 0 and c <= 9)
    return (isconsonant or isNumber)

def main():
    char = str(input())
    
    result = analysis(char)

    print(result)

if __name__ == "__main__":
    main()