# 02. Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas, dezenas e unidades do número lido, observando os termos no plural, a colocação do "e" ou da vírgula entre valores e o ponto “.” no final da frase. Exemplos:
# • 521 = cinco centenas, duas dezenas e uma unidade.
# • 107 = uma centena e sete unidades.
# • 80 = oito dezenas.

# Creation of the function "extensNum" for data processing, This subroutine is called by another subroutine named "showNumQuant" to receive the number written in full
def extensNum(num):
    # Variable "string" is declared as string, it will be responsible for iterating and saving the results and returning them to the main function
    string = ""
    # Multiple choice structure that checks the corresponding number for your name in full
    # zero is not considered, so it receives the "pass" function
    if num == 0:
        pass
    elif num == 1:
        string += "uma"
    elif num == 2:
        string += "duas"
    elif num == 3:
        string += "três"
    elif num == 4:
        string += "quatro"
    elif num == 5:
        string += "cinco"
    elif num == 6:
        string += "seis"
    elif num == 7:
        string += "sete"
    elif num == 8:
        string += "oito"
    elif num == 9:
        string += "nove"
    return string

# Function that does all the processing
def showNumQuant(num):
    # Compound conditional that checks whether the given number is within the proposed limits
    if (0 <= num <= 1000):
        # Creation of the variable "string" responsible for storing all the iteration made
        string = ""
        # Variables that receive mathematical operations in order to separate the number into units, tens and hundreds
        unit = num % 10
        dozen = (num % 100) // 10
        hundred = num // 100

        # Nested conditional structure that separately processes the number corresponding to a hundreds
        if (hundred > 0):
            if (hundred == 1):
                # Here the variable "string" is iterated by calling the subroutine "extensNum" to get the full name of the hundred in singular
                string += f"{extensNum(hundred)} centena"
            else:
                # It happens in the same way as in line 49, but this case is for the plural
                string += f"{extensNum(hundred)} centenas"

            # Nested conditional structure that handles all the treatment of commas, periods and linking verb "and"
            if (dozen > 0) and (unit > 0):
                string += ", "
            else:
                if (dozen > 0) and (unit >= 0):
                    string += " e "
                else:
                    if (dozen >= 0) and (unit > 0):
                        string += " e "
                    else:
                        string += "."
        
        # Nested conditional structure that separately processes the number corresponding to tens
        if (dozen > 0):
            if (dozen == 1):
                # Same way described in line 48
                string += f"{extensNum(dozen)} dezena"
            else:
                # Same way described in line 48/51
                string += f"{extensNum(dozen)} dezenas"
            # Iterations for point treatments and/or linking verb "and"
            if (unit > 0):
                string += " e "
            else:
                string += "."
        # Nested conditional structure that separately processes the number corresponding to units
        if (unit > 0):
            if (unit == 1):
                # Same way described in line 48
                string += f"{extensNum(unit)} unidade."
            else:
                # Same way described in line 48/51
                string += f"{extensNum(unit)} unidades."
        # returns the value of the variable "string"
        return string.strip()
    else:
        return "Número inválido!"

# Creating the main function
def main():
    # Variable "varNum" receives an input and is then converted to the integer type
    varNum = int(input("Digite um valor inteiro entre 0 e 1000: "))
    # The variable "result" receives the call to the "showNumQuant" function
    result = showNumQuant(varNum)
    # Prints the value of the variable "result" on the screen
    print(f"Valor corresponde a: {result}")
# Identify function main for execute
if __name__ == "__main__":
    main()