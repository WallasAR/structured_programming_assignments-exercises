# 3. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
# a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro)
# casas decimais.
# b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa
# decimal. Se n = 0, imprima “SEM NOTAS”.
# c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
# Dica: certifique-se de ler apenas um caractere com input()[0]

# Function to create a list of floating-point numbers in inverse order
def reverseFloatList(num):
    # List initialization
    floatList = []
    # Repetition structure that allows data entry and addition always to the beginning of the list (insert method is responsible for this)
    for count in range(num):
        floatVal = float(input(f"Digite o {count + 1}º valor real: "))

        floatList.insert(0, floatVal)
    # Shows the user the reverse list
    print(f"\nLista de valores reais: {floatList}")

# Function to input and calculate the average of grades
def classResults(num):
    noteList = []
    # Initialization of the variable that will store the sum of all notes
    sumNotes = 0

    # If 'num' is zero, print an empty list and "SEM NOTAS"
    if (num == 0):
        print(f"\nLista de notas: {noteList}\nSEM NOTAS")
    else:
        # Loop to get 'num' grades from the user, calculate the sum, and append them to the list
        for count in range(num):
            note = float(input(f"Digite a {count + 1}º nota: "))
            # Method that places numbers in the list
            noteList.append(note)

            sumNotes += note
        # Calculate the average
        average = sumNotes / num
        # Shows the user the grades and their respective average
        print(f"\nLista de notas: {noteList}\nMédia: {average:.1f}")

# Function to count vowels and create a list of consonants
def vowelsAndConsonants(num):
    letterList = []
    vowels = "aeiouAEIOU"
    countVowels = 0

    # Loop to get 'num' letters from the user, count vowels, and create a list of consonants
    for count in range(num):
        letter = str(input(f"Digite a {count + 1}º letra: ")[0])

        letterList.append(letter)

        if letter in vowels:
            # Vowel counter gets 1 more
            countVowels += 1
            # If the letter is a vowel, remove it from the list
            letterList.remove(letter)
    # Shows the user the number of vowels and the list of consonants
    print(f"\nQuantidade de vogais: {countVowels}\nLista de consoantes: {letterList}")
# Creating the main function
def main():
    # Variable "valNum" receives an input and is then converted to the integer type, it is responsible for giving the quantity parameter to the subroutines
    valNum = int(input("Digite um número inteiro: "))
    # Variable that receives function call "inverseFloatList"
    reverseFloatList(valNum)
    # Variable that receives function call "classResults"
    classResults(valNum)
    # Variable that receives function call "vowelsAndConsonants"
    vowelsAndConsonants(valNum)
# Identify function main for execute
if __name__ == "__main__":
    main()