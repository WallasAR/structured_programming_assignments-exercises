# 01. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma VOGAL ou o valor booleano False (falso) caso contrário.

def analysis(v):
    isvogal = bool((v == "a") or (v == "e") or (v == "i") or (v == "o") or (v == "u"))
    return isvogal

def main():
    char = str(input())
    
    result = analysis(char)

    print(result)

if __name__ == "__main__":
    main()