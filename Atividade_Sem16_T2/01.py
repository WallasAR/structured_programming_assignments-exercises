# 01.Escreva um programa que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada. Inclua as vogais com acentos na contagem.

def countVowels(text):
    vowels = "aeiouáéíóúâêîôûàèìòùãẽĩõũ"
    normalized_vowels = "aeiou" * 5 
    vowel_counts = {v: 0 for v in normalized_vowels}

    for char in text.lower():
        if char in vowels:
            normalized_char = normalized_vowels[vowels.index(char)]
            vowel_counts[normalized_char] += 1

    return vowel_counts

def main():
    texto = input().strip()

    resultado = countVowels(texto)

    for vowel, count in resultado.items():
        if count >= 0:
            print(f"{vowel.upper()}: {count}")  

if __name__ == "__main__":
    main()