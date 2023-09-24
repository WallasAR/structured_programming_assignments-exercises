# 01. Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).

# Processing function
def maritstatus(num, name):
    # Conditional that checks whether the individual is married or single
    if (num == 1):
        # The variable "spouse" receives an input, which is converted to the string type
        spouse = str(input("Qual o nome do Cônjuge?\n")).strip()
        # Returns the sum of the number of characters between the variables "spouse" and "name"
        return len(spouse) + len(name)
    elif (num == 2):
        # Returns the number of characters in the variable "name"
        return len(name)
     
# Main function
def main():
    # The variable "name" receives an input, which is converted to the string type
    name = str(input("Qual o nome do indivíduo?\n ")).strip()
    # The variable "status" receives an input, which is converted to the integer type
    status = int(input("Qual os estado civil? (""1"" -> Casado, ""2"" -> Solteiro)\n"))
    # The variable "namespouse" receives the function call "smaritstatus"
    namespouse = maritstatus(status, name)
    
    # Conditional for outputs
    if maritstatus:
        # Prints a message on the screen
        print(f"A quantidade total de caracteres dos nomes lidos é de {namespouse} letras.")
    else:
        # Prints a message on the screen
        print(f"Quantidade de caracteres do nome lido é de {name} letras. ") 

# Identify function main for execute
if __name__ == "__main__":
    main()