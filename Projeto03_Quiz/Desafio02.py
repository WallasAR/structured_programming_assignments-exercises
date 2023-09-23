# Desafio: Quiz de múltipla escolha

def Q1(resp):
    if resp == "a":
        print("Incorreto!!")
    elif resp == "b":
        print("Correto!!")
    elif resp == "c":
        print("Incorreto!!")
    else:
        print("Opção inválida!!")

def Q2(resp):
    if resp == "a":
        print("Correto!!")
    elif resp == "b":
        print("Incorreto!!")
    elif resp == "c":
        print("Incorreto!!")
    else:
        print("Opção inválida!!")

def Q3(resp):
    if resp == "a":
        print("Incorreto!!")
    elif resp == "b":
        print("Incorreto!!")
    elif resp == "c":
        print("Correto!!")
    else:
        print("Opção inválida!!")

def Q4(resp):
    if resp == "a":
        print("Incorreto!!")
    elif resp == "b":
        print("Correto!!")
    elif resp == "c":
        print("Incorreto!!")
    else:
        print("Opção inválida!!")

def Q5(resp):
    if resp == "a":
        print("Incorreto!!")
    elif resp == "b":
        print("Incorreto!!")
    elif resp == "c":
        print("Correto!!")
    else:
        print("Opção inválida!!")

def main():

    print(''' 
    Q1 -  Qual destes dispositivos é usado principalmente para armazenar informações em forma digital?
    a - Tabela periódica
    b - CD (Compact Disc)
    c - Papel impresso
    ''')
    resposta = input().lower()
    Q1(resposta)    

    print('''
    Q2 - O que significa a sigla "GPS"?
    a -  Global Positioning System
    b -  General Programming Software
    c -  Grand Prix Simulation
    ''')
    resposta = input().lower()
    Q2(resposta)

    print(''' 
    Q3 -  Qual destas empresas é famosa por seus produtos de software, como o Windows e o Office?
    a -  Apple
    b -   IBM
    c -  Microsoft
    ''')
    resposta = input().lower()
    Q3(resposta)

    print(''' 
    Q4 - Qual é o componente principal de um computador onde ocorre o processamento de dados?
    a - Monitor
    b - CPU (Unidade Central de Processamento)
    c - Teclado
    ''')
    resposta = input().lower()
    Q4(resposta)

    print('''
    Q5 - Qual destes não é um tipo de dispositivo de entrada de computador?
    a - Mouse
    b - Microfone
    c - Impressora
     ''')
    resposta = input().lower()
    Q5(resposta)

if __name__ == "__main__":
    main()