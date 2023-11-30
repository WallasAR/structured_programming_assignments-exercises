# 03. Leia um dia e um mês como números inteiros distintos e informe as cidades que fazem aniversário nessa data. Veja o exemplo para o dia 9 e mês 2:
# CIDADES QUE FAZEM ANIVERSÁRIO EM 9 DE FEVEREIRO:
# São Miguel do Passa Quatro(GO)
# Centralina(MG)
# Itaporanga(PB)
# ...

# Function to get the full month name based on its number
def monthInFull(month):
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

# Function to load city data from the 'cidades.csv' file
def LoadCities():
    result = []
    with open('cidades.csv', 'r', encoding='utf-8') as file:
        for line in file:
            uf, ibge, nome, dia, mes, pop = line.split(';')
            result.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    file.close()
    return result

# Function to find cities that have a birthday on a specific day and month
def citiesBirthDayFilter(day, month):
    # Load city data from the 'cidades.csv' file
    cities = LoadCities()
    
    # Initialize an empty list to store cities matching the given day and month
    matchCities = []

    # Iterate through each city in the loaded data
    for city in cities:
        # Check if the city's day and month match the provided day and month
        if ((city[3] == day) and (city[4] == month)):
            # If matched, append the city's name and state abbreviation to the matchCities list
            matchCities.append(f"{city[2]}({city[0]})")
    
    # Return the list of cities that match the given day and month
    return matchCities


# Main function
def main():
    # Get user input
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))

    # Find cities
    result = citiesBirthDayFilter(day, month)
    
    # Get the full month name
    month = monthInFull(month)

    # Display cities' birthdays
    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {day} DE {month}:")
    for city in result:
        print(city)         
        
# Identify function main for execute
if __name__ == "__main__":
    main()