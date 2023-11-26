# 2. Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2 aparece na lista. Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.

# Function to count occurrences of a value in a list
def countOccurrences(arr, val):
    count = 0

    for item in arr:
        if item == val:
            count += 1
    # Returns the list filled with input values
    return count

# Function to input numbers into a list
def inputList():
    ArrayList = []

    while True:
         # Reads input from the user
        val = int(input("Digite um número qualquer (0 para sair): "))
        # If input is 0, break out of the loop
        if val == 0:
            break
        # Appends input values to the list
        ArrayList.append(val)
    # Returns the list filled with input values
    return ArrayList

# Main function
def main():
    # Calls the function to input values into a list
    inputListData = inputList()
    # Reads an integer input to search for in the list
    searchVal = int(input("Digite um valor para pesquisa: "))
    # Calls the function to count occurrences of the input value in the list
    occurrences = countOccurrences(inputListData, searchVal)

    # Prints the original list, the search value, and the number of occurrences
    print(f"Lista: {inputListData}\nValor pesquisado: {searchVal}\nOcorrências deste valor na lista: {occurrences}")
# Identify function main for execute
if __name__ == "__main__":
    main()