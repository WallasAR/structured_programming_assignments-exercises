# 4. Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar e dado por: (x1 ∗ y1) + (x2 ∗ y2) + (x3 ∗ y3) + ⋯ + (xn ∗ yn).

def scalarProduct(list1, list2):
    product = ""  # Initialize an empty string to hold the product representation
    total = 0  # Initialize the total product

    for i in range(len(list1)):
        if i > 0:
            product += " + "  # Add a plus sign if it's not the first term
        product += f"({list1[i]} x {list2[i]})"  # Represent each multiplication
        total += list1[i] * list2[i]  # Calculate the total scalar product

    return f"{product} = {total}"  # Return the product expression and the total product


def read_real_numbers():
    numbers = []  # Initialize an empty list to store numbers

    for i in range(5):
        num = int(input(f"Insira o número {i + 1}: "))  # Read integer inputs
        numbers.append(num)  # Add the number to the list

    return numbers  # Return the list of numbers

# Main function
def main():
    print("Insira os elementos do primeiro conjunto de números: ")
    set1 = read_real_numbers()  # Read the first set of real numbers

    print("\nInsira os elementos do segundo conjunto de números: ")
    set2 = read_real_numbers()  # Read the second set of real numbers

    # Calculate the scalar product of the two sets
    result = scalarProduct(set1, set2)

    # Print the sets and the scalar product
    print(f"Primeiro conjunto: {set1}\nSegundo Conjunto: {set2}\nProduto escalar: {result}")  # Display the sets and the scalar product

# Identify function main for execute
if __name__ == "__main__":
    main()

