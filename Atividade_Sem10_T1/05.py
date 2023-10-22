# 05. Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.

# Creation of the function "highterNum" for data processing
def highterNum():
    # Variable "maxNum" is initialized with value 0
    maxNum = 0
    # Repetition structure that receives an input and compares it with the variable "maxNum", if it is greater, the variable "" receives the value of the variable "". This process is repeated 100 times by the retention structure
    for count in range(100):
        # Data entry
        count = int(input())
        # Conditional structure that will tell you the largest number among the 100 data, comparing and saving it in the variable "maxNum"
        if (count > maxNum):
            maxNum = count
    return maxNum
# Creating the main function
def main():
    # The variable "num" receives the call to the "highterNum" function
    num = highterNum()
    # Shows the result of the variable "result" on the screen
    print(f"{num}") 
# Identify function main for execute
if __name__ == "__main__":
    main() 