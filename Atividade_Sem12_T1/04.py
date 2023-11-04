# 03. O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8 dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989 e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).

# Creation of the function "luckyNum" for data processing
def luckyNum(dBirth):
    # Initialize the sum of digits
    sumNums = 0
    # Extract and add the date digits
    while (dBirth > 0):
        digit = dBirth % 10
        sumNums += digit
        dBirth //= 10
    # Returns the sum of digits
    return sumNums
# Creating the main function
def main():
    # Variable "dateBirth" receives an input and is then converted to the integer type
    dateBirth = int(input("Digite sua data de nascimento (formato ddmmaaaa): "))
    # The variable "num" receives the call to the "luckyNum" function
    num = luckyNum(dateBirth)
    # Shows the result of the variable "" on the screen
    print(f"Seu número da sorte é {num}!")
# Identify function main for execute
if __name__ == "__main__":
    main()