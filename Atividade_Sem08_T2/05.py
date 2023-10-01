# 05. Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:
# Média Final = Nota 1 + Nota 2 ∗ 2 + Nota 3 ∗ 3 + Média Exercícios
#                               7
# A atribuição dos conceitos obedece a tabela abaixo.

# Conceito | Média Final
# A        | >= 9.0
# B        | >= 7.5 e < 9.0
# C        | >= 6.0 e < 7.5
# D        | >= 4.0 e < 6.0
# E        | < 4.0

# O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado” se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.

# Creation of the function "idelWeight" for data processing
def finalResult(n01, n02, n03, exercAver):
    # Variable "finalMedia" receives mathematical equation that calculates the final average
    finalMedia = (n01 + (n02 * 2) + (n03 * 3) + exercAver)/7
    # Variable "finalMedia" receives method to round the final average
    finalMedia = round(finalMedia, 2)
    # Conditional structure that checks which description is appropriate for the calculated average value
    if (finalMedia >= 9.0):
        return f"Média final: {finalMedia:.2f}\nNota: A\nSituaçsão: Aprovado"
    elif (7.5 <= finalMedia < 9.0):
        return f"Média final: {finalMedia:.2f}\nNota: B\nSituação: Aprovado"
    elif (6.0 <= finalMedia < 7.5):
        return f"Média final: {finalMedia:.2f}\nNota: C\nSituação: Aprovado"
    elif (4.0 <= finalMedia < 6.0):
        return f"Média final: {finalMedia:.2f}\nNota: D\nSituação: Reprovado"
    elif (finalMedia < 4.0):
        return f"Média final: {finalMedia:.2f}\nNota: E\nSituação: Reprovado"

# Creating the main function
def main():
     # The variable "regist" receives an input, which is converted to the string type
    regist = str(input("Digite a matricula do Aluno(a):\n "))
    # variables "note01, note02, note03" receive inputs and are all converted to float type
    note01 = float(input("Digite a primeira nota: "))
    note02 = float(input("Digite a segunda nota: "))
    note03 =float(input("Digite a terceira nota: "))
    # The variable "exerciseAver" receives an input, which is converted to the float type
    exerciseAver = float(input("Digite a média obtida pelos exercicios: "))
    # variable "result" receives the function call "finalResult", receiving the final average, the concept and the situation
    result = finalResult(note01, note02, note03, exerciseAver)
    # Shows the variables "regist" and "result" on the screen
    print(f"Matricula: {regist}\n{result}")
    
# Identify function main for execute
if __name__ == "__main__":
    main()