# 03. Escreva um programa que leia um conjunto de 100 números inteiros e exiba o valor médio dos mesmos (com duas casas decimais).

# Creation of the function "average" for data processing
def average():
    # Variable initialization "sumNum"
    sumNum = 0
    # Repetition structure that receives an input, this input is added to the initialized variable "sumNum", this execution is repeated 100 times. After adding all 100 numbers, divide by 100 to find the average
    for count in range(0, 100):
        # Data entry
        count = int(input())
        # Cumulative sum
        sumNum += count
    # Division for the media
    sumNum /= 100
    return round(sumNum, 2)
# Creating the main function
def main():
    # The variable "av" receives the call to the "average" function, receiving the average value of 100 numbers
    av = average()
    # Prints the result of the variable "av"
    print(f"{av:.2f}")
# Identify function main for execute
if __name__ == "__main__":
    main()