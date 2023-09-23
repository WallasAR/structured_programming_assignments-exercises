# Desafio: Como eu fiz?
# Desafio completo

# Desafio: Mantendo a pontuação

def Q1(resp, point):
    if resp == "a":
        print("Incorreto!!")
        return point
    elif resp == "b":
        print("Correto!!\t+1 ponto")
        point += 1
        return point
    elif resp == "c":
        print("Incorreto!!")
        return point
    else:
        print("Opção inválida!!")
        return point

def Q2(resp, point):
    if resp == "a":
        print("Correto!!\t+1 ponto")
        point += 1
        return point
    elif resp == "b":
        print("Incorreto!!")
        return point
    elif resp == "c":
        print("Incorreto!!")
        return point
    else:
        print("Opção inválida!!")
        return point

def Q3(resp, point):
    if resp == "a":
        print("Incorreto!!")
        return point
    elif resp == "b":
        print("Incorreto!!")
        return point
    elif resp == "c":
        print("Correto!!\t+1 ponto")
        point += 1
        return point
    else:
        print("Opção inválida!!")
        return point

def Q4(resp, point):
    if resp == "a":
        print("Incorreto!!")
        return point
    elif resp == "b":
        print("Correto!!\t+1 ponto")
        point += 1
        return point
    elif resp == "c":
        print("Incorreto!!")
        return point
    else:
        print("Opção inválida!!")
        return point

def Q5(resp, point):
    if resp == "a":
        print("Incorreto!!")
        return point
    elif resp == "b":
        print("Incorreto!!")
        return point
    elif resp == "c":
        print("Correto!!\t+1 ponto")
        point += 1
        return point
    else:
        print("Opção inválida!!")
        return point

def main():
    point = 0
    print(''' 
    Q1 -  Qual destes dispositivos é usado principalmente para armazenar informações em forma digital?
    a - Tabela periódica
    b - CD (Compact Disc)
    c - Papel impresso
    ''')
    resposta = input().lower()
    score = Q1(resposta, point)

    point = score

    print('''
    Q2 - O que significa a sigla "GPS"?
    a -  Global Positioning System
    b -  General Programming Software
    c -  Grand Prix Simulation
    ''')
    resposta = input().lower()
    score = Q2(resposta, point)

    point = score

    print(''' 
    Q3 -  Qual destas empresas é famosa por seus produtos de software, como o Windows e o Office?
    a -  Apple
    b -   IBM
    c -  Microsoft
    ''')
    resposta = input().lower()
    score = Q3(resposta, point)
    
    point = score

    print(''' 
    Q4 - Qual é o componente principal de um computador onde ocorre o processamento de dados?
    a - Monitor
    b - CPU (Unidade Central de Processamento)
    c - Teclado
    ''')
    resposta = input().lower()
    score = Q4(resposta, point)

    point = score

    print('''
    Q5 - Qual destes não é um tipo de dispositivo de entrada de computador?
    a - Mouse
    b - Microfone
    c - Impressora
     ''')
    resposta = input().lower()
    score = Q5(resposta, point)

    point = score
    
    print(f"O jogo acabou! Sua pontuação:\n\t>> {score} acertos de 5 questões")
    if score == 5:
        print("\tMUITO BEM! Você acertou todas!!")
    else:
        print("\tTente novamente para acertar todas!!")   

if __name__ == "__main__":
    main()