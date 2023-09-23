# 03. Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.

# Processing function
def signal(color):
    # The variable "color" receives the method capable of making a string lowercase
    color = color.lower()
    # Conditional choices for each situation
    if (color == "v"):
        return "Siga"
    elif (color == "a"):
        return "Atenção"
    elif (color == "e"):
        return "Pare"
    else:
        return "Insira um valor válido!!"

# Main function  
def main():
    # The variable "sigColor" receives an input, which is converted to the string type
    sigColor = str(input("Qual a cor que o sinal de trânsito está exibindo(""V"" para verde, ""A"" para amarelo e ""E"" vermelho)?\n "))
    # The variable "result" receives the function call "signal"
    result = signal(sigColor)
    # Shows the values ​​of the variables "result" on the screen
    print(f"{result}")

# Identify function main for execute
if __name__ == "__main__":
    main()