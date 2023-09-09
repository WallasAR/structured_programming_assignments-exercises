# 04. Escreva um programa que leia um valor inteiro e mostra na tela no valor booleano True caso o número lido seja maior que 100 ou False caso contrário.

# Processing
def verif(var):
    # Return True or False (bool value)
    return bool(var > 100)

# Main function
def main():
    # Variable "var" receives input and converts to type integer
    var = int(input("\nDigite um valor inteiro: "))
    # The "result" variable receives a call to the "verif" function, giving the necessary parameters and receiving the result immediately afterwards
    result = verif(var)
    # Prints the result of the "result" variable on the screen
    print(f"\nO valor dado é maior que 100?\nResposta: {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()

# Note: In run.codes the code has made with conndictional structure, this version is correct for what was proposed.