# 05. Escreva um programa que leia três números e mostre na tela em ordem crescente.

def ascOrder(v1, v2, v3):
    mini = min(v1, v2, v3)
    maxi = max(v1, v2, v3)
    mid = v1 + v2 + v3 - mini - maxi
    return mini, mid, maxi


def main():
    var1 = int(input())
    var2 = int(input())
    var3 = int(input())

    mini, mid, maxi = ascOrder(var1, var2, var3)

    print(f"{mini}\n{mid}\n{maxi}")

if __name__ == "__main__":
    main()