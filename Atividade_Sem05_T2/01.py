# 01. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma VOGAL ou o valor booleano False (falso) caso contrário.

def analysis(v):
    isvogal = bool(v == "a" or "e" or "i" or "o" or "u")
    return isvogal

def main():
    char = str(input())
    
    result = analysis(char)

    print(result)

if __name__ == "__main__":
    main()