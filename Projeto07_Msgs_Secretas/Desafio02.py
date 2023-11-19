# Desafio: Criptografando e descriptografando mensagens
# Criptografe algumas mensagens, e as de um amigo junto com a chave secreta. Veja se seus amigos conseguem descriptografá-las usando o programa deles! 


def main():
    # A list of letters for encryption
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Capture the message from the user
    message = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

    # This variable will store the encrypted message
    encrypted_message = ""

    # Capture the secret key
    key = int(input("Por favor, entre a chave: "))

    # Iterate through each character in the message
    for char in message:
        if char in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.find(char)

            # Add the secret key to find the position of the encrypted character
            new_position = (position + key) % 26

            # Append the encrypted letter to the message
            encrypted_message += alphabet[new_position]
        else:
            # Some characters are not in the alphabet, so simply add them to the encrypted message
            encrypted_message += char

    print("Sua mensagem criptografada é: " + encrypted_message)

if __name__ == "__main__":
    main()
