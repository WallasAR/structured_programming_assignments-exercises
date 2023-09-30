# O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:
#  IMC     Classificação
# < 18,5  Abaixo do peso
# < 25    Peso normal
# < 30    Sobrepeso
# < 35    Obeso leve
# < 40    Obeso moderado
# >= 40   Obeso mórbido

# Creation of the function "IMC" for data processing
def IMC(m, h):
    # variable "calcIMC" receive the mathematical equation to calculate the IMC, once calculated it is treated to two decimal places
    calcIMC = round(m / (h**2), 2)
    # Conditional structure that checks which description is appropriate for the calculated IMC value
    if (calcIMC < 18.5):
        return f"{calcIMC}\nDescrição: Abaixo do peso"
    elif (18.5 <= calcIMC < 25):
        return f"{calcIMC}\nDescrição: Peso normal"
    elif (25 <= calcIMC < 30):
        return f"{calcIMC}\nDescrição: Sobrepeso"
    elif (30 <= calcIMC < 35):
        return f"{calcIMC}\nDescrição: Obeso leve"
    elif (35 <= calcIMC < 40):
        return f"{calcIMC}\nDescrição: Obeso moderado"
    elif (calcIMC >= 40):
        return f"{calcIMC}\nDescrição: Obeso mórbido"

# Creating the main function
def main():
    # The variable "weight" receives an input, which is converted to the float type
    weight = float(input("Insira seu peso: "))
    # The variable "height" receives an input, which is converted to the float type
    height = float(input("Digite também sua altura: "))
    # variable "result" receives function call "IMC", receiving the IMC value and its appropriate description
    result = IMC(weight, height)
    # Shows the value of the "result" variable on the screen
    print(f"O IMC calculado foi de {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()