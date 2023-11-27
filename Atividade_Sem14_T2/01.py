# 1. Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior elemento e a posição que ele se encontra.

def inputList():
    # Initializing the empty list
    num_list = []

    # Reading of 10 integers
    for i in range(10):
        num = int(input(f"Digite o número {i + 1}: "))
        # Adding the number to the list
        num_list.append(num)  
    # Returns the list filled with numbers entered by the user
    return num_list

# Main Function
def main():
    # Call the inputList function to obtain the list of entered numbers
    numList = inputList()

    # Find the largest number in the list
    maxNum = max(numList)
    # Find the index of the largest number in the list
    maxIndex = numList.index(maxNum)

    # Printing the complete list
    print("Lista completa:", numList)

    # Printing the largest element and its position
    print(f"O maior elemento é {maxNum} e está na posição {maxIndex}.")

# Identify function main for execute
if __name__ == "__main__":
    main()
