# 02. Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.

# Creation of the function "choiceRecent" for data processing
def choiceRecent(d1, m1, y1, d2, m2, y2):
    # Conditional structures that check whether a certain variable is greater/less/equal than another, if so assignments are made
    if (y1 > y2):
        Day = d1
        Month = m1
        Year = y1
    elif (m1 <= m2) and (d1 < d2):
        Day = d2
        Month = m2
        Year = y2
    elif(y1 == y2):
        Day = d1
        Month = m1
        Year = y1
    # Returns the variables assigned by conditional structures
    return f"{Day}/{Month}/{Year}"

# Creating the main function
def main():
    # Variables "day1, month1, year1, day2, month2, year2" receive entries related to any date
    day1 = int(input("Digite um dia qualqer: "))
    month1 = int(input("Um mês qualquer: "))
    year1 = int(input("E um ano qualquer: "))
    day2 = int(input("Otimo! Digite outro dia qualquer: "))
    month2 = int(input("Mês: "))
    year2 = int(input("Ano: "))
    # The variable "result" receives the call to the "choiceRecent" function, receiving in return the most recent date
    result = choiceRecent(day1, month1, year1, day2, month2, year2)
    # Shows the value of the "result" variable on the screen
    print(f"Das duas datas lidas, a mais recente é {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()