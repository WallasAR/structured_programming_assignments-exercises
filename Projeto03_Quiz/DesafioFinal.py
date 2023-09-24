# Desafio: Como eu fiz?
# Desafio completo

# Function to check the correctness of "Q1"
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
# Function to check the correctness of "Q2"
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
# Function to check the correctness of "Q3"
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
# Function to check the correctness of "Q4"
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
# Function to check the correctness of "Q5"
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
    # Variable that records the number of correct answers
    point = 0
    print(''' 
    Q1 -  Qual destes dispositivos é usado principalmente para armazenar informações em forma digital?
    a - Tabela periódica
    b - CD (Compact Disc)
    c - Papel impresso
    ''')
    # Variable "resposta" receives an input and then all its characters are changed to lowercase
    resposta = input().lower()
    # The function returns the point, or not, to the "score" variable and then this point is passed to another "point" variable in order to preserve it as the "score" variable is always changed when calling the functions
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
    # Conditional for a more informative output for each situation
    if score == 5:
        print("\tMUITO BEM! Você acertou todas!!")
    else:
        print("\tTente novamente para acertar todas!!")   

if __name__ == "__main__":
    main()