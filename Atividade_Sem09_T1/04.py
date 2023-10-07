# 04. Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.

def analysis(v1, v2, v3):
    secondDif = v1 - v2
    thirdDif = v1 - v3

    if (secondDif > thirdDif):
        return abs(secondDif)
    else:
        return abs(thirdDif)

def main():
    var1 = int(input())
    var2 = int(input())
    var3 = int(input())

    result = analysis(var1, var2, var3)

    print(f"{result}")

if __name__ == "__main__":
    main()