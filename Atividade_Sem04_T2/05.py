# 05. Escreva um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas são 2, 3 e 5. Fórmula para o cálculo da média final é:
# média ponderada = (n1 ∗ 2) + (n2 ∗ 3) + (n3 ∗ 5) / 10

# Processing function
def mpond(n1, n2, n3):
    # variable "calc" save the result of equation
    calc = ((n1*2) + (n2*3) + (n3*5)) / 10
    return calc

# main function
def main():
    # variables "val1, val2, val3" receives inputs and all are converted to float type
    val1 = float(input())
    val2 = float(input())
    val3 = float(input())
    # variable "result" receives the result of the function "mpond"
    result = mpond(val1, val2, val3)
    # output
    print(result)
    
if __name__ == "__main__":
    main()