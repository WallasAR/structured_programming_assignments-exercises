# 03. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos (excluindo o zero). Dica: use repetição com teste no final

# Creation of the function "biggSmall" for data processing
def biggSmall():
    # Variable "num" receives input, then converted to integer type
    num = int(input("Informe um numero inteiro qualquer (digite 0 para o resultado): "))
    # Variables "biggerNum" and "smallerNum" both receive the value of the variable "num"
    biggerNum = num
    smallerNum = num
    # Repetition structure that runs indefinitely
    while True:
        # Variable "num" receives input, then converted to integer type
        num = int(input("Informe um numero inteiro qualquer (digite 0 para o resultado): "))
        # Conditional structure that checks whether the number entered is greater/less than the variables started previously, if the input is 0 the loop will terminate
        if (num == 0):
            break
        if (num > biggerNum):
            biggerNum = num
        if (num < smallerNum):
            smallerNum = num
    # Returns the value of the variables "biggerNum" and "smallerNum"
    return biggerNum, smallerNum    
# Creating the main function
def main():
    # Variables "maxNum" and "minNum" receive the function call "biggSmall"
    maxNum, minNum = biggSmall()
    # Shows the values ​​of the variables "maxNum" and "minNum" on the screen
    print(f"Maior número: {maxNum}\nMenor número: {minNum}")
# Identify function main for execute
if __name__ == "__main__":
    main()