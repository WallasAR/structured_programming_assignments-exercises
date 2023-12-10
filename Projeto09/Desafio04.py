# Desafio: Proteção de senha 
# Crie um programa de proteção de senha, que pede que o usuário informe seu nome e senha e verifica se os dados estão corretos em um dicionário.

password_dictionary = {
        "programador": "acesso",
        "amigo1": "senha1",
        "amigo2": "senha2"
    }
def main():
    print("Programa super secreto")
    login_attempts = 0

    while login_attempts < 3:
        name = input("Nome: ")
        password = input("Senha: ")

        if name in password_dictionary and password == password_dictionary[name]:
            print(f"BEM-VINDO {name.upper()}")
            break
        else:
            print("Acesso negado. Nome de usuário ou senha incorretos.")
            login_attempts += 1

    if login_attempts == 3:
        print("Número máximo de tentativas excedido. Acesso bloqueado.")

if __name__ == "__main__":
    main()
