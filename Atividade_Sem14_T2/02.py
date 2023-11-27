# 2. Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, a quantidade de números negativos e a soma dos números positivos dessa lista.

def readRealNumbers():
    # Initialize the empty list to store the real numbers
    real_numbers = []

    # Read the 10 real numbers
    for i in range(10):
        num = int(input(f"Digite o {i + 1}º número: "))
        # Add the number to the list
        real_numbers.append(num)
    # Returns the list filled with real numbers
    return real_numbers 

# Main function
def main():
    # Call the function to read the real numbers
    numbers = readRealNumbers()

    # Initialize counters
    count_negatives = 0
    sum_positives = 0

    # Iterate through the list to calculate the number of negatives and the sum of positives
    for num in numbers:
        if num < 0:
            # Increment the negative number counter
            count_negatives += 1  
        else:
            # Add positive numbers
            sum_positives += num  
    # Print the complete list, the number of negative numbers and the sum of positive numbers
    print(f"Lista completa: {numbers}\nQuantidade de números negativos: {count_negatives}\nSoma dos números positivos: {sum_positives}")

# Identify function main for execute
if __name__ == "__main__":
    main()
