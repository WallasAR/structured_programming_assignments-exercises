# 4. Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos anteriores da lista original.
# IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna uma lista com a soma cumulativa.

# Function to calculate the cumulative sum of elements in a list
def cumulativeSum(numList):
    # Initialize a variable to hold the running sum
    sumNum = 0
    # Create an empty list to store the cumulative sum of elements
    addElemList = []
    # Loop through each element in the input list
    for elem in numList:
        # Add the current element to the running sum
        sumNum += elem
        # Append the running sum to the new list
        addElemList.append(sumNum)
    # Return the list with cumulative sums of elements
    return addElemList

# Function to input values into a list  
def inputVals():
    # Create an empty list to store input values
    numList = []
    # Loop to continuously input values until 0 is entered
    while True:
        # Input an integer value
        num = int(input("Digite um número qualquer (0 para parar): "))
        # Check if the input is zero. If input is zero, break out of the loop
        if (num == 0):
            break
        # Append non-zero values to the list
        numList.append(num)
    # Return the list of input values
    return numList

# Main function
def main():
    # Get input values from the user
    numList = inputVals()
    # Calculate cumulative sum of the input values
    resultAddElements = cumulativeSum(numList)
    # Print the list with cumulative sums
    print(f"Soma cumulativa da lista original: {resultAddElements}")
# Identify function main for execute
if __name__ == "__main__":
    main()