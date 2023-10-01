# 04. Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para ‘homens’ e 2 para ‘mulheres’. Considerando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
# • para homens: (72.7 * altura) – 58
# • para mulheres: (62.1 * altura) – 44.7

# Creation of the function "idelWeight" for data processing
def idealWeight(h, s):
    # Conditional structure that checks the gender for its respective calculation
    if (s == 1): 
        # Variable "forMan" receives mathematical operation that calculates the ideal weight for men
        forMan = (72.7 * h) - 58
        return forMan
    elif (s == 2):
        # Variable "forWoman" receives mathematical operation that calculates the ideal weight for women
        forWoman = (62.1 * h) - 44.7
        return forWoman

# Creating the main function
def main():
    # The variable "height" receives an input, which is converted to the float type
    height = float(input("Digite sua altura: "))
    # The variable "sex" receives an input, which is converted to the integer type
    sex = int(input("Digite seu sexo(""1"" para masculino, ""2"" para feminino): "))
    # Variable "processResult" receives function call "idealWeight", receiving one of the two variables "forMan" or "forWoman"
    processResult = idealWeight(height, sex)
    # Shows the value of the "result" variable on the screen, restricted to two decimal places
    print(f"O peso ideal para sua altura é {processResult:.2f} Kg")

# Identify function main for execute
if __name__ == "__main__":
    main()