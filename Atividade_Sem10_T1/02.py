# 02. Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade de números pares e números ímpares contidos no mesmo.

# Creation of the function "numDef" for data processing
def numDef():
    # The variables "countP" and "countI" are initialized with a value of 0
    countP = 0
    countI = 0
    # Repetition structure that receives 100 entries and then checks whether it is even, if so, one more is added to the "countP" variable, otherwise one more is added to the "countI" variable
    for count in range(0, 100):
        # Data entry
        count = int(input())
        # Conditional structure that checks if the number is even
        if count % 2 == 0:
            countP += 1
        else:
            countI += 1
    return countP, countI
# Creating the main function
def main():
    # Variables "P" and "I" receive, respectively, the return of the "numDef" function (return countP, countI)
    P, I = numDef()
    # Shows the value of the variables P and I
    print(f"{P}\n{I}")
# Identify function main for execute
if __name__ == "__main__":
    main()