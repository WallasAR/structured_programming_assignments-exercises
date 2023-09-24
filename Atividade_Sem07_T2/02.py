# 02. Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.

# Processing function
def analysis(intNum):
    # Conditional that restricts the number of numbers for processing
    if 100 <= intNum <= 999:
        # Variables to separate digits using mathematical operations
        c = intNum // 100
        d = (intNum % 100) // 10
        u = intNum % 10
        # The variable "count" is responsible for delivering the output corresponding to the number of even numbers
        count = 0
        # Operations to check whether it is even or not, if yes it will be increased in the variable "count"
        if c % 2 == 0:
            count += 1
        if d % 2 == 0:
            count += 1
        if u % 2 == 0:
            count += 1
        # Conditionals that return the output corresponding to the value of the variable "count"
        if (count == 0):
            return "0 dígitos pares"
        elif (count == 1):
            return "1 dígito par"
        elif (count == 2):
            return "2 dígitos pares"
        elif (count == 3):
            return "3 dígitos pares"
    else:
        return "0"

# Main function
def main():
    # The variable "status" receives an input, which is converted to the integer type
    varNum = int(input("Digite um numero inteiro entre 100 e 999: "))
    # The variable "result" receives the function call "analysis"
    result = analysis(varNum)
    # Shows the values ​​of the variables "result" on the screen
    print(f"{result}")

# Identify function main for execute
if __name__ == "__main__":
    main()