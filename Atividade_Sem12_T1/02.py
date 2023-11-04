# 02. Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.

# Creation of the function "buyaCar" for data processing
def buyaCar(cPrice):
        # Initialize the amount saved
        savings = 10000
        # Economy growth rate (0.7% per month)
        income = 0.7/100
        # Car price increase rate (0.4% per month)
        Carperc = 0.4/100
        # Initialize the month counter
        months = 0
        # Repetition structure that runs indefinitely
        while True:
            # Checks if the price of the car is greater than the savings
            if (cPrice > savings):
                # Increment the month counter
                months += 1
                # Calculate, respectively, the growth of economies (line 19) and the increase in car prices (line 20)
                savings += savings * income
                cPrice += cPrice * Carperc
            # Checks whether the amount accumulated in savings is enough to buy the car
            if (savings >= cPrice):
                # Returns the number of months it took to save
                return months
# Creating the main function
def main():
    # Variable "carPrice" receives an input and is then converted to the float type
    carPrice = float(input("Qual o valor inicial do carro? "))
    # The variable "month" receives the call to the "buyaCar" function
    month = buyaCar(carPrice)
    # Shows the result of the variable "month" on the screen
    print(f"Em {month} meses, você tera dinheiro suficiente acumulado na poupança para comprar este carro.")
# Identify function main for execute
if __name__ == "__main__":
    main()