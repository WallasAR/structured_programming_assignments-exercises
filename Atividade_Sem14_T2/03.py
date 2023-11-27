# 3. Escreva um programa que leia uma lista com 20 números inteiros. Escreva os elementos da lista eliminando elementos repetidos.

def removeDuplicates(num_list):
    # Initialize an empty list to store unique elements
    unique_list = []

    # Iterate through the input list
    for num in num_list:
        # If the element is not already in the unique list, add it
        if num not in unique_list:
            unique_list.append(num)

    return unique_list  # Return the list containing unique elements

def readIntNumbers():
    # Function to read 20 integers and store them in a list
    numbers = []
    for i in range(20):
        num = int(input(f"Digite o número {i + 1}: "))
        numbers.append(num)
    return numbers

# Main function
def main():
    # Read 20 integers
    numbers = readIntNumbers()

    # Call the function to remove duplicates from the list
    unique_numbers = removeDuplicates(numbers)

    # Print the list without duplicate elements
    print(f"Lista sem elementos repetidos: {unique_numbers}")
    
# Identify function main for execute
if __name__ == "__main__":
    main()
