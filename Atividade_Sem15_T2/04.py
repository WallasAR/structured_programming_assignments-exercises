# 04.A tabela abaixo demonstra a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em mil unidades.
# Faça um programa que:
# a) leia os dados da tabela pelo teclado;
# b) leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
# c) determine e exiba o ano de maior volume geral de vendas.
# d) determine e exiba a média anual de vendas de cada fabricante durante o período.


# This function prompts the user for sales data for different manufacturers for each year from 2013 to 2018.
def inputData():
    manufacturers = ["Fiat", "Ford", "GM", "Wolkswagen"]
    data = {}

    # For each manufacturer, it prompts for sales in each year and stores the data in a dictionary.
    for manufacturer in manufacturers:
        sales = [int(input()) for year in range(2013, 2019)]
        data[manufacturer] = sales

    return data

# This function identifies the manufacturer that sold the most in a specific year based on the provided data.
def bestSellingManufac(data, year):
    # Gets sales for each manufacturer for a specific year.
    sales_year = {manufacturer: data[manufacturer][year - 2013] for manufacturer in data}
    
    # Determines the manufacturer that sold the most in the specified year.
    best_selling_manufac = max(sales_year, key=sales_year.get)
    sold_amount = sales_year[best_selling_manufac]

    return best_selling_manufac, sold_amount

# This function identifies the year with the highest sales volume based on the provided data.
def year_with_highest_sales_volume(data):
    # Calculates the total sales for each year from 2013 to 2018.
    annual_total = {year: sum(data[manufacturer][year - 2013] for manufacturer in data) for year in range(2013, 2019)}
    
    # Determines the year with the highest sales volume.
    year_highest_volume = max(annual_total, key=annual_total.get)
    highest_volume_year = annual_total[year_highest_volume]

    return year_highest_volume, highest_volume_year

# This function calculates the annual sales average for each manufacturer based on the provided data.
def annual_sales_average(data):
    # Calculates the sales average for each manufacturer.
    averages = {manufacturer: sum(data[manufacturer]) / len(data[manufacturer]) for manufacturer in data}

    return averages

# Main function
def main():
    # Gets sales data for different manufacturers for each year.
    data = inputData()

    # Prompts the user for a specific year.
    chosen_year = int(input())
    
    # Determines the manufacturer that sold the most in the specified year.
    best_selling_manufac, sold_amount = bestSellingManufac(data, chosen_year)
    print(f"A fabricante que mais vendeu em {chosen_year} foi a {best_selling_manufac} com {sold_amount} mil unidades.")

    # Identifies the year with the highest overall sales volume.
    year_highest_volume, highest_volume_year = year_with_highest_sales_volume(data)
    print(f"O ano de maior volume geral de vendas foi {year_highest_volume} com {round(highest_volume_year, 2)} mil unidades.")

    # Calculates the annual sales average for each manufacturer.
    average = annual_sales_average(data)
    print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
    for manufacturer, avg in average.items():
        print(f"A {manufacturer} vendeu em média {round(avg, 2)} unidades por ano.")

# Runs the main function if this script is executed directly
if __name__ == "__main__":
    main()
