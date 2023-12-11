# 03.Um entrevistador precisa saber o ano de nascimento em que 1000 (mil) pessoas nasceram e, no final, deseja saber a quantidade de pessoas que nasceram em cada ano. Crie um dicionário e, a cada valor lido, some 1 (um) na chave correspondente ao ano do dicionário. Mostre quantas pessoas nasceram em cada ano exibindo do mais antigo ao mais recente.

def countBirths():
    birth_years = {}

    for _ in range(1000):
        year = int(input())
        if year in birth_years:
            birth_years[year] += 1
        else:
            birth_years[year] = 1

    for year, quantity in sorted(birth_years.items()):
        print(f"{year}: {quantity}")

def main():
    countBirths()
    
if __name__ == "__main__":
    main()