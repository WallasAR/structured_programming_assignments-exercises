# Desafio: Adicione mais cumprimentos 
# Tente pensar em mais cumprimentos e adicione-os ao seu programa! Lembre-se de que você precisa adicionar uma vírgula (,) entre os itens em suas listas. 

from random import *

def main():
    print("Gerador de Cumprimentos")
    print("-----------------------")

    adjetivos = ["maravilhoso", "acima da média", "excelente", "incrível", "fantástico", "brilhante"] 

    hobbies = ["andar de bicicleta", "programar", "fazer chá", "cozinhar", "tocar instrumentos musicais", "pintar"] 

    nome = input("Qual é o seu nome?: ") 

    print("Aqui está o seu cumprimento, " + nome + ":")

    print(nome + ", você é " + choice(adjetivos) + " em " + choice(hobbies))

    print("De nada!")

if __name__ == "__main__":
    main()
