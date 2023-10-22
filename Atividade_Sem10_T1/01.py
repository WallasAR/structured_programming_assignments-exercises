# 01. Escreva um programa que mostre todos os números inteiros de 1 a 50 (um por linha).

# Creation of the function "showNum" for data processing
def showNum():
    # Repetition structure that uses the variable "count" in a range from 1 to 50
    for count in range(1, 51):
        # Shows the value of the variable "count" until the counter reaches the end of the interval proposed by the structure
        print(count)
# Creating the main function
def main():
    # The function "showNum" is called
    showNum()
# Identify function main for execute
if __name__ == "__main__":
    main()