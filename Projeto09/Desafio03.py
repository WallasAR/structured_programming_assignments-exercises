# Desafio: Planetas distantes 


planet_distances = {
    "Mercúrio": "91,700,000 km da Terra",
    "Vênus": "41,400,000 km da Terra",
    "Terra": "0 km da Terra",
    "Marte": "78,340,000 km da Terra",
    "Júpiter": "628,730,000 km da Terra",
    "Saturno": "1,275,000,000 km da Terra",
    "Urano": "2,720,000,000 km da Terra",
    "Netuno": "4,350,000,000 km da Terra",
    "Plutão": "7,370,000,000 km da Terra" 
}

def main():
    while True:
        planet = input("Digite um planeta: ").capitalize()

        if planet in planet_distances:
            print(f"{planet} está a {planet_distances[planet]}")
        else:
            print("Planeta não encontrado. Por favor, insira um nome de planeta válido.")

        continuar = input("Deseja consultar outro planeta? (S/N): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
