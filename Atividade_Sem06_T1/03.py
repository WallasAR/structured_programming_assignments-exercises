# 03. Escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).

# Processing function
def time(seg):
    # Variable "h" receives the operation(integer division between variable "seg" and a fixed number) to find the hour
    h = seg // 3600
    # Variable "m" receives the operation to find the minutes
    m = (seg % 3600) // 60
    # Finally, the variable "s" receives the operation to find the seconds
    s = (seg % 3600) % 60
    # returns the variables properly treated
    return f"{h}:{m}:{s}"

# Main function
def main():
    # The "seg" variable receives input and is converted to integer type
    seg = int(input("Digite a quantidade de segundos desejada: "))
    # The variable "result" receives the function call "analysis", sending the necessary parameter and receiving the result
    result = time(seg)
    # Prints the result of the "result" variable on the screen
    print(f"{seg} segundos é igual a {result}")

# Identify function main for execute
if __name__ == '__main__':
    main()