# 03. Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total! Leia o preço de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.

# Processing function
def buy(a, b):
    # Variable "priceApple" receives the product between variable "a" and an integer
    priceApple = a * 3
    # Variable "priceBanana" receives the product between variable "b" and an integer
    priceBanana = b * 2
    # returns the sum of variables "priceApple" and "priceBanana" with value rounded to 2 decimal places
    return round(priceApple + priceBanana, 2)

def main():
    # The "apple" variable receives input and is converted to float type
    apple = float(input("Olá mago! Qual o valor da maçã?\nR$ "))
    # The "banana" variable receives input and is converted to float type
    banana = float(input("E o valor da banana?\nR$ "))
    # The variable "result" receives the function call "buy", sending the necessary parameters and receiving the result
    result = buy(apple, banana)
    # Prints the result of the "result" variable on the screen
    print(f"Fica R$ {result:.2f} Sr. Mago, me pague!")

# Identify function main for execute
if __name__ == "__main__":
    main()