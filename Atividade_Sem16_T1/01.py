# 01.Escreva um programa que leia uma chave e um valor, crie um dicionários com os valores lidos. A leitura de uma chave vazia finaliza a leitura do dicionário. Mostre o dicionário na tela; após, leia novamente uma chave e um valor e atualize o valor da chave no dicionário até que seja feita a leitura de uma chave vazia. Mostre novamente o dicionário na tela.


# Function to create a dictionary
def createDict():
    dictionary = {}  # Initializes an empty dictionary

    while True:
        # Reads user input for key
        key = str(input("Insira a chave (deixe em branco para sair): ").strip())  
        
        if key == "":  # Checks if the key is empty to break the loop
            break

        val = str(input("Digite o valor para a chave digitada: ").strip())  # Reads user input for value
        dictionary[key] = val  # Adds the key-value pair to the dictionary

    return dictionary  # Returns the created dictionary

# Main function
def main():
    # Calls createDict() to create a dictionary
    dictionary = createDict()  

    print(f"{dictionary}")  # Prints the dictionary

    # Loop to update the dictionary with new key-value pairs
    while True:
        key = str(input("Insira a nova chave para o dicionário (em branco para sair): ").strip())  # Reads user input for key
        
        # Checks if the key is empty to break the loop
        if key == "":  
            break
        
        val = str(input("Insira o novo valor: ").strip())  # Reads user input for value
        dictionary[key] = val  # Updates the value of the key in the dictionary

    print(f"{dictionary}")  # Prints the updated dictionary

# Identify function main for execute
if __name__ == "__main__":
    main()
