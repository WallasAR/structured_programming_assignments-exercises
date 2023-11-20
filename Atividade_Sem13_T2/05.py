# 5. Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso.
# IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso.

# This function collects 'n' elements of input and appends them to a list
def inputElem(n, lista):
    # Loops 'n' times to gather 'n' inputs
    for count in range(n):  
        # Takes user input and removes leading/trailing whitespaces
        x = input().strip() 
        try:
            # Tries to convert input to a float
            x = float(x)  
        # If conversion fails (input is not a number), it remains a string
        except ValueError: 
            pass
        # Appends the input (either float or string) to the list
        lista.append(x)  
    # Returns the modified list
    return lista  

# Main function
def main():
    # Takes user input for the number of elements
    num = int(input("Enter the number of elements: "))  
    # Initializes an empty list called 'lista'
    lista = []  
    # Calls the inputElem function to populate the list with user inputs
    lista = inputElem(num, lista)  
    # Checks if the sorted version of 'lista' matches the original 'lista'
    if sorted(lista) == lista:
        # Prints 'LISTA ORDENADA' if the list is in ascending order
        print("LISTA ORDENADA")  
    else:
        # Prints 'LISTA NÃO ORDENADA' if the list is not in ascending order
        print("LISTA NÃO ORDENADA")  
# Identify function main for execute
if __name__ == "__main__":
    main() 
