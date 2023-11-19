# Desafio: Calculadora do amor 
# Escreva um programa para avaliar quão duas pessoas são compatíveis, calculando seu placar de compatibilidade. O programa poderia percorrer cada caracter nos 2 nomes, e acrescentar pontos à variável placar cada vez que as letras são encontradas. Você pode decidir as regras para conceder pontos. Por exemplo, você poderia conceder pontos por vogais, ou caracteres que também estão na palavra “amor”:
 
# if char in "aeiou": 
#     placar = placar + 5 
# if char in "amor": 
#     placar = placar + 10 

# Você pode mostrar mensagens personalizadas, baseadas no placar de compatibilidade: 

# if placar < 10:
#     print("Esqueça esta pessoa! Nunca vai dar certo!") 


def loveCalculator(name1, name2):
    score = 0

    # Define the criteria for compatibility
    for char in name1.lower() + name2.lower():
        if char in "aeiou":
            score += 5
        if char in "amor":
            score += 10

    return score

def displayMessage(score):
    if score < 10:
        return "Esqueça esta pessoa! Nunca vai dar certo!"
    elif score < 50:
        return "Hmm... talvez uma pequena chance?"
    elif score < 80:
        return "Vocês dois têm futuro! Continuem tentando!"
    else:
        return "Vocês foram feitos para ficarem juntos! É o destino!"

def main():
    print("Calculadora do Amor <3 <3 <3")
    names = input("Insira os nomes de duas pessoas (separados por espaço):").split()

    if len(names) != 2:
        print("Por favor, digite exatamente dois nomes!")
        return

    name1, name2 = names[0], names[1]
    compatibility_score = loveCalculator(name1, name2)

    print(f"Pontuação de compatibilidade entre {name1} e {name2}: {compatibility_score}")
    message = displayMessage(compatibility_score)
    print(message)

if __name__ == "__main__":
    main()
