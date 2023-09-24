# 03. Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido. 
# • Nenhum dígito é ímpar. • Apenas um dígito é ímpar. • Os dois dígitos são ímpares.

# Processing function
def analysis(intNum):
    # Variables to separate digits using mathematical operations
    d = intNum // 10 
    u = intNum % 2 == 1
    # # The variable "count" is responsible for delivering the output corresponding to the number of odd numbers
    count = 0
    # Operations to check whether it is odd or not, if yes it will be increased in the variable "count"
    if u:
        count += 1
    if d % 2 == 1:
        count += 1
    # Conditionals that return the output corresponding to the value of the variable "count"
    if (count == 0):
        return "Nenhum dígito é ímpar."
    elif (count == 1): 
        return "Apenas um dígito é ímpar."
    elif (count == 2):
        return "Os dois dígitos são ímpares."

# Main function
def main():
    # The variable "VarNum" receives an input, which is converted to the integer type
    VarNum = int(input())
    # The variable "result" receives the function call "analysis"
    result = analysis(VarNum)
    # Shows the values ​​of the variables "result" on the screen
    print(f"{result}")

# Identify function main for execute
if __name__ == "__main__":
    main()