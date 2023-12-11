# 02.Escreva um programa que leia um texto e calcula a frequência relativa de cada letra no texto. Desconsidere a diferença entre maiúsculas e minúsculas mas considere caracteres acentuados. Por exemplo, para a frase: 
# Se, a princípio, a ideia não é absurda, então não há esperança para ela. (Albert Einstein)
# Retorna o dicionário:
# {'S': 4, 'E': 10, 'A': 15, 'P': 4, 'R': 5, 'I': 7, 'N': 7, 'C': 2, 'O': 4, 'D': 2, 'B': 2, 'U': 1, 'T': 3, 'H': 1, 'L': 2}

def normalizeChar(char):
    accents = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ã': 'a', 'ẽ': 'e', 'ĩ': 'i', 'õ': 'o', 'ũ': 'u',
        'ç': 'c'
    }

    return accents.get(char.lower(), char)

def frequencyCalc(text):
    frequency = {}

    for char in text:
        if char.isalpha():
            char_without_accent = normalizeChar(char)
            char_without_accent = char_without_accent.upper()
            if char_without_accent in frequency:
                frequency[char_without_accent] += 1
            else:
                frequency[char_without_accent] = 1

    return frequency

def main():
    texto = input().strip()

    result = frequencyCalc(texto)

    print(f"{result}")

if __name__ == "__main__":
    main()