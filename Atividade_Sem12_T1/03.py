# 02. Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3% ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a população do país A.

# Creation of the function "population" for data processing
def population(ac, bc):
    # Country A birth rate (2%)
    birthRateA = 2/100
    # Country B birth rate (3%)
    birthRateB = 3/100
    # Initialize the time counter
    time = 0
    # Initializes the auxiliary variable "aux"
    aux = 0
    # Ensures that the population of A is greater than or equal to the population of B
    if (bc > ac):
            # Exchanges values ​​between "ac" and "bc", with "aux" as an auxiliary
            aux = ac
            ac = bc
            bc = aux
    while True:
        # Checks if the population of B is smaller than the population of A
        if (bc < ac):
            # Increment the counter
            time += 1
            # Calculate, respectively, the population growth of A and B
            ac += ac * birthRateA
            bc += bc * birthRateB
        # Checks whether the population of B exceeded or equaled that of A
        if (bc >= ac):
            # Returns the value of the variable "time"
            return time 
# Creating the main function
def main():
    # Variables "aCountry" and "bCountry" receives an inputs and all is converted to the integer type
    aCountry = int(input("Digite a população do país A: "))
    bCountry = int(input("Digite a população do país B: "))
    # The variable "result" receives the call to the "population" function
    result = population(aCountry, bCountry)
    # Shows the result of the variable "result" on the screen
    print(f"Em {result} unidades de tempo, a população B ultrapassará a população A")
# Identify function main for execute
if __name__ == "__main__":
    main()