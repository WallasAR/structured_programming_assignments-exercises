# 04. Um sacolão está vendendo frutas com a seguinte tabela de preços:

#         |     Até 5Kg      |    Acima de 5Kg
# Morango |  R$ 2,50 por Kg  |   R$ 2,20 por Kg
# Maça    |  R$ 1,80 por Kg  |   R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Creation of the function "calc" for data processing
def calc(strawb, apple):
    # Variables "valSb, valA" receive a simplified conditional structure that checks the respective price according to the quantity of the fruit
    valSb = 2.50 if (strawb <= 5) else 2.20
    valA = 1.80 if (apple <= 5) else 1.50
    # Variable "valTotal" receives mathematical equation that represents the total price
    valTotal = (valSb * strawb) + (valA * apple)
    # Conditional structure that checks whether the total value or quantity of fruit required is reached for a 10% discount
    if (strawb + apple > 8) or (valSb + valA > 25):
        return round(valTotal * 0.90, 2)
    else: 
        return round(valTotal, 2)

# Creating the main function
def main():
     # The variables "strawberry, apple" receive inputs and are all converted to the float type
    strawberry = float(input("Digite a quantidade (em kg) de morangos: "))
    apple = float(input("Digite a quantidade (em kg) de maçãs: "))
    # The variable "result" receives the call to the "calc" function
    result = calc(strawberry, apple)
    # Prints the value of the variable "result" on the screen
    print(f"Valor a ser pago: R$ {result:.2f}")
# Identify function main for execute
if __name__ == "__main__":
    main()