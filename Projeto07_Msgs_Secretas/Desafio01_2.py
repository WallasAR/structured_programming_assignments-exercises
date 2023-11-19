# Desafio: Criptografando e descriptografando caracteres 
# Use seu programa para criptografar: A letra 'd' usando a chave secreta 7; 
# A letra 'x' usando a chave secreta 4; 
# Você consegue usar seu programa para descriptografar esta mensagem: omqemd (a chave secreta é 12) 


def cipher(text, key, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in text:
        if letter in alphabet:
            position = alphabet.find(letter)
            if mode == 'encrypt':
                newPosit = (position + key) % 26
            else:
                newPosit = (position - key) % 26
            result += alphabet[newPosit]
        else:
            result += letter

    return result

def main():
    # Let's encrypt the letters 'd' and 'x'
    encrypted_d = cipher('d', 7, 'encrypt')
    encrypted_x = cipher('x', 4, 'encrypt')

    print(f"letra 'd' criptografada com chave 7: {encrypted_d}")
    print(f"letra 'x' criptografada com chave 4: {encrypted_x}")

    # Decrypt the message 'omqemd' with the key 12
    decrypted_message = cipher('omqemd', 12, 'decrypt')
    print(f"Mensagem descriptografada: {decrypted_message}")

if __name__ == "__main__":
    main()
