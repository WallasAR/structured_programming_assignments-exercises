# 03. Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit (baseado na fórmula abaixo): Fahrenheit = (Celsius x (9 / 5)) + 32

# Processing
def conversion(c):
    # variable "fahren" save the result of equation
    fahren = (c * (9 / 5)) + 32
    return fahren

# main function
def main():
    # variable "celcius" receives input and converts to type float
    celsius = float(input())
    # variable "result" receives the result of the function "conversion"
    result = conversion(celsius)
    # output
    print(result)

if __name__ == "__main__":
    main()