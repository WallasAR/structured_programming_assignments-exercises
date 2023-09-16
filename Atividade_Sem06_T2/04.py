# 04. Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais! Sabendo que 1 ano terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.

# Processing function
def spaceYears(Year):
    # returns the result of the operation with a rounded number and then transformed into an integer type
    return int(round(Year/2, 2))

def main():
    # The "earthYears" variable receives input and is converted to integer type
    earthYears = int(input("Digite os anos terrestres: "))
    # The variable "result" receives the function call "spaceYears", sending the necessary parameters and receiving the result
    result = spaceYears(earthYears)
    # Prints the result of the "result" variable on the screen
    print(f"Anos espaciais correspondentes: {result} anos")

# Identify function main for execute
if __name__ == "__main__":
    main()