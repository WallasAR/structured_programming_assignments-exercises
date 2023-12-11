# 01.Escreva um programa que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada. Inclua as vogais com acentos na contagem.

# Function to count vowels in a given text
def countVowels(text):
    # Define sets of vowels, including accented and special characters
    vowels = "aeiouáéíóúâêîôûàèìòùãẽĩõũ"
    # Define a normalized set of vowels with only standard characters
    normalized_vowels = "aeiou" * 5 
    # Initialize a dictionary to store counts of each normalized vowel
    vowel_counts = {v: 0 for v in normalized_vowels}

    # Loop through each character in the text (converted to lowercase)
    for char in text.lower():
        # Check if the character is a vowel
        if char in vowels:
            # Map the character to its corresponding normalized vowel
            normalized_char = normalized_vowels[vowels.index(char)]
            # Increment the count of the normalized vowel in the dictionary
            vowel_counts[normalized_char] += 1

    return vowel_counts  # Return the dictionary with vowel counts

# Main function
def main():
    text = input("Digite o texto desejado: ").strip()  # Input text to analyze

    result = countVowels(text)  # Call the countVowels function to get vowel counts

    # Loop through the resulting vowel count dictionary and print the counts
    for vowel, count in result.items():
        if count >= 0:  # Ensure the count is non-negative (always true)
            # Print the uppercase vowel and its count in the input text
            print("CONTAGEM DE VOGAIS")
            print("------------------")
            print(f"{vowel.upper()}: {count}")  

# Execute the main function if this script is executed directly
if __name__ == "__main__":
    main()
