# 05.Escreva um programa que lê matrícula, nome e duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é a matrícula do aluno. A entrada de dados deve terminar quando for lida uma string vazia como matrícula. Após o término da leitura dos dados de entrada, use uma função que retorna a média do aluno, dado sua matrícula. Mostre a média dos alunos até o programa ser finalizado com a leitura de uma matrícula vazia.

def average(notes):
    return sum(notes) / len(notes) if notes else 0

def main():
    alunos = {}

    while True:
        regist = input().strip()
        if regist == "":
            break
        
        nome = input().strip()
        note1 = float(input())
        note2 = float(input())
        
        alunos[regist] = {'nome': nome, 'notas': [note1, note2]}

    while True:
        matricula_desejada = input().strip()
        if matricula_desejada == "":
            break
        
        if matricula_desejada in alunos:
            media_aluno = average(alunos[matricula_desejada]['notas'])
            print(f"{alunos[matricula_desejada]['nome']}: {media_aluno:.1f}")
        else:
            print("Matrícula não encontrada!")

if __name__ == "__main__":
    main()
