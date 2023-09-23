# 02. Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou o valor booleano False (falso) caso contrário.

# Processing function
def boolNum(var):
    # Returns a Boolean value originating from the comparison
    return var % 2 == 1

# Main function
def main():
    # The variable "var" receives an input, which is converted to the integer type
    var = int(input("Digite um número inteiro qualquer: "))
    # The variable "result" receives the function call "boolNum"
    result = boolNum(var)
    # Shows the values ​​of the variables "result" on the screen
    print(f"O número informado é ímpar (representado por True) ou par (representado por False)?\n{result}")

# Identify function main for execute
if __name__ == "__main__":
    main()