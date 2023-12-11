# 03.Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. Leia os dados de todos os contatos do usuário (nome, cidade, estado, telefone) de forma que a agenda fique completa e por fim imprima todos os contatos. Crie um código numérico sequencial para usar como chave do dicionário.

# Function to input contact details and store in a dictionary
def inputContacts(size):
    agenda = {}  # Initialize an empty dictionary to store contacts
    code = 1  # Initialize the starting code number

    # Loop to input contact details until the agenda reaches the given size
    for _ in range(size):
        name = input("Nome: ").strip()
        city = input("Cidade: ").strip()
        state = input("Estado: ").strip()
        phone = input("Telefone: ").strip()

        # Store contact details in the dictionary with the code as the key
        agenda[code] = {
            'Nome': name,
            'Cidade': city,
            'Estado': state,
            'Telefone': phone
        }

        code += 1  # Increment the code for the next contact
    
    return agenda  # Return the dictionary containing contact details

# Function to print all contacts in the specified format
def printContacts(agenda):
    print("-------------- Agenda ---------------------")
    for code, contact in agenda.items():
        # Extracting contact details
        name = contact["Nome"].ljust(25)
        city = contact["Cidade"]
        state = contact["Estado"]
        phone = contact["Telefone"].rjust(40 - len(city) - len(state) - 2)
        
        # Formatting and printing the contacts
        print(f"{name}{city}({state}){phone}")

# Main function
def main():
    size = int(input("Digite o tamanho da agenda: "))
    
    contact_agenda = inputContacts(size)  # Get contact details from user input

    printContacts(contact_agenda)  # Print all contacts in the specified format

if __name__ == "__main__":
    main()

