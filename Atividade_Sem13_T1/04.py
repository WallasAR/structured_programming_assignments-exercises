# 4. Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

# Function that creates the list of 20 elements
def oddAndEven():
    # List initialization
    numList = []
    # Repetition structure that allows data entry and addition to the list the given number of times
    for count in range(20):
        nums = int(input(f"Digite o {count + 1}º número inteiro: "))
        # Method that places numbers in the list
        numList.append(nums)
    # Returns the list
    return numList

# Function that will separate even numbers from the list previously created in the "oddAndEven" function
def even(numList):
    evenList = []
    # Repetition structure that allows comparison the correct number of times
    for count in range(20):
        # Checks through the index if the corresponding element is even, if so it will be added to the list "evenList"
        if numList[count] % 2 == 0:
            evenList.append(numList[count])
    # Returns the list
    return evenList

# It works exactly the same way as the "even" function, however the numbers that will be separated are the odd ones
def odd(numList):
    oddList = []

    for count in range(20):
        # Here we check if the number is odd
        if numList[count] % 2 != 0:
            oddList.append(numList[count])

    return oddList
# Creating the main function
def main():
    # Variable that receives function call "oddAndEven"
    oddEvenList = oddAndEven()
    # Variable that receives function call "evenList", passing the list of the "oddAndEven" function as a parameter
    evenList = even(oddEvenList)
    # Variable that receives function call "oddList", passing the list of the "oddAndEven" function as a parameter
    oddList = odd(oddEvenList)
    # Shows the user the list of all 20 numbers, the list with only even numbers and the list with only odd numbers
    print(f"\nLista de todos os números: {oddEvenList}\nLista com os números pares: {evenList}\nLista com os números ímpares{oddList}")
# Identify function main for execute
if __name__ == "__main__":
    main()