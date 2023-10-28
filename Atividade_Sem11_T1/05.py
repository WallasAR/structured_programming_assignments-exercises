#  05. Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. Pedro também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. Considerando que a situação se refere ao mês de outubro do ano de 2016, faça um programa leia o valor do salário e o valor da dívida e calcula, simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com o cartão de crédito será superior ao seu próprio salário. Represente os meses como inteiros de 1 a 12.
# Dica: Controle essas quatro variáveis:
# “dívida” que aumenta todo mês;
# “salário” que aumenta apenas se o número do mês for 3 (março);
# “mês” que é incrementado sempre, mas que retorna a 1 quando passar de 12;
# “ano” que só é incrementado quando o mês retornar a 1.

# Por exemplo: Considerando que o salário inicial é de R$ 2.000,00 e o valor da dívida é R$ 100,00 o valor
# da dívida irá superar o salário em setembro de 2018 (9/2018)
 
# Creation of the function "subseqDebit" for data processing
def subseqDebit(salar, deb):
    # Variables "month" and "year" are initialized, respectively, with values ​​10 and 2016
    month = 10
    year = 2016
    # Repetition structure that executes as long as the condition is met
    
    while (deb <= salar):

        # Conditional structure that checks if the month is equal to 3 (March), so that Pedro can earn his salary increase
        if (month == 3):
            salar = salar * 1.05 # 1.05 -> Represents the salary increase - 5% - of Pedro
        deb = deb * 1.15 # 1.15 -> Represents the interest rate - 15% - of Pedro's debt
        # Variable "month" receives the sum of itself plus 1, represents the passing of months
        month += 1
        # conditional structure that checks if the variable "month" is greater than 12, if so, 1 is added to the variable that represents the years "year" and the variable "month" returns to 1 (January)
        if (month > 12):
            month = 1
            year += 1
    # Returns the values ​​of the variables "month, year"
    return month, year
# Creating the main function
def main():
    # Variables "salary" and "debt" receive inputs, then are converted to float type
    salary = float(input("Informe quanto o funcionário Pedro ganha: R$ "))
    debt = float(input("Quanto o Pedro está devendo no momento? | R$ "))
    # Variables "month" and "year" receive the function call "subseqDebit"
    month, year = subseqDebit(salary, debt)
    # Shows the values ​​of the variables "month" and "year" on the screen
    print(f"Contando que essa dívida teve início em 10/2016, Em {month}/{year} a dívida de Pedro ultrapassará seu próprio salário! Pague suas contas Pedro!!")
# Identify function main for execute
if __name__ == "__main__":
    main()