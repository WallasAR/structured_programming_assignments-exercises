# 05. Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem “Nota inválida.” caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar uma nota válida, o aluno deve ver seu conceito, segundo a tabela:
# Conceito      Nota
# A             >= 8,5.
# B             >= 7,0
# C             >= 5,0
# D             >= 4
# E             >= 0

# Creation of the function "finalNote" for data processing
def finalNote():
    # Repetition structure that runs indefinitely
    while True:
        # Variable "StudNote" receives input, then converted to float type
        StudNote = float(input("Digite a nota do aluno(a): "))
        # Conditional structure that checks the output corresponding to the student's grade read
        if (StudNote > 10 or StudNote < 0):
            print("Nota inválida.")
        elif (8.5 <= StudNote <= 10):
            return "A"
        elif (7.0 <= StudNote < 8.5):
            return "B"
        elif (5.0 <= StudNote < 7.0):
            return "C"
        elif (4.0 <= StudNote < 5.0):
            return "D"
        else:
            return "E"
# Creating the main function
def main():
    # The variable "result" receives the call to the "finalNote" function
    result = finalNote()
    # Prints the value of the "result" variable on the screen
    print(f"Conceito Final: {result}")
# Identify function main for execute
if __name__ == "__main__":
    main()