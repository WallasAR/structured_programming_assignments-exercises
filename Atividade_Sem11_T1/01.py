# 01. Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre em quantos anos o valor acumulado será o dobro do valor inicial.

# R$100,00 rendendo 8% ao ano irá dobrar em 10 anos.
# Início    R$ 100.00
# 1 ano     R$ 108.00
# 2 anos    R$ 116.64
# 3 anos    R$ 125.97
# 4 anos    R$ 136.05
# 5 anos    R$ 146.93
# 6 anos    R$ 158.69
# 7 anos    R$ 171.38
# 8 anos    R$ 185.09
# 9 anos    R$ 199.90
# 10 anos   R$ 215.89

# Creation of the function "bank" for data processing
def bank(initdep, tax):
    # Variable initialization "years"
    years = 0
    # Variable "totalVal" receives value from variable "initdep" passed by parameter
    totalVal = initdep
    # "penTax" variable receives mathematical operation to convert the given rate to decimal
    percTax = tax/100

    # Repetition structure that repeats addition commands on the variable "years" and operation on the variable "totalVal"
    while (totalVal < initdep * 2):
        years += 1
        totalVal += totalVal * percTax
    return years
# Creating the main function
def main():
    # Variable "initDeposit" receives an input and is then converted to the float type
    initDeposit = float(input("Digite o depósito inicial: R$ "))
    # Variable "tax" receives an input and is then converted to the float type
    tax = float(input("Qual a taxa de juros a.a da poupança? |> "))
    # The variable "result" receives the call to the "bank" function
    result = bank(initDeposit, tax)
    # Prints the value of the variable "result" on the screen
    print(f"O capital inicial será dobrado em {result} anos")
# Identify function main for execute
if __name__ == "__main__":
    main()