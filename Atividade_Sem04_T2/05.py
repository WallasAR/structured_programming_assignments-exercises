# 05. Escreva um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas são 2, 3 e 5. Fórmula para o cálculo da média final é:
# média ponderada = (n1 ∗ 2) + (n2 ∗ 3) + (n3 ∗ 5) / 10

# Processing function
def mpond(n1, n2, n3):
    # Variable "calc" save the result of equation
    calc = ((n1*2) + (n2*3) + (n3*5)) / 10
    return calc

# Main function
def main():
    # Variables "val1, val2, val3" receives inputs and all are converted to float type
    val1 = float(input("Digite a primeira nota do(a) aluno(a): "))
    val2 = float(input("Digite a segunda nota do(a) aluno(a): "))
    val3 = float(input("Digite a terceira nota do(a) aluno(a): "))
    # The "result" variable receives a call to the "mpond" function, giving the necessary parameters and receiving the result immediately afterwards
    result = mpond(val1, val2, val3)
    # Prints the result of the "result" variable on the screen
    print(f"\n\tA média deste(a) aluno(a) é {result}")
    
# Identify function main for execute
if __name__ == "__main__":
    main()