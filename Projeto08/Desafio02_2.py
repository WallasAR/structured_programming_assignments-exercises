# Desafio: Serviço de escolha de nome para animais de estimação 
# Escreva um programa para ajudar um novo dono a dar nome ao seu animal de estimação: 
# Seu programa pode: 
# permitir que o usuário adicione e remova itens da lista; 
# dar nomes diferentes para animais machos e fêmeas, ou para tipos diferentes de animais; 
# perguntar ao usuário quantos nomes eles precisam, caso eles tenham mais de um animal de estimação para dar 

from random import *

def choose_pet_name():
    pet_names = {
        'cachorro': {
            'macho': ["Max", "Buddy", "Rocky", "Charlie"],
            'fêmea': ["Bella", "Lucy", "Daisy", "Luna"],
            'outro': ["Coco", "Oreo", "Snowball", "Peanut"]
        },
        'gato': {
            'macho': ["Simba", "Oliver", "Leo", "Milo"],
            'fêmea': ["Chloe", "Luna", "Cleo", "Molly"],
            'outro': ["Whiskers", "Shadow", "Smokey", "Tiger"]
        }
    }

    print("Serviço de escolha de nome para animais de estimação")

    quantidade = int(input("Quantos animais de estimação você deseja nomear? "))
    for i in range(quantidade):
        tipo_animal = input("Digite o tipo de animal (cachorro/gato): ").lower()

        if tipo_animal in pet_names:
            genero = input("Digite o gênero do animal (macho/fêmea/outro): ").lower()

            if genero in pet_names[tipo_animal]:
                nome_escolhido = choice(pet_names[tipo_animal][genero])
                print(f"Você deve chamar seu {tipo_animal} de estimação de {nome_escolhido}")
                pet_names[tipo_animal][genero].remove(nome_escolhido)
            else:
                print("Não temos nomes para esse gênero de animal no momento.")
        else:
            print("Não temos nomes para esse tipo de animal no momento.")

if __name__ == "__main__":
    choose_pet_name()
