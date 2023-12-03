# 01. Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do maior e menor elemento. O valor de n é inteiro, positivo e deve ser informados pelo usuário.

# This function creates and returns a square matrix of order 'n'
def readSquareMatrix(n):
    matrix = []  # Initializes an empty matrix

    for i in range(n):
        line = []  # Initializes an empty list to represent a row of the matrix
        for j in range(n):
            # Prompts for the element
            element = int(input(f"Digite o elemento da posição [{i}][{j}]: "))  
            line.append(element)  # Adds the element to the row
        matrix.append(line)  # Adds the row to the matrix

    return matrix  # Returns the filled matrix

# This function finds the positions (row and column) of the largest and smallest elements in an array, traversing the array to compare each element and determine the largest and smallest.
def findMaxMin(matrix):
    n = len(matrix)  # Gets the order of the matrix
    # Initialize the largest and smallest element with the beginning of the matrix, in order to scroll through it
    max_element = matrix[0][0] 
    min_element = matrix[0][0]
    # Initializes the position of the largest and smallest element, they will be responsible for storing the respective correct indices
    max_pos = (0, 0)  
    min_pos = (0, 0) 

    # Traverse the array to find the largest and smallest elements, saving their positions
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_pos = (i, j)
            elif matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_pos = (i, j)

    return max_pos, min_pos  # Returns the positions of the largest and smallest elements

# Main function
def main():
    # Request the order of the array
    n = int(input("Digite a ordem da matriz quadrada: "))  
    
    print(f"\nDigite os elementos da matriz {n}x{n}:")
    matrix = readSquareMatrix(n)  # Call the function to fill the matrix

    # Calls the function to find the positions of the largest and smallest element
    max_pos, min_pos = findMaxMin(matrix)   
    
    # Display the positions of the largest and smallest element
    print(f"\nA posição do maior elemento é: {max_pos}")
    print(f"A posição do menor elemento é: {min_pos}")

# Execute the 'main' function when the script is run
if __name__ == "__main__":
    main() 
