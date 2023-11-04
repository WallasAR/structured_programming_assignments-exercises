# 05. Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.

# Creation of the function "isPrime" for data processing
def isPrime(num):
    # Check if the number is less than or equal to 1
    if num <= 1:
        # If it is, return False
        return False
    for i in range(2, int(num**0.5) + 1):
        # Use a for loop to check divisors from 2 to the square root of the number plus 1
        if num % i == 0:
            # If any divisor is found, return False as the number is not prime
            return False
     # If no divisors are found, return True, indicating the number is prime
    return True
# Creating the main function
def main():
    # Variables "x" and "y" receives an inputs and all is converted to the integer type
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    print(f"Os números primos entre o intervalo {x} a {y} é:")
    
    for num in range(x, y + 1):
        if isPrime(num):
            # Display the result
            print(f"{num}")
# Identify function main for execute
if __name__ == "__main__":
    main()