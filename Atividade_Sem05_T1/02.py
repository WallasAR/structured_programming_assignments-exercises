# 02. Escreva um programa que ler o valor do lado de um quadrado. Calcule o mostre a área e o perímetro desse quadrado. OBS: Mostre o resultado com 4 casas decimais, alinhado à direta com 10 espaços na tela.

# Processing function
def squareArPer(side):
    # Variable "side" receives the operation that calculates the area of ​​the square and then stores the result
    area = side**2
    # Likewise, the variable "perim" receives the operation that calculates the perimeter of the square and stores the result in itself
    perim = 4*side
    return area, perim

# Main function
def main():
    # The "sideVal" variable receives input and is converted to float type
    sideVal = float(input("Digite o valor do lado do quadrado: "))
    # The variables "resultA, resultP" receive a call to the function "squareArPer", giving the necessary parameters and receiving the respective results according to the return "return area, perim"
    resultA, resultP = squareArPer(sideVal)
    # Prints on the screen the results of the variables "resultA" and "resultP" duly treated with right alignment and four decimal places
    print(f"{resultA:10.4f}\n{resultP:10.4f}")

# Identify function main for execute
if __name__ == "__main__":
    main()