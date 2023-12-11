# 03.Um entrevistador precisa saber o ano de nascimento em que 1000 (mil) pessoas nasceram e, no final, deseja saber a quantidade de pessoas que nasceram em cada ano. Crie um dicionário e, a cada valor lido, some 1 (um) na chave correspondente ao ano do dicionário. Mostre quantas pessoas nasceram em cada ano exibindo do mais antigo ao mais recente.

# Function to count occurrences of birth years
def countBirths():
    birth_years = {}  # Initialize an empty dictionary to store birth years and their counts

    # Iterate 1000 times to input birth years
    for _ in range(1000):
        year = int(input(f"Digite o ano de nascimento da {_ + 1}ª pessoa: "))  # Input a birth year
        if year in birth_years:
            birth_years[year] += 1  # Increment the count if the year already exists in the dictionary
        else:
            birth_years[year] = 1  # Add the year to the dictionary with a count of 1

    # Iterate through the sorted dictionary items and print each year with its count
    for year, quantity in sorted(birth_years.items()):
        print(f"{year}: {quantity}")

# Main function to execute the countBirths function
def main():
    countBirths()  # Call the countBirths function

# Execute the main function if this script is executed directly
if __name__ == "__main__":
    main()
