# 3. Leia duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.

# Function to generate a list C by summing respective elements of lists A and B
def generateListC(listA, listB):
    listC = []

    # Loop through the elements of listA and listB
    for i in range(len(listA)):
        # Add corresponding elements of listA and listB and append the result to listC
        listC.append(listA[i] + listB[i])

    return listC

# Function to input 20 integers into a list
def inputList():
    numList = []

    # Input 20 integers and append them to numList
    for _ in range(20):
        num = int(input())
        numList.append(num)

    return numList

# Main function
def main():
    print("Digite 20 números inteiros para a lista A: ")
    listA = inputList()

    print("Digite 20 números inteiros para a lista B: ")
    listB = inputList()

    # Generate list C by summing corresponding elements of listA and listB
    listC = generateListC(listA, listB)

    # Display lists A, B, and C
    print(f"Lista A: {listA}\nLista B: {listB}\nLista C: {listC}")
# Identify function main for execute
if __name__ == "__main__":
    main()
