# 05. Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas casas decimais:
# • Valor para pagamento à vista, com desconto de 9%. • Valor da prestação para pagamento em 5 vezes, sem desconto nem juros. • Valor da prestação para pagamento em 10 vezes, com 17% de juros.

# Processing function
def payday(purchVal):
    # Variable "cashValue" receives the operation that calculates the cash discount
    cashValue = purchVal * 0.91
    # Variable "portion5x" receives the operation that calculates the monthly installment of 5x
    portion5x =  purchVal/5
    # Variable "portion10x" receives the operation that calculates the monthly installment of 10x with interest
    portion10x = (purchVal * 1.17)/10
    # return the results
    return cashValue, portion5x, portion10x

# Main function
def main():
    # The "purchaseVal" variable receives input and is converted to float type
    purchaseVal = float(input("Escreva o valor da compra: "))
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result
    cash, p5x, p10x = payday(purchaseVal)
    # Prints the result of the "result" variable on the screen
    print(f"\nValor à vista(9% de desconto) R${cash:.2f}\nParcelado em 5x(sem juros) R${p5x:.2f}\nParcelado em 10x(com 17% de juros) R${p10x:.2f}")

# Identify function main for execute
if __name__ == "__main__":
    main()