# 03. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma CONSOANTE ou o valor booleano False (falso) caso contrário.

def analysis(c):
    isconsonant = bool((c == "e") or (c == "i") or (c == "o") or (c == "u"))
    isconsonant2 = bool(c > "a" and c <= "z" )
    return (not isconsonant and isconsonant2)

def main():
    char = input()
    
    result = analysis(char)

    print(result)

if __name__ == "__main__":
    main()