# 05. Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. Por exemplo, se o número lido for 5678 deverá ser mostrado 8765.

# Processing function
def invert(n):
    # The "numStr" variable receives the iteration of parts in descending form
    numStr = n[3] + n[2] + n[1] + n[0]
    return numStr

# Main function
def main():
    # The "num" variable receives input and is converted to string type
    num = str(input("Digite um número inteiro entre 1000 e 9999: "))
    # The "result" variable receives a call to the "invert" function, giving the necessary parameter and receiving the result immediately afterwards
    result = invert(num)
    # Prints the result of the "result" variable on the screen
    print(f"\nA forma inversa deste número é {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()