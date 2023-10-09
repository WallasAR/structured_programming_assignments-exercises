# 03. Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida. OBS: Use apenas condicionais e os tipos básicos do Python; 
# Não utilize bibliotecas do Python que tratam datas;
# Considere que em anos bissextos o mês de fevereiro tem 29 dias.

# Subroutine that checks if the year is a leap year
def leapYear(year):
    # Returns a boolean value
    return ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0))

# Creation of the function "validDate" for data processing
def validDate(date):
    # Checks whether the number of digits corresponding to the date are correct, if not the value is invalid
    if (len(date) == 8):
        # Variable "day" receives the first two numbers of the string that corresponds to the day, then is converted to an integer
        day = int(date[:2])
        # Variable "month" receives the third and fourth numbers of the string that corresponds to the month, then is converted to an integer
        month = int(date[2:4])
        # Variable "year" receives the last four numbers of the string that corresponds to the year, then is converted to an integer
        year = int(date[4:])
        # Conditional structure that determines the value of the variable "febuary" that will later be used to prove the leap year
        if (leapYear(year)):
            february = 29
        else:
            february = 28 

        # Nested conditional structure that checks if the date is valid
        if ((1 <= month <= 12) and (1 <= day <= 31)):
            # Use of the variable "febuary". Checks if it is a leap year the 29th is valid.
            if (month == 2):
                return 1 <= day <= february
            else:
                # Checking the rest of the months and days. A small vector is created to separate the months that contain 30 days
                if (month in [4, 6, 9, 11]):
                    return 1 <= day <= 30
                else:
                    return 1 <= day <= 31
        else:
            return False
    else:
        return "Data inválida!"

# Creating the main function
def main():
    # Variable "date" receives an input
    date = str(input("Digite uma data qualquer no formato DDMMAAAA: "))
    # The variable "result" receives the call to the "validDate" function, receiving a boolean value
    result = validDate(date)
    # Prints the value of the variable "result" on the screen
    print(f"A data informada é valida?\n{result}")
# Identify function main for execute
if __name__ == "__main__":
    main()