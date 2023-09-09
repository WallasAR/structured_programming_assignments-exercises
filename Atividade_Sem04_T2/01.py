# 01. Escreva um programa que leia dois valores e mostre na tela, nessa ordem:
# a. A soma dos números; b. A concatenação das strings; c. A multiplicação dos números;
# d. A multiplicação como strings; e. A divisão dos números; f. A divisão inteira dos números;
# g. A exponenciação; h. O módulo (resto).

# OBS.: Olá professor! tenho o costume de deixar minha documentação em inglês, espero que não tenha nenhum problema. Motivo: legibilidade para o maior número de pessoas na plataforma do GitHub.

# Functions for processing
#a
def sumNum(n1, n2):
    # Returns the addition of numbers
    return n1 + n2
#b
def concatStr(n1, n2):
    # change variables from type float to string
    n1 = str(n1)
    # The type of variable "n2" is first changed to integer in order to remove the decimal, then it is again changed to type string allowing the proposed concatenation
    n2 = int(n2)
    n2 = str(n2)
    # Returns string concatenation
    return n1 + n2
#c
def multNum(n1, n2):
    # Returns multiplication of numbers
    return n1 * n2
#d
def multStr(n1, n2):
    # Change variables from type float to string and integer respectively
    n1 = str(n1)
    n2 = int(n2)
    # Returns multiplication as string
    return n1 * n2
#e
def divisNum(n1, n2):
    # Returns the division of numbers
    return n1 / n2
#f
def divisInt(n1, n2):
    # Returns integer division of numbers
    return n1 // n2
#g
def expon(n1, n2):
    # Returns the exponentiation
    return n1**n2
#h
def mod(n1,n2):
    # Returns the module
    return n1 % n2

# Function main
def main():
     # Variables "var1, var2" receives inputs and all are converted to float type
    var1 = float(input("Digite o primeiro valor: "))
    var2 = float(input("Digite o segundo valor: "))

    # Output
    # Result = name_func(param) -> variable to receive the result of the functions
    # a
    result = sumNum(var1, var2)
    print(f"\nSoma dos números -> {var1} + {var2} = {result}\n")
    # b
    result = concatStr(var1, var2)
    print(f"Concatenação das Strings -> {var1} com {var2} = {result}\n")
    # c
    result = multNum(var1, var2)
    print(f"Multiplicação dos números -> {var1} x {var2} = {result}\n")
    # d
    result = multStr(var1, var2)
    print(f"Multiplicação como Strings -> {var1} x {var2} = {result}\n")
    # e
    result = divisNum(var1, var2)
    print(f"Divisão dos números -> {var1} / {var2} = {result}\n")
    # f
    result = divisInt(var1, var2)
    print(f"Divisão inteira dos números -> {var1} // {var2} = {result}\n")
    # g
    result = expon(var1, var2)
    print(f"A exponenciação -> {var1} ^ {var2} = {result}\n")
    # h
    result = mod(var1, var2)
    print(f"O módulo -> {var1} % {var2} = {result}\n")

# Identify function main for execute
if __name__ == '__main__':
    main()