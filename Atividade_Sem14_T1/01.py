# 1. As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
# a) len(), que recebe uma lista e retorna número de itens;
# b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
# c) min(),que recebe uma lista e retorna o menor valor
# d) max(), que recebe uma lista retorna o maior valor
# e) sum(), que recebe uma lista retorna a soma dos valores
# Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o resultado encontrado. Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(), minimo(), maximo(), soma().

# Function to calculate the length of the list
def length(ArrayList):
    count = 0
    #  Loops through each element in the input list
    for n in ArrayList:
        # Increments the counter for each element in the list
        count += 1
    # Returns the final count, which represents the length of the list
    return count

# Function to reverse the list
def invert(ArrayList):
    inverted_list = []
    # Initializes an index to start from the end of the input list
    index = len(ArrayList) - 1
    while index >= 0:
        # Appends elements from the input list to the inverted_list in reverse order
        inverted_list.append(ArrayList[index])
        # Decrements the index to move to the previous element in the input list
        index -= 1
    # Returns the reversed list
    return inverted_list

# Function to find the minimum value in the list
def minimum(ArrayList):
    min_value = ArrayList[0]

    for item in ArrayList:
        if item < min_value:
            min_value = item

    return min_value

# Function to find the maximum value in the list
def maximum(ArrayList):
    max_value = ArrayList[0]

    for item in ArrayList:
        if item > max_value:
            max_value = item

    return max_value

# Function to calculate the sum of the numbers in the list
def sumNums(ArrayList):
    total = 0

    for item in ArrayList:
        total += item

    return total

# Function to input numbers into a list
def inputNums():
    ArrayList = []

    while True:
        val = int(input("Digite um número qualquer (0 para sair): "))
        if val == 0:
            break
        ArrayList.append(val)

    return ArrayList

# Main function
def main():
    # Get input values from the user
    ProcessList = inputNums()  

    # Print the read list and results
    print(f"{ProcessList}")
    print(f"{length(ProcessList)}")
    print(f"{invert(ProcessList)}")
    print(f"{minimum(ProcessList)}")
    print(f"{maximum(ProcessList)}")
    print(f"{sumNums(ProcessList)}")
# Identify function main for execute
if __name__ == "__main__":
    main()
