# 2. Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
# DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.

# Function to modify elements of a list based on their index
def multiplyIndices(OrdList):
    # Iterate through the indices of the list
    for indice in range(len(OrdList)):
        # Multiply elements at even indices by 3 and at odd indices by 5
        if (indice % 2 == 0):
            OrdList[indice] *= 3
        else:
            OrdList[indice] *= 5

# Function to input 100 numbers into a list
def inputNums():
    arrList = []
    # Input 100 numbers into the list
    for count in range(100):
        num = int(input(f"Digite o {count + 1}º número inteiro: "))
        arrList.append(num)
    # Returns the list
    return arrList

# Main function
def main():
    # Variable that receives function call "inputNums"
    arrList = inputNums()
    # Sort the list
    OrdList = sorted(arrList)
    # Modify the elements of the sorted list using multiplyIndices function
    multiplyIndices(OrdList)
    # Print the modified list
    print(f"Lista Ordenada e Multiplicada: {OrdList}")
# Identify function main for execute
if __name__ == "__main__":
    main()