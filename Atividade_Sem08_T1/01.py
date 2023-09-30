# 01. Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de nascimento de uma pessoa, calcule e escreva a idade exata em anos

# Creation of the function "yearsOld" for data processing
def yearsOld(da, ma, ya, db, mb, yb):
    # Variable "years" receives the operation to find the age
    years = ya - yb
    # Conditional structure that checks the days and months are in accordance with the exact age, if both conditions are true the number of years will be decreased by 1
    if (da < db) and (ma <= mb):
        years -= 1
    return years

# Creating the main function
def main():
    # Variables "dayact, monthact, yearact" receive entries related to the current date
    dayact = int(input("Digite o dia atual: "))
    monthact = int(input("Me fale o mês atual agora: "))
    yearact = int(input("Por ultimo o ano: "))
    # Variables "dayBirth, monthBirth, yearBirth" receive entries related to date of birth
    dayBirth = int(input("Digite agora o dia em que nasceu: "))
    monthBirth = int(input("O mês: "))
    yearBirth = int(input("E o ano: "))
    # The variable "years" receives the function call "yearsOld", receiving the exact age in years of the user in return
    years = yearsOld(dayact, monthact, yearact, dayBirth, monthBirth, yearBirth)
    # Shows the value of the "years" variable on the screen
    print(f"Certo!! Você tem exatamente {years} anos de idade.")

# Identify function main for execute
if __name__ == "__main__":
    main()