# 2. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
# a) preencha com 0 (zero) e imprima a lista;
# b) preencha com os números de 1 a n e imprima a lista;
# c) preencha com valores inteiros lidos pelo teclado e imprima a lista;
# d) preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert para sempre incluir os elementos no início da lista;
 
# Function that creates a list - all values ​​equal to 0 - with a certain amount passed per parameter
def zeroValList(amount):
    # List initialization
    zeroArr = []
    # Filling the list with zeros
    for count in range(amount):
        # Method that places numbers in the list
        zeroArr.append(0)
    # Returns the list
    return zeroArr

# Function that generates a sequential list with the last number given as a parameter, the detailed explanation is similar to the "zeroValList" function
def seqList(num):
    seqArr = []
    # Filling the list with sequential numbers
    for count in range(num):
        seqArr.append(count + 1) # (count + 1) -> Prevents index zero from being placed in the list

    return seqArr

# Function that receives a certain amount of numbers (passed as a parameter) and generates a list of these numbers
def inputList(num):
    inputArr = []
    # Repetition structure that allows data entry and addition to the list the given number of times
    for count in range(num):
        nums = int(input(f"Digite o {count + 1}º número: "))

        inputArr.append(nums)

    return inputArr
# Function to fill the list in reverse order with values ​​given by the user, the number of numbers is also passed as a parameter in this function
def reverseList(num):
    reverseArr = []
    # Repetition structure that allows data entry and addition always to the beginning of the list (insert method is responsible for this)
    for count in range(num):
        nums = int(input(f"Digite o {count + 1}º valor inteiro para a ordem inversa: "))

        reverseArr.insert(0, nums)

    return reverseArr
# Creating the main function
def main():
    # Variable "valNum" receives an input and is then converted to the integer type, it is responsible for giving the quantity parameter to the subroutines
    valNum = int(input("Digite um número inteiro (n): "))
    # Variable that receives function call "zeroValList"
    zeroList = zeroValList(valNum)
    # Variable that receives function call "seqList"
    sList = seqList(valNum)
    # Variable that receives function call "inputList"
    inpList = inputList(valNum)
    # Variable that receives function call "reverseList"
    revList = reverseList(valNum)
    # Shows the user the list with zeros, the sequential list, the list with numbers read and the reverse list of numbers read by him
    print(f"\nLista preenchida com zeros: {zeroList}\nLista preenchida com números de 1 a n: {sList}\nLista preenchida com valores lidos: {inpList}\nLista preenchida na ordem inversa: {revList}\n")
# Identify function main for execute
if __name__ == "__main__":
    main()