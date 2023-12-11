# 02.Crie um dicionário e armazene nele os dados de livros: título, isbn, autor e preço. A chave do dicionários será um código numérico e sequencial, gerado automaticamente, iniciando pelo número 101 (cento e um). A leitura de uma descrição vazia para o título finaliza a leitura. Imprima todos os dados usando o padrão “Nome do Campo: valor”. Por exemplo:
# Código: 101
# Título: Programação Java para a Web - 1a Edição
# ISBN: 978-85-7522-238-6
# Autor: Décio H. Luckow
# Preço: 99.00
# ...
# Código: 114
# Título: Novelas, Espelhos e um Pouco de Choro
# ISBN: 85-7480-052-X
# Autor: Thelma Guedes
# Preço: 52.00

# Function to input book details and store in a dictionary
def inputBooks():
    books = {} # Initialize an empty dictionary to store book details
    code = 101  # Initialize the starting code number

    while True:
        title = str(input("\nTítulo do exemplar: ").strip())

        # Check for an empty title to end input
        if (title == ""):
            break

        isbn = str(input("ISBN: "))
        author = str(input("Autor: "))
        price = float(input("Preço: "))
        
        # Store book details in the dictionary with the code as the key
        books[code] = {
            "Título": title,
            "ISBN": isbn,
            "Autor": author,
            "Preço": price
        }

        code += 1 # Increment the code for the next book

    return books # Return the dictionary containing book details

# Function to print book details from the dictionary
def output(books):
    for code, book in books.items():
        print(f"Código: {code}")

        for key, value in book.items():
            # Check if the value is the price to format it with two decimal places
            if (key == "Preço"):
                print(f"{key}: {value:.2f}")
            else:
                print(f"{key}: {value}")
        print()

# Main function 
def main():
    
    print("Insira as informações referentes ao livro")
    library = inputBooks() # Get book details from user input

    print("Lista de todos os exemplares da livraria")
    output(library) # Print book details

# Identify function main for execute
if __name__ == "__main__":
    main()
