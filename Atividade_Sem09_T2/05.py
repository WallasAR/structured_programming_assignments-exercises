# 05. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a) "Telefonou para a vítima ?"
# b) "Esteve no local do crime ?"
# c) "Mora perto da vítima ?"
# d) "Devia para a vítima ?"
# e) "Já trabalhou com a vítima ?"

# Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# Subroutine that counts the number of "S" responses and sends it to the other subroutine to do the processing
def count(a01, a02, a03, a04, a05):
    # Variable "positiveResp" is created with value "0", it will be the counter
    positiveResp = 0
    # Conditional structure that checks the user's responses, if it is "S" the variable "" receives the addition of one more
    if (a01.upper() == "S"):
        positiveResp += 1
    if (a02.upper() == "S"):
        positiveResp += 1
    if (a03.upper() == "S"):
        positiveResp += 1
    if (a04.upper() == "S"):
        positiveResp += 1
    if (a05.upper() == "S"):
        positiveResp += 1
    # returns the value of the variable "positiveResp"
    return positiveResp

# Creation of the function "Interrogation" for data processing
def interrogation(a01, a02, a03, a04, a05):
    # Variable "positiveResp" receives function call "count", receiving the number of positive responses
    positiveResp = count(a01, a02, a03, a04, a05)

    # Conditional structure that checks how many responses are positive for a conclusion
    if (positiveResp == 2):
        return "Suspeito"
    if (3 <= positiveResp <= 4):
        return "Cúmplice"
    if (positiveResp == 5):
        return "Assassino"
    else:
        return "Inocente"

# Creating the main function
def main():
    # Variables "answer01, answer02, answer03, answer04, answer05" receive inputs
    answer01 = str(input("I) Telefonou para a vítima ? S OU N!?\n")).strip()
    answer02 = str(input("II) Esteve no local do crime ? EIN?! \n")).strip()
    answer03 = str(input("III) Mora perto da vítima ?\n")).strip()
    answer04 = str(input("IV) Devia para a vítima ?\n")).strip()
    answer05 = str(input("V) Já trabalhou com a vítima ? RESPONDA!\n")).strip()
    # The variable "result" receives the call to the "interrogation" function, Receiving the corresponding conclusion
    result = interrogation(answer01, answer02, answer03, answer04, answer05)
    # Prints the value of the variable "result" on the screen
    print(f"\n\n***** Resultado do Interrogatório *****\nNome: Alan Turing\nSexo: Masculino\nSituação: {result}\n")
# Identify function main for execute
if __name__ == "__main__":
    main()