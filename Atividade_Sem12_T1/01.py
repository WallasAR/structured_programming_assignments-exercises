# 01. A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de sair n sua frente. A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto. Faça um programa que leia quantos metros a tartaruga sai à frente da lebre e calcule quantos minutos levará até que a lebre alcance a tartaruga. Por exemplo, se a tartaruga sair 500 metros à frente a lebre alcança em 56 minutos.

# Creation of the function "race" for data processing
def race(turtle):
    # Initialization of variables "min" and "hare"
    min = 0
    hare = 0
    # Repetition structure that runs indefinitely
    while True:
        if (hare < turtle):
            # Increment the counter in the variable "min"
            min += 1
            # Move the hare 10 units
            hare += 10
            # Move the turtle 1 unit
            turtle += 1
        # Checks whether the hare overtook or caught up with the tortoise
        if (hare >= turtle):
            # Returns the value of the counter variable "min"
            return min
# Creating the main function
def main():
    # Variable "turtle" receives an input and is then converted to the integer type
    turtle = int(input("Qual a vantagem de metros a frente a tartaruga tem? | "))
    # The variable "min" receives the call to the "race" function
    min = race(turtle)
    # Shows the result of the variable "min" on the screen
    print(f"a lebre alcançará a tartarua em {min} minutos.")
# Identify function main for execute
if __name__ == "__main__":
    main()