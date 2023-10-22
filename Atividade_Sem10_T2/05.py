# 05. Escreva um programa que simula o valor (com duas casas decimais) da prestação de uma compra parcelada sem juros de 1x até 24x. O valor da compra é digitado pelo usuário. O valor da prestação sem juros, deve ser calculado como o valor da compra dividido pelo número de prestações de 1 até 24. O programa estará correto se o usuário informar o valor 1000 e o programa produzir o seguinte resultado:
# 1x de R$ 1000.00            13x de R$ 76.92
# 2x de R$ 500.00             14x de R$ 71.43
# 3x de R$ 333.33             15x de R$ 66.67
# 4x de R$ 250.00             16x de R$ 62.50
# 5x de R$ 200.00             17x de R$ 58.82
# 6x de R$ 166.67             18x de R$ 55.56
# 7x de R$ 142.86             19x de R$ 52.63
# 8x de R$ 125.00             20x de R$ 50.00
# 9x de R$ 111.11             21x de R$ 47.62
# 10x de R$ 100.00            22x de R$ 45.45
# 11x de R$ 90.91             23x de R$ 43.48
# 12x de R$ 83.33             24x de R$ 41.67

# Creation of the function "showParcel" for data processing
def showParcel(val):
    # Repeating structure that follows a range between 1 and 24
    for count in range(1, 25):
            # The variable "parcel" receives the division between the variables "val" and "count"
            parcel = val / count
            # Prints the values ​​of the variables "count" and "parcel" on the screen
            print(f"{count}x de R$ {parcel:.2f}")
# Creating the main function
def main():
    # Variable "val" receives an input and is then converted to the float type
    val = float(input())
    # Function call "showParcel"
    showParcel(val)
# Identify function main for execute
if __name__ == "__main__":
    main()