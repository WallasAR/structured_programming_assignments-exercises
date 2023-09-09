# 03. Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit (baseado na fórmula abaixo): Fahrenheit = (Celsius x (9 / 5)) + 32

# Processing
def conversion(c):
    # Variable "fahren" save the result of equation
    fahren = (c * (9 / 5)) + 32
    return fahren

# main function
def main():
    # Variable "celsius" receives input and converts to type float
    celsius = float(input("Digite a temperatura em Graus Celsius(ºC): "))
    # The "result" variable receives a call to the "conversion" function, giving the necessary parameters and receiving the result immediately afterwards
    result = conversion(celsius)
    # Prints the result of the "result" variable on the screen
    print(f"A temperatura correspondente em Fahrenheit {result} ºF.")

# Identify function main for execute
if __name__ == "__main__":
    main()