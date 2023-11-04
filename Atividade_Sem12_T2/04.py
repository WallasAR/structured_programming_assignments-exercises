# 04. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa que leia um número e determine se ele é ou não primo.

# Creation of the function "primeNum" for data processing
def primeNum(num):
    # Initialize a variable to check if the number has dividers (assumed True by default)
    dividers = True
    # Check if the number is less than or equal to 1
    if num <= 1:
        # If it is, then it's not considered prime
        dividers = False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                # If any divider is found, it's not considered prime
                dividers = False
                # Exit the loop early as we already found a divider
                break
    return dividers
# Creating the main function
def main():
    # Variable "num" receives an input and is then converted to the integer type
    num = int(input("Digite um número inteiro qualquer: "))
    # Call the "primeNum" function to check if the number is prime
    div = primeNum(num)
    # Display the result
    print(f"O número dado é primo?\nResposta: {div}")
# Identify function main for execute
if __name__ == "__main__":
    main()