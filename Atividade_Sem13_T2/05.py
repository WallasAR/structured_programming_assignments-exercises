# 5. Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso.
# IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso.

def isOrdened(elemList):
    return elemList == sorted(elemList)

def inputNums():
    elementsList = []
    amount = int(input())

    for count in range(amount):
        val = str(input()).strip()
        elementsList.append(val)
    return elementsList

def main():
    elemList = inputNums()

    if isOrdened(elemList):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")

if __name__ == "__main__":
    main()