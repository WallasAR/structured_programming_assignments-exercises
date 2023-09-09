# 03. Escreva um programa que leia um preço e um valor percentual. Informe o preço acrescido do percentual e o preço com o desconto percentual. Por exemplo, se for lido um preço de 100.00 e um valor percentual de 5.00 o programa deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00. OBS: Mostre sempre duas casas decimais.

# Processing function
def calculate(p, pV):
     # Variable "percIncrease" receives the operation that calculates the percentage increase and then stores the result in itself
    percIncrease = (p * (pV/100)) + p
     # Variable "percDiscount" receives the operation that calculates the percentage discount and then stores the result
    percDiscount = p * ((100 - pV)/100)
    return percIncrease, percDiscount

# Main function
def main():
    # Variables "price, percVal" receives inputs and all are converted to float type
    price = float(input("Informe o preço do produto/serviço: "))
    percVal = float(input("Informe o percentual de desconto: "))
    # The variables "percIncrease and percDiscount" receive a call to the function "calculate", giving the necessary parameters and receiving the respective results according to the return "return percIncrease, percDiscount"
    percIncrease, percDiscount = calculate(price, percVal)
    # Prints on the screen the results of the variables "percIncrease" and "percDiscount" duly treated with two decimal places
    print(f"{percIncrease:.2f}\n{percDiscount:.2f}")
    
# Identify function main for execute
if __name__ == "__main__":
    main()