# 05. O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6% dos animais dos animais vivos no começo do ano morreram e o número de animais nascidos ao longo do ano que sobreviveram foi de 1% da população inicial. Escreva um programa que leia a população de aves no início do ano 1600 e imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução quanto a população total cai para menos de 10% da população original.

# Creation of the function "analysis" for data processing
def analysis(pop):
    # Initialize the year
    year = 1600
    # Initializes variable "totalpop" with the value of variable "pop"
    totalpop = pop
    # Repetition structure that executes while the population is above 10% of the initial population
    while (totalpop >= 0.1 * pop):
        # Calculates the number of deaths (6% -> 0.06)
        deaths = 0.06 * totalpop
        # Calculates the number of births (1% -> 0.01)
        births = 0.01 * totalpop
        # Update total population
        totalpop = totalpop + births - deaths
        # Prints the values ​​of the processed and properly treated variables on the screen
        print(f"Ano: {year:.0f}, natalidade: {births:.0f}, mortalidade: {deaths:.0f}, total da população por ano: {totalpop:.0f}")
        # Increment the year      
        year += 1
# Creating the main function
def main():
    # Variable "population" receives an input and is then converted to the integer type
    population = int(input("Digite a população de aves no início do ano 1600: "))
    # Call of the "analysis" function
    analysis(population)
# Identify function main for execute
if __name__ == "__main__":
    main()