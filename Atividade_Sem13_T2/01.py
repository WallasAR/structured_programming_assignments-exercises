# 1. Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista onde cada valor da lista original é a multiplicado pelo valor da constante.
# IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e o valor da constante e retorna uma nova lista com os elementos multiplicados.

# Function to multiply each element in the list by a constant
def multiplyCons(numList, cons):
    newList = []
    # Loop through each element in the numList
    for element in numList:
        # Multiply the element by the constant and append it to the new list
        newElement = element * cons
        # Method that places numbers in the list
        newList.append(newElement)
    # Returns the new list
    return newList
 
# Function to input values until 0 is entered
def inputVals():
    numList = []

    while True:
        num = int(input("Digite um número inteiro (0 para sair): "))
        if ( num == 0):
            break
        numList.append(num)
    return numList

# Main function
def main():
    # Variable that receives function call "inputVals"
    numList = inputVals()
    # Input a constant value
    consVal = int(input("Digite o valor da constante: "))
    # Multiply the list elements by the constant using the multiplyCons function
    newList = multiplyCons(numList, consVal)
    # Print the new list after multiplication
    print(f"Lista Multiplicada pela constante {consVal}: {newList}")
# Identify function main for execute
if __name__ == "__main__":
    main()