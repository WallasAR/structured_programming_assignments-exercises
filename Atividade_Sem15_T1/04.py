# 04. Leia uma população e informe as cidades com população maior que o valor lido. Veja o exemplo:
# Veja o exemplo para a leitura de 50000 para a população:

# CIDADES COM MAIS DE 50000 HABITANTES:
# IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639
# IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398
# IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323
# ...


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
    # Return the list containing city data
    return result

# Function to filter cities based on population size
def citiesPopulationFilter(pop):
    # Load city data
    cities = LoadCities()
    # Initialize an empty list to store cities with populations greater than 'pop'
    CitiesPop = []

    # Iterate through each city in the loaded data
    for city in cities:
        # Check if the city's population is greater than the provided population value
        if (city[5] > pop):
            # If the condition is met, append the city's information to the CitiesPop list
            CitiesPop.append(f"IBGE: {city[1]} - {city[2]}({city[0]}) - POPULAÇÃO: {city[5]}")
    
    # Return the list of cities with populations greater than the provided value
    return CitiesPop

# Main function to execute the program
def main():
    # Input the population value from the user
    population = int(input())

    # Retrieve cities with populations greater than the provided value
    result = citiesPopulationFilter(population)

    # Display the list of cities with populations greater than the provided value
    print(f"CIDADES COM MAIS DE {population} HABITANTES:")
    for city in result:
        print(city)         
        
# Execute the 'main' function when the script is run
if __name__ == "__main__":
    main()
