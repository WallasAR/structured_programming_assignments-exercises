# 03. Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. Separe esses valores com um hífen.

def verify(b, h):
    if (b == h):
        return "QUADRADO"
    else:
        perim = b + b + h + h
        area = b * h
        return f"{perim} - {area}"

def main():
    var1 = int(input())
    var2 = int(input())

    resultVerif = verify(var1, var2)

    print(f"{resultVerif}")

if __name__ == "__main__":
    main()