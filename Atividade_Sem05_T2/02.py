# 02. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou o valor booleano False (falso) caso contrário.

def analysis(l):
    isletter = bool((l >= "a") and (l <= "z"))
    return isletter

def main():
    char = input()
    
    result = analysis(char)

    print(result)

if __name__ == "__main__":
    main()