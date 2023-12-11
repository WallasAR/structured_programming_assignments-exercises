# 02.Escreva um programa que leia um texto e calcula a frequência relativa de cada letra no texto. Desconsidere a diferença entre maiúsculas e minúsculas mas considere caracteres acentuados. Por exemplo, para a frase: 
# Se, a princípio, a ideia não é absurda, então não há esperança para ela. (Albert Einstein)
# Retorna o dicionário:
# {'S': 4, 'E': 10, 'A': 15, 'P': 4, 'R': 5, 'I': 7, 'N': 7, 'C': 2, 'O': 4, 'D': 2, 'B': 2, 'U': 1, 'T': 3, 'H': 1, 'L': 2}

# Function to normalize characters by removing accents
def normalizeChar(char):
    # Dictionary mapping accented characters to their corresponding non-accented characters
    accents = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ã': 'a', 'ẽ': 'e', 'ĩ': 'i', 'õ': 'o', 'ũ': 'u',
        'ç': 'c'
    }

    # Return the non-accented character if found, otherwise return the original character
    return accents.get(char.lower(), char)

# Function to calculate the frequency of alphabetic characters in a given text
def frequencyCalc(text):
    frequency = {}  # Initialize an empty dictionary to store character frequencies

    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            # Normalize the character by removing accents and convert it to uppercase
            char_without_accent = normalizeChar(char).upper()

            # Update the frequency count for the character in the dictionary
            if char_without_accent in frequency:
                frequency[char_without_accent] += 1
            else:
                frequency[char_without_accent] = 1

    return frequency  # Return the dictionary containing character frequencies

# Main function
def main():
    text = input("Digite o texto desejado: ").strip()  # Input text to analyze

    result = frequencyCalc(text)  # Calculate character frequencies using frequencyCalc function

    print(f"A frequência relativa de cada letra é:\n{result}")  # Print the resulting dictionary containing character frequencies

# Execute the main function if this script is executed directly
if __name__ == "__main__":
    main()
