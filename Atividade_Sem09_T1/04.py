# 04. Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.

# Creation of the function "analysis" for data processing
def analysis(v1, v2, v3):
    # Variables "secondDif" and "thirdDif" receive a subtraction and then the "ads()" method transforms the result of this subtraction to the absolute number
    secondDif = abs(v1 - v2)
    thirdDif = abs(v1 - v3)

    # Compound conditional structure that compares and checks which of the previously calculated values ​​is smaller
    if (secondDif < thirdDif):
        return secondDif
    else:
        return thirdDif

# Creating the main function
def main():
    # The variables "var1, var2, var3" receive inputs and are all converted to the integer type
    var1 = int(input("Informe o primeiro valor inteiro: "))
    var2 = int(input("Informe o segundo valor inteiro: "))
    var3 = int(input("Informe o terceiro valor inteiro: "))
    # The variable "result" receives the call to the "analysis" function, receiving the corresponding return
    result = analysis(var1, var2, var3)
    # Prints the value of the variable "result" on the screen
    print(f"O menor valor da diferença em relação ao primeiro valor dado é {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()