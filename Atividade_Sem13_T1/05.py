# 5. Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, cujos elementos sejam a intercalação dos elementos de A e B.

# Function to receive elements from lists A and B from the user
def inputListsAB():
    # Initialize lists A and B
    listA = []
    listB = []
    # Loop to receive 25 elements from the user's list A
    for count in range(25):
        numListA = int(input(f"Digite o {count + 1}º elemento da lista A: "))

        listA.append(numListA)

    # Loop to receive 25 elements from the user's list B
    for count in range(25):
        numListB = int(input(f"Digite o {count + 1}º elemento da lista B: "))

        listB.append(numListB)
    # Returns lists A and B
    return listA, listB

# Function to merge elements from lists A and B into a list C
def mergeLists(listA, listB):
    # Initialize list C
    listC = []
    # Loop to merge the elements of A and B in list C
    for count in range(25):
        listC.append(listA[count])
        listC.append(listB[count])
    # Returns the merged list C
    return listC

# Creating the main function
def main():
    # Call the function to receive the user's lists A and B
    listA, listB = inputListsAB()
    # Call the function to merge lists A and B into one list C
    mergeForListC = mergeLists(listA, listB)
    # Print lists A, B and C
    print(f"Lista A: {listA}\nLista B: {listB}\nLista C: {mergeForListC}")
# Identify function main for execute
if __name__ == "__main__":
    main()