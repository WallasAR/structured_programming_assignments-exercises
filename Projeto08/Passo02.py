# Etapa 2: Cumprimentos sem fim  

from random import *

def main():
    executa = True

    adjetivos =  [ "maravilhoso", "acima da média", "excelente" ] 

    hobbies = [ "andar de bicicleta", "programar", "fazer chá" ] 

    print("Gerador de Cumprimentos")
    print("-----------------------")

    nome = input("Qual é o seu nome?: ") 

    print(''' 
    Menu 
    c = obter cumprimento 
    q = sair 
    ''') 

    while (executa == True):

        menuChoice = input("\n>_").lower()

        if (menuChoice == "c"):
            print("Aqui está seu cumprimento", nome, ":")

            print(nome, "você é", choice(adjetivos), "em", choice(hobbies))

            print("De nada!")
        elif (menuChoice == "q"):
            executa = False
        else:
            print("Escolha uma opção válida!")

if __name__ == "__main__":
    main()