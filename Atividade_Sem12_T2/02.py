# 02. A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n sempre será maior ou igual a 2.

# Creation of the function "fibonacciSeq" for data processing
def fibonacciSeq(num):
    # Initialize, respectively, the first and second Fibonacci numbers
    a = 0
    b = 1
     # Initialize the output as a string containing the first two Fibonacci numbers
    output = f"{a}, {b}"
    for count in range(2, num):
        # Calculate the next Fibonacci number by adding the previous two
        c = a + b
        # Append the calculated Fibonacci number to the output string
        output += f", {c}"
        # Update the first Fibonacci number with the second
        a = b
        # Update the second Fibonacci number with the calculated value
        b = c
    # Return the Fibonacci sequence as a string
    return output
# Creating the main function
def main():
    # Variable "num" receives an input and is then converted to the integer type
    num = int(input("Digite um número inteiro qualquer: "))
    # Generate the Fibonacci sequence
    output = fibonacciSeq(num)
    # Display the result
    print(f"A Sequência de Fibonacci respectiva é:\n{output}")
# Identify function main for execute
if __name__ == "__main__":
    main()