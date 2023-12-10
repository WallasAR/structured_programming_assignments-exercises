# Desafio: Adicionando traduções 
# Adicione mais algumas traduções ao programa acima. Por exemplo: 
# "vc" = "você❞ 
# "pq" = "porque❞ 


def main():
    textSpeakDictionary = {
        "rs": "risos",
        "tmb": "também",
        "vc": "você",
        "pq": "porque",
        "blz": "beleza",
        "fds": "fim de semana",
        "msg": "mensagem"
    }

    sentence = input("Insira uma frase para traduzir: ").lower()
    wordsToTranslate = sentence.split()
    translatedSentence = ""

    for word in wordsToTranslate:
        if word in textSpeakDictionary:
            translatedSentence += textSpeakDictionary[word] + " "
        else:
            translatedSentence += word + " "

    print("==>")
    print(translatedSentence)

if __name__ == "__main__":
    main()
