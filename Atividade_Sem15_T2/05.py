# 05.Faça um programa que leia e armazene em um array tridimensional contendo os valores do faturamento anual de uma empresa, especificados por filial e também mês a mês. Veja a estrutura do array seguinte:
# Após a leitura dos dados faça o seguinte:
# a) Calcule o total de cada ano por filial;
# b) Calcule o total de todas as filiais por ano;
# c) Calcule o total do período para todas as filiais;
# d) Mostre todos os dados lidos e calculados
# de acordo com o período que ocorrer

# List of month 
months = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Function to read sales data for multiple branches, months, and years
def readSales():
    # Number of branches
    branches = 3  
    # Number of months
    months = 12  
    # Number of years
    years = 4     
    # Initialize sales data with zeros for each year, branch, and month
    sales = [[[0 for _ in range(months)] for _ in range(branches)] for _ in range(years)]

    # Loop through each year, branch, and month to input sales data
    for year in range(years):
        for branch in range(branches):
            for month in range(months):
                value = int(input())  # Input sales value for a particular month
                sales[year][branch][month] = value  # Store the sales value

    return sales

# Function to calculate the total sales for a specific year and branch
def calculate_total_year_branch(sales, year, branch):
    return sum(sales[year - 2014][branch])

# Function to calculate the total sales for all branches in a specific year
def calculate_total_all_branches_per_year(sales, year):
    return sum(calculate_total_year_branch(sales, year, branch) for branch in range(len(sales[0])))

# Function to calculate the total sales for all branches over the entire period
def ShowResults(sales):
    total_period_all_branches = int()  # Initialize the total sales for all branches over the entire period

    # Loop through each year and branch to display sales data and calculate totals
    for year in range(len(sales)):
        for branch in range(len(sales[0])):
            # Display sales data for each month in the format: year;Branch x;Month;SalesValue
            for month in range(len(sales[0][0])):
                print(f"{year + 2014};Filial {branch + 1};{months[month]};{sales[year][branch][month]}")
            
            # Calculate and display the total sales for a specific year and branch
            total_year_branch = calculate_total_year_branch(sales, year + 2014, branch)
            print(f"TOTAL {year + 2014} FILIAL {branch + 1};{total_year_branch}")

        # Calculate and display the total sales for all branches in a specific year
        total_all_branches_per_year = calculate_total_all_branches_per_year(sales, year + 2014)
        print(f"TOTAL {year + 2014} TODAS FILIAIS;{total_all_branches_per_year}")

        total_period_all_branches += total_all_branches_per_year  # Update the total for the entire period
        
    # Display the total sales for all branches over the entire period
    print(f"TOTAL PERÍODO TODAS FILIAIS;{total_period_all_branches}")

# The main function that orchestrates the execution of the program
def main():
    sales = readSales()  # Read the sales data
    ShowResults(sales)   # Display the results

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()

