# 01. Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro 1 para identificar masculino e 2 para identificar feminino.

# Processing function
def conditional(gender):
    # Conditional structure that compares the value given by the variable "gender" with other existing ones
    if (gender == 1):
        return "Ilmo Sr."
    elif (gender == 2):
        return "Ilma Sra."

# Main function
def main():
    # The variable "name" receives an input, which is converted to the string type
    name = str(input("Me diga seu nome: "))
    # The variable "gender" receives an input, which is converted to the integer type
    gender = int(input("Agora me diga seu sexo (Masculino -> 1, Feminino -> 2): "))
     # The variable "result" receives the function call "conditional", sending the necessary parameter and receiving the result
    result = conditional(gender)
    # Shows the values ​​of the variables "result" and "name" on the screen
    print(f"{result} {name}")

# Identify function main for execute
if __name__ == "__main__":
    main()