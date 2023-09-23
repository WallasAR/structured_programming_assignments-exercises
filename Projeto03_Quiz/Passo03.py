# Passo 3: Multiplas escolhas

def choice(resp):
    if resp == "a":
        print("Não - texto é um tipo de dado :( ")
    elif resp == "b":
        print("Correto!! :) ")
    elif resp == "c":
        print("Não seja bobinho! :( ")
    else:
        print("Você não escolheu a, b ou c :( ")

def main():

    print(''' 
    Q1 - No Python, como se chama uma 'caixa' usada para armazenar dados?
    a - texto 
    b - variavel
    c - uma caixa de sapatos
    ''')
    resposta = input().lower()

    choice(resposta)

if __name__ == "__main__":
    main()