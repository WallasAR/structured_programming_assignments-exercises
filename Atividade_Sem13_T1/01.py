# 1. Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.

# Function that will receive the user's numbers and place them in the list
def rList():
    # List initialization "arr"
    arr = []
    for count in range(10):
        nums = int(input(f"Digite o {count + 1}º número: "))
        # Method that places numbers in the list
        arr.append(nums)
    # Returns the list "arr" with all numbers already defined by the user
    return arr

# Function responsible for adding the numbers in the list
def sumListNum(arr):
    # Returns the sum of all numbers in the list
    return sum(arr)

# Function that multiplies the numbers in the list
def multipListNum(arr):
    # Initialization of the variable that will store the result of the multiplication
    result = 1
    # Checks if the counter variable is contained in the list, if it is, the variable "result" will receive the multiplication with the counter variable itself "num"
    for num in arr:
        result *= num
    # Returns the multiplication of all numbers in the list
    return result
# Creating the main function
def main():
    # Variable that receives function call "rList"
    inputNums = rList()
    # Variable that receives function call "sumListNum"
    sumNums = sumListNum(inputNums)
    # Variable that receives function call "MultipListNum"
    multipNum = multipListNum(inputNums)
    # Shows the list, addition and multiplication to the user
    print(f"\nLista: {inputNums}\nSoma dos números da lista: {sumNums}\nMultiplicação dos números da lista: {multipNum}\n")
# Identify function main for execute
if __name__ == "__main__":
    main()