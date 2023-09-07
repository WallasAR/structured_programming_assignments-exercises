# 01. Escreva um programa que leia dois valores e mostre na tela, nessa ordem:
# a. A soma dos números; b. A concatenação das strings; c. A multiplicação dos números;
# d. A multiplicação como strings; e. A divisão dos números; f. A divisão inteira dos números;
# g. A exponenciação; h. O módulo (resto).

# OBS.: Olá professor! tenho o costume de deixar minha documentação em inglês, espero que não tenha nenhum problema. Motivo: legibilidade para o maior número de pessoas na plataforma do GitHub.

# functions for processing
#a
def sumNum(n1, n2):
    # returns the addition of numbers
    return n1 + n2
#b
def concatStr(n1, n2):
    # change variables from type float to string
    n1 = str(n1)
    # the type of variable "n2" is first changed to integer in order to remove the decimal, then it is again changed to type string allowing the proposed concatenation
    n2 = int(n2)
    n2 = str(n2)
    # returns string concatenation
    return n1 + n2
#c
def multNum(n1, n2):
    # returns multiplication of numbers
    return n1 * n2
#d
def multStr(n1, n2):
    # change variables from type float to string and integer respectively.
    n1 = str(n1)
    n2 = int(n2)
    # returns multiplication as string
    return n1 * n2
#e
def divisNum(n1, n2):
    # returns the division of numbers
    return n1 / n2
#f
def divisInt(n1, n2):
    # returns integer division of numbers
    return n1 // n2
#g
def expon(n1, n2):
    # returns the exponentiation.
    return n1**n2
#h
def mod(n1,n2):
    # returns the module
    return n1 % n2

# function main
def main():
    # input
    var1 = float(input())
    var2 = float(input())

    #output
    #result = name_func(param) -> variable to receive the result of the functions 
    # a
    result = sumNum(var1, var2)
    print(result)
    # b
    result = concatStr(var1, var2)
    print(result)
    # c
    result = multNum(var1, var2)
    print(result)
    # d
    result = multStr(var1, var2)
    print(result)
    # e
    result = divisNum(var1, var2)
    print(result)
    # f
    result = divisInt(var1, var2)
    print(result)
    # g
    result = expon(var1, var2)
    print(result)
    # h
    result = mod(var1, var2)
    print(result)

if __name__ == '__main__':
    main()