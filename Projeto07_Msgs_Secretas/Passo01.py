# Passo 1: Criptografando mensagens 

def main():
    # List of letters for encryption
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # The secret key is 3
    key = 3

    letter = input("Por favor, entre com uma letra para criptografar: ")

    # Find the position of the letter in the alphabet
    # Example: 'a' is at position 0, 'e' is at position 4, etc.
    position = alphabet.find(letter)

    # Add the secret key to find the position of the encrypted letter
    new_position = (position + key) % 26  # % 26 means 'wrap around to 0 when you reach 26'

    # The encrypted letter is in the alphabet at the new position
    encrypted_letter = alphabet[new_position]

    print("Sua letra criptografada é " + encrypted_letter)

if __name__ == "__main__":
    main()
