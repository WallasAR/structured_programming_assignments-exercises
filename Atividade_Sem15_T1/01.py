# 01. Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais alta. Caso as temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. Faça a leitura de duas temperaturas, na forma temperatura e escala (t, e) separadamente, e mostre qual é a maior. Considere até 4 (quatro) casas decimais).

# Use upper() e colchetes [] para garantir a leitura correta da escala com apenas um caractere, por exemplo:
#                   escala = input('Escala : ').upper()[0]

# As fórmulas, a seguir, mostram como realizar a conversão entre as escalas solicitadas:
#                 °F = (°C * (9/5)) + 32 | °C = (°F - 32) * (5/9)

def inputTemp():
    # Reads the desired temperature and its scale (ºF or ºC)
    temp = float(input("Digite a temperatura desejada: "))
    scale = str(input("Informe a escala dessa temperatura (ºF ou ºC): ")).upper()[0]  # Converts input to uppercase and takes the first character

    # Returns a tuple containing temperature and scale
    return temp, scale  

# Converts Fahrenheit to Celsius using the conversion formula
def FahrenToCelcius(temperature):
    return ((temperature - 32) * (5/9))

def highestTemp(t1, t2):
    # Extracts temperatures and scales from the first and the second tuple 
    temp1, scale1 = t1  
    temp2, scale2 = t2
    
    if ((scale1 == "C") and (scale2 == "F")):
        # Converts the second temperature from Fahrenheit to Celsius if scales are different
        temp2 = FahrenToCelcius(temp2)
    elif ((scale1 == "F") and (scale2 == "C")):
        # Converts the first temperature from Fahrenheit to Celsius if scales are different
        temp1 = FahrenToCelcius(temp1)
    
    # Returns the first temperature tuple if it's higher
    if (temp1 > temp2):
        return t1  
    else:
        # Returns the second temperature tuple if it's higher
        return t2  

# Main function
def main():
    # Gets input for two temperatures
    temp1 = inputTemp()
    temp2 = inputTemp()

    # Finds the highest temperature among the two
    highTemp = highestTemp(temp1, temp2)

    # Prints the highest temperature and its scale
    print(f"\nA temperatura mais alta é: {highTemp[0]} º{highTemp[1]}")
# Identify function main for execute
if __name__ == "__main__":
    main()
