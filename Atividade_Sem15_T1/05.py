# 05. Leia um mês e uma população. Mostre as cidades com população maior que o valor lido fazem aniversário no mês informado. Veja o exemplo para o mês com valor 4 e 50000 para a população:

# CIDADES COM MAIS DE 50000 HABITANTES E ANIVERSÁRIO EM ABRIL:
# Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril.
# Itacoatiara(AM) tem 84676 habitantes e faz aniversário em 25 de abril.
# Araci(BA) tem 51912 habitantes e faz aniversário em 7 de abril.
# Fortaleza(CE) tem 2431415 habitantes e faz aniversário em 13 de abril.
# ...

# Function to get the full month name based on its number
def monthInFull(month):
    # Mapping each month number to its corresponding full name
    if (month == 1):
        return "JANEIRO"
    elif (month == 2):
        return "FEVEREIRO"
    elif (month == 3):
        return "MARÇO"
    elif (month == 4):
        return "ABRIL"
    elif (month == 5):
        return "MAIO"
    elif (month == 6):
        return "JUNHO"
    elif (month == 7):
        return "JULHO"
    elif (month == 8):
        return "AGOSTO"
    elif (month == 9):
        return "SETEMBRO"
    elif (month == 10):
        return "OUTUBRO"
    elif (month == 11):
        return "NOVEMBRO"
    elif (month == 12):
        return "DEZEMBRO"

# Function to load city data from a file named 'cidades.csv'
def LoadCities():
    result = []
    # Open the file 'cidades.csv' for reading
    with open('cidades.csv', 'r', encoding='utf-8') as file:
        # Iterate through each line in the file
        for line in file:
            # Split each line using ';' as the delimiter and extract city data
            uf, ibge, nome, dia, mes, pop = line.split(';')
            # Append extracted city data as a tuple to the result list
            result.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    # Close the file
    file.close()
    return result

# Function to filter cities based on month and population size
def citiesMonthAndPopFilter(month, pop):
    # Load city data
    cities = LoadCities()
    # Initialize an empty list to store cities matching the criteria
    CitiesPopAndMonth = []

    # Iterate through each city in the loaded data
    for city in cities:
        # Check if the city's month and population satisfy the given conditions
        if ((city[4] == month) and (city[5] > pop)):
            # If conditions are met, append city information to the CitiesPop list
            CitiesPopAndMonth.append(f"{city[2]}({city[0]}) tem {city[5]} habitantes e faz aniversário em {city[3]} de {monthInFull(month).lower()}.")
    
    # Return the list of cities matching the criteria
    return CitiesPopAndMonth

# Main function to execute the program
def main():
    # Input month and population values from the user
    month = int(input())
    population = int(input())

    # Retrieve cities matching the specified month and population criteria
    result = citiesMonthAndPopFilter(month, population)

    # Convert month number to its full name
    month = monthInFull(month)

    # Display the list of cities meeting the specified criteria
    print(f"CIDADES COM MAIS DE {population} HABITANTES E ANIVERSÁRIO EM {month}:")
    for city in result:
        print(city)         
        
# Execute the 'main' function when the script is run
if __name__ == "__main__":
    main()
