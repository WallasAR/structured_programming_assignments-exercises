# 02.Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ... ).


# List of month names
months = [  
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

# Function to convert Celsius to Kelvin
def celsiusToKelvin(tempCelsius):
    return tempCelsius + 273.15

# Function to convert Fahrenheit to Kelvin
def fahrenheitToKelvin(tempFahrenheit):
    return (tempFahrenheit - 32) * (5/9) + 273.15

# Function to input temperature and its unit
def inputTemperature():
    temperature = float(input())  # Input temperature value
    unit = input().strip().upper()  # Input temperature unit (C, F, or K) and convert to uppercase
    
    return temperature, unit

# Function to convert temperature to Kelvin based on unit
def convertToKelvin(temperature, unit):
    if unit == "C":
        return celsiusToKelvin(temperature)  # Convert Celsius to Kelvin
    elif unit == "F":
        return fahrenheitToKelvin(temperature)  # Convert Fahrenheit to Kelvin
    elif unit == "K":
        return temperature  # Temperature is already in Kelvin

# Function to calculate annual average temperature
def calculateAnnualAverage(temperatures):
    total = sum(temperatures)  # Calculate total sum of temperatures
    return round(total / len(temperatures), 2)  # Calculate and return the rounded average

# Function to identify temperatures above the annual average
def aboveAverageTemp(temperatures, average):
    above_avg = []  # List to store months with temperatures above average

    for i, temp in enumerate(temperatures):
        if temp > average:
            above_avg.append((months[i], temp))  # Append month and temperature above average

    return above_avg  # Return list of months with temperatures above average

# Main function
def main():
    monthly_temperatures = []  # List to store temperatures for each month
    

    for month in months:
        temp, unit = inputTemperature()  # Input temperature and unit for each month
        temp_kelvin = convertToKelvin(temp, unit)  # Convert temperature to Kelvin
        monthly_temperatures.append(temp_kelvin)  # Append Kelvin temperature to the list

    annual_average = calculateAnnualAverage(monthly_temperatures)  # Calculate annual average temperature
    above_avg_temperatures = aboveAverageTemp(monthly_temperatures, annual_average)  # Identify temperatures above average

    # Print annual average temperature
    print(f"TEMPERATURA MÉDIA ANUAL\n{annual_average}K")
    print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    
    # Print months with temperatures above the annual average
    for month, temp in above_avg_temperatures:
        print(f"{month}: {round(temp, 2)}K")  # Print month and temperature above average

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()

