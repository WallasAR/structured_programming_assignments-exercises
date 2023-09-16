# 05. Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? Vamos ajudá-los a converter temperaturas! Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:
# °F = (°C * (9/5)) + 32

# Processing function
def conversion(c):
    # Variable "fahren" save the result of equation
    fahren = (c * (9 / 5)) + 32
    # returns the rounding of the variable "fahren" according to 2 decimal places
    return round(fahren,2)

# main function
def main():
    # Variable "celsius" receives input and converts to type float
    celsius = float(input("Digite a temperatura em Graus Celsius(ºC): "))
    # The "result" variable receives a call to the "conversion" function, giving the necessary parameters and receiving the result immediately afterwards
    result = conversion(celsius)
    # Prints the result of the "result" variable on the screen
    print(f"A temperatura correspondente em Fahrenheit {result:.2f} ºF.")

# Identify function main for execute
if __name__ == "__main__":
    main()