# 02. Utilizando a definição de valor da temperatura com tupla da questão anterior, desenvolva uma função que soma duas temperaturas que podem estar em Celsius ou em Fahrenheit. Se as duas temperaturas estiverem na mesma escala, a resposta deve estar na mesma escala. Se as temperaturas estiverem em escalas diferentes, a resposta deve ser dada na escala da segunda temperatura. Considere até 4 (quatro) casas decimais.

def inputTemp():
    # Reads the desired temperature and its scale (ºF or ºC)
    temp = float(input())
    scale = str(input()).upper()[0]  # Converts input to uppercase and takes the first character

    # Returns a tuple containing temperature and scale
    return temp, scale  

# Converts Fahrenheit to Celsius using the conversion formula
def FahrenToCelcius(temperature):
    return ((temperature - 32) * (5/9))

# Converts Celsius to Fahrenheit using the conversion formula
def CelciusToFahren(temperature):
    return ((temperature * (9/5)) + 32)

def highestTemp(t1, t2):
    # Extracts temperatures and scales from the first and the second tuple 
    temp1, scale1 = t1  
    temp2, scale2 = t2
    
    # Performs conversion if the temperatures are in different scales   
    if (scale1 != scale2):
        if (scale1 == "F"):
            temp1 = FahrenToCelcius(temp1)
            scale1 = "C"
        else:
            temp1 = CelciusToFahren(temp1)
            scale1 = "F"

    # Returns the sum and the scale of the second temperature
    return round(temp1 + temp2, 4), scale2

# Main function
def main():
    # Gets input for two temperatures
    temp1 = inputTemp()
    temp2 = inputTemp()

    # Finds the highest temperature among the two
    highTemp = highestTemp(temp1, temp2)

    # Prints the highest temperature and its scale
    print(f"{highTemp}")
    
# Identify function main for execute
if __name__ == "__main__":
    main()