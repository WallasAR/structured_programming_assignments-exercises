# Passo 2: Criptografando mensagens 

def main():
    # A list of letters for encryption
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Capture the message from the user
    message = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

    # This variable will store the encrypted message
    encrypted_message = ""

    # Capture the secret key
    key = int(input(("Por favor, entre a chave: ")))

    # Iterate through each character in the message
    for char in message:
        if char in alphabet:
            # Find the position of the character in the alphabet
            # For example, 'a' is at position 0, 'e' is at position 4, etc.
            position = alphabet.find(char)

            # Add the secret key to find the position of the encrypted character
            new_position = (position + key) % 26  # % 26 means 'wrap around to 0 when you reach 26'

            # Append the encrypted letter to the message
            # The encrypted letter is in the alphabet at the new_position
            encrypted_message += alphabet[new_position]
        else:
            # Some characters (e.g., '£', '?') are not in the alphabet,
            # So simply add the encrypted letter to the message
            encrypted_message += char

    print(("Sua mensagem criptografada é: " + encrypted_message))

if __name__ == "__main__":
    main()
