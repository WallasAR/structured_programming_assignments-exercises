# 04.Suponha que vamos jogar um dado e queremos saber quantas vezes cada face (de 1 a 6) caiu. Faça um programa que leia o resultado de cada jogada do dado e armazena em um dicionário. A face do dado é a chave para o dicionário e a leitura de um valor 0 (zero) na face encerra o jogo. Mostre quantas vezes o dado foi lançado e quantas vezes cada face saiu. A leitura do valor 0 (zero) para a face encerra o jogo e mostra o resultado.

def countFacesData():
    results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    total_rolls = 0

    while True:
        result = int(input())
        if result == 0:
            break
        if result in results:
            results[result] += 1
            total_rolls += 1
        else:
            print("Resultado inválido. Digite um número de 1 a 6.")

    print(f"{total_rolls} {results}")
    

def main():
    countFacesData()

if __name__ == "__main__":
    main()