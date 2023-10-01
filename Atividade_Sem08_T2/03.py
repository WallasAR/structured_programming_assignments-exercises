# 03. Escreva um programa que leia um número inteiro positivo e escreva na tela: 
# • FIZZ se o número é divisível por três;
# • BUZZ se o número é divisível por cinco;
# • FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
# • O próprio número caso não seja divisível por três ou por cinco.
# OBS: para cada número lido apenas uma resposta deve ser impressa.

# Creation of the function "divisible" for data processing
def divisible(num):
    # Sequence of simple conditional structures that check whether the result of the equation is true (in this case, whether it is divisible by 3 and/or 5), if so, an assignment is made
    if (num % 3 == 0):
        response = "FIZZ"
    if (num % 5 == 0):
        response = "BUZZ"
    if (num % 3 == 0) and (num % 5 == 0):
        response = "FIZZBUZZ"
    if (not num % 3 == 0) and (not num % 5 == 0):
        return num
    # Returns the value of the variable "response"
    return response

# Creating the main function
def main():
    # The variable "varInt" receives an input, which is converted to the integer type
    varInt = int(input("Escreva um número inteiro e positivo qualquer: "))
    # Variable "result" receives function call "divisible", returning the value of the variable "response"
    result = divisible(varInt)
    # Print text on the screen
    print('''
          ######### Nota ########### 
    • "FIZZ" se o número é divisível por três;
    • "BUZZ" se o número é divisível por cinco;
    • "FIZZBUZZ" se o número é divisível por três e por cinco ao mesmo tempo.
    • O próprio número caso não seja divisível por três ou por cinco.''')
    # Shows the value of the "result" variable on the screen
    print(f"\n Resultado: {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()