# 01. Escreva um programa que gera a letra da canção muito popular entre os programadores:
# 99 bugs no software, pegue um deles e conserte...
# 100 bugs no software, pegue um deles e conserte...
# 101 bugs no software, pegue um deles e conserte...
# ...
# Faça o programa de forma a gerar a letra da música com o número de bugs no software variando de 99 a
# 250.

# Creation of the function "cantion" for data processing
def cantion():
    # Repetition structure that follows a range between 99 and 250, showing this range on the screen
    for num in range(99, 251):
        # Data output
        print(f"{num} bugs no software, pegue um deles e conserte...")
# Creating the main function
def main():
    # Function call "cantion"
    cantion()
# Identify function main for execute
if __name__ == "__main__":
    main()