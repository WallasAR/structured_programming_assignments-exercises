# Etapa 4: Arrumando seu programa 


textSpeakDictionary = {
    "rs": "risos",
    "tmb": "também",
    "VC": "você",
    "pq": "porque",
}

def displayMenu():
    print("trdtr de exprss")
    print("=" * 13)
    print("Menu:")
    print(" c = converter uma frase")
    print(" p = imprimir dicionário")
    print(" a = adicionar uma palavra")
    print(" d = remover uma palavra")
    print(" q = sair")

def convertSentence():
    sentence = input("Insira uma frase para traduzir:").lower()
    translatedSentence = ""

    for char in "?!.,":
        sentence = sentence.replace(char,"")

    listOfWords = sentence.split()

    for word in listOfWords:
        if word in textSpeakDictionary:
            translatedSentence += textSpeakDictionary[word] + " "
        else:
            translatedSentence += word + " "

    print("==>")
    print(translatedSentence)

def addDictionaryItem():
    txtToAdd = input("Insira a expressão a ser adicionada ao dicionário: ")
    meaning = input("O que ela significa: ")

    if txtToAdd not in textSpeakDictionary:
        textSpeakDictionary[txtToAdd] = meaning
    else:
        print("Essa palavra já existe no dicionário!")

def deleteDictionaryItem():
    txtToDelete = input("Insira a expressão a ser removida do dicionário: ")

    if txtToDelete in textSpeakDictionary:
        del textSpeakDictionary[txtToDelete]
    else:
        print("Essa palavra não está presente no dicionário!")

def main():
    running = True

    displayMenu()

    while running:
        menuChoice = input(">_").lower()

        if menuChoice == 'c':
            convertSentence()
        elif menuChoice == 'p':
            print(textSpeakDictionary)
        elif menuChoice == 'a':
            addDictionaryItem()
        elif menuChoice == 'd':
            deleteDictionaryItem()
        elif menuChoice == 'q':
            running = False
        else:
            print("Escolha inválida!")

if __name__ == "__main__":
    main()