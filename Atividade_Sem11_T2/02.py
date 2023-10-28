# 02. Escreva um programa que, para um número indeterminado de pessoas:

# a. leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag) e não deve ser considerada;
# b. calcule e escreva o número de pessoas;
# c. calcule e escreva a idade média do grupo;
# d. calcule e escreva a menor idade e a maior idade.

# Creation of the function "" for data processing
def analysis():
    # Initialization of the variables that will be used
    numPeop = 0
    sumPeop = 0
    biggerAge = 0
    smallerAge = 200 # Variable has this value to allow exchange in the conditional structure process

    while True:
        # Variable "agePeople" receives input, then converted to integer type
        agePeople = int(input("Informe a idade da pessoa: "))
        # Variable "month" receives the sum of itself plus 1, represents the number of people
        numPeop += 1
        # Variable "sumPeop" receives the sum of itself with the variable "agePeople", this variable will be necessary to calculate the average of all ages
        sumPeop += agePeople
        # Loop stop condition, notice the decrease of 1 in the variable "numPeop", the objective is to remove the count from the value 0
        if (agePeople == 0):
            numPeop -= 1
            break
        # Conditional structures to deduce the oldest and youngest age
        if (agePeople > biggerAge):
            biggerAge = agePeople
        if (agePeople < smallerAge):
            smallerAge = agePeople
    # Variable "average" receives calculation of the average of all ages
    average = sumPeop / numPeop
    # Returns the entire processing result
    return f"Quantidade total de pessoas: {numPeop}\nIdade média do grupo: {average:.2f}\nMenor idade: {smallerAge}\nMaior idade: {biggerAge}"
# Creating the main function
def main(): 
    # The variable "result" receives the call to the "analysis" function
    result = analysis()
    # Show the value ​​of the variable "result" on the screen
    print(f"{result}")
# Identify function main for execute
if __name__ == "__main__":
    main()