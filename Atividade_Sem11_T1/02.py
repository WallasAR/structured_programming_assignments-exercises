# 02. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos (excluindo o zero). Dica: use repetição com teste no final.

# Creation of the function "average" for data processing
def average():
    # Initialization of variable "sumNum" with value 0
    sumNum = 0
    # Initialization of variable "sampleSpace" with value 0
    sampleSpace = 0

    # Repeating structure that runs indefinitely
    while True:
        # Variable "num" receives input, then converted to integer type
        num = int(input())
        # Conditional structure that checks the given input, if it is 0 the loop will terminate, if it is a number greater than 0 operations will be performed
        if (num == 0):
            break
        elif (num > 0):
            # Variable "sumNum" receives the sum between "sumNum" and "num"
            sumNum += num
            # Variable "sampleSpace" receives the sum(sampleSpace + 1)
            sampleSpace += 1
        # Variable "averag" receives the division between "sumNum" and "sampleSpace"
        averag = sumNum / sampleSpace
    return averag
def main():
    # The variable "result" receives the call to the "average" function    
    result = average()
    # Prints the value of the "result" variable on the screen, duly treated with two decimal places
    print(f"{result:.2f}")
if __name__ == "__main__":
    main()