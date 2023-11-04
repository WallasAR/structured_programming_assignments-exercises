# 01. Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que:
# N ! = 1 x 2 x 3 x ... x N-1 x N
# 0 ! = 1

# Creation of the function "factorial" for data processing
def factorial(val):
    # Initialize a variable to store the factorial value, starting at 1
    factor = 1
     # Check if the input value is non-negative
    if (val >= 0):
        # Loop from the input value down to 1 
        for i in range(val, 0, -1):
            # Multiply the current factor by the current value of i
            factor *= i
    # Return the calculated factorial value
    return factor
# Creating the main function
def main():
    # Variable "val" receives an input and is then converted to the integer type
    val = int(input("Digite um número inteiro não negativo qualquer: "))
     # Calculate the factorial of the entered value
    factor = factorial(val)
    # Display the result
    print(f"{val}! = {factor}")
# Identify function main for execute
if __name__ == "__main__":
    main()