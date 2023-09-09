# 04. Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertida de para horas e minutos. Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos. OBS: Mostre o resultado na forma H:M

# Processing function
def time(m):
    # Variable "h" receives the operation that calculates the integer division and then stores the result in itself
    h = m //60
    # Variable "m" receives the operation that calculates the module and then stores the result
    m = m % 60
    return h, m

# Main function
def main():
    # The "min" variable receives input and is converted to int type
    min = int(input("Digite a quantidade de minutos a ser convertida: "))
    # The variables "hours, minutes" receive a call to the function "time", giving the necessary parameter and receiving the respective results according to the return "return h, m"
    hours, minutes = time(min)
    # Prints on the screen the results of the variables "hours" and "minutes" formatted according to what was proposed (H:M)
    print(f"{hours}:{minutes}")

# Identify function main for execute
if __name__ == "__main__":
    main()