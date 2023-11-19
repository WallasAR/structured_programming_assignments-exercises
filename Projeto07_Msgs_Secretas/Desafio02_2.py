# Desafio: Melhorando sua cifra 
# Alguém consegue descriptografar suas mensagens sem a chave? Você consegue modificar seu programa para tornar mais difícil que as pessoas quebrem suas mensagens? Veja aqui algumas idéias: 
# Embaralhe as letras na sua variável alfabeto ; 
# Acrescente 1 à chave cada vez que uma letra for criptografada; 
# Remova todos os espaços e outros caracteres da mensagem criptografada. 


import random

def main():
    # A list of letters for encryption
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(original_alphabet)  # Convert the alphabet string to a list

    # Shuffle the alphabet
    random.shuffle(alphabet)

    # Capture the message from the user
    message = input("Por favor, entre com uma mensagem para criptografar: ").lower()

    # This variable will store the encrypted message
    encrypted_message = ""

    # Capture the initial secret key
    key = int(input("Digite a chave para criptografia (um número inteiro): "))

    # Iterate through each character in the message
    for char in message:
        if char in original_alphabet:
            # Find the position of the character in the original alphabet
            position = original_alphabet.find(char)

            # Add the secret key to find the position of the encrypted character
            new_position = (position + key) % 26

            # Increment the key for the next character
            key += 1

            # Append the encrypted letter to the message
            encrypted_message += alphabet[new_position]
        else:
            # Some characters are not in the alphabet, so simply ignore or add them to the encrypted message
            pass

    # Remove spaces and special characters from the encrypted message
    encrypted_message = ''.join([char for char in encrypted_message if char.isalpha()])

    print("Sua mensagem criptografada é: " + encrypted_message)

if __name__ == "__main__":
    main()
