# 05. Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.

# Processing function
def average(n1, n2, n3):
    calc = round((n1 + n2 + n3) / 3, 2)
    # Nested conditionals that respectively check whether the third grade is greater than 8 to the right of the extra point and the adjustment of the average if it exceeds 10 points.
    if (n3 > 8):
        calc += 1
        if (calc >= 10):
            calc = 10
    # Returns the variable "calc"
    return calc

# Main function
def main():
    # Variables "val1, val2, val3" receives inputs and all are converted to float type
    val1 = float(input("Qual a 1ª nota do aluno(a)? "))
    val2 = float(input("Qual a 2ª nota? "))
    val3 = float(input("Por fim, a 3ª nota? "))
    # The variable "result" receive a call to the function "average", giving the necessary parameters and receiving the respective results 
    result = average(val1, val2, val3)
    # Shows the values ​​of the variables "result" on the screen
    print(f"O aluno(a) teve uma média de {result} pontos.")
    
# Identify function main for execute
if __name__ == "__main__":
    main()