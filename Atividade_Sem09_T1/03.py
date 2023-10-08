# 03. Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. Separe esses valores com um hífen.

# Creation of the function "verify" for data processing
def verify(b, h):
    # Compound conditional structure that checks whether the given values ​​are equal, if so there will be a one-word return, otherwise calculations will be made and returned
    if (b == h):
        return "É um QUADRADO"
    else:
        perim = b + b + h + h
        area = b * h
        return f"É um RETÂNGULO: \n{perim} - {area}"

# Creating the main function
def main():
    # The variables "base" and "height" receive inputs and are all converted to the integer type
    base = int(input("Informe a base da figura geométrica: "))
    height = int(input("Informe a altura da figura geométrica: "))
    # The variable "resultVerif" receives the call to the "verify" function, receiving the corresponding return
    resultVerif = verify(base, height)
    # Prints the value of the variable "resultVerif" on the screen
    print(f"{resultVerif}")

# Identify function main for execute
if __name__ == "__main__":
    main()