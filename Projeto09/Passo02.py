# Etapa 2: Traduzindo frases 

def main():

    textSpeakDictionary = {
        "rs" : "risos",  
        "tmb" : "também" 
    }

    sentence = input("Insira uma frase para traduzir: ").lower() 
    wordsToTranslate = sentence.split()
    translatedSentence = ""

    for word in wordsToTranslate: 
        if word in textSpeakDictionary: 
            translatedSentence += textSpeakDictionary[word] + " "
        else:
            translatedSentence += word + " "

    

if __name__ == "__main__":
    main()