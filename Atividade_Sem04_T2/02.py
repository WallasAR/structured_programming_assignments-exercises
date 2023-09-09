# 02. Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. Considerar sempre os anos com 365 dias e os meses com 30 dias.

# Processing
def onlyDays(y, m, d):
    # variable "calc" save the result of equation
    calc = (y*365) + (m*30) + d
    return calc

# Main function 
def main():
    # Variables "year, month, days" receives inputs and all are converted to int type
    year = int(input("Digite o ano em que nasceu: "))
    month = int(input("Digite o mês: "))
    days = int(input("Por fim, o dia: "))
    # The "result" variable receives a call to the "onlyDays" function, giving the necessary parameters and receiving the result immediately afterwards
    result = onlyDays(year, month, days)
    # Prints the result of the "result" variable on the screen
    print(f"A sua idade expressa em dias é de {result}")

# Identify function main for execute
if __name__ == '__main__':
    main()