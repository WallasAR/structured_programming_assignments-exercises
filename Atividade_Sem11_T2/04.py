# 04. O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.
# CÓDIGO    PRODUTO         PREÇO (R$)
# H         Hamburger       5.50
# C         Cheeseburger    6.80
# M         Misto Quente    4.50
# A         Americano       7.00
# Q         Queijo Prato    4.00
# X         PARA TOTAL DA CONTA

 #Escreva um programa que leia o código de vários itens comprados por um freguês e acumule o total da compra. Ao finalizar com “X”, exiba o total a pagar.
# Observações:
# • Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção
# inválida.”.
# • Enquanto o código não for 'X' o programa deve continuar lendo os itens.
# Dica: Use upper() para ignorar a diferenças entre maiúscula e minúsculas; Use [0] para garantir que
# apenas o primeiro caractere digitado seja considerado. Por exemplo:
# codigo = input('Código: ').upper()[0]

# Creation of the function "burgerPlace" for data processing
def burgerPlace():
    # Variable "total" is initialized
    total = 0
    # Repetition structure that runs indefinitely
    while True:
        # prints text on the screen
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        # Variable "idFood" receives input, then it is converted to uppercase
        idFood = input("O que deseja? | ").upper()[0]
        # Multiple choice structure that checks the output corresponding to the code read from the user, when found, it is added to the variable "total", in order to give the total value of the purchase
        if (idFood == "H"):
            total += 5.50
        elif (idFood == "C"):
            total += 6.80
        elif (idFood == "M"):
            total += 4.50
        elif (idFood == "A"):
            total += 7.00
        elif (idFood == "Q"):
            total += 4.00
        elif (idFood == "X"):
            return total
        else:
            print("Opção inválida.")
# Creating the main function
def main():
    # The variable "orderVal" receives the call to the "burgerPlace" function
    orderVal = burgerPlace()
    # Prints the value of the "orderVal" variable on the screen, duly treated with two decimal places
    print(f"\nO valor total da compra é de R$ {orderVal:.2f}.\n")
# Identify function main for execute
if __name__ == "__main__":
    main()