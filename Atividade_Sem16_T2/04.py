# 04.Suponha que vamos jogar um dado e queremos saber quantas vezes cada face (de 1 a 6) caiu. Faça um programa que leia o resultado de cada jogada do dado e armazena em um dicionário. A face do dado é a chave para o dicionário e a leitura de um valor 0 (zero) na face encerra o jogo. Mostre quantas vezes o dado foi lançado e quantas vezes cada face saiu. A leitura do valor 0 (zero) para a face encerra o jogo e mostra o resultado.

# Function to collect and count results from rolling a six-sided die
def countFacesData():
    results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # Initialize a dictionary to store frequencies of each face
    total_rolls = 0  # Initialize a variable to count the total number of rolls

    # Loop to input results until 0 is entered
    while True:
        result = int(input("Digite o resultado da jogada: "))  # Input a result from rolling the die
        if result == 0:
            break  # Break out of the loop if 0 is entered
        if result in results:  # Check if the result is a valid face (1 to 6)
            results[result] += 1  # Increment the count for the corresponding face
            total_rolls += 1  # Increment the total number of rolls
        else:
            print("Resultado inválido. Digite um número de 1 a 6.")  # Display a message for invalid input

    # Print the total number of rolls and the frequencies of each face
    print(f"Quantidade total de jogadas: {total_rolls}\n{results}")

# Main function
def main():
    countFacesData()  # Call the countFacesData function

# Execute the main function if this script is executed directly
if __name__ == "__main__":
    main()
