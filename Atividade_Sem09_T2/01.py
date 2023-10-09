# 01. Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira, 3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.

# Creation of the function "dayWeek" for data processing
def dayWeek(num):
    # Multiple choice structure that compares the value of the "num" variable with the pre-determined values ​​for each day of the week
    if (num == 1):
        return "domingo"
    elif (num == 2):
        return "segunda-feira"
    elif (num == 3):
        return "terça-feira"
    elif (num == 4):
        return "quarta-feira"
    elif (num == 5):
        return "quinta-feira"
    elif (num == 6):
        return "sexta-feira"
    elif (num == 7):
        return "sábado"
    else:
        return "valor inválido"

# Creating the main function
def main():
    # Variable "num" receives an input and is then converted to the integer type
    num = int(input("Digite um número inteiro entre 1 e 7: "))
    # The variable "result" receives the call to the "dayWeek" function, returning the day of the week corresponding to the given value
    result = dayWeek(num)
    # Prints the value of the variable "result" on the screen
    print(f"O dia correspondente é {result}")
# Identify function main for execute
if __name__ == "__main__":
    main()