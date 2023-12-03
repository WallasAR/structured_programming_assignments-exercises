# 03.Fazer um programa para ler uma matrix n x m de números inteiros. Os valores de n e m são inteiros, positivos edevem ser informados pelo usuário, calcular e armazenar em uma tupla para mostrar, respectivamente:
# a) a soma dos elementos da primeira linha
# b) a soma dos elementos da última coluna
# c) a média de todos os elementos
# d) o menor elemento
# e) o maior elemento

# Function to create a matrix based on user input for dimensions and elements
def CreateMatrix():
    r = int(input("Digite o número de linhas da matriz: "))  # Takes user input for number of rows
    c = int(input("Digite o número de colunas: "))  # Takes user input for number of columns
    
    matrix = []  # Initializes an empty matrix
    for i in range(r):
        line = []  # Initializes an empty list for each row
        for j in range(c):
            element = int(input())  # Takes user input for each element in the matrix
            line.append(element)  # Appends the element to the row list
        matrix.append(line)  # Appends the row list to the matrix
    
    return matrix  # Returns the created matrix

# Function to calculate the sum of elements in the first row of the matrix
def sumFirstLine(matrix):
    sumLine = sum(matrix[0])  # Sums the elements in the first row
    return sumLine

# Function to calculate the sum of elements in the last column of the matrix
def sumLastCollumn(matrix):
    sumCol = sum(matrix[i][-1] for i in range(len(matrix)))  # Sums the elements in the last column
    return sumCol

# Function to calculate the average of all elements in the matrix
def elementsAverage(matrix):
    elements = [element for line in matrix for element in line]
    average = sum(elements) / len(elements)  # Calculates the average of all elements
    return round(average, 4)  # Returns the average rounded to four decimal places

# Function to find the smallest element in the matrix
def smallestElement(matrix):
    elements = [element for line in matrix for element in line]  # Flattens the matrix into a 1D list
    smaller = min(elements)  # Finds the smallest element in the list
    return smaller  # Returns the smallest element

# Function to find the largest element in the matrix
def largestElement(matrix):
    elements = [element for line in matrix for element in line]  # Flattens the matrix into a 1D list
    bigger = max(elements)  # Finds the largest element in the list
    return bigger  # Returns the largest element

# Main function
def main():
    matrix = CreateMatrix()  # Creates a matrix based on user input
    
    # Calculates the required values and stores them in a tuple
    result = (
        sumFirstLine(matrix),
        sumLastCollumn(matrix),
        elementsAverage(matrix),
        smallestElement(matrix),
        largestElement(matrix)
    )
    
    print(f"Tupla com os resultados: {result}")  # Prints the tuple containing the calculated values

# Runs the main function if this script is executed directly
if __name__ == "__main__":
    main()

