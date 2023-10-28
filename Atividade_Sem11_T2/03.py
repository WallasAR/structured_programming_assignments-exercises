# 03. Escreva um programa Python que apresente o menu de opções abaixo:
# OPÇÕES:
# 1 - SAUDAÇÃO
# 2 - BRONCA
# 3 - FELICITAÇÃO
# 0 - FIM

# O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:

# 1 - Olá. Como vai?
# 2 - Vamos estudar mais.
# 3 - Meus Parabéns!
# 0 - Fim de serviço.

# Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção inválida.”. Enquanto a opção for diferente de 0 (zero) deve-se continuar apresentando as opções. Obs: use como estrutura de repetição com teste no final e como estrutura condicional múltipla escolha.

# Creation of the function "menu" for data processing
def menu():
    # Repetition structure that runs indefinitely
    while True:
        # prints text on the screen
        print('''\nOPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')    
        # Variable "choice" receives input, then converted to integer type
        choice = int(input("\nOpção: "))
        # Conditional structure that checks the output corresponding to the number read from the user, 0 represents the end of the loop
        if (choice == 0):
            print("0 - Fim de serviço.")
            break
        elif (choice == 1):
            print("1 - Olá. Como vai?")
        elif (choice == 2):
            print("2 - Vamos estudar mais.")
        elif (choice == 3):
            print("3 - Meus Parabéns!")
        else:
            print("Opção inválida.")
# Creating the main function
def main():
    # Function call "menu" in the main routine
    menu()
# Identify function main for execute
if __name__ == "__main__":
    main()