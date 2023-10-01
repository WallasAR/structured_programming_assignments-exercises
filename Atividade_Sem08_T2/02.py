# 02. Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e 100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20.

# Creation of the function "addiction" for data processing
def addiction(num):
    # Conditional that checks if the number is in the correct restrictions
    if (0 <= num < 100000):
        # variable "aux" receives the value of the variable "num"
        aux = num
        # Variable "unid" receives an operation to calculate the unit of the number
        unit = aux % 10
        # Variable "aux" receives integer division by 10, in order to remove the unit calculated in the previous line
        aux //= 10
        # The variable "dozens" receives an operation to calculate the ten of the number
        dozens = aux % 10
        # The variable "aux" receives integer division by 10, to remove the ten calculated in the previous line
        aux //= 10
        # The variable "hundred" receives an operation to calculate the hundred of the number
        hundred = aux % 10
        # The variable "aux" receives integer division by 10, to remove the hundred calculated in the previous line
        aux //= 10
        # The variable "thousands" receives an operation to calculate the thousand of the number
        thousands = aux % 10
        # The variable "aux" receives integer division by 10, to remove the thousands calculated in the previous line
        aux //= 10
        # Returns the sum of the variables "unit, dozens, hundred, thousands, aux(corresponding as a hundred thousand)"
        return unit + dozens + hundred + thousands + aux
    else:
        return -1
    
# Creating the main function
def main():
    # The variable "var" receives an input, which is converted to the integer type
    var = int(input("Digite um numero inteiro entre 0 e 100 mil: "))
    # Variable "processResult" receives function call "addiction", receiving the sum of the digits
    processResult = addiction(var)
    # Shows the value of the "processResult" variable on the screen
    print(f"A soma dos digitos desse número é igual a {processResult}") 

# Identify function main for execute
if __name__ == "__main__":
    main()