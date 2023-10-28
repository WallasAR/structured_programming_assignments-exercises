# 04. Escreva um programa que leia número inteiro qualquer e mostre na forma invertida. Por exemplo:

# Para o número lido      A saída será
# 123                     321
# 1895                    5981

# Creation of the function "invert" for data processing
def invert(num):
    # Variable "invertNum" is initialized with value 0
    invertNum = 0
    # Repetition structure that executes while the variable "num" is greater than 0
    while (num > 0):
        # Variable "unit" will be responsible for separating the last number
        unit = num % 10
        # variable "invertNum" receives calculation to recreate the number in its inverse form
        invertNum = invertNum * 10 + unit
        # The variable "num" receives integer division by 10, so that the process is repeated for all numbers
        num //= 10
    # Returns the value of the variable "invertNum"
    return invertNum
# Creating the main function
def main():
    # Variable "num" receives input, then converted to integer type
    num = int(input())
    # The variable "invertNum" receives the call to the "invert" function
    invertNum = invert(num)
    # Prints the value of the variable "invertNum" on the screen
    print(f"{invertNum}")
if __name__ == "__main__":
    main()