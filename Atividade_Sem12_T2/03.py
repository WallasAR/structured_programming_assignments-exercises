# 03. Sendo H = 1 + 1/2 + 1/3 + 1/4 + ⋯ 1/n, escreva um programa para calcular o valor de H. O número n é lido.

# Creation of the function "calc" for data processing
def calc(h):
    # Initialize a variable H to store the calculated value
    H = 0

    for i in range(1, h + 1):
        # Increment H by 1 divided by the current value of i
        H += 1 / i
    # Return the calculated value of H rounded to 4 decimal places
    return round(H, 4)
# Creating the main function
def main():
    # Variable "val" receives an input and is then converted to the integer type
    val = int(input("Informe o valor de H: "))
    # Call the "calc" function to calculate the harmonic number
    valH = calc(val)
    # Display the result with 4 decimal places
    print(f"O resultado obtido é igual a {valH:.4f}")
# Identify function main for execute
if __name__ == "__main__":
    main()