# Desafio: Chaves variáveis 
# Modifique o programa de criptografia acima, de modo que o usuário possa entrar com sua própria chave. Você precisará capturar a entrada do usuário, e armazenar em uma variável chave. Lembre-se de usar a função int() para converter a entrada em um número inteiro. 


def main():
    # List of letters to encrypt
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Request the user's secret key
    key = int(input("Digite a chave para criptografia (um número inteiro): "))

    letter = input("Por favor, entre com uma letra para criptografar: ")

    # Find the position of the letter in the alphabet
    position = alphabet.find(letter)

    # Add the secret key to find the position of the encrypted letter
    new_position = (position + key) % 26

    # The encrypted letter is in the alphabet at the new position
    encrypted_letter = alphabet[new_position]

    print("Sua letra criptografada é " + encrypted_letter)

if __name__ == "__main__":
    main()

