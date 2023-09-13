# 04. Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela: • o maior número lido; • o menor número lido; • a média aritmética dos números lidos.

# Processing function
def process(num1, num2, num3, num4, num5):
    # Variable “maxi” receives the method that takes the largest number among the 5 available
    maxi = max(num1, num2, num3, num4, num5)
    # Variable “mini” receives the method that takes the smallest number among the 5 available
    mini = min(num1, num2, num3, num4, num5)
    # Variable "average" receives the operation to calculate the average
    average = (num1 + num2 + num3 + num4 + num5)/5
    # returns the variables properly treated
    return maxi, mini, average

# Main function
def main():
    # Variables "val1, val2, val3, val4, val5" receives inputs and all are converted to int type
    val1 = int(input("Digite o primeiro número inteiro: ")); val2 = int(input("O segundo: ")); val3 = int(input("O terceiro: ")) 
    val4 = int(input("O quarto: ")); val5 = int(input("Por fim, o quinto: "))
    # The variable "result" receives the function call "analysis", sending the necessary parameters and receiving the result
    maxi, mini, average = process(val1, val2, val3, val4, val5)
    # Prints the result of the "result" variable on the screen
    print(f"\nO maior numero lido: {maxi}\nO menor número lido: {mini}\nA média aritmética dos números: {average}")

# Identify function main for execute
if __name__ == "__main__":
    main()