# 05. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um SÍMBOLO (o que não é letra ou número) ou o valor booleano False (falso) caso contrário.

def analysis(c):
    isconsonant = bool(c >= "a" and c <= "z" )
    isNumber = bool(c > "" and c < "")
    return ((not isconsonant) or not isNumber)

def main():
    char = str(input())
    
    result = analysis(char)

    print(result)

if __name__ == "__main__":
    main()