# 04.Crie um programa que cadastre informações de 20 pessoas (nome, idade e cpf) e coloque em um dicionário. Após a leitura, remova todas as pessoas menores de 18 anos do dicionário e coloque-as separadas em outro dicionário. Imprima os dois dicionários separando os campos por ; (ponto-e-vírgula). Use o CPF para chave do dicionário.

# Function to register people's information
def registerPeople():
    people = {}  # Dictionary to store all people
    minors = {}  # Dictionary to store people under 18 years old

    for i in range(20):
        name = input().strip()
        age = int(input())
        cpf = input().strip()

        # Stores the information in the dictionary using CPF as the key
        people[cpf] = {'Name': name, 'Age': age, 'CPF': cpf}

        # Checks if the person is under 18 and stores them in the separate dictionary
        if age < 18:
            minors[cpf] = people.pop(cpf)  # Removes from the main dictionary and adds to minors

    return people, minors  # Returns the two dictionaries

# Function to print the dictionaries separating the fields by semicolon
def printDictionaries(people, minors):
    print("========== MAIORES DE 18 ANOS ==========")
    for cpf, person in people.items():
        print(f"{person['Name']};{person['Age']};{cpf}")

    print("========== MENORES DE 18 ANOS ==========")
    for cpf, person in minors.items():
        print(f"{person['Name']};{person['Age']};{cpf}")

# Main function
def main():
    # Registers people's information
    people, minors = registerPeople()

    # Prints the dictionaries separating the fields by semicolon
    printDictionaries(people, minors)

if __name__ == "__main__":
    main()

